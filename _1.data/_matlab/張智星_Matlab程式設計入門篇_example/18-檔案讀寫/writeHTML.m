filename = [tempname, '.html'];
fid = fopen(filename, 'w');
fprintf(fid, '<html><body>\n');
fprintf(fid, 'This is a test homepage written by MATLAB!\n');
fprintf(fid, '</body></html>');
fclose(fid);
dos(['start ', filename]);	% �ҰʩM .html �۳s�������ε{��