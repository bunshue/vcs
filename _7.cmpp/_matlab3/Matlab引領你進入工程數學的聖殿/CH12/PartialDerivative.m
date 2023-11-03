function P=PartialDerivative(fun,var,varargin)
%PARTIALDERIVATIVE   沮熬旧计﹚竡―じㄧ计熬旧计
% P=PARTIALDERIVATIVE(FUN,VAR)  ―ㄧ计FUN闽跑计VAR熬旧计
% P=PARTIALDERIVATIVE(FUN,VAR,X,A,Y,B,...)  ―ㄧ计FUN闽VAR
%                                           翴(A,B,...)熬旧计
% P=PARTIALDERIVATIVE(FUN,VAR,{'X=A','Y=B',...})  
%
% 块旧把计计
%     ---FUNじ才腹ㄧ计
%     ---VAR才腹跑计
%     ---X,Y,...ㄧ计才腹跑计
%     ---A,B,...ㄧ计才腹跑计
% 块把计
%     ---P肚熬旧计┪熬旧计
%
% See also diff, limit

h=sym('h','real');
s=symvar(fun);
if ~ismember(var,s)
    error('Symbols variables not designated.')
end
delta=subs(fun,var,sym(var+h))-fun;
P1=limit(delta/h,h,0);
if nargin==2
    P=P1;
elseif nargin==3
    x0=varargin{:};
    N=length(x0);
    if N>length(s)
        error('Too many Symbols variable-values.')
    end
    vars=cell(1,N);
    values=cell(1,N);
    for k=1:N
        kk=strfind(x0{k},'=');
        vars{k}=x0{k}(1:kk-1);
        values{k}=str2double(x0{k}(kk+1:end));
    end
    P=subs(P1,vars,values);
elseif nargin>3 && ~mod(nargin,2)
    vars=cell(1,nargin/2-1);
    values=cell(1,nargin/2-1);
    for k=1:length(varargin)/2
        vars{k}=varargin{2*k-1};
        values{k}=varargin{2*k};
    end
    P=subs(P1,vars,values);
else
    error('Illegal numbers of input arguments.')
end