function [p,A,b,FitFun]=Least_square(x,y,phifun,wfun)
%LEAST_SQUARE   �̤p�G���k
% P=LEAST_SQUARE(X,Y,PHIFUN)  �Q�ΰ���PHIFUN�����X���X�MY
% P=LEAST_SQUARE(X,Y,PHIFUN,WFUN)  �Q�ΰ���PHIFUN�M�v���WFUN���X���X�MY
% [P,A,B]=LEAST_SQUARE(...)  �̤p�G���k���X��ƨöǦ^�k��{���s�ժ��t�Ưx�}�M�k�ݦV�q
% [P,A,B,FITFUN]=LEAST_SQUARE(...)  �̤p�G���k���X��ƨöǦ^���X��ƪ�F��
%
% ��ɤJ�ѼƼơG
%     ---X,Y�G������
%     ---PHIFUN�G���X���ơA�i�H�O�ΦW��ƩΤ��p���
%     ---WFUN�G�v���
% ��X�ѼơG
%     ---P�G�̤p�G�����X�t��
%     ---A�G�k��{���s�ժ��t�Ưx�}
%     ---B�G�k��{���s�ժ��k�ݦV�q
%     ---FITFUN�G���X��ƪ�F��
%
% See also polyfit, lsqcurvefit

x=x(:); y=y(:);
if length(x)~=length(y)
    error('�����ƪ��פ��@�P.')
end
if nargin<4
    wfun=ones(size(x));
end
func=char(phifun);
func=strrep(func,'ones(size(x))','1');
func=strrep(func,'.*','*');
func=strrep(func,'./','/');
func=strrep(func,'.^','^');
k=strfind(func,'[');
func=sym(func(k(1):end));
phifun=phifun(x);
n=size(phifun,2);
A=zeros(n);b=zeros(n,1);
for k=1:n
    for j=1:n
        A(k,j)=0;
        for i=1:length(x)
            A(k,j)=A(k,j)+wfun(i)*phifun(i,j)*phifun(i,k);
        end
    end
    for i=1:length(x)
        b(k)=b(k)+wfun(i)*y(i)*phifun(i,k);
    end
end
p=A\b;
FitFun=vpa(dot(p,func),4);