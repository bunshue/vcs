function output=isAbsPath(pathStr)
% isAbsPath: Return 1 if the given path string is a absolute path
%	Usage output=isAbsPath(pathStr)

%	Roger Jang, 20080606

output=any(strcmp(pathStr(1), {'/', '\'}));

if length(pathStr)>3
	if strcmp(pathStr(2:3), ':/')
		output=1;
	elseif strcmp(pathStr(2:3), ':\')
		output=1;
	end
end