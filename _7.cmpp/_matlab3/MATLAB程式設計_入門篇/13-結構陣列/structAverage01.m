clear student		% 清除 student 變數
student(1) = struct('name', 'Banny', 'scores', [85,80,92,78]);
student(2) = struct('name', 'Joey', 'scores', [80,85,90,88]);
student(3) = struct('name', 'Betty', 'scores', [88,82,90,80]);
scoreMat = cat(1, student.scores);		% 1 代表上下並排以改變橫列的維度
average1=mean(scoreMat);
fprintf('四次小考的全班平均：'); disp(average1);
average2=mean(scoreMat');
fprintf('三位學生的小考平均：'); disp(average2);
