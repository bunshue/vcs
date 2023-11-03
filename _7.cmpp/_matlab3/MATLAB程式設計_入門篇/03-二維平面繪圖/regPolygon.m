function regPolygon(n)
% regPolygon: �e���h�䫬�Ψ�~����

if nargin<1, n=8; end

% ====== �e���h�䫬
vertices=exp((0:n)*j*2*pi/n);
plot(vertices, '-o');
% ====== �e�~����
hold on
theta=linspace(0, 2*pi);
plot(exp(j*theta), '-r');
hold off
axis image