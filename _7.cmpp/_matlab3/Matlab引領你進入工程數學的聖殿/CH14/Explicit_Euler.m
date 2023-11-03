function [x,y]=Explicit_Euler(odefun,xspan,y0,h,varargin)
%EXPLICIT_EULER   �کԪk�D�Ѫ�Ȱ��D���ƭȸ�
% [X,Y]=EXPLICIT_EULER(ODEFUN,XSPAN,Y0,H)  �کԪk�D�L����{��ODEFUN���ƭȸ�
% [X,Y]=EXPLICIT_EULER(ODEFUN,XSPAN,Y0,H,P1,P2,...)  �کԪk�D�L����{��ODEFUN
%                                      ���ƭȸѡAODEFUN�t�����[�Ѽ�P1,P2,...
%
% ��ɤJ�ѼƼơG
%     ---ODEFUN�G�L����{������ƴy�z
%     ---XSPAN�G�D�Ѱ϶�[x0,xn]
%     ---Y0�G�_�l����
%     ---H�G���N�B��
%     ---P1,P2,...�GODEFUN��ƪ����[�Ѽ�
% ��X�ѼơG
%     ---X�G�Ǧ^���`�I�A�YX=XSPAN(1):H:XSPAN(2)
%     ---Y�G�L����{�����ƭȸ�
%
% See also ode*

x=xspan(1):h:xspan(2);
N=length(x);
y=zeros(1,N);
y(1)=y0;
for k=1:N-1
    y(k+1)=y(k)+h*feval(odefun,x(k),y(k),varargin{:});
end
x=x';y=y';