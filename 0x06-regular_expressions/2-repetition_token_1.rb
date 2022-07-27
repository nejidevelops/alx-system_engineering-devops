#!/usr/bin/env ruby
#a Ruby script that accepts one argument and pass it to a regular expression matching method
#Find the regular expression that will match any string that contains zero or one occurrences of b
puts ARGV[0].scan(/hb?tn/).join
