function [x,fx,iter,X]=newton(fun,x0,eps,maxiter)
%NEWTON   ���y�k�D��{������
% X=NEWTON(FUN,X0)  ���y�k�D��{���b�_�l�IX0�B����
% X=NEWTON(FUN,X0,EPS)  ���y�k�D��{���b�_�l�IX0�B����׬�EPS����
% X=NEWTON(FUN,X0,EPS,MAXITER)  ���y�k�D��{�����ڨó]�w�̤j���N����
% [X,FX]=NEWTON(...)  ���y�k�D�ڡA�öǦ^�ڳB����ƭ�
% [X,FX,ITER]=NEWTON(...)  ���y�k�D�ڨöǦ^�ڳB����ƭȥH�έ��N����
% [X,FX,ITER,XS]=NEWTON(...)  ���y�k�D�ڨöǦ^�ڳB����ƭȡB���N���ƥH�έ��N�ڧǦC
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��{������ƴy�z�A�i�H���ΦW��ơB���p��Ʃ�M�ɮקΦ�
%     ---X0�G�_�l���N�I
%     ---EPS�G��׳]�w
%     ---MAXITER�G�̤j���N����
% ��X�ѼơG
%     ---X�G�Ǧ^����{������
%     ---FX�G��{���ڹ�������ƭ�
%     ---ITER�G���N����
%     ---XS�G���N�ڧǦC
%
% See also fzero, RootInterval, bisect

if nargin<2
    error('��ɤJ�ѼƼƦܤֻݭn2�ӡI')
end
if nargin<3 || isempty(eps)
    eps=1e-6;
end
if nargin<4 || isempty(maxiter)
    maxiter=1e4;
end
s=symvar(fun);
if length(s)>1
    error('���fun�����u�]�A�@�ӲŸ��ܼ�.')
end
df=diff(fun,s);
k=0;err=1;
while abs(err)>eps
    k=k+1;
    fx0=subs(fun,s,x0);
    dfx0=subs(df,s,x0);
    if dfx0==0
        error('f(x)�bx0�B���ɼƬ�0�A����p��')
    end
    x1=x0-fx0/dfx0;
    err=x1-x0;
    x0=x1;
    X(k)=x1;
end
if k>=maxiter
    error('���N���ƶW���A���N���ѡI')
end
x=x1;fx=subs(fun,x);iter=k;X=X';