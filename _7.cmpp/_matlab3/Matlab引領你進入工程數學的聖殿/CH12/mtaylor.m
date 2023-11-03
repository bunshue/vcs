function T=mtaylor(fun,x0,n)
%MTAYLOR   二元函數的泰勒展開式
% T=MTAYLOR(FUN)  求二元函數FUN在原點處的6階泰勒展開式
% T=MTAYLOR(FUN,X0)  求二元函數FUN在點X0處的6階泰勒展開式
% T=MTAYLOR(FUN,X0,N)  求二元函數FUN在點X0處的N階泰勒展開式
%
% 輸導入參數數：
%     ---FUN：指定的二元函數
%     ---X0：泰勒展開點，以元胞陣列陣列舉出，形如{'x=0','y=0'}
%     ---N：泰勒展開階次
% 輸出參數：
%     ---T：傳回的泰勒展開式
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