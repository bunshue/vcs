function I=quad_inf(fun,a,b,tol,eps)
%QUAD_INF   �L�a���ϱ`�n�����L�a�϶��G��k
% I=QUAD_INF(FUN,A,B)  �D���FUN�b�϶�[A,B]�W���ƭȿn���AA��B�i�H���L�a�A�U�P
% I=QUAD_INF(FUN,A,B,TOL)  �D���FUN�b�϶�[A,B]�W���ƭȿn���A�e�t��TOL
% I=QUAD_INF(FUN,A,B,TOL,EPS)  �D�L�a���ϱ`�n���A��׬�EPS
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�Q�n���
%     ---A,B�G�n���϶������I�A�n�DA<B
%     ---TOL�G�e�t�A�w�]�Ȭ�1e-6
%     ---EPS�G��׭n�D�A���N�פ��h�A�w�]�Ȭ�1e-5
% ��X�ѼơG
%     ---I�G�D�o���n����
%
% See also quadgk, quadl

if nargin<5 || isempty(eps)
    eps=1e-5;
end;
if nargin<4 || isempty(tol)
    tol=1e-6;
end;
N=2;I=0;T=1;
if isinf(a) && isinf(b)
    I=quad_inf(fun,-inf,0)+quad_inf(fun,0,inf);  % ���k�I�s
elseif isinf(b)
    while T>eps
        b=a+N;
        T=quadl(fun,a,b,tol);
        I=I+T;
        a=b; N=2*N;
    end
elseif isinf(a)
    while T>eps
        a=b-N;
        T=quadl(fun,a,b,tol);
        I=I+T;
        b=a; N=2*N;
    end
else
    I=quadl(fun,a,b,tol);
end