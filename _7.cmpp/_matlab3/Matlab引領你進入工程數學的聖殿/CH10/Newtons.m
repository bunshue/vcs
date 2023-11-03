function [x,fval,iter,exitflag]=Newtons(fun,x0,eps,maxiter)
%NEWTONS   ���y�k�D�D�u�ʤ�{���s�ժ���
% X=NEWTONS(FUN,X0)  ���y�k�D�D�u�ʤ�{���s�ժ��ѡA�_�l���N�I��X0
% X=NEWTONS(FUN,X0,EPS)  ���y�k�D�D�u�ʤ�{���s�ժ��ѡA��׭n�D��EPS
% X=NEWTONS(FUN,X0,EPS,MAXITER)  ���y�k�D�D�u�ʤ�{���s�ժ��ѡA�̤j���N���Ƭ�MAXITER
% [X,FVAL]=NEWTONS(...)  ���y�k�D�D�u�ʤ�{���s�ժ��ѨöǦ^�ѳB����ƭ�
% [X,FVAL,ITER]=NEWTONS(...)  ���y�k�D�D�u�ʤ�{���s�ժ��ѨöǦ^���N����
% [X,FVAL,ITER,EXITFLAG]=NEWTONS(...)  ���y�k�D�D�u�ʤ�{���s�ժ��ѨöǦ^���N���\�Ч�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�D�u�ʤ�{���s�ժ��Ÿ���F��
%     ---X0�G�_�l���N�I�V�q
%     ---EPS�G��׭n�D�A�w�]�Ȭ�1e-6
%     ---MAXITER�G�̤j���N���ơA�w�]�Ȭ�1e4
% ��X�ѼơG
%     ---X�G�D�u�ʤ�{��������ѦV�q
%     ---FVAL�G�ѳB����ƭ�
%     ---ITER�G���N����
%     ---EXITFLAG�G���N���\�ЧӡA1��ܦ��\�A0��ܥ���
%
% See also newton

if nargin<2
    error('��ɤJ�ѼƼƦܤֻݭn2��.')
end
if nargin<3
    eps=1e-6;
end
if nargin<4
    maxiter=1e4;
end
if isa(fun,'inline')
    fun=char(fun);
    k=strfind(fun,'.');
    fun(k)=[];
    fun=sym(fun);
elseif ~isa(fun,'sym')
    error('��ƫ��A�����O���p��ƩβŸ����.')
end
s=symvar(fun);
if length(s)>length(x0)
    error('��ƪ��ۥ��ܼƹL�h.')
end
x0=x0(:);
J=jacobian(fun,s);
k=0;err=1;
exitflag=1;
while err>eps
    k=k+1;
    fx0=subs(fun,num2cell(s),num2cell(x0));
    J0=subs(J,num2cell(s),num2cell(x0));
    x1=x0-J0\fx0;
    err=norm(x1-x0);
    x0=x1;
    if k>=maxiter
        exitflag=0;
        break
    end
end
x=x1;
fval=fx0;
iter=k;