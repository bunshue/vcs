'''
文字資訊的視覺化手法
繪製文字雲
'''

import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from janome.tokenizer import Tokenizer
from PIL import Image
import pandas as pd

print('------------------------------------------------------------')	#60個

#繪製英文的文字雲

# 原始文章
cloud_text = """Love encompasses a range of strong and positive emotional and mental states, from the most sublime virtue or good habit, the deepest interpersonal affection and to the simplest pleasure.[1][2] An example of this range of meanings is that the love of a mother differs from the love of a spouse, which differs from the love of food. Most commonly, love refers to a feeling of strong attraction and emotional attachment.[3]
Love is also considered to be a virtue representing human kindness, compassion, and affection, as "the unselfish loyal and benevolent concern for the good of another".[4] It may also describe compassionate and affectionate actions towards other humans, one's self or animals.[5]
Love in its various forms acts as a major facilitator of interpersonal relationships and, owing to its central psychological importance, is one of the most common themes in the creative arts.[6] Love has been postulated to be a function to keep human beings together against menaces and to facilitate the continuation of the species.[7]
Ancient Greek philosophers identified five forms of love: essentially, familial love (in Greek, Storge), friendly love or platonic love (Philia), romantic love (Eros), guest love (Xenia) and divine love (Agape). Modern authors have distinguished further varieties of love: unrequited love, empty love, companionate love, consummate love, infatuated love, self-love, 
and courtly love. Asian cultures have also distinguished Ren, Kama, Bhakti, Mettā, Ishq, Chesed, and other variants or symbioses of these states.[8][9] The triangular theory of love suggests "intimacy, passion and commitment" are core components of love. Love has additional religious or spiritual meaning. This diversity of uses and meanings combined with the complexity of the feelings involved makes love unusually difficult to consistently define, compared to other emotional states."""

wc = wordcloud.WordCloud(width=1000, height=600, background_color="white") 
wc.generate(cloud_text)

plt.imshow(wc) 
plt.axis("off")

plt.show()

print('------------------------------------------------------------')	#60個

#中日文文章的視覺化手法

# 利用半形空白字元切割的中文文章
#text_jp = """ メロスは激怒した。必ず、かの邪智暴虐じゃちぼうぎゃくの王を除かなければならぬと決意した。メロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。けれども邪悪に対しては、人一倍に敏感であった。きょう未明メロスは村を出発し、野を越え山越え、十里はなれた此このシラクスの市にやって来た。メロスには父も、母も無い。女房も無い。十六の、内気な妹と二人暮しだ。この妹は、村の或る律気な一牧人を、近々、花婿はなむことして迎える事になっていた。結婚式も間近かなのである。メロスは、それゆえ、花嫁の衣裳やら祝宴の御馳走やらを買いに、はるばる市にやって来たのだ。先ず、その品々を買い集め、それから都の大路をぶらぶら歩いた。メロスには竹馬の友があった。セリヌンティウスである。今は此のシラクスの市で、石工をしている。その友を、これから訪ねてみるつもりなのだ。久しく逢わなかったのだから、訪ねて行くのが楽しみである。歩いているうちにメロスは、まちの様子を怪しく思った。ひっそりしている。もう既に日も落ちて、まちの暗いのは当りまえだが、けれども、なんだか、夜のせいばかりでは無く、市全体が、やけに寂しい。のんきなメロスも、だんだん不安になって来た。路で逢った若い衆をつかまえて、何かあったのか、二年まえに此の市に来たときは、夜でも皆が歌をうたって、まちは賑やかであった筈はずだが、と質問した。若い衆は、首を振って答えなかった。しばらく歩いて老爺ろうやに逢い、こんどはもっと、語勢を強くして質問した。老爺は答えなかった。メロスは両手で老爺のからだをゆすぶって質問を重ねた。老爺は、あたりをはばかる低声で、わずか答えた。"""
text_tw = """ 梅洛絲氣急敗壞。 他決定一定要除掉那個邪惡、暴虐的國王。 梅羅斯不懂政治。 他是一個村裡的牧民。 他吹過笛子，和羊群生活過。 但他對邪惡比任何人都敏感。 而在今天黎明前，梅洛斯就離開了他的村莊，翻過田野，越過山巒，來到了十里外的錫拉庫扎城。 他沒有父親，沒有母親，也沒有妻子。 他沒有妻子。 他和靦腆的十六歲的妹妹住在一起。 妹妹要從村裡接來一個新郎，是個守規矩的牧民，很快就要結婚了。 婚禮就在眼前。 他大老遠跑來，就是為了買新娘的衣服和宴席。 他先買了貨，然後在京城的主要街道上逛了一圈。 梅羅斯有一個高蹺的朋友。 他就是塞利南提斯。 他現在是雪城這座城市的石匠。 我要去拜訪這位朋友。 好久不見，我很期待去看他。 在城市裡走來走去，梅羅斯對城市的面貌產生了懷疑。 這裡很安靜，也很荒涼。 太陽已經落山了，城市黑漆漆的可以理解，但這不僅僅是因為夜色，整個城市顯得十分寂寞。 無憂無慮的梅洛斯開始感到不安。 他抓住一個在街上遇到的年輕人，問他是不是發生了什麼事，因為兩年前他來這裡的時候，大家都在唱歌，即使到了晚上，這個城市也很熱鬧。 年輕人搖搖頭，沒有回答。 他走了一會兒，遇到老人，就問了他一個問題，這次的話更加有力。 老人沒有回答。 梅羅斯用手搖晃著老人的身體，問他更多的問題。 老人用難以捉摸的低沉聲音回答。"""

wc = wordcloud.WordCloud(width=1000, height=600, background_color="white",
                         font_path=r"C:\Windows\Fonts\msjh.ttc") 
#wc.generate(text_jp) 
wc.generate(text_tw) 
plt.imshow(wc) 
plt.axis("off")

plt.show()

print('------------------------------------------------------------')	#60個

#文章拆寫範例
# 中文的文章
text = """梅洛絲很是氣憤。 他決心要除掉這個邪惡暴虐的國王。 梅羅斯不懂政治。 梅羅斯是村裡的牧民。 他一生都在吹笛子，和羊群玩耍。 但他對邪惡比大多數人更敏感。 今天黎明時分，梅羅斯離開了自己的村莊，穿過田野和山林，來到了十里外的這座錫拉庫扎城。 他沒有父親，沒有母親，沒有妻子。 他沒有妻子。 他和年僅16歲的羞澀妹妹單獨生活。 妹妹要接受村裡某位守法的牧民作為她的新郎。 婚禮即將舉行。 因此，梅洛絲大老遠地來到集市上買新娘的衣服和宴席。 先是買了這些東西，然後他就在城市的大街小巷裡轉悠。 梅洛斯有一個高蹺的朋友。 他就是塞利農提斯。 他現在是錫拉庫扎市的一名石匠。 他要去看望他的朋友。 很久沒有見到他了，所以我很期待去看他。 走著走著，梅洛斯對這個小鎮產生了懷疑。 它是如此的安靜。 太陽已經落山了，城市自然是一片漆黑，但這不僅僅是因為夜晚，整個城市顯得十分寂寞。 就連無憂無慮的梅洛斯也開始感到不安。 他抓住一個在街上遇到的年輕人，問他是不是出了什麼事，他說："兩年前我來這個市場的時候，大家連晚上都在唱歌，鎮上一定很熱鬧。 年輕人搖搖頭，沒有回答。 走了一會兒，遇到老人，他用比較強硬的語氣問了他一個問題。 老人沒有回答。 梅洛斯雙手搖晃著老人的身體，問了更多的問題。 老人低沉地回答道。
"王者殺人。
"他為什麼要這麼做？
你說他心懷不軌，但沒有人心懷不軌。
你殺了很多人？
是的，先是王嫂。 然後自己的繼承人。 那麼他的妹妹。 然後他姐姐的兒子。 然後皇后。 還有他的智囊阿雷基斯。
"真沒想到啊! 國王瘋了嗎？
不，他不是。 他說他不能相信別人。 這些天，他甚至懷疑臣民的心，下令給那些生活稍顯浮誇的人每人一個人質。 如果你拒絕服從他的命令，你就會被釘在十字架上，被殺死。 今天，有6人被殺。
　聽了這話，梅羅斯很是氣憤。 我不能讓他活著 我不能讓你活著
　梅羅斯是個簡單的人。 他背著購物，溜躂著去了城堡。 他立即被巡警逮捕。 當他們搜查他時，在他的口袋裡發現了一把匕首，引起了很大的騷動。 梅羅斯被帶到國王面前。
'你打算用這把匕首做什麼？ 告訴我！ 暴君狄奧尼斯悄悄地問道，但卻很有尊嚴。 王爺的臉色蒼白，眼間的皺紋深重，彷彿刻在了臉上。
'把城市從暴君的手中拯救出來! 把城市從暴君的魔爪中拯救出來。"梅洛斯不無惡感地回答。
'你會嗎？ 國王憐憫他。 國王憐憫他說："你沒辦法。 你不知道我有多孤獨。
別這麼說！ 別這麼說！ 懷疑一個人的內心是一種最可恥的惡習。 國王懷疑他的人民的忠誠。
是你教會了我，懷疑是一種公正的態度。 人心是不可靠的。 人本質上是一種自私的生物。 不要相信他們。 暴君平靜地喃喃自語，嘆了口氣。 我也想要和平。
和平是為了什麼？ 為了保護自己的地位？ 梅洛斯對他冷嘲熱諷。 除了殺害無辜者，什麼是和平？
"閉嘴，你這個卑鄙的小偷! 國王抬起頭，反駁道。 國王抬頭看了看他，說："你的嘴可以說各種無辜的話。 我看不透棉花的深淺。 即使你現在被釘在十字架上，你也不會聽到我的哭泣和道歉。
"哦，王爺真聰明。 你想怎麼自負就怎麼自負。 我已經準備好去死了 我不會求生的。  我想讓我唯一的妹妹有一個丈夫。 三天後，我在村裡舉行婚禮，我會回到這裡。
"胡說八道! 暴君低聲沙啞地笑了起來。 你在說假話 你覺得你放跑的小鳥會回來嗎？
'是的，先生。 是的，它要回來了。 梅洛斯拚命堅持。 我會遵守我的諾言。 原諒我三天。 姐姐在等我回來。 如果你不相信，城裡有一個石匠叫塞利農提斯。 他是我的一個朋友。 我把他留在這裡當人質。 如果我跑了，直到第三天夜裡才回來，就掐死我的朋友。 我求你了，快去吧。
　國王聽了這話，對著北叟輕輕一笑，一副殘忍的樣子。 我相信你會很高興聽到這個消息。 反正他肯定不會回來了。 我不知道該怎麼做。 如果放他走，假裝被這個騙子騙了，第三天就把他殺了，那就有意思了。 所以人不可信。"我愁眉苦臉地說："我要把他釘在十字架上。 我想把他給天下所有的老實人看看。
我聽到你的要求了 你可以叫人代勞。 第三天日落前再來。 如果你遲到了，我就殺了他。 稍後再來。 我會永遠原諒你的罪過。
你在說什麼？
不知道 如果你珍惜自己的生命，就回來吧。 我知道你的心。
　梅洛斯覺得自己很可憐，跺了跺腳。 我不會說什麼的。
　他的朋友塞利農提斯在午夜時分被傳喚到王城。 在暴君狄奧尼索斯面前，好朋友和好朋友兩年來第一次見面。 梅洛斯把整個故事告訴了他的朋友。 塞利農提斯默默地點頭表示肯定，並緊緊地抱住了梅洛斯。 朋友和朋友之間的關係就這樣了。 塞利農提斯被套住了。 梅洛絲立即離開了。 時值初夏，滿天星斗。
　第二天早上，太陽已經高高掛起，村民們已經在田裡幹活了。 太陽已經高高掛在天空，村民們已經在田裡幹活了，梅洛斯十六歲的妹妹替哥哥站在田裡，守著羊群，她的妹妹也在田裡幹活。 她驚訝地發現哥哥搖搖晃晃地朝她走來，疲憊不堪。 她驚訝地發現哥哥搖搖晃晃地朝她走來，疲憊不堪，滿腹疑問。
"這沒什麼。 梅洛斯試圖強顏歡笑。 我在市裡留下了一些生意。 我在市裡留了些事，很快又要去那裡。 你的婚禮將在明天舉行。 越快越好。
　她的妹妹臉紅了。
你開心嗎？ 我給你買了一件漂亮的衣服。 現在去告訴村裡的人，明天就是婚禮了。 婚禮是明天。
　梅洛斯搖搖晃晃地回到家，裝飾了神壇，做了一場盛宴，然後倒在地上沉沉睡去，無法呼吸。
　他醒來的時候是晚上。 他一醒來，就去了新郎家。 一覺醒來，他就去新郎家，要求明天舉行婚禮。 新郎是個牧民，他很驚訝，說這是不可能的，他還沒有準備好，他們應該等到葡萄季節。 梅洛斯進一步追問他，說他不能等，必須等到明天。 他的女婿，也就是牧民，很頑固。 他好不容易才同意。 他們一直爭論到天亮，終於成功地哄騙和說服了女婿。 婚禮是在中午舉行的。 就在新郎新娘準備向神明宣誓的時候，黑雲遮天蔽日，大雨開始傾盆而下。 在場的村民都覺得有些不祥，但還是打起了精神，在自己的小房子裡，冒著濕熱的天氣，歡快地唱著歌，拍著手。 梅洛斯也是滿心歡喜，一時間他甚至忘記了自己對國王的承諾。 隨著夜幕的降臨，宴會越發的動盪和喜慶，人們完全沒有注意到外面的大雨。 梅洛斯以為自己想在這裡呆一輩子。 他希望和這些好心人共度餘生，但現在是他的身體而不是自己的身體。 這是不對的。 梅洛斯把自己搞得焦頭爛額，最後決定離開。 距離明天的日落還有十分鐘。 他以為自己會睡一覺，然後馬上離開。 那時候，雨就會放晴。 我想在這所房子裡呆多久就呆多久。  我相信你會很高興知道，我不是唯一的一個。
恭喜你啊 我累了，我想請假去睡覺。 一覺醒來，我就去市場。 我有重要的事情要處理。 即使我不在這裡，你已經有了一個好丈夫，所以你永遠不會寂寞。 你哥最討厭的就是疑神疑鬼，撒謊。 你知道的，不是嗎？ 你不能對你丈夫有任何的秘密。 這就是我對你說的一切。 你哥哥大概是個大人物，所以你應該為他感到驕傲。
　新娘夢寐以求地點點頭。 梅洛斯就拍了拍新郎的肩膀。
我們都沒有做好準備。 我家唯一的寶物就是姐姐和我的羊。 我沒有別的東西了 我會把它們都送出去。 還有一件事，你應該為自己是梅羅斯的弟弟而感到驕傲。
　新郎在搓著手，抽搐著。 梅羅斯笑著向村民們告別，然後離開了宴會，進入羊圈沉沉睡去，如同死去一般。
　他醒來的時候，是第二天的黃昏。 梅洛斯跳起來，自言自語道："納木措，我是不是睡得太久了？ 今天，我將向國王展示人類的真相。 那麼我將帶著微笑走上十字架。 梅洛斯開始悠閒地準備著。 雨勢似乎有所減弱。 準備工作已經完成。 現在，梅羅斯揮舞著雙臂，像箭一樣在雨中奔跑。
　我今晚就會被殺。 我是奔著被殺去的。 我跑去救我的朋友，他是我的贖金。 我是奔著打敗國王的邪惡和奸詐而去的。 我得走了 我就是這樣被殺的。 從小守護自己的榮譽。 再見了，祖國。 這對年輕的梅洛斯來說是很難的。 有好幾次，他幾乎停了下來。 他一邊跑，一邊大喊大叫，自責不已。 到了下一個村子，雨已經停了，太陽高高掛在天上，天氣越來越熱。 梅洛斯用拳頭擦了擦額頭的汗水，說："既然走到了這一步，我就沒事了。 我的姐妹們會是一對好夫妻。 我現在應該沒有任何顧慮了。 你要做的就是直接去城堡。 你不用這麼著急。 我慢慢走。"說著，他又恢復了天生的慵懶，用好聽的聲音唱起了他最喜歡的小調。 他晃晃悠悠地走了兩三里路，走到半路時，一場突如其來的災難讓他停下了腳步。 看著前面的河水。 昨日的大雨已經溢出了山中的水源，渾濁的水流在下游彙集成一股洪流，一舉摧毀了大橋，迴蕩的洪流在橋樑上彈出一片塵土。 他驚呆了，站在原地不動。 他這裡看看，那裡看看，高聲呼喚，但所有的停泊船都被海浪衝走了，沒有擺渡人的蹤影。 目前在這裡。"""

# 拆解中文文章
tk = Tokenizer()
wakatigaki = tk.tokenize(text, wakati=True)
print(wakatigaki)

# 利用wordcloud函式庫將分割完畢的文字資訊畫成文字雲
wc = wordcloud.WordCloud(width=1000, height=600, background_color="white",
                         font_path=r"C:\Windows\Fonts\msjh.ttc")
wc.generate(" ".join(wakatigaki)) 
plt.imshow(wc) 
plt.axis("off")


plt.show()

print('------------------------------------------------------------')	#60個


#就算名詞只有一個字也繪製的範例

meishi_list = [] 

for token in tk.tokenize(text):
    if token.part_of_speech.split(",")[0] == "名詞":
            meishi_list.append(token.surface)
            
# 要讓只有一個字的單字出現必須設定regexp
wc = wordcloud.WordCloud(width=1000, height=600, background_color="white",
                         font_path=r"C:\Windows\Fonts\msjh.ttc",
                         regexp="[\w']+") 
wc.generate(" ".join(meishi_list)) 
plt.imshow(wc) 
plt.axis("off")


plt.show()

print('------------------------------------------------------------')	#60個


#調整文字雲的形狀
#愛心形狀的文字雲繪製範例
# 原始文章
cloud_text = """Love encompasses a range of strong and positive emotional and mental states, from the most sublime virtue or good habit, the deepest interpersonal affection and to the simplest pleasure.[1][2] An example of this range of meanings is that the love of a mother differs from the love of a spouse, which differs from the love of food. Most commonly, love refers to a feeling of strong attraction and emotional attachment.[3]
Love is also considered to be a virtue representing human kindness, compassion, and affection, as "the unselfish loyal and benevolent concern for the good of another".[4] It may also describe compassionate and affectionate actions towards other humans, one's self or animals.[5]
Love in its various forms acts as a major facilitator of interpersonal relationships and, owing to its central psychological importance, is one of the most common themes in the creative arts.[6] Love has been postulated to be a function to keep human beings together against menaces and to facilitate the continuation of the species.[7]
Ancient Greek philosophers identified five forms of love: essentially, familial love (in Greek, Storge), friendly love or platonic love (Philia), romantic love (Eros), guest love (Xenia) and divine love (Agape). Modern authors have distinguished further varieties of love: unrequited love, empty love, companionate love, consummate love, infatuated love, self-love, and courtly love. Asian cultures have also distinguished Ren, Kama, Bhakti, Mettā, Ishq, Chesed, and other variants or symbioses of these states.[8][9] The triangular theory of love suggests "intimacy, passion and commitment" are core components of love. Love has additional religious or spiritual meaning. This diversity of uses and meanings combined with the complexity of the feelings involved makes love unusually difficult to consistently define, compared to other emotional states."""


mask_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/heart.png'
# 載入遮罩圖片
mask_image = np.array(Image.open(mask_filename))

# 產生以圖片作為遮罩的文字雲
wc = wordcloud.WordCloud(width=700, height=700,
                         background_color="white",
                         font_path=r"C:\Windows\Fonts\msjh.ttc",
                         mask=mask_image, contour_width=6,
                         contour_color="pink", colormap="plasma")
wc.generate(cloud_text) 

# 顯示文字雲
plt.imshow(wc) 
plt.axis("off")

plt.show()

print('------------------------------------------------------------')	#60個

# 指定特定文字的顏色
# 原始文章
text = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 產生文字雲
wc = wordcloud.WordCloud()
wc.generate(text.lower()) 

# 定義調色函數
def color_func(word, **kwargs):    
    # 單字與顏色的對照字典
    color_dict = {"idea": "red", "although": "green"}        
    # 設定未於字典出現的單字的顏色
    default_color = "grey"
    return color_dict.get(word, default_color) 
# 執行調色函數，重新替文字上色
wc.recolor(color_func=color_func) 

# 顯示文字雲
plt.imshow(wc) 
plt.axis("off")

plt.show()

print('------------------------------------------------------------')	#60個

import wordcloud
from PIL import Image

cloud_text = open('eduheadlines.txt','r', encoding='utf-8').read()
print(cloud_text)

mask_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/star.jpg'
# 載入遮罩圖片
mask_image = np.array(Image.open(mask_filename))

wc = wordcloud.WordCloud(width=1000, height=860,
                         background_color="white",
                         font_path=r"C:\Windows\Fonts\msjh.ttc",
                         margin=2,
                         mask=mask_image)
wc.generate(cloud_text)

# 顯示文字雲
plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")

plt.show()

print('------------------------------------------------------------')	#60個

import sqlite3

from wordcloud import WordCloud
from PIL import Image

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
all_news = ""
for row in rows:
    all_news += row[3]

mask_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/cloud.jpg'
# 載入遮罩圖片
mask_image = np.array(Image.open(mask_filename))

wordcloud = WordCloud(background_color="white",
                      width=1000, height=860,
                      font_path=r"C:\Windows\Fonts\msjh.ttc",
                      margin=2,
                      mask=mask_image).generate(all_news)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()


print('------------------------------------------------------------')	#60個

''' 無檔案 stopWords.txt
import sqlite3

from wordcloud import WordCloud
from PIL import Image
import jieba
from collections import Counter

dbfile = "applenews.db"
conn = sqlite3.connect(dbfile)

sql_str = "select * from news;"
rows = conn.execute(sql_str)
all_news = ""
for row in rows:
    all_news += row[3]

stopwords = list()
with open('stopWords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(all_news) if keyterm not in stopwords]
text = ",".join(keyterms)

mask_filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_mask/cloud.jpg'
# 載入遮罩圖片
mask_image = np.array(Image.open(mask_filename))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860,
                      font_path=r"C:\Windows\Fonts\msjh.ttc",
                      margin=2,
                      mask=mask_image).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()
'''

