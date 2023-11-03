function theta=PlaneAngle(PI1,PI2)
%PLANEANGLE   �D�⥭��������
% T=PLANEANGLE(PI1,PI2)  �D����PI1�MPI2������
%
% ��ɤJ�ѼƼơG
%     ---PI1,PI2�G�⥭�����t�ƦV�q
% ��X�ѼơG
%     ---T�G�Ǧ^������������
%
% See also subspace

if isa([PI1;PI2],'sym')
    PI1=[diff(PI1,'x'),diff(PI1,'y'),diff(PI1,'z')];
    PI2=[diff(PI2,'x'),diff(PI2,'y'),diff(PI2,'z')];
end
if isvector(PI1) && isvector(PI2)
    if length(PI1)==3 && length(PI2)==3
        theta=subspace(PI1(:),PI2(:));
    else
        error('��J�V�q������3D�V�q.')
    end
else
    error('Illegal Input arguments.')
end