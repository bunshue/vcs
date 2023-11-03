function [R,D]=ConvergenceRadius(an)
%CONVERGENCERADIUS   ���żƪ����ĥb�|�P���İ�
% R=CONVERGENCERADIUS(AN)  �D���ż�AN�����ĥb�|
% [R,D]=CONVERGENCERADIUS(AN)  �D���ż�AN�����ĥb�|�M���İ�
%
% ��ɤJ�ѼƼơG
%     ---AN�G���żƤ@�붵
% ��X�ѼơG
%     ---R�G���ĥb�|
%     ---D�G���İ�
%
% See also limit

n=sym('n','positive');
s=symvar(an);
if ~ismember(n,s)
    error('���żƨt�ƪ��Ÿ��ܼƥ�����n.')
end
aN=subs(an,n,n+1);
rho=limit(simple(abs(aN/an)),n,inf);
R=1/rho;
if R==0
    D=0;
elseif isinf(double(R))
    D='(-��,+��)';
else
    D=[-R,R];
end