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

using System.Drawing.Text;  //for TextRenderingHint
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

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
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
            System.IO.MemoryStream ms = new System.IO.MemoryStream();
            bmp.Save(ms, ImageFormat.Jpeg);
            //bmp.Dispose();
            pictureBox1.Image = bmp;
            graph.Dispose();

            strKey = strResult;
            byte[] byteReturn = ms.ToArray();
            ms.Close();

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
            /*
            驗證碼字符個數、生成圖片寬度、高度自定均可由構造方法自定，無參構造生成默認字符個數和默認大小的Image,
            方法GetImgWithValidateCode()返回生成的驗證碼圖片，
            方法 IsRight(string inputValCode) 判斷用戶輸入的驗證碼 inputValCode與圖片顯示的字符是否一致，不區分大小寫
            */

            DrawValImg drawimg = new DrawValImg();
            Image img = drawimg.GetImgWithValidateCode();
            pictureBox1.Image = img;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            CreateCaptcha();
        }

        void CreateCaptcha()
        {
            // 創建一個包含隨機內容的驗證碼文本
            System.Random rand = new Random();
            int len = rand.Next(4, 6);
            char[] chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            System.Text.StringBuilder myStr = new System.Text.StringBuilder();
            for (int iCount = 0; iCount < len; iCount++)
            {
                myStr.Append(chars[rand.Next(chars.Length)]);
            }
            string text = myStr.ToString();
            // 保存驗證碼到 session 中以便其他模塊使用
            //this.Session["checkcode"] = text ;
            Size ImageSize = Size.Empty;
            Font myFont = new Font("MS Sans Serif", 20);
            // 計算驗證 碼圖片大小
            using (Bitmap bitmap1 = new Bitmap(10, 10))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    SizeF size = g.MeasureString(text, myFont, 10000);
                    ImageSize.Width = (int)size.Width + 8;
                    ImageSize.Height = (int)size.Height + 8;
                }
            }
            // 創建驗證碼圖片
            Bitmap bitmap2 = new Bitmap(ImageSize.Width, ImageSize.Height);
            {
                // 繪制驗證碼文本
                using (Graphics g = Graphics.FromImage(bitmap2))
                {
                    g.Clear(Color.White);
                    using (StringFormat f = new StringFormat())
                    {
                        f.Alignment = StringAlignment.Near;
                        f.LineAlignment = StringAlignment.Center;
                        f.FormatFlags = StringFormatFlags.NoWrap;
                        g.DrawString(
                           text,
                          myFont,
                          Brushes.Black,
                           new RectangleF(
                          0,
                          0,
                          ImageSize.Width,
                          ImageSize.Height),
                          f);
                    }//using
                }//using
                // 制造噪聲 雜點面積占圖片面積的 30%
                int num = ImageSize.Width * ImageSize.Height * 30 / 100;
                for (int iCount = 0; iCount < num; iCount++)
                {
                    // 在隨機的位置使用隨機的顏色設置圖片的像素
                    int x = rand.Next(ImageSize.Width);
                    int y = rand.Next(ImageSize.Height);
                    int r = rand.Next(255);
                    int g = rand.Next(255);
                    int b = rand.Next(255);
                    Color c = Color.FromArgb(r, g, b);
                    bitmap2.SetPixel(x, y, c);
                }//for

                pictureBox1.Image = bitmap2;

                // 輸出圖片
                System.IO.MemoryStream ms = new System.IO.MemoryStream();
                bitmap2.Save(ms, ImageFormat.Jpeg);
                //this.Response.ContentType = "image/png";
                //ms.WriteTo( this.Response.OutputStream );
                ms.Close();
            }//using
            myFont.Dispose();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //產生圖片驗證碼
            Bitmap bitmap1 = Generate(RandomGeneratorStyle.Number, 10);
            pictureBox1.Image = bitmap1;
        }
        public enum RandomGeneratorStyle
        {
            ///　<summary>
            ///　只有數字
            ///　</summary>
            Number,
            ///　<summary>
            ///　包含數字和大小寫字符
            ///　</summary>
            NumberAndChar,
            ///　<summary>
            ///　包含數字和大寫字符
            ///　</summary>
            NumberAndCharIgnoreCase
        }

        public static string GenerateRandomNumber(RandomGeneratorStyle style, int length)
        {
            string strValidateString = "";
            Random rnd = new Random();
            string strValidateStringSource;
            switch (style)
            {
                case RandomGeneratorStyle.Number:
                    strValidateStringSource = "0123456789";
                    break;
                case RandomGeneratorStyle.NumberAndChar:
                    strValidateStringSource = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    break;
                case RandomGeneratorStyle.NumberAndCharIgnoreCase:
                    strValidateStringSource = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
                    break;
                default:
                    strValidateStringSource = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                    break;
            }
            for (int i = 0; i < length; i++)
            {
                strValidateString += strValidateStringSource[rnd.Next(strValidateStringSource.Length - 1)];
            }
            return strValidateString;
        }

        //繪制驗證碼
        public static Bitmap Generate(RandomGeneratorStyle style, int length)
        {
            Bitmap bmp = new Bitmap((int)Math.Ceiling(length * 20.5), 50);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bmp);//利用該圖片對象生成“畫板”
            string strCode = GenerateRandomNumber(style, length);//生成隨機數
            Font font = new Font("Arial", 24, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(strCode, font, brush, 0, 0);//關鍵的一步，進行繪制。
            //bmp.Save(curPage.Response.OutputStream, ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源
            return bmp;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //產生圖片驗證碼(很複雜)

            //首先實例化驗證碼的類
            ValidateCode validateCode = new ValidateCode();
            //生成驗證碼指定的長度
            string code = validateCode.GetRandomString(4);
            //創建驗證碼的圖片
            Bitmap bitmap1 = validateCode.CreateImage(code);

            pictureBox1.Image = bitmap1;

            //最後將驗證碼返回
            //return File(bytes, @"image/jpeg");
            //File(bytes, @"image/jpeg");

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //調用函數將驗證碼生成圖片
            CreateCheckCodeImage2(GenerateCheckCode());
        }

        private string GenerateCheckCode()
        {  //產生五位的隨機字符串
            int number;
            char code;
            string checkCode = String.Empty;

            System.Random random = new Random();

            for (int i = 0; i < 5; i++)
            {
                number = random.Next();

                if (number % 2 == 0)
                    code = (char)('0' + (char)(number % 10));
                else
                    code = (char)('a' + (char)(number % 26));

                checkCode += code.ToString();
            }
            return checkCode;
        }

        //將驗證碼生成圖片顯示
        private void CreateCheckCodeImage2(string checkCode)
        {
            if (checkCode == null || checkCode.Trim() == String.Empty)
            {
                return;
            }

            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling((checkCode.Length * 18.5)), 28);
            Graphics g = Graphics.FromImage(bitmap1);

            try
            {
                //生成隨機生成器
                Random random = new Random();

                //清空圖片背景色
                g.Clear(Color.AntiqueWhite);

                //畫圖片的背景噪音線
                for (int i = 0; i < 10; i++)
                {
                    int x1 = random.Next(bitmap1.Width);
                    int x2 = random.Next(bitmap1.Width);
                    int y1 = random.Next(bitmap1.Height);
                    int y2 = random.Next(bitmap1.Height);

                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }

                Font font = new Font("Arial", 18, (FontStyle.Bold | FontStyle.Italic));
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 1.2f, true);
                g.DrawString(checkCode, font, brush, 2, 2);

                //畫圖片的前景噪音點
                for (int i = 0; i < 100; i++)
                {
                    int x = random.Next(bitmap1.Width);
                    int y = random.Next(bitmap1.Height);

                    bitmap1.SetPixel(x, y, Color.FromArgb(random.Next()));
                }

                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);

                System.IO.MemoryStream ms = new System.IO.MemoryStream();
                bitmap1.Save(ms, ImageFormat.Gif);
                pictureBox1.Image = bitmap1;
            }
            finally
            {
                //g.Dispose();
                //image.Dispose();
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            Random r = new Random();
            string str = string.Empty;
            //生成5位随机数如 90531
            for (int i = 0; i < 5; i++)
            {
                str += r.Next(0, 10);
            }
            Bitmap bitmap = new Bitmap(150, 40);
            Graphics g = Graphics.FromImage(bitmap);
            //预定义几种字体样式和颜色
            string[] fonts = { "微软雅黑", "宋体", "黑体", "隶书", "仿宋" };
            Color[] colors = { Color.Yellow, Color.Blue, Color.Black, Color.Red, Color.Orange };
            //因为每一数字的字体和颜色可能不同，
            //因此循环将生成的随机数每一数字绘制到图片
            for (int i = 0; i < str.Length; i++)
            {
                Point p = new Point(i * 30, 0);
                g.DrawString(str[i].ToString(), new Font(fonts[r.Next(0, 5)], 20, FontStyle.Bold), new SolidBrush(colors[r.Next(0, 5)]), p);
            }
            //循环在图片范围内绘制出50条线
            for (int i = 0; i < 50; i++)
            {
                //保证线的起始点都在图片范围内
                Point p1 = new Point(r.Next(0, bitmap.Width), r.Next(0, bitmap.Height));
                Point p2 = new Point(r.Next(0, bitmap.Width), r.Next(0, bitmap.Height));
                g.DrawLine(new Pen(Brushes.Green), p1, p2);
            }
            //添加一些像素点
            for (int i = 0; i < 300; i++)
            {
                Point p1 = new Point(r.Next(0, bitmap.Width), r.Next(0, bitmap.Height));
                bitmap.SetPixel(p1.X, p1.Y, Color.Green);
            }
            //在winForm中用PictureBox中显示出来
            pictureBox1.Image = bitmap;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //使用驗證碼類
            Captcha capt = new Captcha();
            Bitmap bitmap1 = capt.GetImage();
            pictureBox1.Image = bitmap1;

        }
    }



    #region 驗證碼生成類
    /// <summary>
    /// 驗證碼生成類
    /// </summary>
    public class ValidateCode
    {
        #region 定義和初始化配置字段
        //用戶存取驗證碼字符串
        public string validationCode = String.Empty;
        //生成的驗證碼字符串
        public char[] chars = null;
        /// <summary>
        /// 獲取系統生成的隨機驗證碼
        /// </summary>
        public String ValidationCode
        {
            get { return validationCode; }
        }
        private Int32 validationCodeCount = 4;
        /// <summary>
        /// 獲取和設置驗證碼字符串的長度
        /// </summary>
        public Int32 ValidationCodeCount
        {
            get { return validationCodeCount; }
            set { validationCodeCount = value; }
        }
        Graphics dc = null;
        private int bgWidth = 130;
        /// <summary>
        /// 驗證碼的寬度，默認爲80
        /// </summary>
        public Int32 Width
        {
            get { return bgWidth; }
            set { bgWidth = value; }
        }

        private int bgHeight = 40;
        /// <summary>
        /// 驗證碼的高度，默認爲40
        /// </summary>
        public Int32 Height
        {
            get { return bgHeight; }
            set { bgHeight = value; }
        }
        /* private string[] fontFace = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };
         /// <summary>
         /// 驗證碼字體列表，默認爲{ "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" }
         /// </summary>
         public String[] FontFace
         {
             get { return fontFace; }
             set { fontFace = value; }
         }*/

        private int fontMinSize = 20;
        /// <summary>
        /// 驗證碼字體的最小值，默認爲15,建議不小於15像素
        /// </summary>
        public Int32 FontMinSize
        {
            get { return fontMinSize; }
            set { fontMinSize = value; }
        }
        private Int32 fontMaxSize = 25;
        /// <summary>
        /// 驗證碼字體的最大值，默認爲20
        /// </summary>
        public Int32 FontMaxSize
        {
            get { return fontMaxSize; }
            set { fontMaxSize = value; }
        }
        private Color[] fontColor = { };
        /// <summary>
        /// 驗證碼字體的顏色，默認爲系統自動生成字體顏色
        /// </summary>
        public Color[] FontColor
        {
            get { return fontColor; }
            set { fontColor = value; }
        }
        private Color backColor = Color.FromArgb(243, 255, 255);
        /// <summary>
        /// 驗證碼的背景色，默認爲Color.FromArgb(243, 251, 254)
        /// </summary>
        public Color BackgroundColor
        {
            get { return backColor; }
            set { backColor = value; }
        }
        private Int32 bezierCount = 3;
        /// <summary>
        /// 貝塞爾曲線的條數,默認爲3條
        /// </summary>
        public Int32 BezierCount
        {
            get { return bezierCount; }
            set { bezierCount = value; }
        }
        private Int32 lineCount = 3;
        /// <summary>
        /// 直線條數，默認爲3條
        /// </summary>
        public Int32 LineCount
        {
            get { return lineCount; }
            set { lineCount = value; }
        }
        Random random = new Random();

        private String charCollection = "2,3,4,5,6,7,8,9,a,s,d,f,g,h,z,c,v,b,n,m,k,q,w,e,r,t,y,u,p,A,S,D,F,G,H,Z,C,V,B,N,M,K,Q,W,E,R,T,Y,U,P"; //定義驗證碼字符及出現頻次 ,避免出現0 o j i l 1 x;  
        /// <summary>
        /// 隨機字符串列表，請使用英文狀態下的逗號分隔。
        /// </summary>
        public String CharCollection
        {
            get { return charCollection; }
            set { charCollection = value; }
        }
        private Int32 intCount = 4;
        /// <summary>
        /// 驗證碼字符串個數，默認爲4個字符
        /// </summary>
        public Int32 IntCount
        {
            get { return intCount; }
            set { intCount = value; }
        }
        private Boolean isPixel = true;
        /// <summary>
        /// 是否添加噪點，默認添加，噪點顏色爲系統隨機生成。
        /// </summary>
        public Boolean IsPixel
        {
            get { return isPixel; }
            set { isPixel = value; }
        }
        private Boolean isRandString = true;
        /// <summary>
        /// 是否添加隨機噪點字符串，默認添加
        /// </summary>
        public Boolean IsRandString
        {
            get { return isRandString; }
            set { isRandString = value; }
        }
        /// <summary>
        /// 隨機背景字符串的個數
        /// </summary>
        public Int32 RandomStringCount
        {
            get;
            set;
        }
        private Int32 randomStringFontSize = 9;
        /// <summary>
        /// 隨機背景字符串的大小
        /// </summary>
        public Int32 RandomStringFontSize
        {
            get { return randomStringFontSize; }
            set { randomStringFontSize = value; }
        }
        /// <summary>
        /// 是否對圖片進行扭曲
        /// </summary>
        public Boolean IsTwist
        {
            get;
            set;
        }
        /// <summary>
        /// 邊框樣式
        /// </summary>
        public enum BorderStyle
        {
            /// <summary>
            /// 無邊框
            /// </summary>
            None,
            /// <summary>
            /// 矩形邊框
            /// </summary>
            Rectangle,
            /// <summary>
            /// 圓角邊框
            /// </summary>
            RoundRectangle
        }
        private Int32 rotationAngle = 40;
        /// <summary>
        /// 驗證碼字符串隨機轉動的角度的最大值
        /// </summary>
        public Int32 RotationAngle
        {
            get { return rotationAngle; }
            set { rotationAngle = value; }
        }
        /// <summary>
        /// 設置或獲取邊框樣式
        /// </summary>
        public BorderStyle Border
        {
            get;
            set;
        }
        private Point[] strPoint = null;


        private Double gaussianDeviation = 0;
        /// <summary>
        /// 對驗證碼圖片進行高斯模糊的閥值，如果設置爲0，則不對圖片進行高斯模糊，該設置可能會對圖片處理的性能有較大影響
        /// </summary>
        public Double GaussianDeviation
        {
            get { return gaussianDeviation; }
            set { gaussianDeviation = value; }
        }
        private Int32 brightnessValue = 0;
        /// <summary>
        /// 對圖片進行暗度和亮度的調整，如果該值爲0，則不調整。該設置會對圖片處理性能有較大影響
        /// </summary>
        public Int32 BrightnessValue
        {
            get { return brightnessValue; }
            set { brightnessValue = value; }
        }
        #endregion
        /// <summary>
        /// 構造函數，用於初始化常用變量
        /// </summary>
        public void DrawValidationCode()
        {
            random = new Random(Guid.NewGuid().GetHashCode());
            strPoint = new Point[validationCodeCount + 1];
            if (gaussianDeviation < 0) gaussianDeviation = 0;
        }

        /// <summary>
        /// 生成驗證碼
        /// </summary>
        /// <param name="target">用於存儲圖片的一般字節序列</param>
        public Bitmap CreateImage(string code)
        {
            MemoryStream target = new MemoryStream();
            Bitmap bitmap1 = new Bitmap(bgWidth + 1, bgHeight + 1);
            //寫字符串
            dc = Graphics.FromImage(bitmap1);
            dc.SmoothingMode = SmoothingMode.HighQuality;
            dc.TextRenderingHint = TextRenderingHint.ClearTypeGridFit; ;
            dc.InterpolationMode = InterpolationMode.HighQualityBilinear;
            dc.CompositingQuality = CompositingQuality.HighQuality;

            try
            {
                dc.Clear(Color.White);
                DrawValidationCode();
                dc.DrawImageUnscaled(DrawBackground(), 0, 0);
                dc.DrawImageUnscaled(DrawRandomString(code), 0, 0);
                //對圖片文字進行扭曲
                bitmap1 = AdjustRippleEffect(bitmap1, 5);
                //對圖片進行高斯模糊
                if (gaussianDeviation > 0)
                {
                    Gaussian gau = new Gaussian();
                    bitmap1 = gau.FilterProcessImage(gaussianDeviation, bitmap1);
                }
                //進行暗度和亮度處理
                if (brightnessValue != 0)
                {
                    //對圖片進行調暗處理
                    bitmap1 = AdjustBrightness(bitmap1, brightnessValue);
                }
                return bitmap1;
            }
            catch
            {
                return null;
            }
        }

        #region 畫驗證碼背景，例如，增加早點，添加曲線和直線等
        /// <summary>
        /// 畫驗證碼背景，例如，增加早點，添加曲線和直線等
        /// </summary>
        /// <returns></returns>
        private Bitmap DrawBackground()
        {
            Bitmap bit = new Bitmap(bgWidth + 1, bgHeight + 1);
            Graphics g = Graphics.FromImage(bit);
            g.SmoothingMode = SmoothingMode.HighQuality;

            g.Clear(Color.White);
            Rectangle rectangle = new Rectangle(0, 0, bgWidth, bgHeight);
            Brush brush = new SolidBrush(backColor);
            g.FillRectangle(brush, rectangle);

            //畫噪點
            if (isPixel)
            {
                g.DrawImageUnscaled(DrawRandomPixel(30), 0, 0);
            }
            g.DrawImageUnscaled(DrawRandBgString(), 0, 0);


            //畫曲線
            //g.DrawImageUnscaled(DrawRandomBezier(bezierCount), 0, 0);
            ////畫直線
            //g.DrawImageUnscaled(DrawRandomLine(lineCount), 0, 0);

            //dc.DrawImageUnscaled(DrawStringline(), 0, 0);
            if (Border == BorderStyle.Rectangle)
            {
                //繪製邊框
                g.DrawRectangle(new Pen(Color.FromArgb(90, 87, 46)), 0, 0, bgWidth, bgHeight);
            }
            else if (Border == BorderStyle.RoundRectangle)
            {
                //畫圓角
                DrawRoundRectangle(g, rectangle, Color.FromArgb(90, 87, 46), 1, 3);
            }

            return bit;

        }
        #endregion

        #region 畫正弦曲線
        private Bitmap DrawTwist(Bitmap bmp, Int32 tWidth, Int32 tHeight, float angle, Color color)
        {
            //爲了方便查看效果，在這裏我定義了一個常量。
            //它在定義數組的長度和for循環中都要用到。
            int size = bgWidth;

            double[] x = new double[size];
            Bitmap b = new Bitmap(bmp.Width, bmp.Height);
            b.MakeTransparent();
            Graphics graphics = Graphics.FromImage(b);
            Pen pen = new Pen(color);

            //畫正弦曲線的橫軸間距參數。建議所用的值應該是 正數且是2的倍數。
            //在這裏採用2。
            int val = 2;

            float temp = 0.0f;

            //把畫布下移100。爲什麼要這樣做，只要你把這一句給註釋掉，運行一下代碼，
            //你就會明白是爲什麼？
            graphics.TranslateTransform(0, 100);
            graphics.SmoothingMode = SmoothingMode.HighQuality;
            graphics.PixelOffsetMode = PixelOffsetMode.HighQuality;
            for (int i = 0; i < size; i++)
            {
                //改變tWidth，實現正弦曲線寬度的變化。
                //改tHeight，實現正弦曲線高度的變化。
                x[i] = Math.Sin(2 * Math.PI * i / tWidth) * tHeight;

                graphics.DrawLine(pen, i * val, temp, i * val + val / 2, (float)x[i]);
                temp = (float)x[i];
            }
            graphics.RotateTransform(60, MatrixOrder.Prepend);

            //旋轉圖片
            // b = KiRotate(b, angle, Color.Transparent);
            return b;
        }
        #endregion

        #region 正弦曲線Wave扭曲圖片
        /// <summary>
        /// 正弦曲線Wave扭曲圖片
        /// </summary>
        /// <param name="srcBmp">圖片路徑</param>
        /// <param name="bXDir">如果扭曲則選擇爲True</param>
        /// <param name="dMultValue">波形的幅度倍數，越大扭曲的程度越高，一般爲3</param>
        /// <param name="dPhase">波形的起始相位，取值區間[0-2*PI)</param>
        /// <returns></returns>
        public Bitmap TwistImage(Bitmap srcBmp, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap destBmp = new Bitmap(srcBmp.Width, srcBmp.Height);
            double PI2 = 6.283185307179586476925286766559;
            // 將位圖背景填充爲白色
            Graphics graph = Graphics.FromImage(destBmp);
            graph.FillRectangle(new SolidBrush(Color.White), 0, 0, destBmp.Width, destBmp.Height);
            graph.Dispose();

            double dBaseAxisLen = bXDir ? (double)destBmp.Height : (double)destBmp.Width;

            for (int i = 0; i < destBmp.Width; i++)
            {
                for (int j = 0; j < destBmp.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? (PI2 * (double)j) / dBaseAxisLen : (PI2 * (double)i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);

                    // 取得當前點的顏色
                    int nOldX = 0, nOldY = 0;
                    nOldX = bXDir ? i + (int)(dy * dMultValue) : i;
                    nOldY = bXDir ? j : j + (int)(dy * dMultValue);

                    Color color = srcBmp.GetPixel(i, j);
                    if (nOldX >= 0 && nOldX < destBmp.Width
                     && nOldY >= 0 && nOldY < destBmp.Height)
                    {
                        destBmp.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return destBmp;
        }
        #endregion

        #region 圖片任意角度旋轉
        /// <summary>
        /// 圖片任意角度旋轉
        /// </summary>
        /// <param name="bmp">原始圖Bitmap</param>
        /// <param name="angle">旋轉角度</param>
        /// <param name="bkColor">背景色</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiRotate(Bitmap bmp, float angle, Color bkColor)
        {
            int w = bmp.Width;
            int h = bmp.Height;

            PixelFormat pf;

            if (bkColor == Color.Transparent)
            {
                pf = PixelFormat.Format32bppArgb;
            }
            else
            {
                pf = bmp.PixelFormat;
            }

            Bitmap tmp = new Bitmap(w, h, pf);
            Graphics g = Graphics.FromImage(tmp);
            g.Clear(bkColor);
            g.DrawImageUnscaled(bmp, 1, 1);
            g.Dispose();

            GraphicsPath path = new GraphicsPath();
            path.AddRectangle(new RectangleF(0f, 0f, w, h));
            Matrix mtrx = new Matrix();
            mtrx.Rotate(angle);
            RectangleF rct = path.GetBounds(mtrx);

            Bitmap dst = new Bitmap((int)rct.Width, (int)rct.Height, pf);
            g = Graphics.FromImage(dst);
            g.Clear(bkColor);
            g.TranslateTransform(-rct.X, -rct.Y);
            g.RotateTransform(angle);
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;
            g.DrawImageUnscaled(tmp, 0, 0);
            g.Dispose();
            tmp.Dispose();

            return dst;
        }
        #endregion

        #region 隨機生成貝塞爾曲線
        /// <summary>
        /// 隨機生成貝塞爾曲線
        /// </summary>
        /// <param name="bmp">一個圖片的實例</param>
        /// <param name="lineNum">線條數量</param>
        /// <returns></returns>
        public Bitmap DrawRandomBezier(Int32 lineNum)
        {
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            b.MakeTransparent();
            Graphics g = Graphics.FromImage(b);
            g.Clear(Color.Transparent);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;

            GraphicsPath gPath1 = new GraphicsPath();
            Int32 lineRandNum = random.Next(lineNum);

            for (int i = 0; i < (lineNum - lineRandNum); i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                        new Point(random.Next(1, (b.Width / 10)), random.Next(1, (b.Height))),
                                        new Point(random.Next((b.Width / 10) * 2, (b.Width / 10) * 4), random.Next(1, (b.Height))),
                                        new Point(random.Next((b.Width / 10) * 4, (b.Width / 10) * 6), random.Next(1, (b.Height))),
                                        new Point(random.Next((b.Width / 10) * 8, b.Width), random.Next(1, (b.Height)))
                                    };

                gPath1.AddBeziers(point);
                g.DrawPath(p, gPath1);
                p.Dispose();
            }
            for (int i = 0; i < lineRandNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                new Point(random.Next(1, b.Width), random.Next(1, b.Height)),
                                new Point(random.Next((b.Width / 10) * 2, b.Width), random.Next(1, b.Height)),
                                new Point(random.Next((b.Width / 10) * 4, b.Width), random.Next(1, b.Height)),
                                new Point(random.Next(1, b.Width), random.Next(1, b.Height))
                                    };
                gPath1.AddBeziers(point);
                g.DrawPath(p, gPath1);
                p.Dispose();
            }
            return b;
        }
        #endregion

        #region 畫直線
        /// <summary>
        /// 畫直線
        /// </summary>
        /// <param name="bmp">一個bmp實例</param>
        /// <param name="lineNum">線條個數</param>
        /// <returns></returns>
        public Bitmap DrawRandomLine(Int32 lineNum)
        {
            if (lineNum < 0) throw new ArgumentNullException("參數bmp爲空！");
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            b.MakeTransparent();
            Graphics g = Graphics.FromImage(b);
            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            for (int i = 0; i < lineNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point pt1 = new Point(random.Next(1, (b.Width / 5) * 2), random.Next(b.Height));
                Point pt2 = new Point(random.Next((b.Width / 5) * 3, b.Width), random.Next(b.Height));
                g.DrawLine(p, pt1, pt2);
                p.Dispose();
            }

            return b;
        }
        #endregion

        #region 畫隨機噪點
        /// <summary>
        /// 畫隨機噪點
        /// </summary>
        /// <param name="pixNum">噪點的百分比</param>
        /// <returns></returns>
        public Bitmap DrawRandomPixel(Int32 pixNum)
        {
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            b.MakeTransparent();
            Graphics graph = Graphics.FromImage(b);
            graph.SmoothingMode = SmoothingMode.HighQuality;
            graph.InterpolationMode = InterpolationMode.HighQualityBilinear;

            //畫噪點 
            for (int i = 0; i < (bgHeight * bgWidth) / pixNum; i++)
            {
                int x = random.Next(b.Width);
                int y = random.Next(b.Height);
                b.SetPixel(x, y, GetRandomDeepColor());
                //下移座標重新畫點
                if ((x + 1) < b.Width && (y + 1) < b.Height)
                {
                    //畫圖片的前景噪音點
                    graph.DrawRectangle(new Pen(Color.Silver), random.Next(b.Width), random.Next(b.Height), 1, 1);
                }

            }

            return b;
        }
        #endregion

        #region 畫隨機字符串中間連線
        /// <summary>
        /// 畫隨機字符串中間連線
        /// </summary>
        /// <returns></returns>
        private Bitmap DrawStringline()
        {
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            b.MakeTransparent();
            Graphics g = Graphics.FromImage(b);
            g.SmoothingMode = SmoothingMode.AntiAlias;

            Point[] p = new Point[validationCodeCount];
            for (int i = 0; i < validationCodeCount; i++)
            {
                p[i] = strPoint[i];
                //throw new Exception(strPoint.Length.ToString());
            }
            // g.DrawBezier(new Pen(GetRandomDeepColor()), strPoint);
            //g.DrawClosedCurve(new Pen(GetRandomDeepColor()), strPoint);
            g.DrawCurve(new Pen(GetRandomDeepColor(), 1), strPoint);

            return b;
        }
        #endregion

        #region 寫入驗證碼的字符串
        /// <summary>
        /// 寫入驗證碼的字符串
        /// </summary>
        private Bitmap DrawRandomString(string Code)
        {
            if (fontMaxSize >= (bgHeight / 5) * 4) throw new ArgumentException("字體最大值參數FontMaxSize與驗證碼高度相近，這會導致描繪驗證碼字符串時出錯，請重新設置參數！");
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            b.MakeTransparent();
            Graphics g = Graphics.FromImage(b);

            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.Half;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.TextRenderingHint = TextRenderingHint.SingleBitPerPixelGridFit;
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;

            chars = Code.ToCharArray();//拆散字符串成單字符數組
            validationCode = chars.ToString();

            //設置字體顯示格式
            StringFormat format = new StringFormat(StringFormatFlags.NoClip);
            format.Alignment = StringAlignment.Center;
            format.LineAlignment = StringAlignment.Center;
            FontFamily f = new FontFamily(GenericFontFamilies.Monospace);


            Int32 charNum = chars.Length;

            Point sPoint = new Point();
            Int32 fontSize = 12;
            for (int i = 0; i < validationCodeCount; i++)
            {
                int findex = random.Next(5);
                //定義字體
                Font textFont = new Font(f, random.Next(fontMinSize, fontMaxSize), FontStyle.Bold);
                //定義畫刷，用於寫字符串
                //Brush brush = new SolidBrush(GetRandomDeepColor());
                Int32 textFontSize = Convert.ToInt32(textFont.Size);
                fontSize = textFontSize;
                Point point = new Point(random.Next((bgWidth / charNum) * i + 5, (bgWidth / charNum) * (i + 1)), random.Next(bgHeight / 5 + textFontSize / 2, bgHeight - textFontSize / 2));



                //如果當前字符X座標小於字體的二分之一大小
                if (point.X < textFontSize / 2)
                {
                    point.X = point.X + textFontSize / 2;
                }
                //防止文字疊加
                if (i > 0 && (point.X - sPoint.X < (textFontSize / 2 + textFontSize / 2)))
                {
                    point.X = point.X + textFontSize;
                }
                //如果當前字符X座標大於圖片寬度，就減去字體的寬度
                if (point.X > (bgWidth - textFontSize / 2))
                {
                    point.X = bgWidth - textFontSize / 2;
                }

                sPoint = point;

                float angle = random.Next(-rotationAngle, rotationAngle);//轉動的度數
                g.TranslateTransform(point.X, point.Y);//移動光標到指定位置
                g.RotateTransform(angle);

                //設置漸變畫刷  
                Rectangle myretang = new Rectangle(0, 1, Convert.ToInt32(textFont.Size), Convert.ToInt32(textFont.Size));
                Color c = GetRandomDeepColor();
                LinearGradientBrush mybrush2 = new LinearGradientBrush(myretang, c, GetLightColor(c, 120), random.Next(180));

                g.DrawString(chars[i].ToString(), textFont, mybrush2, 1, 1, format);

                g.RotateTransform(-angle);//轉回去
                g.TranslateTransform(-point.X, -point.Y);//移動光標到指定位置，每個字符緊湊顯示，避免被軟件識別

                strPoint[i] = point;

                textFont.Dispose();
                mybrush2.Dispose();
            }
            return b;
        }
        #endregion

        #region 畫干擾背景文字
        /// <summary>
        /// 畫背景干擾文字
        /// </summary>
        /// <returns></returns>
        private Bitmap DrawRandBgString()
        {
            Bitmap b = new Bitmap(bgWidth, bgHeight);
            String[] randStr = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
            b.MakeTransparent();
            Graphics g = Graphics.FromImage(b);

            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;

            //設置字體顯示格式
            StringFormat format = new StringFormat(StringFormatFlags.NoClip);
            format.Alignment = StringAlignment.Center;
            format.LineAlignment = StringAlignment.Center;

            FontFamily f = new FontFamily(GenericFontFamilies.Serif);
            Font textFont = new Font(f, randomStringFontSize, FontStyle.Underline);

            int randAngle = 60; //隨機轉動角度

            for (int i = 0; i < RandomStringCount; i++)
            {

                Brush brush = new SolidBrush(GetRandomLightColor());
                Point pot = new Point(random.Next(5, bgWidth - 5), random.Next(5, bgHeight - 5));
                //隨機轉動的度數
                float angle = random.Next(-randAngle, randAngle);

                //轉動畫布
                g.RotateTransform(angle);
                g.DrawString(randStr[random.Next(randStr.Length)], textFont, brush, pot, format);
                //轉回去，爲下一個字符做準備
                g.RotateTransform(-angle);
                //釋放資源
                brush.Dispose();
            }
            textFont.Dispose();
            format.Dispose();
            f.Dispose();

            return b;
        }
        #endregion

        #region 生成隨機字符串
        /// <summary>
        /// 生成隨機字符串    
        /// </summary>
        /// <returns></returns>
        public string GetRandomString(Int32 textLength)
        {
            string[] randomArray = charCollection.Split(','); //將字符串生成數組     
            int arrayLength = randomArray.Length;
            string randomString = "";
            for (int i = 0; i < textLength; i++)
            {
                randomString += randomArray[random.Next(0, arrayLength)];
            }
            return randomString; //長度是textLength +1
        }
        #endregion

        #region 內部方法：繪製驗證碼背景
        private void DrawBackground(HatchStyle hatchStyle)
        {
            //設置填充背景時用的筆刷
            HatchBrush hBrush = new HatchBrush(hatchStyle, backColor);

            //填充背景圖片
            dc.FillRectangle(hBrush, 0, 0, this.bgWidth, this.bgHeight);
        }
        #endregion

        #region 根據指定長度，返回隨機驗證碼
        /// <summary>
        /// 根據指定長度，返回隨機驗證碼
        /// </summary>
        /// <param >制定長度</param>
        /// <returns>隨即驗證碼</returns>
        public string Next(int length)
        {
            this.validationCode = GetRandomCode(length);
            return this.validationCode;
        }
        #endregion

        #region 內部方法：返回指定長度的隨機驗證碼字符串
        /// <summary>
        /// 根據指定大小返回隨機驗證碼
        /// </summary>
        /// <param >字符串長度</param>
        /// <returns>隨機字符串</returns>
        private string GetRandomCode(int length)
        {
            StringBuilder sb = new StringBuilder(6);

            for (int i = 0; i < length; i++)
            {
                sb.Append(Char.ConvertFromUtf32(RandomAZ09()));
            }

            return sb.ToString();
        }
        #endregion

        #region 內部方法：產生隨機數和隨機點

        /// <summary>
        /// 產生0-9A-Z的隨機字符代碼
        /// </summary>
        /// <returns>字符代碼</returns>
        private int RandomAZ09()
        {
            int result = 48;
            Random ram = new Random();
            int i = ram.Next(2);

            switch (i)
            {
                case 0:
                    result = ram.Next(48, 58);
                    break;
                case 1:
                    result = ram.Next(65, 91);
                    break;
            }

            return result;
        }

        /// <summary>
        /// 返回一個隨機點，該隨機點範圍在驗證碼背景大小範圍內
        /// </summary>
        /// <returns>Point對象</returns>
        private Point RandomPoint()
        {
            Random ram = new Random();
            Point point = new Point(ram.Next(this.bgWidth), ram.Next(this.bgHeight));
            return point;
        }
        #endregion

        #region 隨機生成顏色值
        /// <summary>
        /// 生成隨機深顏色
        /// </summary>
        /// <returns></returns>
        public Color GetRandomDeepColor()
        {
            int nRed, nGreen, nBlue;    // nBlue,nRed  nGreen 相差大一點 nGreen 小一些
            //int high = 255;       
            int redLow = 160;
            int greenLow = 100;
            int blueLow = 160;
            nRed = random.Next(redLow);
            nGreen = random.Next(greenLow);
            nBlue = random.Next(blueLow);
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }

        /// <summary>
        /// 生成隨機淺顏色
        /// </summary>
        /// <returns>randomColor</returns>
        public Color GetRandomLightColor()
        {
            int nRed, nGreen, nBlue;    //越大顏色越淺
            int low = 180;           //色彩的下限
            int high = 255;          //色彩的上限      
            nRed = random.Next(high) % (high - low) + low;
            nGreen = random.Next(high) % (high - low) + low;
            nBlue = random.Next(high) % (high - low) + low;
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }
        /// <summary>
        /// 生成隨機顏色值
        /// </summary>
        /// <returns></returns>
        public Color GetRandomColor()
        {
            int nRed, nGreen, nBlue;    //越大顏色越淺
            int low = 10;           //色彩的下限
            int high = 255;          //色彩的上限    
            nRed = random.Next(high) % (high - low) + low;
            nGreen = random.Next(high) % (high - low) + low;
            nBlue = random.Next(high) % (high - low) + low;
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }
        /// <summary>
        /// 獲取與當前顏色值相加後的顏色
        /// </summary>
        /// <param name="c"></param>
        /// <returns></returns>
        public Color GetLightColor(Color c, Int32 value)
        {
            int nRed = c.R, nGreen = c.G, nBlue = c.B;    //越大顏色越淺
            if (nRed + value < 255 && nRed + value > 0)
            {
                nRed = c.R + 40;
            }
            if (nGreen + value < 255 && nGreen + value > 0)
            {
                nGreen = c.G + 40;
            }
            if (nBlue + value < 255 && nBlue + value > 0)
            {
                nBlue = c.B + 40;
            }
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }
        #endregion

        #region 合併圖片
        /// <summary>       
        /// 合併圖片        
        /// </summary>        
        /// <param name="maps"></param>        
        /// <returns></returns>        
        private Bitmap MergerImg(params Bitmap[] maps)
        {
            int i = maps.Length;
            if (i == 0)
                throw new Exception("圖片數不能夠爲0");
            //創建要顯示的圖片對象,根據參數的個數設置寬度            
            Bitmap backgroudImg = new Bitmap(i * 12, 16);
            Graphics g = Graphics.FromImage(backgroudImg);
            //清除畫布,背景設置爲白色            
            g.Clear(Color.White);
            for (int j = 0; j < i; j++)
            {
                //g.DrawImage(maps[j], j * 11, 0, maps[j].Width, maps[j].Height);
                g.DrawImageUnscaled(maps[j], 0, 0);
            }
            g.Dispose();
            return backgroudImg;
        }
        #endregion

        #region 生成不重複的隨機數，該函數會消耗大量系統資源
        /// <summary>
        /// 生成不重複的隨機數，該函數會消耗大量系統資源
        /// </summary>
        /// <returns></returns>
        private static int GetRandomSeed()
        {
            byte[] bytes = new byte[4];
            System.Security.Cryptography.RNGCryptoServiceProvider rng = new System.Security.Cryptography.RNGCryptoServiceProvider();
            rng.GetBytes(bytes);
            return BitConverter.ToInt32(bytes, 0);
        }
        #endregion

        #region 縮放圖片
        /// <summary>
        /// 縮放圖片
        /// </summary>
        /// <param name="bmp">原始Bitmap</param>
        /// <param name="newW">新的寬度</param>
        /// <param name="newH">新的高度</param>
        /// <param name="Mode">縮放質量</param>
        /// <returns>處理以後的圖片</returns>
        public static Bitmap KiResizeImage(Bitmap bmp, int newW, int newH, InterpolationMode Mode)
        {
            try
            {
                Bitmap b = new Bitmap(newW, newH);
                Graphics g = Graphics.FromImage(b);
                // 插值算法的質量
                g.InterpolationMode = Mode;
                g.DrawImage(bmp, new Rectangle(0, 0, newW, newH), new Rectangle(0, 0, bmp.Width, bmp.Height), GraphicsUnit.Pixel);
                g.Dispose();
                return b;
            }
            catch
            {
                return null;
            }
        }
        #endregion

        #region 繪製圓角矩形
        /// <summary>
        /// C# GDI+ 繪製圓角矩形
        /// </summary>
        /// <param name="g">Graphics 對象</param>
        /// <param name="rectangle">Rectangle 對象，圓角矩形區域</param>
        /// <param name="borderColor">邊框顏色</param>
        /// <param name="borderWidth">邊框寬度</param>
        /// <param name="r">圓角半徑</param>
        private static void DrawRoundRectangle(Graphics g, Rectangle rectangle, Color borderColor, float borderWidth, int r)
        {
            // 如要使邊緣平滑，請取消下行的註釋
            g.SmoothingMode = SmoothingMode.HighQuality;

            // 由於邊框也需要一定寬度，需要對矩形進行修正
            //rectangle = new Rectangle(rectangle.X, rectangle.Y, rectangle.Width, rectangle.Height);
            Pen p = new Pen(borderColor, borderWidth);
            // 調用 getRoundRectangle 得到圓角矩形的路徑，然後再進行繪製
            g.DrawPath(p, getRoundRectangle(rectangle, r));
        }
        #endregion

        #region 根據普通矩形得到圓角矩形的路徑
        /// <summary>
        /// 根據普通矩形得到圓角矩形的路徑
        /// </summary>
        /// <param name="rectangle">原始矩形</param>
        /// <param name="r">半徑</param>
        /// <returns>圖形路徑</returns>
        private static GraphicsPath getRoundRectangle(Rectangle rectangle, int r)
        {
            int l = 2 * r;
            // 把圓角矩形分成八段直線、弧的組合，依次加到路徑中
            GraphicsPath gp = new GraphicsPath();
            gp.AddLine(new Point(rectangle.X + r, rectangle.Y), new Point(rectangle.Right - r, rectangle.Y));
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Y, l, l), 270F, 90F);

            gp.AddLine(new Point(rectangle.Right, rectangle.Y + r), new Point(rectangle.Right, rectangle.Bottom - r));
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Bottom - l, l, l), 0F, 90F);

            gp.AddLine(new Point(rectangle.Right - r, rectangle.Bottom), new Point(rectangle.X + r, rectangle.Bottom));
            gp.AddArc(new Rectangle(rectangle.X, rectangle.Bottom - l, l, l), 90F, 90F);

            gp.AddLine(new Point(rectangle.X, rectangle.Bottom - r), new Point(rectangle.X, rectangle.Y + r));
            gp.AddArc(new Rectangle(rectangle.X, rectangle.Y, l, l), 180F, 90F);
            return gp;
        }
        #endregion

        #region 柔化
        ///<summary>
        /// 柔化
        /// </summary>
        /// <param name="b">原始圖</param>
        /// <returns>輸出圖</returns>
        public static Bitmap KiBlur(Bitmap b)
        {

            if (b == null)
            {
                return null;
            }

            int w = b.Width;
            int h = b.Height;

            try
            {

                Bitmap bmpRtn = new Bitmap(w, h, PixelFormat.Format24bppRgb);

                BitmapData srcData = b.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
                BitmapData dstData = bmpRtn.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.WriteOnly, PixelFormat.Format24bppRgb);

                unsafe
                {
                    byte* pIn = (byte*)srcData.Scan0.ToPointer();
                    byte* pOut = (byte*)dstData.Scan0.ToPointer();
                    int stride = srcData.Stride;
                    byte* p;

                    for (int y = 0; y < h; y++)
                    {
                        for (int x = 0; x < w; x++)
                        {
                            //取周圍9點的值
                            if (x == 0 || x == w - 1 || y == 0 || y == h - 1)
                            {
                                //不做
                                pOut[0] = pIn[0];
                                pOut[1] = pIn[1];
                                pOut[2] = pIn[2];
                            }
                            else
                            {
                                int r1, r2, r3, r4, r5, r6, r7, r8, r9;
                                int g1, g2, g3, g4, g5, g6, g7, g8, g9;
                                int b1, b2, b3, b4, b5, b6, b7, b8, b9;

                                float vR, vG, vB;

                                //左上
                                p = pIn - stride - 3;
                                r1 = p[2];
                                g1 = p[1];
                                b1 = p[0];

                                //正上
                                p = pIn - stride;
                                r2 = p[2];
                                g2 = p[1];
                                b2 = p[0];

                                //右上
                                p = pIn - stride + 3;
                                r3 = p[2];
                                g3 = p[1];
                                b3 = p[0];

                                //左側
                                p = pIn - 3;
                                r4 = p[2];
                                g4 = p[1];
                                b4 = p[0];

                                //右側
                                p = pIn + 3;
                                r5 = p[2];
                                g5 = p[1];
                                b5 = p[0];

                                //右下
                                p = pIn + stride - 3;
                                r6 = p[2];
                                g6 = p[1];
                                b6 = p[0];

                                //正下
                                p = pIn + stride;
                                r7 = p[2];
                                g7 = p[1];
                                b7 = p[0];

                                //右下
                                p = pIn + stride + 3;
                                r8 = p[2];
                                g8 = p[1];
                                b8 = p[0];

                                //自己
                                p = pIn;
                                r9 = p[2];
                                g9 = p[1];
                                b9 = p[0];

                                vR = (float)(r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9);
                                vG = (float)(g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9);
                                vB = (float)(b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9);

                                vR /= 9;
                                vG /= 9;
                                vB /= 9;

                                pOut[0] = (byte)vB;
                                pOut[1] = (byte)vG;
                                pOut[2] = (byte)vR;

                            }

                            pIn += 3;
                            pOut += 3;
                        }// end of x

                        pIn += srcData.Stride - w * 3;
                        pOut += srcData.Stride - w * 3;
                    } // end of y
                }

                b.UnlockBits(srcData);
                bmpRtn.UnlockBits(dstData);

                return bmpRtn;
            }
            catch
            {
                return null;
            }

        } // end of KiBlur
        #endregion

        #region 濾鏡
        /// <summary>
        /// 紅色濾鏡
        /// </summary>
        /// <param name="bitmap">Bitmap</param>
        /// <param name="threshold">閥值 -255~255</param>
        /// <returns></returns>
        public Bitmap AdjustToRed(Bitmap bitmap, int threshold)
        {
            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap.GetPixel(x, y);
                    var pR = pixel.R + threshold;
                    pR = Math.Max(pR, 0);
                    pR = Math.Min(255, pR);
                    // 將改過的 RGB 寫回
                    // 只寫入紅色的值 , G B 都放零
                    Color newColor = Color.FromArgb(pixel.A, pR, 0, 0);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap;
        }

        /// <summary>
        /// 綠色濾鏡
        /// </summary>
        /// <param name="bitmap">一個圖片實例</param>
        /// <param name="threshold">閥值 -255~+255</param>
        /// <returns></returns>
        public Bitmap AdjustToGreen(Bitmap bitmap, int threshold)
        {
            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap.GetPixel(x, y);
                    //判斷是否超過255 如果超過就是255 
                    var pG = pixel.G + threshold;
                    //如果小於0就為0
                    if (pG > 255) pG = 255;
                    if (pG < 0) pG = 0;
                    // 將改過的 RGB 寫回
                    // 只寫入綠色的值 , R B 都放零
                    Color newColor = Color.FromArgb(pixel.A, 0, pG, 0);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap;
        }
        /// <summary>
        /// 藍色濾鏡
        /// </summary>
        /// <param name="bitmap">一個圖片實例</param>
        /// <param name="threshold">閥值 -255~255</param>
        /// <returns></returns>
        public Bitmap AdjustToBlue(Bitmap bitmap, int threshold)
        {
            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap.GetPixel(x, y);
                    //判斷是否超過255 如果超過就是255 
                    var pB = pixel.B + threshold;
                    //如果小於0就為0
                    if (pB > 255) pB = 255;
                    if (pB < 0) pB = 0;
                    // 將改過的 RGB 寫回
                    // 只寫入藍色的值 , R G 都放零
                    Color newColor = Color.FromArgb(pixel.A, 0, 0, pB);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap;
        }
        /// <summary>
        /// 調整 RGB 色調
        /// </summary>
        /// <param name="bitmap"></param>
        /// <param name="thresholdRed">紅色閥值</param>
        /// <param name="thresholdBlue">藍色閥值</param>
        /// <param name="thresholdGreen">綠色閥值</param>
        /// <returns></returns>
        public Bitmap AdjustToCustomColor(Bitmap bitmap, int thresholdRed, int thresholdGreen, int thresholdBlue)
        {
            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap.GetPixel(x, y);
                    //判斷是否超過255 如果超過就是255 
                    var pG = pixel.G + thresholdGreen;
                    //如果小於0就為0
                    if (pG > 255) pG = 255;
                    if (pG < 0) pG = 0;
                    //判斷是否超過255 如果超過就是255 
                    var pR = pixel.R + thresholdRed;
                    //如果小於0就為0
                    if (pR > 255) pR = 255;
                    if (pR < 0) pR = 0;
                    //判斷是否超過255 如果超過就是255 
                    var pB = pixel.B + thresholdBlue;
                    //如果小於0就為0
                    if (pB > 255) pB = 255;
                    if (pB < 0) pB = 0;
                    // 將改過的 RGB 寫回
                    // 只寫入綠色的值 , R B 都放零
                    Color newColor = Color.FromArgb(pixel.A, pR, pG, pB);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            return bitmap;
        }
        #endregion

        #region 圖片去色（圖片黑白化）
        /// <summary>
        /// 圖片去色（圖片黑白化）
        /// </summary>
        /// <param name="original">一個需要處理的圖片</param>
        /// <returns></returns>
        public static Bitmap MakeGrayscale(Bitmap original)
        {
            //create a blank bitmap the same size as original
            Bitmap newBitmap = new Bitmap(original.Width, original.Height);

            //get a graphics object from the new image
            Graphics g = Graphics.FromImage(newBitmap);
            g.SmoothingMode = SmoothingMode.HighQuality;
            //create the grayscale ColorMatrix
            ColorMatrix colorMatrix = new ColorMatrix(new float[][] 
                              {
                                 new float[] {.3f, .3f, .3f, 0, 0},
                                 new float[] {.59f, .59f, .59f, 0, 0},
                                 new float[] {.11f, .11f, .11f, 0, 0},
                                 new float[] {0, 0, 0, 1, 0},
                                 new float[] {0, 0, 0, 0, 1}
                              });

            //create some image attributes
            ImageAttributes attributes = new ImageAttributes();

            //set the color matrix attribute
            attributes.SetColorMatrix(colorMatrix);

            //draw the original image on the new image
            //using the grayscale color matrix
            g.DrawImage(original, new Rectangle(0, 0, original.Width, original.Height),
               0, 0, original.Width, original.Height, GraphicsUnit.Pixel, attributes);

            //dispose the Graphics object
            g.Dispose();
            return newBitmap;
        }
        #endregion

        #region 增加或減少亮度
        /// <summary>
        /// 增加或減少亮度
        /// </summary>
        /// <param name="img">Image Source </param>
        /// <param name="valBrightness">0~255</param>
        /// <returns></returns>
        public Bitmap AdjustBrightness(Image img, int valBrightness)
        {
            // 讀入欲轉換的圖片並轉成為 Bitmap
            Bitmap bitmap = new Bitmap(img);

            for (int y = 0; y < bitmap.Height; y++)
            {
                for (int x = 0; x < bitmap.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap.GetPixel(x, y);

                    // 判斷 如果處理過後 255 就設定為 255 如果小於則設定為 0
                    var pR = ((pixel.R + valBrightness > 255) ? 255 : pixel.R + valBrightness) < 0 ? 0 : ((pixel.R + valBrightness > 255) ? 255 : pixel.R + valBrightness);
                    var pG = ((pixel.G + valBrightness > 255) ? 255 : pixel.G + valBrightness) < 0 ? 0 : ((pixel.G + valBrightness > 255) ? 255 : pixel.G + valBrightness);
                    var pB = ((pixel.B + valBrightness > 255) ? 255 : pixel.B + valBrightness) < 0 ? 0 : ((pixel.B + valBrightness > 255) ? 255 : pixel.B + valBrightness);

                    // 將改過的 RGB 寫回
                    Color newColor = Color.FromArgb(pixel.A, pR, pG, pB);

                    bitmap.SetPixel(x, y, newColor);

                }
            }
            // 回傳結果
            return bitmap;
        }
        #endregion

        #region 浮雕效果
        /// <summary>
        /// 浮雕效果
        /// </summary>
        /// <param name="src">一個圖片實例</param>
        /// <returns></returns>
        public Bitmap AdjustToStone(Bitmap src)
        {
            // 依照 Format24bppRgb 每三個表示一 Pixel 0: 藍 1: 綠 2: 紅
            BitmapData bitmapData = src.LockBits(new Rectangle(0, 0, src.Width, src.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                // 抓住第一個 Pixel 第一個數值
                byte* p = (byte*)(void*)bitmapData.Scan0;

                // 跨步值 - 寬度 *3 可以算出畸零地 之後跳到下一行
                int nOffset = bitmapData.Stride - src.Width * 3;

                for (int y = 0; y < src.Height; ++y)
                {
                    for (int x = 0; x < src.Width; ++x)
                    {
                        // 爲了理解方便 所以特地在命名
                        int r, g, b;
                        // 先取得下一個 Pixel
                        var q = p + 3;
                        r = Math.Abs(p[2] - q[2] + 128);
                        r = r < 0 ? 0 : r;
                        r = r > 255 ? 255 : r;
                        p[2] = (byte)r;

                        g = Math.Abs(p[1] - q[1] + 128);
                        g = g < 0 ? 0 : g;
                        g = g > 255 ? 255 : g;
                        p[1] = (byte)g;

                        b = Math.Abs(p[0] - q[0] + 128);
                        b = b < 0 ? 0 : b;
                        b = b > 255 ? 255 : b;
                        p[0] = (byte)b;

                        // 跳去下一個 Pixel
                        p += 3;

                    }
                    // 跨越畸零地
                    p += nOffset;
                }
            }
            src.UnlockBits(bitmapData);
            return src;
        }
        #endregion

        #region 水波紋效果
        /// <summary>
        /// 水波紋效果
        /// </summary>
        /// <param name="src"></param>
        /// <param name="nWave">坡度</param>
        /// www.it165.net
        /// <returns></returns>
        public Bitmap AdjustRippleEffect(Bitmap src, short nWave)
        {

            int nWidth = src.Width;
            int nHeight = src.Height;

            // 透過公式進行水波紋的採樣

            PointF[,] fp = new PointF[nWidth, nHeight];

            Point[,] pt = new Point[nWidth, nHeight];

            Point mid = new Point();
            mid.X = nWidth / 2;
            mid.Y = nHeight / 2;

            double newX, newY;
            double xo, yo;

            //先取樣將水波紋座標跟RGB取出
            for (int x = 0; x < nWidth; ++x)
                for (int y = 0; y < nHeight; ++y)
                {
                    xo = ((double)nWave * Math.Sin(2.0 * 3.1415 * (float)y / 128.0));
                    yo = ((double)nWave * Math.Cos(2.0 * 3.1415 * (float)x / 128.0));

                    newX = (x + xo);
                    newY = (y + yo);

                    if (newX > 0 && newX < nWidth)
                    {
                        fp[x, y].X = (float)newX;
                        pt[x, y].X = (int)newX;
                    }
                    else
                    {
                        fp[x, y].X = (float)0.0;
                        pt[x, y].X = 0;
                    }


                    if (newY > 0 && newY < nHeight)
                    {
                        fp[x, y].Y = (float)newY;
                        pt[x, y].Y = (int)newY;
                    }
                    else
                    {
                        fp[x, y].Y = (float)0.0;
                        pt[x, y].Y = 0;
                    }
                }


            //進行合成
            Bitmap bSrc = (Bitmap)src.Clone();

            // 依照 Format24bppRgb 每三個表示一 Pixel 0: 藍 1: 綠 2: 紅
            BitmapData bitmapData = src.LockBits(new Rectangle(0, 0, src.Width, src.Height), ImageLockMode.ReadWrite,
                                           PixelFormat.Format24bppRgb);
            BitmapData bmSrc = bSrc.LockBits(new Rectangle(0, 0, bSrc.Width, bSrc.Height), ImageLockMode.ReadWrite,
                                             PixelFormat.Format24bppRgb);

            int scanline = bitmapData.Stride;

            IntPtr Scan0 = bitmapData.Scan0;
            IntPtr SrcScan0 = bmSrc.Scan0;

            unsafe
            {
                byte* p = (byte*)(void*)Scan0;
                byte* pSrc = (byte*)(void*)SrcScan0;

                int nOffset = bitmapData.Stride - src.Width * 3;

                int xOffset, yOffset;

                for (int y = 0; y < nHeight; ++y)
                {
                    for (int x = 0; x < nWidth; ++x)
                    {
                        xOffset = pt[x, y].X;
                        yOffset = pt[x, y].Y;

                        if (yOffset >= 0 && yOffset < nHeight && xOffset >= 0 && xOffset < nWidth)
                        {
                            p[0] = pSrc[(yOffset * scanline) + (xOffset * 3)];
                            p[1] = pSrc[(yOffset * scanline) + (xOffset * 3) + 1];
                            p[2] = pSrc[(yOffset * scanline) + (xOffset * 3) + 2];
                        }

                        p += 3;
                    }
                    p += nOffset;
                }
            }

            src.UnlockBits(bitmapData);
            bSrc.UnlockBits(bmSrc);

            return src;
        }
        #endregion

        #region 調整曝光度值
        /// <summary>
        /// 調整曝光度值
        /// </summary>
        /// <param name="src">原圖</param>
        /// <param name="r"></param>
        /// <param name="g"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        public Bitmap AdjustGamma(Bitmap src, double r, double g, double b)
        {
            // 判斷是不是在0.2~5 之間
            r = Math.Min(Math.Max(0.2, r), 5);
            g = Math.Min(Math.Max(0.2, g), 5);
            b = Math.Min(Math.Max(0.2, b), 5);

            // 依照 Format24bppRgb 每三個表示一 Pixel 0: 藍 1: 綠 2: 紅
            BitmapData bitmapData = src.LockBits(new Rectangle(0, 0, src.Width, src.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            unsafe
            {
                // 抓住第一個 Pixel 第一個數值
                byte* p = (byte*)(void*)bitmapData.Scan0;

                // 跨步值 - 寬度 *3 可以算出畸零地 之後跳到下一行
                int nOffset = bitmapData.Stride - src.Width * 3;

                for (int y = 0; y < src.Height; y++)
                {
                    for (int x = 0; x < src.Width; x++)
                    {
                        p[2] = (byte)Math.Min(255, (int)((255.0 * Math.Pow(p[2] / 255.0, 1.0 / r)) + 0.5));
                        p[1] = (byte)Math.Min(255, (int)((255.0 * Math.Pow(p[1] / 255.0, 1.0 / g)) + 0.5));
                        p[0] = (byte)Math.Min(255, (int)((255.0 * Math.Pow(p[0] / 255.0, 1.0 / b)) + 0.5));


                        // 跳去下一個 Pixel
                        p += 3;

                    }
                    // 跨越畸零地
                    p += nOffset;
                }
            }
            src.UnlockBits(bitmapData);
            return src;

        }
        #endregion

        #region 高對比,對過深的顏色調淺，過淺的顏色調深。
        /// <summary>
        /// 高對比,對過深的顏色調淺，過淺的顏色調深。
        /// </summary>
        /// <param name="src"></param>
        /// <param name="effectThreshold"> 高對比程度 -100~100</param>
        /// <returns></returns>
        public Bitmap Contrast(Bitmap src, float effectThreshold)
        {

            // 依照 Format24bppRgb 每三個表示一 Pixel 0: 藍 1: 綠 2: 紅
            BitmapData bitmapData = src.LockBits(new Rectangle(0, 0, src.Width, src.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

            // 判斷是否在 -100~100
            effectThreshold = effectThreshold < -100 ? -100 : effectThreshold;
            effectThreshold = effectThreshold > 100 ? 100 : effectThreshold;

            effectThreshold = (float)((100.0 + effectThreshold) / 100.0);
            effectThreshold *= effectThreshold;

            unsafe
            {
                // 抓住第一個 Pixel 第一個數值 www.it165.net
                byte* p = (byte*)(void*)bitmapData.Scan0;

                // 跨步值 - 寬度 *3 可以算出畸零地 之後跳到下一行
                int nOffset = bitmapData.Stride - src.Width * 3;



                for (int y = 0; y < src.Height; y++)
                {
                    for (int x = 0; x < src.Width; x++)
                    {
                        double buffer = 0;


                        // 公式  (Red/255)-0.5= 偏離中間值程度
                        // ((偏離中間值程度 * 影響範圍)+0.4 ) * 255
                        buffer = ((((p[2] / 255.0) - 0.5) * effectThreshold) + 0.5) * 255.0;
                        buffer = buffer > 255 ? 255 : buffer;
                        buffer = buffer < 0 ? 0 : buffer;
                        p[2] = (byte)buffer;

                        buffer = ((((p[1] / 255.0) - 0.5) * effectThreshold) + 0.5) * 255.0;
                        buffer = buffer > 255 ? 255 : buffer;
                        buffer = buffer < 0 ? 0 : buffer;
                        p[1] = (byte)buffer;


                        buffer = ((((p[0] / 255.0) - 0.5) * effectThreshold) + 0.5) * 255.0;
                        buffer = buffer > 255 ? 255 : buffer;
                        buffer = buffer < 0 ? 0 : buffer;
                        p[0] = (byte)buffer;




                        // 跳去下一個 Pixel
                        p += 3;

                    }
                    // 跨越畸零地
                    p += nOffset;
                }
            }
            src.UnlockBits(bitmapData);
            return src;


        }
        #endregion

        #region 對圖片進行霧化效果
        /// <summary>
        /// 對圖片進行霧化效果
        /// </summary>
        /// <param name="bmp"></param>
        /// <returns></returns>
        public Bitmap Atomization(Bitmap bmp)
        {

            int Height = bmp.Height;
            int Width = bmp.Width;
            Bitmap newBitmap = new Bitmap(Width, Height);
            Bitmap oldBitmap = bmp;
            Color pixel;
            for (int x = 1; x < Width - 1; x++)
            {
                for (int y = 1; y < Height - 1; y++)
                {
                    Random MyRandom = new Random(Guid.NewGuid().GetHashCode());
                    int k = MyRandom.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= Width)
                        dx = Width - 1;
                    if (dy >= Height)
                        dy = Height - 1;
                    pixel = oldBitmap.GetPixel(dx, dy);
                    newBitmap.SetPixel(x, y, pixel);
                }
            }
            return newBitmap;
        }
        #endregion

    } //END Class DrawValidationCode
    #endregion

    #region 高斯模糊算法
    /// <summary>
    /// 高斯模糊算法
    /// </summary>
    public class Gaussian
    {
        public static double[,] Calculate1DSampleKernel(double deviation, int size)
        {
            double[,] ret = new double[size, 1];
            double sum = 0;
            int half = size / 2;
            for (int i = 0; i < size; i++)
            {
                ret[i, 0] = 1 / (Math.Sqrt(2 * Math.PI) * deviation) * Math.Exp(-(i - half) * (i - half) / (2 * deviation * deviation));
                sum += ret[i, 0];
            }
            return ret;
        }
        public static double[,] Calculate1DSampleKernel(double deviation)
        {
            int size = (int)Math.Ceiling(deviation * 3) * 2 + 1;
            return Calculate1DSampleKernel(deviation, size);
        }
        public static double[,] CalculateNormalized1DSampleKernel(double deviation)
        {
            return NormalizeMatrix(Calculate1DSampleKernel(deviation));
        }
        public static double[,] NormalizeMatrix(double[,] matrix)
        {
            double[,] ret = new double[matrix.GetLength(0), matrix.GetLength(1)];
            double sum = 0;
            for (int i = 0; i < ret.GetLength(0); i++)
            {
                for (int j = 0; j < ret.GetLength(1); j++)
                    sum += matrix[i, j];
            }
            if (sum != 0)
            {
                for (int i = 0; i < ret.GetLength(0); i++)
                {
                    for (int j = 0; j < ret.GetLength(1); j++)
                        ret[i, j] = matrix[i, j] / sum;
                }
            }
            return ret;
        }
        public static double[,] GaussianConvolution(double[,] matrix, double deviation)
        {
            double[,] kernel = CalculateNormalized1DSampleKernel(deviation);
            double[,] res1 = new double[matrix.GetLength(0), matrix.GetLength(1)];
            double[,] res2 = new double[matrix.GetLength(0), matrix.GetLength(1)];
            //x-direction
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                    res1[i, j] = processPoint(matrix, i, j, kernel, 0);
            }
            //y-direction
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                    res2[i, j] = processPoint(res1, i, j, kernel, 1);
            }
            return res2;
        }
        private static double processPoint(double[,] matrix, int x, int y, double[,] kernel, int direction)
        {
            double res = 0;
            int half = kernel.GetLength(0) / 2;
            for (int i = 0; i < kernel.GetLength(0); i++)
            {
                int cox = direction == 0 ? x + i - half : x;
                int coy = direction == 1 ? y + i - half : y;
                if (cox >= 0 && cox < matrix.GetLength(0) && coy >= 0 && coy < matrix.GetLength(1))
                {
                    res += matrix[cox, coy] * kernel[i, 0];
                }
            }
            return res;
        }
        /// <summary>
        /// 對顏色值進行灰色處理
        /// </summary>
        /// <param name="cr"></param>
        /// <returns></returns>
        private Color grayscale(Color cr)
        {
            return Color.FromArgb(cr.A, (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11),
               (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11),
              (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11));
        }
        /// <summary>
        /// 對圖片進行高斯模糊
        /// </summary>
        /// <param name="d">模糊數值，數值越大模糊越很</param>
        /// <param name="image">一個需要處理的圖片</param>
        /// <returns></returns>
        public Bitmap FilterProcessImage(double d, Bitmap image)
        {
            Bitmap ret = new Bitmap(image.Width, image.Height);
            Double[,] matrixR = new Double[image.Width, image.Height];
            Double[,] matrixG = new Double[image.Width, image.Height];
            Double[,] matrixB = new Double[image.Width, image.Height];
            for (int i = 0; i < image.Width; i++)
            {
                for (int j = 0; j < image.Height; j++)
                {
                    //matrix[i, j] = grayscale(image.GetPixel(i, j)).R;
                    matrixR[i, j] = image.GetPixel(i, j).R;
                    matrixG[i, j] = image.GetPixel(i, j).G;
                    matrixB[i, j] = image.GetPixel(i, j).B;
                }
            }
            matrixR = Gaussian.GaussianConvolution(matrixR, d);
            matrixG = Gaussian.GaussianConvolution(matrixG, d);
            matrixB = Gaussian.GaussianConvolution(matrixB, d);
            for (int i = 0; i < image.Width; i++)
            {
                for (int j = 0; j < image.Height; j++)
                {
                    Int32 R = (int)Math.Min(255, matrixR[i, j]);
                    Int32 G = (int)Math.Min(255, matrixG[i, j]);
                    Int32 B = (int)Math.Min(255, matrixB[i, j]);
                    ret.SetPixel(i, j, Color.FromArgb(R, G, B));
                }
            }
            return ret;
        }

    }
    #endregion

    public class DrawValImg
    {
        /// <summary>
        /// 無參構造
        /// </summary>
        public DrawValImg() { }
        /// <summary>
        /// 帶有生成字符個數的構造
        /// </summary>
        /// <param name="charNum">驗證碼中包含隨機字符的個數</param>
        public DrawValImg(int charNum)
        {
            this.CharNum = charNum;
        }
        /// <summary>
        /// 帶有驗證碼圖片寬度和高度的構造
        /// </summary>
        /// <param name="width">驗證碼圖片寬度</param>
        /// <param name="height">驗證碼圖片高度</param>
        public DrawValImg(int width, int height)
        {
            this.width = width;
            this.height = height;
        }
        /// <summary>
        /// 帶有生成字符個數，驗證碼圖片寬度和高度的構造
        /// </summary>
        /// <param name="charNum">驗證碼中包含隨機字符的個數</param>
        /// <param name="width">驗證碼圖片寬度</param>
        /// <param name="height">驗證碼圖片高度</param>
        public DrawValImg(int charNum, int width, int height)
        {
            this.CharNum = charNum;
            this.width = width;
            this.height = height;
        }
        /// <summary>
        /// 驗證碼中字符個數
        /// </summary>
        int charNum = 5; //默認字符個數為5
        public int CharNum
        {
            get { return charNum; }
            set { charNum = value; }
        }
        /// <summary>
        /// 字號
        /// </summary>
        int fontSize = 20;
        public int FontSize
        {
            get { return fontSize; }
        }
        /// <summary>
        /// 圖片寬度
        /// </summary>
        int width = 200;
        public int Width
        {
            get { return width; }
        }
        /// <summary>
        /// 圖片高度
        /// </summary>
        int height = 45;
        public int Height
        {
            get { return height; }
            set { height = value; }
        }
        /// <summary>
        /// 隨機生成的字符串
        /// </summary>
        string validStr = "";
        public string ValidStr
        {
            get { return validStr; }
            set { validStr = value; }
        }
        /// <summary>
        /// 產生指定個數的隨機字符串，默認字符個數為5
        /// </summary>
        void GetValidateCode()
        {
            Random rd = new Random(); //創建隨機數對象
            //產生由 charNum 個字母或數字組成的一個字符串
            string str = "abcdefghijkmnpqrstuvwyzABCDEFGHJKLMNPQRSTUVWYZ23456789田國興";//共57個字符，除 l,o,x,I,O,X,1,0 的所有數字和大寫字母
            for (int i = 0; i < charNum; i++)
            {
                validStr = validStr + str.Substring(rd.Next(57), 1);//返回0到56共57個
            }
        }
        /// <summary>
        /// 由隨機字符串，隨即顏色背景，和隨機線條產生的Image
        /// </summary>
        /// <returns>Image</returns>
        public Image GetImgWithValidateCode()//返回 Image
        {
            //產生隨機字符串
            GetValidateCode();
            //聲明一個位圖對象
            Bitmap bitMap = null;
            //聲明一個繪圖畫面
            Graphics gph = null;
            //創建內存流
            MemoryStream memStream = new MemoryStream();
            Random random = new Random();
            //由給定的需要生成字符串中字符個數 CharNum， 圖片寬度 Width 和高度 Height 確定字號 FontSize，
            //確保不因字號過大而不能全部顯示在圖片上
            int fontWidth = (int)Math.Round(width / (charNum + 2) / 1.3);
            int fontHeight = (int)Math.Round(height / 1.5);
            //字號取二者中小者，以確保所有字符能夠顯示，並且字符的下半部分也能顯示
            fontSize = fontWidth <= fontHeight ? fontWidth : fontHeight;
            //創建位圖對象
            bitMap = new Bitmap(width + FontSize, height);
            //根據上面創建的位圖對象創建繪圖圖面
            gph = Graphics.FromImage(bitMap);
            //設定驗證碼圖片背景色
            gph.Clear(GetControllableColor(200));
            //產生隨機干擾線條
            for (int i = 0; i < 10; i++)
            {
                Pen backPen = new Pen(GetControllableColor(100), 2);
                //線條起點
                int x = random.Next(width);
                int y = random.Next(height);
                //線條終點
                int x2 = random.Next(width);
                int y2 = random.Next(height);
                //劃線
                gph.DrawLine(backPen, x, y, x2, y2);
            }
            //定義一個含10種字體的數組
            String[] fontFamily ={ "Arial", "Verdana", "Comic Sans MS", "Impact", "Haettenschweiler",
"Lucida Sans Unicode", "Garamond", "Courier New", "Book Antiqua", "Arial Narrow" };

            SolidBrush sb = new SolidBrush(GetControllableColor(0));
            //通過循環,繪制每個字符,
            for (int i = 0; i < validStr.Length; i++)
            {
                Font textFont = new Font(fontFamily[random.Next(10)], fontSize, FontStyle.Bold);//字體隨機,字號大小30,加粗
                //每次循環繪制一個字符,設置字體格式,畫筆顏色,字符相對畫布的X坐標,字符相對畫布的Y坐標
                int space = (int)Math.Round((double)((width - fontSize * (CharNum + 2)) / CharNum));
                //縱坐標
                int y = (int)Math.Round((double)((height - fontSize) / 3));
                gph.DrawString(validStr.Substring(i, 1), textFont, sb, fontSize + i * (fontSize + space), y);
            }
            //扭曲圖片
            bitMap = TwistImage(bitMap, true, random.Next(3, 5), random.Next(3));
            try
            {
                bitMap.Save(memStream, ImageFormat.Gif);
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
            //gph.Dispose();
            bitMap.Dispose();
            Image img = Image.FromStream(memStream);
            gph.DrawImage(img, 50, 20, width, 10);
            return img;
        }
        /// <summary>
        /// 產生一種 R,G,B 均大於 colorBase 隨機顏色，以確保顏色不會過深
        /// </summary>
        /// <returns>背景色</returns>
        Color GetControllableColor(int colorBase)
        {
            Color color = Color.Black;
            if (colorBase > 200)
            {
                System.Windows.Forms.MessageBox.Show("可控制顏色參數大於200，顏色默認位黑色");
            }
            Random random = new Random();
            //確保 R,G,B 均大於 colorBase，這樣才能保證背景色較淺
            color = Color.FromArgb(random.Next(56) + colorBase, random.Next(56) + colorBase, random.Next(56) + colorBase);
            return color;
        }
        /// <summary>
        /// 扭曲圖片
        /// </summary>
        /// <param name="srcBmp"></param>
        /// <param name="bXDir"></param>
        /// <param name="dMultValue"></param>
        /// <param name="dPhase"></param>
        /// <returns></returns>
        Bitmap TwistImage(Bitmap srcBmp, bool bXDir, double dMultValue, double dPhase)
        {
            int leftMargin = 0;
            int rightMargin = 0;
            int topMargin = 0;
            int bottomMargin = 0;
            //float PI = 3.14159265358979f;
            float PI2 = 6.28318530717959f;
            Bitmap destBmp = new Bitmap(srcBmp.Width, srcBmp.Height);
            double dBaseAxisLen = bXDir ? Convert.ToDouble(destBmp.Height) : Convert.ToDouble(destBmp.Width);
            for (int i = 0; i < destBmp.Width; i++)
            {
                for (int j = 0; j < destBmp.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? PI2 * Convert.ToDouble(j) / dBaseAxisLen : PI2 * Convert.ToDouble(i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);
                    //取得當前點的顏色
                    int nOldX = 0;
                    int nOldY = 0;
                    nOldX = bXDir ? i + Convert.ToInt32(dy * dMultValue) : i;
                    nOldY = bXDir ? j : j + Convert.ToInt32(dy * dMultValue);
                    Color color = srcBmp.GetPixel(i, j);
                    if (nOldX >= leftMargin && nOldX < destBmp.Width - rightMargin && nOldY >= bottomMargin && nOldY < destBmp.Height - topMargin)
                    {
                        destBmp.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return destBmp;
        }
        /// <summary>
        /// 判斷驗證碼是否正確
        /// </summary>
        /// <param name="inputValCode">待判斷的驗證碼</param>
        /// <returns>正確返回 true,錯誤返回 false</returns>
        public bool IsRight(string inputValCode)
        {
            if (validStr.ToUpper().Equals(inputValCode.ToUpper()))//無論輸入大小寫都轉換為大些判斷
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}
