G20         ; Set units to inches
G90         ; Absolute positioning
G1 Z0.1 F100      ; Move to clearance level

;
; Operation:    0
; Name:         
; Type:         Inside
; Paths:        1
; Direction:    Conventional
; Cut Depth:    1
; Pass Depth:   1
; Plunge rate:  5
; Cut rate:     40
;

; Path 0
; Rapid to initial position
G1 X0.2491 Y-0.2287 F100
G1 Z0.0000
; plunge
G1 Z-1.0000 F5
; cut
G1 X0.0009 Y-0.2287 F40
G1 X0.1250 Y-0.0218
G1 X0.2491 Y-0.2287
; Retract
G1 Z0.1000 F100
M2
