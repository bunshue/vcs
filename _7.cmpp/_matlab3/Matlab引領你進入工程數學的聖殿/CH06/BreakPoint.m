function [tf,str]=BreakPoint(x0,fun_left,fun_x0,fun_right)
%BREAKPOINT   �P�_��Ʀb�Y�I�B�����_�I���A
% [TF,STR]=BREAKPOINT(X0,FUN_LEFT,FUN_X0,FUN_RIGHT)  �P�_���FUN�bX0�B�����_�ʡA
%                                                              �öǦ^���_�I���A
%
% ��ɤJ�ѼƼơG
%     ---X0�G�S���I
%     ---FUN_LEFT�GX<X0�ɪ���ƪ�F��
%     ---FUN_X0�GX=X0�ɪ���ƪ�F��
%     ---FUN_RIGHT�GX>X0�ɪ���ƪ�F��
% ��X�ѼơG
%     ---TF�G��ƪ��s��ʡA�Y��ƦbX0�B�s��A�hTF=1�F�_�hTF=0
%     ---STR�G���_�I���A�r��ASTR�i�H��'�L�a���_�I'�B'�i�h���_�I'�B'�������_�I'�B
%              '���D���_�I'�M'��Ʀb���I�s��.'���ر��Τ��@
%
% See also FunContinuity, limit

fx0_left=limit(fun_left,'x',x0,'left');
fx0_right=limit(fun_right,'x',x0,'right');
tf=1;
if isempty(fun_x0)
    tf=0;
else
    if isnan(fx0_left) || isnan(fx0_right) ||...  % �������s�b
            isinf(double(fx0_left)) || isinf(double(fx0_right))
        tf=0;
    else   % �����s�b
        fx0=subs(fun_x0,'x',x0);
        if ~isequal(fx0,fx0_left) || ~isequal(fx0,fx0_right)
            tf=0;
        end
    end
end
if tf==0
    if isinf(double(fx0_left)) || isinf(double(fx0_right))  % ���Υk�����O�_���L�a�j
        str='�L�a���_�I';
    elseif isequal(fx0_left,fx0_right)  % �P�_���k�����O�_�۵�
        str='�i�h���_�I';
    elseif isnan(fx0_left) || isnan(fx0_right)  % �P�_�������Υk�����O�_�s�b
        str='�������_�I';
    else
        str='���D���_�I';
    end
else
    str='��Ʀb���I�s��.';
end
