function [Interval,type]=Monotonicity(varargin)
%MONOTONICITY   �D��Ʀb���w�ϰ�W����հ϶��γ�թ�
% [INTERVAL,TYPE]=MONOTONICITY(FUN,DOMAIN)  �D���FUN�b�϶�DOMAIN�W����հ϶�
% [INTERVAL,TYPE]=MONOTONICITY(FUN,DOMAIN,X0)  �D���FUN�b�϶�DOMAIN�W�����
%                      �϶��A�䤤���FUN�@���ɼƪ��S���w�q���I�]���I���~�^�w��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ�F��
%     ---DOMAIN�G�S���϶�
%     ---X0�G�@���ɼƪ��S���w�q���I�]���I���~�^
% ��X�ѼơG
%     ---INTERVAL�G�Ǧ^����հ϶�
%     ---TYPE�G�U��հ϶��W��ƪ���թ�
%
% See also solve, diff

warning off all
[fun,domain]=deal(varargin{1:2});
x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('���fun�����u�]�A�@�ӲŸ��ܼ�.')
end
if ~isequal(x,s)
    fun=subs(fun,s,x);
end
df=diff(fun);
[num,den]=numden(df);
xd=solve(den);
xd=double(xd);
x=solve(num);
x=double(x);
x=unique([xd(:);x(:)]);
if nargin==3
    x0=varargin{3};
    x=unique([x;x0(:)]);
end
N=length(x);
Interval=cell(1,N+1);
type=cell(1,N+1);
if ~isequal(domain(1),x(1))
    Interval{1}=[domain(1),x(1)];
    if isinf(domain(1))
        f1=realfunvalue(df,x(1)-0.1);
    else
        f1=realfunvalue(df,(domain(1)+x(1))/2);
    end
    type{1}=Judgment(f1,{'��մ��','��ռW�['});
else
    Interval{1}=[];
    type{1}=[];
end
for k=2:N
    Interval{k}=[x(k-1),x(k)];
    f=realfunvalue(df,sum(x([k-1,k]))/2);
    type{k}=Judgment(f,{'��մ��','��ռW�['});
end
if ~isequal(x(end),domain(2))
    Interval{end}=[x(end),domain(2)];
    if isinf(domain(2))
        f2=realfunvalue(df,x(N)+0.1);
    else
        f2=realfunvalue(df,(x(N)+domain(2))/2);
    end
    type{N+1}=Judgment(f2,{'��մ��','��ռW�['});
else
    Interval{N+1}=[];
    type{N+1}=[];
end