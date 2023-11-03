function H=FrequencyTable(X)
%FREQUENCYTABLE   参璸皚じ瞷繵计
% H=FREQUENCYTABLE(X)  参璸痻皚Xいじ瞷繵计
%
% 块旧把计计
%     ---X﹚皚┪痻皚
% 块把计
%     ---H肚参璸挡狦
%
% See also tabulate

if ~isa(X,'sym')
    H=tabulate(X);
    H=H(:,1:2);
else
    sortX=sort(X(:));
    D=[simple(sortX(2:end)-sortX(1:end-1));sym(1)];
    uniqueX=(D~=0);
    k=find([1;uniqueX]);
    H=[sortX(uniqueX) diff(k)];
end