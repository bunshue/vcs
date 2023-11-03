textFile='tangPoem3223.txt';
lines=textread(textFile, '%s', 'delimiter', '\n');
lineNum=length(lines);
% ====== Add S & E
for i=1:lineNum
	lines{i}=['S', lines{i}, 'E'];
end
bigrams=str2ngram(lines, 2);
[uniqBigram, bigramCount] = rowCount(bigrams);
biNum=length(bigramCount);
for i=1:biNum
	bigram(i).token=uniqBigram(i,:);
	bigram(i).count=bigramCount(i);
end
[sorted, index]=sort([bigram.count], 'descend');
bigram=bigram(index);

for i=1:biNum
	if bigram(i).token(1)=='S'
		start=bigram(i).token(2);
		break;
	end
end

start='¶À';
wordNum=9;
for i=1:wordNum
	if i<wordNum
		for j=1:biNum
			if bigram(j).token(1)==start && bigram(j).token(2)~='E'
				break;
			end
		end
	else
		for j=1:biNum
			if bigram(j).token(1)==start && bigram(j).token(2)=='E'
				break;
			end
		end
	end
	start=bigram(j).token(2);
	fprintf('i=%d, bigram(%d).token=%s, bigram(%d).count=%d\n', i, j, bigram(j).token, j, bigram(j).count);
end