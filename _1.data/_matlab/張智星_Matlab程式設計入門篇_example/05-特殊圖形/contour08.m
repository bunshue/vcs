t = linspace(0, 2*pi, 61);	% ���ת���l�I
r = 0:0.05:1;			% ���ת���l�I
[tt, rr] = meshgrid(t, r);	% ���ͤG������l�I
[xx, yy] = pol2cart(tt, rr);	% �N���y���ഫ�ܪ����y��
zz = xx + sqrt(-1)*yy;		% �Ƽƪ�ܡA��i�g�� zz=rr.*exp(sqrt(-1)*tt);
ff = abs(zz.^3-1);		% ���������
h = polar([0 0], [0 1]);	% ���ͦb���y�ФW���@�����u
delete(h);			% �����W�z�ϧΡA���d�U���y�й϶b
hold on
contour(xx, yy, ff, 50);	% �e�X�����u
hold off