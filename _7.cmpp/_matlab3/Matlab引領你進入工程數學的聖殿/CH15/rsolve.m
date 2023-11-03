function x=rsolve(F,G,u,x0)
%RSOLVE   z�ܴ��D�������u�ʩw�`�t��
% X=RSOLVE(F,G,U,X0)  �D�u�ʩw�`�t��X(k+1)=F*X(k)+G*U(k)����
%
% ��ɤJ�ѼƼơG
%     ---F,G�G�t�Ϊ��t�Ưx�}
%     ---U�G�t�ο�J
%     ---X0�G�t�Ϊ����
% ��X�ѼơG
%     ---X�G�t�Ϊ���
%
% See also ztrans, iztrans

[m,n]=size(F);
[q,p]=size(G);
r=length(u);
if m~=n || n~=q
    error('�t�Ưx�}���Ƥ��ŦX.')
end
if isvector(u)
    if r~=p
        error('��J�V�q�P����x�}���Ƥ��ŦX.')
    end
end
I=sym(eye(size(F)));
syms z k
U=ztrans(sym(u));
x=simple(iztrans((z*I-sym(F))\(z*sym(x0)+sym(G)*U),z,k));