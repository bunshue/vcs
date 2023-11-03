function varargout=Rolle(fun,range)
%ROLLE   ���Ҩ�Ʀb�Y�Ӱ϶��W�O�_����ù���w�z
% ROLLE(FUN,RANGE)  �H�ϧΪ��Ҧ��ܽd��Ʀb�Y�Ӱ϶��W��ù���w�z
% TF=ROLLE(FUN,RANGE)  �H�ϧΪ��Ҧ��ܽd��Ʀb�Y�Ӱ϶��˪�ù���w�z�A
%                          �öǦ^����ƬO�_����ù���w�z���q�ATF=1�����FTF=0������
% [TF,XI]=ROLLE(FUN,RANGE)  �Ǧ^����Ʀb���w�϶��W�O�_����ù���w�z���qTF�M�@��ù���I
%
% ��ɤJ�ѼƼơG
%     ---FUN�G��ƪ�MATLAB�y�z�A�i�H�O�ΦW��ơB���p��ƩMM�ɮ�
%     ---RANGE�G�S���϶�
% ��X�ѼơG
%     ---TF�G���O�_����ù���w�z���q
%     ---XI�Gù���I
%
% See also fzero

fab=subs(fun,range);
tf=0;
if fab(1)~=fab(2)
    disp('���fun�b�϶�range�W������ù���w�z.')
    return
else
    tf=1;
end
df=diff(fun);
while 1
    xi=fzero(inline(df),rand);
    if prod(xi-range)<=0
        break
    end
end
if nargout==2 && tf==1
    varargout{1}=tf;
    varargout{2}=xi;
else
    varargout{1}=tf;
    ezplot(fun,range)
    hold on
    plot([xi-diff(range)/10,xi+diff(range)/10],[0,0],'k--')
    title(['\xi=',num2str(xi)])
end
