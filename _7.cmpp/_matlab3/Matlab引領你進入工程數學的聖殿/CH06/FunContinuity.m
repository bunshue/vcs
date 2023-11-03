function tf=FunContinuity(x0,fun_left,fun_x0,fun_right)
%FUNCONTINUITY   耞ㄧ计琘翴矪硈尿┦
% TF=FUNCONTINUITY(X0,FUN_LEFT,FUN_X0,FUN_RIGHT)  耞だ琿ㄧ计FUN翴X0矪硈尿┦
%               璝硈尿玥肚TF=1玥肚TF=0FUNパㄤオ笷Αの翴X0矪笷Αボ
%
% 块旧把计计
%     ---X0疭翴
%     ---FUN_LEFTX<X0ㄧ计笷Α
%     ---FUN_X0X=X0ㄧ计笷Α
%     ---FUN_RIGHTX>X0ㄧ计笷Α
% 块把计
%     ---TFㄧ计硈尿┦璝ㄧ计X0矪硈尿玥TF=1玥TF=0
%
% See also limit

fx0=subs(fun_x0,'x',x0);
fx0_left=limit(fun_left,'x',x0,'left');
fx0_right=limit(fun_right,'x',x0,'right');
if isequal(fx0,fx0_left) && isequal(fx0,fx0_right)
    tf=1;
else
    tf=0;
end
