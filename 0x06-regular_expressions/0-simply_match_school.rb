#!/usr/bin/env ruby

# Get the argument from the command line
input = ARGV[0]

# Define the regular expression pattern
pattern = /School/
  
# Check if the input matches the pattern
if input =~ pattern
  puts "The input '#{input}' matches the pattern for 'School'."
else
  puts "The input '#{input}' does not match the pattern for 'School'."
end
