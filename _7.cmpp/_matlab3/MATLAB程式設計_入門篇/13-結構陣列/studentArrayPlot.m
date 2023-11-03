
studentArrayCreate;
allName={student.name};
allScore=[student.score];

subplot(2,1,1);
plot(allScore, 'o-');
legend(allName);
xlabel('Exam'); ylabel('Score'); title('Scores of each student');
grid on;

subplot(2,1,2);
plot(allScore', 'o-');
legend({'Exam 1', 'Exam 2', 'Exam 3', 'Exam 4', 'Exam 5', 'Exam 6'});
xlabel('Student'); ylabel('Score'); title('Scores of each exam');
grid on;