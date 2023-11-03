function varargout=quadric(varargin)
%QUADRIC   ø��G������
% QUADRIC('elliptic',XC,YC,ZC,A,B,N)  ø�����@��
% QUADRIC('ellipsoid',XC,YC,ZC,A,B,C,N)  ø���y��
% QUADRIC('hyperboloidofonesheet',XC,YC,ZC,A,B,C,N)  ø��渭������
% QUADRIC('hyperboloidoftwosheets',XC,YC,ZC,A,B,C,N)  ø������������
% QUADRIC('ellipticparaboloid',XC,YC,ZC,A,B,N)  ø����ߪ���
% QUADRIC('hyperbolicparaboloid',A,B,N)  ø�������ߪ���
% H=QUADRIC(...)  ø��G�������öǦ^�䱱��X
% [X,Y,Z]=QUADRIC(...)  �p��G���������y�и��
%
% ��ɤJ�ѼƼơG
%     ---XC,YC,ZC�G�G�����������߮y��
%     ---A,B,C�G�G���������Ѽ�
%     ---N�G���w�����I��
%     ---TYPE�G���w�G���������A�A���W�z6�ب���
% ��X�ѼơG
%     ---H�G�G������������X
%     ---X,Y,Z�G�G���������y�и��
%
% See also cylinder, ellipsoid

args=varargin;
type=args{1};
switch lower(type)
    case {1,'elliptic','����@��'}
        [xc,yc,zc,a,b,n]=deal(args{2:end});
        z=linspace(-a,a);
        [X,Y,Z]=cylinder(a*z,n);
        X=X+xc;
        Y=b/a*Y+yc;
        Z=-a+2*a*Z+zc;
    case {2,'ellipsoid','��y��'}
        [xc,yc,zc,a,b,c,n]=deal(args{2:end});
        [X,Y,Z]=ellipsoid(xc,yc,zc,a,b,c,n);
    case {3,'hyperboloidofonesheet','�渭������'}
        % �ѼƤ�{���G
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
    case {4,'hyperboloidoftwosheets','����������'}
        [xc,yc,zc,a,b,c,n]=deal(args{2:end});
        t=linspace(-pi/2.5,pi/2.5,n);
        p=linspace(-pi,pi,30);
        [T,P]=meshgrid(t,p);
        X=a*sec(T)+xc;
        Y=b*tan(T).*cos(P)+yc;
        Z=c*tan(T).*sin(P)+zc;
    case {5,'ellipticparaboloid','���ߪ���'}
        [xc,yc,zc,a,b,n]=deal(args{2:end});
        z=linspace(0,abs(a));
        [X,Y,Z]=cylinder(abs(a)*sqrt(z),n);
        X=X+xc;
        Y=b/a*Y+yc;
        Z=Z+zc;
    case {6,'hyperbolicparaboloid','�����ߪ���'}
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