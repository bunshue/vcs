function I=CoordinateCurveInt(fun,vars,fun_para,t,alpha,beta)
%COORDINATECURVEINT   �p��ĤG���O���u�n��
% I=COORDINATECURVEINT(FUN,VARS,FUN_PARA,T,ALPHA,BETA)  �p����FUN���ĤG���O���u�n��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�Q�n��ƦV�q
%     ---VARS�G�Ÿ��ܼ�
%     ---FUN_PARA�G�n�����u���ѼƤ�{�����Ÿ���F��
%     ---T�G�ѼƤ�{�����Ÿ����ܼ�
%     ---ALPHA,BETA�G�n���϶�
% ��X�ѼơG
%     ---I�G�ĤG���O���u�n����
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