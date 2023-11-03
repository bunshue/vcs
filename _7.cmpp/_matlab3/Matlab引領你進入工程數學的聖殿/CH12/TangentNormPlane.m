function n=TangentNormPlane(funx,funy,funz,t0,trange)
%TANGENTNORMPLANE   ø��Ŷ����u�b�Y�I�B�����u�M�k����
% TANGENTNORMPLANE(FUNX,FUNY,FUNZ,T0)  ø��Ŷ����u�b[FUNX(T0),FUNY(T0),FUNZ(T0)]
%                                      �B�����u�M�k�����A���ܼƽd��[0,2*pi]
% TANGENTNORMPLANE(FUNX,FUNY,FUNZ,T0,TRANGE)  ø��Ŷ����u�b[FUNX(T0),FUNY(T0),FUNZ(T0)]
%                                      �B�����u�M�k�����A���ܼƽd��TRANGE
% N=TANGENTNORMPLANE(...)  ø��Ŷ����u�b�Y�I�B�����u�M�k�����A�öǦ^�k�V�q
%
% ��ɤJ�ѼƼơG
%     ---FUNX,FUNY,FUNZ�G�Ŷ����u���ѼƤ�{��
%     ---T0�G�ѼƤ�{�����ܼƪ���
%     ---TRANGE�G���wø�Ͻd��
% ��X�ѼơG
%     ---N�G�������k�V�q
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