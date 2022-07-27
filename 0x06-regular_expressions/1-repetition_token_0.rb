#!/usr/bin/env ruby
#a Ruby script that accepts one argument and pass it to a regular expression matching method
#Find the regular expression that will match any string that contains a sequence of 2 to 5 t's
puts ARGV[0].scan(/hbt{2,5}n/).join
