function [dy,dx]=diff_ctr(y,dt,n)
%DIFF_CTR   �ƭȷL���D��
% [DY,DX]=DIFF_CTR(Y,DT,N)  �Q�Τ��߮t����k�D���������Y��N�ѼƭȾɼ�
%
% ��ɤJ�ѼƼơG
%     ---Y�G���w�������Z��������
%     ---DT�G���ܼƪ����Z
%     ---N�G�ƭȨD�ɶ���
% ��X�ѼơG
%     ---DY,DX�G�D�o���ɼƦV�q�P���������ܼƦV�q
%
% See also diff

yx1=[y 0 0 0 0 0];yx2=[0 y 0 0 0 0];yx3=[0 0 y 0 0 0];
yx4=[0 0 0 y 0 0];yx5=[0 0 0 0 y 0];yx6=[0 0 0 0 0 y];
switch n
    case 1
        dy=(-diff(yx1)+7*diff(yx2)+7*diff(yx3)-diff(yx4))/(12*dt);
        L0=3;
    case 2
        dy=(-diff(yx1)+15*diff(yx2)-15*diff(yx3)+diff(yx4))/(12*dt^2);
        L0=3;
    case 3
        dy=(-diff(yx1)+7*diff(yx2)-6*diff(yx3)-6*diff(yx4)+...
            7*diff(yx5)-diff(yx6))/(8*dt^3);L0=5;
    case 4
        dy=(-diff(yx1)+11*diff(yx2)-28*diff(yx3)+28*diff(yx4)-...
            11*diff(yx5)+diff(yx6))/(6*dt^4);L0=5;
end
dy=dy(L0+1:end-L0);
dx=((1:length(dy))+L0-2-(n>2))*dt;