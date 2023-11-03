function varargout=Revsurf(x,fun,type)
%REVSURF   繪制旋轉體
% REVSURF(X,FUN)  繪制曲線FUN繞Z軸旋轉所得的旋轉體，其中FUN是關於Z的函數
% REVSURF(X,FUN,TYPE)  繪制FUN繞Z軸旋轉所得的旋轉體，其中FUN由TYPE指定自變數
% H=REVSURF(...)  繪制旋轉體並傳回旋轉體圖形控制碼
% [XX,YY,ZZ]=REVSURF(...)  計算旋轉體座標資料
%
% 輸導入參數數：
%     ---X：函數的自變數資料
%     ---FUN：描述曲線的函數
%     ---TYPE：指定函數的自變數，TYPE有以下兩種取值：
%              1.'cylinder'或1：FUN是關於Z的函數
%              2.'revsurf'或2：FUN是關於X或Y的函數
% 輸出參數：
%     ---H：旋轉體圖形控制碼
%     ---XX,YY,ZZ：旋轉體座標資料
%
% See also cylinder

if nargin==2
    type='cylinder';
end
switch lower(type)
    case {1,'cylinder'}
        xL=min(x(:)); xR=max(x(:));
        [xx,yy,zz]=cylinder(fun(x),40);
        zz=xL+(xR-xL)*zz;
    case {2,'revsurf'}
        [theta,rho]=meshgrid(linspace(0,2*pi),x);
        [xx,yy]=pol2cart(theta,rho);
        R=sqrt(xx.^2+yy.^2);
        zz=fun(R);
    otherwise
        error('Illegal options.')
end
if nargout==0
    surf(xx,yy,zz)
elseif nargout==1
    varargout{1}=surf(xx,yy,zz);
elseif nargout==3
    varargout{1}=xx; varargout{2}=yy; varargout{3}=zz;
else
    error('The number of output arguments is Illegal.')
end