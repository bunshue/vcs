function tf=FunContinuity(x0,fun_left,fun_x0,fun_right)
%FUNCONTINUITY   �P�_��Ʀb�Y�I�B���s���
% TF=FUNCONTINUITY(X0,FUN_LEFT,FUN_X0,FUN_RIGHT)  �P�_���q���FUN�b�IX0�B���s��ʡA
%               �Y�s��h�Ǧ^TF=1�F�_�h�Ǧ^TF=0�AFUN�Ѩ䥪�k��F���H�Φb�IX0�B����F�����
%
% ��ɤJ�ѼƼơG
%     ---X0�G�S���I
%     ---FUN_LEFT�GX<X0�ɪ���ƪ�F��
%     ---FUN_X0�GX=X0�ɪ���ƪ�F��
%     ---FUN_RIGHT�GX>X0�ɪ���ƪ�F��
% ��X�ѼơG
%     ---TF�G��ƪ��s��ʡA�Y��ƦbX0�B�s��A�hTF=1�F�_�hTF=0
%
% See also limit

fx0=subs(fun_x0,'x',x0);
fx0_left=limit(fun_left,'x',x0,'left');
fx0_right=limit(fun_right,'x',x0,'right');
if isequal(fx0,fx0_left) && isequal(fx0,fx0_right)
    tf=1;
else
    tf=0;
end
