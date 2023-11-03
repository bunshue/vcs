function I=quad_inf(fun,a,b,tol,eps)
%QUAD_INF   無窮限反常積分的無窮區間逼近法
% I=QUAD_INF(FUN,A,B)  求函數FUN在區間[A,B]上的數值積分，A或B可以為無窮，下同
% I=QUAD_INF(FUN,A,B,TOL)  求函數FUN在區間[A,B]上的數值積分，容差為TOL
% I=QUAD_INF(FUN,A,B,TOL,EPS)  求無窮限反常積分，精度為EPS
%
% 輸導入參數數：
%     ---FUN：被積函數
%     ---A,B：積分區間的端點，要求A<B
%     ---TOL：容差，預設值為1e-6
%     ---EPS：精度要求，迭代終止准則，預設值為1e-5
% 輸出參數：
%     ---I：求得的積分值
%
% See also quadgk, quadl

if nargin<5 || isempty(eps)
    eps=1e-5;
end;
if nargin<4 || isempty(tol)
    tol=1e-6;
end;
N=2;I=0;T=1;
if isinf(a) && isinf(b)
    I=quad_inf(fun,-inf,0)+quad_inf(fun,0,inf);  % 遞歸呼叫
elseif isinf(b)
    while T>eps
        b=a+N;
        T=quadl(fun,a,b,tol);
        I=I+T;
        a=b; N=2*N;
    end
elseif isinf(a)
    while T>eps
        a=b-N;
        T=quadl(fun,a,b,tol);
        I=I+T;
        b=a; N=2*N;
    end
else
    I=quadl(fun,a,b,tol);
end