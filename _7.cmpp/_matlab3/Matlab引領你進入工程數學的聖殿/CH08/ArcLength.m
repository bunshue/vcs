function L=ArcLength(varargin)
%ARCLENGTH   �p�⥭�����u������
% L=ARCLENGTH(FUNX,FUNY,T,ALPHA,BETA,'dicarl')  �p�⪽���y�Шt�U�ѰѼƤ�{��
%                                                        �Ҵy�z���������u������
% L=ARCLENGTH(FUN,T,ALPHA,BETA,'polar')  �p�ⷥ�y�Шt�U��FUN�Ҵy�z�����u������
%
% ��ɤJ�ѼƼơG
%     ---FUNX,FUNY�G�����y�Шt�U�������u���ѼƤ�{��
%     ---FUN�G�������u�����y�Ф�{��
%     ---ALPHA,BETA�G�n�����U���P�W��
%     ---TYPE�G�y�Шt���A�ATYPE���H�U��ب��ȡG
%               1.'dicarl'��'d'��1�G�����y�Шt
%               2.'polar'��'p'��2�G���y�Шt
% ��X�ѼơG
%     ---L�G�Ǧ^���������u������
%
% See also int

args=varargin;
type=args{end};
switch lower(type)
    case {1,'d','dicarl'}
        [funx,funy,t,alpha,beta]=deal(args{1:5});
    case {2,'p','polar'}
        [fun,t,alpha,beta]=deal(args{1:4});
        funx=fun*cos(t);
        funy=fun*sin(t);        
    otherwise
        error('Illegal options.')
end
dfx=diff(funx,t);
dfy=diff(funy,t);
L=simple(int(sqrt(dfx^2+dfy^2),t,alpha,beta));