require 'rubygems'
require 'mechanize'
require 'fileutils'

PAGE = 'http://wwwc.moex.gov.tw/main/exam/wFrmExamQandASearch.aspx?menu_id=156&sub_menu_id=156'
agent = Mechanize.new #先定義一個mechanize物件

page = agent.get(PAGE) #進入考古題頁面
form = page.form_with(id: "aspnetForm") #找到「查詢」按鈕所在的form
page2 = form.submit( form.button_with( id: "ctl00_holderContent_btnSearch")) #按下按鈕