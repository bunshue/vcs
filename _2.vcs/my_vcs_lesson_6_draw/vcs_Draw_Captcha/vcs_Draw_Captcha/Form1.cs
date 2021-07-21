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
            CreateImage();

            CodeImage(CheckCode(), pictureBox3);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            CreateImage();


            CodeImage(CheckCode(), pictureBox3);
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

    }
}
