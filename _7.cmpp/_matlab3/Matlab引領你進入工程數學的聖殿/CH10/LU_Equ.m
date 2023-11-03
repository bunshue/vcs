function [x,L,U]=LU_Equ(A,b)
%LU_EQU   LU���Ѫk�D�u�ʤ�{���s�ժ���
% X=LU_EQU(A,B)  LU���Ѫk�D�u�ʤ�{���s��AX=B����X
% [X,L,U]=LU_EQU(A,B)  LU���Ѫk�D�u�ʤ�{���s��AX=B����X�A�öǦ^���ѫ᪺�W(�U)�T���x�}
%
% ��ɤJ�ѼƼơG
%     ---A�G�u�ʤ�{���s�ժ��t�Ưx�}
%     ---B�G�u�ʤ�{���s�ժ��k�ݶ�
% ��X�ѼơG
%     ---X�G�u�ʤ�{���s�ժ���
%     ---L�G���ѫ᪺�U�T���x�}
%     ---U�G���ѫ᪺�W�T���x�}
%
% See also TriuEqu

[m,n]=size(A);
if m~=n || length(b)~=m
    error('�u�ʤ�{���s�ժ��t�Ưx�}�M�`�q�����Ƥ��ŦX.')
end
if isa([A,b(:)],'sym')
    U=sym(zeros(n));
    L=sym(eye(n));
else
    U=zeros(n);
    L=eye(n);
end
U(1,:)=A(1,:);
L(2:n,1)=A(2:n,1)/U(1,1);
for k=2:n
    U(k,k:n)=A(k,k:n)-L(k,1:k-1)*U(1:k-1,k:n);
    L(k+1:n,k)=A(k+1:n,k)-L(k+1:n,1:k-1)*U(1:k-1,k);
    L(k+1:n,k)=L(k+1:n,k)/U(k,k);
end
y=flipud(TriuEqu(rot90(L,2),flipud(b(:))));
x=TriuEqu(U,y);