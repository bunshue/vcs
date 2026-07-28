using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for MemoryStream
using System.Drawing.Text;  // for TextRenderingHint
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;  // for LinearGradientBrush
using System.Security.Cryptography;  // for RNGCryptoServiceProvider

// 全自動區分電腦和人類的公開圖靈測試
//（英語：Completely Automated Public Turing test to tell Computers and Humans Apart，簡稱CAPTCHA）
// 俗稱驗證碼

namespace vcs_Draw_Captcha1
{
    public partial class Form1 : Form
    {
        string captcha_text = "This is a lion-mouse";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            timer1_Tick(sender, e);
        }

        void show_item_location()
        {
            int W = 480;
            int H = 100;
            pictureBox00.Size = new Size(W, H);
            pictureBox01.Size = new Size(W, H);
            pictureBox02.Size = new Size(W, H);
            pictureBox03.Size = new Size(W, H);
            pictureBox04.Size = new Size(W, H);
            pictureBox05.Size = new Size(W, H);
            pictureBox06.Size = new Size(W, H);
            pictureBox07.Size = new Size(W, H);
            pictureBox08.Size = new Size(W, H);
            pictureBox09.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);
            pictureBox15.Size = new Size(W, H);
            pictureBox16.Size = new Size(W, H);
            pictureBox17.Size = new Size(W, H);
            pictureBox18.Size = new Size(W, H);
            pictureBox19.Size = new Size(W, H);
            pictureBox20.Size = new Size(W, H);
            pictureBox21.Size = new Size(W, H);
            pictureBox22.Size = new Size(W, H);
            pictureBox23.Size = new Size(W, H);
            pictureBox00.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox01.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox02.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox03.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox04.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox05.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox06.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox07.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox08.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox09.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox10.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox11.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox12.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox13.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox14.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox15.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox16.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox17.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox18.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox19.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox20.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox21.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox22.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox23.SizeMode = PictureBoxSizeMode.Zoom;

            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;
            pictureBox00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            pictureBox04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            pictureBox05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            pictureBox06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            pictureBox07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            pictureBox08.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox09.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            pictureBox12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            pictureBox13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            pictureBox14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            pictureBox15.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            pictureBox16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            pictureBox20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            pictureBox21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            pictureBox22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            pictureBox23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            button0.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 870 - 70);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 70);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1810, 930);
            this.Text = "vcs_Draw_Captcha1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            draw_captcha00();   //for pictureBox00
            draw_captcha01();   //for pictureBox01
            draw_captcha02();   //for pictureBox02
            draw_captcha03();   //for pictureBox03
            draw_captcha04();   //for pictureBox04
            draw_captcha05();   //for pictureBox05
            draw_captcha06();   //for pictureBox06
            draw_captcha07();   //for pictureBox07
            draw_captcha08();   //for pictureBox08
            draw_captcha09();   //for pictureBox09
            draw_captcha10();   //for pictureBox10
            draw_captcha11();   //for pictureBox11
            draw_captcha12();   //for pictureBox12
            draw_captcha13();   //for pictureBox13
            draw_captcha14();   //for pictureBox14
            draw_captcha15();   //for pictureBox15
            draw_captcha16();   //for pictureBox16
            draw_captcha17();   //for pictureBox17
            draw_captcha18();   //for pictureBox18
            draw_captcha19();   //for pictureBox19
            draw_captcha20();   //for pictureBox20
            draw_captcha21();   //for pictureBox21
            draw_captcha22();   //for pictureBox22
            draw_captcha23();   //for pictureBox23
        }

        //------------------------------------------------------------  # 60個

        //Captcha 00 ST
        private void draw_captcha00()
        {
            string captcha_code = "aMg8p37fo3";

            Captcha00 captcha = new Captcha00();
            Bitmap bitmap1 = captcha.CreateImage(captcha_code);
            pictureBox00.Image = bitmap1;
        }
        //Captcha 00 SP

        //------------------------------------------------------------  # 60個

        //Captcha 01 ST
        private void draw_captcha01()
        {
            string captcha_code = "HZGPOHYM2K";
            byte[] bytes = CreateCheckCodeImage01(captcha_code);
        }

        private byte[] CreateCheckCodeImage01(string checkCode)
        {
            if (checkCode == null || checkCode.Trim() == String.Empty)
            {
                return null;
            }

            int iWordWidth = 20;
            int iImageWidth = checkCode.Length * iWordWidth;
            Bitmap bitmap1 = new Bitmap(iImageWidth, 30);
            Graphics g = Graphics.FromImage(bitmap1);
            //生成隨機生成器
            Random rand = new Random();
            //清空圖片背景色
            g.Clear(Color.White);

            //畫圖片的背景噪音點
            for (int i = 0; i < 20; i++)
            {
                int x1 = rand.Next(bitmap1.Width);
                int x2 = rand.Next(bitmap1.Width);
                int y1 = rand.Next(bitmap1.Height);
                int y2 = rand.Next(bitmap1.Height);
                g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
            }

            //畫圖片的背景噪音線
            for (int i = 0; i < 2; i++)
            {
                int x1 = 0;
                int x2 = bitmap1.Width;
                int y1 = rand.Next(bitmap1.Height);
                int y2 = rand.Next(bitmap1.Height);
                if (i == 0)
                {
                    g.DrawLine(new Pen(Color.Gray, 2), x1, y1, x2, y2);
                }
            }
            for (int i = 0; i < checkCode.Length; i++)
            {
                string Code = checkCode[i].ToString();
                int xLeft = iWordWidth * (i);
                rand = new Random(xLeft);
                int iSeed = DateTime.Now.Millisecond;
                int iValue = rand.Next(iSeed) % 4;
                if (iValue == 0)
                {
                    Font f = new Font("Arial", 16, (FontStyle.Bold | FontStyle.Italic));
                    Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                    LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Red, 1.5f, true);
                    g.DrawString(Code, f, brush, xLeft, 2);
                }
                else if (iValue == 1)
                {
                    Font f = new Font("楷體", 16, (FontStyle.Bold));
                    Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                    LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.DarkRed, 1.3f, true);
                    g.DrawString(Code, f, brush, xLeft, 2);
                }
                else if (iValue == 2)
                {
                    Font f = new Font("宋體", 16, (FontStyle.Bold));
                    Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                    LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Green, Color.Blue, 1.2f, true);
                    g.DrawString(Code, f, brush, xLeft, 2);
                }
                else if (iValue == 3)
                {
                    Font f = new Font("黑體", 16, (FontStyle.Bold | FontStyle.Bold));
                    Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                    LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Green, 1.8f, true);
                    g.DrawString(Code, f, brush, xLeft, 2);
                }
            }

            ////畫圖片的前景噪音點 ---有無這段代碼 貌似沒啥變化
            for (int i = 0; i < 8; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);
                bitmap1.SetPixel(x, y, Color.FromArgb(rand.Next()));
            }

            //畫圖片的邊框線
            g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);

            pictureBox01.Image = bitmap1;

            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);
            return ms.ToArray();

            g.Dispose();
            //bitmap1.Dispose();
        }

        //Captcha 01 SP

        //------------------------------------------------------------  # 60個

        //Captcha 02 ST
        void draw_captcha02()
        {
            //產生驗證圖片

            List<char> myList = new List<char>();   //用來存放篩選後的字

            /*  不均勻分配
            myList.Add('A');
            myList.Add('A');
            myList.Add('A');
            myList.Add('B');
            myList.Add('C');
            */

            //特定分配
            for (int i = 50; i <= 57; i++)
            {
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表
            }

            for (int i = 65; i <= 90; i++)
            {
                //ASCII碼，找出大寫英文
                if (i == 73) continue; //排除I
                if (i == 79) continue; //排除O
                myList.Add((char)i);
            }

            for (int i = 97; i <= 122; i++)
            {
                //參考ASCII碼，找出小寫英文
                if (i == 108) continue; //排除l
                if (i == 111) continue; //排除o
                myList.Add((char)i);
            }

            char[] texts = new char[myList.Count];
            texts = myList.ToArray();

            string captcha_code = "vuFfHy9UAB";
            RenderImage02(captcha_code);
        }

        //產生驗證圖片
        private void RenderImage02(string vaildNumAnswer)
        {
            Random rand = new Random();

            int num = 10;
            int ww = 30 * 2 + num * 20;
            //寬度=(留邊)30*2 + 每個字*20
            int hh = 70;

            Bitmap bitmap1 = new Bitmap(ww, hh);
            Graphics g = Graphics.FromImage(bitmap1);

            //產生背景色
            Color cc = Color.FromArgb(rand.Next(256), rand.Next(256), rand.Next(256));
            Brush bb = new SolidBrush(cc);
            g.FillRectangle(bb, 0, 0, ww, hh);

            //產生字色，斥掉背景色
            bb = new SolidBrush(Color.FromArgb(cc.R ^ 255, cc.G ^ 255, cc.B ^ 255));

            //產生字體
            Font ff = new Font("Arial Black", 18, FontStyle.Regular);

            //逐一畫每一個字
            for (int i = 0; i < vaildNumAnswer.Length; i++)
            {
                g.DrawString(vaildNumAnswer.Substring(i, 1), ff, bb, i * 20 + 30, 20);
            }

            //加入雜點
            bb = new SolidBrush(Color.White);
            for (int i = 1; i <= 500; i++)
            {
                g.FillRectangle(bb, rand.Next(ww), rand.Next(hh), 2, 2);
            }
            pictureBox02.Image = bitmap1;
        }
        //Captcha 02 SP

        //------------------------------------------------------------  # 60個

        //Captcha 03 ST
        private void draw_captcha03()
        {
            string captcha_code = " 8 N 0 J";
            CodeImage03(captcha_code, pictureBox03);    //for //for pictureBox03
        }

        private void CodeImage03(string checkCode, PictureBox pbx)
        {
            //richTextBox1.Text += "str = " + checkCode + "\n";
            //richTextBox1.Text += "len = " + checkCode.Length.ToString() + "\n";

            if (checkCode == null || checkCode.Trim() == String.Empty)
            {
                return;
            }

            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling((checkCode.Length * 20.0)), 50);
            //richTextBox1.Text += "W = " + bitmap1.Width.ToString() + ", H = " + bitmap1.Height.ToString() + "\n";

            Graphics g = Graphics.FromImage(bitmap1);

            //產生隨機產生器
            Random rand = new Random();
            //清空圖片背景色
            g.Clear(Color.White);
            //畫圖片的背景噪音線
            for (int i = 0; i < 3; i++)
            {
                int x1 = rand.Next(bitmap1.Width);
                int x2 = rand.Next(bitmap1.Width);
                int y1 = rand.Next(bitmap1.Height);
                int y2 = rand.Next(bitmap1.Height);
                g.DrawLine(new Pen(Color.Black), x1, y1, x2, y2);
            }

            Font f = new Font("Arial", 24, (FontStyle.Bold));
            g.DrawString(checkCode, f, new SolidBrush(Color.Red), 2, 2);

            //畫圖片的前景噪音點
            for (int i = 0; i < 150; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);

                bitmap1.SetPixel(x, y, Color.FromArgb(rand.Next()));
            }

            //畫圖片的邊框線
            g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            pbx.Width = bitmap1.Width;
            pbx.Height = bitmap1.Height;
            pbx.BackgroundImage = bitmap1;
        }
        //Captcha 03 SP

        //------------------------------------------------------------  # 60個

        //Captcha 04 ST
        void draw_captcha04()
        {
            string captcha_code = "uhM2";
            Bitmap bitmap1 = Captcha04.CreateVerifyCodeBmp(captcha_code);
            pictureBox04.Image = bitmap1;
        }
        //Captcha 04 SP

        //------------------------------------------------------------  # 60個

        //Captcha 05 ST
        void draw_captcha05()
        {
            string captcha_code = "9NDW";
            Create05(captcha_code);
        }

        //------------------------------------------------------------  # 60個

        // 該方法是將生成的隨機數寫入圖像文件
        /// <param name="VNum">VNum是一個隨機數</param>
        public MemoryStream Create05(string captcha_code)
        {
            Bitmap bitmap1 = new Bitmap(100, 25);
            Graphics g = null;
            MemoryStream ms = null;
            Random rand = new Random();
            //驗證碼顏色集合
            Color[] c = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
            //驗證碼字體集合
            string[] fonts = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };

            g = Graphics.FromImage(bitmap1);//從bitmap1對象生成新的Graphics對象 

            g.Clear(Color.White);//背景設為白色

            //在隨機位置畫背景點
            for (int i = 0; i < 100; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);
                g.DrawRectangle(new Pen(Color.LightGray, 0), x, y, 1, 1);
            }

            //驗證碼繪制在g中
            for (int i = 0; i < captcha_code.Length; i++)
            {
                int cindex = rand.Next(7);//隨機顏色索引值
                int findex = rand.Next(5);//隨機字體索引值
                Font f = new Font(fonts[findex], 14, FontStyle.Bold);//字體
                Brush b = new SolidBrush(c[cindex]);//顏色
                int ii = 4;
                if ((i + 1) % 2 == 0)//控制驗證碼不在同一高度
                {
                    ii = 2;
                }
                g.DrawString(captcha_code.Substring(i, 1), f, b, 3 + (i * 20), ii);//繪制一個驗證字符
            }
            ms = new MemoryStream();//生成內存流對象
            bitmap1.Save(ms, ImageFormat.Jpeg);//將此圖像以jpg圖像文件的格式保存到流中

            //回收資源
            g.Dispose();

            pictureBox05.Image = bitmap1;
            //bitmap1.Dispose();
            return ms;
        }
        //Captcha 05 SP

        //------------------------------------------------------------  # 60個

        //Captcha 06 ST
        void draw_captcha06()
        {
            //製作驗證碼3

            string captcha_code = "19736";

            Random rand = new Random();
            Bitmap bitmap1 = new Bitmap(120, 25);
            Graphics g = Graphics.FromImage(bitmap1);

            string[] fonts = { "黑體", "楷體", "微軟雅黑", "宋體", "隸書" };
            Color[] colors = { Color.Red, Color.Yellow, Color.Blue, Color.Black, Color.Green };

            for (int i = 0; i < 5; i++)
            {
                Point p = new Point(i * 20, 0);//0,0 20 0
                g.DrawString(captcha_code[i].ToString(), new Font(fonts[rand.Next(0, 5)], 20, FontStyle.Bold), new SolidBrush(colors[rand.Next(0, 5)]), p);
            }

            //畫線
            for (int i = 0; i < 25; i++)
            {
                Point p1 = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                Point p2 = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                g.DrawLine(new Pen(Color.Green), p1, p2);
            }

            //畫像素顆粒
            for (int i = 0; i < 100; i++)
            {
                Point p = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                bitmap1.SetPixel(p.X, p.Y, Color.Black);
            }

            pictureBox06.Image = bitmap1;
        }
        //Captcha 06 SP

        //------------------------------------------------------------  # 60個

        //Captcha 07 ST
        void draw_captcha07()
        {
            string captcha_code = "42959";

            Bitmap bitmap1 = new Bitmap(150, 40);
            Graphics g = Graphics.FromImage(bitmap1);

            //预定义几种字体样式和颜色
            string[] fonts = { "微软雅黑", "宋体", "黑体", "隶书", "仿宋" };
            Color[] colors = { Color.Yellow, Color.Blue, Color.Black, Color.Red, Color.Orange };
            Random rand = new Random();

            //因为每一数字的字体和颜色可能不同，
            //因此循环将生成的随机数每一数字绘制到图片
            for (int i = 0; i < captcha_code.Length; i++)
            {
                Point p = new Point(i * 30, 0);
                g.DrawString(captcha_code[i].ToString(), new Font(fonts[rand.Next(0, 5)], 20, FontStyle.Bold), new SolidBrush(colors[rand.Next(0, 5)]), p);
            }

            //循环在图片范围内绘制出50条线
            for (int i = 0; i < 50; i++)
            {
                //保证线的起始点都在图片范围内
                Point p1 = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                Point p2 = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                g.DrawLine(new Pen(Brushes.Green), p1, p2);
            }

            //添加一些像素点
            for (int i = 0; i < 300; i++)
            {
                Point p1 = new Point(rand.Next(0, bitmap1.Width), rand.Next(0, bitmap1.Height));
                bitmap1.SetPixel(p1.X, p1.Y, Color.Green);
            }
            pictureBox07.Image = bitmap1;
        }
        //Captcha 07 SP

        //------------------------------------------------------------  # 60個

        //Captcha 08 ST
        void draw_captcha08()
        {
            string captcha_code = "D3W0K1N1F7";
            pictureBox08.Image = drawImg08(captcha_code);
        }

        // 生成圖像
        /// <param name="check">字符</param>
        public Bitmap drawImg08(string check)
        {
            Bitmap bitmap1 = new Bitmap(220, 34);
            var ht = Graphics.FromImage(bitmap1);
            ht.Clear(Color.White);
            ht.DrawLine(new Pen(Color.SpringGreen), 1, 1, 90, 34);
            Font f = new Font("微軟雅黑", 20, FontStyle.Bold);
            var jianbian = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Teal, Color.Snow, 2f, true);
            ht.DrawString(check, f, jianbian, 0, 0);
            ht.DrawRectangle(new Pen(Color.Aqua), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            ht.Dispose();
            return bitmap1;
        }
        //Captcha 08 SP

        //------------------------------------------------------------  # 60個

        //Captcha 09 ST
        void draw_captcha09()
        {
            string captcha_code = "HQ58S";

            //將字串儲存到Session中,以便需要時進行驗證                                                
            //context.Session["ValidCode"] = captcha_code;
            //定義寬120畫素,高30畫素的資料定義的影象物件                                          
            Bitmap bitmap1 = new Bitmap(120, 30);
            //繪製圖片                               
            Graphics g = Graphics.FromImage(bitmap1);
            try
            {
                //生成隨機物件
                Random rand = new Random();
                //清除圖片背景色                                                   
                g.Clear(Color.White);
                // 隨機產生圖片的背景噪線                                                       
                for (int i = 0; i < 25; i++)
                {
                    int x1 = rand.Next(bitmap1.Width);
                    int x2 = rand.Next(bitmap1.Width);
                    int y1 = rand.Next(bitmap1.Height);
                    int y2 = rand.Next(bitmap1.Height);
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }
                //設定圖片字型風格
                Font f = new Font("新宋體", 20, (FontStyle.Bold));
                //設定畫筆型別
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 3, true);
                //繪製隨機字元
                g.DrawString(captcha_code, f, brush, 5, 2);

                //繪製圖片的前景噪點
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
                //建立儲存區為記憶體的流
                MemoryStream ms = new MemoryStream();
                //將影象物件儲存為記憶體流       
                bitmap1.Save(ms, ImageFormat.Gif);
            }
            finally
            {
                g.Dispose();
                //image.Dispose();
                pictureBox09.Image = bitmap1;
            }
        }
        //Captcha 09 SP

        //------------------------------------------------------------  # 60個

        //Captcha 10 ST
        void draw_captcha10()
        {
            string captcha_code = "5XF4";
            CaptchaCode10(captcha_code);
        }

        private void CaptchaCode10(string VNum)
        {
            Graphics g = null;
            MemoryStream ms = null;
            int gheight = VNum.Length * 12;
            Bitmap bitmap1 = new Bitmap(gheight, 25);
            g = Graphics.FromImage(bitmap1);
            //生成隨機生成器
            Random rand = new Random();
            //背景顏色
            g.Clear(Color.White);
            for (int i = 0; i < 100; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);
                bitmap1.SetPixel(x, y, Color.FromArgb(rand.Next()));
            }
            //文字字體
            Font f = new Font("Arial Black ", 12);
            //文字顏色
            SolidBrush s = new SolidBrush(Color.Blue);
            g.DrawString(VNum, f, s, 3, 3);
            ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);
            g.Dispose();
            pictureBox10.Image = bitmap1;
            //bitmap1.Dispose();
        }
        //Captcha 10 SP

        //------------------------------------------------------------  # 60個

        //Captcha 11 ST
        void draw_captcha11()
        {
            /*
            驗證碼字符個數、生成圖片寬度、高度自定均可由構造方法自定，無參構造生成默認字符個數和默認大小的Image,
            方法GetImgWithValidateCode()返回生成的驗證碼圖片，
            方法 IsRight(string inputValCode) 判斷用戶輸入的驗證碼 inputValCode與圖片顯示的字符是否一致，不區分大小寫
            */
            Captcha11 captchacode11 = new Captcha11();
            Image img = captchacode11.GetImgWithValidateCode();
            pictureBox11.Image = img;
        }
        //Captcha 11 SP

        //------------------------------------------------------------  # 60個

        //Captcha 12 ST
        void draw_captcha12()
        {
            string captcha_code = "X1T4";

            Size ImageSize = Size.Empty;
            Font f = new Font("MS Sans Serif", 20);

            // 計算驗證 碼圖片大小
            using (Bitmap bitmap1 = new Bitmap(10, 10))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    SizeF size = g.MeasureString(captcha_code, f, 10000);
                    ImageSize.Width = (int)size.Width + 8;
                    ImageSize.Height = (int)size.Height + 8;
                }
            }

            // 創建驗證碼圖片
            Bitmap bitmap2 = new Bitmap(ImageSize.Width, ImageSize.Height);
            {
                Random rand = new Random();

                // 繪制驗證碼文本
                Graphics g = Graphics.FromImage(bitmap2);
                g.Clear(Color.White);
                StringFormat string_format = new StringFormat();
                string_format.Alignment = StringAlignment.Near;
                string_format.LineAlignment = StringAlignment.Center;
                string_format.FormatFlags = StringFormatFlags.NoWrap;
                g.DrawString(captcha_code, f, Brushes.Black, new RectangleF(0, 0, ImageSize.Width, ImageSize.Height), string_format);

                // 制造噪聲 雜點面積占圖片面積的 30%
                int num = ImageSize.Width * ImageSize.Height * 30 / 100;
                for (int iCount = 0; iCount < num; iCount++)
                {
                    // 在隨機的位置使用隨機的顏色設置圖片的像素
                    int x = rand.Next(ImageSize.Width);
                    int y = rand.Next(ImageSize.Height);
                    int rr = rand.Next(255);
                    int gg = rand.Next(255);
                    int bb = rand.Next(255);
                    Color c = Color.FromArgb(rr, gg, bb);
                    bitmap2.SetPixel(x, y, c);
                }

                pictureBox12.Image = bitmap2;

                // 輸出圖片
                MemoryStream ms = new MemoryStream();
                bitmap2.Save(ms, ImageFormat.Jpeg);
                ms.Close();
            }//using
            f.Dispose();
        }
        //Captcha 12 SP

        //------------------------------------------------------------  # 60個

        //Captcha 13 ST
        void draw_captcha13()
        {
            string captcha_code = "3828353473";
            Bitmap bitmap1 = DrawCahpcha13(captcha_code);
            pictureBox13.Image = bitmap1;
        }

        //繪制驗證碼
        public static Bitmap DrawCahpcha13(string captcha_code)
        {
            int length = 10;  // 驗證碼長度
            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling(length * 20.5), 50);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bitmap1);//利用該圖片對象生成“畫板”
            Font f = new Font("Arial", 24, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(captcha_code, f, brush, 0, 0);//關鍵的一步，進行繪制。
            //bitmap1.Save("aaaa.jpg", ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源
            return bitmap1;
        }
        //Captcha 13 SP

        //------------------------------------------------------------  # 60個

        //Captcha 14 ST
        void draw_captcha14()
        {
            //產生圖片驗證碼(很複雜)

            string captcha_code = "WZq5";

            Captcha14 captchacode14 = new Captcha14();

            //設定Border, 但看不出差異
            captchacode14.Border = Captcha14.BorderStyle.RoundRectangle;

            //創建驗證碼的圖片
            Bitmap bitmap1 = captchacode14.CreateImage(captcha_code);

            pictureBox14.Image = bitmap1;
        }
        //Captcha 14 SP

        //------------------------------------------------------------  # 60個

        //Captcha 15 ST
        void draw_captcha15()
        {
            //調用函數將驗證碼生成圖片
            string captcha_code = "v8j82";
            CreateCheckCodeImage15(captcha_code);
        }

        //將驗證碼生成圖片顯示
        private void CreateCheckCodeImage15(string checkCode)
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
                Random rand = new Random();

                //清空圖片背景色
                g.Clear(Color.AntiqueWhite);

                //畫圖片的背景噪音線
                for (int i = 0; i < 10; i++)
                {
                    int x1 = rand.Next(bitmap1.Width);
                    int x2 = rand.Next(bitmap1.Width);
                    int y1 = rand.Next(bitmap1.Height);
                    int y2 = rand.Next(bitmap1.Height);

                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }

                Font f = new Font("Arial", 18, (FontStyle.Bold | FontStyle.Italic));
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 1.2f, true);
                g.DrawString(checkCode, f, brush, 2, 2);

                //畫圖片的前景噪音點
                for (int i = 0; i < 100; i++)
                {
                    int x = rand.Next(bitmap1.Width);
                    int y = rand.Next(bitmap1.Height);

                    bitmap1.SetPixel(x, y, Color.FromArgb(rand.Next()));
                }

                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);

                MemoryStream ms = new MemoryStream();
                bitmap1.Save(ms, ImageFormat.Gif);
                pictureBox15.Image = bitmap1;
            }
            finally
            {
                //g.Dispose();
                //image.Dispose();
            }
        }
        //Captcha 15 SP

        //------------------------------------------------------------  # 60個

        //Captcha 16 ST
        void draw_captcha16()
        {
            ProcessRequest();
        }

        public void ProcessRequest()
        {
            int W = 80;
            int H = 22;
            int fontSize = 16;

            string captcha_code = "m2AG";

            //颜色列表，用于验证码、噪线、噪点 
            Color[] color = { Color.Black, Color.Red, Color.Blue, Color.Green, Color.Orange, Color.Brown, Color.Brown, Color.DarkBlue };
            //字体列表，用于验证码 
            string[] fonts = { "Times New Roman", "Verdana", "Arial", "Gungsuh", "Impact" };
            Random rand = new Random();

            //创建画布
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            //画噪线 
            for (int i = 0; i < 1; i++)
            {
                int x1 = rand.Next(W);
                int y1 = rand.Next(H);
                int x2 = rand.Next(W);
                int y2 = rand.Next(H);
                Color clr = color[rand.Next(color.Length)];
                g.DrawLine(new Pen(clr), x1, y1, x2, y2);
            }
            //画验证码字符串 
            for (int i = 0; i < captcha_code.Length; i++)
            {
                string fnt = fonts[rand.Next(fonts.Length)];
                Font ft = new Font(fnt, fontSize);
                Color clr = color[rand.Next(color.Length)];
                g.DrawString(captcha_code[i].ToString(), ft, new SolidBrush(clr), (float)i * 18 + 2, (float)0);
            }
            ////画噪点 
            //for (int i = 0; i < 1; i++)
            //{
            //    int x = rand.Next(bitmap1.Width);
            //    int y = rand.Next(bitmap1.Height);
            //    Color clr = color[rand.Next(color.Length)];
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
            pictureBox16.Image = bitmap1;
            //bitmap1.Dispose();
        }
        //Captcha 16 SP

        //------------------------------------------------------------  # 60個

        //Captcha 17 ST
        void draw_captcha17()
        {
            //使用驗證碼類
            Captcha17 capt = new Captcha17();
            Bitmap bitmap1 = capt.GetImage();
            pictureBox17.Image = bitmap1;
        }
        //Captcha 17 SP

        //------------------------------------------------------------  # 60個

        //Captcha 18 ST
        void draw_captcha18()
        {
            string captcha_code = "xy6nPlUJAR";
            Bitmap bitmap1 = DrawCahpcha18(captcha_code);
            pictureBox18.Image = bitmap1;
        }

        //繪制驗證碼
        public static Bitmap DrawCahpcha18(string captcha_code)
        {
            int length = 10;
            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling(length * 12.5), 20);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bitmap1);
            Font f = new Font("Arial", 12, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(captcha_code, f, brush, 0, 0);//關鍵的一步，進行繪制。
            //bitmap1.Save("aaaa.jpg", ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源
            return bitmap1;
        }
        //Captcha 18 SP

        //------------------------------------------------------------  # 60個

        //Captcha 19 ST
        void draw_captcha19()
        {
            CreateImage19(captcha_text);
        }

        //彩色驗證碼
        private void CreateImage19(string checkCode)
        {
            int W = checkCode.Length * 15;
            int H = 50;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            //定義顏色
            Color[] c = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
            //定義字體
            string[] fonts = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };
            Random rand = new Random();
            //隨機輸出噪點
            for (int i = 0; i < 50; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);
                g.DrawRectangle(new Pen(Color.LightGray, 0), x, y, 1, 1);
            }

            //輸出不同字體和顏色的驗證碼字符
            for (int i = 0; i < checkCode.Length; i++)
            {
                int cindex = rand.Next(7);
                int findex = rand.Next(5);

                Font f = new Font(fonts[findex], 15, FontStyle.Bold);
                Brush b = new SolidBrush(c[cindex]);
                int ii = 4;
                if ((i + 1) % 2 == 0)
                {
                    ii = 2;
                }
                g.DrawString(checkCode.Substring(i, 1), f, b, 3 + (i * 12), ii);
            }
            //畫一個邊框
            g.DrawRectangle(new Pen(Color.Black, 0), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);

            g.Dispose();

            pictureBox19.Image = bitmap1;
        }

        //Captcha 19 SP

        //------------------------------------------------------------  # 60個

        //Captcha 20 ST
        //中文驗證法碼 ST

        void draw_captcha20()
        {
            string captcha_code = "天階夜色涼如水";

            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling((captcha_code.Length * 20.5)) * 3, 22 * 3);
            Graphics g = Graphics.FromImage(bitmap1);
            Random rand = new Random();
            g.Clear(Color.White);

            //画图片的背景噪音线
            for (int i = 0; i < 2; i++)
            {
                Point tem_Point_1 = new Point(rand.Next(bitmap1.Width), rand.Next(bitmap1.Height));
                Point tem_Point_2 = new Point(rand.Next(bitmap1.Width), rand.Next(bitmap1.Height));
                g.DrawLine(new Pen(Color.Black), tem_Point_1, tem_Point_2);
            }

            Font f = new Font("標楷體", 12 * 2, (FontStyle.Bold));
            LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 1.2f, true);
            g.DrawString(captcha_code, f, brush, 2, 2);
            //画图片的前景噪音点
            for (int i = 0; i < 100; i++)
            {
                Point tem_point = new Point(rand.Next(bitmap1.Width), rand.Next(bitmap1.Height));
                bitmap1.SetPixel(tem_point.X, tem_point.Y, Color.FromArgb(rand.Next()));
            }
            //画图片的边框线
            g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            pictureBox20.Image = bitmap1;
        }

        //中文驗證法碼 SP

        //Captcha 20 SP

        //------------------------------------------------------------  # 60個

        //Captcha 21 ST
        void draw_captcha21()
        {
            string strKey = "";
            int _nlen = 6;
            byte[] data = this.GenerateVerifyImage21(_nlen, ref strKey); //_nLen生成驗證碼的長度
            //Session["Jcode"] = strKey; //用來保存驗證碼的值
            //Page.Response.OutputStream.Write(data, 0, data.Length);
        }

        /// 生成圖片驗證碼
        /// <param name="nLen">驗證碼的長度</param>
        /// <param name="_codes">產生驗證碼的取值</param>
        /// <param name="strKey">輸出參數，驗證碼的內容</param>
        /// <returns>圖片字節流</returns>
        private byte[] GenerateVerifyImage21(int nLen, ref string strKey)
        {
            int nBmpWidth = 26 * nLen + 10;
            int nBmpHeight = 40;
            Bitmap bitmap1 = new Bitmap(nBmpWidth, nBmpHeight);

            // 1. 生成隨機背景顏色
            int nRed, nGreen, nBlue;  // 背景的三元色
            Random rand = new Random((int)DateTime.Now.Ticks);
            nRed = rand.Next(255) % 128 + 128;
            nGreen = rand.Next(255) % 128 + 128;
            nBlue = rand.Next(255) % 128 + 128;

            // 2. 填充位圖背景
            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(new SolidBrush(Color.FromArgb(nRed, nGreen, nBlue)), 0, 0, nBmpWidth, nBmpHeight);

            // 3. 繪制干擾線條，采用比背景略深一些的顏色
            int nLines = 5;
            Pen pen = new Pen(Color.FromArgb(nRed - 17, nGreen - 17, nBlue - 17), 2);
            for (int a = 0; a < nLines; a++)
            {
                int x1 = rand.Next() % nBmpWidth;
                int y1 = rand.Next() % nBmpHeight;
                int x2 = rand.Next() % nBmpWidth;
                int y2 = rand.Next() % nBmpHeight;
                g.DrawLine(pen, x1, y1, x2, y2);
            }

            string captcha_code = "天階夜色涼如水";

            // 4. 循環取得字符，並繪制
            string strResult = "";
            for (int i = 0; i < nLen; i++)
            {
                int x = (i * 26 + rand.Next(5));
                int y = rand.Next(10) + 1;

                // 確定字體
                Font f = new Font("Arial", 14 + rand.Next() % 4, FontStyle.Bold);
                string c = captcha_code.Substring(i, 1);  // 獲取字符
                strResult += c.ToString();

                // 繪制字符, 繪制字體顏色，采用比背景與干擾線略深一些的顏色
                g.DrawString(c.ToString(), f, new SolidBrush(Color.FromArgb(nRed - 68, nGreen - 68, nBlue - 68)), x, y);
            }
            // 5. 輸出字節流
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);
            //bitmap1.Dispose();
            pictureBox21.Image = bitmap1;
            g.Dispose();

            strKey = strResult;
            byte[] byteReturn = ms.ToArray();
            ms.Close();

            return byteReturn;
        }

        //Captcha 21 SP

        //------------------------------------------------------------  # 60個

        //Captcha 22 ST
        void draw_captcha22()
        {
            Bitmap bitmap1 = MakeCaptchaImge22(captcha_text,
                50, //最小
                70, //最大
                pictureBox22.ClientSize.Width,
                pictureBox22.ClientSize.Height);
            pictureBox22.Image = bitmap1;
        }

        private Random rand = new Random();

        // Make a captcha image for the text.
        private Bitmap MakeCaptchaImge22(string txt, int min_size, int max_size, int W, int H)
        {
            // Make the bitmap and associated Graphics object.
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.Clear(Color.White);

            // See how much room is available for each character.
            int ch_wid = (int)(W / txt.Length);

            // Draw each character.
            for (int i = 0; i < txt.Length; i++)
            {
                float font_size = rand.Next(min_size, max_size);
                Font the_font = new Font("Times New Roman", font_size, FontStyle.Bold);
                DrawCharacter22(txt.Substring(i, 1), g, the_font, i * ch_wid, ch_wid, W, H);
            }
            return bitmap1;
        }

        // Draw a deformed character at this position.
        private int PreviousAngle = 0;
        private void DrawCharacter22(string txt, Graphics g, Font the_font, int X, int ch_wid, int wid, int hgt)
        {
            // Center the text.
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;
                RectangleF rectf = new RectangleF(X, 0, ch_wid, hgt);

                // Convert the text into a path.
                using (GraphicsPath gp = new GraphicsPath())
                {
                    gp.AddString(txt, the_font.FontFamily, (int)(Font.Style), the_font.Size, rectf, string_format);

                    // Make random warping parameters.
                    float x1 = (float)(X + rand.Next(ch_wid) / 2);
                    float y1 = (float)(rand.Next(hgt) / 2);
                    float x2 = (float)(X + ch_wid / 2 + rand.Next(ch_wid) / 2);
                    float y2 = (float)(hgt / 2 + rand.Next(hgt) / 2);
                    PointF[] pts = {
                                       new PointF((float)(X + rand.Next(ch_wid) / 4),(float)(rand.Next(hgt) / 4)),
                                       new PointF((float)(X + ch_wid - rand.Next(ch_wid) / 4),(float)(rand.Next(hgt) / 4)),
                                       new PointF((float)(X + rand.Next(ch_wid) / 4),(float)(hgt - rand.Next(hgt) / 4)),
                                       new PointF((float)(X + ch_wid - rand.Next(ch_wid) / 4),(float)(hgt - rand.Next(hgt) / 4))
                                   };
                    Matrix mat = new Matrix();
                    gp.Warp(pts, rectf, mat, WarpMode.Perspective, 0);

                    // Rotate a bit randomly.
                    float dx = (float)(X + ch_wid / 2);
                    float dy = (float)(hgt / 2);
                    g.TranslateTransform(-dx, -dy, MatrixOrder.Append);
                    int angle = PreviousAngle;
                    do
                    {
                        angle = rand.Next(-30, 30);
                    } while (Math.Abs(angle - PreviousAngle) < 20);
                    PreviousAngle = angle;
                    g.RotateTransform(angle, MatrixOrder.Append);
                    g.TranslateTransform(dx, dy, MatrixOrder.Append);

                    // Draw the text.
                    g.FillPath(Brushes.Blue, gp);
                    g.ResetTransform();
                }
            }
        }
        //Captcha 22 SP

        //------------------------------------------------------------  # 60個

        //Captcha 23 ST
        void draw_captcha23()
        {
            using (Font the_font = new Font("Times New Roman", 30))
            {
                pictureBox23.Image = MakeCaptchaImage23(captcha_text, pictureBox23.ClientSize.Width, pictureBox23.ClientSize.Height, the_font, Brushes.Blue);
            }
        }

        // Draw the words with letters overlapping each other.
        private Bitmap MakeCaptchaImage23(string txt, int W, int H, Font the_font, Brush the_brush)
        {
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                int x = 0;
                foreach (char ch in txt.ToCharArray())
                {
                    SizeF ch_size = g.MeasureString(ch.ToString(), the_font);
                    int y = (int)(rand.NextDouble() * (H - ch_size.Height));
                    g.DrawString(ch.ToString(), the_font, the_brush, x, y);
                    x += (int)(ch_size.Width * 0.35);
                }
            }
            return bitmap1;
        }

        //Captcha 23 SP

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        // 該方法用於生成指定位數的隨機數
        /// <param name="VcodeNum">參數是隨機數的位數</param>
        /// <returns>返回一個隨機數字符串</returns>
        private string RndNum(int VcodeNum)
        {
            string Vchar = "1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q,R,S,T,U,V,W,X,Y,Z";
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

        //------------------------------------------------------------  # 60個

        // 獲得隨機字符
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

        public static string GenerateRandomNumber(RandomGeneratorStyle style, int length)
        {
            string strValidateString = "";
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
                strValidateString += strValidateStringSource[rand.Next(strValidateStringSource.Length - 1)];
            }
            return strValidateString;
        }

        //------------------------------------------------------------  # 60個

        private string GenerateCheckCodes01(int iCount)
        {
            char[] oCharacter = {'0','1','2','3','4','5','6','7','8','9',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
            //'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
            };

            //int number;
            string checkCode = String.Empty;
            int iSeed = DateTime.Now.Millisecond;
            Random rand = new Random(iSeed);
            for (int i = 0; i < iCount; i++)
            {
                checkCode += oCharacter[rand.Next(oCharacter.Length)];

                //純數字
                //number = rand.Next(10);
                //number = oCharacter[rand.Next(oCharacter.Length)];
                //checkCode += number.ToString();
            }
            return checkCode;
        }

        //------------------------------------------------------------  # 60個

        // 產生指定個數的隨機字符串
        string GetValidateCode(int length)
        {
            string captcha_code = string.Empty;
            Random rand = new Random(); //創建隨機數對象
            //產生由 charNum 個字母或數字組成的一個字符串
            string str = "abcdefghijkmnpqrstuvwyzABCDEFGHJKLMNPQRSTUVWYZ23456789隨機數對象"; //共59個字符，除 l,o,x,I,O,X,1,0 的所有數字和大寫字母
            for (int i = 0; i < length; i++)
            {
                captcha_code = captcha_code + str.Substring(rand.Next(59), 1);//返回0到58共59個
            }
            Console.WriteLine("11取得 : " + captcha_code);
            return captcha_code;
        }

        //------------------------------------------------------------  # 60個

        private string GenerateCheckCode15(int length)
        {
            //產生五位的隨機字符串
            int number;
            char code;
            string checkCode = String.Empty;

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
                checkCode += code.ToString();
            }
            return checkCode;
        }

        //------------------------------------------------------------  # 60個

        // 生成隨機字符串
        public string GetRandomString(int length)
        {
            Random rand = new Random();

            String charCollection = "2,3,4,5,6,7,8,9,a,s,d,f,g,h,z,c,v,b,n,m,k,q,w,e,r,t,y,u,p,A,S,D,F,G,H,Z,C,V,B,N,M,K,Q,W,E,R,T,Y,U,P"; //定義驗證碼字符及出現頻次 ,避免出現0 o j i l 1 x;  
            // 隨機字符串列表，請使用英文狀態下的逗號分隔

            string[] randomArray = charCollection.Split(','); //將字符串生成數組     
            int arrayLength = randomArray.Length;
            string randomString = "";
            for (int i = 0; i < length; i++)
            {
                randomString += randomArray[rand.Next(0, arrayLength)];
            }
            return randomString;
        }

        //------------------------------------------------------------  # 60個

        private string GetValidCode09(int length)
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

        public static string CaptchaCode08(int length)
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
        public string CreateVerifyCode(int codeLen, int zhCharsCount)
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
                    chs[i] = CreateEnOrNumChar();
                }
            }

            return new string(chs, 0, chs.Length);
        }

        // 生成英文或數字字符
        protected char CreateEnOrNumChar()
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
        private string GetRandomCode(int length)
        {
            StringBuilder sb = new StringBuilder(6);

            for (int i = 0; i < length; i++)
            {
                sb.Append(Char.ConvertFromUtf32(RandomAZ09()));
            }

            return sb.ToString();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //測試隨機文字
            string captcha_text = string.Empty;
            int length = 10;
            Random rand = new Random();

            /*
            captcha_text = RndNum(4);
            richTextBox1.Text += "01取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "02取得 : ";
            for (int i = 0; i < length; i++)
            {
                richTextBox1.Text += GetChar(rand);
            }
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個
                                                                //  純數字
            captcha_text = GenerateRandomNumber(RandomGeneratorStyle.Number, length);//生成隨機數
            richTextBox1.Text += "03取得 : " + captcha_text + "\n";
                                                          //數字+大小寫英文
            captcha_text = GenerateRandomNumber(RandomGeneratorStyle.NumberAndChar, length);//生成隨機數
            richTextBox1.Text += "04取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GenerateCheckCodes01(length);
            richTextBox1.Text += "01取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetValidateCode(length);
            richTextBox1.Text += "02取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GenerateCheckCode15(length);
            richTextBox1.Text += "03取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetRandomString(length);
            richTextBox1.Text += "04取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetValidCode09(length);
            richTextBox1.Text += "09取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = CaptchaCode08(length);
            richTextBox1.Text += "08取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = CreateVerifyCode(length, 5);
            richTextBox1.Text += "00取得 : " + captcha_text + "\n";
            */

            //------------------------------------------------------------  # 60個

            int number;
            char code;
            string checkCode = String.Empty;

            for (int i = 0; i < 4; i++)
            {
                number = rand.Next();

                if (number % 2 == 0)
                {
                    code = (char)('0' + (char)(number % 10));
                }
                else
                {
                    code = (char)('A' + (char)(number % 26));
                }
                checkCode += " " + code.ToString();
            }
            richTextBox1.Text += "03取得 : " + checkCode + "\n";

            //------------------------------------------------------------  # 60個

            string str = string.Empty;
            for (int i = 0; i < length; i++)
            {
                str += rand.Next(0, 10);
            }

            richTextBox1.Text += "07取得 : " + str + "\n";

            //------------------------------------------------------------  # 60個

            int len = rand.Next(4, 6);
            char[] chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            StringBuilder myStr = new StringBuilder();
            for (int iCount = 0; iCount < len; iCount++)
            {
                myStr.Append(chars[rand.Next(chars.Length)]);
            }

            string text = myStr.ToString();
            richTextBox1.Text += "12取得 : " + text + "\n";

            //------------------------------------------------------------  # 60個

            string captcha_code = string.Empty;
            //验证码的字符集，去掉了一些容易混淆的字符 
            char[] character = { '2', '3', '4', '5', '6', '8', '9', 'a', 'b', 'd', 'e', 'f', 'h', 'k', 'm', 'n', 'r', 'x', 'y', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'W', 'X', 'Y' };
            //生成验证码字符串 
            for (int i = 0; i < 4; i++)
            {
                captcha_code += character[rand.Next(character.Length)];
            }
            richTextBox1.Text += "16取得 : " + captcha_code + "\n";

            //------------------------------------------------------------  # 60個

            captcha_text = GetRandomCode(length);
            richTextBox1.Text += "17取得 : " + captcha_text + "\n";

            //------------------------------------------------------------  # 60個

            //亂數產生驗證答案
            //從已知幾個元素中任意選出幾個

            /*
            string vaildNumAnswer = "";
            vaildNumAnswer = "";
            for (int i = 1; i <= length; i++)
            {
                char c = texts[rand.Next(texts.Length)];
                vaildNumAnswer += c;
            }

            //richTextBox1.Text += "02取得 : " + vaildNumAnswer + "\n";
            */

            //------------------------------------------------------------  # 60個

            /*
            //沒有外部輸入驗證碼時隨機生成
            if (String.IsNullOrEmpty(this.verifyCodeText))
            {
                StringBuilder objStringBuilder = new StringBuilder();

                //加入數字1-9
                for (int i = 1; i <= 9; i++)
                {
                    objStringBuilder.Append(i.ToString());
                }

                //加入大寫字母A-Z，不包括O
                if (this.addUpperLetter)
                {
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
                }

                //加入小寫字母a-z，不包括o
                if (this.addLowerLetter)
                {
                    char temp = ' ';

                    for (int i = 0; i < 26; i++)
                    {
                        temp = Convert.ToChar(i + 97);

                        //如果生成的字母不是'o'
                        if (!temp.Equals('o'))
                        {
                            objStringBuilder.Append(temp);
                        }
                    }
                }

                //生成驗證碼字符串
                {
                    int index = 0;

                    for (int i = 0; i < length; i++)
                    {
                        index = rand.Next(0, objStringBuilder.Length);

                        this.verifyCodeText += objStringBuilder[index];

                        objStringBuilder.Remove(index, 1);
                    }
                }
                Console.WriteLine("取得aaaa : " + objStringBuilder);
                Console.WriteLine("取得verifyCodeText : " + verifyCodeText);
            */
        }
    }

    //------------------------------------------------------------  # 60個

    /// 驗證碼
    public class Captcha04
    {
        // 色彩表
        private static Color[] colors = new Color[]
        {
            Color.FromArgb(220,20,60),
            Color.FromArgb(128,0,128),
            Color.FromArgb(65,105,225),
            Color.FromArgb(70,130,180),
            Color.FromArgb(46,139,87),
            Color.FromArgb(184,134,11),
            Color.FromArgb(255,140,0),
            Color.FromArgb(139,69,19),
            Color.FromArgb(0,191,255),
            Color.FromArgb(95,158,160),
            Color.FromArgb(255,20,147),
            Color.FromArgb(255,165,0)
        };

        // 字體表
        private static string[] fonts = new string[]
        {
            "Arial",
            "Verdana",
            "Georgia",
            "黑體"
        };

        // 字體年夜小
        private static int fontSize = 22;

        // 生成驗證碼圖片
        public static Bitmap CreateVerifyCodeBmp(string captcha_code)
        {
            int width = 120;
            int height = 40;
            Bitmap bitmap1 = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bitmap1);
            Random rand = new Random();

            //配景色
            g.FillRectangle(new SolidBrush(Color.White), new Rectangle(0, 0, width, height));

            //文字
            for (int i = 0; i < 4; i++)
            {
                Font f = GetFont(rand);
                Color color = GetColor(rand);
                g.DrawString(captcha_code.Substring(i, 1), f, new SolidBrush(color), new PointF((float)(i * width / 4.0), 0));
            }

            //樂音線
            for (int i = 0; i < 10; i++)
            {
                int x1 = rand.Next(bitmap1.Width);
                int x2 = rand.Next(bitmap1.Width);
                int y1 = rand.Next(bitmap1.Height);
                int y2 = rand.Next(bitmap1.Height);

                Pen p = new Pen(GetColor(rand), 1);
                g.DrawLine(p, x1, y1, x2, y2);
            }

            //歪曲
            bitmap1 = TwistImage(bitmap1, true, 3, rand.NextDouble() * Math.PI * 2);
            g = Graphics.FromImage(bitmap1);

            //噪點
            for (int i = 0; i < 100; i++)
            {
                int x1 = rand.Next(bitmap1.Width);
                int y1 = rand.Next(bitmap1.Height);

                Pen p = new Pen(GetColor(rand), 1);
                g.DrawRectangle(p, x1, y1, 1, 1);
            }

            //邊框
            g.DrawRectangle(new Pen(new SolidBrush(Color.FromArgb(153, 153, 153))), new Rectangle(0, 0, width - 1, height - 1));

            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 獲得隨機字體
        private static Font GetFont(Random rand)
        {
            return new Font(fonts[rand.Next(0, fonts.Length)], fontSize, FontStyle.Bold);
        }

        //------------------------------------------------------------  # 60個

        // 獲得隨機色彩
        private static Color GetColor(Random rand)
        {
            return colors[rand.Next(0, colors.Length)];
        }

        //------------------------------------------------------------  # 60個

        // 正弦曲線Wave歪曲圖片
        /// <param name="srcBmp">圖片途徑</param>  
        /// <param name="bXDir">假如歪曲則選擇為True</param>  
        /// <param name="nMultValue">波形的幅度倍數，越年夜歪曲的水平越高，普通為3</param>  
        /// <param name="dPhase">波形的肇端相位，取值區間[0-2*PI)</param>  
        private static Bitmap TwistImage(Bitmap bitmap0, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);

            // 將位圖配景填充為白色  
            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, bitmap1.Width, bitmap1.Height);
            g.Dispose();

            double dBaseAxisLen = bXDir ? (double)bitmap1.Height : (double)bitmap1.Width;

            for (int i = 0; i < bitmap1.Width; i++)
            {
                for (int j = 0; j < bitmap1.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? (Math.PI * 2 * (double)j) / dBaseAxisLen : (Math.PI * 2 * (double)i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);

                    // 獲得以後點的色彩  
                    int nOldX = 0, nOldY = 0;
                    nOldX = bXDir ? i + (int)(dy * dMultValue) : i;
                    nOldY = bXDir ? j : j + (int)(dy * dMultValue);

                    Color color = bitmap0.GetPixel(i, j);
                    if (nOldX >= 0 && nOldX < bitmap1.Width && nOldY >= 0 && nOldY < bitmap1.Height)
                    {
                        bitmap1.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return bitmap1;
        }
    }

    //------------------------------------------------------------  # 60個

    // Captcha00 的摘要說明
    public class Captcha00
    {
        public Captcha00()
        {
        }

        int fontSize = 20;
        /// 驗證碼字體大小(為了顯示扭曲效果，默認30像素，可以自行修改)
        public int FontSize
        {
            get { return fontSize; }
            set { fontSize = value; }
        }

        int padding = 4;
        // 邊框補(默認4像素)
        public int Padding
        {
            get { return padding; }
            set { padding = value; }
        }

        bool chaos = true;
        // 是否輸出燥點(默認輸出)
        public bool Chaos
        {
            get { return chaos; }
            set { chaos = value; }
        }

        Color chaosColor = Color.LightGray;
        // 輸出燥點的顏色(默認灰色)
        public Color ChaosColor
        {
            get { return chaosColor; }
            set { chaosColor = value; }
        }

        int chaosWight = 1;
        // 輸出燥點的濃度
        public int ChaosWight
        {
            get { return chaosWight; }
            set { chaosWight = value; }
        }

        Color backgroundColor = Color.White;
        // 自定義背景色(默認白色)
        public Color BackgroundColor
        {
            get { return backgroundColor; }
            set { backgroundColor = value; }
        }

        // 自定義隨機顏色數組
        Color[] colors = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };

        public Color[] Colors
        {
            get { return colors; }
            set { colors = value; }
        }

        // 自定義字體數組
        string[] fonts = { "Arial", "Georgia" };

        public string[] Fonts
        {
            get { return fonts; }
            set { fonts = value; }
        }

        //------------------------------------------------------------  # 60個

        // 產生波形濾鏡效果

        private const double PI = 3.1415926535897932384626433832795;
        private const double PI2 = 6.283185307179586476925286766559;

        /// 正弦曲線Wave扭曲圖片（Edit By 51aspx.com）
        /// <param name="srcBmp">圖片路徑</param>
        /// <param name="bXDir">如果扭曲則選擇為True</param>
        /// <param name="nMultValue">波形的幅度倍數，越大扭曲的程度越高，一般為3</param>
        /// <param name="dPhase">波形的起始相位，取值區間[0-2*PI)</param>
        /// 1111
        public Bitmap TwistImage(Bitmap bitmap0, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);

            // 將位圖背景填充為白色
            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, bitmap1.Width, bitmap1.Height);
            g.Dispose();

            double dBaseAxisLen = bXDir ? (double)bitmap1.Height : (double)bitmap1.Width;

            for (int i = 0; i < bitmap1.Width; i++)
            {
                for (int j = 0; j < bitmap1.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? (PI2 * (double)j) / dBaseAxisLen : (PI2 * (double)i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);

                    // 取得當前點的顏色
                    int nOldX = 0, nOldY = 0;
                    nOldX = bXDir ? i + (int)(dy * dMultValue) : i;
                    nOldY = bXDir ? j : j + (int)(dy * dMultValue);

                    Color color = bitmap0.GetPixel(i, j);
                    if (nOldX >= 0 && nOldX < bitmap1.Width && nOldY >= 0 && nOldY < bitmap1.Height)
                    {
                        bitmap1.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 生成校驗碼圖片
        /// <param name="code">驗證碼</param>
        public Bitmap CreateImage(string code)
        {
            Random rand = new Random();
            int fSize = FontSize;
            int fWidth = fSize + Padding;
            int imageWidth = (int)(code.Length * fWidth) + 4 + Padding * 2;
            int imageHeight = fSize * 2 + Padding * 2;

            Bitmap bitmap1 = new Bitmap(imageWidth - 10, imageHeight - 10);
            Graphics g = Graphics.FromImage(bitmap1);

            g.Clear(BackgroundColor);

            //給背景添加隨機生成的燥點
            if (this.Chaos)
            {
                Pen p = new Pen(ChaosColor, 0);
                int c = ChaosWight * 10;

                for (int i = 0; i < c; i++)
                {
                    int x = rand.Next(bitmap1.Width);
                    int y = rand.Next(bitmap1.Height);

                    g.DrawRectangle(p, x, y, 1, 1);
                }
            }

            int left = 0, top = 0, top1 = 1, top2 = 1;

            int n1 = (imageHeight - FontSize - Padding * 2);
            int n2 = n1 / 4;
            top1 = n2;
            top2 = n2 * 2;

            Font f;
            Brush b;

            int cindex;
            int findex;

            //隨機字體和顏色的驗證碼字符
            for (int i = 0; i < code.Length; i++)
            {
                cindex = rand.Next(Colors.Length - 1);
                findex = rand.Next(Fonts.Length - 1);

                f = new Font(Fonts[findex], fSize, FontStyle.Bold);
                b = new SolidBrush(Colors[cindex]);

                if (i % 2 == 1)
                {
                    top = top2;
                }
                else
                {
                    top = top1;
                }

                left = i * fWidth;

                g.DrawString(code.Substring(i, 1), f, b, left, top);
            }

            //畫一個邊框 邊框顏色為Color.Gainsboro
            g.DrawRectangle(new Pen(Color.Gainsboro, 0), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            g.Dispose();

            //產生波形（Add By 51aspx.com）
            bitmap1 = TwistImage(bitmap1, true, 8, 4);

            return bitmap1;
        }
    }

    public class Captcha11
    {
        // 無參構造
        public Captcha11()
        {

        }

        /// 帶有生成字符個數的構造
        /// <param name="charNum">驗證碼中包含隨機字符的個數</param>
        public Captcha11(int charNum)
        {
            this.CharNum = charNum;
        }

        /// 帶有驗證碼圖片寬度和高度的構造
        /// <param name="width">驗證碼圖片寬度</param>
        /// <param name="height">驗證碼圖片高度</param>
        public Captcha11(int width, int height)
        {
            this.width = width;
            this.height = height;
        }

        /// 帶有生成字符個數，驗證碼圖片寬度和高度的構造
        /// <param name="charNum">驗證碼中包含隨機字符的個數</param>
        /// <param name="width">驗證碼圖片寬度</param>
        /// <param name="height">驗證碼圖片高度</param>
        public Captcha11(int charNum, int width, int height)
        {
            this.CharNum = charNum;
            this.width = width;
            this.height = height;
        }

        // 驗證碼中字符個數
        int charNum = 5; //默認字符個數為5
        public int CharNum
        {
            get { return charNum; }
            set { charNum = value; }
        }

        // 字號
        int fontSize = 20;
        public int FontSize
        {
            get { return fontSize; }
        }

        // 圖片寬度
        int width = 200;
        public int Width
        {
            get { return width; }
        }

        // 圖片高度
        int height = 45;
        public int Height
        {
            get { return height; }
            set { height = value; }
        }

        // 隨機生成的字符串
        string captcha_code = "";
        public string ValidStr
        {
            get { return captcha_code; }
            set { captcha_code = value; }
        }

        // 由隨機字符串，隨即顏色背景，和隨機線條產生的Image
        // <returns>Image</returns>
        public Image GetImgWithValidateCode()//返回 Image
        {
            captcha_code = "tA6vZ";

            //聲明一個位圖對象
            Bitmap bitmap1 = null;
            //聲明一個繪圖畫面
            Graphics g = null;
            //創建內存流
            MemoryStream memStream = new MemoryStream();
            Random rand = new Random();
            //由給定的需要生成字符串中字符個數 CharNum， 圖片寬度 Width 和高度 Height 確定字號 FontSize，
            //確保不因字號過大而不能全部顯示在圖片上
            int fontWidth = (int)Math.Round(width / (charNum + 2) / 1.3);
            int fontHeight = (int)Math.Round(height / 1.5);
            //字號取二者中小者，以確保所有字符能夠顯示，並且字符的下半部分也能顯示
            fontSize = fontWidth <= fontHeight ? fontWidth : fontHeight;
            //創建位圖對象
            bitmap1 = new Bitmap(width + FontSize, height);
            //根據上面創建的位圖對象創建繪圖圖面
            g = Graphics.FromImage(bitmap1);
            //設定驗證碼圖片背景色
            g.Clear(GetControllableColor(200));
            //產生隨機干擾線條
            for (int i = 0; i < 10; i++)
            {
                Pen backPen = new Pen(GetControllableColor(100), 2);
                //線條起點
                int x = rand.Next(width);
                int y = rand.Next(height);
                //線條終點
                int x2 = rand.Next(width);
                int y2 = rand.Next(height);
                //劃線
                g.DrawLine(backPen, x, y, x2, y2);
            }
            //定義一個含10種字體的數組
            String[] fontFamily ={ "Arial", "Verdana", "Comic Sans MS", "Impact", "Haettenschweiler",
                                     "Lucida Sans Unicode", "Garamond", "Courier New", "Book Antiqua", "Arial Narrow" };

            SolidBrush sb = new SolidBrush(GetControllableColor(0));
            //通過循環,繪制每個字符,
            for (int i = 0; i < captcha_code.Length; i++)
            {
                Font f = new Font(fontFamily[rand.Next(10)], fontSize, FontStyle.Bold);//字體隨機,字號大小30,加粗
                //每次循環繪制一個字符,設置字體格式,畫筆顏色,字符相對畫布的X坐標,字符相對畫布的Y坐標
                int space = (int)Math.Round((double)((width - fontSize * (CharNum + 2)) / CharNum));
                //縱坐標
                int y = (int)Math.Round((double)((height - fontSize) / 3));
                g.DrawString(captcha_code.Substring(i, 1), f, sb, fontSize + i * (fontSize + space), y);
            }
            //扭曲圖片
            bitmap1 = TwistImage(bitmap1, true, rand.Next(3, 5), rand.Next(3));
            try
            {
                bitmap1.Save(memStream, ImageFormat.Gif);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            //g.Dispose();
            bitmap1.Dispose();
            Image img = Image.FromStream(memStream);
            g.DrawImage(img, 50, 20, width, 10);
            return img;
        }

        // 產生一種 R,G,B 均大於 colorBase 隨機顏色，以確保顏色不會過深
        // <returns>背景色</returns>
        Color GetControllableColor(int colorBase)
        {
            Color color = Color.Black;
            if (colorBase > 200)
            {
                MessageBox.Show("可控制顏色參數大於200，顏色默認位黑色");
            }
            Random rand = new Random();
            //確保 R,G,B 均大於 colorBase，這樣才能保證背景色較淺
            color = Color.FromArgb(rand.Next(56) + colorBase, rand.Next(56) + colorBase, rand.Next(56) + colorBase);
            return color;
        }

        /// 扭曲圖片
        /// <param name="srcBmp"></param>
        /// <param name="bXDir"></param>
        /// <param name="dMultValue"></param>
        /// <param name="dPhase"></param>
        Bitmap TwistImage(Bitmap bitmap0, bool bXDir, double dMultValue, double dPhase)
        {
            int leftMargin = 0;
            int rightMargin = 0;
            int topMargin = 0;
            int bottomMargin = 0;
            //float PI = 3.14159265358979f;
            float PI2 = 6.28318530717959f;
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);
            double dBaseAxisLen = bXDir ? Convert.ToDouble(bitmap1.Height) : Convert.ToDouble(bitmap1.Width);
            for (int i = 0; i < bitmap1.Width; i++)
            {
                for (int j = 0; j < bitmap1.Height; j++)
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
                    Color color = bitmap0.GetPixel(i, j);
                    if (nOldX >= leftMargin && nOldX < bitmap1.Width - rightMargin && nOldY >= bottomMargin && nOldY < bitmap1.Height - topMargin)
                    {
                        bitmap1.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return bitmap1;
        }

        /// 判斷驗證碼是否正確
        /// <param name="inputValCode">待判斷的驗證碼</param>
        /// <returns>正確返回 true,錯誤返回 false</returns>
        public bool IsRight(string inputValCode)
        {
            if (captcha_code.ToUpper().Equals(inputValCode.ToUpper()))//無論輸入大小寫都轉換為大些判斷
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }

    //------------------------------------------------------------  # 60個

    // 驗證碼生成類
    public class Captcha14
    {
        //用戶存取驗證碼字符串
        public string validationCode = String.Empty;
        //生成的驗證碼字符串
        public char[] chars = null;
        /// 獲取系統生成的隨機驗證碼
        public String ValidationCode
        {
            get { return validationCode; }
        }

        private Int32 validationCodeCount = 4;

        /// 獲取和設置驗證碼字符串的長度
        public Int32 ValidationCodeCount
        {
            get { return validationCodeCount; }
            set { validationCodeCount = value; }
        }

        Graphics dc = null;
        private int bgWidth = 130;

        // 驗證碼的寬度，默認爲80
        public Int32 Width
        {
            get { return bgWidth; }
            set { bgWidth = value; }
        }

        private int bgHeight = 40;
        /// 驗證碼的高度，默認爲40
        public Int32 Height
        {
            get { return bgHeight; }
            set { bgHeight = value; }
        }
        /* private string[] fontFace = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };
         /// 驗證碼字體列表，默認爲{ "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" }
         public String[] FontFace
         {
             get { return fontFace; }
             set { fontFace = value; }
         }*/

        // 驗證碼字體的最小值，默認爲15,建議不小於15像素
        private int fontMinSize = 20;

        public Int32 FontMinSize
        {
            get { return fontMinSize; }
            set { fontMinSize = value; }
        }

        // 驗證碼字體的最大值，默認爲20
        private Int32 fontMaxSize = 25;

        public Int32 FontMaxSize
        {
            get { return fontMaxSize; }
            set { fontMaxSize = value; }
        }

        // 驗證碼字體的顏色，默認爲系統自動生成字體顏色
        private Color[] fontColor = { };

        public Color[] FontColor
        {
            get { return fontColor; }
            set { fontColor = value; }
        }

        private Color backColor = Color.FromArgb(243, 255, 255);
        // 驗證碼的背景色，默認爲Color.FromArgb(243, 251, 254)

        public Color BackgroundColor
        {
            get { return backColor; }
            set { backColor = value; }
        }

        private Int32 bezierCount = 3;
        // 貝塞爾曲線的條數,默認爲3條

        public Int32 BezierCount
        {
            get { return bezierCount; }
            set { bezierCount = value; }
        }
        private Int32 lineCount = 3;
        // 直線條數，默認爲3條

        public Int32 LineCount
        {
            get { return lineCount; }
            set { lineCount = value; }
        }

        Random rand = new Random();

        private Int32 intCount = 4;

        // 驗證碼字符串個數，默認爲4個字符

        public Int32 IntCount
        {
            get { return intCount; }
            set { intCount = value; }
        }

        private Boolean isPixel = true;

        // 是否添加噪點，默認添加，噪點顏色爲系統隨機生成

        public Boolean IsPixel
        {
            get { return isPixel; }
            set { isPixel = value; }
        }

        private Boolean isRandString = true;

        // 是否添加隨機噪點字符串，默認添加
        public Boolean IsRandString
        {
            get { return isRandString; }
            set { isRandString = value; }
        }

        // 隨機背景字符串的個數
        public Int32 RandomStringCount
        {
            get;
            set;
        }

        // 隨機背景字符串的大小
        private Int32 randomStringFontSize = 9;

        public Int32 RandomStringFontSize
        {
            get { return randomStringFontSize; }
            set { randomStringFontSize = value; }
        }

        // 是否對圖片進行扭曲
        public Boolean IsTwist
        {
            get;
            set;
        }

        // 邊框樣式
        public enum BorderStyle
        {
            // 無邊框
            None,
            // 矩形邊框
            Rectangle,
            // 圓角邊框
            RoundRectangle
        }

        // 驗證碼字符串隨機轉動的角度的最大值
        private Int32 rotationAngle = 40;

        public Int32 RotationAngle
        {
            get { return rotationAngle; }
            set { rotationAngle = value; }
        }

        // 設置或獲取邊框樣式

        public BorderStyle Border
        {
            get;
            set;
        }

        private Point[] strPoint = null;

        private Double gaussianDeviation = 0;
        // 對驗證碼圖片進行高斯模糊的閥值，如果設置爲0，則不對圖片進行高斯模糊，該設置可能會對圖片處理的性能有較大影響

        public Double GaussianDeviation
        {
            get { return gaussianDeviation; }
            set { gaussianDeviation = value; }
        }

        private Int32 brightnessValue = 0;
        // 對圖片進行暗度和亮度的調整，如果該值爲0，則不調整。該設置會對圖片處理性能有較大影響

        public Int32 BrightnessValue
        {
            get { return brightnessValue; }
            set { brightnessValue = value; }
        }

        //------------------------------------------------------------  # 60個

        // 構造函數，用於初始化常用變量
        public void DrawValidationCode()
        {
            rand = new Random(Guid.NewGuid().GetHashCode());
            strPoint = new Point[validationCodeCount + 1];
            if (gaussianDeviation < 0)
            {
                gaussianDeviation = 0;
            }
        }

        // 生成驗證碼
        // <param name="target">用於存儲圖片的一般字節序列</param>
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

        // 畫驗證碼背景，例如，增加早點，添加曲線和直線等
        private Bitmap DrawBackground()
        {
            Bitmap bitmap1 = new Bitmap(bgWidth + 1, bgHeight + 1);
            Graphics g = Graphics.FromImage(bitmap1);
            g.SmoothingMode = SmoothingMode.HighQuality;

            g.Clear(Color.White);
            Rectangle rectangle = new Rectangle(0, 0, bgWidth, bgHeight);
            Brush brush = new SolidBrush(backColor);
            g.FillRectangle(brush, rectangle);

            //畫噪點
            if (isPixel == true)
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
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 畫正弦曲線
        private Bitmap DrawTwist(Bitmap bitmap0, Int32 tWidth, Int32 tHeight, float angle, Color color)
        {
            //爲了方便查看效果，在這裏我定義了一個常量。
            //它在定義數組的長度和for循環中都要用到。
            int size = bgWidth;

            double[] x = new double[size];
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p = new Pen(color);

            //畫正弦曲線的橫軸間距參數。建議所用的值應該是 正數且是2的倍數。
            //在這裏採用2。
            int val = 2;

            float temp = 0.0f;

            //把畫布下移100。爲什麼要這樣做，只要你把這一句給註釋掉，運行一下代碼，
            //你就會明白是爲什麼？
            g.TranslateTransform(0, 100);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            for (int i = 0; i < size; i++)
            {
                //改變tWidth，實現正弦曲線寬度的變化。
                //改tHeight，實現正弦曲線高度的變化。
                x[i] = Math.Sin(2 * Math.PI * i / tWidth) * tHeight;

                g.DrawLine(p, i * val, temp, i * val + val / 2, (float)x[i]);
                temp = (float)x[i];
            }
            g.RotateTransform(60, MatrixOrder.Prepend);

            //旋轉圖片
            // bitmap1 = KiRotate(b, angle, Color.Transparent);
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 正弦曲線Wave扭曲圖片
        /// <param name="srcBmp">圖片路徑</param>
        /// <param name="bXDir">如果扭曲則選擇爲True</param>
        /// <param name="dMultValue">波形的幅度倍數，越大扭曲的程度越高，一般爲3</param>
        /// <param name="dPhase">波形的起始相位，取值區間[0-2*PI)</param>
        /// <returns></returns>
        /// 2222
        public Bitmap TwistImage(Bitmap bitmap0, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);
            double PI2 = 6.283185307179586476925286766559;
            // 將位圖背景填充爲白色
            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, bitmap1.Width, bitmap1.Height);
            g.Dispose();

            double dBaseAxisLen = bXDir ? (double)bitmap1.Height : (double)bitmap1.Width;

            for (int i = 0; i < bitmap1.Width; i++)
            {
                for (int j = 0; j < bitmap1.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? (PI2 * (double)j) / dBaseAxisLen : (PI2 * (double)i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);

                    // 取得當前點的顏色
                    int nOldX = 0, nOldY = 0;
                    nOldX = bXDir ? i + (int)(dy * dMultValue) : i;
                    nOldY = bXDir ? j : j + (int)(dy * dMultValue);

                    Color color = bitmap0.GetPixel(i, j);
                    if (nOldX >= 0 && nOldX < bitmap1.Width && nOldY >= 0 && nOldY < bitmap1.Height)
                    {
                        bitmap1.SetPixel(nOldX, nOldY, color);
                    }
                }
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        /// 圖片任意角度旋轉
        /// <param name="bmp">原始圖Bitmap</param>
        /// <param name="angle">旋轉角度</param>
        /// <param name="bkColor">背景色</param>
        /// <returns>輸出Bitmap</returns>
        public static Bitmap KiRotate(Bitmap bitmap0, float angle, Color bkColor)
        {
            int w = bitmap0.Width;
            int h = bitmap0.Height;

            PixelFormat pf;

            if (bkColor == Color.Transparent)
            {
                pf = PixelFormat.Format32bppArgb;
            }
            else
            {
                pf = bitmap0.PixelFormat;
            }

            Bitmap bitmap1 = new Bitmap(w, h, pf);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(bkColor);
            g.DrawImageUnscaled(bitmap0, 1, 1);
            g.Dispose();

            GraphicsPath gp = new GraphicsPath();
            gp.AddRectangle(new RectangleF(0f, 0f, w, h));
            Matrix mtrx = new Matrix();
            mtrx.Rotate(angle);
            RectangleF rct = gp.GetBounds(mtrx);

            Bitmap bitmap2 = new Bitmap((int)rct.Width, (int)rct.Height, pf);
            g = Graphics.FromImage(bitmap2);
            g.Clear(bkColor);
            g.TranslateTransform(-rct.X, -rct.Y);
            g.RotateTransform(angle);
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;
            g.DrawImageUnscaled(bitmap1, 0, 0);
            g.Dispose();
            bitmap1.Dispose();

            return bitmap2;
        }

        //------------------------------------------------------------  # 60個

        // 隨機生成貝塞爾曲線
        // <param name="bmp">一個圖片的實例</param>
        // <param name="lineNum">線條數量</param>
        public Bitmap DrawRandomBezier(Int32 lineNum)
        {
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Transparent);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;

            GraphicsPath gp = new GraphicsPath();
            Int32 lineRandNum = rand.Next(lineNum);

            for (int i = 0; i < (lineNum - lineRandNum); i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                    new Point(rand.Next(1, (bitmap1.Width / 10)), rand.Next(1, (bitmap1.Height))),
                                    new Point(rand.Next((bitmap1.Width / 10) * 2, (bitmap1.Width / 10) * 4), rand.Next(1, (bitmap1.Height))),
                                    new Point(rand.Next((bitmap1.Width / 10) * 4, (bitmap1.Width / 10) * 6), rand.Next(1, (bitmap1.Height))),
                                    new Point(rand.Next((bitmap1.Width / 10) * 8, bitmap1.Width), rand.Next(1, (bitmap1.Height)))
                                };

                gp.AddBeziers(point);
                g.DrawPath(p, gp);
                p.Dispose();
            }

            for (int i = 0; i < lineRandNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                    new Point(rand.Next(1, bitmap1.Width), rand.Next(1, bitmap1.Height)),
                                    new Point(rand.Next((bitmap1.Width / 10) * 2, bitmap1.Width), rand.Next(1, bitmap1.Height)),
                                    new Point(rand.Next((bitmap1.Width / 10) * 4, bitmap1.Width), rand.Next(1, bitmap1.Height)),
                                    new Point(rand.Next(1, bitmap1.Width), rand.Next(1, bitmap1.Height))
                                };
                gp.AddBeziers(point);
                g.DrawPath(p, gp);
                p.Dispose();
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 畫直線
        // <param name="bmp">一個bmp實例</param>
        // <param name="lineNum">線條個數</param>
        public Bitmap DrawRandomLine(Int32 lineNum)
        {
            if (lineNum < 0) throw new ArgumentNullException("參數bmp爲空！");
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            for (int i = 0; i < lineNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point pt1 = new Point(rand.Next(1, (bitmap1.Width / 5) * 2), rand.Next(bitmap1.Height));
                Point pt2 = new Point(rand.Next((bitmap1.Width / 5) * 3, bitmap1.Width), rand.Next(bitmap1.Height));
                g.DrawLine(p, pt1, pt2);
                p.Dispose();
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 畫隨機噪點
        /// <param name="pixNum">噪點的百分比</param>
        public Bitmap DrawRandomPixel(Int32 pixNum)
        {
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;

            //畫噪點 
            for (int i = 0; i < (bgHeight * bgWidth) / pixNum; i++)
            {
                int x = rand.Next(bitmap1.Width);
                int y = rand.Next(bitmap1.Height);
                bitmap1.SetPixel(x, y, GetRandomDeepColor());
                //下移座標重新畫點
                if ((x + 1) < bitmap1.Width && (y + 1) < bitmap1.Height)
                {
                    //畫圖片的前景噪音點
                    g.DrawRectangle(new Pen(Color.Silver), rand.Next(bitmap1.Width), rand.Next(bitmap1.Height), 1, 1);
                }
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 畫隨機字符串中間連線
        private Bitmap DrawStringline()
        {
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
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

            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 寫入驗證碼的字符串
        private Bitmap DrawRandomString(string Code)
        {
            if (fontMaxSize >= (bgHeight / 5) * 4)
            {
                throw new ArgumentException("字體最大值參數FontMaxSize與驗證碼高度相近，這會導致描繪驗證碼字符串時出錯，請重新設置參數！");
            }

            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();

            Graphics g = Graphics.FromImage(bitmap1);
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
            FontFamily font_family = new FontFamily(GenericFontFamilies.Monospace);

            Int32 charNum = chars.Length;

            Point sPoint = new Point();
            Int32 fontSize = 12;
            for (int i = 0; i < validationCodeCount; i++)
            {
                int findex = rand.Next(5);
                //定義字體
                Font f = new Font(font_family, rand.Next(fontMinSize, fontMaxSize), FontStyle.Bold);
                //定義畫刷，用於寫字符串
                //Brush brush = new SolidBrush(GetRandomDeepColor());
                Int32 textFontSize = Convert.ToInt32(f.Size);
                fontSize = textFontSize;
                Point point = new Point(rand.Next((bgWidth / charNum) * i + 5, (bgWidth / charNum) * (i + 1)), rand.Next(bgHeight / 5 + textFontSize / 2, bgHeight - textFontSize / 2));

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

                float angle = rand.Next(-rotationAngle, rotationAngle);//轉動的度數
                g.TranslateTransform(point.X, point.Y);//移動光標到指定位置
                g.RotateTransform(angle);

                //設置漸變畫刷  
                Rectangle myretang = new Rectangle(0, 1, Convert.ToInt32(f.Size), Convert.ToInt32(f.Size));
                Color c = GetRandomDeepColor();
                LinearGradientBrush mybrush2 = new LinearGradientBrush(myretang, c, GetLightColor(c, 120), rand.Next(180));

                g.DrawString(chars[i].ToString(), f, mybrush2, 1, 1, format);

                g.RotateTransform(-angle);//轉回去
                g.TranslateTransform(-point.X, -point.Y);//移動光標到指定位置，每個字符緊湊顯示，避免被軟件識別

                strPoint[i] = point;

                f.Dispose();
                mybrush2.Dispose();
            }
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 畫背景干擾文字
        private Bitmap DrawRandBgString()
        {
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            String[] randStr = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" };
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);

            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;
            g.InterpolationMode = InterpolationMode.HighQualityBilinear;

            //設置字體顯示格式
            StringFormat format = new StringFormat(StringFormatFlags.NoClip);
            format.Alignment = StringAlignment.Center;
            format.LineAlignment = StringAlignment.Center;

            FontFamily font_family = new FontFamily(GenericFontFamilies.Serif);
            Font f = new Font(font_family, randomStringFontSize, FontStyle.Underline);

            int randAngle = 60; //隨機轉動角度

            for (int i = 0; i < RandomStringCount; i++)
            {

                Brush brush = new SolidBrush(GetRandomLightColor());
                Point pot = new Point(rand.Next(5, bgWidth - 5), rand.Next(5, bgHeight - 5));
                //隨機轉動的度數
                float angle = rand.Next(-randAngle, randAngle);

                //轉動畫布
                g.RotateTransform(angle);
                g.DrawString(randStr[rand.Next(randStr.Length)], f, brush, pot, format);
                //轉回去，爲下一個字符做準備
                g.RotateTransform(-angle);
                //釋放資源
                brush.Dispose();
            }
            f.Dispose();
            format.Dispose();
            font_family.Dispose();

            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 內部方法：繪製驗證碼背景
        private void DrawBackground(HatchStyle hatchStyle)
        {
            //設置填充背景時用的筆刷
            HatchBrush hBrush = new HatchBrush(hatchStyle, backColor);

            //填充背景圖片
            dc.FillRectangle(hBrush, 0, 0, this.bgWidth, this.bgHeight);
        }

        //------------------------------------------------------------  # 60個

        // 返回一個隨機點，該隨機點範圍在驗證碼背景大小範圍內
        /// <returns>Point對象</returns>
        private Point RandomPoint()
        {
            Random rand = new Random();
            Point point = new Point(rand.Next(this.bgWidth), rand.Next(this.bgHeight));
            return point;
        }

        //------------------------------------------------------------  # 60個

        // 隨機生成顏色值
        // 生成隨機深顏色
        public Color GetRandomDeepColor()
        {
            int nRed, nGreen, nBlue;    // nBlue,nRed  nGreen 相差大一點 nGreen 小一些
            //int high = 255;       
            int redLow = 160;
            int greenLow = 100;
            int blueLow = 160;
            nRed = rand.Next(redLow);
            nGreen = rand.Next(greenLow);
            nBlue = rand.Next(blueLow);
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }

        // 生成隨機淺顏色
        /// <returns>randomColor</returns>
        public Color GetRandomLightColor()
        {
            int nRed, nGreen, nBlue;    //越大顏色越淺
            int low = 180;           //色彩的下限
            int high = 255;          //色彩的上限      
            nRed = rand.Next(high) % (high - low) + low;
            nGreen = rand.Next(high) % (high - low) + low;
            nBlue = rand.Next(high) % (high - low) + low;
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }

        // 生成隨機顏色值
        public Color GetRandomColor()
        {
            int nRed, nGreen, nBlue;    //越大顏色越淺
            int low = 10;           //色彩的下限
            int high = 255;          //色彩的上限    
            nRed = rand.Next(high) % (high - low) + low;
            nGreen = rand.Next(high) % (high - low) + low;
            nBlue = rand.Next(high) % (high - low) + low;
            Color color = Color.FromArgb(nRed, nGreen, nBlue);
            return color;
        }

        // 獲取與當前顏色值相加後的顏色
        // <param name="c"></param>
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

        //------------------------------------------------------------  # 60個

        // 合併圖片
        private Bitmap MergerImg(params Bitmap[] maps)
        {
            int i = maps.Length;
            if (i == 0)
            {
                throw new Exception("圖片數不能夠爲0");
            }

            //創建要顯示的圖片對象,根據參數的個數設置寬度            
            Bitmap bitmap1 = new Bitmap(i * 12, 16);
            Graphics g = Graphics.FromImage(bitmap1);
            //清除畫布,背景設置爲白色            
            g.Clear(Color.White);
            for (int j = 0; j < i; j++)
            {
                //g.DrawImage(maps[j], j * 11, 0, maps[j].Width, maps[j].Height);
                g.DrawImageUnscaled(maps[j], 0, 0);
            }
            g.Dispose();
            return bitmap1;
        }

        //------------------------------------------------------------  # 60個

        // 生成不重複的隨機數，該函數會消耗大量系統資源
        private static int GetRandomSeed()
        {
            byte[] bytes = new byte[4];
            RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();
            rng.GetBytes(bytes);
            return BitConverter.ToInt32(bytes, 0);
        }

        //------------------------------------------------------------  # 60個

        // 縮放圖片
        /// <param name="bmp">原始Bitmap</param>
        /// <param name="newW">新的寬度</param>
        /// <param name="newH">新的高度</param>
        /// <param name="Mode">縮放質量</param>
        /// <returns>處理以後的圖片</returns>
        public static Bitmap KiResizeImage(Bitmap bmp, int newW, int newH, InterpolationMode Mode)
        {
            try
            {
                Bitmap bitmap1 = new Bitmap(newW, newH);
                Graphics g = Graphics.FromImage(bitmap1);
                // 插值算法的質量
                g.InterpolationMode = Mode;
                g.DrawImage(bmp, new Rectangle(0, 0, newW, newH), new Rectangle(0, 0, bmp.Width, bmp.Height), GraphicsUnit.Pixel);
                g.Dispose();
                return bitmap1;
            }
            catch
            {
                return null;
            }
        }

        //------------------------------------------------------------  # 60個

        // 繪製圓角矩形
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
            // 調用 CreateRoundedRectanglePath 得到圓角矩形的路徑，然後再進行繪製
            g.DrawPath(p, CreateRoundedRectanglePath(rectangle, r));
        }

        //------------------------------------------------------------  # 60個

        // 根據普通矩形得到圓角矩形的路徑
        // <param name="rectangle">原始矩形</param>
        // <param name="r">半徑</param>
        // <returns>圖形路徑</returns>
        // 繪製圓角矩形3, 把圓角矩形分成八段直線弧線的組合，依次加到路徑中
        private static GraphicsPath CreateRoundedRectanglePath(Rectangle rect, int R)
        {
            int D = R * 2;
            GraphicsPath gp = new GraphicsPath();
            //左上
            gp.AddArc(new Rectangle(rect.X, rect.Y, D, D), 180, 90);
            //上
            gp.AddLine(new Point(rect.X + R, rect.Y), new Point(rect.Right - R, rect.Y));
            //右上
            gp.AddArc(new Rectangle(rect.Right - D, rect.Y, D, D), 270, 90);
            //右
            gp.AddLine(new Point(rect.Right, rect.Y + R), new Point(rect.Right, rect.Bottom - R));
            //右下
            gp.AddArc(new Rectangle(rect.Right - D, rect.Bottom - D, D, D), 0, 90);
            //下
            gp.AddLine(new Point(rect.Right - R, rect.Bottom), new Point(rect.X + R, rect.Bottom));
            //左下
            gp.AddArc(new Rectangle(rect.X, rect.Bottom - D, D, D), 90, 90);
            //左
            gp.AddLine(new Point(rect.X, rect.Bottom - R), new Point(rect.X, rect.Y + R));
            gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接
            return gp;
        }

        //------------------------------------------------------------  # 60個

        // 柔化
        // <param name="b">原始圖</param>
        // <returns>輸出圖</returns>
        public static Bitmap KiBlur(Bitmap bitmap0)
        {
            if (bitmap0 == null)
            {
                return null;
            }

            int w = bitmap0.Width;
            int h = bitmap0.Height;

            try
            {
                Bitmap bitmap1 = new Bitmap(w, h, PixelFormat.Format24bppRgb);

                BitmapData srcData = bitmap0.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);
                BitmapData dstData = bitmap1.LockBits(new Rectangle(0, 0, w, h), ImageLockMode.WriteOnly, PixelFormat.Format24bppRgb);

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

                bitmap0.UnlockBits(srcData);
                bitmap1.UnlockBits(dstData);

                return bitmap1;
            }
            catch
            {
                return null;
            }

        } // end of KiBlur

        //------------------------------------------------------------  # 60個

        // 濾鏡
        // 紅色濾鏡
        // <param name="threshold">閥值 -255~255</param>
        public Bitmap AdjustToRed(Bitmap bitmap1, int threshold)
        {
            for (int y = 0; y < bitmap1.Height; y++)
            {
                for (int x = 0; x < bitmap1.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap1.GetPixel(x, y);
                    var pR = pixel.R + threshold;
                    pR = Math.Max(pR, 0);
                    pR = Math.Min(255, pR);
                    // 將改過的 RGB 寫回
                    // 只寫入紅色的值 , G B 都放零
                    Color newColor = Color.FromArgb(pixel.A, pR, 0, 0);
                    bitmap1.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap1;
        }

        // 綠色濾鏡
        // <param name="threshold">閥值 -255~+255</param>
        public Bitmap AdjustToGreen(Bitmap bitmap1, int threshold)
        {
            for (int y = 0; y < bitmap1.Height; y++)
            {
                for (int x = 0; x < bitmap1.Width; x++)
                {
                    // 取得每一個 pixel
                    var pixel = bitmap1.GetPixel(x, y);
                    //判斷是否超過255 如果超過就是255 
                    var pG = pixel.G + threshold;
                    //如果小於0就為0
                    if (pG > 255)
                    {
                        pG = 255;
                    }
                    if (pG < 0)
                    {
                        pG = 0;
                    }
                    // 將改過的 RGB 寫回
                    // 只寫入綠色的值 , R B 都放零
                    Color newColor = Color.FromArgb(pixel.A, 0, pG, 0);
                    bitmap1.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap1;
        }

        // 藍色濾鏡
        // <param name="threshold">閥值 -255~255</param>
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
                    if (pB > 255)
                    {
                        pB = 255;
                    }
                    if (pB < 0)
                    {
                        pB = 0;
                    }
                    // 將改過的 RGB 寫回
                    // 只寫入藍色的值 , R G 都放零
                    Color newColor = Color.FromArgb(pixel.A, 0, 0, pB);
                    bitmap.SetPixel(x, y, newColor);
                }
            }
            // 回傳結果
            return bitmap;
        }

        // 調整 RGB 色調
        // <param name="thresholdRed">紅色閥值</param>
        // <param name="thresholdBlue">藍色閥值</param>
        // <param name="thresholdGreen">綠色閥值</param>
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

        //------------------------------------------------------------  # 60個

        // 增加或減少亮度
        // <param name="valBrightness">0~255</param>
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

        //------------------------------------------------------------  # 60個

        // 浮雕效果
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

        //------------------------------------------------------------  # 60個

        // 水波紋效果
        /// <param name="nWave">坡度</param>
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

            double newX;
            double newY;
            double xo;
            double yo;

            //先取樣將水波紋座標跟RGB取出
            for (int x = 0; x < nWidth; ++x)
            {
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
            }

            //進行合成
            Bitmap bSrc = (Bitmap)src.Clone();

            // 依照 Format24bppRgb 每三個表示一 Pixel 0: 藍 1: 綠 2: 紅
            BitmapData bitmapData = src.LockBits(new Rectangle(0, 0, src.Width, src.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);
            BitmapData bmSrc = bSrc.LockBits(new Rectangle(0, 0, bSrc.Width, bSrc.Height), ImageLockMode.ReadWrite, PixelFormat.Format24bppRgb);

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

        //------------------------------------------------------------  # 60個

        // 調整曝光度值
        /// <param name="src">原圖</param>
        /// <param name="r"></param>
        /// <param name="g"></param>
        /// <param name="b"></param>
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

        //------------------------------------------------------------  # 60個

        // 高對比,對過深的顏色調淺，過淺的顏色調深。
        /// <param name="effectThreshold"> 高對比程度 -100~100</param>
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

        //------------------------------------------------------------  # 60個

        // 對圖片進行霧化效果
        /// <param name="bmp"></param>
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
                    Random rand = new Random(Guid.NewGuid().GetHashCode());
                    int k = rand.Next(123456);
                    //像素塊大小
                    int dx = x + k % 19;
                    int dy = y + k % 19;
                    if (dx >= Width)
                    {
                        dx = Width - 1;
                    }
                    if (dy >= Height)
                    {
                        dy = Height - 1;
                    }
                    pixel = oldBitmap.GetPixel(dx, dy);
                    newBitmap.SetPixel(x, y, pixel);
                }
            }
            return newBitmap;
        }

        //------------------------------------------------------------  # 60個
    } //END Class DrawValidationCode

    //------------------------------------------------------------  # 60個

    //高斯模糊算法
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
                {
                    sum += matrix[i, j];
                }
            }
            if (sum != 0)
            {
                for (int i = 0; i < ret.GetLength(0); i++)
                {
                    for (int j = 0; j < ret.GetLength(1); j++)
                    {
                        ret[i, j] = matrix[i, j] / sum;
                    }
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
                {
                    res1[i, j] = processPoint(matrix, i, j, kernel, 0);
                }
            }

            //y-direction
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    res2[i, j] = processPoint(res1, i, j, kernel, 1);
                }
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

        // 對顏色值進行灰色處理
        private Color grayscale(Color cr)
        {
            return Color.FromArgb(cr.A, (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11), (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11),
              (int)(cr.R * .3 + cr.G * .59 + cr.B * 0.11));
        }

        /// 對圖片進行高斯模糊
        /// <param name="d">模糊數值，數值越大模糊越很</param>
        /// <param name="image">一個需要處理的圖片</param>
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

    //------------------------------------------------------------  # 60個

    /// Captcha17
    public class Captcha17
    {
        // 隨機種子
        private Random rand = new Random();

        // 驗證碼長度
        private int length = 4;
        // 驗證碼長度(默認為4)
        public int Length
        {
            get { return this.length; }
            set { this.length = value; }
        }

        // 驗證碼字符串
        private string verifyCodeText = null;

        // 驗證碼字符串
        public string VerifyCodeText
        {
            get { return this.verifyCodeText; }
            set { this.verifyCodeText = value; }
        }

        // 是否加入小寫字母
        private bool addLowerLetter = false;

        // 是否加入小寫字母(不包括o)
        public bool AddLowerLetter
        {
            get { return this.addLowerLetter; }
            set { this.addLowerLetter = value; }
        }

        // 是否加入大寫字母
        private bool addUpperLetter = false;

        // 是否加入大寫字母(不包括O)
        public bool AddUpperLetter
        {
            get { return this.addUpperLetter; }
            set { this.addUpperLetter = value; }
        }

        //------------------------------------------------------------  # 60個

        // 字體大小(默認為18)
        private int fontSize = 18;

        public int FontSize
        {
            get { return this.fontSize; }
            set { this.fontSize = value; }
        }

        //------------------------------------------------------------  # 60個

        // 字體顏色
        private Color fontColor = Color.Blue;

        // 字體顏色(默認為Blue)

        public Color FontColor
        {
            get { return this.fontColor; }
            set { this.fontColor = value; }
        }

        //------------------------------------------------------------  # 60個

        // 字體類型(默認為Verdana)
        private string fontFamily = "Verdana";

        public string FontFamily
        {
            get { return this.fontFamily; }
            set { this.fontFamily = value; }
        }

        //------------------------------------------------------------  # 60個

        // 背景色
        private Color backgroundColor = Color.AliceBlue;

        /// 背景色(默認為AliceBlue)
        public Color BackgroundColor
        {
            get { return this.backgroundColor; }
            set { this.backgroundColor = value; }
        }

        //------------------------------------------------------------  # 60個

        // 前景噪點數量
        private int foreNoisePointCount = 2;

        // 前景噪點數量(默認為2)
        public int ForeNoisePointCount
        {
            get { return this.foreNoisePointCount; }
            set { this.foreNoisePointCount = value; }
        }

        //------------------------------------------------------------  # 60個

        // 隨機碼的旋轉角度
        private int randomAngle = 45;

        // 隨機碼的旋轉角度(默認為40度)
        public int RandomAngle
        {
            get { return this.randomAngle; }
            set { this.randomAngle = value; }
        }

        //------------------------------------------------------------  # 60個

        // 構造方法
        public Captcha17()
        {
            this.GetText();
        }

        // 得到驗證碼字符串
        private void GetText()
        {
            verifyCodeText = "3279";
        }

        //------------------------------------------------------------  # 60個

        // 得到驗證碼圖片
        public Bitmap GetImage()
        {
            Bitmap result = new Bitmap(this.verifyCodeText.Length * 16, 25);
            Graphics g = Graphics.FromImage(result);

            g.SmoothingMode = SmoothingMode.HighQuality;

            //清除整個繪圖面並以指定背景色填充
            g.Clear(this.backgroundColor);

            SolidBrush sb = new SolidBrush(this.fontColor);
            this.AddForeNoisePoint(result);

            this.AddBackgroundNoisePoint(result, g);

            //文字居中
            StringFormat objStringFormat = new StringFormat(StringFormatFlags.NoClip);

            objStringFormat.Alignment = StringAlignment.Center;
            objStringFormat.LineAlignment = StringAlignment.Center;

            //字體樣式
            Font f = new Font(this.fontFamily, rand.Next(this.fontSize - 3, this.fontSize), FontStyle.Regular);

            //驗證碼旋轉，防止機器識別
            char[] chars = this.verifyCodeText.ToCharArray();

            for (int i = 0; i < chars.Length; i++)
            {
                //轉動的度數
                float angle = rand.Next(-this.randomAngle, this.randomAngle);

                g.TranslateTransform(12, 12);
                g.RotateTransform(angle);
                g.DrawString(chars[i].ToString(), f, sb, -2, 2, objStringFormat);
                g.RotateTransform(-angle);
                g.TranslateTransform(2, -12);
            }
            return result;
        }

        // 添加前景噪點
        private void AddForeNoisePoint(Bitmap bitmap1)
        {
            for (int i = 0; i < bitmap1.Width * this.foreNoisePointCount; i++)
            {
                bitmap1.SetPixel(rand.Next(bitmap1.Width), rand.Next(bitmap1.Height), this.fontColor);
            }
        }

        // 添加背景噪點
        private void AddBackgroundNoisePoint(Bitmap bitmap1, Graphics g)
        {
            Pen p = new Pen(Color.Azure, 0);
            for (int i = 0; i < bitmap1.Width * 2; i++)
            {
                g.DrawRectangle(p, rand.Next(bitmap1.Width), rand.Next(bitmap1.Height), 1, 1);
            }
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

