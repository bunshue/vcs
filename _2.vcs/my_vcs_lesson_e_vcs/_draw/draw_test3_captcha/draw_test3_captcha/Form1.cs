using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for MemoryStream
using System.Drawing.Imaging;

using System.Drawing.Drawing2D; //for LinearGradientBrush

namespace draw_test3_captcha
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //產生圖片驗證碼
            string tmp = RndNum(4);
            Create(out tmp);

        }

        /// <summary>
        /// 該方法用於生成指定位數的隨機數
        /// </summary>
        /// <param name="VcodeNum">參數是隨機數的位數</param>
        /// <returns>返回一個隨機數字符串</returns>
        private string RndNum(int VcodeNum)
        {
            string Vchar = "1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,P" +
                ",Q,R,S,T,U,V,W,X,Y,Z";
            string[] VcArray = Vchar.Split(new Char[] { ',' });//拆分成陣列
            string VNum = "";//產生的隨機數
            int temp = -1;//記錄上次隨機數值，盡量避免生產幾個一樣的隨機數
            Random rand = new Random();
            for (int i = 1; i < VcodeNum + 1; i++)
            {
                if (temp != -1)
                {
                    rand = new Random(i * temp * unchecked((int)DateTime.Now.Ticks));
                }
                int t = rand.Next(33);
                if (temp != -1 && temp == t)
                {
                    return RndNum(VcodeNum);
                }
                temp = t;
                VNum += VcArray[t];
            }
            return VNum;
        }
        /// <summary>
        /// 該方法是將生成的隨機數寫入圖像文件
        /// </summary>
        /// <param name="VNum">VNum是一個隨機數</param>
        public MemoryStream Create(out string VNum)
        {
            VNum = RndNum(4);
            Bitmap Img = null;
            Graphics g = null;
            MemoryStream ms = null;
            System.Random random = new Random();
            //驗證碼顏色集合
            Color[] c = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
            //驗證碼字體集合
            string[] fonts = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };

            //定義圖像的大小，生成圖像的實例
            Img = new Bitmap(100, 25);

            g = Graphics.FromImage(Img);//從Img對象生成新的Graphics對象 

            g.Clear(Color.White);//背景設為白色

            //在隨機位置畫背景點
            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(Img.Width);
                int y = random.Next(Img.Height);
                g.DrawRectangle(new Pen(Color.LightGray, 0), x, y, 1, 1);
            }
            //驗證碼繪制在g中
            for (int i = 0; i < VNum.Length; i++)
            {
                int cindex = random.Next(7);//隨機顏色索引值
                int findex = random.Next(5);//隨機字體索引值
                Font f = new Font(fonts[findex], 14, FontStyle.Bold);//字體
                Brush b = new SolidBrush(c[cindex]);//顏色
                int ii = 4;
                if ((i + 1) % 2 == 0)//控制驗證碼不在同一高度
                {
                    ii = 2;
                }
                g.DrawString(VNum.Substring(i, 1), f, b, 3 + (i * 20), ii);//繪制一個驗證字符
            }
            ms = new MemoryStream();//生成內存流對象
            Img.Save(ms, ImageFormat.Jpeg);//將此圖像以jpg圖像文件的格式保存到流中

            //回收資源
            g.Dispose();

            pictureBox1.Image = Img;
            //Img.Dispose();
            return ms;
        }

        private void ValidateCode(string VNum)
        {
            Bitmap Img = null;
            Graphics g = null;
            MemoryStream ms = null;
            int gheight = VNum.Length * 12;
            Img = new Bitmap(gheight, 25);
            g = Graphics.FromImage(Img);
            //生成隨機生成器
            Random random = new Random();
            //背景顏色
            g.Clear(Color.White);
            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(Img.Width);
                int y = random.Next(Img.Height);
                Img.SetPixel(x, y, Color.FromArgb(random.Next()));
            }
            //文字字體
            Font f = new Font("Arial Black ", 12);
            //文字顏色
            SolidBrush s = new SolidBrush(Color.Blue);
            g.DrawString(VNum, f, s, 3, 3);
            ms = new MemoryStream();
            Img.Save(ms, ImageFormat.Jpeg);
            //Response.ClearContent();
            //Response.ContentType = "image/Jpeg ";
            //Response.BinaryWrite(ms.ToArray());
            g.Dispose();
            pictureBox1.Image = Img;
            //Img.Dispose();
            //Response.End();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string tmp = RndNum(4);
            //HttpCookie a = new HttpCookie("ImageV ", tmp);
            //Response.Cookies.Add(a);
            this.ValidateCode(tmp);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ProcessRequest();
        }

        public void ProcessRequest()
        {
            int W = 80;
            int H = 22;
            int fontSize = 16;
            string chkCode = string.Empty;
            //颜色列表，用于验证码、噪线、噪点 
            Color[] color = { Color.Black, Color.Red, Color.Blue, Color.Green, Color.Orange, Color.Brown, Color.Brown, Color.DarkBlue };
            //字体列表，用于验证码 
            string[] font = { "Times New Roman", "Verdana", "Arial", "Gungsuh", "Impact" };
            //验证码的字符集，去掉了一些容易混淆的字符 
            char[] character = { '2', '3', '4', '5', '6', '8', '9', 'a', 'b', 'd', 'e', 'f', 'h', 'k', 'm', 'n', 'r', 'x', 'y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'W', 'X', 'Y' };
            Random rnd = new Random();
            //生成验证码字符串 
            for (int i = 0; i < 4; i++)
            {
                chkCode += character[rnd.Next(character.Length)];
            }

            //写入Session
            //context.Session["dt_session_code"] = chkCode;

            //创建画布
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            //画噪线 
            for (int i = 0; i < 1; i++)
            {
                int x1 = rnd.Next(W);
                int y1 = rnd.Next(H);
                int x2 = rnd.Next(W);
                int y2 = rnd.Next(H);
                Color clr = color[rnd.Next(color.Length)];
                g.DrawLine(new Pen(clr), x1, y1, x2, y2);
            }
            //画验证码字符串 
            for (int i = 0; i < chkCode.Length; i++)
            {
                string fnt = font[rnd.Next(font.Length)];
                Font ft = new Font(fnt, fontSize);
                Color clr = color[rnd.Next(color.Length)];
                g.DrawString(chkCode[i].ToString(), ft, new SolidBrush(clr), (float)i * 18 + 2, (float)0);
            }
            ////画噪点 
            //for (int i = 0; i < 1; i++)
            //{
            //    int x = rnd.Next(bitmap1.Width);
            //    int y = rnd.Next(bitmap1.Height);
            //    Color clr = color[rnd.Next(color.Length)];
            //    bitmap1.SetPixel(x, y, clr);
            //}


            /*  
              //将验证码图片写入内存流，并将其以 "image/Png" 格式输出 
              MemoryStream ms = new MemoryStream();
              try
              {
                  bitmap1.Save(ms, ImageFormat.Png);
              }
              catch (Exception)
              {

              }
              finally
              {
                  g.Dispose();
                  bitmap1.Dispose();
              }
          */

            g.Dispose();
            pictureBox1.Image = bitmap1;
            //bitmap1.Dispose();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //CreateCheckCodeImage(GenerateCheckCodes(10));
            GetCheckCode();
        }

        void GetCheckCode()
        {
            int len = 10;
            string code = GenerateCheckCodes(len);
            byte[] bytes = CreateCheckCodeImage(code);
            return;
        }

        private string GenerateCheckCodes(int iCount)
        {
            char[] oCharacter = {'0','1','2','3','4','5','6','7','8','9',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            //'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            };

            //int number;
            string checkCode = String.Empty;
            int iSeed = DateTime.Now.Millisecond;
            System.Random random = new Random(iSeed);
            for (int i = 0; i < iCount; i++)
            {
                checkCode += oCharacter[random.Next(oCharacter.Length)];

                //純數字
                //number = random.Next(10);
                //number = oCharacter[random.Next(oCharacter.Length)];
                //checkCode += number.ToString();
            }
            return checkCode;
        }

        private byte[] CreateCheckCodeImage(string checkCode)
        {
            if (checkCode == null || checkCode.Trim() == String.Empty)
            {
                return null;
            }
            int iWordWidth = 20;
            int iImageWidth = checkCode.Length * iWordWidth;
            Bitmap image = new Bitmap(iImageWidth, 30);
            Graphics g = Graphics.FromImage(image);
            try
            {
                //生成隨機生成器
                Random random = new Random();
                //清空圖片背景色
                g.Clear(Color.White);

                //畫圖片的背景噪音點
                for (int i = 0; i < 20; i++)
                {
                    int x1 = random.Next(image.Width);
                    int x2 = random.Next(image.Width);
                    int y1 = random.Next(image.Height);
                    int y2 = random.Next(image.Height);
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }

                //畫圖片的背景噪音線
                for (int i = 0; i < 2; i++)
                {
                    int x1 = 0;
                    int x2 = image.Width;
                    int y1 = random.Next(image.Height);
                    int y2 = random.Next(image.Height);
                    if (i == 0)
                    {
                        g.DrawLine(new Pen(Color.Gray, 2), x1, y1, x2, y2);
                    }

                }
                for (int i = 0; i < checkCode.Length; i++)
                {

                    string Code = checkCode[i].ToString();
                    int xLeft = iWordWidth * (i);
                    random = new Random(xLeft);
                    int iSeed = DateTime.Now.Millisecond;
                    int iValue = random.Next(iSeed) % 4;
                    if (iValue == 0)
                    {
                        Font font = new Font("Arial", 16, (FontStyle.Bold | FontStyle.Italic));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Red, 1.5f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 1)
                    {
                        Font font = new Font("楷體", 16, (FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.DarkRed, 1.3f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 2)
                    {
                        Font font = new Font("宋體", 16, (FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Green, Color.Blue, 1.2f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 3)
                    {
                        Font font = new Font("黑體", 16, (FontStyle.Bold |

                        FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Green, 1.8f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                }
                ////畫圖片的前景噪音點 ---有無這段代碼 貌似沒啥變化
                for (int i = 0; i < 8; i++)
                {
                    int x = random.Next(image.Width);
                    int y = random.Next(image.Height);
                    image.SetPixel(x, y, Color.FromArgb(random.Next()));
                }
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);

                pictureBox1.Image = image;

                MemoryStream ms = new MemoryStream();
                image.Save(ms, ImageFormat.Jpeg);
                return ms.ToArray();
                //Response.ClearContent();
                //Response.ContentType = "image/jpeg";
                //Response.BinaryWrite(ms.ToArray());
            }
            finally
            {
                g.Dispose();
                //image.Dispose();
            }
        }

        private string GetValidCode(int num)
        {
            //定義要隨機抽取的字串
            string strRandomCode = "ABCD1EF2GH3IJ4KL5MN6P7QR8ST9UVWXYZ";
            //將定義的字串轉成字元陣列                           
            char[] chastr = strRandomCode.ToCharArray();
            //定義StringBuilder物件用於存放驗證碼                                     
            StringBuilder sbValidCode = new StringBuilder();
            //隨機函式,隨機抽取字元                                       
            Random rd = new Random();
            for (int i = 0; i < num; i++)
            {
                //以strRandomCode的長度產生隨機位置並擷取該位置的字元新增到StringBuilder物件中
                sbValidCode.Append(strRandomCode.Substring(rd.Next(0, strRandomCode.Length), 1));
            }
            return sbValidCode.ToString();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string strValidCode;
            // 產生5位隨機字元
            strValidCode = this.GetValidCode(5);
            //將字串儲存到Session中,以便需要時進行驗證                                                
            //context.Session["ValidCode"] = strValidCode;
            //定義寬120畫素,高30畫素的資料定義的影象物件                                          
            Bitmap image = new Bitmap(120, 30);
            //繪製圖片                               
            Graphics g = Graphics.FromImage(image);
            try
            {
                //生成隨機物件
                Random random = new Random();
                //清除圖片背景色                                                   
                g.Clear(Color.White);
                // 隨機產生圖片的背景噪線                                                       
                for (int i = 0; i < 25; i++)
                {
                    int x1 = random.Next(image.Width);
                    int x2 = random.Next(image.Width);
                    int y1 = random.Next(image.Height);
                    int y2 = random.Next(image.Height);
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }
                //設定圖片字型風格
                Font font = new Font("新宋體", 20, (FontStyle.Bold));
                //設定畫筆型別
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, image.Width, image.Height), Color.Blue, Color.DarkRed, 3, true);
                //繪製隨機字元
                g.DrawString(strValidCode, font, brush, 5, 2);

                //繪製圖片的前景噪點
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);
                //建立儲存區為記憶體的流
                System.IO.MemoryStream ms = new System.IO.MemoryStream();
                //將影象物件儲存為記憶體流       
                image.Save(ms, ImageFormat.Gif);
                //清除當前緩衝區流中的所有內容                                             
                //context.Response.ClearContent();
                //設定輸出流的MIME型別                           
                //context.Response.ContentType = "image/Gif";
                //將記憶體流寫入到輸出流                                        
                //context.Response.BinaryWrite(ms.ToArray());
            }
            finally
            {
                g.Dispose();
                //image.Dispose();
                pictureBox1.Image = image;
            }
        }

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
  
  
  
          Encoding gb=System.Text.Encoding.GetEncoding("gb2312");
          object[] bytes=gb.Encoding.GetBytes ("好")；
  
  
          發現得到了一個長度為2的字節數組bytes，使用
  
  
  
          string lowCode = System.Convert.ToString(bytes[0], 16); //取出元素1編碼內容（兩位16進制）
          string hightCode = System.Convert.ToString(bytes[1], 16);//取出元素2編碼內容（兩位16進制）
  
  
          之後發現字節數組bytes16進制變碼後內容竟然是{ba,c3}，剛好是“好”字的十六進制區位碼（見區位碼表）。
          因此我們就可以隨機生成一個長度為2的十六進制字節數組，使用GetString ()方法對其進行解碼就可以得到漢字字符了。不過對於生成中文漢字驗證碼來說，因為第15區也就是AF區以前都沒有漢字，只有少量符號，漢字都從第16區B0開始，並且從區位D7開始以後的漢字都是和很難見到的繁雜漢字，所以這些都要排出掉。所以隨機生成的漢字十六進制區位碼第1位范圍在B、C、D之間，如果第1位是D的話，第2位區位碼就不能是7以後的十六進制數。在來看看區位碼表發現每區的第一個位置和最後一個位置都是空的，沒有漢字，因此隨機生成的區位碼第3位如果是A的話，第4位就不能是0；第3位如果是F的話，第4位就不能是F。

        */

        private string GetRandomText(int nLen)
        {
            //獲取GB2312編碼頁（表）
            Encoding gb = Encoding.GetEncoding("gb2312");

            //調用函數產生4個隨機中文漢字編碼
            object[] bytes = CreateRegionCode(nLen);

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

        /**/
        /**/
        /**/
        /* 
 * 在.Net中可以使用System.Text來處理所有語言的編碼。在System.Text命名空間中包含眾多編碼的類，可供進行操作及轉換。其中的Encoding類就是重點處理漢字編碼的類。通過在.Net文檔中查詢Encoding類的方法我們可以發現所有和文字編碼有關的都是字節數組，其中有兩個很好用的方法：  
    Encoding.GetBytes ()方法將指定的 String 或字符數組的全部或部分內容編碼為字節數組  
    Encoding.GetString ()方法將指定字節數組解碼為字符串。  

    沒錯我們可以通過這兩個方法將漢字字符編碼為字節數組，同樣知道了漢字GB2312的字節數組編碼也就可以將字節數組解碼為漢字字符。通過對“好”字進行編碼為字節數組後  

    Encoding gb=System.Text.Encoding.GetEncoding("gb2312");   
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
        public static object[] CreateRegionCode(int strlength)
        {
            //定義一個字符串數組儲存漢字編碼的組成元素   
            string[] rBase = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };

            Random rnd = new Random();

            //定義一個object數組用來   
            object[] bytes = new object[strlength];

            /**/
            /**/
            /**/
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
                rnd = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);//更換隨機數發生器的  種子避免產生重復值   
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
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);
                int r3 = rnd.Next(10, 16);
                string str_r3 = rBase[r3].Trim();

                //區位碼第4位   
                rnd = new Random(r3 * unchecked((int)DateTime.Now.Ticks) + i);
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

        /**/
        /// <summary>
        /// 生成圖片驗證碼
        /// </summary>
        /// <param name="nLen">驗證碼的長度</param>
        /// <param name="_codes">產生驗證碼的取值</param>
        /// <param name="strKey">輸出參數，驗證碼的內容</param>
        /// <returns>圖片字節流</returns>
        private byte[] GenerateVerifyImage(int nLen, ref string strKey)
        {
            int nBmpWidth = 26 * nLen + 10;
            int nBmpHeight = 40;
            Bitmap bmp = new Bitmap(nBmpWidth, nBmpHeight);

            // 1. 生成隨機背景顏色
            int nRed, nGreen, nBlue;  // 背景的三元色
            System.Random rd = new Random((int)System.DateTime.Now.Ticks);
            nRed = rd.Next(255) % 128 + 128;
            nGreen = rd.Next(255) % 128 + 128;
            nBlue = rd.Next(255) % 128 + 128;

            // 2. 填充位圖背景
            Graphics graph = Graphics.FromImage(bmp);
            graph.FillRectangle(new SolidBrush(Color.FromArgb(nRed, nGreen, nBlue))
             , 0
             , 0
             , nBmpWidth
             , nBmpHeight);


            // 3. 繪制干擾線條，采用比背景略深一些的顏色
            int nLines = 5;
            Pen pen = new Pen(Color.FromArgb(nRed - 17, nGreen - 17, nBlue - 17), 2);
            for (int a = 0; a < nLines; a++)
            {
                int x1 = rd.Next() % nBmpWidth;
                int y1 = rd.Next() % nBmpHeight;
                int x2 = rd.Next() % nBmpWidth;
                int y2 = rd.Next() % nBmpHeight;
                graph.DrawLine(pen, x1, y1, x2, y2);
            }

            // 采用的字符集，可以隨即拓展，並可以控制字符出現的幾率
            string strCode = GetRandomText(nLen);

            // 4. 循環取得字符，並繪制
            string strResult = "";
            for (int i = 0; i < nLen; i++)
            {
                int x = (i * 26 + rd.Next(5));
                int y = rd.Next(10) + 1;

                // 確定字體
                Font font = new Font("Arial",
                  14 + rd.Next() % 4,
                FontStyle.Bold);
                string c = strCode.Substring(i, 1);  // 獲取字符
                strResult += c.ToString();

                // 繪制字符
                graph.DrawString(c.ToString(),
                    font,
                    new SolidBrush(Color.FromArgb(nRed - 68, nGreen - 68, nBlue - 68)),   //繪制字體顏色，采用比背景與干擾線略深一些的顏色
                     x,
                     y);
            }
            // 5. 輸出字節流
            System.IO.MemoryStream bstream = new System.IO.MemoryStream();
            bmp.Save(bstream, ImageFormat.Jpeg);
            //bmp.Dispose();
            pictureBox1.Image = bmp;
            graph.Dispose();

            strKey = strResult;
            byte[] byteReturn = bstream.ToArray();
            bstream.Close();

            return byteReturn;
        }
    



        private void button5_Click(object sender, EventArgs e)
        {
            string strKey = "";
            int _nlen = 6;
            byte[] data = this.GenerateVerifyImage(_nlen, ref strKey); //_nLen生成驗證碼的長度
            //Session["Jcode"] = strKey; //用來保存驗證碼的值
            //Page.Response.OutputStream.Write(data, 0, data.Length);
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }
}
