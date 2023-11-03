function ngram = str2ngram(str, n)
% str2ngram: Extract n-gram from a given string or cell string
%	Usage: ngram = str2ngram(str, n)
%		str: a single string or a cell string

%	Roger Jang, 20030517

if nargin<1; selfdemo; return; end
if nargin<2; n=2; end

if isstr(str)
	ngram=char(buffer2(str, n, n-1)');
end

if iscell(str)
	ngram=[];
	for i=1:length(str)
		ngram=[ngram; str2ngram(str{i}, n)];
	end
end

% ====== Sub-function
function out = buffer2(y, frameSize, overlap)
% BUFFER2 Frame blocking
%	This is almost the same as "buffer" except that there is no leading zeros

%	Roger Jang, 20010908

y = y(:);
step = frameSize-overlap;
frameCount = floor((length(y)-overlap)/step);

out = zeros(frameSize, frameCount);
for i=1:frameCount,
	startIndex = (i-1)*step+1;
	out(:, i) = y(startIndex:(startIndex+frameSize-1));
end

% ====== Self demo
function selfdemo
str = {'網路上的芳鄰', '清華大學ABCD'};
for i=1:length(str)
	fprintf('str{%d}=%s\n', i, str{i});
end
trigram = feval(mfilename, str, 3);
fprintf('Trigram of the above string is: \n');
disp(trigram);