function varargout=reshapefile(file,n,extension,type)
%RESHAPEFILE   ���{�����U��[�J�Ǹ��β����{���U�檺�en�Ӧr��
% RESHAPEFILE(FILE,N)  ��FILE�ɮת��U��[�J�Ǹ����x�s��TXT�ɮ�
% RESHAPEFILE(FILE,N,EXT)�� RESHAPEFILE(FILE,N,EXT,1)��
% RESHAPEFILE(FILE,N,EXT,'add')  ��FILE�ɮת��U��[�J�Ǹ���
%                                �x�s�����ɦW��EXT�S���ɮ�
% RESHAPEFILE(FILE,N,EXT,2)��
% RESHAPEFILE(FILE,N,EXT,'delete')  ����FILE�ɮצU�檺�eN�Ӧr����
%                                   �x�s�����ɦW��EXT�S���ɮ�
% S=RESHAPEFILE(...)  �N��Ϋ᪺�ɮפ��e�ᵹS
%
% ��ɤJ�ѼƼơG
%     ---FILE�G���ɦW�A�����]�A���ɦW
%     ---N�G���w�Ǹ��ҥe����Ʃλݭn�����r�����Ӽ�
%     ---EXT�G�s�ɮת����ɦW
%     ---TYPE�G���w�O���ɮפ��e�U��[�J�Ǹ��٬O�����ɮצU��e�����r���A
%              TYPE���H�U��ب��ȡG
%              1.1��'add'�G���ɮצU��[�J�Ǹ�
%              2.2��'delete'�G�����ɮצU��e��N�Ӧr��
% ��X�ѼơG
%     ---S�G�s�ɮת����e
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