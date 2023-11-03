function df=DerivativeDefinition(fun,x,x0,type)
%DERIVATIVEDEFINITION   �ھھɼƪ��w�q�D��ƪ��ɨ�ƩΦb�Y�I�B�ɼƭ�
% DF=DERIVATIVEDEFINITION(FUN,X)��
% DF=DERIVATIVEDEFINITION(FUN,X,[])  �D���FUN����X���ɨ��
% DF=DERIVATIVEDEFINITION(FUN,X,X0)  �D���FUN�b�IX0�B���ɨ��
% DF=DERIVATIVEDEFINITION(FUN,X,X0,TYPE)  �ھ�TYPE���w�ɼƫ��A�D��Ʀb�IX0�B���ɼơA
%                                                 TYPE���H�U���ȡG
%                                                 1.'double'��0�G�����ɼƭȡA�����w�]��
%                                                 2.'left'��-1�G���ɼ�
%                                                 3.'right'��1�G�k�ɼ�
% DF=DERIVATIVEDEFINITION(FUN,X,[],TYPE)  �ھ�TYPE���w�ɼƫ��A�D��ƪ��ɨ��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�Ÿ���ƪ�F��
%     ---X�G�Ÿ����ܼ�
%     ---X0�G�D���I
%     ---TYPE�G�ɼƫ��A
% ��X�ѼơG
%     ---DF�G�Ǧ^���ɨ�Ʃξɼƭ�
%
% See also limit, diff

if nargin<4
    type=0;
end
if nargin==2 || isempty(x0)
    x0=x;
end
syms h
delta_y=subs(fun,x,x0+h)-subs(fun,x,x0);
switch type
    case {0,'double'}
        df=limit(delta_y/h,h,0);  % �D�ɼ�
    case {-1,'left'}
        df=limit(delta_y/h,h,0,'left');  % �D���ɼ�
    case {1,'right'}
        df=limit(delta_y/h,h,0,'right');  % �D�k�ɼ�
    otherwise
        error('The Style of Derivative is Illegal.')
end
