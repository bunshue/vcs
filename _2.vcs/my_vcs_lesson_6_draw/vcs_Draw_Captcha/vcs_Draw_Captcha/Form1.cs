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

namespace vcs_Draw_Captcha
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

            CreateImage();

            CodeImage(CheckCode(), pictureBox3);
        }

        void show_item_location()
        {
            int W = 250;
            int H = 250;

            pictureBox_captcha1.Size = new Size(W + 50, 110);
            pictureBox_captcha2.Size = new Size(W + 50, 110);
            pictureBox_captcha3.Size = new Size(W + 50, 110);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 20;
            dx = 160;
            dy = 50;

            pictureBox_captcha1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox_captcha2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 120);
            pictureBox_captcha3.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 120 * 2);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            CreateImage();

            CodeImage(CheckCode(), pictureBox3);

            draw_captcha1();
            draw_captcha2();
            draw_captcha3();
        }

        //中文驗證法碼 ST
        public string txt = "";
        private void CreateImage()
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

            richTextBox1.Text += txt + "\n";

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
                pictureBox1.Image = image;
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

        //英數驗證碼 ST
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

        //英數驗證碼 SP


        //3種 Captcha ST

        void draw_captcha1()
        {
            string txt = "This is a lion-mouse";

            Bitmap bm = MakeCaptchaImge1(txt,
                50, 70,
                pictureBox_captcha1.ClientSize.Width,
                pictureBox_captcha1.ClientSize.Height);
            pictureBox_captcha1.Image = bm;
        }

        void draw_captcha2()
        {
            string txt = "This is a lion-mouse";

            using (Font the_font = new Font("Times New Roman", 30))
            {
                pictureBox_captcha2.Image = MakeCaptchaImage2(txt,
                    pictureBox_captcha2.ClientSize.Width,
                    pictureBox_captcha2.ClientSize.Height,
                    the_font, Brushes.Blue);
            }
        }

        //產生驗證圖片 ST
        void draw_captcha3()
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
            pictureBox_captcha3.Image = vaildNumImage;
        }
        //產生驗證圖片 SP

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

        //3種 Captcha SP




    }
}
