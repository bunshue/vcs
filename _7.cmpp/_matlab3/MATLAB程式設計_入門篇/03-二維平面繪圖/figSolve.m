bound=[eps, 0.1];
fplot('sin(1/x)', bound, 1e-4);
hold on
fplot('x', bound);
hold off