function varargout=HomogenDE(fun,coef,t)
%HOMOGENDE   齊次或可化為齊次方程式的求解
% L=HOMOGENDE(FUN,COEF)  求微分方程式dY/dX=FUN((a*x+b*y+c)/(a1*x+b1*y+c1))的通解
% L=HOMOGENDE(FUN,COEF,T)  求可化為齊次方程式的通解，並指定FUN的自變數為T
% [L,S]=L=HOMOGENDE(...)  求可化為齊次方程式的通解並傳回其解的字串形式
%
% 輸導入參數數：
%     ---FUN：關於(a*x+b*y+c)/(a1*x+b1*y+c1)的函數
%     ---COEF：系數矩陣[a,b,c;a1,b1,c1]
%     ---T：函數FUN的自變數
% 輸出參數：
%     ---L：微分方程式的通解
%     ---S：微分方程式解的字串表示
%
% See also SeparableVarsDE

if nargin==2
    t=symvar(fun);
end
if length(t)>1
    error('符號變數個數有誤.')
end
syms x y
D=det(coef(:,1:2));
if D==0
    v=sym('v','real');
    L=coef(2,1)/coef(1,1);
    fun=subs(fun,t,(v+coef(1,3))/(L*v+coef(2,3)));
    I=SeparableVarsDE(sym(coef(1,2)),1/(fun+coef(1,1)/coef(1,2)),x,v);
    yy=subs(I,v,coef(1,1)*x+coef(1,2)*y);
else
    u=sym('u','real');
    X=sym('X','real');
    Y=sym('Y','real');
    x0=-coef(:,1:2)\coef(:,3);
    fun=subs(fun,t,(coef(1,1)+coef(1,2)*u)/(coef(2,1)+coef(2,2)*u));
    I=SeparableVarsDE(1/X,1/(fun-u),X,u);
    I=subs(I,u,Y/X);
    yy=subs(I,{X,Y},{x-x0(1),y-x0(2)});
end
varargout{1}=yy;
if nargout==2
    varargout{2}=['Solution:',char(yy)];
end