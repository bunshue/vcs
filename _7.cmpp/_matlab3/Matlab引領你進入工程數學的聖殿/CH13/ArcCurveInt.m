function I=ArcCurveInt(fun,vars,varargin)
%ARCCURVEINT   璸衡材摸Ρ絬縩だ
% I=ARCCURVEINT(FUN,{'X','Y'},FUNX,FUNY,T,ALPHA,BETA)  璸衡じㄧ计材摸Ρ絬縩だ
% I=ARCCURVEINT(FUN,{'X','Y','Z'},FUNX,FUNY,FUNZ,T,ALPHA,BETA)  璸衡じㄧ计
%                                                               材摸Ρ絬縩だ
% I=ARCCURVEINT(FUN,{'X','Y','Z',...},FUNX,FUNY,FUNZ,...,T,ALPHA,BETA)
%                                                璸衡じㄧ计材摸Ρ絬縩だ
%
% 块旧把计计
%     ---FUN砆縩ㄧ计
%     ---VARS砆縩ㄧ计才腹跑计
%     ---FUNX,FUNY,...縩だΡ絬把计よ祘Α
%     ---T把计よ祘Α才腹跑计
%     ---ALPHA,BETA縩だ絛瞅
% 块把计
%     ---IΡ絬縩だ
%
% See also diff, int

args=varargin;
[t,alpha,beta]=deal(args{end-2:end});
S=0;
for k=1:nargin-5
    fun=subs(fun,vars{k},args{k});
    df=diff(args{k},t);
    S=S+df^2;
end
I=int(fun*sqrt(S),t,alpha,beta);