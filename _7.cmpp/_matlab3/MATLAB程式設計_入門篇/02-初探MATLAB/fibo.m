function out = fibo(n)
% fibo: Fibonacci number

%	Roger Jang, 20030726

if n==1
	out=0;
	return;
elseif n==2
	out=1;
	return;
else
	out=fibo(n-1)+fibo(n-2);
end