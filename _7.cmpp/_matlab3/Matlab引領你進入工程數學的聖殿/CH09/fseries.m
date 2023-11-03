function [A,B,F,type]=fseries(f,x,n,a,b)
%FSERIES   �Ÿ̸��żƨD�ѡA�öǦ^�Ÿ̸��żƪ����A
% [A,B,F]=FSERIES(FUN,X,N)  �D�_(�ΰ�)���FUN�b�϶�[-pi,pi]�W��N���Ÿ̸��i��
% [A,B,F]=FSERIES(FUN,X,N,ALPHA,BETA)  �D�_(�ΰ�)���FUN�b���w�϶��W��N���Ÿ̸��i��
% [A,B,F,TYPE]=FSERIES(...)  �D��ƪ��Ÿ̸��i���öǦ^�Ÿ̸��żƫ��A
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���w���ݮi�}���
%     ---X�G���ܼ�
%     ---N�G�i�}����
%     ---ALPHA,BETA�G�żƮi�}�϶��A�w�]�Ȭ�[-pi,pi]
% ��X�ѼơG
%     ---A,B�G�Ÿ̸��t�ƦV�q
%     ---F�G��ƪ��Ÿ̸��i�}��
%     ---TYPE�G�Ÿ̸��żƫ��A�r��
%
% See also int, fseriessym, fseriesquadl

if nargin==3
    a=-pi;b=pi;
end
L=(b-a)/2;
f1=subs(f,-x);
A=sym(zeros(1,n+1));
B=sym(zeros(1,n));
F=0;
if isequal(simple(f+f1),0)  % �_���
    for k=1:n
        B(k)=2*int(f*sin(k*pi*x/L),x,0,L)/L;
        F=F+B(k)*sin(k*pi*x/L);
    end
    type='�����ż�';
elseif isequal(f,f1)  % �����
    for k=0:n
        A(k+1)=2*int(f*cos(k*pi*x/L),x,0,L)/L;
        F=F+A(k+1)*cos(k*pi*x/L);
    end
    type='�E���ż�';
else  % �@����
    A(1)=int(f,x,-L,L)/L;
    F=A(1)/2;
    for k=1:n
        A(k+1)=int(f*cos(k*pi*x/L),x,-L,L)/L;
        B(k)=int(f*sin(k*pi*x/L),x,-L,L)/L;
        F=F+A(k+1)*cos(k*pi*x/L)+B(k)*sin(k*pi*x/L);
    end
    type='�@��T���ż�';
end