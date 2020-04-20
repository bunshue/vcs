function out=myFibo(n)

if n==0 | n==1, out=1; return; end
out=myFibo(n-1)+myFibo(n-2);