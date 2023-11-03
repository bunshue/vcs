function varargout=Laplace_Define(varargin)
%LAPLACE_DEFINE   沮﹚竡―ㄧ计┰ん跑传
% FS=LAPLACE_DEFINE(FT,T,S,'laplace')  ―ㄧ计FTlaplace跑传
% FT=LAPLACE_DEFINE(FS,S,T,'ilaplace')  ―ㄧ计FSlaplace癴跑传
%
% 块旧把计计
%     ---FT,FS﹚办ㄧ计㎝確办ㄧ计
%     ---T,Sㄧ计FT㎝FS跑计
%     ---TYPE﹚laplace跑传篈Τ'laplace'㎝'ilaplace'ㄢ贺
% 块把计
%     ---FS,FT―眔確办ㄧ计㎝办ㄧ计
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