A{1,1} = 'this is the first cell.';
A{1,2} = [5+j*6, 4+j*5];
A{2,1} = [1 2 3; 4 5 6; 7 8 9];
A{2,2} = {'Tim'; 'Chris'};
celldisp(A)			% 顯示異質陣列 A 各個構成元素的實際內容