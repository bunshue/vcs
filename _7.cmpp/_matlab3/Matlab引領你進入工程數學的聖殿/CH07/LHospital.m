function varargout=LHospital(num,den,x,a)
%LHOSPITAL   洛必達法則求極限
% L=LHOSPITAL(NUM,DEN)或L=LHOSPITAL(NUM,DEN,[])  洛必達法則計算NUM/DEN在0處的極限
% L=LHOSPITAL(NUM,DEN,X)  洛必達法則計算NUM/DEN關於X=0處的極限
% L=LHOSPITAL(NUM,DEN,X,A)  洛必達法則計算NUM/DEN關於X=A處的極限
% [L,FORM]=LHOSPITAL(...)  洛必達法則計算NUM/DEN的極限並傳回極限值L和未定式型態FORM
% [L,FORM,K]=LHOSPITAL(...)  洛必達法則計算NUM/DEN的極限並傳回極限值L、
%                                 未定式型態FORM和洛必達法則使用次數K
%
% 輸導入參數數：
%     ---NUM,DEN：極限式的分子和分母表達式
%     ---X：符號自變數
%     ---A：極限點
% 輸出參數：
%     ---L：極限值
%     ---FORM：未定式型態，內含'∞/∞'和'0/0'
%     ---K：洛必達法則使用次數
%
% See also diff, subs

if nargin<4
    a=0;
end
if nargin<3 || isempty(x)
    x=unique([symvar(num),symvar(den)]);
    if length(x)>1
        error('The Symbolic variable not point out.')
    end
end
fa=subs(num,x,a);
Fa=subs(den,x,a);
if isinf(fa) && isinf(Fa)
    form='∞/∞';
elseif fa==0 && Fa==0
    form='0/0';
else
    error('未定式型式不正確.')
end
k=1;
while 1
    num=diff(num);
    den=diff(den);
    fa=subs(num,x,a);
    Fa=subs(den,x,a);
    switch form
        case '∞/∞'
            if isinf(Fa) && ~isinf(fa)
                L=0;
                break
            end
            if ~isinf(Fa)
                L=subs(num/den,x,sym(a));
                break
            end
        case '0/0'
            if Fa==0 && fa~=0
                L=inf;
                break
            end
            if Fa~=0
                L=subs(num/den,x,sym(a));
                break
            end
    end
    k=k+1;
end
if nargout==1
    varargout{1}=L;
elseif nargout==2
    varargout{1}=L;
    varargout{2}=form;
elseif nargout==3
    varargout{1}=L;
    varargout{2}=form;
    varargout{3}=k;
else
    error('Wrong number of output arguments.')
end
