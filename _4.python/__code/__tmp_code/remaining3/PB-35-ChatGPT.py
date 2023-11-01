def displayArtInfo(self, art_object):
    art_info_text = '[Title]: ' + art_object['title'] + '\n'
    art_info_text += '[Artist]: ' + art_object['artistDisplayName'] + '\n'
    art_info_text += '[Country]: ' + art_object['country'] + '\n' #新增國家
    art_info_text += '[Date]: ' + art_object['objectDate'] + '\n' #新增日期
    art_info_text += '[Type]: ' + art_object['classification'] + '\n'
    art_info_text += '[URL]: ' + art_object['objectURL']

    self.art_info.set(art_info_text)



























