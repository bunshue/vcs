theta = linspace(0, 2*pi, 50);
rho = sin(0.5*theta);
[x, y] = pol2cart(theta, rho);	% �ѷ��y���ഫ�ܪ����y��
compass(x, y);			% �e�X�H���I���V�q�_�l�I��ù�L��
