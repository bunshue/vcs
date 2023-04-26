
filename = 'mono.wav';
[y, fs] = audioread(filename);

figure(1)
%sound(y, fs); % ���񦹭��T, fs: sample rate = 11025
time = (1:length(y))/fs; % �ɶ��b���V�q
plot(time, y); % �e�X�ɶ��b�W���i��

info=audioinfo(filename);
fprintf('�ɮצW�� = %s\n', info.Filename);
fprintf('���Y�覡 = %s\n', info.CompressionMethod);
fprintf('�q�D�Ӽ� = %g ��\n', info.NumChannels);
fprintf('�����W�v = %g Hz\n', info.SampleRate);
fprintf('�����I�`�Ӽ� = %g ��\n', info.TotalSamples);
fprintf('���T���� = %g ��\n', info.Duration);
fprintf('�����I�ѪR�� = %g �줸/�����I\n', info.BitsPerSample);


figure(2)
filename = 'stereo.wav';
[y, fs]=audioread(filename); % Ū�����T��
%sound(y, fs); % ���񭵰T
left=y(:,1); % ���n�D���T
right=y(:,2); % �k�n�D���T
time = (1:length(y))/fs; % �ɶ��b���V�q
subplot(3,1,1)
plot(time, y); % ���k�n�D�e�@�_
subplot(3,1,2)
plot((1:length(left))/fs, left);	% �e���n�D
subplot(3,1,3)
plot((1:length(right))/fs, right);	% �e�k�n�D


%Ū�X�����ɮ�
figure(3)
filename = 'original_speech.wav';
[y, fs] = audioread(filename, [4001 50000]); % Ū�����T�ɲ�4001��50000�I
plot(y)

%Ū�X�����ɮ�, �[�J'native'Ū�X�����T�N�|�O�H����ɮפ�����ƫ��A����
figure(4)
filename = 'original_speech.wav';
[y, fs] = audioread(filename, [4001 50000], 'native');
plot(y)

