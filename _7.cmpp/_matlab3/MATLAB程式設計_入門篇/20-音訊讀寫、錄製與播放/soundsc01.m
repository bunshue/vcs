[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
playblocking(p);
soundsc(y, fs);