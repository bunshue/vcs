function [Interval,type]=Monotonicity(varargin)
%MONOTONICITY   求函數在指定區域上的單調區間及單調性
% [INTERVAL,TYPE]=MONOTONICITY(FUN,DOMAIN)  求函數FUN在區間DOMAIN上的單調區間
% [INTERVAL,TYPE]=MONOTONICITY(FUN,DOMAIN,X0)  求函數FUN在區間DOMAIN上的單調
%                      區間，其中函數FUN一階導數的沒有定義的點（極點除外）已知
%
% 輸導入參數數：
%     ---FUN：函數表達式
%     ---DOMAIN：特殊的區間
%     ---X0：一階導數的沒有定義的點（極點除外）
% 輸出參數：
%     ---INTERVAL：傳回的單調區間
%     ---TYPE：各單調區間上函數的單調性
%
% See also solve, diff

warning off all
[fun,domain]=deal(varargin{1:2});
x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('函數fun必須只包括一個符號變數.')
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
    type{1}=Judgment(f1,{'單調減少','單調增加'});
else
    Interval{1}=[];
    type{1}=[];
end
for k=2:N
    Interval{k}=[x(k-1),x(k)];
    f=realfunvalue(df,sum(x([k-1,k]))/2);
    type{k}=Judgment(f,{'單調減少','單調增加'});
end
if ~isequal(x(end),domain(2))
    Interval{end}=[x(end),domain(2)];
    if isinf(domain(2))
        f2=realfunvalue(df,x(N)+0.1);
    else
        f2=realfunvalue(df,(x(N)+domain(2))/2);
    end
    type{N+1}=Judgment(f2,{'單調減少','單調增加'});
else
    Interval{N+1}=[];
    type{N+1}=[];
end