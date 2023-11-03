function [x,iter,exitflag]=Equ_iter(varargin)
%EQU_ITER   ���N�k�D�u�ʤ�{���s�ժ���
% X=EQU_ITER(A,B,'jacobi')  ���J�񭡥N�k�D�u�ʤ�{���s��AX=B����X�A�_�l���N�IX0�B
%                           ���EPS�M�̤j���N����ITER_MAX�����w�]��
% X=EQU_ITER(A,B,X0,EPS,ITER_MAX,'jacobi')  ���J�񭡥N�k�D�u�ʤ�{���s��AX=B����X
% [X,ITER]=EQU_ITER(...)  ���J�񭡥N�k�D�u�ʤ�{���s�ժ��ѨöǦ^���N����
% [X,ITER,EXITFLAG]=EQU_ITER(...)  ���J�񭡥N�k�D�u�ʤ�{���s�ժ��ѨöǦ^���N���ƩM���\�Ч�
% X=EQU_ITER(A,B,'seidel')  �����ɼw����k�D�u�ʤ�{���s��AX=B����X�A�_�l���N�IX0�B
%                           ���EPS�M�̤j���N����ITER_MAX�����w�]��
% X=EQU_ITER(A,B,X0,EPS,ITER_MAX,'seidel')  �����ɼw����k�D�u�ʤ�{���s��AX=B����X
% [X,ITER]=EQU_ITER(...,'seidel')  �����ɼw����k�D�u�ʤ�{���s��AX=B����X�öǦ^���N����
% [X,ITER,EXITFLAG]=EQU_ITER(...,'seidel')  �����ɼw����k�D�u�ʤ�{���s��AX=B����X�A
%                                           �öǦ^���N���ƩM���\�Ч�
% X=EQU_ITER(A,B,W,'sor')  SOR��k�D�u�ʤ�{���s��AX=B����X�A�_�l���N�IX0�B
%                          ���EPS�M�̤j���N����ITER_MAX�����w�]��
% X=EQU_ITER(A,B,W,X0,EPS,ITER_MAX,'sor')  SOR��k�D�u�ʤ�{���s��AX=B����X
% [X,ITER]=EQU_ITER(...,'sor')  SOR��k�D�u�ʤ�{���s��AX=B����X�öǦ^���N����
% [X,ITER,EXITFLAG]=EQU_ITER(...,'sor')  SOR��k�D�u�ʤ�{���s��AX=B����X�A
%                                        �öǦ^���N���ƩM���\�Ч�
%
% ��ɤJ�ѼƼơG
%     ---A�G�u�ʤ�{���s�ժ��t�Ưx�}
%     ---B�G�u�ʤ�{���s�ժ��k�ݶ�
%     ---W�G�W�Q���]�l
%     ---X0�G�_�l�V�q�A�w�]�Ȭ��s�V�q
%     ---EPS�G��׭n�D�A�w�]�Ȭ�1e-6
%     ---ITER_MAX�G�̤j���N���ơA�w�]�Ȭ�100
%     ---TYPE�G���N��k���A�ATYPE���H�U�X�ب��ȡG
%              1.'jacobi'��1�G���J�񭡥N�k
%              2.'seidel'��2�G�����ɼw�����N�k
%              3.'sor'��3�GSOR���N�k
% ��X�ѼơG
%     ---X�G�u�ʤ�{���s�ժ������
%     ---ITER�G���N����
%     ---EXITFLAG�G���N���\�P�_���ЧӡG1��ܭ��N���\�A0��ܭ��N����
% 
% See also Gauss

args=varargin;
style=args{end};
A=args{1};
b=args{2};
[m,n]=size(A);
if m~=n || length(b)~=m
    error('�u�ʤ�{���s�ժ��t�Ưx�}�M�`�q�����Ƥ��ŦX.')
end
iter=0;
exitflag=1;
D=diag(diag(A));
L=tril(A,-1);
U=triu(A,1);
switch lower(style)
    case {1,'jacobi'}  % Jacobi���N�k
        if nargin==3
            x0=zeros(n,1);
            eps=1e-6;
            iter_max=100;
        elseif nargin==6
            [x0,eps,iter_max]=deal(args{3:5});
        else
            error('��ɤJ�ѼƼƭӼƦ��~.')
        end
        J=-inv(D)*(L+U);f=D\b;
        while iter<iter_max
            x=J*x0+f;
            if norm(x-x0,inf)<eps
                break
            end
            x0=x;iter=iter+1;
        end
    case {2,'seidel'}  % Gauss-Seidel���N�k
        if nargin==3
            x0=zeros(n,1);
            eps=1e-6;
            iter_max=100;
        elseif nargin==6
            [x0,eps,iter_max]=deal(args{3:5});
        else
            error('��ɤJ�ѼƼƭӼƦ��~.')
        end
        G=-inv(D+L)*U;f_G=(D+L)\b;
        while iter<iter_max
            x=G*x0+f_G;
            if norm(x-x0,inf)<eps
                break
            end
            x0=x;iter=iter+1;
        end
    case {3,'sor'}  % SOR���N�k
        w=args{3};
        if nargin==4
            x0=zeros(n,1);
            eps=1e-6;
            iter_max=100;
        elseif nargin==7
            [x0,eps,iter_max]=deal(args{4:6});
        else
            error('��ɤJ�ѼƼƭӼƦ��~.')
        end
        S=(D+w*L)\((1-w)*D-w*U);f_w=w*((D+w*L)\b);
        while iter<iter_max
            x=S*x0+f_w;
            if norm(x-x0,inf)<eps
                break
            end
            x0=x;iter=iter+1;
        end
    otherwise
        error('Illegal options.')
end
if iter==iter_max
    exitflag=0;
end