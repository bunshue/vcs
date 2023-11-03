function [x,e]=LinearEqs(A,b)
%LINEAREQS   �u�ʤ�{���s�ժ��D��
% X=LINEAREQS(A,B)  �Q��MATLAB���a��ƨD�u�ʤ�{���s��AX=B����X
% [X,E]=LINEAREQS(A,B)  �D�u�ʤ�{���s�ժ���X�öǦ^��~�t
%
% ��ɤJ�ѼƼơG
%     ---A�G��{���s�ժ��t�Ưx�}
%     ---B�G��{���s�ժ��k�ݦV�q
% ��X�ѼơG
%     ---X�G��{���s�ժ���
%     ---E�G�Ѫ��~�t
%
% See also null, inv(\), pinv

[m,n]=size(A);b=b(:);
if m~=length(b);
    error('�t�Ưx�}A�M�k�ݦV�qb���Ƥ��ŦX.')
end
r1=rank(A);r2=rank([A b]);
if ~all(b)  % �����u�ʤ�{���s��
    if r1==n
        x=zeros(size(b));
    else
        z=null(sym(A));   %�ѥX�W�d�ƪ��ƹs�Ŷ�
        k=sym('k%d',[n-r1,1]);   %�w�q�U��¦�Ѩt�������t��
        x=z*k;   %���{�����q��
    end
else  % �D�����u�ʤ�{���s��
    if r1==r2&&r1==n
        disp('��{���s�լO��w���A���ߤ@�ѡI')
        x=A\b;
    elseif r1==r2&&r1~=n
        disp('��{���s�լO��w���A���L�a�ѡI')
        warning off all
        z=null(sym(A));   %�ѥX�W�d�ƪ��ƹs�Ŷ�
        x0=sym(A)\b;  %�D�X�@�ӯS��
        k=sym('k%d',[n-r1,1]);   %�w�q�U��¦�Ѩt�������t��
        x=x0+z*k;   %���{�����q��
    else
        disp('��{���s�լO�W�w���A�u���̤p�G���N�q�U���ѡI')
        x=pinv(A)*b;
    end
end
e=norm(double(A*x-b));