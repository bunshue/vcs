;-**************************************************************************--
;- Copyright (c) 1999-2001  Digital Core Design  DCD                        --
;-**************************************************************************--
;- Please review the terms of the license agreement before using this file. --
;- If you are not an authorized user, please destroy this source code file  --
;- and notify DCD immediately that you inadvertently received an            --
;- unauthorized copy.                                                       --
;-**************************************************************************--
;
;-----------------------------------------------------------------------------
;- Project name         : DR80390
;- Project description  : 
;-
;- File name            : MDU.A51
;- File contents        : DR80390 C compiler interface functions.  
;                         Some operations have been replaced:
;                         --------------------------------------------------
;                         'IMUL'  - Integer Multiplcation
;                         'UIDIV' - Unsigned Integer Division 
;                         'SIDIV' - Signed Integer Division 
;                         'ULDIV' - Unsigned Long Integer Division 
;                         'SLDIV' - Signed Long Integer Division 
;---------------------------------------------------------------------------
;- Notes                : Tested with Keil software (C/ASM/Linker)
;---------------------------------------------------------------------------
;    DR80390 uses the: 
;       following SFRs: MD0 (0xF9); MD1 (0xFA); MD2 (0xFB); MD3 (0xFC)
;                       MD4 (0xFD); MD5 (0xFE); ARCON (0xFF)
;
;    Input data are stored in current R0-R7 register bank.
;    Result is returned using R4-R7.
;
;    ACC, PSW content are changed by each function
;---------------------------------------------------------------------------
;- Design Engineer      : P.K.
;- Version              : 1.00
;- Last modification    : 2002-01-10
;                         2006-04-18, by Dong Hsu, Myson Century
;                           Avoid the problem: A shift counter 0 will cause
;                           the MDU to shift the value 16-bit left of right.
;                         2009-07-28, by Kaven Feng
;                           to fix the proper operation time according to specification
;-----------------------------------------------------------------------------
;
$NOMOD51 ; Prevents names conflict

NAME    MDU_F

; DR80517 registers definition
;
MD0     DATA    0F9H
MD1     DATA    0FAH
MD2     DATA    0FBH
MD3     DATA    0FCH
MD4     DATA    0FDH
MD5     DATA    0FEH
ARCON   DATA    0FFH
;
; std. 805x Accumulator location
ACC     DATA    0E0H
PSW     DATA    0D0H

DPL     DATA    082H
DPH     DATA    083H
B       DATA    0F0H
F0      BIT     PSW.5

;---------------------------------------------------------
; 'IMUL' Integer Multiplication function replacement begin
;---------------------------------------------------------
?PR?IMUL?MDU  SEGMENT CODE
        PUBLIC  ?C?IMUL    
        RSEG  ?PR?IMUL?MDU
?C?IMUL:
        MOV     MD0,R5   
        MOV     MD4,R7
        MOV     MD1,R4
        MOV     MD5,R6
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 10 execution clock
        MOV     R7,MD0   
        MOV     R6,MD1
        RET

;---------------------------------------------------------
; 'LSHL' long left shift function replacement begin
;
; Input Parameters:
;     R4.R5.R6.R7: the 32-bit value to be shifted left
;              R0: the shift counter
;
; Output Parameters (value):
;     R4.R5.R6.R7: the result
;
;---------------------------------------------------------
?PR?LSHL?MDU  SEGMENT CODE
        PUBLIC  ?C?LSHL    
        RSEG  ?PR?LSHL?MDU
?C?LSHL:
        mov A, R0           ; Added by Dong Hsu
        jz  LSHLexit        ; Added by Dong Hsu

        MOV MD0, R7
        MOV MD1, R6
        MOV MD2, R5
        MOV MD3, R4
;Dong   MOV ARCON, R0   ; set shift left
        mov ARCON, A    ; set shift left. Modified by Dong Hsu
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 18 execution clock
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        MOV R7, MD0
        MOV R6, MD1
        MOV R5, MD2
        MOV R4, MD3

LSHLexit:                   ; Added by Dong Hsu
        RET
        
;---------------------------------------------------------
; 'ULSHR' long right shift function replacement begin
;
; Input Parameters:
;     R4.R5.R6.R7: the 32-bit value to be shifted right
;              R0: the shift counter
;
; Output Parameters (value):
;     R4.R5.R6.R7: the result
;
;---------------------------------------------------------
?PR?ULSHR?MDU  SEGMENT CODE
        PUBLIC  ?C?ULSHR    
        RSEG  ?PR?ULSHR?MDU
?C?ULSHR:
        mov A, R0           ; Added by Dong Hsu
        jz  ULSHRexit       ; Added by Dong Hsu

        MOV MD0, R7
        MOV MD1, R6
        MOV MD2, R5
        MOV MD3, R4
;Dong   MOV ACC, R0         ; removed by Dong Hsu
        ORL ACC, #20H       ; Shift direction: right
        MOV ARCON, A    ; set shift right
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 18 execution clock
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        NOP             
        MOV R7, MD0
        MOV R6, MD1
        MOV R5, MD2
        MOV R4, MD3

ULSHRexit:                  ; Added by Dong Hsu
        RET

;--------------------------------------------------------------
; 'LMUL' Long Integer Multiplication function replacement begin
;--------------------------------------------------------------
?PR?LMUL?MDU  SEGMENT CODE
        PUBLIC  ?C?LMUL    
        RSEG  ?PR?LMUL?MDU
?C?LMUL:
        MOV     MD0,R5  ; 16 * 16
        MOV     MD4,R3
        MOV     MD1,R4
        MOV     MD5,R2
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 18 execution clock
        MOV     R5,MD0  ; product low
        MOV     R4,MD1
        MOV     A,MD2
        MOV     A,MD3   ; product high
        MOV     MD0,R7   
        MOV     MD4,R1
        MOV     MD1,R6
        MOV     MD5,R0
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 18 execution clock
        MOV     A,MD0
        ADD     A,R5
        MOV     R5,A
        MOV     A,MD1
        ADDC    A,R4
        MOV     R4,A
        MOV     A,MD2
        MOV     A,MD3
        MOV     MD0,R7
        MOV     MD4,R3
        MOV     MD1,R6
        MOV     MD5,R2
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 18 execution clock
        MOV     R7,MD0
        MOV     R6,MD1
        MOV     A,MD2
        ADD     A,R5
        MOV     R5,A
        MOV     A,MD3
        ADDC    A,R4
        MOV     R4,A
        RET


;----------------------------------------------------------------
; 'SLDIV' Signed Long Integer division function replacement begin
;----------------------------------------------------------------
?PR?SLDIV?MDU  SEGMENT CODE
        PUBLIC  ?C?SLDIV    
        RSEG  ?PR?SLDIV?MDU
?C?SLDIV:
        CLR     F0
        MOV     A,R0
        JNB     ACC.7,C_14BE
        CPL     F0
        CLR     A
        CLR     C
        SUBB    A,R3
        MOV     R3,A
        CLR     A
        SUBB    A,R2
        MOV     R2,A
        CLR     A
        SUBB    A,R1
        MOV     R1,A
        CLR     A
        SUBB    A,R0
        MOV     R0,A
C_14BE: MOV     A,R4
        JNB     ACC.7,C_14D9
        CPL     F0
        LCALL   C_14DF
        LCALL   ULDIV
        CLR     A
        CLR     C
        SUBB    A,R3
        MOV     R3,A
        CLR     A
        SUBB    A,R2
        MOV     R2,A
        CLR     A
        SUBB    A,R1
        MOV     R1,A
        CLR     A
        SUBB    A,R0
        MOV     R0,A
        SJMP    C_14DC
C_14D9: LCALL   ULDIV
C_14DC: JNB     F0,C_14EC
C_14DF: CLR     A
        CLR     C
        SUBB    A,R7
        MOV     R7,A
        CLR     A
        SUBB    A,R6
        MOV     R6,A
        CLR     A
        SUBB    A,R5
        MOV     R5,A
        CLR     A
        SUBB    A,R4
        MOV     R4,A
C_14EC: RET

;------------------------------------------------------------------
; 'ULDIV' Unsigned Long Integer Division function replacement begin
;------------------------------------------------------------------
?PR?ULDIV?MDU  SEGMENT CODE
        PUBLIC  ?C?ULDIV    
        RSEG  ?PR?ULDIV?MDU
?C?ULDIV:
ULDIV:
        MOV     A,R0
        ORL     A,R1
        JNZ     C_06B8
        MOV     MD0,R7
        MOV     MD1,R6
        MOV     MD2,R5
        MOV     MD3,R4
        MOV     MD4,R3
        MOV     MD5,R2
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 17 execution clock
        NOP
        MOV     R7,MD0
        MOV     R6,MD1
        MOV     R5,MD2
        MOV     R4,MD3
        MOV     R3,MD4
        MOV     R2,MD5
        RET
C_06B8: MOV     MD0,R3
        MOV     MD1,R2
        MOV     MD2,R1
        MOV     MD3,R0
        MOV     ARCON,#0xA4  
        MOV     A,R0
        XCH     A,R4
        MOV     R0,A
        MOV     DPL,MD2
        MOV     DPH,MD3
        MOV     B,ARCON
        MOV     MD0,R7
        MOV     MD1,R6
        MOV     MD2,R5
        MOV     MD3,R0
        MOV     MD4,DPL
        MOV     MD5,DPH
        ANL     B,#0x1F
        MOV     A,#0xC1
        CLR     C
        SUBB    A,B
        ORL     A,#20
        MOV     ARCON,A
        MOV     A,R6
        XCH     A,R2
        MOV     R6,A
        MOV     A,R1
        MOV     DPL,MD0
        MOV     DPH,MD1
        MOV     MD0,DPL
        MOV     MD4,A
        MOV     MD1,DPH
        MOV     MD5,R4
        XCH     A,R5
        XCH     A,R7
        XCH     A,R3
        XCH     A,R7
        CLR     C
        SUBB    A,MD0
        XCH     A,R0
        SUBB    A,MD1
        MOV     MD0,DPL
        MOV     MD4,R7
        MOV     MD1,DPH
        MOV     MD5,R6
C_0711: MOV     R1,A
        MOV     0xF0.0,C
        CLR     C
        MOV     A,R3
        SUBB    A,MD0
        MOV     R3,A
        MOV     A,R2
        SUBB    A,MD1
        MOV     R2,A
        MOV     A,R0
        SUBB    A,MD2
        XCH     A,R1
        SUBB    A,MD3
        MOV     R0,A
        ORL     C,0xF0.0
        JNC     C_073D
        DEC     DPL
        MOV     A,DPL
        CJNE    A,#0xFF,C_0731
        DEC     DPH
C_0731: MOV     A,R7
        ADD     A,R3
        MOV     R3,A
        MOV     A,R6
        ADDC    A,R2
        MOV     R2,A
C_0737: MOV     A,R5
        ADDC    A,R1
        MOV     R1,A
        MOV     A,R4
        ADDC    A,R0
        MOV     R0,A
C_073D: MOV     R7,DPL
        MOV     R6,DPH
        CLR     A
        MOV     R5,A
        MOV     R4,A
        RET


;-----------------------------------------------------------
; 'SIDIV' Signed Integer Division function replacement begin
;-----------------------------------------------------------
?PR?SIDIV?MDU  SEGMENT CODE
        PUBLIC  ?C?SIDIV    
        RSEG  ?PR?SIDIV?MDU
?C?SIDIV:
        CLR     F0
        MOV     A,R4
        JNB     ACC.7,C_05AB
        CPL     F0
        CLR     A
        CLR     C
        SUBB    A,R5
        MOV     R5,A
        CLR     A
        SUBB    A,R4
        MOV     R4,A
C_05AB: MOV     A,R6
        JNB     ACC.7,C_05C4
        CPL     F0
        CLR     A
        CLR     C
        SUBB    A,R7
        MOV     R7,A
        CLR     A
        SUBB    A,R6
        MOV     R6,A
        LCALL   UIDIV
        CLR     C
        CLR     A
        SUBB    A,R5
        MOV     R5,A
        CLR     A
        SUBB    A,R4
        MOV     R4,A
        SJMP    C_05C7
C_05C4: LCALL   UIDIV
C_05C7: JNB     F0,C_05D1
        CLR     C
        CLR     A
        SUBB    A,R7
        MOV     R7,A
        CLR     A
        SUBB    A,R6
        MOV     R6,A
C_05D1: RET

;-------------------------------------------------------------
; 'UIDIV' Unsigned Integer Division function replacement begin
;-------------------------------------------------------------
?PR?UIDIV?MDU  SEGMENT CODE
        PUBLIC  ?C?UIDIV    
        RSEG  ?PR?UIDIV?MDU
?C?UIDIV:
UIDIV:
        MOV     MD0,R7
        MOV     MD1,R6
        MOV     MD4,R5
        MOV     MD5,R4
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP
        NOP             ; added by Kaven, 9 execution clock
        NOP                                                 
        MOV     R7,MD0
        MOV     R6,MD1
        MOV     R5,MD4
        MOV     R4,MD5
        RET
END

