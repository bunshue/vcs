function PI=CalculatePI(n)
%CALCULATEPI   ��P�vPI���żƺ�k
% PI=CALCULATEPI(N)  �Q�ξ��żƭp���P�v����
%
% ��ɤJ�ѼƼơG
%     ---N�G�żƩҨ�������
% ��X�ѼơG
%     ---PI�G��P�v�������
%
% See also pi

if nargin==0
    n=1000;
end
PI=0;
for k=1:n
    a=(-1)^(k-1)/(2*k-1);
    PI=PI+a;
end
PI=4*PI;