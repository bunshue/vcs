n=100000;
subplot(231); x=rand(n, 1); hist(x, 100);
subplot(232); x=rand(n, 1); hist(x.^3, 100);
subplot(233); x=rand(n, 1); hist(nthroot(x, 3), 100);
subplot(234); x=randn(n, 1); hist(x, 100);
subplot(235); x=randn(n, 1); hist(x.^3, 100);
subplot(236); x=randn(n, 1); hist(nthroot(x, 3), 100);