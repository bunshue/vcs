Z = peaks(50);
C(:, :, 1) = rand(50);	% C(:,:,1) �N�� R�]Red�A����^�����q
C(:, :, 2) = rand(50);	% C(:,:,2) �N�� G�]Green�A���^�����q
C(:, :, 3) = rand(50);	% C(:,:,3) �N�� B�]Blue�A�Ŧ�^�����q
surf(Z, C);
axis tight