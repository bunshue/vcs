function varargout=fouriern(fun,oldvars,newvars,type,method)
%FOURIERN   �h���Ÿ̸��ܴ����D��
% F2=FOURIERN(F1,OLDVARS,NEWVARS)  �D���F1���h���Ÿ̸��ܴ�
% F2=FOURIERN(F1,OLDVARS,NEWVARS,TYPE)  �D���F1���Ÿ̸��ܴ��ΰf�ܴ��A
%                                       �ܴ����A��TYPE���w
% F2=FOURIERN(F1,OLDVARS,NEWVARS,TYPE,METHOD)  ���w����fourier��ƨD�ܴ��٬O
%                                              ����int��ƨD��
% [F2,S]=FOURIERN(...)  �D�h���Ÿ̸��ܴ��öǦ^�ܴ����A
%
% ��ɤJ�ѼƼơG
%     ---F1�G�_�l���
%     ---OLDVARS�G���F1���ܼ�
%     ---NEWVARS�G�ܴ��᪺�ܼ�
%     ---TYPE�G���w�ܴ����A�A��'fourier'�M'ifourier'��ب���
%     ---METHOD�G���w�D���ܴ�����k�A��'fourier'�M'int'��ؤ�k
% ��X�ѼơG
%     ---F2�G�D�ܴ��᪺���
%     ---S�G�ܴ����A�A������TYPE
%
% See also fourier, int

if nargin<5
    method='fourier';
end
if nargin<4 || isempty(type)
    type='fourier';
end
if ~isa(fun,'sym')
    error('FUN must be a Symbolic function.')
end
N=length(oldvars);
if length(newvars)~=N
    error('�ܼƺ��Ƥ��@�P.')
end
switch lower(method)
    case 'fourier'
        fcn=lower(type);
        for k=1:N
            fun=feval(fcn,fun,oldvars(k),newvars(k));
        end
    case 'int'
        if isequal(lower(type),'fourier')
            for k=1:N
                fun=int(fun*exp(-1j*oldvars(k)*newvars(k)),oldvars(k),-inf,inf);
            end
        elseif isequal(lower(type),'ifourier')
            for k=1:N
                fun=1/2/pi*int(fun*exp(1j*oldvars(k)*newvars(k)),...
                     oldvars(k),-inf,inf);
            end
        else
            error('Illegal TYPE.')
        end
    otherwise
        error('Illegal METHOD.')
end
if nargout==1
    varargout{1}=fun;
elseif nargout==2
    varargout{1}=fun;varargout{2}=[upper(type),'�ܴ�'];
end