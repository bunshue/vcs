%��жU
year_rate = 0.015;
month_rate = year_rate / 12;
r = 1 + month_rate;
year = 30;
AA = 1200;
M = 4;
for i = 1:1:12*year
    AA = (AA) * r - M;
    X = ['��', num2str(i),'�Ӥ�, ���Q�M ', num2str(AA), '   �@�I ', num2str(i*M)];
    disp(X)
end
    