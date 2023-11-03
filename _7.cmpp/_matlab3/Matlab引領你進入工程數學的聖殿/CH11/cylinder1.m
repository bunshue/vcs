function varargout=cylinder1(x,y,N)
%CYLINDER1   繪制磁柱
% CYLINDER1  繪制底面圓的圓心在原點，半徑為1，高度為1的圓柱
% CYLINDER1(X,Y)  繪制以X和Y構成的曲線為母線的高度為1的磁柱
% CYLINDER1(X,Y,N)  繪制以X和Y構成的曲線為母線的磁柱，並將其高度分為N等分
% H=CYLINDER1(...)  繪制磁柱並傳回其控制碼
% [XX,YY,ZZ]=CYLINDER1(...)  計算磁柱座標資料
%
% 輸導入參數數：
%     ---X,Y：母線的座標資料
%     ---N：磁柱高度的等分數
% 輸出參數：
%     ---H：磁柱的控制碼
%     ---XX,YY,ZZ：磁柱座標資料
%
% See also cylinder

if nargin<3
    N=2;
end
t=linspace(0,2*pi);
if nargin<1
    x=cos(t);y=sin(t);
end   
if length(x)~=length(y)
    error('曲線座標維數不符合.')
end
x=x(:); y=y(:);
X=repmat(x,1,N);
Y=repmat(y,1,N);
Z=repmat(linspace(0,1,N),length(x),1);
if nargout==0
    surf(X,Y,Z)
elseif nargout==1
    h=surf(X,Y,Z);
    varargout{1}=h;
else
    varargout{1}=X; varargout{2}=Y; varargout{3}=Z;
end