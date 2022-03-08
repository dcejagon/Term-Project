G21         ; Set units to mm
G90         ; Absolute positioning
G1 Z2.54 F2540      ; Move to clearance level

;
; Operation:    0
; Name:         
; Type:         Inside
; Paths:        1
; Direction:    Conventional
; Cut Depth:    25.4
; Pass Depth:   25.4
; Plunge rate:  127
; Cut rate:     1016
;

; Path 0
; Rapid to initial position
G1 X6.3274 Y-5.8082 F2540
G1 Z0.0000
; plunge
G1 Z-25.4000 F127
; cut
G1 X0.0226 Y-5.8082 F1016
G1 X3.1750 Y-0.5540
G1 X6.3274 Y-5.8082
; Retract
G1 Z2.5400 F2540
M2
