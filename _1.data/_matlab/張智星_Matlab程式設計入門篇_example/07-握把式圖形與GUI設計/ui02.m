function ui02(action)
% ui02: Example of UI programming using "switchyard programming"

%	Roger Jang, 20040405

if nargin<1, action='initialize'; end

switch(action)
	case 'initialize'	% �ϧε�����UI����󪺪�l�ơC
		% ���ͷs�ϧε����A�䥪�U�����y�Ь�[30, 30]�A
		% ���׬�300�A���׬�200�]���HPixel�����^
		figH = figure('position', [30 30 300 200]);

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
		h1 = uicontrol('style', 'checkbox', ...
			'tag', 'ui4grid', ...
			'string', 'Grid on', ...
			'position', [10, 10, 60, 20], 'value', 1);

		% �ĤG��UI�����A�ΥH���wX�b��Y�b����l�I�ƥءC
		h2 = uicontrol('style', 'edit', ...
			'tag', 'ui4pointNum', ...
			'string', int2str(pointNum), ...
			'position', [90, 10, 60, 20]);

		% �ĤT��UI�����A�ΥH���w��ܦ����ҥΨ쪺�զ�L�C
		h3 = uicontrol('style', 'popupmenu', ...
			'tag', 'ui4colorMap', ...
			'string', 'hsv|hot|cool', ...
			'position', [170, 10, 60, 20]);

		% �Ĥ@��UI����󪺤������O���ugrid�v�C
		set(h1, 'callback', 'grid');
		% �ĤG��UI����󪺤������O���uui02('setPointNum')�v�C
		set(h2, 'callback', 'ui02(''setPointNum'')');
		% �ĤT��UI����󪺤������O���uui02('setColorMap')�v�C
		set(h3, 'callback', 'ui02(''setColorMap'')');
	case 'setPointNum'	% �ĤG��UI�����callback�C
		% ��X�Ĥ@�βĤG��UI����󪺴���C
		h1 = findobj(0, 'tag', 'ui4grid');
		h2 = findobj(0, 'tag', 'ui4pointNum');

		% ���o�ĤG��UI����󪺼ƭȡC
		pointNum = round(str2num(get(h2, 'string')));

		% �Y�Ʀr�Ӥj�ΤӤp�A�h�]�w��10�C
		if pointNum <= 1 | pointNum > 100,
			pointNum = 10;
			set(h2, 'string', int2str(pointNum));
		end

		% �ھکұo���Ʀr�A���epeaks�����C
		[xx, yy, zz] = peaks(pointNum);
		surf(xx, yy, zz);
		axis tight;

		% �ھڲĤ@��UI�����A�M�w�O�_�n�e��u�C
		if get(h1, 'value')==1,
			grid on;
		else
			grid off;
		end
	case 'setColorMap'	% �ĤT��UI�����callback�C
		% ��X�ĤT��UI����󪺴���C
		h3 = findobj(0, 'tag', 'ui4colorMap');

		% �ھڲĤT��UI�����ӨM�w�ϥΪ���L�x�}�C
		switch get(h3, 'value')
			case 1
				colormap(hsv);
			case 2
				colormap(hot);
			case 3
				colormap(cool);
			otherwise
				disp('Unknown option');
		end
	otherwise
		error('Unknown action string!');
end
