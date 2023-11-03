function [tf,str]=BreakPoint(x0,fun_left,fun_x0,fun_right)
%BREAKPOINT   判斷函數在某點處的間斷點型態
% [TF,STR]=BREAKPOINT(X0,FUN_LEFT,FUN_X0,FUN_RIGHT)  判斷函數FUN在X0處的間斷性，
%                                                              並傳回間斷點型態
%
% 輸導入參數數：
%     ---X0：特殊的點
%     ---FUN_LEFT：X<X0時的函數表達式
%     ---FUN_X0：X=X0時的函數表達式
%     ---FUN_RIGHT：X>X0時的函數表達式
% 輸出參數：
%     ---TF：函數的連續性，若函數在X0處連續，則TF=1；否則TF=0
%     ---STR：間斷點型態字串，STR可以為'無窮間斷點'、'可去間斷點'、'振蕩間斷點'、
%              '跳躍間斷點'和'函數在該點連續.'五種情形之一
%
% See also FunContinuity, limit

fx0_left=limit(fun_left,'x',x0,'left');
fx0_right=limit(fun_right,'x',x0,'right');
tf=1;
if isempty(fun_x0)
    tf=0;
else
    if isnan(fx0_left) || isnan(fx0_right) ||...  % 極限不存在
            isinf(double(fx0_left)) || isinf(double(fx0_right))
        tf=0;
    else   % 極限存在
        fx0=subs(fun_x0,'x',x0);
        if ~isequal(fx0,fx0_left) || ~isequal(fx0,fx0_right)
            tf=0;
        end
    end
end
if tf==0
    if isinf(double(fx0_left)) || isinf(double(fx0_right))  % 左或右極限是否為無窮大
        str='無窮間斷點';
    elseif isequal(fx0_left,fx0_right)  % 判斷左右極限是否相等
        str='可去間斷點';
    elseif isnan(fx0_left) || isnan(fx0_right)  % 判斷左極限或右極限是否存在
        str='振蕩間斷點';
    else
        str='跳躍間斷點';
    end
else
    str='函數在該點連續.';
end
