function PI=CalculatePI(n)
%CALCULATEPI   蛾㏄瞯PI计衡猭
% PI=CALCULATEPI(N)  ノ经计璸衡蛾㏄瞯
%
% 块旧把计计
%     ---N计┮兜计
% 块把计
%     ---PI蛾㏄瞯
%
% See also pi

if nargin==0
    n=1000;
end
PI=0;
for k=1:n
    a=(-1)^(k-1)/(2*k-1);
    PI=PI+a;
end
PI=4*PI;