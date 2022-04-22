using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Drawing.Text;      //for TextRenderingHint

// 全自動區分電腦和人類的公開圖靈測試
//（英語：Completely Automated Public Turing test to tell Computers and Humans Apart，簡稱CAPTCHA）
// 俗稱驗證碼

namespace vcs_Draw_Captcha1
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
            timer1_Tick(sender, e);
        }

        void show_item_location()
        {
            int W = 300;
            int H = 110;

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

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 10;
            y_st = 10;
            dx = W + 10;
            dy = H + 10;

            pictureBox00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            pictureBox04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            pictureBox05.Location = new Point(x_st + dx * 0, y_st + dy * 5);

            pictureBox06.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox07.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox08.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox09.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            pictureBox10.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            pictureBox11.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            pictureBox12.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox13.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox14.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox15.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            pictureBox16.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            pictureBox17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            pictureBox18.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox19.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox20.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox21.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox22.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            pictureBox23.Location = new Point(x_st + dx * 3, y_st + dy * 5);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

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
        }

        //Captcha 00 ST
        private void draw_captcha00()
        {
            VryImgGen captcha = new VryImgGen();
            captcha.Length = 10;
            string code = captcha.CreateVerifyCode();
            //richTextBox1.Text += code + "\n";

            Bitmap bitmap1 = captcha.CreateImage(code);
            pictureBox00.Image = bitmap1;
        }
        //Captcha 00 SP

        //Captcha 01 ST
        //中文驗證法碼 ST
        public string txt = "";
        private void draw_captcha01()
        {
            //获取GB2312编码页（表） 
            Encoding gb = Encoding.GetEncoding("gb2312");
            //调用函数产生4个随机中文汉字编码 
            object[] bytes = CreateCode(4);
            //根据汉字编码的字节数组解码出中文汉字 
            string str1 = gb.GetString((byte[])Convert.ChangeType(bytes[0], typeof(byte[])));
            string str2 = gb.GetString((byte[])Convert.ChangeType(bytes[1], typeof(byte[])));
            string str3 = gb.GetString((byte[])Convert.ChangeType(bytes[2], typeof(byte[])));
            string str4 = gb.GetString((byte[])Convert.ChangeType(bytes[3], typeof(byte[])));
            txt = str1 + str2 + str3 + str4;

            if (txt == null || txt == String.Empty)
            {
                return;
            }

            //lb_captcha1.Text = txt;

            Bitmap image = new Bitmap((int)Math.Ceiling((txt.Length * 20.5)) * 3, 22 * 3);
            Graphics g = Graphics.FromImage(image);
            try
            {
                //生成随机生成器
                Random random = new Random();
                //清空图片背景色
                g.Clear(Color.White);
                //画图片的背景噪音线
                for (int i = 0; i < 2; i++)
                {
                    Point tem_Point_1 = new Point(random.Next(image.Width), random.Next(image.Height));
                    Point tem_Point_2 = new Point(random.Next(image.Width), random.Next(image.Height));
                    g.DrawLine(new Pen(Color.Black), tem_Point_1, tem_Point_2);
                }
                Font font = new Font("宋体", 12 * 2, (FontStyle.Bold));
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, image.Width, image.Height), Color.Blue, Color.DarkRed, 1.2f, true);
                g.DrawString(txt, font, brush, 2, 2);
                //画图片的前景噪音点
                for (int i = 0; i < 100; i++)
                {
                    Point tem_point = new Point(random.Next(image.Width), random.Next(image.Height));
                    image.SetPixel(tem_point.X, tem_point.Y, Color.FromArgb(random.Next()));
                }
                //画图片的边框线
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);
                pictureBox01.Image = image;
            }
            catch { }
        }

        /**/
        /* 
        此函数在汉字编码范围内随机创建含两个元素的十六进制字节数组，每个字节数组代表一个汉字，并将 
        四个字节数组存储在object数组中。 
        参数：strlength，代表需要产生的汉字个数 
        */
        public static object[] CreateCode(int strlength)
        {
            //定义一个字符串数组储存汉字编码的组成元素 
            string[] r = new String[16] { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" };
            Random rnd = new Random();
            //定义一个object数组用来 
            object[] bytes = new object[strlength];
            /**/
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
                rnd = new Random(r1 * unchecked((int)DateTime.Now.Ticks) + i);//更换随机数发生器的种子避免产生重复值 
                int r2;
                if (r1 == 13)
                    r2 = rnd.Next(0, 7);
                else
                    r2 = rnd.Next(0, 16);
                string str_r2 = r[r2].Trim();
                //区位码第3位 
                rnd = new Random(r2 * unchecked((int)DateTime.Now.Ticks) + i);
                int r3 = rnd.Next(10, 16);
                string str_r3 = r[r3].Trim();
                //区位码第4位 
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
        //中文驗證法碼 SP
        //Captcha 01 SP

        //Captcha 02 ST
        void draw_captcha02()
        {
            //產生驗證圖片

            //從已知幾個元素中任意選出幾個
            int num = 10;

            string vaildNumAnswer = "";

            Random rr = new Random();

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
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表


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

            //亂數產生驗證答案
            vaildNumAnswer = "";
            for (int i = 1; i <= num; i++)
            {
                char c = texts[rr.Next(texts.Length)];
                vaildNumAnswer += c;
            }
            //richTextBox1.Text += vaildNumAnswer + "\n";

            RenderImage(vaildNumAnswer);
        }

        //產生驗證圖片
        private void RenderImage(string vaildNumAnswer)
        {
            Random rr = new Random();

            int num = 10;
            int ww = 30 * 2 + num * 20;
            //寬度=(留邊)30*2 + 每個字*20
            int hh = 70;

            Bitmap vaildNumImage = new Bitmap(ww, hh);
            Graphics g = Graphics.FromImage(vaildNumImage);

            //產生背景色
            Color cc = Color.FromArgb(rr.Next(256), rr.Next(256), rr.Next(256));
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
                g.FillRectangle(bb, rr.Next(ww), rr.Next(hh), 2, 2);
            }
            pictureBox02.Image = vaildNumImage;
        }
        //Captcha 02 SP

        //Captcha 03 ST
        private void draw_captcha03()
        {
            CodeImage(CheckCode(), pictureBox03);    //for //for pictureBox03
        }

        private string CheckCode()
        {
            int number;
            char code;
            string checkCode = String.Empty;

            Random random = new Random();

            for (int i = 0; i < 4; i++)
            {
                number = random.Next();

                if (number % 2 == 0)
                    code = (char)('0' + (char)(number % 10));
                else
                    code = (char)('A' + (char)(number % 26));

                checkCode += " " + code.ToString();
            }
            return checkCode;
        }

        private void CodeImage(string checkCode, PictureBox pbx)
        {
            if (checkCode == null || checkCode.Trim() == String.Empty)
                return;

            Bitmap image = new Bitmap((int)Math.Ceiling((checkCode.Length * 20.0)), 50);
            Graphics g = Graphics.FromImage(image);

            try
            {
                //產生隨機產生器
                Random random = new Random();
                //清空圖片背景色
                g.Clear(Color.White);
                //畫圖片的背景噪音線
                for (int i = 0; i < 3; i++)
                {
                    int x1 = random.Next(image.Width);
                    int x2 = random.Next(image.Width);
                    int y1 = random.Next(image.Height);
                    int y2 = random.Next(image.Height);
                    g.DrawLine(new Pen(Color.Black), x1, y1, x2, y2);
                }
                Font font = new Font("Arial", 24, (FontStyle.Bold));
                g.DrawString(checkCode, font, new SolidBrush(Color.Red), 2, 2);

                //畫圖片的前景噪音點
                for (int i = 0; i < 150; i++)
                {
                    int x = random.Next(image.Width);
                    int y = random.Next(image.Height);

                    image.SetPixel(x, y, Color.FromArgb(random.Next()));
                }
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);
                pbx.Width = image.Width;
                pbx.Height = image.Height;
                pbx.BackgroundImage = image;
            }
            catch
            { }
        }
        //Captcha 03 SP

        //Captcha 04 ST
        void draw_captcha04()
        {
            string code;
            Bitmap bitmap1 = VerifyCodeHelper.CreateVerifyCodeBmp(out code);
            Bitmap bitmap2 = new Bitmap(bitmap1, 300, 200);  //改變大小

            //lb_captcha4.Text = code;
            pictureBox04.Image = bitmap1;
            //pictureBox4.Image = bitmap2;  //改變大小
        }
        //Captcha 04 SP

        //Captcha 05 ST

        //Captcha 05 SP


        //Captcha 06 ST
        void draw_captcha06()
        {
            //製作驗證碼3
            //C#生成驗證碼例子及代碼

            Random r = new Random();
            string str = "";
            for (int i = 0; i < 5; i++)
            {
                int rNumber = r.Next(0, 10);
                str += rNumber;
            }

            //創建一個圖片對象
            Bitmap bmp = new Bitmap(120, 25);
            //創建GDI對象
            Graphics g = Graphics.FromImage(bmp);
            // MessageBox.Show(str);

            string[] fonts = { "黑體", "楷體", "微軟雅黑", "宋體", "隸書" };
            Color[] colors = { Color.Red, Color.Yellow, Color.Blue, Color.Black, Color.Green };

            for (int i = 0; i < 5; i++)
            {
                Point p = new Point(i * 20, 0);//0,0 20 0
                g.DrawString(str[i].ToString(), new Font(fonts[r.Next(0, 5)], 20, FontStyle.Bold), new SolidBrush(colors[r.Next(0, 5)]), p);
            }

            //畫線
            for (int i = 0; i < 25; i++)
            {
                Point p1 = new Point(r.Next(0, bmp.Width), r.Next(0, bmp.Height));
                Point p2 = new Point(r.Next(0, bmp.Width), r.Next(0, bmp.Height));
                g.DrawLine(new Pen(Color.Green), p1, p2);
            }

            //畫像素顆粒
            for (int i = 0; i < 100; i++)
            {
                Point p = new Point(r.Next(0, bmp.Width), r.Next(0, bmp.Height));
                bmp.SetPixel(p.X, p.Y, Color.Black);
            }

            //把畫好的圖片放到PictureBox上
            pictureBox06.Image = bmp;
        }
        //Captcha 06 SP

        //Captcha 07 ST
        void draw_captcha07()
        {
            string txt = "This is a lion-mouse";

            Bitmap bm = MakeCaptchaImge1(txt,
                50, 70,
                pictureBox13.ClientSize.Width,
                pictureBox13.ClientSize.Height);
            pictureBox07.Image = bm;
        }
        //Captcha 07 SP

        //Captcha 08 ST
        void draw_captcha08()
        {
            string txt = "This is a lion-mouse";

            using (Font the_font = new Font("Times New Roman", 30))
            {
                pictureBox08.Image = MakeCaptchaImage2(txt,
                    pictureBox14.ClientSize.Width,
                    pictureBox14.ClientSize.Height,
                    the_font, Brushes.Blue);
            }
        }

        private Random Rand = new Random();

        // Make a captcha image for the text.
        private Bitmap MakeCaptchaImge1(string txt, int min_size, int max_size, int wid, int hgt)
        {
            // Make the bitmap and associated Graphics object.
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.SmoothingMode = SmoothingMode.HighQuality;
                g.Clear(Color.White);

                // See how much room is available for each character.
                int ch_wid = (int)(wid / txt.Length);

                // Draw each character.
                for (int i = 0; i < txt.Length; i++)
                {
                    float font_size = Rand.Next(min_size, max_size);
                    using (Font the_font = new Font("Times New Roman", font_size, FontStyle.Bold))
                    {
                        DrawCharacter1(txt.Substring(i, 1), g, the_font, i * ch_wid, ch_wid, wid, hgt);
                    }
                }
            }

            return bm;
        }

        // Draw a deformed character at this position.
        private int PreviousAngle = 0;
        private void DrawCharacter1(string txt, Graphics g, Font the_font, int X, int ch_wid, int wid, int hgt)
        {
            // Center the text.
            using (StringFormat string_format = new StringFormat())
            {
                string_format.Alignment = StringAlignment.Center;
                string_format.LineAlignment = StringAlignment.Center;
                RectangleF rectf = new RectangleF(X, 0, ch_wid, hgt);

                // Convert the text into a path.
                using (GraphicsPath graphics_path = new GraphicsPath())
                {
                    graphics_path.AddString(txt,
                        the_font.FontFamily, (int)(Font.Style),
                        the_font.Size, rectf, string_format);

                    // Make random warping parameters.
                    float x1 = (float)(X + Rand.Next(ch_wid) / 2);
                    float y1 = (float)(Rand.Next(hgt) / 2);
                    float x2 = (float)(X + ch_wid / 2 + Rand.Next(ch_wid) / 2);
                    float y2 = (float)(hgt / 2 + Rand.Next(hgt) / 2);
                    PointF[] pts = {
                    new PointF(
                        (float)(X + Rand.Next(ch_wid) / 4),
                        (float)(Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + ch_wid - Rand.Next(ch_wid) / 4),
                        (float)(Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + Rand.Next(ch_wid) / 4),
                        (float)(hgt - Rand.Next(hgt) / 4)),
                    new PointF(
                        (float)(X + ch_wid - Rand.Next(ch_wid) / 4),
                        (float)(hgt - Rand.Next(hgt) / 4))
                };
                    Matrix mat = new Matrix();
                    graphics_path.Warp(pts, rectf, mat,
                        WarpMode.Perspective, 0);

                    // Rotate a bit randomly.
                    float dx = (float)(X + ch_wid / 2);
                    float dy = (float)(hgt / 2);
                    g.TranslateTransform(-dx, -dy, MatrixOrder.Append);
                    int angle = PreviousAngle;
                    do
                    {
                        angle = Rand.Next(-30, 30);
                    } while (Math.Abs(angle - PreviousAngle) < 20);
                    PreviousAngle = angle;
                    g.RotateTransform(angle, MatrixOrder.Append);
                    g.TranslateTransform(dx, dy, MatrixOrder.Append);

                    // Draw the text.
                    g.FillPath(Brushes.Blue, graphics_path);
                    g.ResetTransform();
                }
            }
        }

        // Draw the words with letters overlapping each other.
        private Bitmap MakeCaptchaImage2(string txt, int wid, int hgt, Font the_font, Brush the_brush)
        {
            Bitmap bm = new Bitmap(wid, hgt);
            using (Graphics g = Graphics.FromImage(bm))
            {
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                int x = 0;
                foreach (char ch in txt.ToCharArray())
                {
                    SizeF ch_size = g.MeasureString(ch.ToString(), the_font);
                    int y = (int)(Rand.NextDouble() * (hgt - ch_size.Height));
                    g.DrawString(ch.ToString(), the_font, the_brush, x, y);
                    x += (int)(ch_size.Width * 0.35);
                }
            }
            return bm;
        }

        void draw_captcha05()
        {
            string ccc = "this is a lion-mouse";
            CreateImage(ccc);
        }

        //彩色驗證碼
        private void CreateImage(string checkCode)
        {
            int W = checkCode.Length * 15;
            int H = 50;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            //定義顏色
            Color[] c = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
            //定義字體
            string[] font = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };
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

                Font f = new Font(font[findex], 15, FontStyle.Bold);
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

            pictureBox05.Image = bitmap1;
        }
    }

    /// <summary>
    /// 驗證碼
    /// </summary>
    public class VerifyCodeHelper
    {
        #region 變量
        /// <summary>
        /// 色彩表
        /// </summary>
        private static Color[] colors = new Color[]{
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
      Color.FromArgb(255,165,0)};

        /// <summary>
        /// 字體表
        /// </summary>
        private static string[] fonts = new string[] { 
      "Arial",
      "Verdana", 
      "Georgia", 
      "黑體" };

        /// <summary>
        /// 字體年夜小
        /// </summary>
        private static int fontSize = 22;
        #endregion

        #region 生成驗證碼圖片
        /// <summary>
        /// 生成驗證碼圖片
        /// </summary>
        public static Bitmap CreateVerifyCodeBmp(out string code)
        {
            int width = 120;
            int height = 40;
            Bitmap bmp = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bmp);
            Random rnd = new Random();

            //配景色
            g.FillRectangle(new SolidBrush(Color.White), new Rectangle(0, 0, width, height));

            //文字
            StringBuilder sbCode = new StringBuilder();
            for (int i = 0; i < 4; i++)
            {
                string str = GetChar(rnd);
                Font font = GetFont(rnd);
                Color color = GetColor(rnd);
                g.DrawString(str, font, new SolidBrush(color), new PointF((float)(i * width / 4.0), 0));
                sbCode.Append(str);
            }
            code = sbCode.ToString();

            //樂音線
            for (int i = 0; i < 10; i++)
            {
                int x1 = rnd.Next(bmp.Width);
                int x2 = rnd.Next(bmp.Width);
                int y1 = rnd.Next(bmp.Height);
                int y2 = rnd.Next(bmp.Height);

                Pen p = new Pen(GetColor(rnd), 1);
                g.DrawLine(p, x1, y1, x2, y2);
            }

            //歪曲
            bmp = TwistImage(bmp, true, 3, rnd.NextDouble() * Math.PI * 2);
            g = Graphics.FromImage(bmp);

            //噪點
            for (int i = 0; i < 100; i++)
            {
                int x1 = rnd.Next(bmp.Width);
                int y1 = rnd.Next(bmp.Height);

                Pen p = new Pen(GetColor(rnd), 1);
                g.DrawRectangle(p, x1, y1, 1, 1);
            }

            //邊框
            g.DrawRectangle(new Pen(new SolidBrush(Color.FromArgb(153, 153, 153))), new Rectangle(0, 0, width - 1, height - 1));

            return bmp;
        }
        #endregion

        #region 獲得隨機字符
        /// <summary>
        /// 獲得隨機字符
        /// </summary>
        private static string GetChar(Random rnd)
        {
            int n = rnd.Next(0, 61);
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
        #endregion

        #region 獲得隨機字體
        /// <summary>
        /// 獲得隨機字體
        /// </summary>
        private static Font GetFont(Random rnd)
        {
            return new Font(fonts[rnd.Next(0, fonts.Length)], fontSize, FontStyle.Bold);
        }
        #endregion

        #region 獲得隨機色彩
        /// <summary>
        /// 獲得隨機色彩
        /// </summary>
        private static Color GetColor(Random rnd)
        {
            return colors[rnd.Next(0, colors.Length)];
        }
        #endregion

        #region 正弦曲線Wave歪曲圖片
        /// <summary>  
        /// 正弦曲線Wave歪曲圖片（Edit By 51aspx.com）  
        /// </summary>  
        /// <param name="srcBmp">圖片途徑</param>  
        /// <param name="bXDir">假如歪曲則選擇為True</param>  
        /// <param name="nMultValue">波形的幅度倍數，越年夜歪曲的水平越高，普通為3</param>  
        /// <param name="dPhase">波形的肇端相位，取值區間[0-2*PI)</param>  
        private static Bitmap TwistImage(Bitmap srcBmp, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap destBmp = new Bitmap(srcBmp.Width, srcBmp.Height);

            // 將位圖配景填充為白色  
            Graphics graph = Graphics.FromImage(destBmp);
            graph.FillRectangle(new SolidBrush(Color.White), 0, 0, destBmp.Width, destBmp.Height);
            graph.Dispose();

            double dBaseAxisLen = bXDir ? (double)destBmp.Height : (double)destBmp.Width;

            for (int i = 0; i < destBmp.Width; i++)
            {
                for (int j = 0; j < destBmp.Height; j++)
                {
                    double dx = 0;
                    dx = bXDir ? (Math.PI * 2 * (double)j) / dBaseAxisLen : (Math.PI * 2 * (double)i) / dBaseAxisLen;
                    dx += dPhase;
                    double dy = Math.Sin(dx);

                    // 獲得以後點的色彩  
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

    }

    /// <summary>
    /// VryImgGen 的摘要說明
    /// </summary>
    public class VryImgGen
    {
        public static string ChineseChars = String.Empty;

        /// <summary>
        /// 英文與數字串
        /// </summary>
        protected static readonly string EnglishOrNumChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

        public VryImgGen()
        {
            rnd = new Random(unchecked((int)DateTime.Now.Ticks));
        }

        /// <summary>
        /// 全局隨機數生成器
        /// </summary>
        private Random rnd;

        int length = 5;
        /// <summary>
        /// 驗證碼長度(默認6個驗證碼的長度)
        /// </summary>
        public int Length
        {
            get { return length; }
            set { length = value; }
        }

        int fontSize = 20;
        /// <summary>
        /// 驗證碼字體大小(為了顯示扭曲效果，默認30像素，可以自行修改)
        /// </summary>
        public int FontSize
        {
            get { return fontSize; }
            set { fontSize = value; }
        }

        int padding = 4;
        /// <summary>
        /// 邊框補(默認4像素)
        /// </summary>
        public int Padding
        {
            get { return padding; }
            set { padding = value; }
        }

        bool chaos = true;
        /// <summary>
        /// 是否輸出燥點(默認輸出)
        /// </summary>
        public bool Chaos
        {
            get { return chaos; }
            set { chaos = value; }
        }

        Color chaosColor = Color.LightGray;
        /// <summary>
        /// 輸出燥點的顏色(默認灰色)
        /// </summary>
        public Color ChaosColor
        {
            get { return chaosColor; }
            set { chaosColor = value; }
        }

        int chaosWight = 1;
        /// <summary>
        /// 輸出燥點的濃度
        /// </summary>
        public int ChaosWight
        {
            get { return chaosWight; }
            set { chaosWight = value; }
        }

        Color backgroundColor = Color.White;
        /// <summary>
        /// 自定義背景色(默認白色)
        /// </summary>
        public Color BackgroundColor
        {
            get { return backgroundColor; }
            set { backgroundColor = value; }
        }

        Color[] colors = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
        /// <summary>
        /// 自定義隨機顏色數組
        /// </summary>
        public Color[] Colors
        {
            get { return colors; }
            set { colors = value; }
        }

        string[] fonts = { "Arial", "Georgia" };
        /// <summary>
        /// 自定義字體數組
        /// </summary>
        public string[] Fonts
        {
            get { return fonts; }
            set { fonts = value; }
        }

        #region 產生波形濾鏡效果

        private const double PI = 3.1415926535897932384626433832795;
        private const double PI2 = 6.283185307179586476925286766559;

        /// <summary>
        /// 正弦曲線Wave扭曲圖片（Edit By 51aspx.com）
        /// </summary>
        /// <param name="srcBmp">圖片路徑</param>
        /// <param name="bXDir">如果扭曲則選擇為True</param>
        /// <param name="nMultValue">波形的幅度倍數，越大扭曲的程度越高，一般為3</param>
        /// <param name="dPhase">波形的起始相位，取值區間[0-2*PI)</param>
        /// <returns></returns>
        public Bitmap TwistImage(Bitmap srcBmp, bool bXDir, double dMultValue, double dPhase)
        {
            Bitmap destBmp = new Bitmap(srcBmp.Width, srcBmp.Height);

            // 將位圖背景填充為白色
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

        /// <summary>
        /// 生成校驗碼圖片
        /// </summary>
        /// <param name="code">驗證碼</param>
        /// <returns></returns>
        public Bitmap CreateImage(string code)
        {
            int fSize = FontSize;
            int fWidth = fSize + Padding;

            int imageWidth = (int)(code.Length * fWidth) + 4 + Padding * 2;
            int imageHeight = fSize * 2 + Padding * 2;

            Bitmap image = new Bitmap(imageWidth - 10, imageHeight - 10);

            Graphics g = Graphics.FromImage(image);

            g.Clear(BackgroundColor);

            //給背景添加隨機生成的燥點
            if (this.Chaos)
            {

                Pen pen = new Pen(ChaosColor, 0);
                int c = ChaosWight * 10;

                for (int i = 0; i < c; i++)
                {
                    int x = rnd.Next(image.Width);
                    int y = rnd.Next(image.Height);

                    g.DrawRectangle(pen, x, y, 1, 1);
                }
            }

            int left = 0, top = 0, top1 = 1, top2 = 1;

            int n1 = (imageHeight - FontSize - Padding * 2);
            int n2 = n1 / 4;
            top1 = n2;
            top2 = n2 * 2;

            Font f;
            Brush b;

            int cindex, findex;

            //隨機字體和顏色的驗證碼字符
            for (int i = 0; i < code.Length; i++)
            {
                cindex = rnd.Next(Colors.Length - 1);
                findex = rnd.Next(Fonts.Length - 1);

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
            g.DrawRectangle(new Pen(Color.Gainsboro, 0), 0, 0, image.Width - 1, image.Height - 1);
            g.Dispose();

            //產生波形（Add By 51aspx.com）
            image = TwistImage(image, true, 8, 4);

            return image;
        }

        /// <summary>
        /// 生成隨機字符碼
        /// </summary>
        /// <param name="codeLen">字符串長度</param>
        /// <param name="zhCharsCount">中文字符數</param>
        /// <returns></returns>
        public string CreateVerifyCode(int codeLen, int zhCharsCount)
        {
            char[] chs = new char[codeLen];

            int index;
            for (int i = 0; i < zhCharsCount; i++)
            {
                index = rnd.Next(0, codeLen);
                if (chs[index] == '\0')
                    chs[index] = CreateZhChar();
                else
                    --i;
            }
            for (int i = 0; i < codeLen; i++)
            {
                if (chs[i] == '\0')
                    chs[i] = CreateEnOrNumChar();
            }

            return new string(chs, 0, chs.Length);
        }

        /// <summary>
        /// 生成默認長度5的隨機字符碼
        /// </summary>
        /// <returns></returns>
        public string CreateVerifyCode()
        {
            return CreateVerifyCode(Length, 0);
        }

        /// <summary>
        /// 生成英文或數字字符
        /// </summary>
        /// <returns></returns>
        protected char CreateEnOrNumChar()
        {
            return EnglishOrNumChars[rnd.Next(0, EnglishOrNumChars.Length)];
        }

        /// <summary>
        /// 生成漢字字符
        /// </summary>
        /// <returns></returns>
        protected char CreateZhChar()
        {
            //若提供了漢字集，查詢漢字集選取漢字
            if (ChineseChars.Length > 0)
            {
                return ChineseChars[rnd.Next(0, ChineseChars.Length)];
            }
            //若沒有提供漢字集，則根據《GB2312簡體中文編碼表》編碼規則構造漢字
            else
            {
                byte[] bytes = new byte[2];

                //第一個字節值在0xb0, 0xf7之間
                bytes[0] = (byte)rnd.Next(0xb0, 0xf8);
                //第二個字節值在0xa1, 0xfe之間
                bytes[1] = (byte)rnd.Next(0xa1, 0xff);

                //根據漢字編碼的字節數組解碼出中文漢字
                string str1 = Encoding.GetEncoding("gb2312").GetString(bytes);

                return str1[0];
            }
        }
    }
}

