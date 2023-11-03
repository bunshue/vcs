function varargout=max_min(fun,xrange,yrange,type)
%MAX_MIN   喷靡Τ超跋办じㄧ计ざ﹚瞶
% MAX_MIN(FUN,XRANGE,YRANGE)  瓜てよ猭ボ絛Τ超跋办じㄧ计ざ﹚瞶
% MAX_MIN(FUN,XRANGE,YRANGE,TYPE)  瓜てよ猭ボ絛Τ超跋办じㄧ计ざ﹚瞶
%                                  瓜Τㄢ贺陪ボ家Α'rect'㎝'circ'
% [ZMAX,ZMIN]=MAX_MIN(...)  肚ㄧ计﹚跋办程㎝程
%
% 块旧把计计
%     ---FUN﹚じㄧ计
%     ---XRANGE,YRANGE跑计絛瞅
%     ---TYPE瓜酶篈Τ'rect'㎝'circ'ㄢ
% 块把计
%     ---ZMAX,ZMINㄧ计程㎝程
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