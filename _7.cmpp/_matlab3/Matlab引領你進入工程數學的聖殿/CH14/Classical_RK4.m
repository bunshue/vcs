function [x,y]=Classical_RK4(odefun,xspan,y0,h,varargin)
%CLASSICAL_RK4   �g��|��Runge-Kutta�k�D�Ѫ�Ȱ��D���ƭȸ�
% [X,Y]=CLASSICAL_RK4(ODEFUN,XSPAN,Y0,H)  �g��|��Runge-Kutta�k�D�ѷL����{��ODEFUN
% [X,Y]=CLASSICAL_RK4(ODEFUN,XSPAN,Y0,H,P1,P2,...)  �g��|��Runge-Kutta�k�D��
%                                  �L����{��ODEFUN�AODEFUN�]�A���[�Ѽ�P1,P2,...
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
% See also Explicit_Euler

x=xspan(1):h:xspan(2);
N=length(x);
y=zeros(1,N);
y(1)=y0;
for k=1:length(x)-1
    K1=feval(odefun,x(k),y(k),varargin{:});
    K2=feval(odefun,x(k)+h/2,y(k)+h/2*K1,varargin{:});
    K3=feval(odefun,x(k)+h/2,y(k)+h/2*K2,varargin{:});
    K4=feval(odefun,x(k)+h,y(k)+h*K3,varargin{:});
    y(k+1)=y(k)+h/6*(K1+2*K2+2*K3+K4);
end
x=x';y=y';