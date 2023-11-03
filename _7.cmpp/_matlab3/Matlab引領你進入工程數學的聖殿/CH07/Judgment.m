function s=Judgment(f,str)
%JUDGMENT   判斷函數的單調性或凹凸性
% S=JUDGMENT(F,STR)
%
% 輸導入參數數：
%     ---F：實數
%     ---STR：性質型態字串元胞陣列
% 輸出參數：
%     ---S：傳回的性質型態字串
%
% See also iscellstr, cellstr

if ~iscellstr(str) || numel(str)~=2
    error('Input argument str is Illegal.')
end
if f<0
    s=str{1};
else
    s=str{2};
end