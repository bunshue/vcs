function varargout=reshapefile(file,n,extension,type)
%RESHAPEFILE   為程式的各行加入序號或移除程式各行的前n個字元
% RESHAPEFILE(FILE,N)  為FILE檔案的各行加入序號並儲存為TXT檔案
% RESHAPEFILE(FILE,N,EXT)或 RESHAPEFILE(FILE,N,EXT,1)或
% RESHAPEFILE(FILE,N,EXT,'add')  為FILE檔案的各行加入序號並
%                                儲存為副檔名由EXT特殊的檔案
% RESHAPEFILE(FILE,N,EXT,2)或
% RESHAPEFILE(FILE,N,EXT,'delete')  移除FILE檔案各行的前N個字元並
%                                   儲存為副檔名由EXT特殊的檔案
% S=RESHAPEFILE(...)  將整形後的檔案內容賦給S
%
% 輸導入參數數：
%     ---FILE：原檔名，必須包括副檔名
%     ---N：指定序號所占的位數或需要移除字元的個數
%     ---EXT：新檔案的副檔名
%     ---TYPE：指定是為檔案內容各行加入序號還是移除檔案各行前面的字元，
%              TYPE有以下兩種取值：
%              1.1或'add'：為檔案各行加入序號
%              2.2或'delete'：移除檔案各行前面N個字元
% 輸出參數：
%     ---S：新檔案的內容
%
% See also importdata, fprintf

if nargin<4
    type='add';
end
if nargin<3
    extension='.txt';
end
if ~(isnumeric(n) && isscalar(n))
    error('n must be a scalar numeric.')
end
fid=fopen(file);
tline = fgetl(fid);
count=1;
while ischar(tline)
    S{count}=tline;
    tline = fgetl(fid);
    count=count+1;
end
fclose(fid);
N=length(S);
T=cell(1,N);
for k=1:N
    n=ceil(abs(n));
    L=S{k};
    if any(strcmpi(num2str(type),{'1','add'}))
        L=[sprintf(['%0',num2str(n),'d.',blanks(1)],k),L];
    elseif any(strcmpi(num2str(type),{'2','delete'}))
        if n>length(L)
            n=length(L);
        end
        L(1:n)=[];
    end
    T{k}=L;
end
str=char(T);
if nargout==0
    [~,name]=fileparts(file);
    fid=fopen([name,extension],'wt');
    format=[repmat('%c',1,size(str,2)),'\n'];
    fprintf(fid,format,str');
    fclose(fid);
elseif nargout==1
    varargout{1}=str;
else
    error('Illegal number of output arguments.')
end