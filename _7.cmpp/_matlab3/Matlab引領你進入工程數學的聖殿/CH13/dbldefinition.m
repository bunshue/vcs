function I=dbldefinition(fun,D,m,n)
%DBLDEFINITION   沮縩だ﹚竡璸衡縩だ
% I=DBLDEFINITION(FUN,D,M)  璸衡ㄧ计FUN跋办D縩だDだM*M场だ
% I=DBLDEFINITION(FUN,D,M,N)  璸衡ㄧ计FUN跋办D縩だDだM*N场だ
%
% 块旧把计计
%     ---FUNじㄧ计MATLAB磞瓃琌拔ㄧ计┪ず羛ㄧ计单
%     ---D縩だ跋办
%     ---M,N縩だ跋办购だ计
% 块把计
%     ---I縩だ
%
% See also sum, diff

if nargin<4
    n=m;
end
a=min(D(1,:));
b=max(D(1,:));
c=min(D(2,:));
d=max(D(2,:));
x=linspace(a,b,m);
y=linspace(c,d,n);
[X,Y]=meshgrid(x,y);
in=inpolygon(X(:),Y(:),D(1,:),D(2,:));
f=fun(X(in),Y(in));
I=sum(f*diff(x(1:2))*diff(y(1:2)));