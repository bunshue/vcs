function varargout=PlaneEquation(varargin)
%PLANEEQUATION   ―キよ祘Α
% L=PLANEEQUATION(N,M0)  キ翴猭Αよ祘Α
% L=PLANEEQUATION(A,B,C,D)  キよ祘Α
% [L,TYPE]=PLANEEQUATION(...)  ―キよ祘Α肚よ祘Α篈
%
% 块旧把计计
%     ---Nキ翴M0矪猭秖
%     ---M0キ翴
%     ---A,B,C,Dキよ祘Α╰计
% 块把计
%     ---Lキよ祘Α
%     ---TYPEキよ祘Α篈﹃
%
% See also dot

syms x y z
if nargin==2
    [n,M0]=deal(varargin{:});
    M=[x,y,z];
    M0M=M-M0;
    L=dot(n,M0M);
    type='キ翴猭Αよ祘Α';
elseif nargin==4
    [A,B,C,D]=deal(varargin{:});
    L=A*x+B*y+C*z+D;
    type='キΑよ祘Α';
else
    error('Illegal Input arguments.')
end
L=[char(L),'=0'];
if nargout==1
    varargout{1}=L;
elseif nargout==2
    varargout{1}=L;varargout{2}=type;
else
    error('Illegal output arguments.')
end