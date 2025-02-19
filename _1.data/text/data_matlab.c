

Roger Jang (張智星)


MATLAB程式設計：入門篇
http://mirlab.org/jang/books/matlabProgramming4beginner/

MATLAB程式設計：進階篇
http://mirlab.org/jang/books/matlabProgramming4guru/



>> X = imread('picture1.jpg');
>> image(X)
>> size(X)
[m,n]=size(X)
class(X)

info = imfinfo('picture1.jpg')



>> [y,fs]=audioread('Dog.wav');
sound(y,fs);	%播放此音訊
time=(1:length(y))/fs;	%時間軸的向量
plot(time,y)	%畫出時間軸上的波形


>> 

 audioinfo('Dog.wav')




fileName='Dog.wav';
info=audioinfo(fileName);
fprintf('檔案名稱 = %s\n', info.Filename);
fprintf('壓縮方式 = %s\n', info.CompressionMethod);
fprintf('通道個數 = %g 個\n', info.NumChannels);
fprintf('取樣頻率 = %g Hz\n', info.SampleRate);
fprintf('取樣點總個數 = %g 個\n', info.TotalSamples);
fprintf('音訊長度 = %g 秒\n', info.Duration);
fprintf('取樣點解析度 = %g 位元/取樣點\n', info.BitsPerSample);



fileName='16.監獄風雲.mp3';
info=audioinfo(fileName);
disp(info);








%把檔案內的字，一行一行取出來。
fid=fopen('name.dat');
while feof(fid)==0
    line=fgetl(fid);
    disp(line);
end

file name.dat:
John
Mary
George
Dog



%做DCT
X=[158 158 158 159 153 154 158 154;157 156 160 157 155 152 157 153;153 154 155 151 151 156 155 159;153 157 159 150 160 158 156 150;
153 155 152 159 156 155 158 158;155 154 160 152 154 156 151 160;157 157 153 153 155 152 156 160;153 156 153 157 153 154 151 158]
Y=dct(X)


%畫圖測試
x=[-15:.1:15];
y=sin(x);
z=sign(y);
plot(x,z)
hold on,plot(x,y);
axis('equal');grid
hold off;




%3D plot test
clear,clc,clf
[x,y]=meshgrid(-2:.2:2);
z=sqrt(x.^2+y.^2);
subplot(221),mesh(x,y,z)
subplot(222),meshc(x,y,z)
subplot(223),meshz(x,y,z)
subplot(224),plot3(x,y,z)




%使用load讀取一個矩陣檔案。
load math_test_result.txt
x=math_test_result(:,1);
y=math_test_result(:,2);
plot(x,y);




matlab的格式化列印：
temp=123.456;
fprintf('The temperature is %8.5f 度\n',temp);

與C差在：1. 多了f，2.單引號。






matlab

函數分佈的快速繪圖

fplot的指令可以用來自動的畫一個已定義的函數分佈圖，而無須產生繪圖所須要的一組數據做為變數。

fplot的指令可以用來自動的畫一個已定義的函數分佈圖，而無須產生繪圖所須要的一組數據做為變數。其語法為fplot('fun',[xmin xmax ymin ymax])，其中 fun為一已定義的函數名稱，例如 sin, cos等等；而 xmin, xmax, ymin, ymax 則是設定繪圖橫軸及縱軸的下限及上限。以下的例子是將一函數 f(x)=sin(x)/x在-20≦x≦20,-0.4≦y≦1.2之間畫出：

>> fplot('sin(x)./x',[-20 20 -0.4 1.2])

>> title('Fplot of f(x)=sin(x)/x')

>> xlabel('x'), ylabel('f(x)')




>> title(['Poly. regression, deg=',int2str(n)])

>> xlabel('Time'), ylabel('Temp'), grid

>> pause % 每次要暫停看清楚圖再執行下一步驟

>> end

在上述的 title指令中我們示範了如何將一變數輸入（n代表多項式的階數），是利用int2str這個指令，它是用來將一整數(integer) 轉換成為一個字串 (string)，因為在title中只能以字串出現。此外在 title指令中尚須以 [ ] 將所有敘述包括在內。類似的指令尚有 num2str 它是用來將實數轉換成一字串。有關這幾個新介紹的詳細說明，請參考 title, int2str, num2str 的線上說明。




多項式的根

一個多項式視其階數而定，它的根可以有一個到數個，可能為實數也可能是複數。要求一高階多項式的根往往須借助數值方法，所幸MATLAB已將這些數值方法寫成一函數roots(p)，我們只要輸入多項式的各階係數（以 p 代表）即可求解到對應的根。

>> p=[1 3 2];

>> r=roots(p)


poly 函數就是在求出多項式的各階係數，其語法為 poly(r)，其中 r 是代表根的陣列。而 real 則是用來去除因計算時產生的假虛部係數，為何會有此種情形請參考以下的例子。

>> r=[-2 1];

>> pp=poly(r) % pp=(x+2)(x-1)=x^2+3x+2

pp =

1 3 2





數學式的化簡

以下的函數適用來簡化數學式，如展開、化簡或聚集數學式。相關的指令有：

collect(S) 聚集S的係數

collect(S,'v') 聚集S的係數，是以v為獨立變數

expand(S) 將S表示式展開

factor(S) 還原S的因式(factorization)

	simple(S) 如果可能的話，將S表示式再做簡化

	simplify(S) 利用Maple簡化法則化簡S表示式

	我們來看一些例子

	>> S1 = 'x^3-1';

	>> S2 = '(x-3)^2+(y-4)^2';

	>> S3 = 'sqrt(a^4*b^7)'

	>> S4 = '14*x^2/(22*x*y)';

	>> factor(S1)

	ans=

	(x-1)*(x^2+x+1)

	>> expand(S2)

	ans=

	x^2-6*x+25+y^2-8*y

	>>collect(S2)

	ans=

	x^2-6*x+9+(y-4)^2

	>>collect(S2,'y')

	ans=

	y^2-8*y+(x-3)62+16

	>>simplify(S3)

	ans=

	a^2*b^(7/2)

	>>simple(S4)

	ans=

	7/11*x/y









t=linspace(0,10,10);t=t';
w=5;
x=0.5+sin(w.*t)+sin(3*w.*t)/3+sin(5*w.*t)/5;
figure(1);plot(x);
x1=x+0.5*randn(size(t));
figure(2);plot(x1);
fx=fft(x);mfx=abs(fx);
fx1=fft(x1);mfx1=abs(fx1);
figure(3);plot(mfx);
figure(4);plot(mfx1);


clf;
w=5;
%t=linspace(-10,10,1024);t=t';
%t=linspace(10,10,1024);t=t';
%t=[linspace(0,0,200) linspace(1,1,200) linspace(0,0,200)];t=t';
t=linspace(-10,10,1024);t=t';

subplot(321);plot(t);
%x=0.5+sin(w.*t)+sin(3*w.*t)/3+sin(5*w.*t)/5;
x=sin(w.*t);
subplot(322);plot(t,x);

%x=sin(w.*t);
%x=[linspace(0,0,20) linspace(1,1,20)];x=x';
%x=linspace(-10,10,40);x=x';
%x=[linspace(0,0,20) linspace(1,1,20)];x=x';
x1=x+0.5*randn(size(t));
subplot(323);plot(x1);


fx=fft(x);mfx=abs(fx);
fx1=fft(x1);mfx1=abs(fx1);
subplot(325);plot(mfx);
subplot(326);plot(mfx1);





clf
b=[1 -1 0];
a=[1 -1.6 +0.85];
x=[1 zeros(1,99)];
y=filter(b,a,x);
plot(y,'o'),grid


clf
x=[4 3 7 -9 1 0 0]';
y=fft(x);
z=abs(y);
plot(z);

