function out = ranking(x)
% ranking: Find the rank of each element in a vector
%	Usage: out = ranking(x)
%		x(i) is rank out(i) within the vector x

%	Roger Jang, 20030726

if nargin<1, selfdemo; return; end

[sorted, position]=sort(x, 'descend');	% 由大到小排列
n=length(x);
rank=1:n;
[junk, index]=sort(position);
out=rank(index);

% ====== Self demo
function selfdemo
x=[92, 95, 58, 75, 69, 82];
out=ranking(x);
fprintf('x=%s\n', mat2str(x));
fprintf('ranking(x)=%s\n', mat2str(out));