function h=projection(F,G,limit,type)
%PROJECTION   ø��Ŷ����u�b�y�Э��W����v
% PROJECTION(F,G)  ø���F�MG����u�bxOy���Wx��[-2*pi,2*pi]����v
% PROJECTION(F,G,LIMIT)  ø���F�MG����u�bxOy���Wx��LIMIT����v
% PROJECTION(F,G,LIMIT,TYPE)  ø���F�MG����u�b���w�y�Э��W����v
% H=PROJECTION(...)  ø��Ŷ����u�b�����W����v�öǦ^�䱱��X
%
% ��ɤJ�ѼƼơG
%     ---F,G�G��Ӭۥ檺������{��
%     ---LIMIT�G���ܼƽd��
%     ---TYPE�G���w�y�Э������A
% ��X�ѼơG
%     ---H�G��v�ϧΪ�����X
%
% See also ezplot

if nargin<4
    type='z';
end
if nargin<3
    limit=[-2*pi,2*pi];
end
s=unique([symvar(F),symvar(G)]);
if ~ismember(type,s)
    error('Illegal options.')
end
x=solve(F,type);
G=subs(G,type,x(1));
hp=ezplot(G,limit);
if nargout>0
    h=hp;
end