% 統計 n-gram (bigram, trigram 等）在一篇文章出現的次數

filename='tangPoem3223.txt';
string=fileread(filename);
string=string(string>255);

for n=2:5
	fprintf('Collect %g-grams...\n', n);
	ngram=str2ngram(string, n);

	fprintf('Sort %g %g-grams...\n', size(ngram,1), n);
	[uniqNgram, count] = countrows(ngram);

	fprintf('Display %d distinct n-grams according to counts...\n', size(uniqNgram,1));
	for i = 1:10
		fprintf('%d/%d: %s ===> %g\n', i, size(uniqNgram,1), uniqNgram(i, :), count(i));
	end
end