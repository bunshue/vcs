function equation=Asymptote(fun,varargin)
%ASYMPTOTE   �D���u������u
% EQUATION=ASYMPTOTE(FUN,H)  �D���u����������u�AH�i�H��1,'h','hor'��'horizontal'
% EQUATION=ASYMPTOTE(FUN,V,X0)  �D���u����������u�AV�i�H��2,'v','ver'��'vertical'
% EQUATION=ASYMPTOTE(FUN,L)  �D���u���׺���u�AL�i�H��3,'l'��'lean'
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���u��{������ƧΦ�
%     ---X0�G��������u��{��X=X0
%     ---H,V,L�G���w����u�����A�AH��ܤ�������u�FV��ܫ�������u�FL��ܱ׺���u
% ��X�ѼơG
%     ---EQUATION�G����u����{���A�Y���s�b�A�h�Ǧ^�r��'���s�b'
%
% See also limit

type=varargin{1};
x=sym('x','real');
s=symvar(fun);
if length(s)>1
    error('���fun�����u�]�A�@�ӲŸ��ܼ�.')
end
if ~isequal(x,s)
    fun=subs(fun,s,x);
end
switch lower(type)
    case {1,'h','hor','horizontal'}  % ��������u
        k=limit(fun,x,inf);
        if isinf(double(k))
            equation='���s�b';
        else
            equation=char(['y=',char(k)]);
        end
    case {2,'v','ver','vertical'}  % ��������u
        x0=varargin{2};
        if isempty(x0) || nargin==2
            equation='���s�b';
        else
            N=length(x0);
            equation=cell(1,N);
            for k=1:N
                if ~isinf(double(limit(fun,x,x0(k),'right'))) &&...
                        ~isinf(double(limit(fun,x,x0(k),'left')))
                    equation{k}='���s�b';
                else
                    equation{k}=char(['x=',char(sym(x0(k)))]);
                end
            end
        end
    case {3,'l','lean'}  % �׺���u
        K=limit(fun/x,x,inf);
        b=limit(fun-K*x,inf);
        if isinf(double(K)) || isequal(K,0)
            equation='���s�b';
        else
            equation=char(['y=',char(K),'*x+',char(b)]);
        end
    otherwise
        error('Illegal options.')
end