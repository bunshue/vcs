clear student		% 清除 student 變數
student(1) = struct('name', 'Banny', 'scores', [85,80,92,78]);
student(2) = struct('name', 'Joey', 'scores', [80,85,90,88]);
student(3) = struct('name', 'Betty', 'scores', [88,82,90,80]);
student(2).name='Alex';		% 改變第二位學生的姓名
disp(student(2));			% 顯示第二位學生的資料
student(3).scores(2)=100;	% 改變第三位學生的第二次小考成績
disp(student(3));			% 顯示第三位學生的資料
