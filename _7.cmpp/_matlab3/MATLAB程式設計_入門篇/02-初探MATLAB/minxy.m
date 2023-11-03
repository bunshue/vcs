function [minValue, minIndex] = minxy(matrix)
%MINXY Minimum of a 2D matrix
%	Usage: [minValue, minIndex] = minxy(A)
%		minValue: the minimum of the matrix A
%		minIndex: the 2D index of minValue in A

%	Roger Jang, 20010219

[columnMin, columnMinIndex] = min(matrix);
[minValue, tmp] = min(columnMin);
minIndex = [columnMinIndex(tmp) tmp];
