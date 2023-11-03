function [I,str]=ComplexQuad(varargin)
%COMPLEXQUAD   �_�ƨD�n��k�D�ѩw�n��
% I=COMPLEXQUAD(X,Y,TYPE)  �ϥίS���_�ƨD�n��k�D������ƪ��ƭȿn��
% I=COMPLEXQUAD(FUN,A,B,N,TYPE)  �ϥίS���_�ƨD�n��k�D���FUN���ƭȿn��
% [I,STR]=COMPLEXQUAD(...)  �ϥδ_�ƨD�n��k�D�ƭȿn���öǦ^�Ҫ��Ϊ��_�Ƥ�k
%
% ��ɤJ�ѼƼơG
%     ---X,Y�G�[����ơA�����V�q
%     ---FUN�G�Q�n���
%     ---A,B�G�n���U���M�W��
%     ---N�G�n���϶�������
%     ---TYPE�G�S���_�Ƥ�k���A�A���H�U���ȡG
%              1.'trape'��1�G�_�Ʊ�ΨD�n
%              2.'simpson'��2�G�_�ƨ����˨D�n
%              3.'cotes'��4�G�_��Cotes�D�n
% ��X�ѼơG
%     ---I�G�Ǧ^���ƭȿn����
%     ---STR�G�Ǧ^���_�Ƥ�k
%
% See also InterpolatoryQuad

args=varargin;
type=args{end};
num=[1,2,4];
S={'trape','simpson','cotes'};
if ~isnumeric(type)
    I=ismember(S,type);
    n=num(I==1);
else
    n=type;
end
if isnumeric(args{1})
    x=args{1};
    y=args{2};
    N=length(x);
    if rem(N-1,n)~=0
        error('��ƪ����׻P�ҿ諸�D�n��k���ŦX.')
    end
    Nn=(N-1)/n;
    h=(x(N)-x(1))/Nn;
else
    [fun,a,b,Nn]=deal(args{1:end-1});
    h=(b-a)/Nn;
    x=a+h/n*(0:n*Nn);
    N=length(x);
    y=feval(fun,x);
end
switch lower(type)
    case {1,'trape'}
        str='�_�Ʊ�ΨD�n';
        I=h*[1,2*ones(1,Nn-1),1]*y'/2;
    case {2,'simpson'}
        str='�_�ƨ����˨D�n';
        a=[1,reshape([4*ones(1,Nn-1);2*ones(1,Nn-1)],1,[]),4,1];
        I=h/6*a*y';
    case {4,'cotes'}
        str='�_��Cotes�D�n';
        a=[7,reshape([32*ones(1,Nn-1);12*ones(1,Nn-1);...
            32*ones(1,Nn-1);14*ones(1,Nn-1)],1,N-5),32,12,32,7];
        I=h/90*a*y';
    otherwise
        error('Illegal options.')
end