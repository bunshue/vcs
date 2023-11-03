function varargout=cylinder1(x,y,N)
%CYLINDER1   ø��ϬW
% CYLINDER1  ø����ꪺ��ߦb���I�A�b�|��1�A���׬�1����W
% CYLINDER1(X,Y)  ø��HX�MY�c�������u�����u�����׬�1���ϬW
% CYLINDER1(X,Y,N)  ø��HX�MY�c�������u�����u���ϬW�A�ñN�䰪�פ���N����
% H=CYLINDER1(...)  ø��ϬW�öǦ^�䱱��X
% [XX,YY,ZZ]=CYLINDER1(...)  �p��ϬW�y�и��
%
% ��ɤJ�ѼƼơG
%     ---X,Y�G���u���y�и��
%     ---N�G�ϬW���ת�������
% ��X�ѼơG
%     ---H�G�ϬW������X
%     ---XX,YY,ZZ�G�ϬW�y�и��
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
    error('���u�y�к��Ƥ��ŦX.')
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