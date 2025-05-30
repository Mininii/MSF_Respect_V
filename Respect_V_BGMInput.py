from eudplib import *
import math

#Laptop : 'C:\\Users\\whatd\\Desktop\\Stormcoast Fortress\\ScmDraft 2\\MapSource\\MEME_EUD_Project\\'
#Desktop : 'C:\\Users\\USER\\Documents\\MapSource\\MEME_EUD_Project'

def Exec_OggFile():
	BGMArr = [
	"BGM_OP.ogg",
	"BGM_BlueWhite.ogg",
	"BGM_OnlyForYou.ogg",
	"BGM_Kamui.ogg",
	"BGM_ALiCE.ogg",
	"BGM_ECiLA.ogg",
	"BGM_D2.ogg",
	"BGM_OBLIVION.ogg",
	"BGM_Hypernaid.ogg",
	"BGM_Mysti_Era_Mui.ogg",
	"BGM_NewGameStart.ogg",
	"BGM_OverMe.ogg",
	"BGM_EnemyStorm.ogg",
	"BGM_Diomedes.ogg",
	"BGM_Dream_it.ogg",
	"BGM_Blythe.ogg",
	"BGM_Black_Swan.ogg",
	"BGM_Launcher.ogg",
	"BGM_Miles.ogg",
	"BGM_DontDie.ogg",
	"BGM_Daydream.ogg",
	"BGM_Hello.ogg",
	"BGM_DIE_IN.ogg",
	"BGM_ReBIRTH.ogg",
	"BGM_Omen.ogg",
	"BGM_Summer2017.ogg",
	"BGM_SpaceofSoul.ogg",
	"BGM_OP_DLC.ogg",
	"BGM_OP_DLC2.ogg",
	"ADEnd.ogg",
	"ADUse.ogg",
	"BossWin.ogg",
	"CTEnd.ogg",
	"Herokill.ogg",
	"hongparksa.ogg",
	"Marinedead.ogg",
	"PP_SFX.ogg",
	"revive.ogg",
	"scan.wav",
	"scanr.wav",
	"SoundHorror.ogg",
	"unlock.ogg",
	"Wavecall_R.ogg",
	"zzirizziri.ogg",
	"BGM_SongForYou.ogg",
	"BGM_Never_Die.ogg",
	"BGM_MyHead.ogg",
	"BGM_Misty_ErA_OneDay.ogg",
	"BGM_Misty_ErA.ogg",
	"BGM_Lisrim.ogg",
	"BGM_Licrom.ogg",
	"BGM_KICK_IT.ogg",
	"BGM_Insane_Drift.ogg",
	"BGM_ELIXIR.ogg",
	"BGM_CottonCandySoda.ogg",
	"BGM_Away.ogg",
	"BGM_1234.ogg",
	"BGM_Maple.ogg"

	]
	for i in BGMArr:
		MPQAddFile('staredit\\wav\\'+i, open('C:/euddraft0.9.2.0/Respect_V_BGM/'+i, 'rb').read())

	for i in range(61):
		p = i+1
		if p<=9:
			MPQAddFile('staredit\\wav\\gMAX_00'+str(p)+'.ogg', open('C:/euddraft0.9.2.0/Respect_V_BGM/gMAX_00'+str(p)+'.ogg', 'rb').read())
		elif p>=10 and p<= 99:
			MPQAddFile('staredit\\wav\\gMAX_0'+str(p)+'.ogg', open('C:/euddraft0.9.2.0/Respect_V_BGM/gMAX_0'+str(p)+'.ogg', 'rb').read())

			