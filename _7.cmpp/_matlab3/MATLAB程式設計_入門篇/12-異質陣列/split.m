function tokenList = split(str, delimiter)
% split: Split a string based on a given delimiter
%	Usage:
%	tokenList = split(str, delimiter)
%	See also JOIN.

%	Roger Jang, 20010324

if nargin==0; selfdemo; return; end

tokenList = {};
remain = str;
i = 1;
while ~isempty(remain),
	[token, remain] = strtok(remain, delimiter);
	tokenList{i} = token;
	i = i+1;
end

function selfdemo
str='This-is-a-test';
tokenList=feval(mfilename, str, '-');
str
fprintf('After running "tokenList=split(str, ''-'')":\n');
tokenList