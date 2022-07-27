#!/usr/bin/env ruby
#a Ruby script that accepts one argument and pass it to a regular expression matching method
#Find the regular expression that will match any string that contains at least one t
puts ARGV[0].scan(/hbt+n/).join
