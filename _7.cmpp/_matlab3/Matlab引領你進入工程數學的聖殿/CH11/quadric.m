function varargout=quadric(varargin)
%QUADRIC   繪制二次曲面
% QUADRIC('elliptic',XC,YC,ZC,A,B,N)  繪制橢圓錐面
% QUADRIC('ellipsoid',XC,YC,ZC,A,B,C,N)  繪制橢球面
% QUADRIC('hyperboloidofonesheet',XC,YC,ZC,A,B,C,N)  繪制單葉雙曲面
% QUADRIC('hyperboloidoftwosheets',XC,YC,ZC,A,B,C,N)  繪制雙葉雙曲面
% QUADRIC('ellipticparaboloid',XC,YC,ZC,A,B,N)  繪制橢圓拋物面
% QUADRIC('hyperbolicparaboloid',A,B,N)  繪制雙曲拋物面
% H=QUADRIC(...)  繪制二次曲面並傳回其控制碼
% [X,Y,Z]=QUADRIC(...)  計算二次曲面的座標資料
%
% 輸導入參數數：
%     ---XC,YC,ZC：二次曲面的中心座標
%     ---A,B,C：二次曲面的參數
%     ---N：指定取樣點數
%     ---TYPE：指定二次曲面型態，有上述6種取值
% 輸出參數：
%     ---H：二次曲面的控制碼
%     ---X,Y,Z：二次曲面的座標資料
%
% See also cylinder, ellipsoid

args=varargin;
type=args{1};
switch lower(type)
    case {1,'elliptic','橢圓錐面'}
        [xc,yc,zc,a,b,n]=deal(args{2:end});
        z=linspace(-a,a);
        [X,Y,Z]=cylinder(a*z,n);
        X=X+xc;
        Y=b/a*Y+yc;
        Z=-a+2*a*Z+zc;
    case {2,'ellipsoid','橢球面'}
        [xc,yc,zc,a,b,c,n]=deal(args{2:end});
        [X,Y,Z]=ellipsoid(xc,yc,zc,a,b,c,n);
    case {3,'hyperboloidofonesheet','單葉雙曲面'}
        % 參數方程式：
        % x=a*sec(t)*cos(p)
        % y=b*sec(t)*sin(p)
        % z=c*tan(t)
        [xc,yc,zc,a,b,c,n]=deal(args{2:end});
        t=linspace(-pi/2.5,pi/2.5,n);
        p=linspace(-pi,pi,30);
        [T,P]=meshgrid(t,p);
        X=a*sec(T).*cos(P)+xc;
        Y=b*sec(T).*sin(P)+yc;
        Z=c*tan(T)+zc;
    case {4,'hyperboloidoftwosheets','雙葉雙曲面'}
        [xc,yc,zc,a,b,c,n]=deal(args{2:end});
        t=linspace(-pi/2.5,pi/2.5,n);
        p=linspace(-pi,pi,30);
        [T,P]=meshgrid(t,p);
        X=a*sec(T)+xc;
        Y=b*tan(T).*cos(P)+yc;
        Z=c*tan(T).*sin(P)+zc;
    case {5,'ellipticparaboloid','橢圓拋物面'}
        [xc,yc,zc,a,b,n]=deal(args{2:end});
        z=linspace(0,abs(a));
        [X,Y,Z]=cylinder(abs(a)*sqrt(z),n);
        X=X+xc;
        Y=b/a*Y+yc;
        Z=Z+zc;
    case {6,'hyperbolicparaboloid','雙曲拋物面'}
        [a,b,n]=deal(args{2:end});
        x=linspace(-a^2, a^2,n);
        y=linspace(-b^2, b^2,n);
        [X,Y]=meshgrid(x,y);
        Z=X.^2/a^2-Y.^2/b^2;
end
if nargout==0
    surf(X,Y,Z)
elseif nargout==1
    h=surf(X,Y,Z);
    varargout{1}=h;
elseif nargout==3
    varargout{1}=X; varargout{2}=Y; varargout{3}=Z;
else
    error('The Number of output arguments is wrong.')
end