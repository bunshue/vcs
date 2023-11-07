import re
import chatBot_module as m

def bot_speak_re(sentence):
	s1 = re.sub(r'\[[^\]]*\]', '', sentence)
	print(s1)
	en_list = re.findall(r'[a-zA-Z ]+',s1)
	s2 = re.sub(r'[a-zA-Z \-]+', '@English@', s1)
	all_list = s2.split('@')
	index = 0
	for text in all_list:
		if text != 'English':    
			m.bot_speak(text, 'zh-tw')
		else:
			m.bot_speak(en_list[index], 'en')
			index += 1
#-----------------------------------------------#
sentence = 	'阿爾伯特·愛因斯坦，或譯亞伯特·愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。'
bot_speak_re(sentence)




