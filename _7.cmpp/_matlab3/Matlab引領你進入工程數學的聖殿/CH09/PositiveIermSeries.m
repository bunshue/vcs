function [L,type]=PositiveIermSeries(un,mode)
%POSITIVEIERMSERIES   �����żƪ���ȼf�Īk�M�ڭȼf�Īk
% L=POSITIVEIERMSERIES(UN)  ��ȼf�Īk�P�_�����żƪ��Ĵ���
% L=POSITIVEIERMSERIES(UN,MODE)  ��ίS���f�Īk�P�_�����żƪ��Ĵ���
% [L,TYPE]=POSITIVEIERMSERIES(...)  ��ίS���f�Īk�P�_�����żƪ��Ĵ���
%                                   �öǦ^�ҨϥΪ��f�Īk
%
% ��ɤJ�ѼƼơG
%     ---UN�G�����żƳq��
%     ---MODE�G�S���f�Īk�AMODE���H�U��Ө��ȡG
%              1.'d'��'���'��1�G��ȼf�Īk
%              2.'k'��'�ڭ�'��2�G�ڭȼf�Īk
% ��X�ѼơG
%     ---L�G�Ǧ^���q�����Y�ث��A��������
%     ---TYPE�G�ҨϥΪ��f�Īk
%
% See also limit

if nargin==1
    mode=1;
end
n=sym('n','positive');
s=symvar(un);
if ~ismember(n,s)
    error('�����żƤ@�붵���Ÿ��ܼƥ�����n.')
end
switch lower(mode)
    case {1,'d','���'}
        type='��ȼf�Īk';
        uN=subs(un,'n',n+1);
        L=limit(simple(uN/un),'n',inf);
    case {2,'k','�ڭ�'}
        type='�ڭȼf�Īk';
        L=limit(simple(un^(1/n)),'n',inf);
    otherwise
        error('Illegal options.')
end
if length(s)==1
    if double(L)<1
        type=[type,'�G����'];
    elseif double(L)>1
        type=[type,'�G�o��'];
    else
        error('�ثe�ҿ�����f�Īk����.')
    end
end