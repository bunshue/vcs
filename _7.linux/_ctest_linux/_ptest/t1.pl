#!/usr/bin/perl
@group = 1..10;
for(@group) {
	print "$_";
	if(($_ > 5) && ($_ < 8))
	{
		print "\tgood\n";
	}
	else
	{
		print "\n";
	}
}


for($i = 0; $i < 10; $i++)
{
	print("i = $i\n");

}

$i = 0;
while ($i < 10)
{
	print("i = $i\t");
	print "group[$i] = $group[$i]\n";
	$i++;
}

#@array1=(1..12);
@array1=(A..Z);
print "Array1:\t";
print @array1;
print "\n";

# 啟動 big5 字串解析; 標準輸出入及標準錯誤都設為 big5 編碼
#use encoding 'big5', STDIN => 'big5', STDOUT => 'big5';
print length("駱駝");            #  2 (雙引號表示字符)
print length('駱駝');            #  4 (單引號表示位元組)
print index("諄諄教誨", "彖帢"); # -1 (不包含此子字串)
print index('諄諄教誨', '彖帢'); #  1 (從第二個位元組開始)





