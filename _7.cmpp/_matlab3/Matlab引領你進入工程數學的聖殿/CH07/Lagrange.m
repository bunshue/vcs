function xi=Lagrange(fun,range)
%LAGRANGE   ���Ҩ�Ʀb�Y�Ӱ϶��W�O�_�����Ԯ�Ԥ餤�ȩw�z
% LAGRANGE(FUN,RANGE)  �H�ϧΪ��Ҧ��ܽd��Ʀb�Y�Ӱ϶��W���Ԯ�Ԥ餤�ȩw�z
% XI=LAGRANGE(FUN,RANGE)  �Ǧ^��Ʀb���w�϶��W���@�өԮ�Ԥ餤���I
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ�MATLAB�y�z�A�i�H�O�ΦW��ơB���p��ƩMM�ɮ�
%     ---RANGE�G�S���϶�
% ��X�ѼơG
%     ---XI�G�Ԯ�Ԥ餤���I
%
% Sea also Rolle

fab=subs(fun,range);
df=diff(fun);
while 1
    x=fzero(inline(df-diff(fab)/diff(range)),rand);
    if prod(x-range)<=0
        break
    end
end
if nargout==1
    xi=x;
else
    ezplot(fun,range)
    hold on
    x_range=[x-diff(range)/10,x+diff(range)/10];
    y_range=diff(fab)/diff(range)*(x_range-x)+subs(fun,x);
    plot(x_range,y_range,'k--')
    title(['\xi=',num2str(x)])
end
