function result=diff_para(y,x,t,n)
%DIFF_PARA   �ѼƤ�{���D��
% R=DIFF_PARA(Y,X)��R=DIFF_PARA(Y,X,[])  ��Ÿ���F��X�u�t���@�ӲŸ��ܼƮɡA
%                                                �D��X�MY�M�w���ѼƤ�{�����ɼ�dY/dX
% R=DIFF_PARA(Y,X,T)  �D��X�MY�M�w���ѼƤ�{��������ܼ�T���ɼ�dY/dX
% R=DIFF_PARA(Y,X,T,N)  �D��X�MY�M�w���ѼƤ�{��������ܼ�T��N���ɼ�dNY/dXN
%
% ��ɤJ�ѼƼơG
%     ---Y,X�G�ѼƤ�{�����Ÿ���F��
%     ---T�G�ѼƤ�{�����Ÿ����ܼ�
%     ---N�G�D�ɶ���
% ��X�ѼơG
%     ---R�G�ѼƤ�{���D�ɵ��G
%
% See also diff

if nargin<4
    n=1;
end
if nargin==2 || isempty(t)
    t=symvar(x);
    if length(t)>1
        error('The Symbolic variable not point out.')
    end
end
if n==1
    result=diff(y,t)/diff(x,t);
else
    result=diff(diff_para(y,x,t,n-1),t)/diff(x,t);
end
