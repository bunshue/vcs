function T=mtaylor(fun,x0,n)
%MTAYLOR   �G����ƪ����Ǯi�}��
% T=MTAYLOR(FUN)  �D�G�����FUN�b���I�B��6�����Ǯi�}��
% T=MTAYLOR(FUN,X0)  �D�G�����FUN�b�IX0�B��6�����Ǯi�}��
% T=MTAYLOR(FUN,X0,N)  �D�G�����FUN�b�IX0�B��N�����Ǯi�}��
%
% ��ɤJ�ѼƼơG
%     ---FUN�G���w���G�����
%     ---X0�G���Ǯi�}�I�A�H���M�}�C�}�C�|�X�A�Φp{'x=0','y=0'}
%     ---N�G���Ǯi�}����
% ��X�ѼơG
%     ---T�G�Ǧ^�����Ǯi�}��
%
% See also taylor, diff

if nargin<3
    n=6;
end
if nargin<2 || isempty(x0)
    x0={'x=0','y=0'};
end
vars=cell(1,2); values=cell(1,2);
for k=1:2
    kk=strfind(x0{k},'=');
    vars{k}=x0{k}(1:kk-1);
    values{k}=sym(x0{k}(kk+1:end));
end
T=subs(fun,vars,values);
for m=1:n
    S=0;
    for p=0:m
        sigma=nchoosek(m,p)*(sym(vars{1})-values{1})^p*...
            (sym(vars{2})-values{2})^(m-p)*...
            subs(diff(diff(fun,vars{1},p),vars{2},m-p),vars,values);
        S=S+sigma;
    end
    T=T+S/gamma(m+1);
end