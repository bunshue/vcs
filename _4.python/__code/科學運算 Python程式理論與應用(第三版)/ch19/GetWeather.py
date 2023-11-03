#coding=utf-8
# file: GetWeather.py
#
import tkinter
import json
import urllib.request

#傳回dict型態: twitter = {'image': imgPath, 'message': content}
def getCityWeather_RealTime(cityID):
    url = "http://www.weather.com.cn/data/sk/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')

        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        temp        = jsonDatas["weatherinfo"]["temp"]
        fx          = jsonDatas["weatherinfo"]["WD"]        #風向
        fl          = jsonDatas["weatherinfo"]["WS"]        #風力
        sd          = jsonDatas["weatherinfo"]["SD"]        #相對濕度
        tm          = jsonDatas["weatherinfo"]["time"]

        content = "#" + city + "#" + " " + temp + "℃ " + fx + fl + " " + "相對濕度" + sd + " "  + "發布時間:" + tm+"\n"
        twitter = {'image': "", 'message': content}

    except (SyntaxError) as err:
        print("SyntaxError: " + err.args)
    except:
        print("OtherError: ")
    else:
        return twitter
    finally:
        None

#傳回dict型態: twitter = {'image': imgPath, 'message': content}
def getCityWeatherDetail_SixDay(cityID):
    url = "http://m.weather.com.cn/data/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')
        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        tempF1      = jsonDatas["weatherinfo"]["tempF1"]
        weather     = jsonDatas["weatherinfo"]["img_title1"]
        img         = jsonDatas["weatherinfo"]["img1"]
        fx          = jsonDatas["weatherinfo"]["fx1"]       #風向
        cy            = jsonDatas["weatherinfo"]["index"]        #暖        #穿衣指數
        zw            = jsonDatas["weatherinfo"]["index_uv"]        #最弱   #紫外線指數
        xc            = jsonDatas["weatherinfo"]["index_xc"]        #不宜     #洗車
        tr            = jsonDatas["weatherinfo"]["index_tr"]        #很適宜    #旅游
        co            = jsonDatas["weatherinfo"]["index_co"]        #舒適     #舒適度
        cl            = jsonDatas["weatherinfo"]["index_cl"]        #較適宜  #晨練指數
        ls            = jsonDatas["weatherinfo"]["index_ls"]        #不太適宜  #晾曬指數
        ag            = jsonDatas["weatherinfo"]["index_ag"]        #不易發"    #過敏
        temp1       = jsonDatas["weatherinfo"]["temp1"]
        temp2       = jsonDatas["weatherinfo"]["temp2"]
        temp3       = jsonDatas["weatherinfo"]["temp3"]
        temp4       = jsonDatas["weatherinfo"]["temp4"]
        temp5       = jsonDatas["weatherinfo"]["temp5"]
        temp6       = jsonDatas["weatherinfo"]["temp6"]
        weather1    = jsonDatas["weatherinfo"]["weather1"]
        weather2    = jsonDatas["weatherinfo"]["weather2"]
        weather3    = jsonDatas["weatherinfo"]["weather3"]
        weather4    = jsonDatas["weatherinfo"]["weather4"]
        weather5    = jsonDatas["weatherinfo"]["weather5"]
        weather6    = jsonDatas["weatherinfo"]["weather6"]

        if int(img) < 10:
            imgPath = "icon\d" + "0" + str(img) + ".gif"
        else:
            imgPath = "icon\d"       + str(img) + ".gif"

        content = "#" + city + "#" + "\n<指數> " + "穿衣:" + cy + "\n 紫外線:" + zw + "\n 洗車:" + xc \
                + "\n 旅游:" + tr + "\n 舒適度:" + co + "\n 晨練:" + cl + "\n 晾曬:" + ls + "\n 過敏:" + ag + "\n" \
                + "\n<天氣>" + "\n 1天:" + temp1 + " " + weather1 + "\n 2天:" + temp2 + " " + weather2  + "\n 3天:" + temp3 + " " + weather3\
                + "\n 4天:" + temp4 + " " + weather4 + "\n 5天:" + temp5 + " " + weather5  + "\n 6天:" + temp6 + " " + weather6

        twitter = {'image': imgPath, 'message': content}

    except (SyntaxError) as err:
        print("SyntaxError: " + err.args)
    except:
        print(" : ")
    else:
        return twitter
    finally:
        None

#傳回dict型態: twitter = {'image': imgPath, 'message': content}
def getCityWeather_AllDay(cityID):
    url = "http://www.weather.com.cn/data/cityinfo/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')
        jsonDatas = json.loads(weatherInfomation)

        city        = jsonDatas["weatherinfo"]["city"]
        temp1       = jsonDatas["weatherinfo"]["temp1"]
        temp2       = jsonDatas["weatherinfo"]["temp2"]
        weather     = jsonDatas["weatherinfo"]["weather"]
        img1        = jsonDatas["weatherinfo"]["img1"]
        img2        = jsonDatas["weatherinfo"]["img2"]
        ptime        = jsonDatas["weatherinfo"]["ptime"]

        content = city + "," + weather + ",最高氣溫:" + temp1 + ",最低氣溫:"  + temp2 + ",發布時間:" + ptime +'\n\n'
        twitter = {'image': "icon\d" + img1, 'message': content}

    except (SyntaxError) as err:
        print(">>>>>> SyntaxError: " + err.args)
    except:
        print(">>>>>> OtherError: ")
    else:
        return twitter
    finally:
        None

class Window:
	def __init__(self, root):
		self.citys=self.getCitys('E:\Python\第19章\city.txt')
		self.root = root									# 建立元件
		self.label = tkinter.Label(root, text = '輸入城市:')
		self.label.place(x = 5, y = 15)
		self.entryCity = tkinter.Entry(root)
		self.entryCity.place(x = 65, y = 15)
		self.get = tkinter.Button(root, 
				text = '取得天氣', command = self.Get)
		self.get.place(x = 230, y = 15)
		self.edit = tkinter.Text(root,width = 300,height = 350)
		self.edit.place(y = 50)

	#從指定檔案中傳回城市與解碼對照字典
	def getCitys(self,file):
		file=open(file,encoding='utf-8')
		city={}
		for c in file.read().split('|'):
			cn,cc = c.split(',')
			city.update({cn:cc})
		return city
	
	def Get(self):
		city = self.entryCity.get().encode('utf-8')						# 取得城市
		for k in iter(self.citys.keys()):
			if k.endswith(city.decode()) :
				CityCode=self.citys[k]
				break

		title_small = "【實時天氣】\n"
		twitter = getCityWeather_RealTime(CityCode)
		self.edit.insert(tkinter.END, 							# 輸出日期和城市
					title_small + twitter['message']+'\n')

		title_small = "【今日天氣】\n"
		twitter = getCityWeather_AllDay(CityCode)
		self.edit.insert(tkinter.END, 							# 輸出日期和城市
					title_small + twitter['message']+'\n')

		title_small = "【今後六天】\n"
		twitter = getCityWeatherDetail_SixDay(CityCode)
		self.edit.insert(tkinter.END, 							# 輸出日期和城市
					title_small + twitter['message']+'\n')

if __name__ == '__main__':
    root = tkinter.Tk()
    window = Window(root)
    root.minsize(400,445)
    root.mainloop()
