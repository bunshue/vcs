function varargout=PlaneEquation(varargin)
%PLANEEQUATION   �D��������{��
% L=PLANEEQUATION(N,M0)  �������I�k����{��
% L=PLANEEQUATION(A,B,C,D)  �������@���{��
% [L,TYPE]=PLANEEQUATION(...)  �D��������{���öǦ^��{�����A
%
% ��ɤJ�ѼƼơG
%     ---N�G�����W�IM0�B���k�V�q
%     ---M0�G�����W���@�I
%     ---A,B,C,D�G������{�����t��
% ��X�ѼơG
%     ---L�G������{��
%     ---TYPE�G������{�����A�r��
%
% See also dot

syms x y z
if nargin==2
    [n,M0]=deal(varargin{:});
    M=[x,y,z];
    M0M=M-M0;
    L=dot(n,M0M);
    type='�������I�k����{��';
elseif nargin==4
    [A,B,C,D]=deal(varargin{:});
    L=A*x+B*y+C*z+D;
    type='�������@�릡��{��';
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