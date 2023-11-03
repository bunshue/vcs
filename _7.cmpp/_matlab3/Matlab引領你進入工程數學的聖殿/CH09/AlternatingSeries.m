function type=AlternatingSeries(un)
%ALTERNATINGSERIES   交錯級數審斂法
% TYPE=ALTERNATINGSERIES(UN)  利用萊布尼茨定理判斷交錯級數(-1)^(N-1)*UN的斂散性
%
% 輸導入參數數：
%     ---UN：正項級數
% 輸出參數：
%     ---TYPE：表征級數斂散性的字串
%
% See also limit

n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('正項級數一般項的符號變數必須為n.')
end
uN=subs(un,n,n+1);
x=subs(un-uN,n,1:1e6);
L=limit(un,n,inf);
if L==0 && all(x>=0)
    type='收斂';
elseif L~=0
    type='發散';
else
    type='不確定';
end