function [Interval,type,Inflexion]=Concavity(varargin)
%CONCAVITY   �D��Ʀb���w�ϰ�W���W�Y�϶��Ω��I
% [INTERVAL,TYPE,INFLEXION]=CONCAVITY(FUN,DOMAIN)  �D���FUN�b�϶�DOMAIN�W��
%                                   �W�Y�϶��M���I�H�ΦU�W�Y�϶��W���u���W�Y��
% [INTERVAL,TYPE,INFLEXION]=CONCAVITY(FUN,DOMAIN,X0)  �D���FUN�b�϶�DOMAIN�W
%         ���W�Y�϶��M���I�H�ΦU�W�Y�϶��W���u���W�Y�ʡA�䤤�G���ɼƵL�w�q�I�w��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ�F��
%     ---DOMAIN�G���w�϶�
% ��X�ѼơG
%     ---INTERVAL�G�W�Y�϶�
%     ---TYPE�G�U�W�Y�϶��W���u���W�Y��
%     ---INFLEXION�G���I
%
% See also solve, diff, Monotonicity

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
df=diff(fun,2);
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
Inflexion=[];
if ~isequal(domain(1),x(1))
    Interval{1}=[domain(1),x(1)];
    if isinf(domain(1))
        f1=realfunvalue(df,x(1)-0.1);
    else
        f1=realfunvalue(df,(domain(1)+x(1))/2);
    end
    type{1}=Judgment(f1,{'�Y��','�W��'});
else
    Interval{1}=[];
    type{1}=[];
end
for k=2:N
    Interval{k}=[x(k-1),x(k)];
    f=realfunvalue(df,sum(x([k-1,k]))/2);
    type{k}=Judgment(f,{'�Y��','�W��'});
end
if ~isequal(x(end),domain(2))
    Interval{end}=[x(end),domain(2)];
    if isinf(domain(2))
        f2=realfunvalue(df,x(N)+0.1);
    else
        f2=realfunvalue(df,(x(N)+domain(2))/2);
    end
    type{N+1}=Judgment(f2,{'�Y��','�W��'});
else
    Interval{N+1}=[];
    type{N+1}=[];
end
for k=2:N+1
    if all(strcmp(type(k-1:k),{'�W��','�Y��'})) ||...
            all(strcmp(type(k-1:k),{'�Y��','�W��'}))
        Inflexion=[Inflexion,x(k-1)];
    end
end
