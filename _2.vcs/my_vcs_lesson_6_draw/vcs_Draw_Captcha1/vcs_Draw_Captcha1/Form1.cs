﻿using System;
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
using System.Drawing.Text;      //for TextRenderingHint
using System.Security.Cryptography; //for RNGCryptoServiceProvider

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
            timer1_Tick(sender, e);
        }

        void show_item_location()
        {
            int W = 280;
            int H = 90;

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
            pictureBox24.Size = new Size(W, H);
            pictureBox25.Size = new Size(W, H);
            pictureBox26.Size = new Size(W, H);
            pictureBox27.Size = new Size(W, H);
            pictureBox28.Size = new Size(W, H);
            pictureBox29.Size = new Size(W, H);
            pictureBox30.Size = new Size(W, H);
            pictureBox31.Size = new Size(W, H);

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

            pictureBox24.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox25.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox26.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox27.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            pictureBox28.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            pictureBox29.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            pictureBox30.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            pictureBox31.Location = new Point(x_st + dx * 3, y_st + dy * 7);

            richTextBox1.Size = new Size(W * 2 + 40, 790);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Location = new Point(100, 100);
            this.Size = new Size(1800, 850);
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
            draw_captcha09();   //for pictureBox09
            draw_captcha10();   //for pictureBox10
            draw_captcha11();   //for pictureBox11
            draw_captcha12();   //for pictureBox12
            draw_captcha13();   //for pictureBox13
            draw_captcha14();   //for pictureBox14
            draw_captcha15();   //for pictureBox15

            draw_captcha16();    //for pictureBox16
            draw_captcha17();    //for pictureBox17
            draw_captcha18();    //for pictureBox18
            draw_captcha19();    //for pictureBox19
            draw_captcha20();    //for pictureBox20
            draw_captcha21();    //for pictureBox21
            draw_captcha22();    //for pictureBox22
            draw_captcha23();    //for pictureBox23

            draw_captcha24();   //for pictureBox24
            draw_captcha25();   //for pictureBox25
            draw_captcha26();   //for pictureBox26
            draw_captcha27();   //for pictureBox27
            draw_captcha28();   //for pictureBox28
            draw_captcha29();   //for pictureBox29
            draw_captcha30();   //for pictureBox30
            draw_captcha31();   //for pictureBox31
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
        private void draw_captcha01()
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
            Random random = new Random(iSeed);
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
            Bitmap bitmap1 = new Bitmap(iImageWidth, 30);
            Graphics g = Graphics.FromImage(bitmap1);
            try
            {
                //生成隨機生成器
                Random random = new Random();
                //清空圖片背景色
                g.Clear(Color.White);

                //畫圖片的背景噪音點
                for (int i = 0; i < 20; i++)
                {
                    int x1 = random.Next(bitmap1.Width);
                    int x2 = random.Next(bitmap1.Width);
                    int y1 = random.Next(bitmap1.Height);
                    int y2 = random.Next(bitmap1.Height);
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }

                //畫圖片的背景噪音線
                for (int i = 0; i < 2; i++)
                {
                    int x1 = 0;
                    int x2 = bitmap1.Width;
                    int y1 = random.Next(bitmap1.Height);
                    int y2 = random.Next(bitmap1.Height);
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
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Red, 1.5f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 1)
                    {
                        Font font = new Font("楷體", 16, (FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.DarkRed, 1.3f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 2)
                    {
                        Font font = new Font("宋體", 16, (FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Green, Color.Blue, 1.2f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                    else if (iValue == 3)
                    {
                        Font font = new Font("黑體", 16, (FontStyle.Bold |

                        FontStyle.Bold));
                        Rectangle rc = new Rectangle(xLeft, 0, iWordWidth, bitmap1.Height);
                        LinearGradientBrush brush = new LinearGradientBrush(rc, Color.Blue, Color.Green, 1.8f, true);
                        g.DrawString(Code, font, brush, xLeft, 2);
                    }
                }
                ////畫圖片的前景噪音點 ---有無這段代碼 貌似沒啥變化
                for (int i = 0; i < 8; i++)
                {
                    int x = random.Next(bitmap1.Width);
                    int y = random.Next(bitmap1.Height);
                    bitmap1.SetPixel(x, y, Color.FromArgb(random.Next()));
                }
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);

                pictureBox01.Image = bitmap1;

                MemoryStream ms = new MemoryStream();
                bitmap1.Save(ms, ImageFormat.Jpeg);
                return ms.ToArray();
            }
            finally
            {
                g.Dispose();
                //bitmap1.Dispose();
            }
        }
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

            Bitmap bitmap1 = new Bitmap(ww, hh);
            Graphics g = Graphics.FromImage(bitmap1);

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
            pictureBox02.Image = bitmap1;
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

            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling((checkCode.Length * 20.0)), 50);
            Graphics g = Graphics.FromImage(bitmap1);

            try
            {
                //產生隨機產生器
                Random random = new Random();
                //清空圖片背景色
                g.Clear(Color.White);
                //畫圖片的背景噪音線
                for (int i = 0; i < 3; i++)
                {
                    int x1 = random.Next(bitmap1.Width);
                    int x2 = random.Next(bitmap1.Width);
                    int y1 = random.Next(bitmap1.Height);
                    int y2 = random.Next(bitmap1.Height);
                    g.DrawLine(new Pen(Color.Black), x1, y1, x2, y2);
                }
                Font font = new Font("Arial", 24, (FontStyle.Bold));
                g.DrawString(checkCode, font, new SolidBrush(Color.Red), 2, 2);

                //畫圖片的前景噪音點
                for (int i = 0; i < 150; i++)
                {
                    int x = random.Next(bitmap1.Width);
                    int y = random.Next(bitmap1.Height);

                    bitmap1.SetPixel(x, y, Color.FromArgb(random.Next()));
                }
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
                pbx.Width = bitmap1.Width;
                pbx.Height = bitmap1.Height;
                pbx.BackgroundImage = bitmap1;
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
        void draw_captcha05()
        {
            //pictureBox05
        }
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
            Bitmap bitmap1 = new Bitmap(120, 25);
            //創建GDI對象
            Graphics g = Graphics.FromImage(bitmap1);

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
                Point p1 = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                Point p2 = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                g.DrawLine(new Pen(Color.Green), p1, p2);
            }

            //畫像素顆粒
            for (int i = 0; i < 100; i++)
            {
                Point p = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                bitmap1.SetPixel(p.X, p.Y, Color.Black);
            }

            //把畫好的圖片放到PictureBox上
            pictureBox06.Image = bitmap1;
        }
        //Captcha 06 SP

        //Captcha 07 ST
        void draw_captcha07()
        {
            Random r = new Random();
            string str = string.Empty;
            //生成5位随机数如 90531
            for (int i = 0; i < 5; i++)
            {
                str += r.Next(0, 10);
            }
            Bitmap bitmap1 = new Bitmap(150, 40);
            Graphics g = Graphics.FromImage(bitmap1);
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
                Point p1 = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                Point p2 = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                g.DrawLine(new Pen(Brushes.Green), p1, p2);
            }
            //添加一些像素点
            for (int i = 0; i < 300; i++)
            {
                Point p1 = new Point(r.Next(0, bitmap1.Width), r.Next(0, bitmap1.Height));
                bitmap1.SetPixel(p1.X, p1.Y, Color.Green);
            }
            //在winForm中用PictureBox中显示出来
            pictureBox07.Image = bitmap1;
        }
        //Captcha 07 SP

        //Captcha 08 ST
        void draw_captcha08()
        {
            //pictureBox08
        }
        //Captcha 08 SP

        //Captcha 09 ST
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

        void draw_captcha09()
        {
            string strValidCode;
            // 產生5位隨機字元
            strValidCode = this.GetValidCode(5);
            //將字串儲存到Session中,以便需要時進行驗證                                                
            //context.Session["ValidCode"] = strValidCode;
            //定義寬120畫素,高30畫素的資料定義的影象物件                                          
            Bitmap bitmap1 = new Bitmap(120, 30);
            //繪製圖片                               
            Graphics g = Graphics.FromImage(bitmap1);
            try
            {
                //生成隨機物件
                Random random = new Random();
                //清除圖片背景色                                                   
                g.Clear(Color.White);
                // 隨機產生圖片的背景噪線                                                       
                for (int i = 0; i < 25; i++)
                {
                    int x1 = random.Next(bitmap1.Width);
                    int x2 = random.Next(bitmap1.Width);
                    int y1 = random.Next(bitmap1.Height);
                    int y2 = random.Next(bitmap1.Height);
                    g.DrawLine(new Pen(Color.Silver), x1, y1, x2, y2);
                }
                //設定圖片字型風格
                Font font = new Font("新宋體", 20, (FontStyle.Bold));
                //設定畫筆型別
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 3, true);
                //繪製隨機字元
                g.DrawString(strValidCode, font, brush, 5, 2);

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

        //Captcha 10 ST
        void draw_captcha10()
        {
            //pictureBox10
        }
        //Captcha 10 SP

        //Captcha 11 ST
        void draw_captcha11()
        {
            /*
            驗證碼字符個數、生成圖片寬度、高度自定均可由構造方法自定，無參構造生成默認字符個數和默認大小的Image,
            方法GetImgWithValidateCode()返回生成的驗證碼圖片，
            方法 IsRight(string inputValCode) 判斷用戶輸入的驗證碼 inputValCode與圖片顯示的字符是否一致，不區分大小寫
            */

            DrawValImg drawimg = new DrawValImg();
            Image img = drawimg.GetImgWithValidateCode();
            pictureBox11.Image = img;
        }
        //Captcha 11 SP

        //Captcha 12 ST
        void draw_captcha12()
        {
            // 創建一個包含隨機內容的驗證碼文本
            Random rand = new Random();
            int len = rand.Next(4, 6);
            char[] chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".ToCharArray();
            StringBuilder myStr = new StringBuilder();
            for (int iCount = 0; iCount < len; iCount++)
            {
                myStr.Append(chars[rand.Next(chars.Length)]);
            }
            string text = myStr.ToString();

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

                pictureBox12.Image = bitmap2;

                // 輸出圖片
                MemoryStream ms = new MemoryStream();
                bitmap2.Save(ms, ImageFormat.Jpeg);
                ms.Close();
            }//using
            myFont.Dispose();
        }
        //Captcha 12 SP

        //Captcha 13 ST
        void draw_captcha13()
        {
            //產生圖片驗證碼
            Bitmap bitmap1 = DrawCahpcha1(RandomGeneratorStyle.Number, 20);
            pictureBox13.Image = bitmap1;
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
        public static Bitmap DrawCahpcha1(RandomGeneratorStyle style, int length)
        {
            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling(length * 20.5), 50);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bitmap1);//利用該圖片對象生成“畫板”
            string strCode = GenerateRandomNumber(style, length);//生成隨機數
            Font font = new Font("Arial", 24, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(strCode, font, brush, 0, 0);//關鍵的一步，進行繪制。
            //bitmap1.Save("aaaa.jpg", ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源
            return bitmap1;
        }
        //Captcha 13 SP

        //Captcha 14 ST
        void draw_captcha14()
        {
            //產生圖片驗證碼(很複雜)

            //首先實例化驗證碼的類
            ValidateCode validateCode = new ValidateCode();
            //生成驗證碼指定的長度
            string code = validateCode.GetRandomString(4);
            //創建驗證碼的圖片
            Bitmap bitmap1 = validateCode.CreateImage(code);

            pictureBox14.Image = bitmap1;

            //最後將驗證碼返回
            //return File(bytes, @"image/jpeg");
            //File(bytes, @"image/jpeg");
        }
        //Captcha 14 SP

        //Captcha 15 ST
        void draw_captcha15()
        {
            //調用函數將驗證碼生成圖片
            CreateCheckCodeImage2(GenerateCheckCode());
        }

        private string GenerateCheckCode()
        {  //產生五位的隨機字符串
            int number;
            char code;
            string checkCode = String.Empty;

            Random random = new Random();

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

        //Captcha 16 ST
        void draw_captcha16()
        {
            //pictureBox16
        }
        //Captcha 16 SP

        //Captcha 17 ST
        void draw_captcha17()
        {
            //使用驗證碼類
            Captcha capt = new Captcha();
            Bitmap bitmap1 = capt.GetImage();
            pictureBox17.Image = bitmap1;
        }

        //Captcha 18 ST
        void draw_captcha18()
        {
            //產生圖片驗證碼
            Bitmap bitmap1 = DrawCahpcha2(RandomGeneratorStyle.NumberAndChar, 20);
            pictureBox18.Image = bitmap1;
        }

        /* same
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
        */

        public static string Generate2(RandomGeneratorStyle style, int length)
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
        public static Bitmap DrawCahpcha2(RandomGeneratorStyle style, int length)
        {
            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling(length * 12.5), 20);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bitmap1);//利用該圖片對象生成“畫板”
            string strCode = Generate2(style, length);//生成隨機數
            Font font = new Font("Arial", 12, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(strCode, font, brush, 0, 0);//關鍵的一步，進行繪制。
            //bitmap1.Save("aaaa.jpg", ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源
            return bitmap1;
        }
        //Captcha 18 SP

        //Captcha 19 ST
        void draw_captcha19()
        {
            //pictureBox19
        }
        //Captcha 19 SP

        //Captcha 20 ST
        void draw_captcha20()
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
            Bitmap bitmap1 = new Bitmap(100, 25);
            Graphics g = null;
            MemoryStream ms = null;
            Random random = new Random();
            //驗證碼顏色集合
            Color[] c = { Color.Black, Color.Red, Color.DarkBlue, Color.Green, Color.Orange, Color.Brown, Color.DarkCyan, Color.Purple };
            //驗證碼字體集合
            string[] fonts = { "Verdana", "Microsoft Sans Serif", "Comic Sans MS", "Arial", "宋體" };

            g = Graphics.FromImage(bitmap1);//從bitmap1對象生成新的Graphics對象 

            g.Clear(Color.White);//背景設為白色

            //在隨機位置畫背景點
            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(bitmap1.Width);
                int y = random.Next(bitmap1.Height);
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
            bitmap1.Save(ms, ImageFormat.Jpeg);//將此圖像以jpg圖像文件的格式保存到流中

            //回收資源
            g.Dispose();

            pictureBox20.Image = bitmap1;
            //bitmap1.Dispose();
            return ms;
        }
        //Captcha 20 SP

        //Captcha 21 ST
        private void ValidateCode(string VNum)
        {
            Bitmap bitmap1 = null;
            Graphics g = null;
            MemoryStream ms = null;
            int gheight = VNum.Length * 12;
            bitmap1 = new Bitmap(gheight, 25);
            g = Graphics.FromImage(bitmap1);
            //生成隨機生成器
            Random random = new Random();
            //背景顏色
            g.Clear(Color.White);
            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(bitmap1.Width);
                int y = random.Next(bitmap1.Height);
                bitmap1.SetPixel(x, y, Color.FromArgb(random.Next()));
            }
            //文字字體
            Font f = new Font("Arial Black ", 12);
            //文字顏色
            SolidBrush s = new SolidBrush(Color.Blue);
            g.DrawString(VNum, f, s, 3, 3);
            ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);
            g.Dispose();
            pictureBox21.Image = bitmap1;
            //bitmap1.Dispose();
        }

        void draw_captcha21()
        {
            string tmp = RndNum(4);
            //HttpCookie a = new HttpCookie("ImageV ", tmp);
            //Response.Cookies.Add(a);
            this.ValidateCode(tmp);
        }
        //Captcha 21 SP

        //Captcha 22 ST
        void draw_captcha22()
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
            pictureBox22.Image = bitmap1;
            //bitmap1.Dispose();
        }
        //Captcha 22 SP

        //Captcha 23 ST

        /// <summary>
        /// 字符
        /// </summary>
        /// <param name="len">幾位</param>
        /// <returns></returns>
        public static string validation(int cd)
        {
            var ran = new Random();
            int num, tem;
            string rtuStr = "";
            for (int i = 0; i < cd; i++)
            {
                num = ran.Next();
                if (i % 2 == 1)
                    tem = num % 10 + '0'; //數字
                else
                    tem = num % 26 + 'A'; //字母
                rtuStr += Convert.ToChar(tem).ToString();
            }
            return rtuStr;
        }

        /// <summary>
        /// 生成圖像
        /// </summary>
        /// <param name="check">字符</param>
        public Bitmap drawImg(string check)
        {
            Bitmap bitmap1 = new Bitmap(220, 34);
            var ht = Graphics.FromImage(bitmap1);
            ht.Clear(Color.White);
            ht.DrawLine(new Pen(Color.SpringGreen), 1, 1, 90, 34);
            Font font = new Font("微軟雅黑", 20, FontStyle.Bold);
            var jianbian = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Teal, Color.Snow, 2f, true);
            ht.DrawString(check, font, jianbian, 0, 0);
            ht.DrawRectangle(new Pen(Color.Aqua), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            ht.Dispose();
            return bitmap1;
        }

        void draw_captcha23()
        {
            int digits = 10;
            string captcha = validation(digits);
            pictureBox23.Image = drawImg(captcha);
        }

        //Captcha 23 SP

        //Captcha 24 ST
        //中文驗證法碼 ST
        public string txt = "";
        private void draw_captcha24()
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

            Bitmap bitmap1 = new Bitmap((int)Math.Ceiling((txt.Length * 20.5)) * 3, 22 * 3);
            Graphics g = Graphics.FromImage(bitmap1);
            try
            {
                //生成随机生成器
                Random random = new Random();
                //清空图片背景色
                g.Clear(Color.White);
                //画图片的背景噪音线
                for (int i = 0; i < 2; i++)
                {
                    Point tem_Point_1 = new Point(random.Next(bitmap1.Width), random.Next(bitmap1.Height));
                    Point tem_Point_2 = new Point(random.Next(bitmap1.Width), random.Next(bitmap1.Height));
                    g.DrawLine(new Pen(Color.Black), tem_Point_1, tem_Point_2);
                }
                Font font = new Font("標楷體", 12 * 2, (FontStyle.Bold));
                LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, bitmap1.Width, bitmap1.Height), Color.Blue, Color.DarkRed, 1.2f, true);
                g.DrawString(txt, font, brush, 2, 2);
                //画图片的前景噪音点
                for (int i = 0; i < 100; i++)
                {
                    Point tem_point = new Point(random.Next(bitmap1.Width), random.Next(bitmap1.Height));
                    bitmap1.SetPixel(tem_point.X, tem_point.Y, Color.FromArgb(random.Next()));
                }
                //画图片的边框线
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
                pictureBox24.Image = bitmap1;
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
        //Captcha 24 SP

        //Captcha 25 ST

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
            Bitmap bitmap1 = new Bitmap(nBmpWidth, nBmpHeight);

            // 1. 生成隨機背景顏色
            int nRed, nGreen, nBlue;  // 背景的三元色
            Random rd = new Random((int)DateTime.Now.Ticks);
            nRed = rd.Next(255) % 128 + 128;
            nGreen = rd.Next(255) % 128 + 128;
            nBlue = rd.Next(255) % 128 + 128;

            // 2. 填充位圖背景
            Graphics graph = Graphics.FromImage(bitmap1);
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
            MemoryStream ms = new MemoryStream();
            bitmap1.Save(ms, ImageFormat.Jpeg);
            //bitmap1.Dispose();
            pictureBox25.Image = bitmap1;
            graph.Dispose();

            strKey = strResult;
            byte[] byteReturn = ms.ToArray();
            ms.Close();

            return byteReturn;
        }

        void draw_captcha25()
        {
            string strKey = "";
            int _nlen = 6;
            byte[] data = this.GenerateVerifyImage(_nlen, ref strKey); //_nLen生成驗證碼的長度
            //Session["Jcode"] = strKey; //用來保存驗證碼的值
            //Page.Response.OutputStream.Write(data, 0, data.Length);
        }
        //Captcha 25 SP

        //Captcha 26 ST
        void draw_captcha26()
        {
        }
        //Captcha 26 SP

        //Captcha 27 ST
        void draw_captcha27()
        {
        }
        //Captcha 27 SP

        //Captcha 28 ST
        void draw_captcha28()
        {
        }
        //Captcha 28 SP

        //Captcha 29 ST
        void draw_captcha29()
        {
            Bitmap bitmap1 = MakeCaptchaImge1(captcha_text,
                50, //最小
                70, //最大
                pictureBox29.ClientSize.Width,
                pictureBox29.ClientSize.Height);
            pictureBox29.Image = bitmap1;
        }
        //Captcha 29 SP

        //Captcha 30 ST
        void draw_captcha30()
        {
            using (Font the_font = new Font("Times New Roman", 30))
            {
                pictureBox30.Image = MakeCaptchaImage2(captcha_text,
                    pictureBox30.ClientSize.Width,
                    pictureBox30.ClientSize.Height,
                    the_font, Brushes.Blue);
            }
        }

        private Random Rand = new Random();

        // Make a captcha image for the text.
        private Bitmap MakeCaptchaImge1(string txt, int min_size, int max_size, int W, int H)
        {
            // Make the bitmap and associated Graphics object.
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.SmoothingMode = SmoothingMode.HighQuality;
                g.Clear(Color.White);

                // See how much room is available for each character.
                int ch_wid = (int)(W / txt.Length);

                // Draw each character.
                for (int i = 0; i < txt.Length; i++)
                {
                    float font_size = Rand.Next(min_size, max_size);
                    using (Font the_font = new Font("Times New Roman", font_size, FontStyle.Bold))
                    {
                        DrawCharacter1(txt.Substring(i, 1), g, the_font, i * ch_wid, ch_wid, W, H);
                    }
                }
            }
            return bitmap1;
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
        private Bitmap MakeCaptchaImage2(string txt, int W, int H, Font the_font, Brush the_brush)
        {
            Bitmap bitmap1 = new Bitmap(W, H);
            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;

                int x = 0;
                foreach (char ch in txt.ToCharArray())
                {
                    SizeF ch_size = g.MeasureString(ch.ToString(), the_font);
                    int y = (int)(Rand.NextDouble() * (H - ch_size.Height));
                    g.DrawString(ch.ToString(), the_font, the_brush, x, y);
                    x += (int)(ch_size.Width * 0.35);
                }
            }
            return bitmap1;
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

            pictureBox31.Image = bitmap1;
        }

        //Captcha 30 SP

        //Captcha 31 ST
        void draw_captcha31()
        {
            CreateImage(captcha_text);
        }
        //Captcha 31 SP
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
            Bitmap bitmap1 = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bitmap1);
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
                int x1 = rnd.Next(bitmap1.Width);
                int x2 = rnd.Next(bitmap1.Width);
                int y1 = rnd.Next(bitmap1.Height);
                int y2 = rnd.Next(bitmap1.Height);

                Pen p = new Pen(GetColor(rnd), 1);
                g.DrawLine(p, x1, y1, x2, y2);
            }

            //歪曲
            bitmap1 = TwistImage(bitmap1, true, 3, rnd.NextDouble() * Math.PI * 2);
            g = Graphics.FromImage(bitmap1);

            //噪點
            for (int i = 0; i < 100; i++)
            {
                int x1 = rnd.Next(bitmap1.Width);
                int y1 = rnd.Next(bitmap1.Height);

                Pen p = new Pen(GetColor(rnd), 1);
                g.DrawRectangle(p, x1, y1, 1, 1);
            }

            //邊框
            g.DrawRectangle(new Pen(new SolidBrush(Color.FromArgb(153, 153, 153))), new Rectangle(0, 0, width - 1, height - 1));

            return bitmap1;
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
                    int x = rnd.Next(bitmap1.Width);
                    int y = rnd.Next(bitmap1.Height);

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
            g.DrawRectangle(new Pen(Color.Gainsboro, 0), 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            g.Dispose();

            //產生波形（Add By 51aspx.com）
            bitmap1 = TwistImage(bitmap1, true, 8, 4);

            return bitmap1;
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
            Bitmap bitmap1 = null;
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
            bitmap1 = new Bitmap(width + FontSize, height);
            //根據上面創建的位圖對象創建繪圖圖面
            gph = Graphics.FromImage(bitmap1);
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
            bitmap1 = TwistImage(bitmap1, true, random.Next(3, 5), random.Next(3));
            try
            {
                bitmap1.Save(memStream, ImageFormat.Gif);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            //gph.Dispose();
            bitmap1.Dispose();
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
                MessageBox.Show("可控制顏色參數大於200，顏色默認位黑色");
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
        #endregion

        #region 畫正弦曲線
        private Bitmap DrawTwist(Bitmap bitmap0, Int32 tWidth, Int32 tHeight, float angle, Color color)
        {
            //爲了方便查看效果，在這裏我定義了一個常量。
            //它在定義數組的長度和for循環中都要用到。
            int size = bgWidth;

            double[] x = new double[size];
            Bitmap bitmap1 = new Bitmap(bitmap0.Width, bitmap0.Height);
            bitmap1.MakeTransparent();
            Graphics graphics = Graphics.FromImage(bitmap1);
            Pen p = new Pen(color);

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

                graphics.DrawLine(p, i * val, temp, i * val + val / 2, (float)x[i]);
                temp = (float)x[i];
            }
            graphics.RotateTransform(60, MatrixOrder.Prepend);

            //旋轉圖片
            // bitmap1 = KiRotate(b, angle, Color.Transparent);
            return bitmap1;
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
        #endregion

        #region 圖片任意角度旋轉
        /// <summary>
        /// 圖片任意角度旋轉
        /// </summary>
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

            GraphicsPath path = new GraphicsPath();
            path.AddRectangle(new RectangleF(0f, 0f, w, h));
            Matrix mtrx = new Matrix();
            mtrx.Rotate(angle);
            RectangleF rct = path.GetBounds(mtrx);

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
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Transparent);
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;

            GraphicsPath gPath1 = new GraphicsPath();
            Int32 lineRandNum = random.Next(lineNum);

            for (int i = 0; i < (lineNum - lineRandNum); i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                        new Point(random.Next(1, (bitmap1.Width / 10)), random.Next(1, (bitmap1.Height))),
                                        new Point(random.Next((bitmap1.Width / 10) * 2, (bitmap1.Width / 10) * 4), random.Next(1, (bitmap1.Height))),
                                        new Point(random.Next((bitmap1.Width / 10) * 4, (bitmap1.Width / 10) * 6), random.Next(1, (bitmap1.Height))),
                                        new Point(random.Next((bitmap1.Width / 10) * 8, bitmap1.Width), random.Next(1, (bitmap1.Height)))
                                    };

                gPath1.AddBeziers(point);
                g.DrawPath(p, gPath1);
                p.Dispose();
            }
            for (int i = 0; i < lineRandNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point[] point = {
                                new Point(random.Next(1, bitmap1.Width), random.Next(1, bitmap1.Height)),
                                new Point(random.Next((bitmap1.Width / 10) * 2, bitmap1.Width), random.Next(1, bitmap1.Height)),
                                new Point(random.Next((bitmap1.Width / 10) * 4, bitmap1.Width), random.Next(1, bitmap1.Height)),
                                new Point(random.Next(1, bitmap1.Width), random.Next(1, bitmap1.Height))
                                    };
                gPath1.AddBeziers(point);
                g.DrawPath(p, gPath1);
                p.Dispose();
            }
            return bitmap1;
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
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Transparent);
            g.PixelOffsetMode = PixelOffsetMode.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            for (int i = 0; i < lineNum; i++)
            {
                Pen p = new Pen(GetRandomDeepColor());
                Point pt1 = new Point(random.Next(1, (bitmap1.Width / 5) * 2), random.Next(bitmap1.Height));
                Point pt2 = new Point(random.Next((bitmap1.Width / 5) * 3, bitmap1.Width), random.Next(bitmap1.Height));
                g.DrawLine(p, pt1, pt2);
                p.Dispose();
            }

            return bitmap1;
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
            Bitmap bitmap1 = new Bitmap(bgWidth, bgHeight);
            bitmap1.MakeTransparent();
            Graphics graph = Graphics.FromImage(bitmap1);
            graph.SmoothingMode = SmoothingMode.HighQuality;
            graph.InterpolationMode = InterpolationMode.HighQualityBilinear;

            //畫噪點 
            for (int i = 0; i < (bgHeight * bgWidth) / pixNum; i++)
            {
                int x = random.Next(bitmap1.Width);
                int y = random.Next(bitmap1.Height);
                bitmap1.SetPixel(x, y, GetRandomDeepColor());
                //下移座標重新畫點
                if ((x + 1) < bitmap1.Width && (y + 1) < bitmap1.Height)
                {
                    //畫圖片的前景噪音點
                    graph.DrawRectangle(new Pen(Color.Silver), random.Next(bitmap1.Width), random.Next(bitmap1.Height), 1, 1);
                }
            }
            return bitmap1;
        }
        #endregion

        #region 畫隨機字符串中間連線
        /// <summary>
        /// 畫隨機字符串中間連線
        /// </summary>
        /// <returns></returns>
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
        #endregion

        #region 寫入驗證碼的字符串
        /// <summary>
        /// 寫入驗證碼的字符串
        /// </summary>
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
            return bitmap1;
        }
        #endregion

        #region 畫干擾背景文字
        /// <summary>
        /// 畫背景干擾文字
        /// </summary>
        /// <returns></returns>
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

            return bitmap1;
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
        #endregion

        #region 生成不重複的隨機數，該函數會消耗大量系統資源
        /// <summary>
        /// 生成不重複的隨機數，該函數會消耗大量系統資源
        /// </summary>
        /// <returns></returns>
        private static int GetRandomSeed()
        {
            byte[] bytes = new byte[4];
            RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();
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
        #endregion

        #region 濾鏡
        /// <summary>
        /// 紅色濾鏡
        /// </summary>
        /// <param name="bitmap">Bitmap</param>
        /// <param name="threshold">閥值 -255~255</param>
        /// <returns></returns>
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

        /// <summary>
        /// 綠色濾鏡
        /// </summary>
        /// <param name="bitmap">一個圖片實例</param>
        /// <param name="threshold">閥值 -255~+255</param>
        /// <returns></returns>
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
            Bitmap bitmap1 = new Bitmap(original.Width, original.Height);

            //get a graphics object from the new image
            Graphics g = Graphics.FromImage(bitmap1);
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
            g.DrawImage(original, new Rectangle(0, 0, original.Width, original.Height), 0, 0, original.Width, original.Height, GraphicsUnit.Pixel, attributes);

            //dispose the Graphics object
            g.Dispose();
            return bitmap1;
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

    //高斯模糊算法
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
}

