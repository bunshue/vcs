using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Drawing.Text;              //for TextRenderingHint
using System.Security.Cryptography;     //for RNGCryptoServiceProvider

namespace vcs_test_all_01_Random
{
    public partial class Form1 : Form
    {
        //任意陣列
        private string[] ItemArray;
        private List<string> ItemList;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //任意陣列
            // Initialize the array and list.
            ItemArray = new string[] { "Apple", "Banana", "Cherry", "Date", "Eagle", "Fish", "Golf", "Harp", "Ibex", "Jackel", "Kangaroo" };
            ItemList = new List<string>(ItemArray);

            // Display the array and list in ListBoxes.
            lstArray.DataSource = ItemArray;
            lstList.DataSource = ItemList;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            groupBox1.Size = new Size(410, 720);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button0.Location = new Point(x_st + dx * 0 + 10, y_st + dy * 10 + 30);
            button1.Location = new Point(x_st + dx * 0 + 10, y_st + dy * 11 + 30);

            dx = 190 + 10;
            y_st = 20;
            bt_random0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_random1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_random2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_random3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_random4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_random5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_random6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_random7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_random8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_random9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_random10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_random11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_random12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_random13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_random14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_random15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_random16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_random17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_random18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            bt_random19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(450, 860);
            richTextBox1.Location = new Point(x_st + dx * 5 + 50, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Size = new Size(256, 256);
            pictureBox1.Location = new Point(800, 20);

            pictureBox2.Size = new Size(256 / 2, 50);
            pictureBox2.Location = new Point(800, 20 + 256 + 10);

            pictureBox3.Size = new Size(256 / 2, 50);
            pictureBox3.Location = new Point(800 + 256 / 2, 20 + 256 + 10);

            pictureBox4.Size = new Size(256 / 2, 50);
            pictureBox4.Location = new Point(800, 20 + 256 + 10 + 50 + 10);

            pictureBox5.Size = new Size(256 / 2, 50);
            pictureBox5.Location = new Point(800 + 256 / 2, 20 + 256 + 10 + 50 + 10);

            int w = 270;
            int h = 50;
            x_st = 430;
            y_st = 430;
            dx = w + 30;
            dy = 46;

            tb_random_text0.Size = new Size(w, h);
            tb_random_text1.Size = new Size(w, h);
            tb_random_text2.Size = new Size(w, h);
            tb_random_text3.Size = new Size(w, h);
            tb_random_text4.Size = new Size(w, h);
            tb_random_text5.Size = new Size(w, h);
            tb_random_text6.Size = new Size(w, h);
            tb_random_text7.Size = new Size(w, h);
            tb_random_text8.Size = new Size(w, h);
            tb_random_text9.Size = new Size(w, h);
            tb_random_text10.Size = new Size(w, h);
            tb_random_text11.Size = new Size(w, h);
            tb_random_text12.Size = new Size(w, h);
            tb_random_text13.Size = new Size(w, h);
            tb_random_text14.Size = new Size(w, h);
            tb_random_text15.Size = new Size(w, h);
            tb_random_text16.Size = new Size(w, h);
            tb_random_text17.Size = new Size(w, h);
            tb_random_text18.Size = new Size(w, h);
            tb_random_text19.Size = new Size(w, h);

            lb_random0.Location = new Point(x_st, y_st + dy * 0);
            lb_random1.Location = new Point(x_st, y_st + dy * 1);
            lb_random2.Location = new Point(x_st, y_st + dy * 2);
            lb_random3.Location = new Point(x_st, y_st + dy * 3);
            lb_random4.Location = new Point(x_st, y_st + dy * 4);
            lb_random5.Location = new Point(x_st, y_st + dy * 5);
            lb_random6.Location = new Point(x_st, y_st + dy * 6);
            lb_random7.Location = new Point(x_st, y_st + dy * 7);
            lb_random8.Location = new Point(x_st, y_st + dy * 8);
            lb_random9.Location = new Point(x_st, y_st + dy * 9);
            lb_random10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_random11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_random12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_random13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            lb_random14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            lb_random15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            lb_random16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            lb_random17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            lb_random18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            lb_random19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            int ddx = 20;
            tb_random_text0.Location = new Point(x_st + ddx, y_st + dy * 0);
            tb_random_text1.Location = new Point(x_st + ddx, y_st + dy * 1);
            tb_random_text2.Location = new Point(x_st + ddx, y_st + dy * 2);
            tb_random_text3.Location = new Point(x_st + ddx, y_st + dy * 3);
            tb_random_text4.Location = new Point(x_st + ddx, y_st + dy * 4);
            tb_random_text5.Location = new Point(x_st + ddx, y_st + dy * 5);
            tb_random_text6.Location = new Point(x_st + ddx, y_st + dy * 6);
            tb_random_text7.Location = new Point(x_st + ddx, y_st + dy * 7);
            tb_random_text8.Location = new Point(x_st + ddx, y_st + dy * 8);
            tb_random_text9.Location = new Point(x_st + ddx, y_st + dy * 9);
            tb_random_text10.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 0);
            tb_random_text11.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 1);
            tb_random_text12.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 2);
            tb_random_text13.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 3);
            tb_random_text14.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 4);
            tb_random_text15.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 5);
            tb_random_text16.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 6);
            tb_random_text17.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 7);
            tb_random_text18.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 8);
            tb_random_text19.Location = new Point(x_st + dx * 1 + ddx, y_st + dy * 9);

            lb_random0.Text = "0";
            lb_random1.Text = "1";
            lb_random2.Text = "2";
            lb_random3.Text = "3";
            lb_random4.Text = "4";
            lb_random5.Text = "5";
            lb_random6.Text = "6";
            lb_random7.Text = "7";
            lb_random8.Text = "8";
            lb_random9.Text = "9";
            lb_random10.Text = "10";
            lb_random11.Text = "11";
            lb_random12.Text = "12";
            lb_random13.Text = "13";
            lb_random14.Text = "14";
            lb_random15.Text = "15";
            lb_random16.Text = "16";
            lb_random17.Text = "17";
            lb_random18.Text = "18";
            lb_random19.Text = "19";

            this.Size = new Size(1540, 930);
            this.Text = "vcs_test_all_01_Random";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void bt_random0_Click(object sender, EventArgs e)
        {
            //取得亂數的方法
            int[] rs = new int[10];
            for (int i = 0; i < 10; i++)
            {
                rs[i] = GetRandom1();
            }

            richTextBox1.Text += "方法一, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";
            }

            richTextBox1.Text += "\t大部分都一樣\n";

            for (int i = 0; i < 10; i++)
            {
                rs[i] = GetRandom2();
            }

            richTextBox1.Text += "方法二, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";
            }

            richTextBox1.Text += "\t可取得亂數\n";
        }

        private int GetRandom1()
        {
            Random rand = new Random();
            return rand.Next(0, 1000);
        }

        //定義一個自增的數字作為種子
        private static int _RandomSeed = (int)DateTime.Now.Ticks;
        private int GetRandom2()
        {
            if (_RandomSeed == int.MaxValue)
            {
                _RandomSeed = 1;
            }

            //Random初始化+種子
            Random rand = new Random(_RandomSeed++);  // 使用亂數種子
            return rand.Next(0, 1000);
        }

        private void bt_random1_Click(object sender, EventArgs e)
        {
            Random rand = new Random();
            string result1 = "";
            string result2 = "";
            string result3 = "";
            string result4 = "";
            for (int i = 0; i < 5; i++)
            {
                result1 += rand.Next().ToString() + " ";
                result2 += rand.Next(10).ToString() + " ";
                result3 += rand.Next(10, 20).ToString() + " ";
                result4 += rand.NextDouble().ToString() + " ";
            }
            richTextBox1.Text += "取>=0的亂數值：" + result1 + "\n";
            richTextBox1.Text += "取0~10的亂數值：" + result2 + "\n";
            richTextBox1.Text += "取10~20的亂數值：" + result3 + "\n";
            richTextBox1.Text += "取0.0~1.0的亂數值：" + result4 + "\n";
        }

        private void bt_random2_Click(object sender, EventArgs e)
        {
            Random rand = new Random();

            int[] cards = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int tmp;

            for (int i = 0; i < cards.Length; i++)
            {
                int n = rand.Next(cards.Length);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = cards[i];
                cards[i] = cards[n];
                cards[n] = tmp;
            }
            richTextBox1.Text += "方法一結果：";
            for (int i = 0; i < cards.Length; i++)
            {
                richTextBox1.Text += cards[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < cards.Length; i++)
            {
                cards[i] = i;
            }

            for (int i = cards.Length - 1; i > 0; i--)
            {
                int n = rand.Next(i + 1);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = cards[i];
                cards[i] = cards[n];
                cards[n] = tmp;
            }

            richTextBox1.Text += "方法二結果：";
            for (int i = 0; i < cards.Length; i++)
            {
                richTextBox1.Text += cards[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }
        //------------------------------------------------------------  # 60個

        /*
ASP.Net實現中文漢字驗證碼

1、漢字編碼原理
  到底怎麼辦到隨機生成漢字的呢？漢字從哪裡來的呢？是不是有個後台數據表，其中存放了所需要的所有漢字，使用程序隨機取出幾個漢字組合就行了呢？使用後台數據庫先將所有漢字存起來使用時隨機取出，這也是一種辦法，但是中文漢字有這麼多，怎麼來制作呢？其實可以不使用任何後台數據庫，使用程序就能做到這一切。要知道如何生成漢字，就得先了解中文漢字的編碼原理。
  1980年，為了使每一個漢字有一個全國統一的代碼，我國頒布了第一個漢字編碼的國家標准： GB2312-80《信息交換用漢字編碼字符集》基本集，簡稱GB2312，這個字符集是我國中文信息處理技術的發展基礎，也是國內所有漢字系統的統一標准。到了後來又公布了國家標准GB18030-2000《信息交換用漢字編碼字符集基本集的擴充》，簡稱GB18030，編程時如果涉及到編碼和本地化的朋友應該對GB18030很熟悉。這是是我國繼GB2312-1980和GB13000-1993之後最重要的漢字編碼標准，同時也是未來我國計算機系統必須遵循的基礎性標准之一。
  目前在中文Windows操作系統中，.Net編程中默認的的代碼頁就是GB18030簡體中文。但是事實上如果生成中文漢字驗證碼只須要使用GB2312字符集就已經足夠了。字符集中除了我們平時大家都認識的漢字外，也包含了很多我們不認識平時也很少見到的漢字。如果生成中文漢字驗證碼中有很多我們不認識的漢字讓我們輸入，對於使用拼音輸入法的朋友來說可不是好事，五筆使用者還能勉強根據漢字的長相打出來，呵呵！所以對於GB2312字符集中的漢字我們也不是全都要用。
  中文漢字字符可以使用區位碼來表示，見
  
  漢字區位碼表 http://navicy2005.home4u.china.com/resource/gb2312tbl.htm
  漢字區位碼代碼表 http://navicy2005.home4u.china.com/resource/gb2312tbm.htm
  
  其實這兩個表是同一回事，只不過一個使用十六進制分區表示，一個使用區位所在的數字位置表示。 例如“好”字的十六進制區位碼是ba c3，前兩位是區域，後兩位代表位置，ba處在第26區，“好”處在此區漢字的第35位也就是c3位置，所以數字代碼就是2635。這就是GB2312漢字區位原理。根據《漢字區位碼表 》我們可以發現第15區也就是AF區以前都沒有漢字，只有少量符號，漢字都從第16區B0開始，這就是為什麼GB2312字符集都是從16區開始的。
  
  2、.Net程序處理漢字編碼原理分析
  在.Net中可以使用System.Text來處理所有語言的編碼。在System.Text命名空間中包含眾多編碼的類，可供進行操作及轉換。其中的Encoding類就是重點處理漢字編碼的類。通過在.Net文檔中查詢Encoding類的方法我們可以發現所有和文字編碼有關的都是字節數組，其中有兩個很好用的方法：
    
  Encoding.GetBytes ()方法將指定的 String 或字符數組的全部或部分內容編碼為字節數組
  Encoding.GetString ()方法將指定字節數組解碼為字符串。
    
  沒錯我們可以通過這兩個方法將漢字字符編碼為字節數組，同樣知道了漢字GB2312的字節數組編碼也就可以將字節數組解碼為漢字字符。通過對“好”字進行編碼為字節數組後
    
  Encoding gb=Encoding.GetEncoding("gb2312");
  object[] bytes=gb.Encoding.GetBytes ("好")；
    
  發現得到了一個長度為2的字節數組bytes，使用
    
  string lowCode = System.Convert.ToString(bytes[0], 16); //取出元素1編碼內容（兩位16進制）
  string hightCode = System.Convert.ToString(bytes[1], 16);//取出元素2編碼內容（兩位16進制）
   
  之後發現字節數組bytes16進制變碼後內容竟然是{ba,c3}，剛好是“好”字的十六進制區位碼（見區位碼表）。
  因此我們就可以隨機生成一個長度為2的十六進制字節數組，使用GetString ()方法對其進行解碼就可以得到漢字字符了。不過對於生成中文漢字驗證碼來說，因為第15區也就是AF區以前都沒有漢字，只有少量符號，漢字都從第16區B0開始，並且從區位D7開始以後的漢字都是和很難見到的繁雜漢字，所以這些都要排出掉。所以隨機生成的漢字十六進制區位碼第1位范圍在B、C、D之間，如果第1位是D的話，第2位區位碼就不能是7以後的十六進制數。在來看看區位碼表發現每區的第一個位置和最後一個位置都是空的，沒有漢字，因此隨機生成的區位碼第3位如果是A的話，第4位就不能是0；第3位如果是F的話，第4位就不能是F。
  */

        private string GetRandomText21(int nLen)
        {
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //調用函數產生4個隨機中文漢字編碼
            object[] bytes = CreateRegionCode21(nLen);

            //根據漢字編碼的字節數組解碼出中文漢字
            string[] strs = new string[nLen];
            string randString = "";
            for (int i = 0; i < nLen; i++)
            {
                strs[i] = gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));
                randString += strs[i];
            }
            return randString;
        }
        /* 
        在.Net中可以使用System.Text來處理所有語言的編碼。在System.Text命名空間中包含眾多編碼的類，可供進行操作及轉換。其中的Encoding類就是重點處理漢字編碼的類。通過在.Net文檔中查詢Encoding類的方法我們可以發現所有和文字編碼有關的都是字節數組，其中有兩個很好用的方法：  
        Encoding.GetBytes ()方法將指定的 String 或字符數組的全部或部分內容編碼為字節數組  
        Encoding.GetString ()方法將指定字節數組解碼為字符串。  

        沒錯我們可以通過這兩個方法將漢字字符編碼為字節數組，同樣知道了漢字GB2312的字節數組編碼也就可以將字節數組解碼為漢字字符。通過對“好”字進行編碼為字節數組後  

        Encoding gb=Encoding.GetEncoding("gb2312");   
        object[] bytes=gb.Encoding.GetBytes ("好")；

        發現得到了一個長度為2的字節數組bytes，使用  

        string lowCode = System.Convert.ToString(bytes[0], 16); //取出元素1編碼內容（兩位16進制）   
        string hightCode = System.Convert.ToString(bytes[1], 16);//取出元素2編碼內容（兩位16進制）   

        之後發現字節數組bytes16進制變碼後內容竟然是{ba,c3}，剛好是“好”字的十六進制區位碼（見區位碼表）。  
        因此我們就可以隨機生成一個長度為2的十六進制字節數組，使用GetString ()方法對其進行解碼就可以得到漢字字符了。
         不過對於生成中文漢字驗證碼來說，因為第15區也就是AF區以前都沒有漢字，只有少量符號，漢字都從第16區B0開始，
         * 並且從區位D7開始以後的漢字都是和很難見到的繁雜漢字，所以這些都要排出掉。所以隨機生成的漢字十六進制區位碼第1位范圍在B、C、D之間，
         * 如果第1位是D的話，第2位區位碼就不能是7以後的十六進制數。在來看看區位碼表發現每區的第一個位置和最後一個位置都是空的，沒有漢字
        &nbs因此隨機生成的區位碼第3位如果是A的話，第4位就不能是0；第3位如果是F的話，第4位就不能是F。
        此函數在漢字編碼范圍內隨機創建含兩個元素的十六進制字節數組，每個字節數組代表一個漢字，並將   
        四個字節數組存儲在object數組中。   
        參數：strlength，代表需要產生的漢字個數   
        */
        public static object[] CreateRegionCode21(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素   
            string[] rBase = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };

            Random rnd = new Random();

            //定義一個object數組用來   
            object[] bytes = new object[strlength];

            /*每循環一次產生一個含兩個元素的十六進制字節數組，並將其放入bject數組中   
             每個漢字有四個區位碼組成   
             區位碼第1位和區位碼第2位作為字節數組第一個元素   
             區位碼第3位和區位碼第4位作為字節數組第二個元素   
            */
            for (int i = 0; i < strlength; i++)
            {
                //區位碼第1位   
                int r1 = rnd.Next(11, 14);
                string str_r1 = rBase[r1].Trim();

                //區位碼第2位   
                rnd = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子//更換隨機數發生器的  種子避免產生重復值   
                int r2;
                if (r1 == 13)
                {
                    r2 = rnd.Next(0, 7);
                }
                else
                {
                    r2 = rnd.Next(0, 16);
                }
                string str_r2 = rBase[r2].Trim();

                //區位碼第3位   
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r3 = rnd.Next(10, 16);
                string str_r3 = rBase[r3].Trim();

                //區位碼第4位   
                rnd = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r4;
                if (r3 == 10)
                {
                    r4 = rnd.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rnd.Next(0, 15);
                }
                else
                {
                    r4 = rnd.Next(0, 16);
                }
                string str_r4 = rBase[r4].Trim();

                //定義兩個字節變量存儲產生的隨機漢字區位碼   
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //將兩個字節變量存儲在字節數組中   
                byte[] str_r = new byte[] { byte1, byte2 };

                //將產生的一個漢字的字節數組放入object數組中   
                bytes.SetValue(str_r, i);
            }
            return bytes;
        }

        //------------------------------------------------------------  # 60個

        /* 
        此函数在汉字编码范围内随机创建含两个元素的十六进制字节数组，每个字节数组代表一个汉字，并将 
        四个字节数组存储在object数组中。 
        参数：strlength，代表需要产生的汉字个数 
        */
        public static object[] CreateCode20(int strlength)
        {
            //定义一个字符串数组储存汉字编码的组成元素 
            string[] r = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };
            Random rnd = new Random();
            //定义一个object数组用来 
            object[] bytes = new object[strlength];
            /*每循环一次产生一个含两个元素的十六进制字节数组，并将其放入bject数组中 
             每个汉字有四个区位码组成 
             区位码第1位和区位码第2位作为字节数组第一个元素 
             区位码第3位和区位码第4位作为字节数组第二个元素 
            */
            for (int i = 0; i < strlength; i++)
            {
                //区位码第1位 
                int r1 = rnd.Next(11, 14);
                string str_r1 = r[r1].Trim();
                //区位码第2位 
                rnd = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子//更换随机数发生器的种子避免产生重复值 
                int r2;
                if (r1 == 13)
                    r2 = rnd.Next(0, 7);
                else
                    r2 = rnd.Next(0, 16);
                string str_r2 = r[r2].Trim();
                //区位码第3位 
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r3 = rnd.Next(10, 16);
                string str_r3 = r[r3].Trim();
                //区位码第4位 
                rnd = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r4;
                if (r3 == 10)
                {
                    r4 = rnd.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rnd.Next(0, 15);
                }
                else
                {
                    r4 = rnd.Next(0, 16);
                }
                string str_r4 = r[r4].Trim();
                //定义两个字节变量存储产生的随机汉字区位码 
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //将两个字节变量存储在字节数组中 
                byte[] str_r = new byte[] { byte1, byte2 };
                //将产生的一个汉字的字节数组放入object数组中 
                bytes.SetValue(str_r, i);
            }
            return bytes;
        }

        private void bt_random3_Click(object sender, EventArgs e)
        {
            //隨機中文

            int nLen = 10;
            // 采用的字符集，可以隨即拓展，並可以控制字符出現的幾率
            string strCode = GetRandomText21(nLen);
            richTextBox1.Text += "取得 : " + strCode + "\n";

            //------------------------------------------------------------  # 60個

            //获取GB2312编码页（表） 
            Encoding gb = Encoding.GetEncoding("gb2312");
            //调用函数产生4个随机中文汉字编码 
            object[] bytes = CreateCode20(4);
            //根据汉字编码的字节数组解码出中文汉字 
            string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[0], typeof(byte[])));
            string str2 = gb.GetString((byte[])Convert.ChangeType(bytes[1], typeof(byte[])));
            string str3 = gb.GetString((byte[])Convert.ChangeType(bytes[2], typeof(byte[])));
            string str4 = gb.GetString((byte[])Convert.ChangeType(bytes[3], typeof(byte[])));
            string txt = str1 + str2 + str3 + str4;

            richTextBox1.Text += "取得 : " + txt + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_random4_Click(object sender, EventArgs e)
        {
            //C# 產生亂數的方式(Random)
            Random rand = new Random(); //加入Random，產生的數字不會重覆
            for (int i = 0; i < 20; i++)
            {
                richTextBox1.Text += rand.Next(10, 21).ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_random5_Click(object sender, EventArgs e)
        {
            Random rand = new Random();//亂數種子
            //int i = rand.Next(0, 100);//回傳0-99的亂數
            //如果用for 或其它回圈抓亂數，一定要把 Random 亂數 = new Random();//亂數種子 放在回圈外面。

            //Random rand = new Random();//亂數種子
            for (int i = 0; i < 100; i++)
            {
                int j = rand.Next(0, 100);
                richTextBox1.Text += j.ToString() + "  ";
            }
            richTextBox1.Text += "\n";

            /* dddd
            Random rand = new Random();
            int index = rand.Next(len);
            //richTextBox1.Text += index.ToString() + " ";
            //pictureBox2.BackColor = Colors[index % len];  //same
            */
        }

        //------------------------------------------------------------  # 60個

        private void bt_random6_Click(object sender, EventArgs e)
        {
            Random rand = new Random();

            for (int i = 0; i < 20; i++)
            {
                var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                var builder = new StringBuilder();
                int length = 5;
                for (int j = 0; j < length; j++)
                {
                    builder.Append(str[rand.Next(0, str.Length)]);
                }
                string name_string = builder.ToString();
                int score_chi = rand.Next(80, 100) + 1;
                int score_eng = rand.Next(70, 100) + 1;
                int score_math = rand.Next(60, 100) + 1;

                richTextBox1.Text += "Name : " + name_string + "\t" + score_chi.ToString() + "\t" + score_eng.ToString() + "\t" + score_math.ToString() + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        public static string GetRandomString3(int length)
        {
            //var str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var str = "ABCDE";
            var rand = new Random();
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[rand.Next(0, str.Length)]);
            }
            return builder.ToString();
        }

        private const int ROUND = 1000;
        int[] useless = new int[ROUND];

        public class MySearchInfo
        {
            public char c;
            public int cnt;
            public MySearchInfo(char c, int cc)
            {
                this.c = c;
                this.cnt = cc;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告searchinfos 為List
        // 以下List 裡為 MySearchInfo 型態
        List<MySearchInfo> result = new List<MySearchInfo>();
        private void bt_random7_Click(object sender, EventArgs e)
        {
            //隨機產生一些英文字母, 統計各種字母出現次數
            int i;
            int j;
            for (i = 0; i < ROUND; i++)
            {
                useless[i] = 0;
            }
            result.Clear();

            string str = GetRandomString3(ROUND);
            richTextBox1.Text += "產生任意字串 : " + str + "\n";

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += "取得字元 " + str[i] + "\n";
            }

            for (i = 0; i < ROUND; i++)
            {
                for (j = i + 1; j < ROUND; j++)
                {
                    if (useless[i] != -1)
                    {
                        //richTextBox1.Text += "compare i = " + i.ToString() + ", j = " + j.ToString() + "\n";
                        if (str[i] == str[j])
                        {
                            //richTextBox1.Text += "X";
                            useless[i]++;
                            useless[j] = -1;
                        }
                        else
                        {

                        }
                    }
                }
            }

            for (i = 0; i < ROUND; i++)
            {
                //richTextBox1.Text += useless[i].ToString() + " ";
                if (useless[i] != -1)
                {
                    //richTextBox1.Text += "found " + str[i] + " at i = " + i.ToString() + ", cnt = " + useless[i].ToString() + "\n";
                    result.Add(new MySearchInfo(str[i], (useless[i] + 1)));
                }
            }

            richTextBox1.Text += "結果:\n";
            for (i = 0; i < result.Count; i++)
            {
                richTextBox1.Text += "第 " + (i + 1).ToString() + " 種, 字元 : " + result[i].c.ToString() + ", 出現次數 : " + result[i].cnt.ToString() + ", 比例 : " + ((double)result[i].cnt * 100 / ROUND).ToString() + " %\n";
            }
        }

        private void bt_random8_Click(object sender, EventArgs e)
        {
            byte[] data = new byte[100];
            new Random().NextBytes(data);

            richTextBox1.Text += "亂數陣列內容:\n";
            for (int i = 0; i < data.Length; i++)
            {
                richTextBox1.Text += data[i].ToString();
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                {
                    richTextBox1.Text += " ";
                }
            }
            richTextBox1.Text += "\n";
        }

        private void bt_random9_Click(object sender, EventArgs e)
        {
            int i;
            int N = 30;
            // Make an array to hold the assignment.
            int[] aa = new int[N];
            for (i = 0; i < N; i++)
            {
                aa[i] = i;
            }
            richTextBox1.Text += "原陣列\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += aa[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //Randomize the array
            RandomizeArray(aa);
            richTextBox1.Text += "新陣列\n";
            for (i = 0; i < N; i++)
            {
                richTextBox1.Text += aa[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

        }

        //Randomize the array
        void RandomizeArray(int[] items)
        {
            Random rand = new Random();
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = rand.Next(i, items.Length);
                int temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        private void bt_random10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "整個string array都變成亂數陣列\n";
            int N = 10;

            string[] names = new string[N];
            names[0] = "AAA";
            names[1] = "BBB";
            names[2] = "CCC";
            names[3] = "DDD";
            names[4] = "EEE";
            names[5] = "FFF";
            names[6] = "GGG";
            names[7] = "HHH";
            names[8] = "III";
            names[9] = "JJJ";

            richTextBox1.Text += "原陣列\t";
            for (int i = 0; i < N; i++)
            {
                richTextBox1.Text += names[i] + " ";
            }
            richTextBox1.Text += "\n";

            // Randomize.
            //Randomizer.Randomize<string>(names);  //same
            Randomizer.Randomize(names);

            richTextBox1.Text += "新陣列\t";
            for (int i = 0; i < N; i++)
            {
                richTextBox1.Text += names[i] + " ";
            }
            richTextBox1.Text += "\n";

            int groups = 4;
            richTextBox1.Text += "分成 " + groups.ToString() + " 組\n";
            int groupNum = 0;
            for (int i = 0; i < N; i++)
            {
                richTextBox1.Text += "第 " + groupNum.ToString() + " 組\t" + names[i] + "\n";
                groupNum = ++groupNum % groups;
            }
        }

        //------------------------------------------------------------  # 60個

        // 隨機數生成器

        //Random初始化+種子
        Random rand = new Random(unchecked((int)DateTime.Now.Ticks));  // 使用亂數種子

        // 英文與數字串
        string EnglishOrNumChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // 生成英文或數字字符
        protected char CreateEnOrNumChar()
        {
            return EnglishOrNumChars[rand.Next(0, EnglishOrNumChars.Length)];
        }

        private void bt_random11_Click(object sender, EventArgs e)
        {
            // 生成隨機字符碼
            int codeLen = 10;

            char[] chs = new char[codeLen];

            for (int i = 0; i < codeLen; i++)
            {
                if (chs[i] == '\0')
                {
                    chs[i] = CreateEnOrNumChar();
                }
            }

            string code = new string(chs, 0, chs.Length);
            richTextBox1.Text += code + "\n";
        }

        //------------------------------------------------------------  # 60個

        //亂數方法比較 ST
        private void bt_random12_Click(object sender, EventArgs e)
        {
            int N = 20;
            int min = 1;
            int max = 100;
            int[] rand_numbers = new int[N];

            richTextBox1.Text += "N = " + N.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            richTextBox1.Text += "使用內建的Random()函數建立亂數資料\n";
            Random rand = new Random();
            for (int i = 0; i < N; i++)
            {
                rand_numbers[i] = rand.Next(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "使用RNGCryptoServiceProvider函數建立亂數資料\n";
            for (int i = 0; i < N; i++)
            {
                rand_numbers[i] = RandomInteger(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        // The random number provider.
        private RNGCryptoServiceProvider Rand = new RNGCryptoServiceProvider();

        // Return a random integer between a min and max value.
        private int RandomInteger(int min, int max)
        {
            uint scale = uint.MaxValue;
            while (scale == uint.MaxValue)
            {
                // Get four random bytes.
                byte[] four_bytes = new byte[4];
                Rand.GetBytes(four_bytes);

                // Convert that into an uint.
                scale = BitConverter.ToUInt32(four_bytes, 0);
            }
            // Add min to the scaled difference between max and min.
            return (int)(min + (max - min) * (scale / (double)uint.MaxValue));
        }
        //亂數方法比較 SP

        private void bt_random13_Click(object sender, EventArgs e)
        {
            //建立亂七八糟陣列
            byte[] dataArray = new byte[100];//字節

            new Random().NextBytes(dataArray);//創建隨機字節

            for (int i = 0; i < dataArray.Length; i++)
            {
                //sf.WriteByte(dataArray[i]);//將字節寫入文件理.
                richTextBox1.Text += dataArray[i].ToString() + " ";
            }
        }

        private void bt_random14_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗1

            int rand = 50;
            int recordx = this.Left;　//保存原來窗體的左上角的x坐標
            int recordy = this.Top;　//保存原來窗體的左上角的y坐標

            Random random = new Random();

            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }

                this.Left = recordx;　//還原原始窗體的左上角的x坐標
                this.Top = recordy;　//還原原始窗體的左上角的y坐標
            }
            this.WindowState = FormWindowState.Maximized;
        }

        private void bt_random15_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗2
            int rand = 10;
            int recordx = this.Left;
            int recordy = this.Top;

            Random random = new Random();

            for (int i = 0; i < 50; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }
                Thread.Sleep(1);
            }
            this.Left = recordx;
            this.Top = recordy;

            this.WindowState = FormWindowState.Maximized;
        }

        private void nudgeWindow()
        {
            // 記錄視窗舊位置
            int oldLeft = Left;
            int oldTop = Top;

            // 變動位置
            Random rand = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = rand.Next(Left - 20, Left + 20);
                Left = left;
                int top = rand.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }

        private void bt_random16_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗3
            nudgeWindow();
            this.WindowState = FormWindowState.Maximized;
        }

        private void bt_random17_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            //來電震動視窗4
            Point now_p = this.Location;

            Random rand = new Random();

            for (int i = 0; i < 50; i++)
            {
                Point new_p = new Point(now_p.X + rand.Next(-10, 10), now_p.Y + rand.Next(-10, 10)); //新的位置
                this.Location = new_p;
                System.Threading.Thread.Sleep(20);
                this.Location = now_p; //還原位置
            }
            this.WindowState = FormWindowState.Maximized;
        }

        private Color[] Colors = new Color[]
        {
            Color.AliceBlue,
            Color.AntiqueWhite,
            Color.Aqua,
            Color.Aquamarine,
            Color.Azure,
            Color.Beige,
            Color.Bisque,

            Color.Black,
            Color.BlanchedAlmond,
            Color.Blue,
            Color.BlueViolet,
            Color.Brown,
            Color.BurlyWood,
            Color.CadetBlue,

            Color.Chartreuse,
            Color.Chocolate,
            Color.Coral,
            Color.CornflowerBlue,
            Color.Cornsilk,
            Color.Crimson,
            Color.Cyan,

            Color.DarkBlue,
            Color.DarkCyan,
            Color.DarkGoldenrod,
            Color.DarkGray,
            Color.DarkGreen,
            Color.DarkKhaki,
            Color.DarkMagenta,

            Color.DarkOliveGreen,
            Color.DarkOrange,
            Color.DarkOrchid,
            Color.DarkRed,
            Color.DarkSalmon,
            Color.DarkSeaGreen,
            Color.DarkSlateBlue,

            Color.DarkSlateGray,
            Color.DarkTurquoise,
            Color.DarkViolet,
            Color.DeepPink,
            Color.DeepSkyBlue,
            Color.DimGray,
            Color.DodgerBlue,

            Color.Firebrick,
            Color.FloralWhite,
            Color.ForestGreen,
            Color.Fuchsia,
            Color.Gainsboro,
            Color.GhostWhite,
            Color.Gold,

            Color.Goldenrod,
            Color.Gray,
            Color.Green,
            Color.GreenYellow,
            Color.Honeydew,
            Color.HotPink,
            Color.IndianRed,

            Color.Indigo,
            Color.Ivory,
            Color.Khaki,
            Color.Lavender,
            Color.LavenderBlush,
            Color.LawnGreen,
            Color.LemonChiffon,

            Color.LightBlue,
            Color.LightCoral,
            Color.LightCyan,
            Color.LightGoldenrodYellow,
            Color.LightGreen,
            Color.LightGray,
            Color.LightPink,

            Color.LightSalmon,
            Color.LightSeaGreen,
            Color.LightSkyBlue,
            Color.LightSlateGray,
            Color.LightSteelBlue,
            Color.LightYellow,
            Color.Lime,

            Color.LimeGreen,
            Color.Linen,
            Color.Magenta,
            Color.Maroon,
            Color.MediumAquamarine,
            Color.MediumBlue,
            Color.MediumOrchid,

            Color.MediumPurple,
            Color.MediumSeaGreen,
            Color.MediumSlateBlue,
            Color.MediumSpringGreen,
            Color.MediumTurquoise,
            Color.MediumVioletRed,
            Color.MidnightBlue,

            Color.MintCream,
            Color.MistyRose,
            Color.Moccasin,
            Color.NavajoWhite,
            Color.Navy,
            Color.OldLace,
            Color.Olive,

            Color.OliveDrab,
            Color.Orange,
            Color.OrangeRed,
            Color.Orchid,
            Color.PaleGoldenrod,
            Color.PaleGreen,
            Color.PaleTurquoise,

            Color.PaleVioletRed,
            Color.PapayaWhip,
            Color.PeachPuff,
            Color.Peru,
            Color.Pink,
            Color.Plum,
            Color.PowderBlue,

            Color.Purple,
            Color.Red,
            Color.RosyBrown,
            Color.RoyalBlue,
            Color.SaddleBrown,
            Color.Salmon,
            Color.SandyBrown,

            Color.SeaGreen,
            Color.SeaShell,
            Color.Sienna,
            Color.Silver,
            Color.SkyBlue,
            Color.SlateBlue,
            Color.SlateGray,

            Color.Snow,
            Color.SpringGreen,
            Color.SteelBlue,
            Color.Tan,
            Color.Teal,
            Color.Thistle,
            Color.Tomato,

            Color.Turquoise,
            Color.Violet,
            Color.Wheat,
            Color.White,
            Color.WhiteSmoke,
            Color.Yellow,
            Color.YellowGreen,
        };

        private Random random = new Random();

        private Color GetRandomColor2()
        {
            return Colors[random.Next(0, Colors.Length)];
        }

        //隨機顏色如下
        public static Color GetRandomColor5()
        {
            //Random初始化+種子
            Random rand1 = new Random((int)DateTime.Now.Ticks);  // 使用亂數種子

            System.Threading.Thread.Sleep(300);

            //Random初始化+種子
            Random rand2 = new Random((int)DateTime.Now.Ticks);  // 使用亂數種子

            System.Threading.Thread.Sleep(300);

            //Random初始化+種子
            Random rand3 = new Random((int)DateTime.Now.Ticks);  // 使用亂數種子

            int R = rand1.Next(256);
            int G = rand2.Next(256);
            int B = rand3.Next(256);

            return Color.FromArgb(R, G, B);
        }

        // 顏色模板
        //  黑、白、紅、綠、藍、黃/ 棕 、灰
        private const int BLACK = 0;
        private const int WHITE = 1;
        private const int RED1 = 2;
        private const int RED2 = 3;
        private const int GREEN1 = 4;
        private const int GREEN2 = 5;
        private const int BLUE1 = 6;
        private const int BLUE2 = 7;
        private const int YELLOW1 = 8;
        private const int YELLOW2 = 9;
        private const int BROWN = 10;
        private const int GRAY = 11;

        void show_random_color()
        {
            //顯示顏色
            int[,] colorVelue = null;
            colorVelue = new int[,] {
            {50,50,50},    //黑
            {255,255,255},  //白
            {240,80,80}, //紅小
            {240,160,160},  //紅大
            {60,180,60}, //綠小
            {160,240,160},  //綠大
            {80,80,240}, //藍小
            {160,160,240},  //藍大
            {240,190,80}, //黃小
            {240,240,160},  //黃大
            {205,133,63},   //棕/褐
            //{162,162,162},//灰，特殊
            };

            int total_colors = colorVelue.GetUpperBound(0) + 1;
            //richTextBox1.Text += "total_colors = " + total_colors.ToString() + "\n";

            Random rand = new Random();
            int sel = rand.Next(total_colors);
            /*
            switch (sel)
            {
                case -1:
                    richTextBox1.Text += "無此色\n";
                    break;
                case 0:
                    richTextBox1.Text += "黑\n";
                    break;
                case 1:
                    richTextBox1.Text += "白\n";
                    break;
                case 2:
                    richTextBox1.Text += "紅\n";
                    break;
                case 3:
                    richTextBox1.Text += "紅\n";
                    break;
                case 4:
                    richTextBox1.Text += "綠\n";
                    break;
                case 5:
                    richTextBox1.Text += "綠\n";
                    break;
                case 6:
                    richTextBox1.Text += "藍\n";
                    break;
                case 7:
                    richTextBox1.Text += "藍\n";
                    break;
                case 8:
                    richTextBox1.Text += "黃\n";
                    break;
                case 9:
                    richTextBox1.Text += "黃\n";
                    break;
                case 10:
                    richTextBox1.Text += "棕\n";
                    break;
                case 11:
                    richTextBox1.Text += "灰\n";
                    break;
                default:
                    richTextBox1.Text += "其他\n";
                    break;
            }
            */
            int R = colorVelue[sel, 0];
            int G = colorVelue[sel, 1];
            int B = colorVelue[sel, 2];
            //richTextBox1.Text += "show color " + sel.ToString() + " " + R.ToString() + " " + G.ToString() + " " + B.ToString() + "\n";

            pictureBox4.BackColor = Color.FromArgb(R, G, B);
        }

        // 產生隨機二維陣列
        private int[,] Values =
        {
            {1, 2, 3, 4, 5},
            {6, 7, 8, 9, 10},
            {11, 12, 13, 14, 15},
            {16, 17, 18, 19, 20},
        };

        private void timer1_Tick(object sender, EventArgs e)
        {
            //製作random color的方法
            int len = Colors.Length;

            pictureBox2.BackColor = GetRandomColor2();          //same

            Random rd = new Random();
            pictureBox3.BackColor = Color.FromArgb((byte)rd.Next(0, 255), (byte)rd.Next(0, 255), (byte)rd.Next(0, 255));

            show_random_color();

            pictureBox5.BackColor = GetRandomColor5();

            tb_random_text0.Text = RandomText0();
            tb_random_text1.Text = RandomText1();
            tb_random_text2.Text = RandomText2();
            tb_random_text5.Text = RandomText5(10);
            tb_random_text6.Text = RandomText6(10);
            tb_random_text7.Text = RandomText7();
            tb_random_text8.Text = RandomText8();
            tb_random_text9.Text = RandomText9();
            tb_random_text10.Text = RandomText10();
            tb_random_text11.Text = RandomText11();

            string result = string.Empty;
            /*
            //任意中文字, 有點問題
            int lower = 0x20;
            int upper = 0xD7FF;

            result = NextString(lower, upper, 4);
            richTextBox1.Text += result + "\n";
            */

            //亂數產生Unicode中文範圍的中文字元
            //呼叫視窗使用Unicode字串來顯示
            Console.OutputEncoding = System.Text.Encoding.Unicode;
            //產生1000字Unicode中文字
            tb_random_text3.Text = "";
            for (int i = 0; i < 4; i++)
            {
                tb_random_text3.Text += getRandomUnicode().Substring(0, 1);
            }

            result = VerficationText(10);
            tb_random_text4.Text = result;

            // 產生隨機二維陣列
            Values.Randomize2();
            this.pictureBox1.Refresh();
        }

        /// <summary>  
        /// 獲取驗證碼【字符串】  
        /// </summary>  
        /// <param name="Length">驗證碼長度【必須大於0】</param>  
        /// <returns></returns>  
        public static string VerficationText(int Length)
        {
            char[] _verfication = new char[Length];
            Random _random = new Random();
            char[] _dictionary = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };
            for (int i = 0; i < Length; i++)
            {
                _verfication[i] = _dictionary[_random.Next(_dictionary.Length - 1)];
            }
            return new string(_verfication);
        }

        public string NextString(int charLowerBound, int charUpperBound, int length)
        {
            Random rand = new Random();
            return new String(Enumerable.Repeat(0, length).Select(p => (char)rand.Next(charLowerBound, charUpperBound)).ToArray());
        }

        //取得一個亂數的Unicode中文字
        private static string getRandomUnicode()
        {
            //Unicode中文字範圍
            int iMin = Convert.ToInt32("4E00", 16);
            int iMax = Convert.ToInt32("9FFF", 16); //不考慮最末16個空白
            //隨機一個中文字之整數
            System.Random oRnd = new System.Random(System.Guid.NewGuid().GetHashCode());
            int iChar = oRnd.Next(iMin, iMax);
            //整數轉成Byte[]，再轉成字串
            return System.Text.Encoding.Unicode.GetString(System.BitConverter.GetBytes(iChar));
        }

        // Draw the values.
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int num_rows = Values.GetUpperBound(0) + 1;
            int num_cols = Values.GetUpperBound(1) + 1;
            int col_wid = this.pictureBox1.ClientSize.Width / num_cols;
            int row_hgt = this.pictureBox1.ClientSize.Height / num_rows;

            e.Graphics.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            Font f = new Font("Times New Roman", 20);
            StringFormat string_format = new StringFormat();
            string_format.Alignment = StringAlignment.Center;
            string_format.LineAlignment = StringAlignment.Center;
            int y = 0;
            for (int row = 0; row < num_rows; row++)
            {
                int x = 0;
                for (int col = 0; col < num_cols; col++)
                {
                    Rectangle rect = new Rectangle(x, y, col_wid, row_hgt);
                    e.Graphics.DrawString(Values[row, col].ToString(), f, Brushes.Blue, rect, string_format);
                    x += col_wid;
                }
                y += row_hgt;
            }
        }

        private string GenCode(int num)
        {
            //string str = "的一是在不123456789了Q有和人這Q中大為W上個國我以要他時來E用ASDFGHJKLIUYTREWQZXCVBNM3們生到作地R於出就分對成會可主發年動同工也能下2過子2說產43種ASDFGHJKLIUYTREWQZXCVBNM3面而方後多定行學法0所民得經十三之進著等部度sASDFGHJKLIUYTREWQZXCVBNM3家電力裡如水化高自二k123456789q加量都兩體制機9當使點從業1本去把性3好應開它E合R還因由其D些然前外天政ASDFGHJKLIUYTREWQZXCVBNM3W四日那社E義事平SWQ形RFE相a全h表間樣與關j各重新線內數正心反8你明l看原又麼z利比或T但質123456789氣第4向道命W3此變43條只DF沒結0S解a問A意建8月公0無7系軍很情AUF者4W最立代想D1已L通G並提7g直4L34題H黨123456789程展五U3果料U象員革4位入常文2總次品式活設U及AY管A特件長求w老頭基資5邊流2路F級S少圖3山統接知5TK較S將0組3見計F別她手5角期b根0論ASDFGHJKLIUYTREWQZXCVBNM3油思s術極交受U123456789聯20什認六共S權F收asdecvrrtfghujnmkiolpz證改F清D己美4再采轉更7單SD風5切U8打白J2教速花帶安IM場123456789身車J例真務具萬每目至達G走積r,示345議聲U報N斗完類0八離ASDFGHJKLIUYTREWQ123456789ZXCVBNM3華名確A才SS科張CDXG信U馬節話XZ米U整空Z元Y況D今集a溫傳土許步pGBY群廣J石記asdecvrrtfghujnmk123456789iolpz需段H4研界拉J林律叫K且究O觀越H織K6裝U影casdecvr123456789rtfghujnmkiolpzL算低持v音眾o3書t布A復TV容兒8際商Z非驗連斷HJ深難近礦千周委素M技備半辦V青VT5省PD列n習響B約s支般史d感I勞便團9往5酸歷市克何除消構府u稱太准精值號Zi率族G維XB劃選標C寫存候毛3親快2效M斯Masdecvrrtfghujnmkiolpz3院C查江4型眼5王4B按格5養N易5置M派5層片U始C卻專狀育7廠U京asdecvrrtfghujnmkiolpz識7適屬圓8包火住調m滿縣局7照參紅細引聽該鐵價嚴";
            string str = "123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ";//去掉的O容易混淆的字母
            char[] chastr = str.ToCharArray();
            // string[] source ={ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "#", "$", "%", "&", "@" };
            string code = "";
            Random rd = new Random();
            for (int i = 0; i < num; i++)
            {
                //code += source[rd.Next(0, source.Length)];
                code += str.Substring(rd.Next(0, str.Length), 1);
            }
            return code;
        }

        //生成大量隨機碼 ST
        private void bt_random18_Click(object sender, EventArgs e)
        {
            //生成大量隨機碼
            StreamWriter swriter = new StreamWriter("1.txt", true);
            for (int i = 0; i < 100; i++)
            {
                swriter.Write(generateRandomString(20));
                swriter.WriteLine();
                Console.WriteLine("Number: {0}", i);
            }
            swriter.Flush();
            swriter.Close();
        }

        static Random random2 = new Random();
        static string generateRandomString(int length)
        {
            var chars = "ABCDEFGHIJKLMNPQRSTUVWXYZ123456789";
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < length; i++)
            {
                int index = random2.Next(chars.Length);
                result.Append(chars[index]);
            }
            return result.ToString();
        }
        //生成大量隨機碼 SP

        //批量生成隨機密碼, 存檔 ST
        private void bt_random19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "批量生成隨機密碼，必須包含數字和字母，並用加密算法加密\n";

            //批量生成隨機密碼, 存檔

            //批量生成隨機密碼，必須包含數字和字母，並用加密算法加密
            /*
            要求：密碼必須包含數字和字母
            思路：
            1.列出數字和字符。 組成字符串 ：chars
            2.利用randrom.Next(int i)返回一個小於所指定最大值的非負隨機數。
            3. 隨機取不小於chars長度的隨機數a,取字符串chars的第a位字符。
            4.循環 8次，得到8位密碼
            5.循環N次，批量得到密碼。
            */

            string chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            //Random初始化+種子
            Random randrom = new Random((int)DateTime.Now.Ticks);  // 使用亂數種子
            string filename = "tmp_pwd.txt";

            for (int j = 0; j < 1000; j++)
            {
                string str = "";
                for (int i = 0; i < 8; i++)
                {
                    str += chars[randrom.Next(chars.Length)];//randrom.Next(int i)返回一個小於所指定最大值的非負隨機數
                }
                if (IsNumber(str))//判斷是否全是數字
                {
                    continue;
                }
                if (IsLetter(str))//判斷是否全是字母
                {
                    continue;
                }
                File.AppendAllText(filename, str);
                string pws = Md5(str, 32);//MD5加密
                File.AppendAllText(filename, "," + pws + "\r\n");
            }

            richTextBox1.Text += "完成\n";
        }

        //判斷是否全是數字
        static bool IsNumber(string str)
        {
            if (str.Trim("0123456789".ToCharArray()) == "")
            {
                return true;
            }
            return false;
        }

        //判斷是否全是字母
        static bool IsLetter(string str)
        {
            if (str.Trim("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".ToCharArray()) == "")
            {
                return true;
            }
            return false;
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="str">加密字元</param>
        /// <param name="code">加密位數16/32</param>
        /// <returns></returns>
        public static string Md5(string str, int code)
        {
            string strEncrypt = string.Empty;

            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] fromData = Encoding.GetEncoding("GB2312").GetBytes(str);
            byte[] targetData = md5.ComputeHash(fromData);
            for (int i = 0; i < targetData.Length; i++)
            {
                strEncrypt += targetData[i].ToString("X2");
            }
            if (code == 16)
            {
                strEncrypt = strEncrypt.Substring(8, 16);
            }
            return strEncrypt;
        }
        //批量生成隨機密碼, 存檔 SP

        private void btnPick_Click(object sender, EventArgs e)
        {
            // Pick a random line from the TextBox.
            txtResult.Text = txtNames.Lines.PickRandom();
        }

        private void button31_Click(object sender, EventArgs e)
        {
            // Pick some items.
            int num_values = 5;
            txtResult.Lines = txtNames.Lines.PickRandom(num_values).ToArray();
        }

        //任意陣列
        private void btnRandomize_Click(object sender, EventArgs e)
        {
            RandomizeLists();
        }

        private void RandomizeLists()
        {
            ItemArray.Randomize();
            ItemList.Randomize();

            // Redisplay the values.
            lstArray.DataSource = null;
            lstArray.DataSource = ItemArray;
            lstList.DataSource = null;
            lstList.DataSource = ItemList;
        }

        //RandomText ST

        //--- RandomText0 --- ST

        private string RandomText0()
        {
            //取得任意字串
            int len = 20;
            string random_pattern = CreateAndCheckCode(real_random, len);
            return random_pattern;
        }

        //Random初始化+種子
        Random real_random = new Random(~unchecked((int)DateTime.Now.Ticks));  // 使用亂數種子

        private string CreateAndCheckCode(Random random, int length) // code 激活碼前綴
        {
            //char[] Pattern = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
            char[] Pattern = new char[] { '1', '2', '3', 'A', 'B', 'C' };
            string result = string.Empty;
            int n = Pattern.Length;
            for (int i = 0; i < length; i++)
            {
                int rand = random.Next(0, n);
                result += Pattern[rand];
            }
            return result;
        }
        //--- RandomText0 --- SP


        //--- RandomText1 --- ST
        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼
        /*
        此函數在漢字編碼范圍內隨機創建含兩個元素的十六進制字節數組，每個字節數組代表一個漢字，並將
        四個字節數組存儲在object數組中。
        參數：strlength，代表需要產生的漢字個數
        */
        public static object[] CreateRegionCode(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素
            string[] r = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };

            Random rand = new Random();

            //定義一個object數組用來
            object[] bytes = new object[strlength];

            /*
            每循環一次產生一個含兩個元素的十六進制字節數組，並將其放入bject數組中
            每個漢字有四個區位碼組成
            區位碼第1位和區位碼第2位作為字節數組第一個元素
            區位碼第3位和區位碼第4位作為字節數組第二個元素
            */
            for (int i = 0; i < strlength; i++)
            {
                //區位碼第1位
                int r1 = rand.Next(11, 14);
                string str_r1 = r[r1].Trim();

                //區位碼第2位
                //Random初始化+種子
                rand = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子//更換隨機數發生器的種子避免產生重復值
                int r2;
                if (r1 == 13)
                {
                    r2 = rand.Next(0, 7);
                }
                else
                {
                    r2 = rand.Next(0, 16);
                }
                string str_r2 = r[r2].Trim();

                //區位碼第3位
                //Random初始化+種子
                rand = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r3 = rand.Next(10, 16);
                string str_r3 = r[r3].Trim();

                //區位碼第4位
                //Random初始化+種子
                rand = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r4;
                if (r3 == 10)
                {
                    r4 = rand.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rand.Next(0, 15);
                }
                else
                {
                    r4 = rand.Next(0, 16);
                }
                string str_r4 = r[r4].Trim();

                //定義兩個字節變量存儲產生的隨機漢字區位碼
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //將兩個字節變量存儲在字節數組中
                byte[] str_r = new byte[] { byte1, byte2 };

                //將產生的一個漢字的字節數組放入object數組中
                bytes.SetValue(str_r, i);
            }
            return bytes;
        }

        private string RandomText1()
        {
            //產生隨機漢字
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //int len = 20;
            //調用函數產生隨機中文漢字編碼
            object[] bytes = CreateRegionCode(4);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[0], typeof(byte[])));
            string str2 = gb.GetString((byte[])Convert.ChangeType(bytes[1], typeof(byte[])));
            string str3 = gb.GetString((byte[])Convert.ChangeType(bytes[2], typeof(byte[])));
            string str4 = gb.GetString((byte[])Convert.ChangeType(bytes[3], typeof(byte[])));
            string txt = str1 + str2 + str3 + str4;
            return "隨機文字 : " + txt;
        }
        //--- RandomText1 --- SP

        //--- RandomText2 --- ST
        private string RandomText2()
        {
            //產生隨機字串
            int len = 10;
            return GenCode(len);
        }
        //--- RandomText2 --- SP

        //--- RandomText3 --- ST

        //--- RandomText3 --- SP

        //--- RandomText4 --- ST

        //--- RandomText4 --- SP

        //--- RandomText5 --- ST

        //隨機生成漢字（摘錄保存的代碼），生成漢字摘錄代碼
        /// <summary>
        /// 隨機生成漢字
        /// </summary>
        /// <param name="strlength">長度（4位）</param>
        /// <returns></returns>
        public string RandomText5(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素
            string[] r = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };
            Random rand = new Random();
            //定義一個object數組用來
            object[] bytes = new object[strlength];
            /**/
            /*每循環一次產生一個含兩個元素的十六進制字節數組，並將其放入bject數組中
            每個漢字有四個區位碼組成
            區位碼第1位和區位碼第2位作為字節數組第一個元素
            區位碼第3位和區位碼第4位作為字節數組第二個元素
            */
            for (int i = 0; i < strlength; i++)
            {
                //區位碼第1位
                int r1 = rand.Next(11, 14);
                string str_r1 = r[r1].Trim();
                //區位碼第2位
                //Random初始化+種子
                rand = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子//更換隨機數發生器的種子避免產生重復值
                int r2;
                if (r1 == 13)
                {
                    r2 = rand.Next(0, 7);
                }
                else
                {
                    r2 = rand.Next(0, 16);
                }
                string str_r2 = r[r2].Trim();
                //區位碼第3位
                //Random初始化+種子
                rand = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r3 = rand.Next(10, 16);
                string str_r3 = r[r3].Trim();
                //區位碼第4位
                //Random初始化+種子
                rand = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子
                int r4;
                if (r3 == 10)
                {
                    r4 = rand.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rand.Next(0, 15);
                }
                else
                {
                    r4 = rand.Next(0, 16);
                }
                string str_r4 = r[r4].Trim();
                //定義兩個字節變量存儲產生的隨機漢字區位碼
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //將兩個字節變量存儲在字節數組中
                byte[] str_r = new byte[] { byte1, byte2 };
                //將產生的一個漢字的字節數組放入object數組中
                bytes.SetValue(str_r, i);
            }

            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //根據漢字編碼的字節數組解碼出中文漢字

            string txt = string.Empty;

            for (int i = 0; i < strlength; i++)
            {
                string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));
                txt += str1;
            }
            return txt;
        }
        //--- RandomText5 --- SP


        //--- RandomText6 --- ST
        public string RandomText6(int len)
        {
            //產生隨機漢字
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //調用函數產生隨機中文漢字編碼
            object[] bytes = CreateRegionCode2(len);

            //根據漢字編碼的字節數組解碼出中文漢字
            string str = string.Empty;
            for (int i = 0; i < len; i++)
            {
                str += gb.GetString((byte[])Convert.ChangeType(bytes[i], typeof(byte[])));
            }
            return str;
        }

        /*
        此函數在漢字編碼范圍內隨機創建含兩個元素的十六進制字節數組，每個字節數組代表一個漢字，並將
        四個字節數組存儲在object數組中。
        參數：strlength，代表需要產生的漢字個數
        */
        public static object[] CreateRegionCode2(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素
            string[] rBase = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };

            Random rand = new Random();

            //定義一個object數組用來
            object[] bytes = new object[strlength];

            /*
            每循環一次產生一個含兩個元素的十六進制字節數組，並將其放入bject數組中
            每個漢字有四個區位碼組成
            區位碼第1位和區位碼第2位作為字節數組第一個元素
            區位碼第3位和區位碼第4位作為字節數組第二個元素
            */

            for (int i = 0; i < strlength; i++)
            {
                //區位碼第1位
                int r1 = rand.Next(11, 14);
                string str_r1 = rBase[r1].Trim();

                //區位碼第2位

                //Random初始化+種子
                rand = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子//更換隨機數發生器的種子避免產生重復值

                int r2;
                if (r1 == 13)
                {
                    r2 = rand.Next(0, 7);
                }
                else
                {
                    r2 = rand.Next(0, 16);
                }
                string str_r2 = rBase[r2].Trim();

                //區位碼第3位
                //Random初始化+種子
                rand = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子

                int r3 = rand.Next(10, 16);
                string str_r3 = rBase[r3].Trim();

                //區位碼第4位
                //Random初始化+種子
                rand = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);  // 使用亂數種子

                int r4;
                if (r3 == 10)
                {
                    r4 = rand.Next(1, 16);
                }
                else if (r3 == 15)
                {
                    r4 = rand.Next(0, 15);
                }
                else
                {
                    r4 = rand.Next(0, 16);
                }
                string str_r4 = rBase[r4].Trim();

                //定義兩個字節變量存儲產生的隨機漢字區位碼
                byte byte1 = Convert.ToByte(str_r1 + str_r2, 16);
                byte byte2 = Convert.ToByte(str_r3 + str_r4, 16);
                //將兩個字節變量存儲在字節數組中
                byte[] str_r = new byte[] { byte1, byte2 };

                //將產生的一個漢字的字節數組放入object數組中
                bytes.SetValue(str_r, i);
            }
            return bytes;
        }
        //--- RandomText6 --- SP

        //--- RandomText7 --- ST
        private string RandomText7()
        {
            string random_string = GetRandomString(16);
            return random_string;
        }

        public static string GetRandomString(int length)
        {
            var str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
            var rand = new Random();
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[rand.Next(0, str.Length)]);
            }
            return builder.ToString();
        }
        //--- RandomText7 --- SP


        //--- RandomText8 --- ST
        private string RandomText8()
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.

            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[8];
            var random = new Random();
            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }
            var finalString = new String(stringChars);

            return finalString;
        }
        //--- RandomText8 --- SP

        //--- RandomText9 --- ST
        private string RandomText9()
        {
            //隨機生成四位驗證碼（0~9，a~Z）
            int LEN = 4;
            Random r = new Random();
            string code = "0123456789abcdefghjklmnopqistuvwxyzABCDEFGHIJKLMNOPQISTUVWXYZ";
            string captcha = "";
            for (int i = 0; i < LEN; i++)
            {
                int ra = r.Next(code.Length);
                captcha = code.Substring(ra, 1) + captcha;
            }
            //richTextBox1.Text += captcha + "\n";
            return captcha;
        }
        //--- RandomText9 --- SP

        //--- RandomText10 --- ST
        private string RandomText10()
        {
            // Make the random words.
            // Get the number of words and letters per word.
            int num_letters = 10;

            // Make an array of the letters we will use.
            char[] letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();

            // Make a random number generator.
            Random rand = new Random();

            // Make a word.
            string word = "";
            for (int j = 1; j <= num_letters; j++)
            {
                // Pick a random number between 0 and 25
                // to select a letter from the letters array.
                int letter_num = rand.Next(0, letters.Length - 1);

                // Append the letter.
                word += letters[letter_num];
            }
            return word;
        }
        //--- RandomText10 --- SP

        //--- RandomText11 --- ST
        private string RandomText11()
        {
            //生成隨機字符串
            string random_str = RandomStringGenerator.GetRandomString();
            return random_str;
        }

        /// <summary> 
        /// 生成隨機字符串
        /// </summary> 
        private class RandomStringGenerator
        {
            static readonly Random r = new Random();
            const string _chars = "0123456789";
            public static string GetRandomString()
            {
                char[] buffer = new char[5];
                for (int i = 0; i < 5; i++)
                {
                    buffer[i] = _chars[r.Next(_chars.Length)];
                }
                return new string(buffer);
            }
        }
        //--- RandomText11 --- SP

        //RandomText SP

        //------------------------------------------------------------  # 60個

        private string GetCaptchaCode01(int length)
        {
            char[] oCharacter = {'0','1','2','3','4','5','6','7','8','9',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            //'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            };

            string captcha_text = String.Empty;
            Random rand = new Random(DateTime.Now.Millisecond);
            for (int i = 0; i < length; i++)
            {
                captcha_text += oCharacter[rand.Next(oCharacter.Length)];

                //純數字
                //int number;
                //number = rand.Next(10);
                //number = oCharacter[rand.Next(oCharacter.Length)];
                //captcha_text += number.ToString();
            }
            return captcha_text;
        }

        //------------------------------------------------------------  # 60個

        // 產生指定個數的隨機字符串
        private string GetCaptchaCode02(int length)
        {
            string captcha_code = string.Empty;
            Random rand = new Random(); //創建隨機數對象
            //產生由 charNum 個字母或數字組成的一個字符串
            string str = "abcdefghijkmnpqrstuvwyzABCDEFGHJKLMNPQRSTUVWYZ23456789隨機數對象"; //共59個字符，除 l,o,x,I,O,X,1,0 的所有數字和大寫字母
            for (int i = 0; i < length; i++)
            {
                captcha_code = captcha_code + str.Substring(rand.Next(59), 1);//返回0到58共59個
            }
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        private string GetCaptchaCode03(int length)
        {
            //產生五位的隨機字符串
            int number;
            char code;
            string captcha_code = String.Empty;

            Random rand = new Random();

            for (int i = 0; i < length; i++)
            {
                number = rand.Next();

                if (number % 2 == 0)
                {
                    code = (char)('0' + (char)(number % 10));
                }
                else
                {
                    code = (char)('a' + (char)(number % 26));
                }
                captcha_code += code.ToString();
            }
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        // 生成隨機字符串
        public string GetCaptchaCode04(int length)
        {
            Random rand = new Random();

            String charCollection = "2,3,4,5,6,7,8,9,a,s,d,f,g,h,z,c,v,b,n,m,k,q,w,e,r,t,y,u,p,A,S,D,F,G,H,Z,C,V,B,N,M,K,Q,W,E,R,T,Y,U,P"; //定義驗證碼字符及出現頻次 ,避免出現0 o j i l 1 x;  
            // 隨機字符串列表，請使用英文狀態下的逗號分隔

            string[] randomArray = charCollection.Split(','); //將字符串生成數組     
            int arrayLength = randomArray.Length;
            string captcha_code = "";
            for (int i = 0; i < length; i++)
            {
                captcha_code += randomArray[rand.Next(0, arrayLength)];
            }
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        // 該方法用於生成指定位數的隨機數
        /// <param name="VcodeNum">參數是隨機數的位數</param>
        /// <returns>返回一個隨機數字符串</returns>
        private string GetCaptchaCode05(int length)
        {
            string Vchar = "1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R,S,T,U,V,W,X,Y,Z";
            string[] VcArray = Vchar.Split(new Char[] { ',' });//拆分成陣列
            string VNum = "";//產生的隨機數
            int temp = -1;//記錄上次隨機數值，盡量避免生產幾個一樣的隨機數
            Random rand = new Random();
            for (int i = 1; i < length + 1; i++)
            {
                if (temp != -1)
                {
                    rand = new Random(i * temp * unchecked((int)DateTime.Now.Ticks));
                }
                int t = rand.Next(33);
                if (temp != -1 && temp == t)
                {
                    return GetCaptchaCode05(length);
                }
                temp = t;
                VNum += VcArray[t];
            }
            return VNum;
        }

        //------------------------------------------------------------  # 60個

        public enum RandomGeneratorStyle
        {
            //  純數字
            Number,
            //  數字+大小寫英文
            NumberAndChar,
            //  數字+大寫英文
            NumberAndCharIgnoreCase
        }

        public static string GetCaptchaCode06(RandomGeneratorStyle style, int length)
        {
            string captcha_text = "";
            Random rand = new Random();
            string strValidateStringSource;
            switch (style)
            {
                case RandomGeneratorStyle.Number:  // 純數字
                    strValidateStringSource = "0123456789";
                    break;
                case RandomGeneratorStyle.NumberAndChar:  // 數字+大小寫英文
                    strValidateStringSource = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    break;
                case RandomGeneratorStyle.NumberAndCharIgnoreCase:  //  數字+大寫英文
                    strValidateStringSource = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                    break;
                default:
                    strValidateStringSource = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    break;
            }
            for (int i = 0; i < length; i++)
            {
                captcha_text += strValidateStringSource[rand.Next(strValidateStringSource.Length - 1)];
            }
            return captcha_text;
        }

        //------------------------------------------------------------  # 60個

        private string GetCaptchaCode07(int length)
        {
            //定義要隨機抽取的字串
            string strRandomCode = "ABCD1EF2GH3IJ4KL5MN6P7QR8ST9UVWXYZ";
            //將定義的字串轉成字元陣列                           
            char[] chastr = strRandomCode.ToCharArray();
            //定義StringBuilder物件用於存放驗證碼                                     
            StringBuilder sbValidCode = new StringBuilder();
            //隨機函式,隨機抽取字元                                       
            Random rand = new Random();
            for (int i = 0; i < length; i++)
            {
                //以strRandomCode的長度產生隨機位置並擷取該位置的字元新增到StringBuilder物件中
                sbValidCode.Append(strRandomCode.Substring(rand.Next(0, strRandomCode.Length), 1));
            }
            return sbValidCode.ToString();
        }

        //------------------------------------------------------------  # 60個

        public static string GetCaptchaCode08(int length)
        {
            Random rand = new Random();
            int num, tem;
            string captcha_code = "";
            for (int i = 0; i < length; i++)
            {
                num = rand.Next();
                if (i % 2 == 1)
                {
                    tem = num % 10 + '0'; //數字
                }
                else
                {
                    tem = num % 26 + 'A'; //字母
                }
                captcha_code += Convert.ToChar(tem).ToString();
            }
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        /// 生成隨機字符碼
        /// <param name="codeLen">字符串長度</param>
        /// <param name="zhCharsCount">中文字符數</param>
        public string GetCaptchaCode09(int codeLen, int zhCharsCount)
        {
            Random rand = new Random();

            char[] chs = new char[codeLen];

            int index;
            for (int i = 0; i < zhCharsCount; i++)
            {
                index = rand.Next(0, codeLen);
                if (chs[index] == '\0')
                {
                    chs[index] = CreateZhChar();
                }
                else
                {
                    --i;
                }
            }
            for (int i = 0; i < codeLen; i++)
            {
                if (chs[i] == '\0')
                {
                    chs[i] = CreateEnOrNumChar2();
                }
            }

            return new string(chs, 0, chs.Length);
        }

        // 生成英文或數字字符
        protected char CreateEnOrNumChar2()
        {
            // 英文與數字串
            string EnglishOrNumChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

            Random rand = new Random();
            return EnglishOrNumChars[rand.Next(0, EnglishOrNumChars.Length)];
        }

        // 生成漢字字符
        protected char CreateZhChar()
        {
            string ChineseChars = String.Empty;

            Random rand = new Random();

            //若提供了漢字集，查詢漢字集選取漢字
            if (ChineseChars.Length > 0)
            {
                return ChineseChars[rand.Next(0, ChineseChars.Length)];
            }
            //若沒有提供漢字集，則根據《GB2312簡體中文編碼表》編碼規則構造漢字
            else
            {
                byte[] bytes = new byte[2];

                //第一個字節值在0xb0, 0xf7之間
                bytes[0] = (byte)rand.Next(0xb0, 0xf8);
                //第二個字節值在0xa1, 0xfe之間
                bytes[1] = (byte)rand.Next(0xa1, 0xff);

                //根據漢字編碼的字節數組解碼出中文漢字
                string str1 = Encoding.GetEncoding("gb2312").GetString(bytes);

                return str1[0];
            }
        }

        //------------------------------------------------------------  # 60個

        // 內部方法：產生隨機數和隨機點
        // 產生0-9A-Z的隨機字符代碼
        // <returns>字符代碼</returns>
        private int RandomAZ09()
        {
            int result = 48;
            Random rand = new Random();
            int i = rand.Next(2);

            switch (i)
            {
                case 0:
                    result = rand.Next(48, 58);
                    break;
                case 1:
                    result = rand.Next(65, 91);
                    break;
            }

            return result;
        }

        // 內部方法：返回指定長度的隨機驗證碼字符串
        // 根據指定大小返回隨機驗證碼
        // <param >字符串長度</param>
        // <returns>隨機字符串</returns>
        private string GetCaptchaCode10(int length)
        {
            StringBuilder sb = new StringBuilder(6);

            for (int i = 0; i < length; i++)
            {
                sb.Append(Char.ConvertFromUtf32(RandomAZ09()));
            }

            return sb.ToString();
        }

        //------------------------------------------------------------  # 60個

        private static string GetChar(Random rand)
        {
            int n = rand.Next(0, 61);
            if (n <= 9)
            {
                return ((char)(48 + n)).ToString();
            }
            else if (n <= 35)
            {
                return ((char)(65 + n - 10)).ToString();
            }
            else
            {
                return ((char)(97 + n - 36)).ToString();
            }
        }

        private string GetCaptchaCode11(int length)
        {
            string captcha_code = "";
            for (int i = 0; i < length; i++)
            {
                captcha_code += GetChar(rand);
            }
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //測試隨機文字1

            string captcha_text = string.Empty;
            int length = 10;
            Random rand = new Random();

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode01(length);
            richTextBox1.Text += "01取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode02(length);
            richTextBox1.Text += "02取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode03(length);
            richTextBox1.Text += "03取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode04(length);
            richTextBox1.Text += "04取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode05(length);
            richTextBox1.Text += "05取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            //  純數字
            captcha_text = GetCaptchaCode06(RandomGeneratorStyle.Number, length);//生成隨機數
            richTextBox1.Text += "06a取得 : " + captcha_text + "\n";
            //數字+大小寫英文
            captcha_text = GetCaptchaCode06(RandomGeneratorStyle.NumberAndChar, length);//生成隨機數
            richTextBox1.Text += "06b取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode07(length);
            richTextBox1.Text += "07取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode08(length);
            richTextBox1.Text += "08取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode09(length, 5);
            richTextBox1.Text += "09取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode10(length);
            richTextBox1.Text += "10取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetCaptchaCode11(length);
            richTextBox1.Text += "11取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個
            // 以上用函數, 以下用算的
            //------------------------------------------------------------  # 60個

            int len = rand.Next(4, 6);

            char[] chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            StringBuilder myStr = new StringBuilder();
            for (int iCount = 0; iCount < len; iCount++)
            {
                myStr.Append(chars[rand.Next(chars.Length)]);
            }
            captcha_text = myStr.ToString();
            richTextBox1.Text += "12取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = string.Empty;
            //验证码的字符集，去掉了一些容易混淆的字符 
            char[] character = { '2', '3', '4', '5', '6', '8', '9', 'a', 'b', 'd', 'e', 'f', 'h', 'k', 'm', 'n', 'r', 'x', 'y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'W', 'X', 'Y' };
            //生成验证码字符串 
            for (int i = 0; i < 4; i++)
            {
                captcha_text += character[rand.Next(character.Length)];
            }
            richTextBox1.Text += "13取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            //亂數產生驗證答案
            //從已知幾個元素中任意選出幾個

            string texts = "fjalkdfjalkdjfalkjdf";

            string vaildNumAnswer = "";
            vaildNumAnswer = "";
            for (int i = 1; i <= length; i++)
            {
                char c = texts[rand.Next(texts.Length)];
                vaildNumAnswer += c;
            }
            richTextBox1.Text += "14取得 : " + vaildNumAnswer + "\n";

            //------------------------------------------------------------  # 60個

            StringBuilder objStringBuilder = new StringBuilder();

            //加入數字1-9
            for (int i = 1; i <= 9; i++)
            {
                objStringBuilder.Append(i.ToString());
            }

            //加入大寫字母A-Z，不包括O
            char temp = ' ';

            for (int i = 0; i < 26; i++)
            {
                temp = Convert.ToChar(i + 65);

                //如果生成的字母不是'O'
                if (!temp.Equals('O'))
                {
                    objStringBuilder.Append(temp);
                }
            }

            //加入小寫字母a-z，不包括o
            temp = ' ';

            for (int i = 0; i < 26; i++)
            {
                temp = Convert.ToChar(i + 97);

                //如果生成的字母不是'o'
                if (!temp.Equals('o'))
                {
                    objStringBuilder.Append(temp);
                }
            }

            //生成驗證碼字符串
            int index = 0;

            captcha_text = string.Empty;

            for (int i = 0; i < length; i++)
            {
                index = rand.Next(0, objStringBuilder.Length);

                captcha_text += objStringBuilder[index];

                objStringBuilder.Remove(index, 1);
            }

            richTextBox1.Text += "15取得 : " + objStringBuilder + "\n";
            richTextBox1.Text += "15取得 : " + captcha_text + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //測試隨機文字2
        }

        //------------------------------------------------------------  # 60個

    }

    class Randomizer
    {
        public static void Randomize<T>(T[] items)
        {
            Random rand = new Random();

            // For each spot in the array, pick a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }
    }

    public static class RandomTools
    {
        // The Random object this method uses.
        private static Random rand = null;

        // Return a random value.
        public static T PickRandom<T>(this T[] values)
        {
            // Create the Random object if it doesn't exist.
            if (rand == null)
            {
                rand = new Random();
            }

            // Pick an item and return it.
            return values[rand.Next(0, values.Length)];
        }

        // Return num_items random values.
        public static List<T> PickRandom<T>(this T[] values, int num_values)
        {
            // Create the Random object if it doesn't exist.
            if (rand == null)
            {
                rand = new Random();
            }

            // Don't exceed the array's length.
            if (num_values >= values.Length)
            {
                num_values = values.Length - 1;
            }

            // Make an array of indexes 0 through values.Length - 1.
            int[] indexes = Enumerable.Range(0, values.Length).ToArray();

            // Build the return list.
            List<T> results = new List<T>();

            // Randomize the first num_values indexes.
            for (int i = 0; i < num_values; i++)
            {
                // Pick a random entry between i and values.Length - 1.
                int j = rand.Next(i, values.Length);

                // Swap the values.
                int temp = indexes[i];
                indexes[i] = indexes[j];
                indexes[j] = temp;

                // Save the ith value.
                results.Add(values[indexes[i]]);
            }
            // Return the selected items.
            return results;
        }
    }

    // Extension methods to randomize different kinds of collections.
    public static class RandomizationExtensions
    {
        private static Random rand = new Random();

        // Randomize an array.
        public static void Randomize<T>(this T[] items)
        {
            // For each spot in the array, pick
            // a random item to swap into that spot.
            for (int i = 0; i < items.Length - 1; i++)
            {
                int j = rand.Next(i, items.Length);
                T temp = items[i];
                items[i] = items[j];
                items[j] = temp;
            }
        }

        // Randomize a list.
        public static void Randomize<T>(this List<T> items)
        {
            // Convert into an array.
            T[] item_array = items.ToArray();

            // Randomize.
            item_array.Randomize();

            // Copy the items back into the list.
            items.Clear();
            items.AddRange(item_array);
        }

        // Randomize a 2D array.
        public static void Randomize<T>(this T[,] values)
        {
            // Get the dimensions.
            int num_rows = values.GetUpperBound(0) + 1;
            int num_cols = values.GetUpperBound(1) + 1;
            int num_cells = num_rows * num_cols;

            // Randomize the array.
            for (int i = 0; i < num_cells - 1; i++)
            {
                // Pick a random cell between i and the end of the array.
                int j = rand.Next(i, num_cells);

                // Convert to row/column indexes.
                int row_i = i / num_cols;
                int col_i = i % num_cols;
                int row_j = j / num_cols;
                int col_j = j % num_cols;

                // Swap cells i and j.
                T temp = values[row_i, col_i];
                values[row_i, col_i] = values[row_j, col_j];
                values[row_j, col_j] = temp;
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
        public static string GetRandomString2(int length)
        {
            var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            Random rand = new Random();
            var builder = new StringBuilder();
            for (var i = 0; i < length; i++)
            {
                builder.Append(str[rand.Next(0, str.Length)]);
            }
            return builder.ToString();
        }
*/


