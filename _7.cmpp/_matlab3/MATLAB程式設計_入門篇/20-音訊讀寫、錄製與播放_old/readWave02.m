fileName='welcome.wav';
[y, fs, nbits]=wavread(fileName);
fprintf('���T�ɮ� "%s" ����T�G\n', fileName);
fprintf('���T���� = %g ��\n', length(y)/fs);
fprintf('�����W�v = %g �����I/��\n', fs);
fprintf('�ѪR�� = %g �줸/�����I\n', nbits);