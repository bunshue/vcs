function out = capalize(in)
%capalize: Captalize each word of a given sentence
%	Usage: out = captalize(in)

%	Multiple spaces are reduced to a single space too.

%	Roger Jang 20000723

if nargin<1, selfdemo; return; end

if isempty(in),
	out = '';
	return;
end

i = 1;
[token, rem] = strtok(in);
while ~isempty(token)
	extracted{i} = token;
	i = i+1;
	[token, rem] = strtok(rem);
end

for i = 1:length(extracted),
	string = extracted{i};
	new_string = [upper(string(1)), string(2:end)];
	extracted{i} = new_string;
end

out = extracted{1};
for i = 2:length(extracted),
	out = [out, ' ', extracted{i}];
end

% ====== Self demo
function selfdemo
input = 'this is A test for Me too';
output = feval(mfilename, input);
fprintf('input = %s\n', input);
fprintf('output = %s\n', output);