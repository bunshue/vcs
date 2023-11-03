function output=zzz(a)
sum1=sum(diag(a));
b=fliplr(a);
sum2=sum(diag(b));
output=sum1+sum2;
