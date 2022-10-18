#!/usr/bin/env ruby
puts ARGVs[0].scan(/(?<=from:\to:\flags:).+?(?=\])/).join(',')
