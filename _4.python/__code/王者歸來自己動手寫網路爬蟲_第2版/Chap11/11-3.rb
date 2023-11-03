require 'rubygems'
require 'nokogiri'
require 'open-uri'

BASE_WIKIPEDIA_URL = "https://en.wikipedia.org"
LIST_URL = "#{BASE_WIKIPEDIA_URL}/wiki/Grammy_Award_for_Album_of_the_Year"

page = Nokogiri::HTML(open(LIST_URL))
rows = page.css('div.mw-content-ltr table.wikitable tr')

rows[1..-2].each do |row|

  hrefs = row.css("td a").map{ |a| 
    a['href'] if a['href'] =~ /^\/wiki\// 
  }.compact.uniq

  hrefs.each do |href|
    remote_url = BASE_WIKIPEDIA_URL + href
    puts remote_url    
  end 
end