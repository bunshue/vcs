function total = myFun(varargin)
total=0;
for i=1:length(varargin)
	disp(sprintf('Input %d is "%s".', i, inputname(i)));
	total=total+varargin{i};
end	