function [A,B,F] = fseriesquadl(fun,x,n,a,b)
%FSERIESQUADL   �Ÿ̸��żƪ��ƭȨD��
% [A,B,F]=FSERIESQUADL(FUN,X,N)  �D���FUN�b�϶�[-pi,pi]�W��N���ƭȳŸ̸��i��
% [A,B,F]=FSERIESQUADL(FUN,X,N,ALPHA,BETA)  �D���FUN�b���w�϶��W���ƭȳŸ̸��i��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���w���ݮi�}���
%     ---X�G���ܼƸ��
%     ---N�G�i�}����
%     ---ALPHA,BETA�G�żƮi�}�϶��A�w�]�Ȭ�[-pi,pi]
% ��X�ѼơG
%     ---A,B�G�Ÿ̸��t�ƦV�q
%     ---F�G��ƪ��Ÿ̸��i�}���bX�W����
%
% See also quadl, fseriessym

if nargin==3
    a=-pi;b=pi; 
end
L=(b-a)/2;
f=inline(fun);
var=char(argnames(f));
A=zeros(1,n+1);B=zeros(1,n);
A(1) = quadl(f,-L,L)/L; % �p��A_0
F=A(1)/2;
for k=1:n;
    fcos=inline(['(',fun,')','.*cos(',num2str(k*pi/L),'*',var,')']); 
    fsin=inline(['(',fun,')','.*sin(',num2str(k*pi/L),'*',var,')']); 
    A(k+1) =quadl(fcos,-L,L)/L;  % �p��t��A(2:n+1)
    B(k)=quadl(fsin,-L,L)/L;  % �p��t��B(1:n)
    F=F+A(k+1)*cos(k*pi*x/L)+B(k)*sin(k*pi*x/L);
end