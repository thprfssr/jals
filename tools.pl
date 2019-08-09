#!/bin/perl
use strict;
use Exporter;


# This function returns the word of a given dictionary entry.
sub get_word
{
	my $entry = $_[0];
	utf8::decode($entry);
	my $regex = qr/ \(.+?\):/;
	my @array = split($regex, $entry);
	my $word = $array[0];
	utf8::decode($word);
	return $word;
}

# This function checks that the entry is syntactically correct.
sub is_valid_entry
{
	my $entry = $_[0];
	my $regex = qr/.+? \([^\(\)]+?\): .+/;
	return ($entry =~ /$regex/);
}

# We end in 1 because otherwise, when we include this file into another,
# Perl will complain that a true value was not returned, or something.
1;
