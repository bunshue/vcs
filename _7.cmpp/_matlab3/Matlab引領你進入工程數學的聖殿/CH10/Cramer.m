function x=Cramer(A,b)
%CRAMER   �J�ܩi�k�h�D��w�u�ʤ�{���s�ժ���
% X=CRAMER(A,B)  �J�ܩi�k�h�D�u�ʤ�{���s��AX=B����X
%
% ��ɤJ�ѼƼơG
%     ---A�G�u�ʤ�{���s�ժ��t�Ưx�}
%     ---B�G�u�ʤ�{���s�ժ��k�ݦV�q
% ��X�ѼơG
%     ---X�G�u�ʤ�{���s�ժ���
%
% See also det

[m,n]=size(A);
if m~=n || length(b)~=m
    error('�u�ʤ�{���s�ժ��t�Ưx�}�M�`�q�����Ƥ��ŦX.')
end
if isa([A,b(:)],'sym')
    x=sym(zeros(n,1));
else
    x=zeros(n,1);
end
D=det(A);
for k=1:n
    Dk=A;
    Dk(:,k)=b(:);
    Dk=det(Dk);
    x(k)=Dk/D;
end