%算房貸
year_rate = 0.015;
month_rate = year_rate / 12;
r = 1 + month_rate;
year = 30;
AA = 1200;
M = 4;
for i = 1:1:12*year
    AA = (AA) * r - M;
    X = ['第', num2str(i),'個月, 本利和 ', num2str(AA), '   共付 ', num2str(i*M)];
    disp(X)
end
    