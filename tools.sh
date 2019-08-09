#!/bin/bash


function get_word_from_entry
{
perl <<-EOF
use strict;
require "./tools.pl";

print(get_word("$1") . "\n")
EOF
}

function is_valid_entry
{
perl <<-EOF
use strict;
require "./tools.pl";

if (is_valid_entry("$1")) {
	print(1);
} else {
	print(0);
}
EOF
}
