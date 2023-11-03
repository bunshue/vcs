function x=TriuEqu(U,b)
%TRIUEQU   ���h�k�D�W�T����{���s�ժ���
% X=TRIUEQU(U,B)  ���h�k�D��{���s��UX=B���ѡA�䤤U�O�W�T���}
%
% ��ɤJ�ѼƼơG
%     ---U�G�u�ʤ�{���s�ժ��t�Ưx�}�A�O�@�ӤW�T���x�}
%     ---B�G�u�ʤ�{���s�ժ��k�ݦV�q
% ��X�ѼơG
%     ---X�G�u�ʤ�{���s�ժ���
%
% See also Cramer

[m,n]=size(U);
if m~=n || length(b)~=m
    error('�u�ʤ�{���s�ժ��t�Ưx�}�M�`�q�����Ƥ��ŦX.')
end
if isa([U,b(:)],'sym')
    x=sym(zeros(n,1));
else
    x=zeros(n,1);
end
x(n)=b(n)/U(n,n);  % �Dx_n
for k=n-1:-1:1
    x(k)=(b(k)-U(k,k+1:n)*x(k+1:n))/U(k,k);  % �Dx_k�Ak=n-1,n-2,�K,1
end