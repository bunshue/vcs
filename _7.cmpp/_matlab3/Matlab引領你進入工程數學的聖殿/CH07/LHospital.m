function varargout=LHospital(num,den,x,a)
%LHOSPITAL   �����F�k�h�D����
% L=LHOSPITAL(NUM,DEN)��L=LHOSPITAL(NUM,DEN,[])  �����F�k�h�p��NUM/DEN�b0�B������
% L=LHOSPITAL(NUM,DEN,X)  �����F�k�h�p��NUM/DEN����X=0�B������
% L=LHOSPITAL(NUM,DEN,X,A)  �����F�k�h�p��NUM/DEN����X=A�B������
% [L,FORM]=LHOSPITAL(...)  �����F�k�h�p��NUM/DEN�������öǦ^������L�M���w�����AFORM
% [L,FORM,K]=LHOSPITAL(...)  �����F�k�h�p��NUM/DEN�������öǦ^������L�B
%                                 ���w�����AFORM�M�����F�k�h�ϥΦ���K
%
% ��ɤJ�ѼƼơG
%     ---NUM,DEN�G�����������l�M������F��
%     ---X�G�Ÿ����ܼ�
%     ---A�G�����I
% ��X�ѼơG
%     ---L�G������
%     ---FORM�G���w�����A�A���t'��/��'�M'0/0'
%     ---K�G�����F�k�h�ϥΦ���
%
% See also diff, subs

if nargin<4
    a=0;
end
if nargin<3 || isempty(x)
    x=unique([symvar(num),symvar(den)]);
    if length(x)>1
        error('The Symbolic variable not point out.')
    end
end
fa=subs(num,x,a);
Fa=subs(den,x,a);
if isinf(fa) && isinf(Fa)
    form='��/��';
elseif fa==0 && Fa==0
    form='0/0';
else
    error('���w�����������T.')
end
k=1;
while 1
    num=diff(num);
    den=diff(den);
    fa=subs(num,x,a);
    Fa=subs(den,x,a);
    switch form
        case '��/��'
            if isinf(Fa) && ~isinf(fa)
                L=0;
                break
            end
            if ~isinf(Fa)
                L=subs(num/den,x,sym(a));
                break
            end
        case '0/0'
            if Fa==0 && fa~=0
                L=inf;
                break
            end
            if Fa~=0
                L=subs(num/den,x,sym(a));
                break
            end
    end
    k=k+1;
end
if nargout==1
    varargout{1}=L;
elseif nargout==2
    varargout{1}=L;
    varargout{2}=form;
elseif nargout==3
    varargout{1}=L;
    varargout{2}=form;
    varargout{3}=k;
else
    error('Wrong number of output arguments.')
end
