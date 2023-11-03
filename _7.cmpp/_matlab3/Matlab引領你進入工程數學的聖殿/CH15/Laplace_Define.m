function varargout=Laplace_Define(varargin)
%LAPLACE_DEFINE   �ھکw�q�D��ƪ��Ԥ��ܴ�
% FS=LAPLACE_DEFINE(FT,T,S,'laplace')  �D���FT��laplace�ܴ�
% FT=LAPLACE_DEFINE(FS,S,T,'ilaplace')  �D���FS��laplace�f�ܴ�
%
% ��ɤJ�ѼƼơG
%     ---FT,FS�G���w���ɰ��ƩM�_����
%     ---T,S�G���FT�MFS�����ܼ�
%     ---TYPE�G���wlaplace�ܴ������A�A��'laplace'�M'ilaplace'��ب���
% ��X�ѼơG
%     ---FS,FT�G�D�o���_���ƩM�ɰ���
%
% See also int

args=varargin;
type=args{end};
switch lower(type)
    case {1,'laplace'}
        [fun,t,s]=args{1:end-1};
        L=int(fun*exp(-s*t),t);
        L=-subs(L,t,0);
    case {2,'ilaplace'}
        [fun,s,t]=args{1:end-1};
        [~,B]=numden(fun);
        S=sort(solve(B,s));
        H=FrequencyTable(S);
        S=H(:,1); P=H(:,2);
        L=0;
        for i=1:length(S)
            F=(s-S(i))^P(i)*fun*exp(s*t);
            M=diff(F,s,double(P(i)-1));
            L=L+1/gamma(P(i))*limit(M,s,S(i));
        end
end
varargout{1}=L;