                              1 ;--------------------------------------------------------
                              2 ; File Created by SDCC : free open source ANSI-C Compiler
                              3 ; Version 3.9.5 #11456 (MINGW64)
                              4 ;--------------------------------------------------------
                              5 	.cs08
                              6 	.module evoz80
                              7 	.optsdcc -ms08
                              8 	
                              9 	.area HOME    (CODE)
                             10 	.area GSINIT0 (CODE)
                             11 	.area GSINIT  (CODE)
                             12 	.area GSFINAL (CODE)
                             13 	.area CSEG    (CODE)
                             14 	.area XINIT   (CODE)
                             15 	.area CONST   (CODE)
                             16 	.area DSEG    (PAG)
                             17 	.area OSEG    (PAG, OVR)
                             18 	.area XSEG
                             19 	.area XISEG
                             20 	.area	CODEIVT (ABS)
   FFFE                      21 	.org	0xfffe
   FFFE 80 00                22 	.dw	__sdcc_gs_init_startup
                             23 
                             24 	.area GSINIT0
   8000                      25 __sdcc_gs_init_startup:
   8000 45 80 00      [ 3]   26 	ldhx	#0x8000
   8003 94            [ 2]   27 	txs
   8004 CD 80 3F      [ 6]   28 	jsr	__sdcc_external_startup
   8007 27 03         [ 3]   29 	beq	__sdcc_init_data
   8009 CC 80 21      [ 4]   30 	jmp	__sdcc_program_startup
   800C                      31 __sdcc_init_data:
                             32 ; _hc08_genXINIT() start
   800C 45 00 00      [ 3]   33         ldhx #0
   800F                      34 00001$:
   800F 65 00 00      [ 3]   35         cphx #l_XINIT
   8012 27 0A         [ 3]   36         beq  00002$
   8014 D6 80 41      [ 4]   37         lda  s_XINIT,x
   8017 D7 00 82      [ 4]   38         sta  s_XISEG,x
   801A AF 01         [ 2]   39         aix  #1
   801C 20 F1         [ 3]   40         bra  00001$
   801E                      41 00002$:
                             42 ; _hc08_genXINIT() end
                             43 	.area GSFINAL
   801E CC 80 21      [ 4]   44 	jmp	__sdcc_program_startup
                             45 
                             46 	.area CSEG
   8021                      47 __sdcc_program_startup:
   8021 CD 80 28      [ 6]   48 	jsr	_main
   8024 20 FE         [ 3]   49 	bra	.
                             50 ;--------------------------------------------------------
                             51 ; Public variables in this module
                             52 ;--------------------------------------------------------
                             53 	.globl _doFun
                             54 	.globl _main
                             55 	.globl _sayBye
                             56 	.globl _sayHi
                             57 	.globl _main_PARM_2
                             58 ;--------------------------------------------------------
                             59 ; ram data
                             60 ;--------------------------------------------------------
                             61 	.area DSEG    (PAG)
                             62 ;--------------------------------------------------------
                             63 ; overlayable items in ram 
                             64 ;--------------------------------------------------------
                             65 ;--------------------------------------------------------
                             66 ; absolute ram data
                             67 ;--------------------------------------------------------
                             68 	.area IABS    (ABS)
                             69 	.area IABS    (ABS)
                             70 ;--------------------------------------------------------
                             71 ; absolute external ram data
                             72 ;--------------------------------------------------------
                             73 	.area XABS    (ABS)
                             74 ;--------------------------------------------------------
                             75 ; external initialized ram data
                             76 ;--------------------------------------------------------
                             77 	.area XISEG
                             78 ;--------------------------------------------------------
                             79 ; extended address mode data
                             80 ;--------------------------------------------------------
                             81 	.area XSEG
   0080                      82 _main_PARM_2:
   0080                      83 	.ds 2
                             84 ;--------------------------------------------------------
                             85 ; global & static initialisations
                             86 ;--------------------------------------------------------
                             87 	.area HOME    (CODE)
                             88 	.area GSINIT  (CODE)
                             89 	.area GSFINAL (CODE)
                             90 	.area GSINIT  (CODE)
                             91 ;--------------------------------------------------------
                             92 ; Home
                             93 ;--------------------------------------------------------
                             94 	.area HOME    (CODE)
                             95 	.area HOME    (CODE)
                             96 ;--------------------------------------------------------
                             97 ; code
                             98 ;--------------------------------------------------------
                             99 	.area CSEG    (CODE)
                            100 ;------------------------------------------------------------
                            101 ;Allocation info for local variables in function 'sayHi'
                            102 ;------------------------------------------------------------
                            103 ;evoz80.c:2: void sayHi() {
                            104 ;	-----------------------------------------
                            105 ;	 function sayHi
                            106 ;	-----------------------------------------
                            107 ;	Register assignment is optimal.
                            108 ;	Stack space usage: 0 bytes.
   8026                     109 _sayHi:
                            110 ;evoz80.c:3: }
   8026 81            [ 6]  111 	rts
                            112 ;------------------------------------------------------------
                            113 ;Allocation info for local variables in function 'sayBye'
                            114 ;------------------------------------------------------------
                            115 ;evoz80.c:5: void sayBye() {
                            116 ;	-----------------------------------------
                            117 ;	 function sayBye
                            118 ;	-----------------------------------------
                            119 ;	Register assignment is optimal.
                            120 ;	Stack space usage: 0 bytes.
   8027                     121 _sayBye:
                            122 ;evoz80.c:6: }
   8027 81            [ 6]  123 	rts
                            124 ;------------------------------------------------------------
                            125 ;Allocation info for local variables in function 'main'
                            126 ;------------------------------------------------------------
                            127 ;argv                      Allocated with name '_main_PARM_2'
                            128 ;argc                      Allocated to registers 
                            129 ;------------------------------------------------------------
                            130 ;evoz80.c:8: int main(int argc, char ** argv) {
                            131 ;	-----------------------------------------
                            132 ;	 function main
                            133 ;	-----------------------------------------
                            134 ;	Register assignment is optimal.
                            135 ;	Stack space usage: 0 bytes.
   8028                     136 _main:
                            137 ;evoz80.c:9: return 0;
   8028 4F            [ 1]  138 	clra
   8029 97            [ 1]  139 	tax
                            140 ;evoz80.c:10: }
   802A 81            [ 6]  141 	rts
                            142 ;------------------------------------------------------------
                            143 ;Allocation info for local variables in function 'doFun'
                            144 ;------------------------------------------------------------
                            145 ;a                         Allocated to registers a 
                            146 ;------------------------------------------------------------
                            147 ;evoz80.c:12: void doFun() {
                            148 ;	-----------------------------------------
                            149 ;	 function doFun
                            150 ;	-----------------------------------------
                            151 ;	Register assignment is optimal.
                            152 ;	Stack space usage: 0 bytes.
   802B                     153 _doFun:
                            154 ;evoz80.c:13: char a = 5;
   802B A6 05         [ 2]  155 	lda	#0x05
                            156 ;evoz80.c:15: while(a>0 && a!=10) {   
   802D                     157 00104$:
   802D 4D            [ 1]  158 	tsta
   802E 27 09         [ 3]  159 	beq	00106$
   8030 41 0A 06      [ 4]  160 	cbeqa	#0x0a,00106$
                            161 ;evoz80.c:16: if(a==3) {
   8033 41 03 F7      [ 4]  162 	cbeqa	#0x03,00104$
                            163 ;evoz80.c:19: a = a - 1; 
   8036 4A            [ 1]  164 	deca
   8037 20 F4         [ 3]  165 	bra	00104$
   8039                     166 00106$:
                            167 ;evoz80.c:22: sayHi();
   8039 CD 80 26      [ 6]  168 	jsr	_sayHi
                            169 ;evoz80.c:23: sayBye();
                            170 ;evoz80.c:25: }
   803C CC 80 27      [ 4]  171 	jmp	_sayBye
                            172 	.area CSEG    (CODE)
                            173 	.area CONST   (CODE)
                            174 	.area XINIT   (CODE)
                            175 	.area CABS    (ABS,CODE)
