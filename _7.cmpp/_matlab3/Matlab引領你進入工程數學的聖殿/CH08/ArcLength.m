function L=ArcLength(varargin)
%ARCLENGTH   計算平面曲線的弧長
% L=ARCLENGTH(FUNX,FUNY,T,ALPHA,BETA,'dicarl')  計算直角座標系下由參數方程式
%                                                        所描述的平面曲線的弧長
% L=ARCLENGTH(FUN,T,ALPHA,BETA,'polar')  計算極座標系下有FUN所描述的曲線的弧長
%
% 輸導入參數數：
%     ---FUNX,FUNY：直角座標系下平面曲線的參數方程式
%     ---FUN：平面曲線的極座標方程式
%     ---ALPHA,BETA：積分的下限與上限
%     ---TYPE：座標系型態，TYPE有以下兩種取值：
%               1.'dicarl'或'd'或1：直角座標系
%               2.'polar'或'p'或2：極座標系
% 輸出參數：
%     ---L：傳回的平面曲線的弧長
%
% See also int

args=varargin;
type=args{end};
switch lower(type)
    case {1,'d','dicarl'}
        [funx,funy,t,alpha,beta]=deal(args{1:5});
    case {2,'p','polar'}
        [fun,t,alpha,beta]=deal(args{1:4});
        funx=fun*cos(t);
        funy=fun*sin(t);        
    otherwise
        error('Illegal options.')
end
dfx=diff(funx,t);
dfy=diff(funy,t);
L=simple(int(sqrt(dfx^2+dfy^2),t,alpha,beta));