function type=AlternatingSeries(un)
%ALTERNATINGSERIES   ����żƼf�Īk
% TYPE=ALTERNATINGSERIES(UN)  �Q�εܥ������w�z�P�_����ż�(-1)^(N-1)*UN���Ĵ���
%
% ��ɤJ�ѼƼơG
%     ---UN�G�����ż�
% ��X�ѼơG
%     ---TYPE�G���ż��Ĵ��ʪ��r��
%
% See also limit

n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('�����żƤ@�붵���Ÿ��ܼƥ�����n.')
end
uN=subs(un,n,n+1);
x=subs(un-uN,n,1:1e6);
L=limit(un,n,inf);
if L==0 && all(x>=0)
    type='����';
elseif L~=0
    type='�o��';
else
    type='���T�w';
end