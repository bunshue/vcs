function I=InterpolatoryQuad(varargin)
%INTERPOLATORYQUAD   ���ȫ���k�D�ѩw�n��
% I=INTERPOLATORYQUAD(X,Y)  �p��������ƿn��
% I=INTERPOLATORYQUAD(FUN,A,B,N)  �p����FUN�b�n����[A,B]�W���n���A�ë��w�϶������Ƭ�N
%
% ��ɤJ�ѼƼơG
%     ---X,Y�G�[����ơA�������V�q
%     ---FUN�G�Q�n���
%     ---A,B�G�n���U���M�W��
%     ---N�G�϶�������
% ��X�ѼơG
%     ---I�G���ȫ��D�n���G
%
% See also polyfit, polyint, polyval

args=varargin;
if isnumeric(args{1})
    x=args{1};
    y=args{2};
    N=length(x)-1;
else
    [fun,a,b,N]=deal(args{:});
    h=(b-a)/N;
    x=a+h*(0:N);
    y=feval(fun,x);
end
p=polyfit(x,y,N);
P=polyint(p);
I=polyval(P,x(end))-polyval(P,x(1));