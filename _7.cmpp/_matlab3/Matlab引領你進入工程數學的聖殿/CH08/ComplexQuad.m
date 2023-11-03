function [I,str]=ComplexQuad(varargin)
%COMPLEXQUAD   確て―縩よ猭―秆﹚縩だ
% I=COMPLEXQUAD(X,Y,TYPE)  ㄏノ疭確て―縩よ猭―瞒床戈计縩だ
% I=COMPLEXQUAD(FUN,A,B,N,TYPE)  ㄏノ疭確て―縩よ猭―ㄧ计FUN计縩だ
% [I,STR]=COMPLEXQUAD(...)  ㄏノ確て―縩よ猭―计縩だ肚┮ノ確てよ猭
%
% 块旧把计计
%     ---X,Y芠代戈单秖
%     ---FUN砆縩ㄧ计
%     ---A,B縩だ㎝
%     ---N縩だ跋丁单だ计
%     ---TYPE疭確てよ猭篈Τ
%              1.'trape'┪1確て辫―縩
%              2.'simpson'┪2確てǒ炊此―縩
%              3.'cotes'┪4確てCotes―縩
% 块把计
%     ---I肚计縩だ
%     ---STR肚確てよ猭
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
        error('戈籔┮匡―縩よ猭ぃ才.')
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
        str='確て辫―縩';
        I=h*[1,2*ones(1,Nn-1),1]*y'/2;
    case {2,'simpson'}
        str='確てǒ炊此―縩';
        a=[1,reshape([4*ones(1,Nn-1);2*ones(1,Nn-1)],1,[]),4,1];
        I=h/6*a*y';
    case {4,'cotes'}
        str='確てCotes―縩';
        a=[7,reshape([32*ones(1,Nn-1);12*ones(1,Nn-1);...
            32*ones(1,Nn-1);14*ones(1,Nn-1)],1,N-5),32,12,32,7];
        I=h/90*a*y';
    otherwise
        error('Illegal options.')
end