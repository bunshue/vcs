function [A,B,F]=fseriessym(f,x,n,a,b)
%FSERIESSYM   �Ÿ̸��żƪ��Ÿ��D��
% [A,B,F]=FSERIESSYM(FUN,X,N)  �N���FUN�b�϶�[-pi,pi]�W�i��N���Ÿ̸��ż�
% [A,B,F]=FSERIESSYM(FUN,X,N,ALPHA,BETA)  �N���FUN�b���w�϶��W�i��N���Ÿ̸��ż�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���w���ݮi�}���
%     ---X�G���ܼ�
%     ---N�G�i�}����
%     ---ALPHA,BETA�G�żƮi�}�϶��A�w�]�Ȭ�[-pi,pi]
% ��X�ѼơG
%     ---A,B�G�Ÿ̸��t�ƦV�q
%     ---F�G��ƪ��Ÿ̸��i�}��
%
% See also int

if nargin==3
    a=-pi;b=pi; 
end
L=(b-a)/2; 
A=int(f,x,-L,L)/L;
B=[];F=A/2;
for k=1:n
   ak=int(f*cos(k*pi*x/L),x,-L,L)/L;
   bk=int(f*sin(k*pi*x/L),x,-L,L)/L;
   A=[A,ak];
   B=[B,bk];
   F=F+ak*cos(k*pi*x/L)+bk*sin(k*pi*x/L);
end