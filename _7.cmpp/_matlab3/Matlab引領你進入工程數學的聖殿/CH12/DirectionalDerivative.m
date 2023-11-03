function dfdl=DirectionalDerivative(fun,vars,direction,M)
%DIRECTIONALDERIVATIVE   璸衡よ弘艶计
% DFDL=DIRECTIONALDERIVATIVE(FUN,VARS,DIRECTION,M)  璸衡ㄧ计翴Mよ弘艶计
%
% 块旧把计计
%     ---FUNじㄧ计才腹笷Α
%     ---VARS才腹跑计
%     ---DIRECTIONよ秖
%     ---M﹚翴畒夹
% 块把计
%     ---DFDL肚よ弘艶计
%
% See also Distance, dot

if ~isa(fun,'sym')
    error('FUN must be a Symbolic function.')
end
N=length(vars);
df=sym(zeros(1,N));
for k=1:N
    df(k)=subs(diff(fun,vars{k}),vars,num2cell(M));
end
C=Direction_Cosine(direction);
dfdl=dot(df,C);