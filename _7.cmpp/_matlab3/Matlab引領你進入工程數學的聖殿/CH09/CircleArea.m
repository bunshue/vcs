function A=CircleArea(R,n)
%CIRCLEAREA   �ꭱ�n���L���G��p��
% A=CIRCLEAREA(R,N)  �Q�Φh��έ��n�L���G��ꪺ���n
%
% ��ɤJ�ѼƼơG
%     ---R�G�ꪺ�b�|
%     ---N�G���h������
% ��X�ѼơG
%     ---A�G�ꪺ������n
%
% See also symsum

M=R;
A=sqrt(3)/4*M^2*6;
for k=2:n
    G=sqrt(R^2-(M/2)^2);
    j=R-G;
    m=sqrt((M/2)^2+j^2);
    a=1/2*M*j*3*2^(k-1);
    M=m;
    A=A+a;
end
if isa(R,'sym')
    A=simple(A);
end