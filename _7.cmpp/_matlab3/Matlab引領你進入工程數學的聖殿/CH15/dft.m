function X=dft(x,dim)
%DFT   離散傅裡葉變換
% Y=DFT(X)  求資料矩陣X的離散傅裡葉變換
% Y=DFT(X,DIM)  對矩陣X的行維或列維求傅裡葉變換
%
% 輸導入參數數：
%     ---X：資料矩陣
%     ---DIM：指定維的方向
% 輸出參數：
%     ---Y：離散傅裡葉變換結果
%
% See also fourier

if isvector(x)
    x=x(:).';
end
if nargin<2 || isvector(x)
    dim=1;
end
N=size(x,setdiff([1,2],dim));
n=0:N-1;
k=0:N-1;
WN=exp(-1j*2*pi/N);
nk=n'*k;
W=WN.^nk;
if dim==1
    X=x*W;
else
    X=(x.'*W).';
end