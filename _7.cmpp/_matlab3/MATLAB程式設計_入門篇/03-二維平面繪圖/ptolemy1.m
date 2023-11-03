r=1;
theta=linspace(0, 2*pi);
plot(r*sin(theta), r*cos(theta));
axis image
axis([-1.2, 1.2, -1.2, 1.2]);

A=exp(j*pi/3);
B=exp(j*pi);
C=exp(j*3.3*pi/2);
D=exp(-j*pi/6);
line(real([A B]), imag([A B]), 'color', 'r');
line(real([A C]), imag([A C]), 'color', 'r');
line(real([A D]), imag([A D]), 'color', 'r');
line(real([B C]), imag([B C]), 'color', 'r');
line(real([B D]), imag([B D]), 'color', 'r');
line(real([C D]), imag([C D]), 'color', 'r');

text(real(A), imag(A), 'A');
text(real(B), imag(B), 'B');
text(real(C), imag(C), 'C');
text(real(D), imag(D), 'D');