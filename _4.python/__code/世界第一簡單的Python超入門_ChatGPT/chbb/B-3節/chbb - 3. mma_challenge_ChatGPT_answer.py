from PIL import Image, ImageTk
import tkinter as tk
import requests, random, io

class MetropolitanApp:
    def __init__(self, base):
        # 設定 WebAPI 網址
        self.api_object_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        self.api_search_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?'

        # 設定變數
        self.total_num = 0
        self.index_num = 0
        self.canvas_width = 400
        self.canvas_height = 400
        self.art_ids = dict()
        self.art_info = tk.StringVar()

        # 初始畫面所顯示的作品 ID
        default_art_id = 55648

        # 設定 frame 區塊
        search_frame = tk.Frame(base)
        control_frame = tk.Frame(base)

        # 設定顯示搜尋結果的 label 區
        self.label_text = tk.StringVar()
        self.label_text.set('Enter keyword and push search button')
        self.label = tk.Label(base, textvariable=self.label_text)

        # 設定文字輸入框
        self.entry = tk.Entry(search_frame)

        # 按鈕的設定
        self.search_button = tk.Button(search_frame, text='Search', command=self.searchArt)
        self.random_button = tk.Button(control_frame, text='Random', command=self.selectRandom)
        self.next_button = tk.Button(control_frame, text='Next', command=self.nextArt)
        self.prev_button = tk.Button(control_frame, text='Prev', command=self.prevArt)

        # 設定 canvas 和預設顯示的作品
        self.canvas = tk.Canvas(base, bg='pink', borderwidth=5, relief=tk.RIDGE, width=self.canvas_width, height=self.canvas_height)
        response = self.getArtObject(default_art_id)
        image_url = response['primaryImageSmall']

        # 顯示預設的作品圖片
        image_pil = Image.open(io.BytesIO(requests.get(image_url).content))
        image_pil = self.resizeArtImage(image_pil)
        self.photo_image = ImageTk.PhotoImage(image_pil)
        self.canvas_number = self.canvas.create_image(self.canvas_width/2 + 5, self.canvas_height/2 + 5, anchor=tk.CENTER, image=self.photo_image)

        # 最下面那塊作品資訊區的設定
        self.artInfoArea = tk.Message(base, relief="raised", textvariable=self.art_info, width=self.canvas_width)
        self.displayArtInfo(response)

        # 將各物件配置在 base 視窗上
        search_frame.pack()
        self.entry.grid(column=0, row=0, pady=10)
        self.search_button.grid(column=1, row=0, padx=10, pady=10)

        self.label.pack()
        self.canvas.pack()

        control_frame.pack()
        self.prev_button.grid(column=0, row=0, padx=50, pady=10)
        self.random_button.grid(column=1, row=0, padx=50, pady=10)
        self.next_button.grid(column=2, row=0, padx=50, pady=10)

        self.artInfoArea.pack()

    def searchArt(self):
        search_art_url = self.api_search_url + 'q=' + self.entry.get() + '&hasImages=true'
        response = requests.get(search_art_url)
        response_dict = response.json()

        self.index_num = 0
        # 存放搜尋結果 
        self.total_num = response_dict['total']
        self.art_ids = response_dict['objectIDs']
        self.displayArt(self.art_ids[0])

    def nextArt(self):
        self.index_num = self.index_num + 1
        if (self.index_num > self.total_num -1):
            self.index_num = 0

        next_art_id = self.art_ids[self.index_num]
        self.displayArt(next_art_id)

    def prevArt(self):
        self.index_num = self.index_num - 1
        if(self.index_num < 0):
            self.index_num = self.total_num -1

        prev_art_id = self.art_ids[self.index_num]
        self.displayArt(prev_art_id)

    def selectRandom(self):
        self.index_num = random.randint(0, (self.total_num-1))
        art_id = self.art_ids[self.index_num]
        self.displayArt(art_id)

    def getArtObject(self, object_id):
        get_object_url = self.api_object_url + str(object_id)
        api_response = requests.get(get_object_url)
        return api_response.json()

    def displayArt(self, object_id):
        art_object = self.getArtObject(object_id)
        self.label_text.set(str(self.index_num + 1) + ' / ' + str(self.total_num))
        self.displayArtImage(art_object)
        self.displayArtInfo(art_object)

    def displayArtImage(self, art_object):
        image_url = art_object['primaryImageSmall']
        image_pil = Image.open(io.BytesIO(requests.get(image_url).content))
        image_pil = self.resizeArtImage(image_pil)
        self.photo_image = ImageTk.PhotoImage(image_pil)
        self.canvas.itemconfig(self.canvas_number, image=self.photo_image)

    def displayArtInfo(self, art_object):
        art_info_text = '[Title]: ' + art_object['title'] + '\n'
        art_info_text += '[Artist]: ' + art_object['artistDisplayName'] + '\n'
        art_info_text += '[Country]: ' + art_object['country'] + '\n' #新增國家
        art_info_text += '[Date]: ' + art_object['objectDate'] + '\n' #新增日期
        art_info_text += '[Type]: ' + art_object['classification'] + '\n'
        art_info_text += '[URL]: ' + art_object['objectURL']

        self.art_info.set(art_info_text)


    def resizeArtImage(self, art_image):
        if (art_image.width > art_image.height):
            resize_ratio = round(self.canvas_width / art_image.width, 2)
        else:
            resize_ratio = round(self.canvas_height / art_image.height, 2)
        art_image = art_image.resize((int(art_image.width*resize_ratio), int(art_image.height*resize_ratio)))
        return art_image


# 建立基礎視窗，並產生 MetropolitanApp 物件
base = tk.Tk()
base.title('The Metropolitan Museum of Art Collection Viewer')
base.geometry('500x700')
app = MetropolitanApp(base)
base.mainloop()