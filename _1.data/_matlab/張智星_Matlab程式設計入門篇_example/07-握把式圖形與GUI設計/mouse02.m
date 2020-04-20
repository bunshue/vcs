function mouse02(action)
% mouse02: ���Үi�ܦp��H�ӳ]�w�ƹ��ƥ󪺤������O

%	Roger Jang, 20040406

if nargin == 0, action = 'start'; end

switch(action)	% �}�ҹϧε���
	case 'start'
		axis([0 1 0 1]);	% �]�w�϶b�d��
		box on;			% �N�϶b�[�W�Ϯ�
		title('Click and drag your mouse in this window!');
		% �]�w�ƹ����s�Q���U�ɪ��������O
		set(gcf, 'WindowButtonDownFcn', sprintf('%s %s', mfilename, 'down'));
	case 'down'	% �ƹ����s�Q���U�ɪ��������O
		% �]�w�ƹ����ʮɪ��������O
		set(gcf, 'WindowButtonMotionFcn', sprintf('%s %s', mfilename, 'move'));
		% �]�w�ƹ����s�Q����ɪ��������O��
		set(gcf, 'WindowButtonUpFcn', sprintf('%s %s', mfilename, 'up'));
		% �C�L�uMouse down!�v�T��
		fprintf('Mouse down!\n');
	case 'move'	% �ƹ����ʮɪ��������O
		fprintf('Mouse is moving! ');
		feval(mfilename, 'print');
		% �C�L�uMouse is moving!�v�T���ηƹ��{�b��m
	case 'up'	% �ƹ����s�Q����ɪ��������O
		feval(mfilename, 'print');
		% �M���ƹ����ʮɪ��������O
		set(gcf, 'WindowButtonMotionFcn', '');
		% �M���ƹ����s�Q����ɪ��������O
		set(gcf, 'WindowButtonUpFcn', '');
		% �C�L�uMouse up!�v�T��
		fprintf('Mouse up!\n');
	case 'print'
		currPt = get(gca, 'CurrentPoint');
		x = currPt(1,1); y = currPt(1,2);
		line(x, y, 'marker', '.', 'EraseMode', 'xor');
		fprintf('Current location = (%g, %g)\n', currPt(1,1), currPt(1,2));
end