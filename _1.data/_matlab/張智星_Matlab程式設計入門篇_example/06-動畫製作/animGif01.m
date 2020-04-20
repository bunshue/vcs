close all; clear all;
filename='gifTest.gif';
z=peaks;
for i=0:0.05:5
	surf(z*(i-2.5)); colormap('jet');
	axis([-inf inf -inf inf -10 10]);
	drawnow
	im=frame2im(getframe);
	[imind, cm]=rgb2ind(im,256);
	if i==1
		imwrite(imind, cm, filename, 'gif', 'Loopcount', inf);
	else
		imwrite(imind, cm, filename, 'gif', 'WriteMode', 'append');
	end
end
dos(['start ', filename]);