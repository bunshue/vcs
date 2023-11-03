function I=InterpolatoryQuad(varargin)
%INTERPOLATORYQUAD   插值型方法求解定積分
% I=INTERPOLATORYQUAD(X,Y)  計算離散資料積分
% I=INTERPOLATORYQUAD(FUN,A,B,N)  計算函數FUN在積分限[A,B]上的積分，並指定區間等分數為N
%
% 輸導入參數數：
%     ---X,Y：觀測資料，等長的向量
%     ---FUN：被積函數
%     ---A,B：積分下限和上限
%     ---N：區間等分數
% 輸出參數：
%     ---I：插值型求積結果
%
% See also polyfit, polyint, polyval

args=varargin;
if isnumeric(args{1})
    x=args{1};
    y=args{2};
    N=length(x)-1;
else
    [fun,a,b,N]=deal(args{:});
    h=(b-a)/N;
    x=a+h*(0:N);
    y=feval(fun,x);
end
p=polyfit(x,y,N);
P=polyint(p);
I=polyval(P,x(end))-polyval(P,x(1));