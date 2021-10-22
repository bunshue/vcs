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
                Font f = new System.Drawing.Font(fonts[findex], 14, System.Drawing.FontStyle.Bold);//字體
                Brush b = new System.Drawing.SolidBrush(c[cindex]);//顏色
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
                        Font font = new Font("Arial", 16, (FontStyle.Bold | System.Drawing.FontStyle.Italic));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Red, 1.5f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 1)
                    {
                        Font font = new System.Drawing.Font("楷體", 16, (FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.DarkRed, 1.3f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 2)
                    {
                        Font font = new System.Drawing.Font("宋體", 16, (System.Drawing.FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, image.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Green, Color.Blue, 1.2f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 3)
                    {
                        Font font = new System.Drawing.Font("黑體", 16, (System.Drawing.FontStyle.Bold |

                        System.Drawing.FontStyle.Bold));
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
                image.Save(ms, System.Drawing.Imaging.ImageFormat.Jpeg);
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
    }
}
