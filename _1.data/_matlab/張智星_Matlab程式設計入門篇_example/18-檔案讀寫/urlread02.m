tempFile = [tempname, '.html'];				% ���w�Ȧs�ɮ�
urlwrite('http://www.google.com.tw', tempFile);		% �N�������e�g���ɮ�
dos(['start ', tempFile]);				% �}�Ҧ��ɮ�