function r=CrossPoint(varargin)
%CROSSPOINT   確定圖形所在的水平區間
% R=CROSSPOINT(F1,F2)  傳回曲線F1和F2的交點水平座標，符號自變數為自由自變數
% R=CROSSPOINT(F1,F2,X)  傳回曲線F1和F2的交點水平座標，符號自變數為X
% 
% 輸導入參數數：
%     ---F1,F2：曲線的函數描述
% 輸出參數：
%     ---R：交點水平座標區間
%
% See also solve

[f1,f2]=deal(varargin{1:2});
s=unique([symvar(f1),symvar(f2)]);
if nargin==2 && length(s)==1
    x=s;
else
    x=varargin{3};
end
x0=solve(f1-f2,x);
N=length(x0);
r=zeros(N-1,2);
for k=1:N-1
    r(k,:)=[x0(k),x0(k+1)];
end