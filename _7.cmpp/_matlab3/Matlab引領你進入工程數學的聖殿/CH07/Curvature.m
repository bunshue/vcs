function K=Curvature(varargin)
%CURVATURE   ―ㄧ计Ρ瞯
% K=CURVATURE(FUN,X)
% K=CURVATURE(FUNX,FUNY,T)
%
% 块旧把计计
%     ---FUNㄧ计よ祘Α
%     ---FUNX,FUNYㄧ计把计よ祘Α
%     ---X,Tㄧ计才腹跑计
% 块把计
%     ---KΡ瞯
%
% See also diff

args=varargin;
if nargin==2
    fun=args{1}; x=args{2};
    df=diff(fun,x);
    d2f=diff(df,x);
    K=abs(d2f)/(1+df^2)^(3/2);
elseif nargin==3
    funx=args{1}; funy=args{2}; t=args{3};
    dx=diff(funx,t);
    d2x=diff(dx,t);
    dy=diff(funy,t);
    d2y=diff(dy,t);
    K=abs(dx*d2y-dy*d2x)/(dx^2+dy^2)^(3/2);
end