function [x,U]=Gauss(A,b)
%GAUSS   �������h�k�D�u�ʤ�{���s�ժ���
% X=GAUSS(A,B)  �������h�k�D�u�ʤ�{���s��AX=B����X
% [X,U]=GAUSS(A,B)  �������h�k�D�u�ʤ�{���s��AX=B����X�öǦ^���h�᪺�W�T����{���s�ժ��W�s�x�}
%
% ��ɤJ�ѼƼơG
%     ---A�G�u�ʤ�{���s�ժ��t�Ưx�}
%     ---B�G�u�ʤ�{���s�ժ��k�ݶ�
% ��X�ѼơG
%     ---X�G�u�ʤ�{���s�ժ���
%     ---U�G���h�᪺�W�T����{���s�ժ��W�s�x�}
%
% See also TriuEqu

[m,n]=size(A);
if m~=n || length(b)~=m
    error('�u�ʤ�{���s�ժ��t�Ưx�}�M�`�q�����Ƥ��ŦX.')
end
% ���h�L�{
for k=1:n-1
    m=A(k+1:n,k)/A(k,k);
    A(k+1:n,k+1:n)=A(k+1:n,k+1:n)-m*A(k,k+1:n);
    b(k+1:n)=b(k+1:n)-m*b(k);
    if isa([A,b(:)],'sym')
        A(k+1:n,k)=sym(zeros(n-k,1));
    else
        A(k+1:n,k)=zeros(n-k,1);
    end
end
U=[A,b];
x=TriuEqu(A,b);