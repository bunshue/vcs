function [L,type]=PositiveIermSeries(un,mode)
%POSITIVEIERMSERIES   正項級數的比值審斂法和根值審斂法
% L=POSITIVEIERMSERIES(UN)  比值審斂法判斷正項級數的斂散性
% L=POSITIVEIERMSERIES(UN,MODE)  選用特殊的審斂法判斷正項級數的斂散性
% [L,TYPE]=POSITIVEIERMSERIES(...)  選用特殊的審斂法判斷正項級數的斂散性
%                                   並傳回所使用的審斂法
%
% 輸導入參數數：
%     ---UN：正項級數通項
%     ---MODE：特殊的審斂法，MODE有以下兩個取值：
%              1.'d'或'比值'或1：比值審斂法
%              2.'k'或'根值'或2：根值審斂法
% 輸出參數：
%     ---L：傳回的通項的某種型態的極限值
%     ---TYPE：所使用的審斂法
%
% See also limit

if nargin==1
    mode=1;
end
n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('正項級數一般項的符號變數必須為n.')
end
switch lower(mode)
    case {1,'d','比值'}
        type='比值審斂法';
        uN=subs(un,'n',n+1);
        L=limit(simple(uN/un),'n',inf);
    case {2,'k','根值'}
        type='根值審斂法';
        L=limit(simple(un^(1/n)),'n',inf);
    otherwise
        error('Illegal options.')
end
if length(s)==1
    if double(L)<1
        type=[type,'：收斂'];
    elseif double(L)>1
        type=[type,'：發散'];
    else
        error('目前所選取的審斂法失效.')
    end
end