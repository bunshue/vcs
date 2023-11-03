function r=RootInterval(fun,a,b,h)
%ROOTINTERVAL   �v�B���y�k�D��{�����j�ڰ϶�
% R=ROOTINTERVAL(FUN,A,B)
% R=ROOTINTERVAL(FUN,A,B,H)
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��{����MATLAB�y�z�A�i�H���ΦW��ƩΤ��p���
%     ---A,B�G�϶����I
%     ---H�G�B��
% ��X�ѼơG
%     ---R�G�Ǧ^���j�ڰ϶��A�O�@�ӦC�Ƭ�2���x�}

if nargin==3
    h=(b-a)/100;
end
a1=a;b1=a1+h;
r=[];
while b1<b
    if fun(a1)*fun(b1)<0
        r=[r;[a1,b1]];
        a1=b1;b1=a1+h;
    else
        a1=b1;b1=a1+h;
        continue
    end
end