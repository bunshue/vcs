function varargout=max_min(fun,xrange,yrange,type)
%MAX_MIN   ���Ҧ��ɳ��ϰ�W�G����ƪ����ȩw�z
% MAX_MIN(FUN,XRANGE,YRANGE)  �ϧΤƤ�k�ܽd���ɳ��ϰ�W�G����ƪ����ȩw�z
% MAX_MIN(FUN,XRANGE,YRANGE,TYPE)  �ϧΤƤ�k�ܽd���ɳ��ϰ�W�G����ƪ����ȩw�z�A
%                                  �ϧΥi�H�������ܼҦ��G'rect'�M'circ'
% [ZMAX,ZMIN]=MAX_MIN(...)  �Ǧ^��Ʀb���w�ϰ�W���̤j�ȩM�̤p��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���w���G�����
%     ---XRANGE,YRANGE�G���ܼƽd��
%     ---TYPE�G�ϧ�ø��A�A��'rect'�M'circ'��Ө���
% ��X�ѼơG
%     ---ZMAX,ZMIN�G��ƪ��̤j�ȩM�̤p��
%
% See also ezsurf, max, min

if nargin==3
    type='circ';
end
if ~any(strcmp(type,{'rect','circ'}))
    error('The Input argument type must be either ''rect'' or ''circ''.')
end
h=ezsurf(fun,[xrange yrange],type);
X=get(h,'XData');
Y=get(h,'YData');
Z=get(h,'ZData');
zmax=max(Z(:));
zmin=min(Z(:));
hold on
surf(X,Y,zmax*ones(size(X)))
surf(X,Y,zmin*ones(size(X)))
shading interp
if nargout>0
    varargout{1}=zmax;varargout{2}=zmin;
end