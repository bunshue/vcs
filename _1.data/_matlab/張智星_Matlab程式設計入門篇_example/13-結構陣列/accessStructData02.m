clear student		% 清除 student 變數
student(1) = struct('name', 'Banny', 'scores', [85,80,92,78]);
student(2) = struct('name', 'Joey', 'scores', [80,85,90,88]);
student(3) = struct('name', 'Betty', 'scores', [88,82,90,80]);
fieldName='name';
for i=1:length(student)
	fprintf('%d: Value of %s is %s\n', i, fieldName, student(i).(fieldName));
end
