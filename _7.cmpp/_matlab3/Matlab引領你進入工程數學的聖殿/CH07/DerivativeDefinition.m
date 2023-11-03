function df=DerivativeDefinition(fun,x,x0,type)
%DERIVATIVEDEFINITION   沮旧计﹚竡―ㄧ计旧ㄧ计┪琘翴矪旧计
% DF=DERIVATIVEDEFINITION(FUN,X)┪
% DF=DERIVATIVEDEFINITION(FUN,X,[])  ―ㄧ计FUN闽X旧ㄧ计
% DF=DERIVATIVEDEFINITION(FUN,X,X0)  ―ㄧ计FUN翴X0矪旧ㄧ计
% DF=DERIVATIVEDEFINITION(FUN,X,X0,TYPE)  沮TYPE﹚旧计篈―ㄧ计翴X0矪旧计
%                                                 TYPEΤ
%                                                 1.'double'┪0蛮凹旧计箇砞
%                                                 2.'left'┪-1オ旧计
%                                                 3.'right'┪1旧计
% DF=DERIVATIVEDEFINITION(FUN,X,[],TYPE)  沮TYPE﹚旧计篈―ㄧ计旧ㄧ计
%
% 块旧把计计
%     ---FUN才腹ㄧ计笷Α
%     ---X才腹跑计
%     ---X0―旧翴
%     ---TYPE旧计篈
% 块把计
%     ---DF肚旧ㄧ计┪旧计
%
% See also limit, diff

if nargin<4
    type=0;
end
if nargin==2 || isempty(x0)
    x0=x;
end
syms h
delta_y=subs(fun,x,x0+h)-subs(fun,x,x0);
switch type
    case {0,'double'}
        df=limit(delta_y/h,h,0);  % ―旧计
    case {-1,'left'}
        df=limit(delta_y/h,h,0,'left');  % ―オ旧计
    case {1,'right'}
        df=limit(delta_y/h,h,0,'right');  % ―旧计
    otherwise
        error('The Style of Derivative is Illegal.')
end
