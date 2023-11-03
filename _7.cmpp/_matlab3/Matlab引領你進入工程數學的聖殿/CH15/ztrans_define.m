function varargout=ztrans_define(varargin)
%ZTRANS_DEFINE   沮﹚竡―ㄧ计z跑传
% EZ=ZTRANS_DEFINE(EN,N,Z,'ztrans')  ―ENz跑传
% EN=ZTRANS_DEFINE(EZ,Z,N,'iztrans')  ―z跑传ΑEZz癴跑传
%
% 块旧把计计
%     ---EN,EZ﹚┪z跑传Α笷Α
%     ---N,ZEN㎝EZ才腹跑计
%     ---TYPE﹚z跑传篈Τ'ztrans'㎝'iztrans'ㄢ贺
% 块把计
%     ---EZ,EN―眔z跑传Α┪z癴跑传Α
%
% See also Laplace_Define

args=varargin;
type=args{end};
switch lower(type)
    case {1,'ztrans'}
        [en,n,z]=deal(varargin{1:end-1});
        Ez=symsum(en*z^(-n),n,0,inf);
        varargout{1}=Ez;
    case {2,'iztrans'}
        [Ez,z,n]=deal(varargin{1:end-1});
        Ez=Ez*z^(n-1);
        [~,den]=numden(simple(Ez));
        zk=sort(solve(den,z));
        H=FrequencyTable(zk);
        S=H(:,1); P=H(:,2);
        R=0;
        for k=1:length(S)
            D=diff((z-zk(k))^P(k)*Ez,z,double(P(k)-1));
            R=R+1/gamma(P(k))*limit(D,z,zk(k));
        end
        varargout{1}=R;
end