function equation=Asymptote(fun,varargin)
%ASYMPTOTE   求曲線的漸近線
% EQUATION=ASYMPTOTE(FUN,H)  求曲線的水平漸近線，H可以為1,'h','hor'或'horizontal'
% EQUATION=ASYMPTOTE(FUN,V,X0)  求曲線的垂直漸近線，V可以為2,'v','ver'或'vertical'
% EQUATION=ASYMPTOTE(FUN,L)  求曲線的斜漸近線，L可以為3,'l'或'lean'
%
% 輸導入參數數：
%     ---FUN：曲線方程式的函數形式
%     ---X0：垂直漸近線方程式X=X0
%     ---H,V,L：指定漸近線的型態，H表示水平漸近線；V表示垂直漸近線；L表示斜漸近線
% 輸出參數：
%     ---EQUATION：漸近線的方程式，若不存在，則傳回字串'不存在'
%
% See also limit

type=varargin{1};
x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('函數fun必須只包括一個符號變數.')
end
if ~isequal(x,s)
    fun=subs(fun,s,x);
end
switch lower(type)
    case {1,'h','hor','horizontal'}  % 水平漸近線
        k=limit(fun,x,inf);
        if isinf(double(k))
            equation='不存在';
        else
            equation=char(['y=',char(k)]);
        end
    case {2,'v','ver','vertical'}  % 垂直漸近線
        x0=varargin{2};
        if isempty(x0) || nargin==2
            equation='不存在';
        else
            N=length(x0);
            equation=cell(1,N);
            for k=1:N
                if ~isinf(double(limit(fun,x,x0(k),'right'))) &&...
                        ~isinf(double(limit(fun,x,x0(k),'left')))
                    equation{k}='不存在';
                else
                    equation{k}=char(['x=',char(sym(x0(k)))]);
                end
            end
        end
    case {3,'l','lean'}  % 斜漸近線
        K=limit(fun/x,x,inf);
        b=limit(fun-K*x,inf);
        if isinf(double(K)) || isequal(K,0)
            equation='不存在';
        else
            equation=char(['y=',char(K),'*x+',char(b)]);
        end
    otherwise
        error('Illegal options.')
end