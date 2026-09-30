"""MSF_Respect_V 원클릭 빌드 — SCMDraft 컴파일도 EUD Editor(e3s) 빌드도 필요 없다.

    build.bat 더블클릭                         (= python tools\\build.py)
    python tools\\build.py --tepc-only          1단계(tepc)만 돌린다
    python tools\\build.py --refresh-data       build/ 를 EUD Editor 가 마지막으로 만든 빌드 데이터로 다시 채운다

  1. tepc     main.lua -> 트리거. 입력은 이 폴더의 원본 맵 "Respect V_BGM.scx"
              (지형·유닛·로케이션만 든 chk 하나짜리. 트리거는 tepc 가 통째로 새로 쓴다).
              TRIGP*.chk 는 C:\\euddraft0.9.2.0\\Ctemp 로 가고 euddraft 의 STRCtrig 어셈블러가 넣는다.
  2. euddraft build/eudplibData/EUDEditor.eds 의 입출력 경로만 이번 빌드로 바꿔 돌린다.
              build/ 는 EUD Editor 3 가 Respect_V_DLC.e3s 로 만든 빌드 데이터(DataEditor.py, ExtraDataEditor.py,
              RequireData, custom_txt.tbl, eds)를 복사해 둔 것이라 빌드할 때 e3s 나 EUD Editor 가 필요 없다.
              음원(C:\\euddraft0.9.2.0\\Respect_V_BGM, 저작권 때문에 저장소 밖)은 eds 의 [Respect_V_Plugin] 이 넣고,
              끝나면 전부 들어갔는지 최종 맵을 열어 바이트까지 확인한다.
  3. CPLP     보호판 *_out.scx 를 만든다 = 실제로 플레이할 맵.

  지형·유닛을 고칠 때: SCMDraft 로 "Respect V_BGM.scx" 를 고쳐 저장만 한다 (SCMDraft 에서 트리거 컴파일은 필요 없다).
  EUD Editor 데이터(유닛 스탯·버튼·요구조건·tbl)를 고칠 때만: EUD Editor 로 한 번 빌드한 뒤 --refresh-data.
  구조는 MSF_Memory_2/tools/build.py 와 같고, 음원 검사는 MSF_UE_RE/tools/build_scrdb.py 에서 가져왔다.
"""
import argparse
import os
import re
import shutil
import struct
import subprocess
import sys
import time

sys.dont_write_bytecode = True                     # tools\__pycache__ 를 저장소에 남기지 않는다
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import mpq  # noqa: E402  (StormLib ctypes 포장, MSF_UE_RE/tools/mpq.py 사본)

PROJ = os.path.dirname(HERE)                       # ...\MSF_Respect_V
DOCS = os.path.dirname(PROJ)                       # main.lua 의 Curdir = MapSource 와 MSF_Respect_V 의 부모
BUILD = os.path.join(PROJ, "build")
EUDDIR = r"C:\euddraft0.9.2.0"
EUDDRAFT = os.path.join(EUDDIR, "euddraft.exe")
CPLP = os.path.join(EUDDIR, "CustomPlibLockProtector.exe")
CPLP_PLUGIN = os.path.join(EUDDIR, "plugins", "CPLP.py")
BGM_PLUGIN = os.path.join(EUDDIR, "plugins", "Respect_V_Plugin.py")    # eds 의 [Respect_V_Plugin]
BGM_DIR = os.path.join(EUDDIR, "Respect_V_BGM")                        # Respect_V_BGMInput.py 가 여기서 넣는다
SOUND_EXT = (".ogg", ".wav")                                           # Respect_V_BGMInput.py 와 같은 규칙(대소문자 그대로)
SRCMAP = os.path.join(PROJ, "Respect V_BGM.scx")   # SCMDraft 로 저장하는 원본 (chk 하나, 음원 없음)
# EUD Editor 가 만들던 출력 이름을 그대로 쓴다 (e3s 의 eds 와 같다).
FINAL = r"C:\Program Files (x86)\StarCraft\Maps\마린키우기_RESPECT_V_Test.scx"
FINAL_OUT = FINAL[:-4] + "_out.scx"                 # CPLP 가 새로 쓰는 보호판 = 실제로 플레이할 맵
TEPC = os.path.join(DOCS, "theSeed", "tools", "tepc_20260905.exe")
STAT = os.path.join(DOCS, "theSeed", "stat_txt.tbl")
# EUD Editor 3.0.12.8.1 이 Respect_V_DLC.e3s 로 빌드할 때 쓰는 임시 폴더 (--refresh-data 의 원본).
EUD_EDITOR_DATA = r"C:\Users\USER\Desktop\맵제작 자료\EUD.Editor.3.0.12.8.1\Data\temp\BuildData_Respect_V_DLC"
# 이 맵의 TE 메인(main.eps)은 SCA 를 쓰지 않는다. EUD Editor 가 늘 복사해 두는 SCA 라이브러리는 뺀다.
SCA_LIBS = {"SCArchive", "SCATool", "SCAFastLoader", "SCAScript", "SCAScriptReturn",
            "SCALuaWrapper", "SCAWrapper", "SCAFlexible"}
SKIP_DIRS = {"__pycache__", "__epspy__", "backup"}


def lua_str(s):
    return s.replace("\\", "\\\\")


def decode(b):
    for enc in ("utf-8", "cp949"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode("utf-8", "replace")


def bgm_files():
    """Respect_V_BGMInput.py 가 넣을 파일들 (같은 규칙: 폴더 바로 아래의 .ogg/.wav)."""
    if not os.path.isdir(BGM_DIR):
        return []
    return sorted(f for f in os.listdir(BGM_DIR)
                  if os.path.splitext(f)[1] in SOUND_EXT and os.path.isfile(os.path.join(BGM_DIR, f)))


def preflight(tepc_only):
    need = [(SRCMAP, "원본 맵 (SCMDraft 로 저장)"), (TEPC, "tepc"), (STAT, "stat_txt.tbl"),
            (os.path.join(PROJ, "main.lua"), "main.lua")]
    if not tepc_only:
        need += [(EUDDRAFT, "euddraft"), (CPLP, "CustomPlibLockProtector.exe"),
                 (CPLP_PLUGIN, "euddraft 의 [CPLP] 플러그인"), (BGM_PLUGIN, "euddraft 의 [Respect_V_Plugin] 플러그인"),
                 (os.path.join(BUILD, "eudplibData", "EUDEditor.eds"),
                  "build 데이터 (python tools\\build.py --refresh-data)")]
    missing = ["%s 가 없다: %s" % (what, p) for p, what in need if not os.path.isfile(p)]
    if not tepc_only and not bgm_files():
        missing.append("음원 폴더가 없거나 비었다: %s" % BGM_DIR)
    return missing


def refresh_data():
    """EUD Editor 의 임시 빌드 폴더 -> build/ (SCA 라이브러리·캐시·e3s 백업 제외)."""
    src_eds = os.path.join(EUD_EDITOR_DATA, "eudplibData", "EUDEditor.eds")
    if not os.path.isfile(src_eds):
        raise SystemExit("EUD Editor 빌드 데이터가 없다: %s\n  EUD Editor 3 로 Respect_V_DLC.e3s 를 한 번 빌드하면 생긴다."
                         % src_eds)
    tmp = BUILD + ".tmp"
    shutil.rmtree(tmp, ignore_errors=True)
    copied = []
    for sub in ("eudplibData", "temp"):
        for root, dirs, files in os.walk(os.path.join(EUD_EDITOR_DATA, sub)):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for f in files:
                if os.path.splitext(f)[0] in SCA_LIBS or f.endswith(".pyc"):
                    continue
                s = os.path.join(root, f)
                rel = os.path.relpath(s, EUD_EDITOR_DATA)
                d = os.path.join(tmp, rel)
                os.makedirs(os.path.dirname(d), exist_ok=True)
                shutil.copy2(s, d)
                copied.append(rel)
    # 뺀 SCA 라이브러리를 누가 부르면 빌드가 깨진다. 남은 파일에 이름이 보이면 멈춘다.
    pat = re.compile(r"\b(%s)\b" % "|".join(sorted(SCA_LIBS)))
    for rel in copied:
        with open(os.path.join(tmp, rel), "rb") as f:
            m = pat.search(decode(f.read()))
        if m:
            shutil.rmtree(tmp, ignore_errors=True)
            raise SystemExit("%s 가 SCA 라이브러리 %s 를 부른다 - SCA_LIBS 에서 빼고 다시 하라" % (rel, m.group(1)))
    shutil.rmtree(BUILD, ignore_errors=True)
    os.replace(tmp, BUILD)
    print("build/ 새로 채움 (%s)\n  %d개: %s" % (EUD_EDITOR_DATA, len(copied), ", ".join(sorted(copied))))


def scmd_unit_names():
    """SCMDraft 식 유닛 이름('이름 (부제)') -> ID. tepc 는 stat_txt 의 첫 필드만 알아서 이 표를 끼운다
    (MSF_UE_RE/tools/build_scrdb.py 와 같다)."""
    d = open(STAT, "rb").read()
    n = struct.unpack_from("<H", d, 0)[0]
    offs = struct.unpack_from("<%dH" % n, d, 2)
    out = {}
    for i in range(228):
        parts = d[offs[i]:].split(b"\0", 2)
        if len(parts) >= 2 and parts[1] not in (b"", b"*"):
            out[(parts[0] + b" (" + parts[1] + b")").decode("latin-1")] = i
    return out


def compile_tepc(work, stage1):
    print("\n=== 1. tepc (main.lua -> %s)" % stage1)
    os.makedirs(work, exist_ok=True)
    shutil.copy2(TEPC, os.path.join(work, "tepc.exe"))    # tepc 는 제 옆에 임시 chk 를 쓴다
    shutil.copy2(SRCMAP, os.path.join(work, "in.scx"))    # 원본 맵은 읽기만 한다
    # SCMDraft 의 TEP 편집기 본문이 하던 일: 맵 디렉터리(TRIGP 가 갈 곳)와 Curdir 를 잡고 main.lua 를 부른다.
    # main.lua 는 Curdir 기준으로 MapSource\Library 와 MSF_Respect_V 의 .lua 를 스스로 읽는다.
    names = scmd_unit_names()
    lines = ['__MapDirSetting("%s")' % lua_str(EUDDIR),
             'Curdir = "%s"' % lua_str(DOCS + "\\"),
             "local SCMDUnit = {"]
    for k, v in sorted(names.items(), key=lambda kv: kv[1]):
        lines.append('\t["%s"] = %d,' % (k.replace("\\", "\\\\").replace('"', '\\"'), v))
    lines += ["}",
              "local NativeParseUnit = ParseUnit",
              "function ParseUnit(Unit)",
              '\tif type(Unit) == "string" and SCMDUnit[Unit] ~= nil then return SCMDUnit[Unit] end',
              "\treturn NativeParseUnit(Unit)",
              "end",
              'dofile("%s")' % lua_str(os.path.join(PROJ, "main.lua")),
              ""]
    with open(os.path.join(work, "editor.lua"), "w", encoding="utf-8", newline="") as f:
        f.write("\r\n".join(lines))
    cmd = [os.path.join(work, "tepc.exe"), "in.scx", "editor.lua", stage1, "--cflag", "1", "--stat-txt", STAT]
    started = time.time()
    r = subprocess.run(cmd, cwd=work, capture_output=True, timeout=3600)
    log = decode(r.stdout + r.stderr)
    with open(os.path.join(work, "tepc.log"), "w", encoding="utf-8") as f:
        f.write(log)
    print("  rc=%d (%.1f초, 로그 -> %s)" % (r.returncode, time.time() - started, os.path.join(work, "tepc.log")))
    print("\n".join("  | " + l for l in log.splitlines()[-15:]))
    if r.returncode == 0 and not os.path.isfile(stage1):
        print("tepc 가 rc=0 인데 %s 를 만들지 않았다" % stage1)
        return 6
    return r.returncode


def write_eds(eds, stage1):
    """EUD Editor 가 만든 eds 에서 입출력만 이번 빌드로 바꾼다. STRCtrig 는 v5.5 + Ctemp 로 맞춘다."""
    with open(eds, "r", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    out, section = [], ""
    for ln in lines:
        low = ln.strip().lower()
        if low.startswith("[") and low.endswith("]"):
            section = low
            if low.startswith("[strctrig assembler v5.4]"):
                out.append("[STRCtrig Assembler v5.5]")   # CtrigAsm v5.5 가 만든 TRIGP 청크는 v5.5 가 읽는다
                continue
        if section.startswith("[strctrig assembler") and low.startswith("path"):
            out.append("Path : %s\\Ctemp\\" % EUDDIR)       # tepc 는 TRIGP*.chk 를 <맵 디렉터리>\Ctemp 에 쓴다
            continue
        if section == "[main]" and low.startswith("input:"):
            out.append("input: " + stage1)
            continue
        if section == "[main]" and low.startswith("output:"):
            out.append("output: " + FINAL)
            continue
        out.append(ln)
    if not any(l.strip().lower() == "[cplp]" for l in out):
        out.append("[CPLP]")
    with open(eds, "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(out) + "\n")
    print("  eds: 입력 %s\n       출력 %s" % (stage1, FINAL))


def run_euddraft(work, stage1, since):
    print("\n=== 2. euddraft")
    stage = os.path.join(work, "eudbuild")
    shutil.copytree(BUILD, stage)
    eds = os.path.join(stage, "eudplibData", "EUDEditor.eds")
    write_eds(eds, stage1)
    cmd = [EUDDRAFT, eds]
    print("  " + " ".join('"%s"' % c if " " in c else c for c in cmd))
    # 오류가 나면 euddraft 가 "Press Enter" 로 멈추므로 표준입력을 막아 둔다.
    r = subprocess.run(cmd, cwd=EUDDIR, timeout=3600, stdin=subprocess.DEVNULL, capture_output=True)
    out = decode(r.stdout + r.stderr)
    with open(os.path.join(work, "euddraft.log"), "w", encoding="utf-8") as f:
        f.write(out)
    # 원본 지형의 null 타일 경고가 "Null tiles at: ..." 수만 자짜리 한 줄을 찍는다. 콘솔에는 앞부분만 (전체는 로그).
    print("\n".join("  | " + (l if len(l) <= 200 else l[:200] + " ...(%d자, 로그 참고)" % len(l))
                    for l in out.rstrip().splitlines()[-25:]))
    print("  rc=%d (전체 로그 -> %s)" % (r.returncode, os.path.join(work, "euddraft.log")))
    if r.returncode != 0:
        return r.returncode
    if not os.path.isfile(FINAL) or os.path.getmtime(FINAL) < since:
        print("euddraft 가 %s 를 새로 만들지 않았다 (게임에서 맵을 열어 두었으면 닫고 다시)" % FINAL)
        return 4
    return 0


def verify_bgm(path, sounds):
    """음원이 전부 원래 이름으로, 바이트까지 같게 들어갔는지 본다. 틀린 파일 이름 목록을 돌려준다."""
    bad = []
    with mpq.Archive(path) as a:
        for name in sounds:
            with open(os.path.join(BGM_DIR, name), "rb") as f:
                if a.read("staredit\\wav\\" + name) != f.read():
                    bad.append(name)
    return bad


def run_cplp(since):
    print("\n=== 3. CPLP")
    cmd = [CPLP, FINAL]
    print("  " + " ".join('"%s"' % c if " " in c else c for c in cmd))
    for attempt in (1, 2):
        r = subprocess.run(cmd, cwd=EUDDIR, timeout=3600, stdin=subprocess.DEVNULL)
        print("  rc=%d" % r.returncode)
        if r.returncode == 0:
            break
        if attempt == 1:
            # DPS·MSF_UE_RE 빌드에서 본 것: CPLP 는 가끔 이유 없이 실패하고(rc=3, 0xC0000409)
            # 같은 입력으로 다시 돌리면 통과한다. euddraft 까지 끝난 빌드를 버리지 않게 한 번만 다시 한다.
            print("  CPLP 실패. 한 번 다시 시도한다.")
            time.sleep(1.0)
    if r.returncode != 0:
        return r.returncode
    if not os.path.isfile(FINAL_OUT) or os.path.getmtime(FINAL_OUT) < since:
        print("CPLP 가 %s 를 새로 만들지 않았다" % FINAL_OUT)
        return 5
    return 0


def main():
    ap = argparse.ArgumentParser(description="MSF_Respect_V 원클릭 빌드 (tepc -> euddraft -> CPLP)")
    ap.add_argument("--tepc-only", action="store_true", help="1단계(tepc)만 돌린다")
    ap.add_argument("--refresh-data", action="store_true",
                    help="build/ 를 EUD Editor 가 마지막으로 만든 빌드 데이터로 다시 채우고 끝낸다")
    args = ap.parse_args()
    if args.refresh_data:
        refresh_data()
        return 0

    started = time.time()
    missing = preflight(args.tepc_only)
    if missing:
        print("빌드를 시작할 수 없다:")
        for m in missing:
            print("  - " + m)
        return 1

    # 작업 폴더는 %TEMP% 아래 전용 이름. 원본 맵 폴더와 겹치면 시작할 때 rmtree 가 원본을 지운다.
    work = os.path.join(os.environ.get("TEMP", "."), "respect_v_build")
    shutil.rmtree(work, ignore_errors=True)
    stage1 = os.path.join(work, "stage1.scx")
    rc = compile_tepc(work, stage1)
    if rc != 0 or args.tepc_only:
        return rc
    rc = run_euddraft(work, stage1, started)
    if rc != 0:
        return rc
    sounds = bgm_files()
    bad = verify_bgm(FINAL, sounds)
    if bad:
        print("오류: 음원 %d개 중 %d개가 최종 맵에 없거나 다르다: %s" % (len(sounds), len(bad), bad[:5]))
        return 7
    print("  음원 %d개가 최종 맵에 원래 이름·내용 그대로 들어감" % len(sounds))
    rc = run_cplp(started)
    if rc != 0:
        return rc
    print("\n최종 산출물 (%.0f초)" % (time.time() - started))
    for p in (FINAL, FINAL_OUT):
        print("  %s (%d B)" % (p, os.path.getsize(p)))
    print("  플레이할 맵 = %s" % os.path.basename(FINAL_OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
