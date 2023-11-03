function S=GraphicArea(varargin)
%GRAPHICAREA   使用定積分求平面圖形的面積
% S=GRAPHICAREA(F,G,A,B,'dicarl')  計算直角座標系下曲線F和G與直線X=A、X=B所圍圖形
%                                         的面積，適用於函數F和G只包括一個符號變數的情形
% S=GRAPHICAREA(F,G,X,A,B,'dicarl')  計算直角座標系下曲線F和G與直線X=A、X=B所圍
%                                           圖形的面積，並指定符號自變數為X
% S=GRAPHICAREA(R,ALPHA,BETA,'polar')  計算極座標系下曲線R與T=ALPHA、T=BETA所圍圖形
%                                              的面積，其中R只包括一個符號變數T
% S=GRAPHICAREA(R,T,ALPHA,BETA,'polar')  計算極座標系下曲線R與T=ALPHA、T=BETA所圍
%                                                圖形的面積，並指定符號自變數為T
%
% 輸導入參數數：
%     ---F,G：直角座標系下曲線的函數描述
%     ---R：極座標系下曲線的函數描述
%     ---A,B：直角座標系下的積分下限與上限
%     ---ALPHA,BETA：極座標系下的積分下限與上限
%     ---TYPE：座標系型態，有'dicarl'和'polar'兩種取值
% 輸出參數：
%     ---S：傳回的圖形的面積
%
% See also int

args=varargin;
type=args{end};
switch lower(type)
    case 'dicarl'
        f1=args{1};
        f2=args{2};
        s=unique([symvar(f1),symvar(f2)]);
        if length(s)>1 || nargin==6
            x=args{3};
            a=args{4};
            b=args{5};
        else
            if nargin==5
                x=s;
                a=args{3};
                b=args{4};
            end
        end
        S=simple(int(f1-f2,x,a,b));
    case 'polar'
        r=args{1};
        s=symvar(r);
        if length(s)>1 || nargin==5
            t=args{2};
            alpha=args{3};
            beta=args{4};
        else
            if nargin==4
                t=s;
                alpha=args{2};
                beta=args{3};
            end
        end
        S=simple(1/2*int(r^2,t,alpha,beta));
    otherwise
        error('Illegal options.')
end
S=abs(S);