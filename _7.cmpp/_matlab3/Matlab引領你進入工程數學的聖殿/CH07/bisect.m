function [x,fx,iter,X]=bisect(fun,a,b,eps,varargin)
%BISECT   �G���k�D��{������
% X=BISECT(FUN,A,B)
% X=BISECT(FUN,A,B,EPS)
% X=BISECT(FUN,A,B,EPS,P1,P2,...)
% [X,FX]=BISECT(...)
% [X,FX,ITER]=BISECT(...)
% [X,FX,ITER,XS]=BISECT(...)
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��{������ƴy�z�A�i�H���ΦW��ơB���p��Ʃ�M�ɮקΦ�
%     ---A,B�G�϶����I
%     ---EPS�G��׳]�w
%     ---P1,P2,...�G��{�������[�Ѽ�
% ��X�ѼơG
%     ---X�G�Ǧ^����{������
%     ---FX�G��{���ڹ�������ƭ�
%     ---ITER�G���N����
%     ---XS�G���N�ڧǦC
%
% See also fzero, RootInterval

if nargin<3
    error('��ɤJ�ѼƼƦܤֻݭn3�ӡI')
end
if nargin<4 || isempty(eps)
    eps=1e-6;
end
fa=feval(fun,a,varargin{:});
fb=feval(fun,b,varargin{:});
% fa=fun(a,varargin{:});fb=fun(b,varargin{:});
k=1;
if fa*fb>0  % �������G���k�ϥα���
    warning(['�϶�[',num2str(a),',',num2str(b),']���i��S����']);
elseif fa==0  % �϶������I����
    x=a; fx=fa;
elseif fb==0  % �϶��k���I����
    x=b; fx=fb;
else
    while abs(b-a)>eps;  % ����G���k��������
        x=(a+b)/2;  % �G���϶����I
        fx=feval(fun,x,varargin{:}); % �p�⤤�I����ƭ�
        if fa*fx>0;  % ����
            a=x;   % ���I��s
            fa=fx;  % ���I��ƭȧ�s
        elseif fb*fx>0;  % ����
            b=x;  % ���I��s
            fb=fx;  % ���I��ƭȧ�s
        else
            break
        end
        X(k)=x;
        k=k+1;
    end
end
iter=k;