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
            //int H = 250;

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
            draw_captcha4();
            draw_captcha5();
            draw_captcha6();
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


        //6種 Captcha ST

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

        void draw_captcha4()
        {
            string code;
            Bitmap bitmap1 = VerifyCodeHelper.CreateVerifyCodeBmp(out code);
            Bitmap bitmap2 = new Bitmap(bitmap1, 300, 200);  //改變大小

            richTextBox1.Text += code + "\n";
            pictureBox4.Image = bitmap1;
            //pictureBox4.Image = bitmap2;  //改變大小

            /*
            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            */
        }

        void draw_captcha5()
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

            pictureBox5.Image = bitmap1;
        }

        void draw_captcha6()
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
            pictureBox6.Image = bmp;
        }
        //6種 Captcha SP
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
}
