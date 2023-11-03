function [t,y] = lineshoot(f1,f2,tspan,x0f,varargin)
%LINESHOOT   �u����Ȱ��D�����v�k�D��
% [T,Y] = LINESHOOT(F1,F2,TSPAN,X0F)  ���v�k�D�u����Ȱ��DF1����
% [T,Y] = LINESHOOT(F1,F2,TSPAN,X0F,P1,P2,...)  ���v�k�D�u����Ȱ��DF1���ѡA�䤤
%                                               F1�MF2�]�A���[�Ѽ�P1,P2,...
%
% ��ɤJ�ѼƼơG
%     ---F1,F2�G�L����{���Ψ����������{������ƴy�z
%     ---TSPAN�G�D�Ѱ϶�
%     ---X0F�G��ȱ���
%     ---P1,P2,...�G���F1�MF2�����[�Ѽ�
% ��X�ѼơG
%     ---T�G�Ǧ^���`�I
%     ---Y�G��Ȱ��D����
%
% See also ode45

[~,y1] = ode45(f2,tspan,[1;0],varargin);  % �p����y_1(t)
[~,y2] = ode45(f2,tspan,[0;1],varargin);  % �p����y_2(t)
[~,yp] = ode45(f1,tspan,[0;0],varargin);  % �p����y_p(t)
m = (x0f(2)-x0f(1)*y1(end,1)-yp(end,1))/y2(end,1);  % �D�Ѽ�m
[t,y] = ode45(f1,tspan,[x0f(1);m],varargin);  % �D�X��L����{������