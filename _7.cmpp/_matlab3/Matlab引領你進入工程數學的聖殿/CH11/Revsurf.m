function varargout=Revsurf(x,fun,type)
%REVSURF   ø�������
% REVSURF(X,FUN)  ø��uFUN¶Z�b����ұo��������A�䤤FUN�O����Z�����
% REVSURF(X,FUN,TYPE)  ø��FUN¶Z�b����ұo��������A�䤤FUN��TYPE���w���ܼ�
% H=REVSURF(...)  ø�������öǦ^������ϧα���X
% [XX,YY,ZZ]=REVSURF(...)  �p�������y�и��
%
% ��ɤJ�ѼƼơG
%     ---X�G��ƪ����ܼƸ��
%     ---FUN�G�y�z���u�����
%     ---TYPE�G���w��ƪ����ܼơATYPE���H�U��ب��ȡG
%              1.'cylinder'��1�GFUN�O����Z�����
%              2.'revsurf'��2�GFUN�O����X��Y�����
% ��X�ѼơG
%     ---H�G������ϧα���X
%     ---XX,YY,ZZ�G������y�и��
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