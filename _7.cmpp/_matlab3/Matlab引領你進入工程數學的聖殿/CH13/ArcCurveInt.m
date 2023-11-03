function I=ArcCurveInt(fun,vars,varargin)
%ARCCURVEINT   �p��Ĥ@���O���u�n��
% I=ARCCURVEINT(FUN,{'X','Y'},FUNX,FUNY,T,ALPHA,BETA)  �p��G����ƪ��Ĥ@���O���u�n��
% I=ARCCURVEINT(FUN,{'X','Y','Z'},FUNX,FUNY,FUNZ,T,ALPHA,BETA)  �p��T����ƪ�
%                                                               �Ĥ@���O���u�n��
% I=ARCCURVEINT(FUN,{'X','Y','Z',...},FUNX,FUNY,FUNZ,...,T,ALPHA,BETA)
%                                                �p��h����ƪ��Ĥ@���O���u�n��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�Q�n���
%     ---VARS�G�Q�n��ƪ��Ÿ��ܼ�
%     ---FUNX,FUNY,...�G�n�����u���ѼƤ�{��
%     ---T�G�ѼƤ�{�����Ÿ����ܼ�
%     ---ALPHA,BETA�G�n���d��
% ��X�ѼơG
%     ---I�G���u�n����
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