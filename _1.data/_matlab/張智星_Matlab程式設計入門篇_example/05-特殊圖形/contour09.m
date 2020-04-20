t = linspace(0, 2*pi, 61);		% ���ת���l�I
r = 0:0.05:1;				% ���ת���l�I
[tt, rr] = meshgrid(t, r);		% ���ͤG������l�I
zz=rr.*exp(sqrt(-1)*tt);        % �Ƽƪ��
xx=real(zz);
yy=imag(zz);
ff = abs(zz.^3-1);			% ��������ƭ�
h = polar([0 0], [0 1]);		% ���ͦb���y�ФW���@�����u
delete(h);				% �����W�z�ϧΡA���d�U���y�й϶b
hold on
contour(xx, yy, ff, 20);		% �����u
surf(xx, yy, ff);			% ������
hold off
view(-19, 22);				% �]�w�[������