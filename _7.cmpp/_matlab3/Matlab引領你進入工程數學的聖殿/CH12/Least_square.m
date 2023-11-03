function [p,A,b,FitFun]=Least_square(x,y,phifun,wfun)
%LEAST_SQUARE   最小二乘法
% P=LEAST_SQUARE(X,Y,PHIFUN)  利用基函數PHIFUN來擬合資料X和Y
% P=LEAST_SQUARE(X,Y,PHIFUN,WFUN)  利用基函數PHIFUN和權函數WFUN擬合資料X和Y
% [P,A,B]=LEAST_SQUARE(...)  最小二乘法擬合資料並傳回法方程式群組的系數矩陣和右端向量
% [P,A,B,FITFUN]=LEAST_SQUARE(...)  最小二乘法擬合資料並傳回擬合函數表達式
%
% 輸導入參數數：
%     ---X,Y：實驗資料
%     ---PHIFUN：擬合基函數，可以是匿名函數或內聯函數
%     ---WFUN：權函數
% 輸出參數：
%     ---P：最小二乘擬合系數
%     ---A：法方程式群組的系數矩陣
%     ---B：法方程式群組的右端向量
%     ---FITFUN：擬合函數表達式
%
% See also polyfit, lsqcurvefit

x=x(:); y=y(:);
if length(x)~=length(y)
    error('實驗資料長度不一致.')
end
if nargin<4
    wfun=ones(size(x));
end
func=char(phifun);
func=strrep(func,'ones(size(x))','1');
func=strrep(func,'.*','*');
func=strrep(func,'./','/');
func=strrep(func,'.^','^');
k=strfind(func,'[');
func=sym(func(k(1):end));
phifun=phifun(x);
n=size(phifun,2);
A=zeros(n);b=zeros(n,1);
for k=1:n
    for j=1:n
        A(k,j)=0;
        for i=1:length(x)
            A(k,j)=A(k,j)+wfun(i)*phifun(i,j)*phifun(i,k);
        end
    end
    for i=1:length(x)
        b(k)=b(k)+wfun(i)*y(i)*phifun(i,k);
    end
end
p=A\b;
FitFun=vpa(dot(p,func),4);