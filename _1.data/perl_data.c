








----------------pppp perl test ST----------------

chomp()�G�ѩ�ϥΪ̿�J�Ʀr����ݭn��"Enter"��A�]���ܼ� a�Bb�B�M c �����r��᳣̫��"����"������r���F�]���ڭ̻ݭn�ϥ� chomp() ��"����"������r���h���C
���A || �ԭz�G�o�ӱԭz���N��O"�p�G���A�� false�A�h���� || �᪺�ԭz�C"
die ���Ϊk�O�N��᭱���r����ܥX�Ӥ���A��{���������C

��X�̪�5��svn check in�ɮ�


Perl �оǺ����G
�@�Bhttp://web.nchu.edu.tw/~jlu/cyut/perl.shtml
�G�Bhttp://www.sinica.edu.tw/~andyliu/tc/Perl/perl.html
�T�Bhttp://linux.tnc.edu.tw/techdoc/perl_intro/
�ѦҸ��
����

perl���O
http://irw.ncut.edu.tw/peterju/perl.html

�i�_��perl���R�@��log�ح�����ơH

qq�O����N��

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
perl��printf�PC�ۦP�C
print
%4d  25 =>   25
%04d 25 => 0025


----------------pppp perl test SP----------------








# �Ұ� big5 �r��ѪR; �зǿ�X�J�μзǿ��~���]�� big5 �s�X
use encoding 'big5', STDIN => 'big5', STDOUT => 'big5';
print length("�d�m");            #  2 (���޸���ܦr��)
print length('�d�m');            #  4 (��޸���ܦ줸��)
print index("�ναл�", "να"); # -1 (���]�t���l�r��)
print index('�ναл�', 'να'); #  1 (�q�ĤG�Ӧ줸�ն}�l)

https://tw.perlmaven.com/string-functions-length-lc-uc-index-substr
https://tw.perlmaven.com/the-default-variable-of-perl


Perl Maven

Perl ���@�өǲ��� scalar �ܼƥs�@ $_�A���s�@"�w�]�ܼ�"�άO"topic"�C

�b Perl�����\�h�禡�M�ާ@�l�ϥγo���ܼƷ�@�w�]�ܼơA��p�b�S������Ѽƪ��ɭԡC�@��Ө��A�A���Ӥ��| �b�u�ꪺ�{���X���ݨ�$_�C�]�N�O���A���Χ� $_ ���T���g�b�{�����C

�N�O���A�o�˴N�ۦp�A�ҷQ�����C 


lc	�ഫ��r�ꬰ�p�g
uc	�ഫ��r�ꬰ�j�g
length	�p��r��̪��r�ŭӼ�
index �禡�A�ǤJ��Ӧr���A�Ǧ^�ĤG�r����Ĥ@�r�ꤺ����m�C 


chomp	�h���r�ꪺ����Ÿ�



�]perl�i���ݫŧi�ܼ�,�G�n�j���ŧiuse strict;�M��Hmy();�N�ܼƸm��䤤
 
 
use strict;
use warnings;
use 5.010;

my $str = 'HeLlo';

say lc $str;      # hello
say uc $str;      # HELLO
say length $str;  # 5

say()�A ���� print()�A�p�G�������Ѽƪ��ܡA�|�L�X $_�����e�C 


Perl �����اǦ� sort �i�H�����Ƨǰ}�C�A�o���t�H�N�~�C�Ө��²�����ϥΧΦ��A�K�O�ǤJ�@�Ӱ}�C�A���n�|�Ǧ^�Ʀn���s�}�C�G@sorted = sort @original�C




