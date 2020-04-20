function [output, output2]=showFcnVar(a, b, c);

if nargin<3, c=0; end
if nargin<2, b=0; end
if nargin<1, a=0; end

output=a+b+c;
if nargout>1
	output2=a*b*c;
end

fprintf('nargin=%d\n', nargin);
fprintf('nargout=%d\n', nargout);
fprintf('mfilename=%s\n', mfilename);
for i=1:nargin
	fprintf('inputname(%d)=%s\n', i, inputname(i));
end