karDir='D:\dataSet\liu3000';
songObj=recursiveFileList(karDir, 'kar');

for i=1:length(songObj)
	songObj(i).name=songObj(i).name(1:end-4);
	songObj(i).artist=songObj(i).parentDir;
	songObj(i).path=strrep(songObj(i).path, '\', '/');
	items=split(songObj(i).path, '/');
	songObj(i).language=items{end-2};
end
songObj=rmfield(songObj, 'date');
songObj=rmfield(songObj, 'bytes');
songObj=rmfield(songObj, 'isdir');
songObj=rmfield(songObj, 'datenum');
songObj=rmfield(songObj, 'path');
songObj=rmfield(songObj, 'parentDir');
save songObj songObj

% Get rid of "unknown" artist
songObj(find(strcmp('¤£¸Ô', {songObj.artist})))=[];
songObj(find(strcmp('unknown', {songObj.artist})))=[];
songObj(find(strcmp('¦Ñºq', {songObj.artist})))=[];
% Find the most productive artist
allArtist={songObj.artist};
uniqArtist=unique(allArtist);
for i=1:length(uniqArtist)
	artistObj(i).name=uniqArtist{i};
	artistObj(i).index=find(strcmp(allArtist, uniqArtist{i}));
	artistObj(i).count=length(artistObj(i).index);
end
[junk, index]=sort([artistObj.count], 'descend');
artistObj=artistObj(index);
n=10;
for i=1:n
	fprintf('%d/%d: artist=%s, count=%d\n', i, n, artistObj(i).name, artistObj(i).count);
end
% Find the count for each language
allLanguage={songObj.language};
uniqLanguage=unique(allLanguage);
for i=1:length(uniqLanguage)
	languageObj(i).language=uniqLanguage{i};
	languageObj(i).index=find(strcmp(allLanguage, uniqLanguage{i}));
	languageObj(i).count=length(languageObj(i).index);
end
for i=1:length(languageObj)
		fprintf('%d/%d: language=%s, count=%d\n', i, length(languageObj), languageObj(i).language, languageObj(i).count);
end