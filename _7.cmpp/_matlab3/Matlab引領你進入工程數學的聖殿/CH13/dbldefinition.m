function I=dbldefinition(fun,D,m,n)
%DBLDEFINITION   �ھڤG���n�����w�q�p��G���n��
% I=DBLDEFINITION(FUN,D,M)  �p����FUN�b�ϰ�D�W���G���n���AD����M*M����
% I=DBLDEFINITION(FUN,D,M,N)  �p����FUN�b�ϰ�D�W���G���n���AD����M*N����
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�G����ƪ�MATLAB�y�z�A�i�H�O�ΦW��ƩΤ��p��Ƶ�
%     ---D�G�n���ϰ�
%     ---M,N�G�n���ϰ쪺������
% ��X�ѼơG
%     ---I�G�G���n����
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