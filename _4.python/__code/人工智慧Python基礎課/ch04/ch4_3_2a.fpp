5       	 <--SHAPES
4       	 <--LINES
id1
2       	 <--TYPE
300       	 <--LEFT
53       	 <--TOP
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
299       	 <--LEFT
279       	 <--TOP
70       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
STOP



id3
91       	 <--TYPE
246       	 <--LEFT
97       	 <--TOP
179       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
INPUT
請輸入華氏溫度: 
f

id6
91       	 <--TYPE
258       	 <--LEFT
218       	 <--TOP
150       	 <--WIDTH
40       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
OUTPUT
攝氏溫度= 
c

id7
0       	 <--TYPE
254       	 <--LEFT
161       	 <--TOP
160       	 <--WIDTH
30       	 <--HEIGHT
16777215       	 <--BACKCOLOR
0       	 <--BORDERCOLOR
0       	 <--BORDERCOLOR
-reserved 1-
-reserved 2-
DEFINITION
c
(5.0 / 9.0) * (f - 32.0)
tmp
  
---- LINES ---- from,to ----
id6,id2
0

id1,id3
0

id3,id7
0

id7,id6
0

