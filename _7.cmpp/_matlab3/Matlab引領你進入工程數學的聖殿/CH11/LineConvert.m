function S=LineConvert(PI1,PI2)
%LINECONVERT   �N���u���@���{����Ƭ��ѼƤ�{��
% S=LINECONVERT(PI1,PI2)  �D����PI1�MPI2����u���ѼƤ�{��
%
% ��ɤJ�ѼƼơG
%     ---PI1,PI2�G�������t�ƦV�q
% ��X�ѼơG
%     ---S�G�ѼƤ�{����F��
%
% See also \, cross

if ~isvector(PI1) && ~isvector(PI2)
    error('PI1 and PI2 must be vectors.')
end
if length(PI1)==4 && length(PI2)==4
    A=[PI1(1:3);PI2(1:3)];
    b=-[PI1(4);PI2(4)];
    x0=A\b;
    s=cross(A(1,:),A(2,:));
    syms t
    S=x0(:)+s(:)*t;
else
    error('��J�V�q������4���V�q.')
end