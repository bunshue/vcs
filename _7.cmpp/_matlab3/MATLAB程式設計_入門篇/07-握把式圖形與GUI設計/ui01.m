% ���ͷs�ϧε����A�䥪�U�����y�Ь�[30, 30]�A
% ���׬�300�A���׬�200�]���HPixel�����^
figure('position', [30 30 300 200]);

% �b�ϧε��������ͤ@�ӹ϶b�A�䥪�U�����y�Ь�[0.1, 0.2],
% ���׬�0.8�A���׬�0.8�]�ϥμзǤƪ����A�Y�ϧΪ����U����[0, 0]�A
% ���פΰ��׳��O1�C�^
axes('position', [0.1 0.2 0.8 0.8]);

% �����W���Ĥ@�ӹϧΡA���T�תŶ���peaks��ơC
pointNum = 20;
[xx, yy, zz] = peaks(pointNum);
surf(xx, yy, zz);
colormap hsv
axis tight

% �Ĥ@��UI�����A�ΥH����I����u����ܡC
h1 = uicontrol('style', 'checkbox', 'string', 'Grid on', ...
	'position', [10, 10, 60, 20], 'value', 1);

% �ĤG��UI�����A�ΥH���wX�b��Y�b����l�I�ƥءC
h2 = uicontrol('style', 'edit', 'string', int2str(pointNum), ...
	'position', [90, 10, 60, 20]);

% �ĤT��UI�����A�ΥH���w��ܦ����ҥΨ쪺��L�x�}�C
h3 = uicontrol('style', 'popupmenu', ...
	'string', 'hsv|hot|cool', ...
	'position', [170, 10, 60, 20]);

% �Ĥ@��UI����󪺤������O���ugrid�v�C
set(h1, 'callback', 'grid');
% �ĤG��UI����󪺤������O���ucb2�v�C
set(h2, 'callback', 'cb2');
% �ĤT��UI����󪺤������O���ucb3�v�C
set(h3, 'callback', 'cb3');
