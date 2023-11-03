function H=FrequencyTable(X)
%FREQUENCYTABLE   �έp�}�C�����X�{���W��
% H=FREQUENCYTABLE(X)  �έp�x�}X���U�����X�{���W��
%
% ��ɤJ�ѼƼơG
%     ---X�G���w���}�C�ίx�}
% ��X�ѼơG
%     ---H�G�Ǧ^���έp���G
%
% See also tabulate

if ~isa(X,'sym')
    H=tabulate(X);
    H=H(:,1:2);
else
    sortX=sort(X(:));
    D=[simple(sortX(2:end)-sortX(1:end-1));sym(1)];
    uniqueX=(D~=0);
    k=find([1;uniqueX]);
    H=[sortX(uniqueX) diff(k)];
end