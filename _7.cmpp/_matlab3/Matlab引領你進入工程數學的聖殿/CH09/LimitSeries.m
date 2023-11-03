function [L,type]=LimitSeries(un,p)
%LIMITSERIES   正項級數的極限審斂法
% L=LIMITSERIES(UN)  極限審斂法判斷正項級數UN的斂散性，p-級數中p取1
% L=LIMITSERIES(UN,P)  極限審斂法判斷正項級數UN的斂散性，P>1
% [L,TYPE]=LIMITSERIES(...)  極限審斂法判斷正項級數UN的斂散性，並傳回級數的斂散性字串
%
% 輸導入參數數：
%     ---UN：正項級數
%     ---P：p級數的階次
% 輸出參數：
%     ---L：極限值
%     ---TYPE：表征級數斂散性的字串
%
% See also limit

if nargin==1
    p=1;
end
if p<1
    error('等比級數的冪指數p必須大於等於1.')
end
n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('正項級數一般項的符號變數必須為n.')
end
L=limit(n^p*un,n,inf);
if p==1
    if length(s)==1
        if double(L)>0
            type='發散';
        end
    end
else
    if double(L)>=0
        type='收斂';
    end
end