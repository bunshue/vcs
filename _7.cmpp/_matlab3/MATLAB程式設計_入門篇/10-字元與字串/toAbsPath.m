function output=toAbsPath(pathStr)
% toAbsPath: Convert a path string to an absolute path
%	Usage: output=toAbsPath(pathStr)
%
%	For example:
%		absPath=toAbsPath('myWork\code')

%	Roger Jang, 20080606

output=pathStr;
if ~isAbsPath(pathStr)
	output=[pwd, '\', pathStr];
end