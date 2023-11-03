function [t,y] = nlshoot(f1,fv,tspan,x0f,tol,varargin)
%NLSHOOT   �D�u����Ȱ��D�����v�k�D��
% [T,Y] = NLSHOOT(F1,FV,TSPAN,X0F,TOL)  ���v�k�D�D�u����Ȱ��DF1����
% [T,Y] = NLSHOOT(F1,FV,TSPAN,X0F,TOL,P1,P2,...)  ���v�k�D�D�u����Ȱ��DF1���ѡA
%                                              �䤤F1�AFV�]�A���[�Ѽ�P1,P2,...
%
% ��ɤJ�ѼƼơG
%     ---F1,FV�G�L����{���P�e�����Ъ������ܼ�v1,v2,v3,v4���L����{������ƴy�z
%     ---TSPAN�G�D�Ѱ϶�
%     ---X0F�G���w����ȱ���
%     ---TOL�G��׭n�D�A�Ω󱱨�Ѽ�m���~�t
%     ---P1,P2,...�G���F1�MFV�����[�Ѽ�
% ��X�ѼơG
%     ---T�G�Ǧ^���`�I
%     ---Y�G��Ȱ��D����
%
% See also ode45, lineshoot

m0=1;  % m�����
err=1;
while abs(err)>tol;
    [~,v] = ode45(fv,tspan,[x0f(1);m0;0;1],varargin);  % �p�⭡�N��
    m=m0-(v(end,1)-x0f(2))/v(end,3);  % ��sm���ƭ�
    err=m-m0;
    m0=m;
end
[t,y] = ode45(f1,tspan,[x0f(1);m],varargin);  % �Q�αo�쪺��ȨD�Ѥ�{��