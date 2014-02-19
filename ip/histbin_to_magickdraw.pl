#!/usr/bin/perl -W
# histbin_to_magickdraw.pl
# convert .... $(echo -e "<count>:#color\n<count>:#color\n..." | ./histbin_to_magickdraw.pl)
# generates count-relative color patch images based on histogram bin data
#
use strict;

my $WIDTH = 200;
my $HEIGHT = 200;
my @data = ();
my $sum = 0;
while(<>)
{
	chomp; chomp;
	my ($count,$color) = split /:/;
	push @data, [$count,$color];
	$sum += $count;
}

my $ppc = $WIDTH/$sum;
my $pos = 0;
foreach(@data)
{
	my $w = int($ppc*$_->[0]);
	my $c = $_->[1];
	printf " -fill $c -draw \'rectangle %d,%d %d,%d\' ", $pos, $HEIGHT, $pos+$w, $HEIGHT;
	$pos += $w;
	return if($pos >= $WIDTH);
}
