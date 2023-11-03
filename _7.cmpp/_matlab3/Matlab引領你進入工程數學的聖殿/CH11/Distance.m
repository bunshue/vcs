function D=Distance(A,B)
%DISTANCE   �p����I�������Z��
% DISTANCE(A)  ø����I���IA���V�q�A���D�Ъ`�����I��A���Z��
% DISTANCE(A,B)   ø���IB���IA���V�q�A���D�Ъ`��A�AB�����Z��
% D=DISTANCE(...)  �p����I��A��A�BB�������Z��
%
% ��ɤJ�ѼƼơG
%     ---A�G���I
%     ---B�G�_�I
% ��X�ѼơG
%     ---D�GA�BB�����Z��
%
% See also norm, sqrt

if nargin==1
    B=zeros(size(A));
end
[m,n]=size(A);
if ~isequal([m,n],size(B)) || m~=1
    error('�I���y�Ъ�ܧΦ����~.')
end
C=A-B;
L=0;
for k=1:n
    L=L+C(k)^2;
end
L=sqrt(L);
if isnumeric([A,B]) && (n==2 || n==3) && nargout==0
    drawvec(C,B)
    title(['|AB|=',num2str(L)])
elseif nargout==1
    D=L;
end