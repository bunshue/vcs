function d=poly_str(xd,yd,xi,N)
%POLY_STR   ���ȫ��D�ɺ�k
% D=POLY_STR(XD,YD,XI,N)  �������XD,YD�i��h�������ȨèD��b�IXI�B��N���ɼ�
%
% ��ɤJ�ѼƼơG
%     ---XD,YD�G������
%     ---XI�G�ƭȨD���I
%     ---N�G�D�ɶ���
% ��X�ѼơG
%     ---D�GN���ƭȾɼ�
%
% See also diff, polyfit, polyder, polyval

L=length(xd)-1;
p=polyfit(xd,yd,L);
for k=1:N
    p=polyder(p);
end
d=polyval(p,xi);