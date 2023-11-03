function n=TangentPlaneNormLine(F,M)
%TANGENTPLANENORMLINE   ø����W�Y�I�B���������M�k�u
% TANGENTPLANENORMLINE(F,M0)  ø���F�bM0�W���k�u�M������
% N=TANGENTPLANENORMLINE(F,M0)  ø���F�bM0�W���k�u�M�������A�öǦ^���������k�V�q
%
% ��ɤJ�ѼƼơG
%     ---F�G������{�����Ÿ���F��
%     ---M0�G�����W���@�I
% ��X�ѼơG
%     ---N�G���������k�V�q
%
% See also TangentNormPlane

if ~isa(F,'sym')
    error('F must a Symbolic function.')
end
x0=M(1); y0=M(2); z0=M(3);
dFx0=subs(diff(F,'x'),{'x','y','z'},num2cell(M));
dFy0=subs(diff(F,'y'),{'x','y','z'},num2cell(M));
dFz0=subs(diff(F,'z'),{'x','y','z'},num2cell(M));
if ~ishold
    hold on
end
x_Lim=xlim;
t=linspace(0,diff(x_Lim)/5);
plot3(x0+dFx0*t,y0+dFy0*t,z0+dFz0*t,'b','LineWidth',2)
if dFx0~=0
    y=ylim; z=zlim;
    [Y,Z]=meshgrid(linspace(y(1),y(2)),linspace(z(1),z(2)));
    X=x0-(dFy0*(Y-y0)+dFz0*(Z-z0))/dFx0;
elseif dFy0~=0
    x=xlim; z=zlim;
    [X,Z]=meshgrid(linspace(x(1),x(2)),linspace(z(1),z(2)));
    Y=y0-(dFx0*(X-x0)+dFz0*(Z-z0))/dFy0;
else
    x=xlim; y=ylim;
    [X,Y]=meshgrid(linspace(x(1),x(2)),linspace(y(1),y(2)));
    Z=z0-(dFx0*(X-x0)+dFy0*(Y-y0))/dFz0;
end
surf(X,Y,Z)
shading interp
alpha(0.75)
if nargout>0
    n=[dFx0,dFy0,dFz0];
end