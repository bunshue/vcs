function Evolute_Draw(varargin)
%EVOLUTE_DRAW   酶Ρ絬亥﹠絬
% EVOLUTE_DRAW(FUN,RANGE)
% EVOLUTE_DRAW(FUNX,FUNY,RANGE)
%
% 块旧把计计
%     ---FUNΡ絬ㄧ计よ祘Α
%     ---FUNX,FUNYΡ絬ㄧ计把计よ祘Α
%     ---RANGE酶瓜跋丁
%
% See also diff, diff_para

args=varargin;
range=args{end};
if nargin==2
    y=args{1};
    x=sym('x','real');
    s=symvar(y);
    if length(s)>1
        error('ㄧ计funゲ斗珹才腹跑计.')
    end
    if ~isequal(x,s)
        y=subs(fun,s,x);
    end
    df=simple(diff(y,x));
    d2f=simple(diff(df,x));
elseif nargin==3
    x=args{1}; y=args{2};
    t=sym('t','real');
    s=unique([symvar(x),symvar(y)]);
    if length(s)>1
        error('ㄧ计funx㎝funyゲ斗珹才腹跑计.')
    end
    if ~isequal(t,s)
        x=subs(x,s,t);
        y=subs(y,s,t);
    end
    df=simple(diff_para(y,x,t,1));
    d2f=simple(diff_para(y,x,t,2));
else
    error('The number of input arguments is illegal.')
end
X=inline(x);
Y=inline(y);
alpha=inline(simple(x-df*(1+df^2)/d2f));
beta=inline(simple(y+(1+df^2)/d2f));
theta=linspace(range(1),range(2),300);
plot(X(theta),Y(theta),'k',alpha(theta),beta(theta),'r--')
xx=sort([X(range),alpha(range)]);
xlim([xx(1) xx(end)])