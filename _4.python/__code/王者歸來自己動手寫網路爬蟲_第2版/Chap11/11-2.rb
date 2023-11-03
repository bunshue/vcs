rows[1..-2].each do |row|
  hrefs = row.css("td a").map{ |a| 
    a['href'] if a['href'].match("/wiki/")
  }.compact.uniq

  hrefs.each do |href|
   puts href
  end
end