function [L,type]=LimitSeries(un,p)
%LIMITSERIES   �����żƪ������f�Īk
% L=LIMITSERIES(UN)  �����f�Īk�P�_�����ż�UN���Ĵ��ʡAp-�żƤ�p��1
% L=LIMITSERIES(UN,P)  �����f�Īk�P�_�����ż�UN���Ĵ��ʡAP>1
% [L,TYPE]=LIMITSERIES(...)  �����f�Īk�P�_�����ż�UN���Ĵ��ʡA�öǦ^�żƪ��Ĵ��ʦr��
%
% ��ɤJ�ѼƼơG
%     ---UN�G�����ż�
%     ---P�Gp�żƪ�����
% ��X�ѼơG
%     ---L�G������
%     ---TYPE�G���ż��Ĵ��ʪ��r��
%
% See also limit

if nargin==1
    p=1;
end
if p<1
    error('����żƪ�������p�����j�󵥩�1.')
end
n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('�����żƤ@�붵���Ÿ��ܼƥ�����n.')
end
L=limit(n^p*un,n,inf);
if p==1
    if length(s)==1
        if double(L)>0
            type='�o��';
        end
    end
else
    if double(L)>=0
        type='����';
    end
end