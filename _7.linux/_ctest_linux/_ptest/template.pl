#! /usr/bin/perl
print "\ndavid: This is a perl template.\n\n";
@array1=(1..12);
print "Array1:\t";
print @array1;
print "\n";

foreach (@ARGV) {
	print "引數 ===> $_\n";
}

$num=$#ARGV + 1;

print "\n程式名稱為：$0\n";
print "\n共有 $num 個引數, 分別為:\n";

for($i = 0; $i < ($#ARGV+1); $i++)
{
	print $ARGV[$i] . "\n";
}


