dept1 = char('ee', 'cs', 'econ');	% dept1 �O�@�Ӧr���}�C
cellData = cellstr(dept1);		% �N dept1 �ন�@�Ӳ��Ȱ}�C cellData
dept2 = char(cellData);			% �N cellData �ഫ���r���}�C dept2
isequal(dept1, dept2)			% ���� dept1 �M dept2 �O�_�۵�