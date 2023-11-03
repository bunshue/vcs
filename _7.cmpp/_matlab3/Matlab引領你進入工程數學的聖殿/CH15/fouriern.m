function varargout=fouriern(fun,oldvars,newvars,type,method)
%FOURIERN   多重傅裡葉變換的求解
% F2=FOURIERN(F1,OLDVARS,NEWVARS)  求函數F1的多重傅裡葉變換
% F2=FOURIERN(F1,OLDVARS,NEWVARS,TYPE)  求函數F1的傅裡葉變換或逆變換，
%                                       變換型態由TYPE指定
% F2=FOURIERN(F1,OLDVARS,NEWVARS,TYPE,METHOD)  指定采用fourier函數求變換還是
%                                              采用int函數求解
% [F2,S]=FOURIERN(...)  求多重傅裡葉變換並傳回變換型態
%
% 輸導入參數數：
%     ---F1：起始函數
%     ---OLDVARS：函數F1的變數
%     ---NEWVARS：變換後的變數
%     ---TYPE：指定變換型態，有'fourier'和'ifourier'兩種取值
%     ---METHOD：指定求解變換的方法，有'fourier'和'int'兩種方法
% 輸出參數：
%     ---F2：求變換後的函數
%     ---S：變換型態，對應於TYPE
%
% See also fourier, int

if nargin<5
    method='fourier';
end
if nargin<4 || isempty(type)
    type='fourier';
end
if ~isa(fun,'sym')
    error('FUN must be a Symbolic function.')
end
N=length(oldvars);
if length(newvars)~=N
    error('變數維數不一致.')
end
switch lower(method)
    case 'fourier'
        fcn=lower(type);
        for k=1:N
            fun=feval(fcn,fun,oldvars(k),newvars(k));
        end
    case 'int'
        if isequal(lower(type),'fourier')
            for k=1:N
                fun=int(fun*exp(-1j*oldvars(k)*newvars(k)),oldvars(k),-inf,inf);
            end
        elseif isequal(lower(type),'ifourier')
            for k=1:N
                fun=1/2/pi*int(fun*exp(1j*oldvars(k)*newvars(k)),...
                     oldvars(k),-inf,inf);
            end
        else
            error('Illegal TYPE.')
        end
    otherwise
        error('Illegal METHOD.')
end
if nargout==1
    varargout{1}=fun;
elseif nargout==2
    varargout{1}=fun;varargout{2}=[upper(type),'變換'];
end