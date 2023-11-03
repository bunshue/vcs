function P=PartialDerivative(fun,var,varargin)
%PARTIALDERIVATIVE   �ھڰ��ɼƪ��w�q�D�h����ƪ����ɼ�
% P=PARTIALDERIVATIVE(FUN,VAR)  �D���FUN�����ܼ�VAR�����ɼ�
% P=PARTIALDERIVATIVE(FUN,VAR,X,A,Y,B,...)  �D���FUN����VAR���b
%                                           �I(A,B,...)�W�����ɼƪ���
% P=PARTIALDERIVATIVE(FUN,VAR,{'X=A','Y=B',...})  �P�W
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�h���Ÿ����
%     ---VAR�G�Ÿ����ܼ�
%     ---X,Y,...�G��ƪ��Ÿ��ܼ�
%     ---A,B,...�G��ƪ��Ÿ��ܼƪ���
% ��X�ѼơG
%     ---P�G�Ǧ^�����ɼƩΰ��ɼƪ���
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