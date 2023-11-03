function out = fibo(n)
% fibo: Fibonacci number using an analytic expression

%	Roger Jang, 20030726

r1=(1+sqrt(5))/2;
r2=(1-sqrt(5))/2;
out=(r1^(n-1)-r2^(n-1))/sqrt(5);