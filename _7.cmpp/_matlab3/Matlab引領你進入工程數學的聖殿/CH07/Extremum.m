function [X,FVAL,TYPE]=Extremum(fun,range)
%EXTREMUM   �D��Ʀb���w�϶��W�������I�η���
% X=EXTREMUM(FUN,RANGE)
% [X,FVAL]=EXTREMUM(...)
% [X,FVAL,TYPE]=EXTREMUM(...)
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ��Ÿ���F��
%     ---RANGE�G�D�Ȱ϶�
% ��X�ѼơG
%     ---X�G�����I
%     ---FVAL�G����
%     ---TYPE�G���ȫ��A�y�z
%
% See also diff, solve

x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('���fun�����u�]�A�@�ӲŸ��ܼ�.')
end
if ~isequal(x,s)
    fun=subs(fun,s,x);
end
df=diff(fun);
x0=unique(double(solve(df)));
d2f=diff(df);
N=length(x0);
X=[];
for kk=1:N
    if prod(x0(kk)-range)<=0
        X=[X,x0(kk)];
    end
end
FVAL=subs(fun,X);
D=subs(d2f,X);
TYPE=cell(1,N);
for k=1:N
    if D(k)==0
        TYPE{k}='���T�w';
    elseif D(k)>0
        TYPE{k}='���p��';
    else
        TYPE{k}='���j��';
    end
end