BASE_WIKIPEDIA_URL = "https://en.wikipedia.org"
LIST_URL = "#{BASE_WIKIPEDIA_URL}/wiki/Grammy_Award_for_Album_of_the_Year"
page = Nokogiri::HTML(open(LIST_URL))
rows = page.css('div.mw-content-ltr table.wikitable tr')