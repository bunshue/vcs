from PIL import Image, ImageTk
import tkinter as tk
import requests, random, io

class MetropolitanApp:
    def __init__(self, base):
        # URLの設定
        self.api_object_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/'
        self.api_search_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?'

        # 変数の設定
        self.total_num = 0
        self.index_num = 0
        self.canvas_width = 400
        self.canvas_height = 400
        self.art_ids = dict()
        self.art_info = tk.StringVar()

        # 最初に表示する作品のID
        # 解答1 default_art_id に好きな作品のidを設定する
        default_art_id = 460337

        # frameの設定
        search_frame = tk.Frame(base)
        control_frame = tk.Frame(base)

        # 検索結果を表示するlabelの設定
        self.label_text = tk.StringVar()
        self.label_text.set('Enter keyword and push search button')
        self.label = tk.Label(base, textvariable=self.label_text)

        # テキストボックスEntryの設定
        self.entry = tk.Entry(search_frame)

        # ボタンの設定
        self.search_button = tk.Button(search_frame, text='Search', command=self.searchArt)
        self.random_button = tk.Button(control_frame, text='Random', command=self.selectRandom)
        self.next_button = tk.Button(control_frame, text='Next', command=self.nextArt)
        self.prev_button = tk.Button(control_frame, text='Prev', command=self.prevArt)

        # canvasの設定と最初に表示する作品の設定
        self.canvas = tk.Canvas(base, bg='black', borderwidth=5, relief=tk.RIDGE, width=self.canvas_width, height=self.canvas_height)
        response = self.getArtObject(default_art_id)
        image_url = response['primaryImageSmall']

        # デフォルトの作品の画像の表示
        image_pil = Image.open(io.BytesIO(requests.get(image_url).content))
        image_pil = self.resizeArtImage(image_pil)
        self.photo_image = ImageTk.PhotoImage(image_pil)
        self.canvas_number = self.canvas.create_image(self.canvas_width/2 + 5, self.canvas_height/2 + 5, anchor=tk.CENTER, image=self.photo_image)

        # 作品の情報を表示するMessageの設定
        self.artInfoArea = tk.Message(base, relief="raised", textvariable=self.art_info, width=self.canvas_width)
        self.displayArtInfo(response)

        # 部品の配置の設定
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
        # 検索結果の格納
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
        # 解答2 art_info_textに、追加したい情報を入力 以下は countryとDateを追加
        art_info_text += '[Country]: ' + art_object['country'] + '\n'
        art_info_text += '[Date]: ' + art_object['objectDate'] + '\n'

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


# アプリのベースとMetropolitan Appのインスタンスの生成
base = tk.Tk()
base.title('The Metropolitan Museum of Art Collection Viewer')
base.geometry('500x700')
app = MetropolitanApp(base)
base.mainloop()