load clown.mat		% ���J�p���v����ơA�t�ܼ� X �M map
subplot(2,2,1); image(X); axis image
subplot(2,2,2); image(X(1:100, 1:100)); axis image
subplot(2,2,3); image(X(1:3, 1:3)); axis image
X(1:3, 1:3)
subplot(2,2,4); image(69); axis image
colorbar
colormap(map);
