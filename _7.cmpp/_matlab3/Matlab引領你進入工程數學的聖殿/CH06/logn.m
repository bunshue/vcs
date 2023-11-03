function y=logn(x,a)
%LOGN   �D���N�������
% Y=LOGN(X,A)  �D���Ƭ�A�B�u�Ƭ�X����ơA�N���G�Ǧ^��Y��
%
% ��ɤJ�ѼƼơG
%     ---X�G��ƪ��u��
%     ---A�G��ƪ�����
% ��X�ѼơG
%     ---Y�G�Ǧ^����ƭ�
%
% See also log, log2, log10

if ~isequal(class(x),class(a))
    error('LOGN requires input arguments be the same class.');
end
if ~(isa([x,a],'double')||isa([x,a],'single'))
    error('LOGN requires input arguments of double or single class.');
end
switch a
    case exp(1)
        y=log(x);  % �۵M���
    case 2
        y=log2(x);  % �H2���������
    case 10
        y=log10(x);  % �`�ι��
    otherwise
        y=log(x)/log(a);  % ���������A�o�̴���������b����e
end
