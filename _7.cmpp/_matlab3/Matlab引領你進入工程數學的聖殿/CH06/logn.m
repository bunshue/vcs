function y=logn(x,a)
%LOGN   ―ヴ種┏癸计
% Y=LOGN(X,A)  ―┏计A痷计X癸计盢挡狦肚Yい
%
% 块旧把计计
%     ---X癸计痷计
%     ---A癸计┏计
% 块把计
%     ---Y肚癸计
%
% See also log, log2, log10

if ~isequal(class(x),class(a))
    error('LOGN requires input arguments be the same class.');
end
if ~(isa([x,a],'double')||isa([x,a],'single'))
    error('LOGN requires input arguments of double or single class.');
end
switch a
    case exp(1)
        y=log(x);  % 礛癸计
    case 2
        y=log2(x);  % 2┏癸计
    case 10
        y=log10(x);  % 盽ノ癸计
    otherwise
        y=log(x)/log(a);  % 传┏そΑ硂柑传┏そΑいbe
end
