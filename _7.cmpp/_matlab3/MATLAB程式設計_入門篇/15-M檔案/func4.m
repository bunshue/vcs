function [ave1, ave2] = func4(vector1, vector2)

if nargin == 1,		% �u���@�ӿ�J�ܼ�
	ave1 = sum(vector1)/length(vector1);
end

if nargout == 2,	% ����ӿ�X�ܼ�
	ave1 = sum(vector1)/length(vector1);
	ave2 = sum(vector2)/length(vector2);
end