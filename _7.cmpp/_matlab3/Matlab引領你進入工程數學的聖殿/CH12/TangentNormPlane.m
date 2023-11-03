function n=TangentNormPlane(funx,funy,funz,t0,trange)
%TANGENTNORMPLANE   繪制空間曲線在某點處的切線和法平面
% TANGENTNORMPLANE(FUNX,FUNY,FUNZ,T0)  繪制空間曲線在[FUNX(T0),FUNY(T0),FUNZ(T0)]
%                                      處的切線和法平面，自變數範圍為[0,2*pi]
% TANGENTNORMPLANE(FUNX,FUNY,FUNZ,T0,TRANGE)  繪制空間曲線在[FUNX(T0),FUNY(T0),FUNZ(T0)]
%                                      處的切線和法平面，自變數範圍為TRANGE
% N=TANGENTNORMPLANE(...)  繪制空間曲線在某點處的切線和法平面，並傳回法向量
%
% 輸導入參數數：
%     ---FUNX,FUNY,FUNZ：空間曲線的參數方程式
%     ---T0：參數方程式自變數的值
%     ---TRANGE：指定繪圖範圍
% 輸出參數：
%     ---N：平面的法向量
%
% See also diff

if nargin==4
    trange=[0,2*pi];
end
if prod(t0-trange)>0
    error('t0 must in the interval trange.')
end
if ~isa(funx,'sym') || ~isa(funy,'sym') || ~isa(funz,'sym')
    error('FUNX,FUNY,FUNZ must be Symbolic functions.')
end
s=unique([symvar(funx),symvar(funy),symvar(funz)]);
if length(s)>1
    error('Too many Symbolic variables.')
end
x0=subs(funx,t0);
y0=subs(funy,t0);
z0=subs(funz,t0);
dfunx0=subs(diff(funx),t0);
dfuny0=subs(diff(funy),t0);
dfunz0=subs(diff(funz),t0);
t=linspace(trange(1),trange(2));
plot3(subs(funx,t),subs(funy,t),subs(funz,t),'k')
hold on
plot3(x0+dfunx0*t,y0+dfuny0*t,z0+dfunz0*t,'b','LineWidth',2)
if dfunx0~=0
    y=ylim; z=zlim;
    [Y,Z]=meshgrid(linspace(y(1),y(2)),linspace(z(1),z(2)));
    X=x0-(dfuny0*(Y-y0)+dfunz0*(Z-z0))/dfunx0;
elseif dfuny0~=0
    x=xlim; z=zlim;
    [X,Z]=meshgrid(linspace(x(1),x(2)),linspace(z(1),z(2)));
    Y=y0-(dfunx0*(X-x0)+dfunz0*(Z-z0))/dfuny0;
else
    x=xlim; y=ylim;
    [X,Y]=meshgrid(linspace(x(1),x(2)),linspace(y(1),y(2)));
    Z=z0-(dfunx0*(X-x0)+dfuy0*(Y-y0))/dfunz0;
end
surf(X,Y,Z)
shading interp
alpha(0.75)
if nargout>0
    n=[dfunx0,dfuny0,dfunz0];
end