function y=realfunvalue(fun,x)
%REALFUNVALUE   �b�_�ƽd�򤺨D��Ʀb�Y�I�B�����ƭ�
% Y=REALFUNVALUE(FUN,X)  �b�_�ƽd�򤺨D���FUN�bX�B�����ƭ�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ��Ÿ���F��
%     ---X�G�S�����ܼƭ�
% ��X�ѼơG
%     ---Y�G�Ǧ^�����ƭ�
%
% See also finverse, solve

warning off all
F=subs(fun,x);
if ~isreal(F)
    t=symvar(fun);
    t=sym(t,'real');
    f=finverse(fun);
    y=solve(f-x,t);
else
    y=F;
end
y=double(y);