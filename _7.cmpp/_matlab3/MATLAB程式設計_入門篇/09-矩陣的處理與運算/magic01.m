M = magic(5)      
fprintf('�����`�M�G'); sum(M)			% M ���C�@�Ӫ����`�M
fprintf('��C�`�M�G'); sum(M, 2)			% M ���C�@�Ӿ�C�`�M
fprintf('�﨤�u�`�M�G'); sum(diag(M))		% M ���﨤�u�`�M
fprintf('�Ϲ﨤�u�`�M�G'); sum(diag(fliplr(M)))	% M ���Ϲ﨤�u�`�M