function D=Distance(A,B)
%DISTANCE   計算兩點之間的距離
% DISTANCE(A)  繪制原點到點A的向量，圖題標注為原點到A的距離
% DISTANCE(A,B)   繪制點B到點A的向量，圖題標注為A，B間的距離
% D=DISTANCE(...)  計算原點到A或A、B之間的距離
%
% 輸導入參數數：
%     ---A：終點
%     ---B：起點
% 輸出參數：
%     ---D：A、B間的距離
%
% See also norm, sqrt

if nargin==1
    B=zeros(size(A));
end
[m,n]=size(A);
if ~isequal([m,n],size(B)) || m~=1
    error('點的座標表示形式有誤.')
end
C=A-B;
L=0;
for k=1:n
    L=L+C(k)^2;
end
L=sqrt(L);
if isnumeric([A,B]) && (n==2 || n==3) && nargout==0
    drawvec(C,B)
    title(['|AB|=',num2str(L)])
elseif nargout==1
    D=L;
end