function xi=IntermediateTheorem(fun,range,C)
%INTERMEDIATETHEOREM   ���ҳs���ƪ����ȩw�z
% IntermediateTheorem(FUN,RANGE,C)  �H�ϧΪ��Φ����ҳs���Ʀb���϶��W�����ȩw�z
% XI=IntermediateTheorem(FUN,RANGE,C)  �Ǧ^�s���ƪ��@�Ӥ����I�A����ø��ϧ�
%
% ��ɤJ�ѼƼơG
%     ---FUN�G�s���ƪ���F��
%     ---RANGE�G�S���϶�[a,b]
%     ---C�G����FUN(a)�PFUN(b)�����N���
% ��X�ѼơG
%     ---XI�GXI����FUN(XI)=C�A�Y�����w��X�h�H�ϧμҦ�����
%
% See also fzero

if nargin==2
    C=0;
end
fab=feval(fun,range);
if prod(fab-C)<=0  % �P�_C�O�_�ݩ�f(a)�Mf(b)����
    if fab(1)==0
        x0=range(1);
    elseif fab(2)==0
        x0=range(2);
    else
        x0=fzero(@(x)fun(x)-C,range);
    end
else
    return
end
if nargout==1  % �P�_��X�ѼƭӼ�
    xi=x0;
else
    fplot(fun,range)
    hold on
    plot(xlim,[C,C],'k--')
    plot(x0,fun(x0),'k*')
    title(['\xi=',num2str(x0)])
end
