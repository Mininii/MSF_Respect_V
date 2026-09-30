from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, -1),# units:Graphics  index:0    from 78 To 77
        SetMemory(0x6644F8, Add, 768),# units:Graphics  index:1    from 74 To 77
        SetMemory(0x664500, Add, -4194304),# units:Graphics  index:10    from 73 To 9
        SetMemory(0x664504, Add, 33554432),# units:Graphics  index:15    from 71 To 73
        SetMemory(0x66450C, Add, -4),# units:Graphics  index:20    from 78 To 74
        SetMemory(0x664518, Add, 5),# units:Graphics  index:32    from 73 To 78
        SetMemory(0x664530, Add, 256),# units:Graphics  index:57    from 12 To 13
        SetMemory(0x664540, Add, -2),# units:Graphics  index:72    from 39 To 37
        SetMemory(0x66454C, Add, -9),# units:Graphics  index:84    from 50 To 41
        SetMemory(0x664550, Add, -18688),# units:Graphics  index:89    from 115 To 42
        SetMemory(0x664550, Add, -4915200),# units:Graphics  index:90    from 116 To 41
        SetMemory(0x664550, Add, -536870912),# units:Graphics  index:91    from 43 To 11
        SetMemory(0x664554, Add, 27),# units:Graphics  index:92    from 43 To 70
        SetMemory(0x664554, Add, -9764864),# units:Graphics  index:94    from 199 To 50
        SetMemory(0x664554, Add, -687865856),# units:Graphics  index:95    from 114 To 73
        SetMemory(0x664558, Add, -152),# units:Graphics  index:96    from 200 To 48
        SetMemory(0x664558, Add, 50331648),# units:Graphics  index:99    from 74 To 77
        SetMemory(0x66455C, Add, 3),# units:Graphics  index:100    from 74 To 77
        SetMemory(0x664564, Add, -63),# units:Graphics  index:108    from 108 To 45
        SetMemory(0x66456C, Add, -15360),# units:Graphics  index:117    from 98 To 38
        SetMemory(0x66456C, Add, -3932160),# units:Graphics  index:118    from 103 To 43
        SetMemory(0x66456C, Add, 2466250752),# units:Graphics  index:119    from 43 To 190
        SetMemory(0x664570, Add, 9472),# units:Graphics  index:121    from 43 To 80
        SetMemory(0x664588, Add, 24832),# units:Graphics  index:145    from 43 To 140
        SetMemory(0x664590, Add, 9472),# units:Graphics  index:153    from 43 To 80
        SetMemory(0x664594, Add, 6356992),# units:Graphics  index:158    from 43 To 140
        SetMemory(0x661260, Add, -330),# units:Construction Animation  index:108    from 330 To 0
        SetMemory(0x661284, Add, -330),# units:Construction Animation  index:117    from 330 To 0
        SetMemory(0x661288, Add, -330),# units:Construction Animation  index:118    from 330 To 0
        SetMemory(0x661294, Add, -325),# units:Construction Animation  index:121    from 325 To 0
        SetMemory(0x66065C, Add, 32),# units:Unit Direction  index:108    from 0 To 32
        SetMemory(0x660664, Add, 2097152),# units:Unit Direction  index:118    from 0 To 32
        SetMemory(0x660668, Add, 8192),# units:Unit Direction  index:121    from 0 To 32
        SetMemory(0x660688, Add, 8192),# units:Unit Direction  index:153    from 0 To 32
        SetMemory(0x664824, Add, 256),# units:Shield Enable  index:117    from 0 To 1
        SetMemory(0x66484C, Add, -65536),# units:Shield Enable  index:158    from 1 To 0
        SetMemory(0x660E18, Add, 648806400),# units:Shield Amount  index:13    from 100 To 10000
        SetMemory(0x660F78, Add, 4288348160),# units:Shield Amount  index:189    from 100 To 65535
        SetMemory(0x662384, Add, 5114880),# units:Hit Points  index:13    from 5120 To 5120000
        SetMemory(0x6623DC, Add, -5300),# units:Hit Points  index:35    from 6400 To 1100
        SetMemory(0x6623E0, Add, -48500),# units:Hit Points  index:36    from 51200 To 2700
        SetMemory(0x6623E4, Add, 195840),# units:Hit Points  index:37    from 8960 To 204800
        SetMemory(0x6623E8, Add, 286720),# units:Hit Points  index:38    from 20480 To 307200
        SetMemory(0x6623EC, Add, 486400),# units:Hit Points  index:39    from 102400 To 588800
        SetMemory(0x6623F4, Add, 117760),# units:Hit Points  index:41    from 10240 To 128000
        SetMemory(0x6623F8, Add, 25548800),# units:Hit Points  index:42    from 51200 To 25600000
        SetMemory(0x6623FC, Add, 276480),# units:Hit Points  index:43    from 30720 To 307200
        SetMemory(0x662400, Add, 524800),# units:Hit Points  index:44    from 38400 To 563200
        SetMemory(0x662404, Add, 1505280),# units:Hit Points  index:45    from 30720 To 1536000
        SetMemory(0x662408, Add, 747520),# units:Hit Points  index:46    from 20480 To 768000
        SetMemory(0x66240C, Add, 198400),# units:Hit Points  index:47    from 6400 To 204800
        SetMemory(0x662410, Add, 1664000),# units:Hit Points  index:48    from 204800 To 1868800
        SetMemory(0x662418, Add, 1008640),# units:Hit Points  index:50    from 15360 To 1024000
        SetMemory(0x66241C, Add, 2432000),# units:Hit Points  index:51    from 102400 To 2534400
        SetMemory(0x662424, Add, 650240),# units:Hit Points  index:53    from 40960 To 691200
        SetMemory(0x662428, Add, 276480),# units:Hit Points  index:54    from 30720 To 307200
        SetMemory(0x66242C, Add, 1203200),# units:Hit Points  index:55    from 76800 To 1280000
        SetMemory(0x662430, Add, 2201600),# units:Hit Points  index:56    from 102400 To 2304000
        SetMemory(0x66243C, Add, -50412),# units:Hit Points  index:59    from 51200 To 788
        SetMemory(0x6624B8, Add, 16640),# units:Hit Points  index:90    from 15360 To 32000
        SetMemory(0x6624D0, Add, 512),# units:Hit Points  index:96    from 15360 To 15872
        SetMemory(0x6624D4, Add, -49540),# units:Hit Points  index:97    from 51200 To 1660
        SetMemory(0x6624EC, Add, 3296000),# units:Hit Points  index:103    from 32000 To 3328000
        SetMemory(0x6624F0, Add, 1971200),# units:Hit Points  index:104    from 76800 To 2048000
        SetMemory(0x662504, Add, 1664000),# units:Hit Points  index:109    from 128000 To 1792000
        SetMemory(0x662510, Add, 1894400),# units:Hit Points  index:112    from 153600 To 2048000
        SetMemory(0x662528, Add, -121600),# units:Hit Points  index:118    from 153600 To 32000
        SetMemory(0x66252C, Add, 255),# units:Hit Points  index:119    from 1 To 256
        SetMemory(0x662534, Add, 31999),# units:Hit Points  index:121    from 1 To 32000
        SetMemory(0x66253C, Add, 1984000),# units:Hit Points  index:123    from 192000 To 2176000
        SetMemory(0x662568, Add, 6080000),# units:Hit Points  index:134    from 64000 To 6144000
        SetMemory(0x66256C, Add, 6182400),# units:Hit Points  index:135    from 217600 To 6400000
        SetMemory(0x662570, Add, 6950400),# units:Hit Points  index:136    from 217600 To 7168000
        SetMemory(0x662574, Add, 6092800),# units:Hit Points  index:137    from 256000 To 6348800
        SetMemory(0x662578, Add, 8826880),# units:Hit Points  index:138    from 217600 To 9044480
        SetMemory(0x66257C, Add, 5836288),# units:Hit Points  index:139    from 192000 To 6028288
        SetMemory(0x662580, Add, 9034240),# units:Hit Points  index:140    from 153600 To 9187840
        SetMemory(0x662584, Add, 8990720),# units:Hit Points  index:141    from 153600 To 9144320
        SetMemory(0x662588, Add, 5588480),# units:Hit Points  index:142    from 192000 To 5780480
        SetMemory(0x66258C, Add, 7633920),# units:Hit Points  index:143    from 102400 To 7736320
        SetMemory(0x662590, Add, 5913600),# units:Hit Points  index:144    from 102400 To 6016000
        SetMemory(0x662598, Add, 8115200),# units:Hit Points  index:146    from 76800 To 8192000
        SetMemory(0x6625A4, Add, 3008000),# units:Hit Points  index:149    from 192000 To 3200000
        SetMemory(0x6625B4, Add, 31999),# units:Hit Points  index:153    from 1 To 32000
        SetMemory(0x662644, Add, 2145100800),# units:Hit Points  index:189    from 179200 To 2145280000
        SetMemory(0x663154, Add, 134217728),# units:Elevation Level  index:7    from 4 To 12
        SetMemory(0x66315C, Add, 2048),# units:Elevation Level  index:13    from 4 To 12
        SetMemory(0x66316C, Add, 786432),# units:Elevation Level  index:30    from 4 To 16
        SetMemory(0x66318C, Add, 134217728),# units:Elevation Level  index:63    from 4 To 12
        SetMemory(0x663190, Add, 8),# units:Elevation Level  index:64    from 4 To 12
        SetMemory(0x6631A8, Add, 2048),# units:Elevation Level  index:89    from 4 To 12
        SetMemory(0x6631A8, Add, 917504),# units:Elevation Level  index:90    from 4 To 18
        SetMemory(0x6631BC, Add, 8),# units:Elevation Level  index:108    from 4 To 12
        SetMemory(0x6631C4, Add, 917504),# units:Elevation Level  index:118    from 4 To 18
        SetMemory(0x6631C4, Add, 134217728),# units:Elevation Level  index:119    from 4 To 12
        SetMemory(0x6631C8, Add, 3584),# units:Elevation Level  index:121    from 4 To 18
        SetMemory(0x6631E8, Add, 3584),# units:Elevation Level  index:153    from 4 To 18
        SetMemory(0x663228, Add, 134217728),# units:Elevation Level  index:219    from 4 To 12
        SetMemory(0x661020, Add, 8650752),# units:Unknown (old Movement)  index:90    from 65 To 197
        SetMemory(0x661034, Add, 65),# units:Unknown (old Movement)  index:108    from 0 To 65
        SetMemory(0x66103C, Add, 49408),# units:Unknown (old Movement)  index:117    from 0 To 193
        SetMemory(0x66103C, Add, 12910592),# units:Unknown (old Movement)  index:118    from 0 To 197
        SetMemory(0x66103C, Add, 3305111552),# units:Unknown (old Movement)  index:119    from 0 To 197
        SetMemory(0x661040, Add, 50432),# units:Unknown (old Movement)  index:121    from 0 To 197
        SetMemory(0x661060, Add, 50432),# units:Unknown (old Movement)  index:153    from 0 To 197
        SetMemory(0x663DD0, Add, 16),# units:Rank/Sublabel  index:0    from 2 To 18
        SetMemory(0x663DD0, Add, 3328),# units:Rank/Sublabel  index:1    from 5 To 18
        SetMemory(0x663DF0, Add, -2),# units:Rank/Sublabel  index:32    from 4 To 2
        SetMemory(0x663E28, Add, 3072),# units:Rank/Sublabel  index:89    from 0 To 12
        SetMemory(0x663E34, Add, -4),# units:Rank/Sublabel  index:100    from 22 To 18
        SetMemory(0x663E44, Add, 4352),# units:Rank/Sublabel  index:117    from 0 To 17
        SetMemory(0x662EA8, Add, -1526726656),# units:Comp AI Idle  index:11    from 93 To 2
        SetMemory(0x662EC0, Add, -11337728),# units:Comp AI Idle  index:34    from 175 To 2
        SetMemory(0x662ED8, Add, -39424),# units:Comp AI Idle  index:57    from 156 To 2
        SetMemory(0x662EE4, Add, -23296),# units:Comp AI Idle  index:69    from 93 To 2
        SetMemory(0x662EE8, Add, -48),# units:Comp AI Idle  index:72    from 50 To 2
        SetMemory(0x662EF0, Add, -14336),# units:Comp AI Idle  index:81    from 58 To 2
        SetMemory(0x662EF0, Add, -939524096),# units:Comp AI Idle  index:83    from 58 To 2
        SetMemory(0x662EF4, Add, -157),# units:Comp AI Idle  index:84    from 159 To 2
        SetMemory(0x662EF8, Add, -352321536),# units:Comp AI Idle  index:91    from 23 To 2
        SetMemory(0x662EFC, Add, -21),# units:Comp AI Idle  index:92    from 23 To 2
        SetMemory(0x662EFC, Add, -131072),# units:Comp AI Idle  index:94    from 2 To 0
        SetMemory(0x662F0C, Add, -154),# units:Comp AI Idle  index:108    from 156 To 2
        SetMemory(0x662F14, Add, -39424),# units:Comp AI Idle  index:117    from 156 To 2
        SetMemory(0x662F14, Add, -10092544),# units:Comp AI Idle  index:118    from 156 To 2
        SetMemory(0x662F14, Add, -2583691264),# units:Comp AI Idle  index:119    from 156 To 2
        SetMemory(0x662F18, Add, -39424),# units:Comp AI Idle  index:121    from 156 To 2
        SetMemory(0x662F30, Add, -34048),# units:Comp AI Idle  index:145    from 156 To 23
        SetMemory(0x662F38, Add, -39424),# units:Comp AI Idle  index:153    from 156 To 2
        SetMemory(0x662F38, Add, -8716288),# units:Comp AI Idle  index:154    from 156 To 23
        SetMemory(0x662F3C, Add, -8716288),# units:Comp AI Idle  index:158    from 156 To 23
        SetMemory(0x662F40, Add, -133),# units:Comp AI Idle  index:160    from 156 To 23
        SetMemory(0x662F44, Add, -2231369728),# units:Comp AI Idle  index:167    from 156 To 23
        SetMemory(0x662F48, Add, -133),# units:Comp AI Idle  index:168    from 156 To 23
        SetMemory(0x662F4C, Add, -8716288),# units:Comp AI Idle  index:174    from 156 To 23
        SetMemory(0x662F4C, Add, -2231369728),# units:Comp AI Idle  index:175    from 156 To 23
        SetMemory(0x662F74, Add, -1241513984),# units:Comp AI Idle  index:215    from 97 To 23
        SetMemory(0x662F78, Add, -18944),# units:Comp AI Idle  index:217    from 97 To 23
        SetMemory(0x662F78, Add, -1241513984),# units:Comp AI Idle  index:219    from 97 To 23
        SetMemory(0x662270, Add, -1526726656),# units:Human AI Idle  index:11    from 93 To 2
        SetMemory(0x662288, Add, -11337728),# units:Human AI Idle  index:34    from 175 To 2
        SetMemory(0x6622A0, Add, -23296),# units:Human AI Idle  index:57    from 93 To 2
        SetMemory(0x6622AC, Add, -23296),# units:Human AI Idle  index:69    from 93 To 2
        SetMemory(0x6622B0, Add, -48),# units:Human AI Idle  index:72    from 50 To 2
        SetMemory(0x6622B8, Add, -14336),# units:Human AI Idle  index:81    from 58 To 2
        SetMemory(0x6622B8, Add, -939524096),# units:Human AI Idle  index:83    from 58 To 2
        SetMemory(0x6622C0, Add, -41984),# units:Human AI Idle  index:89    from 166 To 2
        SetMemory(0x6622C0, Add, -10747904),# units:Human AI Idle  index:90    from 166 To 2
        SetMemory(0x6622C0, Add, -352321536),# units:Human AI Idle  index:91    from 23 To 2
        SetMemory(0x6622C4, Add, -21),# units:Human AI Idle  index:92    from 23 To 2
        SetMemory(0x6622C4, Add, -41984),# units:Human AI Idle  index:93    from 166 To 2
        SetMemory(0x6622C4, Add, -10878976),# units:Human AI Idle  index:94    from 166 To 0
        SetMemory(0x6622C4, Add, -2751463424),# units:Human AI Idle  index:95    from 166 To 2
        SetMemory(0x6622C8, Add, -164),# units:Human AI Idle  index:96    from 166 To 2
        SetMemory(0x6622D4, Add, -122),# units:Human AI Idle  index:108    from 124 To 2
        SetMemory(0x6622DC, Add, -5376),# units:Human AI Idle  index:117    from 23 To 2
        SetMemory(0x6622DC, Add, -1376256),# units:Human AI Idle  index:118    from 23 To 2
        SetMemory(0x6622DC, Add, -352321536),# units:Human AI Idle  index:119    from 23 To 2
        SetMemory(0x6622E0, Add, -5376),# units:Human AI Idle  index:121    from 23 To 2
        SetMemory(0x662300, Add, -5376),# units:Human AI Idle  index:153    from 23 To 2
        SetMemory(0x66233C, Add, -1241513984),# units:Human AI Idle  index:215    from 97 To 23
        SetMemory(0x662340, Add, -18944),# units:Human AI Idle  index:217    from 97 To 23
        SetMemory(0x662340, Add, -1241513984),# units:Human AI Idle  index:219    from 97 To 23
        SetMemory(0x6648A0, Add, -1526726656),# units:Return to Idle  index:11    from 93 To 2
        SetMemory(0x6648B8, Add, -11337728),# units:Return to Idle  index:34    from 175 To 2
        SetMemory(0x6648D0, Add, -23296),# units:Return to Idle  index:57    from 93 To 2
        SetMemory(0x6648DC, Add, -23296),# units:Return to Idle  index:69    from 93 To 2
        SetMemory(0x6648E0, Add, -48),# units:Return to Idle  index:72    from 50 To 2
        SetMemory(0x6648E8, Add, -14336),# units:Return to Idle  index:81    from 58 To 2
        SetMemory(0x6648E8, Add, -939524096),# units:Return to Idle  index:83    from 58 To 2
        SetMemory(0x6648F0, Add, -41984),# units:Return to Idle  index:89    from 166 To 2
        SetMemory(0x6648F0, Add, -10747904),# units:Return to Idle  index:90    from 166 To 2
        SetMemory(0x6648F0, Add, -352321536),# units:Return to Idle  index:91    from 23 To 2
        SetMemory(0x6648F4, Add, -21),# units:Return to Idle  index:92    from 23 To 2
        SetMemory(0x6648F4, Add, -41984),# units:Return to Idle  index:93    from 166 To 2
        SetMemory(0x6648F4, Add, -10878976),# units:Return to Idle  index:94    from 166 To 0
        SetMemory(0x6648F4, Add, -2751463424),# units:Return to Idle  index:95    from 166 To 2
        SetMemory(0x6648F8, Add, -164),# units:Return to Idle  index:96    from 166 To 2
        SetMemory(0x664904, Add, -122),# units:Return to Idle  index:108    from 124 To 2
        SetMemory(0x66490C, Add, -5376),# units:Return to Idle  index:117    from 23 To 2
        SetMemory(0x66490C, Add, -1376256),# units:Return to Idle  index:118    from 23 To 2
        SetMemory(0x66490C, Add, -352321536),# units:Return to Idle  index:119    from 23 To 2
        SetMemory(0x664910, Add, -5376),# units:Return to Idle  index:121    from 23 To 2
        SetMemory(0x664930, Add, -5376),# units:Return to Idle  index:153    from 23 To 2
        SetMemory(0x66496C, Add, -1241513984),# units:Return to Idle  index:215    from 97 To 23
        SetMemory(0x664970, Add, -18944),# units:Return to Idle  index:217    from 97 To 23
        SetMemory(0x664970, Add, -1241513984),# units:Return to Idle  index:219    from 97 To 23
        SetMemory(0x663328, Add, -184549376),# units:Attack Unit  index:11    from 21 To 10
        SetMemory(0x66332C, Add, -184549376),# units:Attack Unit  index:15    from 21 To 10
        SetMemory(0x663340, Add, -10813440),# units:Attack Unit  index:34    from 175 To 10
        SetMemory(0x663358, Add, -2816),# units:Attack Unit  index:57    from 21 To 10
        SetMemory(0x66335C, Add, -184549376),# units:Attack Unit  index:63    from 21 To 10
        SetMemory(0x663364, Add, -2816),# units:Attack Unit  index:69    from 21 To 10
        SetMemory(0x663368, Add, -43),# units:Attack Unit  index:72    from 53 To 10
        SetMemory(0x663370, Add, -12544),# units:Attack Unit  index:81    from 59 To 10
        SetMemory(0x663370, Add, -822083584),# units:Attack Unit  index:83    from 59 To 10
        SetMemory(0x663378, Add, -45568),# units:Attack Unit  index:89    from 188 To 10
        SetMemory(0x663378, Add, -11665408),# units:Attack Unit  index:90    from 188 To 10
        SetMemory(0x663378, Add, -218103808),# units:Attack Unit  index:91    from 23 To 10
        SetMemory(0x66337C, Add, -13),# units:Attack Unit  index:92    from 23 To 10
        SetMemory(0x66337C, Add, -45568),# units:Attack Unit  index:93    from 188 To 10
        SetMemory(0x66337C, Add, -12320768),# units:Attack Unit  index:94    from 188 To 0
        SetMemory(0x66337C, Add, -2986344448),# units:Attack Unit  index:95    from 188 To 10
        SetMemory(0x663380, Add, -178),# units:Attack Unit  index:96    from 188 To 10
        SetMemory(0x66338C, Add, -13),# units:Attack Unit  index:108    from 23 To 10
        SetMemory(0x663394, Add, -3328),# units:Attack Unit  index:117    from 23 To 10
        SetMemory(0x663394, Add, -851968),# units:Attack Unit  index:118    from 23 To 10
        SetMemory(0x663394, Add, -218103808),# units:Attack Unit  index:119    from 23 To 10
        SetMemory(0x663398, Add, -3328),# units:Attack Unit  index:121    from 23 To 10
        SetMemory(0x6633B8, Add, -3328),# units:Attack Unit  index:153    from 23 To 10
        SetMemory(0x663A70, Add, -11337728),# units:Attack Move  index:34    from 175 To 2
        SetMemory(0x663A98, Add, -48),# units:Attack Move  index:72    from 50 To 2
        SetMemory(0x663AA0, Add, -14336),# units:Attack Move  index:81    from 58 To 2
        SetMemory(0x663AA0, Add, -939524096),# units:Attack Move  index:83    from 58 To 2
        SetMemory(0x663AA8, Add, -47616),# units:Attack Move  index:89    from 188 To 2
        SetMemory(0x663AA8, Add, -12189696),# units:Attack Move  index:90    from 188 To 2
        SetMemory(0x663AA8, Add, -352321536),# units:Attack Move  index:91    from 23 To 2
        SetMemory(0x663AAC, Add, -21),# units:Attack Move  index:92    from 23 To 2
        SetMemory(0x663AAC, Add, -47616),# units:Attack Move  index:93    from 188 To 2
        SetMemory(0x663AAC, Add, -12320768),# units:Attack Move  index:94    from 188 To 0
        SetMemory(0x663AAC, Add, -3120562176),# units:Attack Move  index:95    from 188 To 2
        SetMemory(0x663AB0, Add, -186),# units:Attack Move  index:96    from 188 To 2
        SetMemory(0x663ABC, Add, -21),# units:Attack Move  index:108    from 23 To 2
        SetMemory(0x663AC4, Add, -5376),# units:Attack Move  index:117    from 23 To 2
        SetMemory(0x663AC4, Add, -1376256),# units:Attack Move  index:118    from 23 To 2
        SetMemory(0x663AC4, Add, -352321536),# units:Attack Move  index:119    from 23 To 2
        SetMemory(0x663AC8, Add, -5376),# units:Attack Move  index:121    from 23 To 2
        SetMemory(0x663AE8, Add, -5376),# units:Attack Move  index:153    from 23 To 2
        SetMemory(0x6636B8, Add, 3),# units:Ground Weapon  index:0    from 0 To 3
        SetMemory(0x6636B8, Add, 256),# units:Ground Weapon  index:1    from 2 To 3
        SetMemory(0x6636BC, Add, 1),# units:Ground Weapon  index:4    from 7 To 8
        SetMemory(0x6636C0, Add, -1),# units:Ground Weapon  index:8    from 16 To 15
        SetMemory(0x6636C0, Add, -1572864),# units:Ground Weapon  index:10    from 26 To 2
        SetMemory(0x6636C4, Add, 1),# units:Ground Weapon  index:12    from 19 To 20
        SetMemory(0x6636C4, Add, -1761607680),# units:Ground Weapon  index:15    from 130 To 25
        SetMemory(0x6636D0, Add, 822083584),# units:Ground Weapon  index:27    from 21 To 70
        SetMemory(0x6636D8, Add, -25),# units:Ground Weapon  index:32    from 25 To 0
        SetMemory(0x6636D8, Add, -2359296),# units:Ground Weapon  index:34    from 130 To 94
        SetMemory(0x6636E4, Add, -5242880),# units:Ground Weapon  index:46    from 130 To 50
        SetMemory(0x6636EC, Add, -79),# units:Ground Weapon  index:52    from 130 To 51
        SetMemory(0x6636F0, Add, -9728),# units:Ground Weapon  index:57    from 130 To 92
        SetMemory(0x6636F0, Add, -2424832),# units:Ground Weapon  index:58    from 130 To 93
        SetMemory(0x6636F4, Add, -30),# units:Ground Weapon  index:60    from 130 To 100
        SetMemory(0x6636F4, Add, -1703936),# units:Ground Weapon  index:62    from 130 To 104
        SetMemory(0x6636F4, Add, -1862270976),# units:Ground Weapon  index:63    from 130 To 19
        SetMemory(0x6636F8, Add, -1040187392),# units:Ground Weapon  index:67    from 130 To 68
        SetMemory(0x6636FC, Add, 65536),# units:Ground Weapon  index:70    from 73 To 74
        SetMemory(0x663700, Add, -3),# units:Ground Weapon  index:72    from 130 To 127
        SetMemory(0x663708, Add, -25856),# units:Ground Weapon  index:81    from 130 To 29
        SetMemory(0x663708, Add, -905969664),# units:Ground Weapon  index:83    from 130 To 76
        SetMemory(0x66370C, Add, -51),# units:Ground Weapon  index:84    from 130 To 79
        SetMemory(0x66370C, Add, 318767104),# units:Ground Weapon  index:87    from 69 To 88
        SetMemory(0x663710, Add, -10240),# units:Ground Weapon  index:89    from 130 To 90
        SetMemory(0x663710, Add, -589824),# units:Ground Weapon  index:90    from 130 To 121
        SetMemory(0x663710, Add, -184549376),# units:Ground Weapon  index:91    from 130 To 119
        SetMemory(0x663714, Add, -10),# units:Ground Weapon  index:92    from 130 To 120
        SetMemory(0x663714, Add, -26624),# units:Ground Weapon  index:93    from 130 To 26
        SetMemory(0x663714, Add, -1761607680),# units:Ground Weapon  index:95    from 130 To 25
        SetMemory(0x663718, Add, -43),# units:Ground Weapon  index:96    from 130 To 87
        SetMemory(0x663718, Add, -2686976),# units:Ground Weapon  index:98    from 130 To 89
        SetMemory(0x663718, Add, -1828716544),# units:Ground Weapon  index:99    from 112 To 3
        SetMemory(0x66371C, Add, -113),# units:Ground Weapon  index:100    from 116 To 3
        SetMemory(0x66371C, Add, 65536),# units:Ground Weapon  index:102    from 21 To 22
        SetMemory(0x66372C, Add, -15104),# units:Ground Weapon  index:117    from 130 To 71
        SetMemory(0x66372C, Add, -131072),# units:Ground Weapon  index:118    from 130 To 128
        SetMemory(0x663730, Add, -2048),# units:Ground Weapon  index:121    from 130 To 122
        SetMemory(0x663734, Add, -39),# units:Ground Weapon  index:124    from 130 To 91
        SetMemory(0x6645E8, Add, -131072),# units:Max Ground Hits  index:10    from 3 To 1
        SetMemory(0x664600, Add, -2),# units:Max Ground Hits  index:32    from 3 To 1
        SetMemory(0x664638, Add, 256),# units:Max Ground Hits  index:89    from 0 To 1
        SetMemory(0x664654, Add, 256),# units:Max Ground Hits  index:117    from 0 To 1
        SetMemory(0x6616E0, Add, 3),# units:Air Weapon  index:0    from 0 To 3
        SetMemory(0x6616E0, Add, 256),# units:Air Weapon  index:1    from 2 To 3
        SetMemory(0x6616E8, Add, -8388608),# units:Air Weapon  index:10    from 130 To 2
        SetMemory(0x6616EC, Add, 0),# units:Air Weapon  index:12    from 20 To 20
        SetMemory(0x6616F0, Add, 7864320),# units:Air Weapon  index:18    from 10 To 130
        SetMemory(0x6616F8, Add, 805306368),# units:Air Weapon  index:27    from 22 To 70
        SetMemory(0x661700, Add, -130),# units:Air Weapon  index:32    from 130 To 0
        SetMemory(0x661708, Add, 65536),# units:Air Weapon  index:42    from 130 To 131
        SetMemory(0x661718, Add, -655360),# units:Air Weapon  index:58    from 103 To 93
        SetMemory(0x66171C, Add, -1862270976),# units:Air Weapon  index:63    from 130 To 19
        SetMemory(0x661724, Add, 0),# units:Air Weapon  index:70    from 74 To 74
        SetMemory(0x661728, Add, -3),# units:Air Weapon  index:72    from 130 To 127
        SetMemory(0x661738, Add, -589824),# units:Air Weapon  index:90    from 130 To 121
        SetMemory(0x661738, Add, -184549376),# units:Air Weapon  index:91    from 130 To 119
        SetMemory(0x66173C, Add, -10),# units:Air Weapon  index:92    from 130 To 120
        SetMemory(0x661740, Add, -720896),# units:Air Weapon  index:98    from 100 To 89
        SetMemory(0x661740, Add, -1828716544),# units:Air Weapon  index:99    from 112 To 3
        SetMemory(0x661744, Add, -113),# units:Air Weapon  index:100    from 116 To 3
        SetMemory(0x661754, Add, -15104),# units:Air Weapon  index:117    from 130 To 71
        SetMemory(0x661754, Add, -131072),# units:Air Weapon  index:118    from 130 To 128
        SetMemory(0x661758, Add, -2048),# units:Air Weapon  index:121    from 130 To 122
        SetMemory(0x66175C, Add, 62),# units:Air Weapon  index:124    from 29 To 91
        SetMemory(0x65FC20, Add, 65536),# units:Max Air Hits  index:10    from 0 To 1
        SetMemory(0x65FC38, Add, 1),# units:Max Air Hits  index:32    from 0 To 1
        SetMemory(0x65FC8C, Add, 256),# units:Max Air Hits  index:117    from 0 To 1
        SetMemory(0x6601A4, Add, 196608),# units:AI Internal  index:46    from 0 To 3
        SetMemory(0x6601B4, Add, 3),# units:AI Internal  index:60    from 0 To 3
        SetMemory(0x6601C0, Add, 3),# units:AI Internal  index:72    from 0 To 3
        SetMemory(0x6601D0, Add, 50331648),# units:AI Internal  index:91    from 0 To 3
        SetMemory(0x6601D4, Add, 3),# units:AI Internal  index:92    from 0 To 3
        SetMemory(0x664080, Add, 192),# units:Special Ability Flags  index:0    from 402718720 To 402718912
        SetMemory(0x664084, Add, 192),# units:Special Ability Flags  index:1    from 404816384 To 404816576
        SetMemory(0x664098, Add, 0),# units:Special Ability Flags  index:6    from 805306384 To 805306384
        SetMemory(0x66409C, Add, -4),# units:Special Ability Flags  index:7    from 1476460552 To 1476460548
        SetMemory(0x6640A8, Add, 128),# units:Special Ability Flags  index:10    from 402718784 To 402718912
        SetMemory(0x6640B4, Add, 4),# units:Special Ability Flags  index:13    from 402653184 To 402653188
        SetMemory(0x6640C0, Add, -384),# units:Special Ability Flags  index:16    from 404816448 To 404816064
        SetMemory(0x6640D0, Add, 128),# units:Special Ability Flags  index:20    from 402718784 To 402718912
        SetMemory(0x6640D8, Add, 536870912),# units:Special Ability Flags  index:22    from 1512079684 To 2048950596
        SetMemory(0x6640F8, Add, 4),# units:Special Ability Flags  index:30    from 1107296256 To 1107296260
        SetMemory(0x664100, Add, 128),# units:Special Ability Flags  index:32    from 402718720 To 402718848
        SetMemory(0x66417C, Add, 4),# units:Special Ability Flags  index:63    from 471859456 To 471859460
        SetMemory(0x664180, Add, -4),# units:Special Ability Flags  index:64    from 1476411400 To 1476411396
        SetMemory(0x6641A0, Add, -4),# units:Special Ability Flags  index:72    from 1543503876 To 1543503872
        SetMemory(0x6641D0, Add, -4194304),# units:Special Ability Flags  index:84    from 1480638468 To 1476444164
        SetMemory(0x6641E4, Add, 4194308),# units:Special Ability Flags  index:89    from 402718720 To 406913028
        SetMemory(0x6641E8, Add, 536872964),# units:Special Ability Flags  index:90    from 402718720 To 939591684
        SetMemory(0x6641EC, Add, 939591684),# units:Special Ability Flags  index:91    from 0 To 939591684
        SetMemory(0x6641F0, Add, 939591684),# units:Special Ability Flags  index:92    from 0 To 939591684
        SetMemory(0x6641F8, Add, 536870912),# units:Special Ability Flags  index:94    from 402718724 To 939589636
        SetMemory(0x664200, Add, 536870912),# units:Special Ability Flags  index:96    from 402718720 To 939589632
        SetMemory(0x66420C, Add, 128),# units:Special Ability Flags  index:99    from 404816448 To 404816576
        SetMemory(0x664210, Add, 128),# units:Special Ability Flags  index:100    from 404816448 To 404816576
        SetMemory(0x664228, Add, 4194816),# units:Special Ability Flags  index:106    from 3288338465 To 3292533281
        SetMemory(0x664230, Add, -736034815),# units:Special Ability Flags  index:108    from 1140850691 To 404815876
        SetMemory(0x664254, Add, -671088323),# units:Special Ability Flags  index:117    from 1140850691 To 469762368
        SetMemory(0x664258, Add, -201259007),# units:Special Ability Flags  index:118    from 1140850691 To 939591684
        SetMemory(0x66425C, Add, 2015363139),# units:Special Ability Flags  index:119    from 67108865 To 2082472004
        SetMemory(0x664260, Add, 536870910),# units:Special Ability Flags  index:120    from 1140850691 To 1677721601
        SetMemory(0x664264, Add, -201259007),# units:Special Ability Flags  index:121    from 1140850691 To 939591684
        SetMemory(0x664278, Add, 4194816),# units:Special Ability Flags  index:126    from 1140850689 To 1145045505
        SetMemory(0x66427C, Add, 4194816),# units:Special Ability Flags  index:127    from 1140850689 To 1145045505
        SetMemory(0x664288, Add, 4194816),# units:Special Ability Flags  index:130    from 67174561 To 71369377
        SetMemory(0x66428C, Add, -128),# units:Special Ability Flags  index:131    from 2231439489 To 2231439361
        SetMemory(0x664290, Add, -128),# units:Special Ability Flags  index:132    from 2231439489 To 2231439361
        SetMemory(0x664294, Add, -128),# units:Special Ability Flags  index:133    from 2231439489 To 2231439361
        SetMemory(0x6642C4, Add, 536870911),# units:Special Ability Flags  index:145    from 83894401 To 620765312
        SetMemory(0x6642CC, Add, 4194688),# units:Special Ability Flags  index:147    from 84115585 To 88310273
        SetMemory(0x6642D0, Add, 4194688),# units:Special Ability Flags  index:148    from 84115585 To 88310273
        SetMemory(0x6642D8, Add, 4194688),# units:Special Ability Flags  index:150    from 84082817 To 88277505
        SetMemory(0x6642DC, Add, -128),# units:Special Ability Flags  index:151    from 84115585 To 84115457
        SetMemory(0x6642E0, Add, 4194688),# units:Special Ability Flags  index:152    from 84115585 To 88310273
        SetMemory(0x6642E4, Add, 855703427),# units:Special Ability Flags  index:153    from 83886209 To 939589636
        SetMemory(0x6642E8, Add, 4194816),# units:Special Ability Flags  index:154    from 3288338433 To 3292533249
        SetMemory(0x6642F8, Add, -520609665),# units:Special Ability Flags  index:158    from 1141374977 To 620765312
        SetMemory(0x664300, Add, 0),# units:Special Ability Flags  index:160    from 3288858625 To 3288858625
        SetMemory(0x664320, Add, 4194816),# units:Special Ability Flags  index:168    from 1140850689 To 1145045505
        SetMemory(0x664338, Add, 4194816),# units:Special Ability Flags  index:174    from 67108865 To 71303681
        SetMemory(0x66433C, Add, 4194816),# units:Special Ability Flags  index:175    from 67108865 To 71303681
        SetMemory(0x664340, Add, -536870912),# units:Special Ability Flags  index:176    from 603987969 To 67117057
        SetMemory(0x664344, Add, -536870912),# units:Special Ability Flags  index:177    from 603987969 To 67117057
        SetMemory(0x664348, Add, -536870912),# units:Special Ability Flags  index:178    from 603987969 To 67117057
        SetMemory(0x664370, Add, -536870912),# units:Special Ability Flags  index:188    from 603987969 To 67117057
        SetMemory(0x664374, Add, 4194816),# units:Special Ability Flags  index:189    from 1140850689 To 1145045505
        SetMemory(0x664378, Add, 4194816),# units:Special Ability Flags  index:190    from 1140850689 To 1145045505
        SetMemory(0x6643A0, Add, 4194816),# units:Special Ability Flags  index:200    from 1140850689 To 1145045505
        SetMemory(0x6643A4, Add, 4194816),# units:Special Ability Flags  index:201    from 84115585 To 88310401
        SetMemory(0x6643EC, Add, 4),# units:Special Ability Flags  index:219    from 545261568 To 545261572
        SetMemory(0x662DB8, Add, 3),# units:Target Acquisition Range  index:0    from 4 To 7
        SetMemory(0x662DB8, Add, 0),# units:Target Acquisition Range  index:1    from 7 To 7
        SetMemory(0x662DB8, Add, 65536),# units:Target Acquisition Range  index:2    from 5 To 6
        SetMemory(0x662DBC, Add, 117440512),# units:Target Acquisition Range  index:7    from 1 To 8
        SetMemory(0x662DC0, Add, 196608),# units:Target Acquisition Range  index:10    from 3 To 6
        SetMemory(0x662DC4, Add, 1536),# units:Target Acquisition Range  index:13    from 3 To 9
        SetMemory(0x662DC4, Add, 50331648),# units:Target Acquisition Range  index:15    from 0 To 3
        SetMemory(0x662DC8, Add, 1),# units:Target Acquisition Range  index:16    from 6 To 7
        SetMemory(0x662DD8, Add, 2),# units:Target Acquisition Range  index:32    from 3 To 5
        SetMemory(0x662DE4, Add, 262144),# units:Target Acquisition Range  index:46    from 0 To 4
        SetMemory(0x662E00, Add, 2),# units:Target Acquisition Range  index:72    from 8 To 10
        SetMemory(0x662E10, Add, 458752),# units:Target Acquisition Range  index:90    from 0 To 7
        SetMemory(0x662E10, Add, -16777216),# units:Target Acquisition Range  index:91    from 8 To 7
        SetMemory(0x662E14, Add, 3),# units:Target Acquisition Range  index:92    from 4 To 7
        SetMemory(0x662E14, Add, 50331648),# units:Target Acquisition Range  index:95    from 0 To 3
        SetMemory(0x662E2C, Add, 768),# units:Target Acquisition Range  index:117    from 0 To 3
        SetMemory(0x662E2C, Add, 458752),# units:Target Acquisition Range  index:118    from 0 To 7
        SetMemory(0x662E30, Add, 1792),# units:Target Acquisition Range  index:121    from 0 To 7
        SetMemory(0x662E50, Add, 1792),# units:Target Acquisition Range  index:153    from 0 To 7
        SetMemory(0x663238, Add, 4),# units:Sight Range  index:0    from 7 To 11
        SetMemory(0x663238, Add, 512),# units:Sight Range  index:1    from 9 To 11
        SetMemory(0x66323C, Add, 67108864),# units:Sight Range  index:7    from 7 To 11
        SetMemory(0x663240, Add, 262144),# units:Sight Range  index:10    from 7 To 11
        SetMemory(0x66324C, Add, 2),# units:Sight Range  index:20    from 7 To 9
        SetMemory(0x663258, Add, 1),# units:Sight Range  index:32    from 7 To 8
        SetMemory(0x663290, Add, 196608),# units:Sight Range  index:90    from 7 To 10
        SetMemory(0x663290, Add, 33554432),# units:Sight Range  index:91    from 8 To 10
        SetMemory(0x663294, Add, 3),# units:Sight Range  index:92    from 7 To 10
        SetMemory(0x663298, Add, 16777216),# units:Sight Range  index:99    from 10 To 11
        SetMemory(0x6632AC, Add, 131072),# units:Sight Range  index:118    from 8 To 10
        SetMemory(0x6632B0, Add, 512),# units:Sight Range  index:121    from 8 To 10
        SetMemory(0x6632D0, Add, 768),# units:Sight Range  index:153    from 7 To 10
        SetMemory(0x663618, Add, -6),# units:Armor Upgrade  index:72    from 6 To 0
        SetMemory(0x66362C, Add, -1006632960),# units:Armor Upgrade  index:95    from 60 To 0
        SetMemory(0x66363C, Add, -54),# units:Armor Upgrade  index:108    from 60 To 6
        SetMemory(0x663644, Add, -14080),# units:Armor Upgrade  index:117    from 60 To 5
        SetMemory(0x66364C, Add, -15360),# units:Armor Upgrade  index:125    from 60 To 0
        SetMemory(0x662188, Add, -16777216),# units:Unit Size  index:11    from 3 To 2
        SetMemory(0x6621C4, Add, -256),# units:Unit Size  index:69    from 3 To 2
        SetMemory(0x6621D8, Add, 65536),# units:Unit Size  index:90    from 1 To 2
        SetMemory(0x6621F4, Add, -65536),# units:Unit Size  index:118    from 3 To 2
        SetMemory(0x6621F8, Add, -256),# units:Unit Size  index:121    from 3 To 2
        SetMemory(0x662218, Add, 512),# units:Unit Size  index:153    from 0 To 2
        SetMemory(0x662230, Add, 1),# units:Unit Size  index:176    from 0 To 1
        SetMemory(0x662230, Add, 256),# units:Unit Size  index:177    from 0 To 1
        SetMemory(0x662230, Add, 65536),# units:Unit Size  index:178    from 0 To 1
        SetMemory(0x66223C, Add, 1),# units:Unit Size  index:188    from 0 To 1
        SetMemory(0x65FEC8, Add, 768),# units:Armor  index:1    from 0 To 3
        SetMemory(0x65FF20, Add, 65536),# units:Armor  index:90    from 0 To 1
        SetMemory(0x66209C, Add, -67108864),# units:Right-click Action  index:7    from 5 To 1
        SetMemory(0x6620A0, Add, -16777216),# units:Right-click Action  index:11    from 2 To 1
        SetMemory(0x6620A4, Add, -16777216),# units:Right-click Action  index:15    from 2 To 1
        SetMemory(0x6620B8, Add, -65536),# units:Right-click Action  index:34    from 2 To 1
        SetMemory(0x6620C4, Add, -65536),# units:Right-click Action  index:46    from 2 To 1
        SetMemory(0x6620CC, Add, -1),# units:Right-click Action  index:52    from 2 To 1
        SetMemory(0x6620D0, Add, -256),# units:Right-click Action  index:57    from 2 To 1
        SetMemory(0x6620D4, Add, -16777216),# units:Right-click Action  index:63    from 2 To 1
        SetMemory(0x6620D8, Add, -3),# units:Right-click Action  index:64    from 4 To 1
        SetMemory(0x6620DC, Add, -256),# units:Right-click Action  index:69    from 2 To 1
        SetMemory(0x6620EC, Add, -1),# units:Right-click Action  index:84    from 2 To 1
        SetMemory(0x6620F0, Add, -256),# units:Right-click Action  index:89    from 2 To 1
        SetMemory(0x6620F0, Add, -65536),# units:Right-click Action  index:90    from 2 To 1
        SetMemory(0x6620F0, Add, 16777216),# units:Right-click Action  index:91    from 0 To 1
        SetMemory(0x6620F4, Add, 1),# units:Right-click Action  index:92    from 0 To 1
        SetMemory(0x6620F4, Add, -256),# units:Right-click Action  index:93    from 2 To 1
        SetMemory(0x6620F4, Add, -131072),# units:Right-click Action  index:94    from 2 To 0
        SetMemory(0x6620F4, Add, -16777216),# units:Right-click Action  index:95    from 2 To 1
        SetMemory(0x6620F8, Add, -1),# units:Right-click Action  index:96    from 2 To 1
        SetMemory(0x662104, Add, 1),# units:Right-click Action  index:108    from 0 To 1
        SetMemory(0x66210C, Add, 256),# units:Right-click Action  index:117    from 0 To 1
        SetMemory(0x66210C, Add, 65536),# units:Right-click Action  index:118    from 0 To 1
        SetMemory(0x66210C, Add, 16777216),# units:Right-click Action  index:119    from 0 To 1
        SetMemory(0x662110, Add, 256),# units:Right-click Action  index:121    from 0 To 1
        SetMemory(0x662130, Add, 256),# units:Right-click Action  index:153    from 0 To 1
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FD4, Add, -70),# units:Ready Sound  index:10    from 295 To 225
        SetMemory(0x662000, Add, -20),# units:Ready Sound  index:32    from 295 To 275
        SetMemory(0x662050, Add, -33),# units:Ready Sound  index:72    from 582 To 549
        SetMemory(0x662070, Add, 47710208),# units:Ready Sound  index:89    from 0 To 728
        SetMemory(0x65FFB0, Add, 175),# units:What Sound Start  index:0    from 287 To 462
        SetMemory(0x65FFB0, Add, 15204352),# units:What Sound Start  index:1    from 230 To 462
        SetMemory(0x65FFC4, Add, -69),# units:What Sound Start  index:10    from 299 To 230
        SetMemory(0x65FFF0, Add, -12),# units:What Sound Start  index:32    from 299 To 287
        SetMemory(0x660040, Add, -28),# units:What Sound Start  index:72    from 587 To 559
        SetMemory(0x660060, Add, 44498944),# units:What Sound Start  index:89    from 54 To 733
        SetMemory(0x660064, Add, -46),# units:What Sound Start  index:90    from 46 To 0
        SetMemory(0x66006C, Add, 9699328),# units:What Sound Start  index:95    from 50 To 198
        SetMemory(0x660074, Add, -34537472),# units:What Sound Start  index:99    from 989 To 462
        SetMemory(0x660078, Add, 232),# units:What Sound Start  index:100    from 230 To 462
        SetMemory(0x660098, Add, 11993088),# units:What Sound Start  index:117    from 390 To 573
        SetMemory(0x66009C, Add, -398),# units:What Sound Start  index:118    from 398 To 0
        SetMemory(0x6600A0, Add, -26279936),# units:What Sound Start  index:121    from 401 To 0
        SetMemory(0x6600E0, Add, -983040),# units:What Sound Start  index:153    from 15 To 0
        SetMemory(0x662BF0, Add, 175),# units:What Sound End  index:0    from 290 To 465
        SetMemory(0x662BF0, Add, 15204352),# units:What Sound End  index:1    from 233 To 465
        SetMemory(0x662C04, Add, -69),# units:What Sound End  index:10    from 302 To 233
        SetMemory(0x662C30, Add, -12),# units:What Sound End  index:32    from 302 To 290
        SetMemory(0x662C80, Add, -28),# units:What Sound End  index:72    from 590 To 562
        SetMemory(0x662CA0, Add, 44564480),# units:What Sound End  index:89    from 56 To 736
        SetMemory(0x662CA4, Add, -48),# units:What Sound End  index:90    from 48 To 0
        SetMemory(0x662CAC, Add, 9764864),# units:What Sound End  index:95    from 52 To 201
        SetMemory(0x662CB4, Add, -34537472),# units:What Sound End  index:99    from 992 To 465
        SetMemory(0x662CB8, Add, 232),# units:What Sound End  index:100    from 233 To 465
        SetMemory(0x662CD8, Add, 12189696),# units:What Sound End  index:117    from 390 To 576
        SetMemory(0x662CDC, Add, -398),# units:What Sound End  index:118    from 398 To 0
        SetMemory(0x662CE0, Add, -26279936),# units:What Sound End  index:121    from 401 To 0
        SetMemory(0x662D20, Add, -983040),# units:What Sound End  index:153    from 15 To 0
        SetMemory(0x663B38, Add, 177),# units:Piss Sound Start  index:0    from 280 To 457
        SetMemory(0x663B38, Add, 15138816),# units:Piss Sound Start  index:1    from 226 To 457
        SetMemory(0x663B4C, Add, -77),# units:Piss Sound Start  index:10    from 303 To 226
        SetMemory(0x663B78, Add, -23),# units:Piss Sound Start  index:32    from 303 To 280
        SetMemory(0x663BC8, Add, -29),# units:Piss Sound Start  index:72    from 583 To 554
        SetMemory(0x663BE8, Add, 47775744),# units:Piss Sound Start  index:89    from 0 To 729
        SetMemory(0x663BF4, Add, 12648448),# units:Piss Sound Start  index:95    from 0 To 193
        SetMemory(0x663BFC, Add, -34275328),# units:Piss Sound Start  index:99    from 980 To 457
        SetMemory(0x663C00, Add, 231),# units:Piss Sound Start  index:100    from 226 To 457
        SetMemory(0x661EE8, Add, 175),# units:Piss Sound End  index:0    from 286 To 461
        SetMemory(0x661EE8, Add, 15204352),# units:Piss Sound End  index:1    from 229 To 461
        SetMemory(0x661EFC, Add, -80),# units:Piss Sound End  index:10    from 309 To 229
        SetMemory(0x661F28, Add, -23),# units:Piss Sound End  index:32    from 309 To 286
        SetMemory(0x661F78, Add, -28),# units:Piss Sound End  index:72    from 586 To 558
        SetMemory(0x661F98, Add, 47972352),# units:Piss Sound End  index:89    from 0 To 732
        SetMemory(0x661FA4, Add, 12910592),# units:Piss Sound End  index:95    from 0 To 197
        SetMemory(0x661FAC, Add, -34537472),# units:Piss Sound End  index:99    from 988 To 461
        SetMemory(0x661FB0, Add, 232),# units:Piss Sound End  index:100    from 229 To 461
        SetMemory(0x663C10, Add, 175),# units:Yes Sound Start  index:0    from 291 To 466
        SetMemory(0x663C10, Add, 15204352),# units:Yes Sound Start  index:1    from 234 To 466
        SetMemory(0x663C24, Add, -76),# units:Yes Sound Start  index:10    from 310 To 234
        SetMemory(0x663C50, Add, -19),# units:Yes Sound Start  index:32    from 310 To 291
        SetMemory(0x663CA0, Add, -28),# units:Yes Sound Start  index:72    from 591 To 563
        SetMemory(0x663CC0, Add, 48300032),# units:Yes Sound Start  index:89    from 0 To 737
        SetMemory(0x663CCC, Add, 13238272),# units:Yes Sound Start  index:95    from 0 To 202
        SetMemory(0x663CD4, Add, -34537472),# units:Yes Sound Start  index:99    from 993 To 466
        SetMemory(0x663CD8, Add, 232),# units:Yes Sound Start  index:100    from 234 To 466
        SetMemory(0x661440, Add, 175),# units:Yes Sound End  index:0    from 294 To 469
        SetMemory(0x661440, Add, 15204352),# units:Yes Sound End  index:1    from 237 To 469
        SetMemory(0x661454, Add, -76),# units:Yes Sound End  index:10    from 313 To 237
        SetMemory(0x661480, Add, -19),# units:Yes Sound End  index:32    from 313 To 294
        SetMemory(0x6614D0, Add, -29),# units:Yes Sound End  index:72    from 594 To 565
        SetMemory(0x6614F0, Add, 48496640),# units:Yes Sound End  index:89    from 0 To 740
        SetMemory(0x6614FC, Add, 13500416),# units:Yes Sound End  index:95    from 0 To 206
        SetMemory(0x661504, Add, -34537472),# units:Yes Sound End  index:99    from 996 To 469
        SetMemory(0x661508, Add, 232),# units:Yes Sound End  index:100    from 237 To 469
        SetMemory(0x6629C8, Add, -31),# units:StarEdit Placement Box Width  index:90    from 32 To 1
        SetMemory(0x6629CC, Add, -31),# units:StarEdit Placement Box Width  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -31),# units:StarEdit Placement Box Width  index:92    from 32 To 1
        SetMemory(0x6629E0, Add, -31),# units:StarEdit Placement Box Width  index:96    from 32 To 1
        SetMemory(0x662A10, Add, -63),# units:StarEdit Placement Box Width  index:108    from 64 To 1
        SetMemory(0x662A34, Add, -32),# units:StarEdit Placement Box Width  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -63),# units:StarEdit Placement Box Width  index:118    from 64 To 1
        SetMemory(0x662A3C, Add, -95),# units:StarEdit Placement Box Width  index:119    from 96 To 1
        SetMemory(0x662A40, Add, -63),# units:StarEdit Placement Box Width  index:120    from 64 To 1
        SetMemory(0x662A44, Add, -95),# units:StarEdit Placement Box Width  index:121    from 96 To 1
        SetMemory(0x662A6C, Add, -127),# units:StarEdit Placement Box Width  index:131    from 128 To 1
        SetMemory(0x662A70, Add, -127),# units:StarEdit Placement Box Width  index:132    from 128 To 1
        SetMemory(0x662A74, Add, -127),# units:StarEdit Placement Box Width  index:133    from 128 To 1
        SetMemory(0x662AA4, Add, -95),# units:StarEdit Placement Box Width  index:145    from 96 To 1
        SetMemory(0x662AC4, Add, -31),# units:StarEdit Placement Box Width  index:153    from 32 To 1
        SetMemory(0x662AD8, Add, -127),# units:StarEdit Placement Box Width  index:158    from 128 To 1
        SetMemory(0x662B54, Add, -95),# units:StarEdit Placement Box Width  index:189    from 96 To 1
        SetMemory(0x662BB8, Add, -128),# units:StarEdit Placement Box Width  index:214    from 128 To 0
        SetMemory(0x6629C8, Add, -2031616),# units:StarEdit Placement Box Height  index:90    from 32 To 1
        SetMemory(0x6629CC, Add, -2031616),# units:StarEdit Placement Box Height  index:91    from 32 To 1
        SetMemory(0x6629D0, Add, -2031616),# units:StarEdit Placement Box Height  index:92    from 32 To 1
        SetMemory(0x6629E0, Add, -2031616),# units:StarEdit Placement Box Height  index:96    from 32 To 1
        SetMemory(0x662A10, Add, -4128768),# units:StarEdit Placement Box Height  index:108    from 64 To 1
        SetMemory(0x662A34, Add, -2097152),# units:StarEdit Placement Box Height  index:117    from 64 To 32
        SetMemory(0x662A38, Add, -4128768),# units:StarEdit Placement Box Height  index:118    from 64 To 1
        SetMemory(0x662A3C, Add, -4128768),# units:StarEdit Placement Box Height  index:119    from 64 To 1
        SetMemory(0x662A40, Add, -4128768),# units:StarEdit Placement Box Height  index:120    from 64 To 1
        SetMemory(0x662A44, Add, -6225920),# units:StarEdit Placement Box Height  index:121    from 96 To 1
        SetMemory(0x662A6C, Add, -6225920),# units:StarEdit Placement Box Height  index:131    from 96 To 1
        SetMemory(0x662A70, Add, -6225920),# units:StarEdit Placement Box Height  index:132    from 96 To 1
        SetMemory(0x662A74, Add, -6225920),# units:StarEdit Placement Box Height  index:133    from 96 To 1
        SetMemory(0x662AA4, Add, -6225920),# units:StarEdit Placement Box Height  index:145    from 96 To 1
        SetMemory(0x662AC4, Add, -2031616),# units:StarEdit Placement Box Height  index:153    from 32 To 1
        SetMemory(0x662AD8, Add, -6225920),# units:StarEdit Placement Box Height  index:158    from 96 To 1
        SetMemory(0x662B54, Add, -4128768),# units:StarEdit Placement Box Height  index:189    from 64 To 1
        SetMemory(0x662BB8, Add, -6291456),# units:StarEdit Placement Box Height  index:214    from 96 To 0
        SetMemory(0x6626E8, Add, -127),# units:Addon Horizontal (X) Position  index:2    from 128 To 1
        SetMemory(0x662710, Add, -128),# units:Addon Horizontal (X) Position  index:12    from 128 To 0
        SetMemory(0x6626E8, Add, -2031616),# units:Addon Vertical (Y) Position  index:2    from 32 To 1
        SetMemory(0x662710, Add, -2097152),# units:Addon Vertical (Y) Position  index:12    from 32 To 0
        SetMemory(0x661A08, Add, -28),# units:Unit Size Left  index:72    from 32 To 4
        SetMemory(0x661A98, Add, -15),# units:Unit Size Left  index:90    from 16 To 1
        SetMemory(0x661AA0, Add, -14),# units:Unit Size Left  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -14),# units:Unit Size Left  index:92    from 15 To 1
        SetMemory(0x661AC8, Add, -15),# units:Unit Size Left  index:96    from 16 To 1
        SetMemory(0x661B28, Add, -33),# units:Unit Size Left  index:108    from 37 To 4
        SetMemory(0x661B70, Add, -31),# units:Unit Size Left  index:117    from 47 To 16
        SetMemory(0x661B78, Add, -46),# units:Unit Size Left  index:118    from 47 To 1
        SetMemory(0x661B80, Add, -46),# units:Unit Size Left  index:119    from 48 To 2
        SetMemory(0x661B90, Add, -47),# units:Unit Size Left  index:121    from 48 To 1
        SetMemory(0x661C50, Add, -47),# units:Unit Size Left  index:145    from 48 To 1
        SetMemory(0x661C90, Add, -15),# units:Unit Size Left  index:153    from 16 To 1
        SetMemory(0x661CB8, Add, -63),# units:Unit Size Left  index:158    from 64 To 1
        SetMemory(0x661DB0, Add, -47),# units:Unit Size Left  index:189    from 48 To 1
        SetMemory(0x661E78, Add, -47),# units:Unit Size Left  index:214    from 48 To 1
        SetMemory(0x661E80, Add, -12),# units:Unit Size Left  index:215    from 16 To 4
        SetMemory(0x661A08, Add, -1835008),# units:Unit Size Up  index:72    from 32 To 4
        SetMemory(0x661A98, Add, -983040),# units:Unit Size Up  index:90    from 16 To 1
        SetMemory(0x661AA0, Add, -917504),# units:Unit Size Up  index:91    from 15 To 1
        SetMemory(0x661AA8, Add, -917504),# units:Unit Size Up  index:92    from 15 To 1
        SetMemory(0x661AC8, Add, -983040),# units:Unit Size Up  index:96    from 16 To 1
        SetMemory(0x661B28, Add, -786432),# units:Unit Size Up  index:108    from 16 To 4
        SetMemory(0x661B70, Add, -524288),# units:Unit Size Up  index:117    from 24 To 16
        SetMemory(0x661B78, Add, -1507328),# units:Unit Size Up  index:118    from 24 To 1
        SetMemory(0x661B80, Add, -1966080),# units:Unit Size Up  index:119    from 32 To 2
        SetMemory(0x661B90, Add, -3080192),# units:Unit Size Up  index:121    from 48 To 1
        SetMemory(0x661C50, Add, -3080192),# units:Unit Size Up  index:145    from 48 To 1
        SetMemory(0x661C90, Add, -983040),# units:Unit Size Up  index:153    from 16 To 1
        SetMemory(0x661CB8, Add, -3080192),# units:Unit Size Up  index:158    from 48 To 1
        SetMemory(0x661DB0, Add, -2031616),# units:Unit Size Up  index:189    from 32 To 1
        SetMemory(0x661E78, Add, -2031616),# units:Unit Size Up  index:214    from 32 To 1
        SetMemory(0x661E80, Add, -786432),# units:Unit Size Up  index:215    from 16 To 4
        SetMemory(0x661A0C, Add, -27),# units:Unit Size Right  index:72    from 31 To 4
        SetMemory(0x661A9C, Add, -14),# units:Unit Size Right  index:90    from 15 To 1
        SetMemory(0x661AA4, Add, -15),# units:Unit Size Right  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -15),# units:Unit Size Right  index:92    from 16 To 1
        SetMemory(0x661ACC, Add, -14),# units:Unit Size Right  index:96    from 15 To 1
        SetMemory(0x661B2C, Add, -27),# units:Unit Size Right  index:108    from 31 To 4
        SetMemory(0x661B74, Add, -13),# units:Unit Size Right  index:117    from 28 To 15
        SetMemory(0x661B7C, Add, -27),# units:Unit Size Right  index:118    from 28 To 1
        SetMemory(0x661B84, Add, -45),# units:Unit Size Right  index:119    from 47 To 2
        SetMemory(0x661B94, Add, -46),# units:Unit Size Right  index:121    from 47 To 1
        SetMemory(0x661C54, Add, -46),# units:Unit Size Right  index:145    from 47 To 1
        SetMemory(0x661C94, Add, -14),# units:Unit Size Right  index:153    from 15 To 1
        SetMemory(0x661CBC, Add, -62),# units:Unit Size Right  index:158    from 63 To 1
        SetMemory(0x661DB4, Add, -46),# units:Unit Size Right  index:189    from 47 To 1
        SetMemory(0x661E7C, Add, -47),# units:Unit Size Right  index:214    from 48 To 1
        SetMemory(0x661E84, Add, -11),# units:Unit Size Right  index:215    from 15 To 4
        SetMemory(0x661A0C, Add, -1769472),# units:Unit Size Down  index:72    from 31 To 4
        SetMemory(0x661A9C, Add, -917504),# units:Unit Size Down  index:90    from 15 To 1
        SetMemory(0x661AA4, Add, -983040),# units:Unit Size Down  index:91    from 16 To 1
        SetMemory(0x661AAC, Add, -983040),# units:Unit Size Down  index:92    from 16 To 1
        SetMemory(0x661ACC, Add, -917504),# units:Unit Size Down  index:96    from 15 To 1
        SetMemory(0x661B2C, Add, -1376256),# units:Unit Size Down  index:108    from 25 To 4
        SetMemory(0x661B74, Add, -458752),# units:Unit Size Down  index:117    from 22 To 15
        SetMemory(0x661B7C, Add, -1376256),# units:Unit Size Down  index:118    from 22 To 1
        SetMemory(0x661B84, Add, -1900544),# units:Unit Size Down  index:119    from 31 To 2
        SetMemory(0x661B94, Add, -3014656),# units:Unit Size Down  index:121    from 47 To 1
        SetMemory(0x661C54, Add, -3014656),# units:Unit Size Down  index:145    from 47 To 1
        SetMemory(0x661C94, Add, -917504),# units:Unit Size Down  index:153    from 15 To 1
        SetMemory(0x661CBC, Add, -3014656),# units:Unit Size Down  index:158    from 47 To 1
        SetMemory(0x661DB4, Add, -1966080),# units:Unit Size Down  index:189    from 31 To 1
        SetMemory(0x661E7C, Add, -2031616),# units:Unit Size Down  index:214    from 32 To 1
        SetMemory(0x661E84, Add, -720896),# units:Unit Size Down  index:215    from 15 To 4
        SetMemory(0x662F88, Add, 12),# units:Portrait  index:0    from 0 To 12
        SetMemory(0x662F88, Add, 720896),# units:Portrait  index:1    from 1 To 12
        SetMemory(0x662F9C, Add, -1),# units:Portrait  index:10    from 2 To 1
        SetMemory(0x662FA4, Add, -851968),# units:Portrait  index:15    from 15 To 2
        SetMemory(0x662FC8, Add, -2),# units:Portrait  index:32    from 2 To 0
        SetMemory(0x663018, Add, -1),# units:Portrait  index:72    from 47 To 46
        SetMemory(0x663030, Add, -7),# units:Portrait  index:84    from 55 To 48
        SetMemory(0x663038, Add, -851968),# units:Portrait  index:89    from 62 To 49
        SetMemory(0x66303C, Add, 65472),# units:Portrait  index:90    from 63 To 65535
        SetMemory(0x663044, Add, -4063232),# units:Portrait  index:95    from 64 To 2
        SetMemory(0x66304C, Add, -5373952),# units:Portrait  index:99    from 94 To 12
        SetMemory(0x663050, Add, -81),# units:Portrait  index:100    from 93 To 12
        SetMemory(0x663060, Add, 43),# units:Portrait  index:108    from 17 To 60
        SetMemory(0x663070, Add, 1703936),# units:Portrait  index:117    from 17 To 43
        SetMemory(0x663074, Add, 65518),# units:Portrait  index:118    from 17 To 65535
        SetMemory(0x663078, Add, 4293787648),# units:Portrait  index:121    from 17 To 65535
        SetMemory(0x6630B8, Add, 4294901760),# units:Portrait  index:153    from 0 To 65535
        SetMemory(0x6638EC, Add, -100),# units:Mineral Cost  index:50    from 100 To 0
        SetMemory(0x6638EC, Add, -13107200),# units:Mineral Cost  index:51    from 200 To 0
        SetMemory(0x663920, Add, -13107200),# units:Mineral Cost  index:77    from 200 To 0
        SetMemory(0x663924, Add, -300),# units:Mineral Cost  index:78    from 300 To 0
        SetMemory(0x66393C, Add, 99),# units:Mineral Cost  index:90    from 1 To 100
        SetMemory(0x663974, Add, 50),# units:Mineral Cost  index:118    from 50 To 100
        SetMemory(0x663978, Add, 6488064),# units:Mineral Cost  index:121    from 1 To 100
        SetMemory(0x6639B8, Add, 6488064),# units:Mineral Cost  index:153    from 1 To 100
        SetMemory(0x65FD64, Add, -50),# units:Vespene Cost  index:50    from 50 To 0
        SetMemory(0x65FD64, Add, -19660800),# units:Vespene Cost  index:51    from 300 To 0
        SetMemory(0x65FD9C, Add, -100),# units:Vespene Cost  index:78    from 100 To 0
        SetMemory(0x65FDB4, Add, 99),# units:Vespene Cost  index:90    from 1 To 100
        SetMemory(0x65FDEC, Add, 50),# units:Vespene Cost  index:118    from 50 To 100
        SetMemory(0x65FDF0, Add, 6488064),# units:Vespene Cost  index:121    from 1 To 100
        SetMemory(0x65FE30, Add, 6488064),# units:Vespene Cost  index:153    from 1 To 100
        SetMemory(0x660470, Add, -27459584),# units:Build Time  index:37    from 420 To 1
        SetMemory(0x660474, Add, -419),# units:Build Time  index:38    from 420 To 1
        SetMemory(0x660474, Add, -58916864),# units:Build Time  index:39    from 900 To 1
        SetMemory(0x660478, Add, -19595264),# units:Build Time  index:41    from 300 To 1
        SetMemory(0x66047C, Add, -599),# units:Build Time  index:42    from 600 To 1
        SetMemory(0x66047C, Add, -39256064),# units:Build Time  index:43    from 600 To 1
        SetMemory(0x660480, Add, -599),# units:Build Time  index:44    from 600 To 1
        SetMemory(0x660480, Add, -49086464),# units:Build Time  index:45    from 750 To 1
        SetMemory(0x660484, Add, -749),# units:Build Time  index:46    from 750 To 1
        SetMemory(0x660484, Add, -29425664),# units:Build Time  index:47    from 450 To 1
        SetMemory(0x6604C0, Add, -78577664),# units:Build Time  index:77    from 1200 To 1
        SetMemory(0x6604C4, Add, -1499),# units:Build Time  index:78    from 1500 To 1
        SetMemory(0x6604DC, Add, 599),# units:Build Time  index:90    from 1 To 600
        SetMemory(0x660518, Add, 39256064),# units:Build Time  index:121    from 1 To 600
        SetMemory(0x66052C, Add, -116981760),# units:Build Time  index:131    from 1800 To 15
        SetMemory(0x660530, Add, -1485),# units:Build Time  index:132    from 1500 To 15
        SetMemory(0x660530, Add, -116981760),# units:Build Time  index:133    from 1800 To 15
        SetMemory(0x660534, Add, -585),# units:Build Time  index:134    from 600 To 15
        SetMemory(0x660534, Add, -38338560),# units:Build Time  index:135    from 600 To 15
        SetMemory(0x660538, Add, -885),# units:Build Time  index:136    from 900 To 15
        SetMemory(0x660538, Add, -116981760),# units:Build Time  index:137    from 1800 To 15
        SetMemory(0x66053C, Add, -885),# units:Build Time  index:138    from 900 To 15
        SetMemory(0x66053C, Add, -38338560),# units:Build Time  index:139    from 600 To 15
        SetMemory(0x660540, Add, -1185),# units:Build Time  index:140    from 1200 To 15
        SetMemory(0x660540, Add, -116981760),# units:Build Time  index:141    from 1800 To 15
        SetMemory(0x660544, Add, -1185),# units:Build Time  index:142    from 1200 To 15
        SetMemory(0x660544, Add, -18677760),# units:Build Time  index:143    from 300 To 15
        SetMemory(0x660548, Add, -285),# units:Build Time  index:144    from 300 To 15
        SetMemory(0x66054C, Add, -285),# units:Build Time  index:146    from 300 To 15
        SetMemory(0x660550, Add, -38338560),# units:Build Time  index:149    from 600 To 15
        SetMemory(0x660558, Add, 39256064),# units:Build Time  index:153    from 1 To 600
        SetMemory(0x6637E8, Add, -2),# units:Staredit Group Flags  index:72    from 12 To 10
        SetMemory(0x6637F0, Add, -131072),# units:Staredit Group Flags  index:82    from 12 To 10
        SetMemory(0x6637F8, Add, -31744),# units:Staredit Group Flags  index:89    from 136 To 12
        SetMemory(0x6637F8, Add, -8323072),# units:Staredit Group Flags  index:90    from 136 To 9
        SetMemory(0x6637FC, Add, -2113929216),# units:Staredit Group Flags  index:95    from 136 To 10
        SetMemory(0x66380C, Add, -8),# units:Staredit Group Flags  index:108    from 18 To 10
        SetMemory(0x663814, Add, -1536),# units:Staredit Group Flags  index:117    from 18 To 12
        SetMemory(0x663814, Add, -524288),# units:Staredit Group Flags  index:118    from 18 To 10
        SetMemory(0x663814, Add, -301989888),# units:Staredit Group Flags  index:119    from 18 To 0
        SetMemory(0x663818, Add, -2048),# units:Staredit Group Flags  index:121    from 18 To 10
        SetMemory(0x663838, Add, -2048),# units:Staredit Group Flags  index:153    from 17 To 9
        SetMemory(0x66383C, Add, -196608),# units:Staredit Group Flags  index:158    from 20 To 17
        SetMemory(0x663874, Add, -1979711488),# units:Staredit Group Flags  index:215    from 128 To 10
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663D18, Add, -131072),# units:Supply Required  index:50    from 2 To 0
        SetMemory(0x663DBC, Add, 33554432),# units:Supply Required  index:215    from 0 To 2
        SetMemory(0x6609C0, Add, -2048),# units:Space Provided  index:57    from 8 To 0
        SetMemory(0x660A04, Add, 1024),# units:Space Provided  index:125    from 4 To 8
        SetMemory(0x6634F4, Add, -75),# units:Build Score  index:118    from 75 To 0
        SetMemory(0x663538, Add, -655360),# units:Build Score  index:153    from 10 To 0
        SetMemory(0x663F0C, Add, 65335),# units:Destroy Score  index:42    from 200 To 65535
        SetMemory(0x663F18, Add, 900),# units:Destroy Score  index:48    from 2600 To 3500
        SetMemory(0x663F24, Add, 45875200),# units:Destroy Score  index:55    from 1200 To 1900
        SetMemory(0x663F28, Add, 1000),# units:Destroy Score  index:56    from 2200 To 3200
        SetMemory(0x663F6C, Add, -10),# units:Destroy Score  index:90    from 10 To 0
        SetMemory(0x663F74, Add, -10),# units:Destroy Score  index:94    from 10 To 0
        SetMemory(0x663FA4, Add, -225),# units:Destroy Score  index:118    from 225 To 0
        SetMemory(0x663FE8, Add, -655360),# units:Destroy Score  index:153    from 10 To 0
        SetMemory(0x660738, Add, -16777216),# units:Broodwar Unit Flag  index:99    from 1 To 0
        SetMemory(0x66073C, Add, -1),# units:Broodwar Unit Flag  index:100    from 1 To 0
        SetMemory(0x66151C, Add, 0),# units:Staredit Availability Flags  index:3    from 463 To 463
        SetMemory(0x6615C8, Add, 65536),# units:Staredit Availability Flags  index:89    from 454 To 455
        SetMemory(0x6615CC, Add, 1),# units:Staredit Availability Flags  index:90    from 454 To 455
        SetMemory(0x6615CC, Add, 29818880),# units:Staredit Availability Flags  index:91    from 0 To 455
        SetMemory(0x6615D0, Add, 455),# units:Staredit Availability Flags  index:92    from 0 To 455
        SetMemory(0x6615D4, Add, 65536),# units:Staredit Availability Flags  index:95    from 454 To 455
        SetMemory(0x661600, Add, -524288),# units:Staredit Availability Flags  index:117    from 463 To 455
        SetMemory(0x661604, Add, -8),# units:Staredit Availability Flags  index:118    from 463 To 455
        SetMemory(0x661604, Add, 29818880),# units:Staredit Availability Flags  index:119    from 0 To 455
        SetMemory(0x661608, Add, 29818880),# units:Staredit Availability Flags  index:121    from 0 To 455
        SetMemory(0x661638, Add, 29818880),# units:Staredit Availability Flags  index:145    from 0 To 455
        SetMemory(0x661648, Add, 29818880),# units:Staredit Availability Flags  index:153    from 0 To 455
        SetMemory(0x661654, Add, 455),# units:Staredit Availability Flags  index:158    from 0 To 455
        SetMemory(0x6616C4, Add, 438),# units:Staredit Availability Flags  index:214    from 17 To 455
        SetMemory(0x6616D0, Add, 455),# units:Staredit Availability Flags  index:220    from 0 To 455
        SetMemory(0x6616D0, Add, 29818880),# units:Staredit Availability Flags  index:221    from 0 To 455
        SetMemory(0x6572F0, Add, 85),# weapons:Label  index:8    from 236 To 321
        SetMemory(0x657304, Add, 76480512),# weapons:Label  index:19    from 247 To 1414
        SetMemory(0x657368, Add, 1077),# weapons:Label  index:68    from 288 To 1365
        SetMemory(0x657390, Add, 2),# weapons:Label  index:88    from 304 To 306
        SetMemory(0x657390, Add, 61276160),# weapons:Label  index:89    from 305 To 1240
        SetMemory(0x657394, Add, 1060),# weapons:Label  index:90    from 306 To 1366
        SetMemory(0x657394, Add, -3276800),# weapons:Label  index:91    from 307 To 257
        SetMemory(0x657398, Add, 60620800),# weapons:Label  index:93    from 312 To 1237
        SetMemory(0x6573C8, Add, 85721088),# weapons:Label  index:117    from 229 To 1537
        SetMemory(0x6573CC, Add, 1309),# weapons:Label  index:118    from 229 To 1538
        SetMemory(0x6573D4, Add, 58523648),# weapons:Label  index:123    from 229 To 1122
        SetMemory(0x6573D8, Add, 894),# weapons:Label  index:124    from 229 To 1123
        SetMemory(0x6573D8, Add, 58654720),# weapons:Label  index:125    from 229 To 1124
        SetMemory(0x6573DC, Add, 896),# weapons:Label  index:126    from 229 To 1125
        SetMemory(0x6573DC, Add, 1900544),# weapons:Label  index:127    from 229 To 258
        SetMemory(0x656CB4, Add, 38),# weapons:Graphics  index:3    from 143 To 181
        SetMemory(0x656CB8, Add, 37),# weapons:Graphics  index:4    from 145 To 182
        SetMemory(0x656CC8, Add, 12),# weapons:Graphics  index:8    from 146 To 158
        SetMemory(0x656CDC, Add, 42),# weapons:Graphics  index:13    from 141 To 183
        SetMemory(0x656CE4, Add, 2),# weapons:Graphics  index:15    from 144 To 146
        SetMemory(0x656CEC, Add, 2),# weapons:Graphics  index:17    from 144 To 146
        SetMemory(0x656CF4, Add, 9),# weapons:Graphics  index:19    from 148 To 157
        SetMemory(0x656D0C, Add, -10),# weapons:Graphics  index:25    from 172 To 162
        SetMemory(0x656D14, Add, 31),# weapons:Graphics  index:27    from 150 To 181
        SetMemory(0x656D70, Add, 3),# weapons:Graphics  index:50    from 162 To 165
        SetMemory(0x656DA0, Add, 2),# weapons:Graphics  index:62    from 153 To 155
        SetMemory(0x656DDC, Add, -8),# weapons:Graphics  index:77    from 159 To 151
        SetMemory(0x656E08, Add, 17),# weapons:Graphics  index:88    from 143 To 160
        SetMemory(0x656E0C, Add, 62),# weapons:Graphics  index:89    from 144 To 206
        SetMemory(0x656E10, Add, 1),# weapons:Graphics  index:90    from 146 To 147
        SetMemory(0x656E14, Add, -4),# weapons:Graphics  index:91    from 152 To 148
        SetMemory(0x656E18, Add, 17),# weapons:Graphics  index:92    from 148 To 165
        SetMemory(0x656E1C, Add, 54),# weapons:Graphics  index:93    from 148 To 202
        SetMemory(0x656E7C, Add, 38),# weapons:Graphics  index:117    from 142 To 180
        SetMemory(0x656E80, Add, 27),# weapons:Graphics  index:118    from 142 To 169
        SetMemory(0x656E84, Add, 1),# weapons:Graphics  index:119    from 142 To 143
        SetMemory(0x656E88, Add, 10),# weapons:Graphics  index:120    from 142 To 152
        SetMemory(0x656E8C, Add, 8),# weapons:Graphics  index:121    from 142 To 150
        SetMemory(0x656E90, Add, 6),# weapons:Graphics  index:122    from 142 To 148
        SetMemory(0x656E98, Add, 6),# weapons:Graphics  index:124    from 142 To 148
        SetMemory(0x656E9C, Add, 3),# weapons:Graphics  index:125    from 142 To 145
        SetMemory(0x656EA0, Add, 34),# weapons:Graphics  index:126    from 142 To 176
        SetMemory(0x656EA4, Add, 36),# weapons:Graphics  index:127    from 142 To 178
        SetMemory(0x656EA8, Add, 6),# weapons:Graphics  index:128    from 142 To 148
        SetMemory(0x6579A4, Add, 0),# weapons:Target Flags  index:6    from 18 To 18
        SetMemory(0x6579A8, Add, 2),# weapons:Target Flags  index:8    from 1 To 3
        SetMemory(0x6579B4, Add, 131072),# weapons:Target Flags  index:15    from 1 To 3
        SetMemory(0x6579BC, Add, 0),# weapons:Target Flags  index:19    from 2 To 2
        SetMemory(0x6579C4, Add, 2),# weapons:Target Flags  index:22    from 1 To 3
        SetMemory(0x6579D0, Add, 131072),# weapons:Target Flags  index:29    from 1 To 3
        SetMemory(0x657A2C, Add, 2),# weapons:Target Flags  index:74    from 1 To 3
        SetMemory(0x657A30, Add, 2),# weapons:Target Flags  index:76    from 1 To 3
        SetMemory(0x657A48, Add, 2),# weapons:Target Flags  index:88    from 1 To 3
        SetMemory(0x657A48, Add, 131072),# weapons:Target Flags  index:89    from 1 To 3
        SetMemory(0x657A4C, Add, 131072),# weapons:Target Flags  index:91    from 1 To 3
        SetMemory(0x657A50, Add, 2),# weapons:Target Flags  index:92    from 1 To 3
        SetMemory(0x657A50, Add, 131072),# weapons:Target Flags  index:93    from 1 To 3
        SetMemory(0x657A54, Add, 2),# weapons:Target Flags  index:94    from 1 To 3
        SetMemory(0x657A5C, Add, 65536),# weapons:Target Flags  index:99    from 2 To 3
        SetMemory(0x657A60, Add, 2),# weapons:Target Flags  index:100    from 1 To 3
        SetMemory(0x657A64, Add, 131072),# weapons:Target Flags  index:103    from 1 To 3
        SetMemory(0x657A68, Add, 2),# weapons:Target Flags  index:104    from 1 To 3
        SetMemory(0x657A84, Add, 0),# weapons:Target Flags  index:119    from 3 To 3
        SetMemory(0x657A98, Add, 0),# weapons:Target Flags  index:128    from 3 To 3
        SetMemory(0x656A84, Add, -64),# weapons:Minimum Range  index:27    from 64 To 0
        SetMemory(0x656A88, Add, -64),# weapons:Minimum Range  index:28    from 64 To 0
        SetMemory(0x657470, Add, 32),# weapons:Maximum Range  index:0    from 128 To 160
        SetMemory(0x657478, Add, -32),# weapons:Maximum Range  index:2    from 224 To 192
        SetMemory(0x65747C, Add, 32),# weapons:Maximum Range  index:3    from 192 To 224
        SetMemory(0x6574A4, Add, 250),# weapons:Maximum Range  index:13    from 10 To 260
        SetMemory(0x6575D4, Add, 128),# weapons:Maximum Range  index:89    from 32 To 160
        SetMemory(0x657240, Add, 1024),# weapons:Damage Upgrade  index:113    from 7 To 11
        SetMemory(0x657244, Add, 13568),# weapons:Damage Upgrade  index:117    from 7 To 60
        SetMemory(0x657244, Add, 3473408),# weapons:Damage Upgrade  index:118    from 7 To 60
        SetMemory(0x65724C, Add, 117440512),# weapons:Damage Upgrade  index:127    from 7 To 14
        SetMemory(0x657250, Add, 7),# weapons:Damage Upgrade  index:128    from 7 To 14
        SetMemory(0x657288, Add, 0),# weapons:Weapon Type  index:50    from 2 To 2
        SetMemory(0x6572B0, Add, -33554432),# weapons:Weapon Type  index:91    from 3 To 1
        SetMemory(0x6572CC, Add, -16777216),# weapons:Weapon Type  index:119    from 3 To 2
        SetMemory(0x6572D0, Add, -512),# weapons:Weapon Type  index:121    from 3 To 1
        SetMemory(0x65667C, Add, -256),# weapons:Weapon Behavior  index:13    from 2 To 1
        SetMemory(0x656680, Add, 50331648),# weapons:Weapon Behavior  index:19    from 0 To 3
        SetMemory(0x656688, Add, -1280),# weapons:Weapon Behavior  index:25    from 5 To 0
        SetMemory(0x6566A0, Add, 65536),# weapons:Weapon Behavior  index:50    from 0 To 1
        SetMemory(0x6566AC, Add, -65536),# weapons:Weapon Behavior  index:62    from 2 To 1
        SetMemory(0x6566BC, Add, 256),# weapons:Weapon Behavior  index:77    from 1 To 2
        SetMemory(0x6566C8, Add, -1),# weapons:Weapon Behavior  index:88    from 2 To 1
        SetMemory(0x6566C8, Add, 256),# weapons:Weapon Behavior  index:89    from 1 To 2
        SetMemory(0x6566C8, Add, -16777216),# weapons:Weapon Behavior  index:91    from 2 To 1
        SetMemory(0x6566CC, Add, 1),# weapons:Weapon Behavior  index:92    from 0 To 1
        SetMemory(0x6566CC, Add, 768),# weapons:Weapon Behavior  index:93    from 0 To 3
        SetMemory(0x6566D4, Add, -83886080),# weapons:Weapon Behavior  index:103    from 8 To 3
        SetMemory(0x6566E4, Add, -256),# weapons:Weapon Behavior  index:117    from 2 To 1
        SetMemory(0x6566E4, Add, -65536),# weapons:Weapon Behavior  index:118    from 2 To 1
        SetMemory(0x6566E8, Add, -65536),# weapons:Weapon Behavior  index:122    from 2 To 1
        SetMemory(0x6566EC, Add, -1),# weapons:Weapon Behavior  index:124    from 2 To 1
        SetMemory(0x6566EC, Add, 393216),# weapons:Weapon Behavior  index:126    from 2 To 8
        SetMemory(0x6566EC, Add, -16777216),# weapons:Weapon Behavior  index:127    from 2 To 1
        SetMemory(0x6566F0, Add, -1),# weapons:Weapon Behavior  index:128    from 2 To 1
        SetMemory(0x657050, Add, -3271557120),# weapons:Remove After  index:19    from 255 To 60
        SetMemory(0x65709C, Add, -32512),# weapons:Remove After  index:93    from 255 To 128
        SetMemory(0x6566FC, Add, 2),# weapons:Explosion Type  index:4    from 1 To 3
        SetMemory(0x6566FC, Add, 65536),# weapons:Explosion Type  index:6    from 2 To 3
        SetMemory(0x656700, Add, 33554432),# weapons:Explosion Type  index:11    from 1 To 3
        SetMemory(0x656708, Add, 33554432),# weapons:Explosion Type  index:19    from 1 To 3
        SetMemory(0x656728, Add, 65536),# weapons:Explosion Type  index:50    from 2 To 3
        SetMemory(0x656728, Add, 16777216),# weapons:Explosion Type  index:51    from 2 To 3
        SetMemory(0x656890, Add, 60),# weapons:Inner Splash Range  index:4    from 0 To 60
        SetMemory(0x65689C, Add, 655360),# weapons:Inner Splash Range  index:11    from 0 To 10
        SetMemory(0x6568AC, Add, 3145728),# weapons:Inner Splash Range  index:19    from 0 To 48
        SetMemory(0x656938, Add, 327680),# weapons:Inner Splash Range  index:89    from 0 To 5
        SetMemory(0x6570D0, Add, 60),# weapons:Medium Splash Range  index:4    from 0 To 60
        SetMemory(0x6570DC, Add, 1310720),# weapons:Medium Splash Range  index:11    from 0 To 20
        SetMemory(0x6570EC, Add, 3145728),# weapons:Medium Splash Range  index:19    from 0 To 48
        SetMemory(0x657178, Add, 3276800),# weapons:Medium Splash Range  index:89    from 0 To 50
        SetMemory(0x657788, Add, 60),# weapons:Outer Splash Range  index:4    from 0 To 60
        SetMemory(0x657794, Add, 4587520),# weapons:Outer Splash Range  index:11    from 0 To 70
        SetMemory(0x6577A4, Add, 3145728),# weapons:Outer Splash Range  index:19    from 0 To 48
        SetMemory(0x6577B0, Add, 327680),# weapons:Outer Splash Range  index:25    from 25 To 30
        SetMemory(0x657830, Add, 6553600),# weapons:Outer Splash Range  index:89    from 0 To 100
        SetMemory(0x656EBC, Add, 5430),# weapons:Damage Amount  index:6    from 125 To 5555
        SetMemory(0x656EEC, Add, 2040),# weapons:Damage Amount  index:30    from 260 To 2300
        SetMemory(0x656EF4, Add, 2293760),# weapons:Damage Amount  index:35    from 5 To 40
        SetMemory(0x656EF8, Add, 190),# weapons:Damage Amount  index:36    from 10 To 200
        SetMemory(0x656EF8, Add, 22937600),# weapons:Damage Amount  index:37    from 50 To 400
        SetMemory(0x656EFC, Add, 21),# weapons:Damage Amount  index:38    from 10 To 31
        SetMemory(0x656EFC, Add, 8519680),# weapons:Damage Amount  index:39    from 20 To 150
        SetMemory(0x656F00, Add, 60),# weapons:Damage Amount  index:40    from 20 To 80
        SetMemory(0x656F00, Add, 22937600),# weapons:Damage Amount  index:41    from 50 To 400
        SetMemory(0x656F04, Add, 32440320),# weapons:Damage Amount  index:43    from 5 To 500
        SetMemory(0x656F0C, Add, 60),# weapons:Damage Amount  index:46    from 20 To 80
        SetMemory(0x656F0C, Add, 9175040),# weapons:Damage Amount  index:47    from 40 To 180
        SetMemory(0x656F10, Add, 31),# weapons:Damage Amount  index:48    from 9 To 40
        SetMemory(0x656F10, Add, 13893632),# weapons:Damage Amount  index:49    from 18 To 230
        SetMemory(0x656F14, Add, 125),# weapons:Damage Amount  index:50    from 5 To 130
        SetMemory(0x656F1C, Add, 400),# weapons:Damage Amount  index:54    from 500 To 900
        SetMemory(0x656F1C, Add, 203948032),# weapons:Damage Amount  index:55    from 110 To 3222
        SetMemory(0x656F58, Add, 1430),# weapons:Damage Amount  index:84    from 14 To 1444
        SetMemory(0x656F64, Add, 851968),# weapons:Damage Amount  index:91    from 7 To 20
        SetMemory(0x656F88, Add, 28573696),# weapons:Damage Amount  index:109    from 20 To 456
        SetMemory(0x656F90, Add, 18808832),# weapons:Damage Amount  index:113    from 25 To 312
        SetMemory(0x6576BC, Add, 458752),# weapons:Damage Bonus  index:35    from 1 To 8
        SetMemory(0x6576C0, Add, 19),# weapons:Damage Bonus  index:36    from 1 To 20
        SetMemory(0x6576C0, Add, 3866624),# weapons:Damage Bonus  index:37    from 1 To 60
        SetMemory(0x6576C4, Add, 4),# weapons:Damage Bonus  index:38    from 1 To 5
        SetMemory(0x6576C4, Add, 917504),# weapons:Damage Bonus  index:39    from 1 To 15
        SetMemory(0x6576C8, Add, 10),# weapons:Damage Bonus  index:40    from 3 To 13
        SetMemory(0x6576C8, Add, 2424832),# weapons:Damage Bonus  index:41    from 3 To 40
        SetMemory(0x6576D4, Add, 9),# weapons:Damage Bonus  index:46    from 2 To 11
        SetMemory(0x6576D4, Add, 3473408),# weapons:Damage Bonus  index:47    from 2 To 55
        SetMemory(0x6576D8, Add, 5),# weapons:Damage Bonus  index:48    from 1 To 6
        SetMemory(0x6576D8, Add, 1900544),# weapons:Damage Bonus  index:49    from 1 To 30
        SetMemory(0x6576DC, Add, 24),# weapons:Damage Bonus  index:50    from 1 To 25
        SetMemory(0x657720, Add, -1),# weapons:Damage Bonus  index:84    from 1 To 0
        SetMemory(0x65772C, Add, -65536),# weapons:Damage Bonus  index:91    from 1 To 0
        SetMemory(0x657750, Add, 3342336),# weapons:Damage Bonus  index:109    from 2 To 53
        SetMemory(0x657758, Add, 3407872),# weapons:Damage Bonus  index:113    from 1 To 53
        SetMemory(0x657010, Add, -117440512),# weapons:Weapon Cooldown  index:91    from 22 To 15
        SetMemory(0x6564E8, Add, -1),# weapons:Damage Factor  index:8    from 2 To 1
        SetMemory(0x656998, Add, 223),# weapons:Attack Angle  index:8    from 32 To 255
        SetMemory(0x6569EC, Add, -112),# weapons:Attack Angle  index:92    from 128 To 16
        SetMemory(0x6569EC, Add, -24576),# weapons:Attack Angle  index:93    from 128 To 32
        SetMemory(0x656A04, Add, 15663104),# weapons:Attack Angle  index:118    from 16 To 255
        SetMemory(0x657890, Add, -64),# weapons:Launch Spin  index:8    from 64 To 0
        SetMemory(0x6578E8, Add, -1073741824),# weapons:Launch Spin  index:99    from 64 To 0
        SetMemory(0x65791C, Add, 5120),# weapons:Forward Offset  index:13    from 0 To 20
        SetMemory(0x657968, Add, 167772160),# weapons:Forward Offset  index:91    from 0 To 10
        SetMemory(0x656C2C, Add, 0),# weapons:Upward Offset  index:13    from 0 To 0
        SetMemory(0x656C34, Add, 8388608),# weapons:Upward Offset  index:22    from 0 To 128
        SetMemory(0x656C78, Add, 335544320),# weapons:Upward Offset  index:91    from 0 To 20
        SetMemory(0x656790, Add, -76),# weapons:Icon  index:8    from 327 To 251
        SetMemory(0x6567A4, Add, -3801088),# weapons:Icon  index:19    from 333 To 275
        SetMemory(0x656830, Add, 362),# weapons:Icon  index:88    from 0 To 362
        SetMemory(0x656830, Add, 21757952),# weapons:Icon  index:89    from 0 To 332
        SetMemory(0x656834, Add, 272),# weapons:Icon  index:90    from 0 To 272
        SetMemory(0x656834, Add, 22085632),# weapons:Icon  index:91    from 0 To 337
        SetMemory(0x656838, Add, 45),# weapons:Icon  index:92    from 0 To 45
        SetMemory(0x656848, Add, 41),# weapons:Icon  index:100    from 332 To 373
        SetMemory(0x656868, Add, -7143424),# weapons:Icon  index:117    from 323 To 214
        SetMemory(0x65686C, Add, -150),# weapons:Icon  index:118    from 323 To 173
        SetMemory(0x656874, Add, 65536),# weapons:Icon  index:123    from 323 To 324
        SetMemory(0x656878, Add, 11),# weapons:Icon  index:124    from 323 To 334
        SetMemory(0x656878, Add, 131072),# weapons:Icon  index:125    from 323 To 325
        SetMemory(0x65687C, Add, -786432),# weapons:Icon  index:127    from 323 To 311
        SetMemory(0x6CA47C, Add, 85),# flingy:Sprite  index:178    from 303 To 388
        SetMemory(0x6CA480, Add, -5439488),# flingy:Sprite  index:181    from 305 To 222
        SetMemory(0x6CA484, Add, 37),# flingy:Sprite  index:182    from 306 To 343
        SetMemory(0x6C9FA8, Add, 38867),# flingy:Speed  index:44    from 1133 To 40000
        SetMemory(0x6C9FB4, Add, 1279),# flingy:Speed  index:47    from 1 To 1280
        SetMemory(0x6CA018, Add, 38600),# flingy:Speed  index:72    from 1400 To 40000
        SetMemory(0x6CA19C, Add, 2400),# flingy:Speed  index:169    from 0 To 2400
        SetMemory(0x6CA1B8, Add, 25600),# flingy:Speed  index:176    from 0 To 25600
        SetMemory(0x6CA1C0, Add, 8533),# flingy:Speed  index:178    from 0 To 8533
        SetMemory(0x6CA1C8, Add, 2400),# flingy:Speed  index:180    from 0 To 2400
        SetMemory(0x6CA1D0, Add, 1840),# flingy:Speed  index:182    from 0 To 1840
        SetMemory(0x6CA1D4, Add, 8533),# flingy:Speed  index:183    from 0 To 8533
        SetMemory(0x6C9CD0, Add, 3983),# flingy:Acceleration  index:44    from 17 To 4000
        SetMemory(0x6C9CD4, Add, 3276734464),# flingy:Acceleration  index:47    from 1 To 50000
        SetMemory(0x6C9D08, Add, 3983),# flingy:Acceleration  index:72    from 17 To 4000
        SetMemory(0x6C9DC8, Add, 78643200),# flingy:Acceleration  index:169    from 0 To 1200
        SetMemory(0x6C9DD8, Add, 8533),# flingy:Acceleration  index:176    from 0 To 8533
        SetMemory(0x6C9DDC, Add, 667),# flingy:Acceleration  index:178    from 0 To 667
        SetMemory(0x6C9DE0, Add, 1200),# flingy:Acceleration  index:180    from 0 To 1200
        SetMemory(0x6C9DE4, Add, 200),# flingy:Acceleration  index:182    from 0 To 200
        SetMemory(0x6C9DE4, Add, 17498112),# flingy:Acceleration  index:183    from 0 To 267
        SetMemory(0x6C99E0, Add, -37756),# flingy:Halt Distance  index:44    from 37756 To 0
        SetMemory(0x6C9A50, Add, -37756),# flingy:Halt Distance  index:72    from 37756 To 0
        SetMemory(0x6C9BF0, Add, 38402),# flingy:Halt Distance  index:176    from 0 To 38402
        SetMemory(0x6C9BF8, Add, 54582),# flingy:Halt Distance  index:178    from 0 To 54582
        SetMemory(0x6C9C00, Add, 3412),# flingy:Halt Distance  index:180    from 0 To 3412
        SetMemory(0x6C9C08, Add, 54582),# flingy:Halt Distance  index:182    from 0 To 54582
        SetMemory(0x6C9C0C, Add, 136352),# flingy:Halt Distance  index:183    from 0 To 136352
        SetMemory(0x6C9E4C, Add, 107),# flingy:Turn Radius  index:44    from 20 To 127
        SetMemory(0x6C9E4C, Add, 838860800),# flingy:Turn Radius  index:47    from 20 To 70
        SetMemory(0x6C9E68, Add, 107),# flingy:Turn Radius  index:72    from 20 To 127
        SetMemory(0x6C9EBC, Add, 0),# flingy:Turn Radius  index:158    from 127 To 127
        SetMemory(0x6C9EC8, Add, 32512),# flingy:Turn Radius  index:169    from 0 To 127
        SetMemory(0x6C9ED0, Add, 127),# flingy:Turn Radius  index:176    from 0 To 127
        SetMemory(0x6C9ED0, Add, -5701632),# flingy:Turn Radius  index:178    from 127 To 40
        SetMemory(0x6C9ED4, Add, 127),# flingy:Turn Radius  index:180    from 0 To 127
        SetMemory(0x6C9ED4, Add, 2621440),# flingy:Turn Radius  index:182    from 0 To 40
        SetMemory(0x6C9ED4, Add, 2130706432),# flingy:Turn Radius  index:183    from 0 To 127
        SetMemory(0x6C9884, Add, -33554432),# flingy:Movement Control  index:47    from 2 To 0
        SetMemory(0x6C9900, Add, -512),# flingy:Movement Control  index:169    from 2 To 0
        SetMemory(0x6C9908, Add, -2),# flingy:Movement Control  index:176    from 2 To 0
        SetMemory(0x6C9908, Add, -65536),# flingy:Movement Control  index:178    from 2 To 1
        SetMemory(0x6C990C, Add, -2),# flingy:Movement Control  index:180    from 2 To 0
        SetMemory(0x6C990C, Add, -65536),# flingy:Movement Control  index:182    from 2 To 1
        SetMemory(0x6C990C, Add, -16777216),# flingy:Movement Control  index:183    from 2 To 1
        SetMemory(0x6663C0, Add, 237),# sprites:Image File  index:304    from 738 To 975
        SetMemory(0x6663C4, Add, 13238272),# sprites:Image File  index:307    from 741 To 943
        SetMemory(0x6663C8, Add, -6815744),# sprites:Image File  index:309    from 422 To 318
        SetMemory(0x666460, Add, -391),# sprites:Image File  index:384    from 751 To 360
        SetMemory(0x665DCC, Add, -1),# sprites:Is Visible  index:388    from 1 To 0
        SetMemory(0x669FD0, Add, 8),# images:Draw Function  index:424    from 9 To 17
        SetMemory(0x66A034, Add, 268435456),# images:Draw Function  index:527    from 0 To 16
        SetMemory(0x66A050, Add, 134217728),# images:Draw Function  index:555    from 8 To 16
        SetMemory(0x66A054, Add, 7),# images:Draw Function  index:556    from 9 To 16
        SetMemory(0x66A1C4, Add, 2560),# images:Draw Function  index:925    from 0 To 10
        SetMemory(0x66A1C4, Add, 1048576),# images:Draw Function  index:926    from 0 To 16
        SetMemory(0x66A1C4, Add, 167772160),# images:Draw Function  index:927    from 0 To 10
        SetMemory(0x66EE20, Add, 4),# images:Iscript ID  index:118    from 157 To 161
        SetMemory(0x66EEF4, Add, -57),# images:Iscript ID  index:171    from 173 To 116
        SetMemory(0x66EF14, Add, -61),# images:Iscript ID  index:179    from 177 To 116
        SetMemory(0x66EF64, Add, -69),# images:Iscript ID  index:199    from 185 To 116
        SetMemory(0x66EF74, Add, -71),# images:Iscript ID  index:203    from 187 To 116
        SetMemory(0x66EF84, Add, -73),# images:Iscript ID  index:207    from 189 To 116
        SetMemory(0x66EFA4, Add, 102),# images:Iscript ID  index:215    from 144 To 246
        SetMemory(0x66EFC4, Add, 14),# images:Iscript ID  index:223    from 68 To 82
        SetMemory(0x66F1E8, Add, -1),# images:Iscript ID  index:360    from 244 To 243
        SetMemory(0x66F45C, Add, -63),# images:Iscript ID  index:517    from 298 To 235
        SetMemory(0x66F48C, Add, 26),# images:Iscript ID  index:529    from 240 To 266
        SetMemory(0x66F824, Add, -96),# images:Iscript ID  index:759    from 336 To 240
        SetMemory(0x66FAE0, Add, -290),# images:Iscript ID  index:934    from 406 To 116
        SetMemory(0x66FAEC, Add, -294),# images:Iscript ID  index:937    from 410 To 116
        SetMemory(0x66FB04, Add, -58),# images:Iscript ID  index:943    from 291 To 233
        SetMemory(0x66FB08, Add, -290),# images:Iscript ID  index:944    from 360 To 70
        SetMemory(0x66FB28, Add, -306),# images:Iscript ID  index:952    from 375 To 69
        SetMemory(0x66FB84, Add, -155),# images:Iscript ID  index:975    from 390 To 235
        SetMemory(0x655740, Add, -100),# upgrades:Mineral Cost Base  index:0    from 100 To 0
        SetMemory(0x65574C, Add, -6553600),# upgrades:Mineral Cost Base  index:7    from 100 To 0
        SetMemory(0x655750, Add, -100),# upgrades:Mineral Cost Base  index:8    from 100 To 0
        SetMemory(0x655750, Add, -6553600),# upgrades:Mineral Cost Base  index:9    from 100 To 0
        SetMemory(0x655754, Add, -100),# upgrades:Mineral Cost Base  index:10    from 100 To 0
        SetMemory(0x655754, Add, -6553600),# upgrades:Mineral Cost Base  index:11    from 100 To 0
        SetMemory(0x65575C, Add, 9900),# upgrades:Mineral Cost Base  index:14    from 100 To 10000
        SetMemory(0x65575C, Add, -13107200),# upgrades:Mineral Cost Base  index:15    from 200 To 0
        SetMemory(0x655760, Add, -6553600),# upgrades:Mineral Cost Base  index:17    from 100 To 0
        SetMemory(0x655764, Add, -200),# upgrades:Mineral Cost Base  index:18    from 200 To 0
        SetMemory(0x655764, Add, -9830400),# upgrades:Mineral Cost Base  index:19    from 150 To 0
        SetMemory(0x655768, Add, -100),# upgrades:Mineral Cost Base  index:20    from 100 To 0
        SetMemory(0x655768, Add, -9830400),# upgrades:Mineral Cost Base  index:21    from 150 To 0
        SetMemory(0x65576C, Add, -200),# upgrades:Mineral Cost Base  index:22    from 200 To 0
        SetMemory(0x65576C, Add, -9830400),# upgrades:Mineral Cost Base  index:23    from 150 To 0
        SetMemory(0x655794, Add, -6553600),# upgrades:Mineral Cost Base  index:43    from 100 To 0
        SetMemory(0x6559C0, Add, -25),# upgrades:Mineral Cost Factor  index:0    from 75 To 50
        SetMemory(0x6559CC, Add, -3604480),# upgrades:Mineral Cost Factor  index:7    from 75 To 20
        SetMemory(0x6559D0, Add, 75),# upgrades:Mineral Cost Factor  index:8    from 75 To 150
        SetMemory(0x6559D0, Add, 16384000),# upgrades:Mineral Cost Factor  index:9    from 50 To 300
        SetMemory(0x6559D4, Add, 30),# upgrades:Mineral Cost Factor  index:10    from 50 To 80
        SetMemory(0x6559D4, Add, 9830400),# upgrades:Mineral Cost Factor  index:11    from 50 To 200
        SetMemory(0x6559DC, Add, 142),# upgrades:Mineral Cost Factor  index:14    from 75 To 217
        SetMemory(0x6559DC, Add, -4915200),# upgrades:Mineral Cost Factor  index:15    from 100 To 25
        SetMemory(0x655840, Add, -100),# upgrades:Vespene Cost Base  index:0    from 100 To 0
        SetMemory(0x65584C, Add, -6553600),# upgrades:Vespene Cost Base  index:7    from 100 To 0
        SetMemory(0x655850, Add, -100),# upgrades:Vespene Cost Base  index:8    from 100 To 0
        SetMemory(0x655850, Add, -6553600),# upgrades:Vespene Cost Base  index:9    from 100 To 0
        SetMemory(0x655854, Add, -100),# upgrades:Vespene Cost Base  index:10    from 100 To 0
        SetMemory(0x655854, Add, -6553600),# upgrades:Vespene Cost Base  index:11    from 100 To 0
        SetMemory(0x65585C, Add, -100),# upgrades:Vespene Cost Base  index:14    from 100 To 0
        SetMemory(0x65585C, Add, -13107200),# upgrades:Vespene Cost Base  index:15    from 200 To 0
        SetMemory(0x655860, Add, -6553600),# upgrades:Vespene Cost Base  index:17    from 100 To 0
        SetMemory(0x655864, Add, -200),# upgrades:Vespene Cost Base  index:18    from 200 To 0
        SetMemory(0x655864, Add, -9830400),# upgrades:Vespene Cost Base  index:19    from 150 To 0
        SetMemory(0x655868, Add, -100),# upgrades:Vespene Cost Base  index:20    from 100 To 0
        SetMemory(0x655868, Add, -9830400),# upgrades:Vespene Cost Base  index:21    from 150 To 0
        SetMemory(0x65586C, Add, -200),# upgrades:Vespene Cost Base  index:22    from 200 To 0
        SetMemory(0x65586C, Add, -9830400),# upgrades:Vespene Cost Base  index:23    from 150 To 0
        SetMemory(0x655894, Add, -6553600),# upgrades:Vespene Cost Base  index:43    from 100 To 0
        SetMemory(0x6557C0, Add, -75),# upgrades:Vespene Cost Factor  index:0    from 75 To 0
        SetMemory(0x6557CC, Add, -4915200),# upgrades:Vespene Cost Factor  index:7    from 75 To 0
        SetMemory(0x6557D0, Add, -75),# upgrades:Vespene Cost Factor  index:8    from 75 To 0
        SetMemory(0x6557D0, Add, -3276800),# upgrades:Vespene Cost Factor  index:9    from 50 To 0
        SetMemory(0x6557D4, Add, -50),# upgrades:Vespene Cost Factor  index:10    from 50 To 0
        SetMemory(0x6557D4, Add, -3276800),# upgrades:Vespene Cost Factor  index:11    from 50 To 0
        SetMemory(0x6557DC, Add, -75),# upgrades:Vespene Cost Factor  index:14    from 75 To 0
        SetMemory(0x6557DC, Add, -6553600),# upgrades:Vespene Cost Factor  index:15    from 100 To 0
        SetMemory(0x655B80, Add, -4000),# upgrades:Research Time Base  index:0    from 4000 To 0
        SetMemory(0x655B8C, Add, -262144000),# upgrades:Research Time Base  index:7    from 4000 To 0
        SetMemory(0x655B90, Add, -4000),# upgrades:Research Time Base  index:8    from 4000 To 0
        SetMemory(0x655B90, Add, -262144000),# upgrades:Research Time Base  index:9    from 4000 To 0
        SetMemory(0x655B94, Add, -4000),# upgrades:Research Time Base  index:10    from 4000 To 0
        SetMemory(0x655B94, Add, -262144000),# upgrades:Research Time Base  index:11    from 4000 To 0
        SetMemory(0x655B9C, Add, -4000),# upgrades:Research Time Base  index:14    from 4000 To 0
        SetMemory(0x655B9C, Add, -262144000),# upgrades:Research Time Base  index:15    from 4000 To 0
        SetMemory(0x655BA0, Add, -98304000),# upgrades:Research Time Base  index:17    from 1500 To 0
        SetMemory(0x655BA4, Add, -2500),# upgrades:Research Time Base  index:18    from 2500 To 0
        SetMemory(0x655BA4, Add, -163840000),# upgrades:Research Time Base  index:19    from 2500 To 0
        SetMemory(0x655BA8, Add, -2500),# upgrades:Research Time Base  index:20    from 2500 To 0
        SetMemory(0x655BA8, Add, -163840000),# upgrades:Research Time Base  index:21    from 2500 To 0
        SetMemory(0x655BAC, Add, -2500),# upgrades:Research Time Base  index:22    from 2500 To 0
        SetMemory(0x655BAC, Add, -163840000),# upgrades:Research Time Base  index:23    from 2500 To 0
        SetMemory(0x655BD4, Add, -98304000),# upgrades:Research Time Base  index:43    from 1500 To 0
        SetMemory(0x655940, Add, -480),# upgrades:Research Time Factor  index:0    from 480 To 0
        SetMemory(0x65594C, Add, -31457280),# upgrades:Research Time Factor  index:7    from 480 To 0
        SetMemory(0x655950, Add, -480),# upgrades:Research Time Factor  index:8    from 480 To 0
        SetMemory(0x655950, Add, -31457280),# upgrades:Research Time Factor  index:9    from 480 To 0
        SetMemory(0x655954, Add, -480),# upgrades:Research Time Factor  index:10    from 480 To 0
        SetMemory(0x655954, Add, -31457280),# upgrades:Research Time Factor  index:11    from 480 To 0
        SetMemory(0x65595C, Add, -480),# upgrades:Research Time Factor  index:14    from 480 To 0
        SetMemory(0x65595C, Add, -31457280),# upgrades:Research Time Factor  index:15    from 480 To 0
        SetMemory(0x655C24, Add, -16777216),# upgrades:Race  index:43    from 2 To 1
        SetMemory(0x65570C, Add, 16515072),# upgrades:Max. Repeats  index:14    from 3 To 255
        SetMemory(0x655710, Add, 5888),# upgrades:Max. Repeats  index:17    from 1 To 24
        SetMemory(0x655714, Add, 2048),# upgrades:Max. Repeats  index:21    from 1 To 9
        SetMemory(0x656388, Add, -49),# techdata:Energy Required  index:4    from 50 To 1
    ])

