








----------------pppp perl test ST----------------

chomp()：由於使用者輸入數字之後需要按"Enter"鍵，因此變數 a、b、和 c 內的字串最後都有"跳行"的控制字元；因此我們需要使用 chomp() 把"跳行"的控制字元去除。
狀態 || 敘述：這個敘述的意思是"如果狀態為 false，則執行 || 後的敘述。"
die 的用法是將其後面的字串顯示出來之後，把程式結束掉。

找出最近5個svn check in檔案


Perl 教學網站：
一、http://web.nchu.edu.tw/~jlu/cyut/perl.shtml
二、http://www.sinica.edu.tw/~andyliu/tc/Perl/perl.html
三、http://linux.tnc.edu.tw/techdoc/perl_intro/
參考資料
網路

perl筆記
http://irw.ncut.edu.tw/peterju/perl.html

可否用perl分析一個log裏面的資料？

qq是什麼意思

perl software
http://www.perl.org/
http://www.perl.org/get.html
http://www.perl.org/get.html#win32

perl debug
perl -d test.pl
s: step
p: print  p $a
q: quit
h: help
perl之printf與C相同。
print
%4d  25 =>   25
%04d 25 => 0025


----------------pppp perl test SP----------------








# 啟動 big5 字串解析; 標準輸出入及標準錯誤都設為 big5 編碼
use encoding 'big5', STDIN => 'big5', STDOUT => 'big5';
print length("駱駝");            #  2 (雙引號表示字符)
print length('駱駝');            #  4 (單引號表示位元組)
print index("諄諄教誨", "彖帢"); # -1 (不包含此子字串)
print index('諄諄教誨', '彖帢'); #  1 (從第二個位元組開始)

https://tw.perlmaven.com/string-functions-length-lc-uc-index-substr
https://tw.perlmaven.com/the-default-variable-of-perl


Perl Maven

Perl 有一個怪異的 scalar 變數叫作 $_，它叫作"預設變數"或是"topic"。

在 Perl中有許多函式和操作子使用這個變數當作預設變數，比如在沒有明顯參數的時候。一般而言，你應該不會 在真實的程式碼中看到$_。也就是說你不用把 $_ 明確的寫在程式中。

就是說，這樣就誠如你所想做的。 


lc	轉換原字串為小寫
uc	轉換原字串為大寫
length	計算字串裡的字符個數
index 函式，傳入兩個字串後，傳回第二字串位於第一字串內的位置。 


chomp	去除字串的換行符號



因perl可不需宣告變數,故要強迫宣告use strict;然後以my();將變數置於其中
 
 
use strict;
use warnings;
use 5.010;

my $str = 'HeLlo';

say lc $str;      # hello
say uc $str;      # HELLO
say length $str;  # 5

say()， 類似 print()，如果不給予參數的話，會印出 $_的內容。 


Perl 的內建序式 sort 可以直接排序陣列，這不另人意外。而其最簡明的使用形式，便是傳入一個陣列，它好會傳回排好的新陣列：@sorted = sort @original。




