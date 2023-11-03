function [I,Interval,s]=int_geo(fun,a,b,N)
%INT_GEO  �ھکw�n�����X��N�q�D�w�n��
% I=INT_GEO(FUN,A,B)  �Q�Ωw�n�����X��N�q�p����FUN���n���ȡA�n���W�U�����O��B�MA
% I=INT_GEO(FUN,A,B,N)  �Q�Ωw�n�����X��N�q�p��w�n���A�϶������Ƭ�N
% [I,INTERVAL]=INT_GEO(...)  �Q�Ωw�n�����X��N�q�p��w�n���A�öǦ^���Ϋ�t�϶�
% [I,INTERVAL,S]=INT_GEO(...)  �Q�Ωw�n�����X��N�q�p��w�n���A�öǦ^���Ϋ�t�϶�
%                                    �H�ι����϶��W���n����
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ�MATLAB�y�z�A�i�H���ΦW��ơB���p��Ʃ�M�ɮ�
%     ---A,B�G�n���U���M�W��
%     ---N�G�U���Ϋ�t�϶�������
% ��X�ѼơG
%     ---I�G�n����
%     ---INTERVAL�G���Ϋ�t�϶�
%     ---S�G�U�϶��W���n����
%
% See also RootInterval, bisect, diff

if nargin<4
    N=1000;
end
r=RootInterval(fun,a,b);
if ~isempty(r)
    n=size(r,1);
    x=ones(1,n+2);
    x(1)=a; x(end)=b;
    for k=1:n
        x(k+1)=bisect(fun,r(k,1),r(k,2));
    end
    x=unique(x);
    L=length(x);
    Interval=zeros(2,L-1);
    for kk=1:L-1
        Interval(:,kk)=x(kk:kk+1);
    end
else
    Interval=[a;b];
end
h=diff(Interval)/N;
M=mean(Interval);
fM=feval(fun,M);
fM(fM>0)=1;
fM(fM<0)=-1;
s=zeros(1,size(Interval,2));
for k=1:size(Interval,2)
    xx=Interval(1,k)+h(k)*(0:N);
    fx=abs(feval(fun,xx));
    s(k)=sum(fx)*h(k);
end
I=sum(s.*fM);