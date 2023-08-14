11       	 <--SHAPES
12       	 <--LINES
id1
2       	 <--TYPE
172       	 <--LEFT
70       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
START



id2
2       	 <--TYPE
283       	 <--LEFT
488       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
STOP



id3
0       	 <--TYPE
280       	 <--LEFT
71       	 <--TOP
83       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
target
38

id6
92       	 <--TYPE
253       	 <--LEFT
325       	 <--TOP
132       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
target
guess

id8
92       	 <--TYPE
264       	 <--LEFT
166       	 <--TOP
112       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_EQUAL
1
1

id7
0       	 <--TYPE
281       	 <--LEFT
119       	 <--TOP
78       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
guess
1

id4
91       	 <--TYPE
193       	 <--LEFT
263       	 <--TOP
253       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
叫块瞦代计(1~100): 
guess

id5
92       	 <--TYPE
431       	 <--LEFT
324       	 <--TOP
124       	 <--WIDTH
50       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
IF_GREATER
guess
target

id11
91       	 <--TYPE
445       	 <--LEFT
459       	 <--TOP
97       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
计び!


id12
91       	 <--TYPE
243       	 <--LEFT
420       	 <--TOP
151       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
瞦い计 = 
target

id13
91       	 <--TYPE
571       	 <--LEFT
393       	 <--TOP
101       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
计び! 


  
---- LINES ---- from,to ----
id1,id3
0

id3,id7
0

id7,id8
0

id8,id4
0
YES
id4,id6
0

id6,id5
0
NO
id5,id11
0
YES
id6,id12
0
YES
id12,id2
0

id5,id13
0
NO
id13,id8
40

id11,id8
170

