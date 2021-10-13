using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Printing;  //for PrintPageEventArgs

namespace 真的只是一個測試3_Draw
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 165;
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //字串旋轉列印
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("彩色轉灰階", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(20, 20));

            Font f = new Font("標楷體", 50);
            RotateDeawString(g, f, 35, "旋轉列印字串", 20, 20);
        }

        /// <summary>
        /// 旋轉列印字串
        /// </summary>
        /// <param name="e">PrintPageEventArgs</param>
        /// <param name="font">字型</param>
        /// <param name="degree">旋轉角度</param>
        /// <param name="msg">列印訊息</param>
        /// <param name="x">重設原點 X 位置</param>
        /// <param name="y">重設原點 Y 位置</param>
        private void RotateDeawString(Graphics g, Font font, int degree, string msg, int x, int y)
        {
            // 原點位置重設
            g.TranslateTransform(mmTo100InchX(x), mmTo100InchY(y));
            // 設定旋轉角度
            g.RotateTransform(degree);
            // 標題
            g.DrawString(msg, font, Brushes.Black, mmTo100InchX(0), mmTo100InchY(0));
            //繪圖畫布還原
            g.ResetTransform();
        }

        private int mmTo100InchX(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private int mmTo100InchY(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }


        private void button1_Click(object sender, EventArgs e)
        {
            string code;
            Bitmap bitmap1 = VerifyCodeHelper.CreateVerifyCodeBmp(out code);
            Bitmap bitmap2 = new Bitmap(bitmap1, 300, 200);  //改變大小

            richTextBox1.Text += code + "\n";
            pictureBox1.Image = bitmap1;
            //pictureBox1.Image = bitmap2;

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


            

        }

        private void button2_Click(object sender, EventArgs e)
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
            string[] font = {"Verdana","Microsoft Sans Serif","Comic Sans MS","Arial","宋體"};
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

            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
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
            pictureBox1.Image = bmp;

        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
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

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
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
}

