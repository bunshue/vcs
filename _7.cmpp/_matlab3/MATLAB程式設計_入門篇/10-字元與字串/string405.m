A = [1 2 1; 3 5 6 ];  
B = mat2str(A)		% �N�x�} A �ন�r�� B   
A2 = eval(B);		% �A�N�r�� B ��^�x�} A2
isequal(A, A2)		% ���� A �M A2 �O�_�۵�