function I=CoordinateCurveInt(fun,vars,fun_para,t,alpha,beta)
%COORDINATECURVEINT   計算第二類別曲線積分
% I=COORDINATECURVEINT(FUN,VARS,FUN_PARA,T,ALPHA,BETA)  計算函數FUN的第二類別曲線積分
%
% 輸導入參數數：
%     ---FUN：被積函數向量
%     ---VARS：符號變數
%     ---FUN_PARA：積分曲線的參數方程式的符號表達式
%     ---T：參數方程式的符號自變數
%     ---ALPHA,BETA：積分區間
% 輸出參數：
%     ---I：第二類別曲線積分值
%
% See also diff, int

N=length(fun);
S=0;
for k=1:N
    df=diff(fun_para(k),t);
    S=S+subs(fun(k),vars,num2cell(fun_para))*df;
end
I=int(S,t);
I=subs(I,t,sym(beta))-subs(I,t,sym(alpha));