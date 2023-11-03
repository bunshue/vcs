#以下為必要的ruby gem一定要先安裝
require 'rubygems'
require 'nokogiri'
require 'open-uri'
require 'fileutils'

#建立下載目錄
DATA_DIR = "download/albumoftheyear"
FileUtils::mkdir_p DATA_DIR unless File.exists?(DATA_DIR)

#下載的URL以及子頁
BASE_WIKIPEDIA_URL = "https://en.wikipedia.org"
LIST_URL = "#{BASE_WIKIPEDIA_URL}/wiki/Grammy_Award_for_Album_of_the_Year"

#指定User-Agent
HEADERS_HASH = {"User-Agent" => "Ruby Crawler"}

#指定要下載的頁面
page = Nokogiri::HTML(open(LIST_URL))

#指定要抓出的表格的selector
rows = page.css('div.mw-content-ltr table.wikitable tr')

#開始從表格中抓取
rows[1..-2].each do |row|

  hrefs = row.css("td a").map{ |a| 
    a['href'] if a['href'] =~ /^\/wiki\// 
  }.compact.uniq

  hrefs.each do |href|
    remote_url = BASE_WIKIPEDIA_URL + href
    local_fname = "#{DATA_DIR}/#{File.basename(href)}.html"
    unless File.exists?(local_fname)
      puts "抓取 #{remote_url}..."
      begin
        wiki_content = open(remote_url, HEADERS_HASH).read
      rescue Exception=>e
        puts "Error: #{e}"
        sleep 5
      else
        File.open(local_fname, 'w'){|file| file.write(wiki_content)}
        puts "\t...成功, 已儲存至 #{local_fname}"
      ensure
        sleep 1.0 + rand
      end  
    end 
  end
end