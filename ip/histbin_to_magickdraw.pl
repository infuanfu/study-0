#!/usr/bin/perl -W
# histbin_to_magickdraw.pl
# convert .... $(echo -e "<count>:#color\n<count>:#color\n..." | ./histbin_to_magickdraw.pl)
# generates count-relative color patch images based on histogram bin data
#
use strict;

my $WIDTH = 1280;
my $HEIGHT = 50;
my @data = ();
my $sum = 0;
while(<>)
{
	#27839: (255,255,255) #FFFFFF white
	if(/(\d+):[^#]+(\#.{6})/)
	{
		push @data, [$1,$2];
		$sum += $1;
	}
}

my $ppc = $WIDTH/$sum;
my $pos = 0;
foreach(@data)
{
	my $w = 1+int($ppc*$_->[0]);
	my $c = $_->[1];
	printf " -draw \'fill $c rectangle %d,%d %d,%d' ", $pos, 0, $pos+$w, $HEIGHT;
	$pos += $w;
	last if($pos >= $WIDTH);
}
