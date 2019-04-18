#!/usr/bin/perl


use strict;
use warnings;
use 5.010;

my $str = 'HeLlo';

say lc $str;      # hello
say uc $str;      # HELLO
say length $str;  # 5


my $name;
my $len1;
my $len2;

#print "What's your name?\n";
#$name = <STDIN>;
#$len1 = length($name);
#chomp($name);
#$len2 = length($name);
#print "Hello, $name, nice to meet you.\n";
#print "len1 = " .$len1.", len2 = ".$len2."\n";

my @ss;
@ss=("A".."G");
print @ss;
lc(@ss);
print @ss;

print "\n";

my $sss = "AaBbCcDdEeFf";
say "1 ".$sss;
say "2 say lc ".lc($sss);
say "3 say uc ".uc($sss);
$sss = lc($sss);
say "4 ".$sss;
$sss = uc($sss);
say "5 ".$sss;


#print 'donea';
#print "doneb";
#say 'donec';
#say "doned";
