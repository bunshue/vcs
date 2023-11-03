function [X,FVAL,TYPE]=Extremum(fun,range)
%EXTREMUM   求函數在指定區間上的極值點及極值
% X=EXTREMUM(FUN,RANGE)
% [X,FVAL]=EXTREMUM(...)
% [X,FVAL,TYPE]=EXTREMUM(...)
%
% 輸導入參數數：
%     ---FUN：函數的符號表達式
%     ---RANGE：求值區間
% 輸出參數：
%     ---X：極值點
%     ---FVAL：極值
%     ---TYPE：極值型態描述
%
% See also diff, solve

x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('函數fun必須只包括一個符號變數.')
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
        TYPE{k}='不確定';
    elseif D(k)>0
        TYPE{k}='極小值';
    else
        TYPE{k}='極大值';
    end
end