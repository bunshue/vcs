x = 3:6;
y = 5:9;
[xx, yy] = meshgrid(x, y);		% xx �M yy ���O�x�}  
zz = xx.*yy;				% �p���ƭ� zz�A�]�O�x�}
subplot(2,2,1); mesh(xx);
title('xx'); axis tight
subplot(2,2,2); mesh(yy);
title('yy'); axis tight
subplot(2,2,3); mesh(xx, yy, zz);
title('zz �� xx �� yy �@��'); axis tight