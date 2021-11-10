using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Xml;
using System.Net;
using System.Text.RegularExpressions;
using System.Management;
using System.Runtime.InteropServices;
using Shell32;

using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

using vcs_MyClassLibrary;

namespace test7
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
            x_st = 10;
            y_st = 10;
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

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 70);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //連接符 與 佔位符
            string str1 = "lion";
            string str2 = "mouse";
            string m = String.Format("{0}", str1);   //字符串格式輸出
            string n = String.Format("{0}", str2);


            richTextBox1.Text += "str = " + m + "-" + n + "\n";     //用“+”連接符



        }


        private void button1_Click(object sender, EventArgs e)
        {
            //動態創建按鈕和事件

            int i = 0;
            for (i = 0; i < 10; i++)
            {
                Button btn = new Button();//創建一個新的按鈕
                btn.Name = "button" + i.ToString();//這是我用來區別各個按鈕的辦法
                btn.Text = "button" + i.ToString();
                btn.Size = new Size(80, 45);
                Point p = new Point(400, 13 + i * 50);//創建一個坐標,用來給新的按鈕定位
                btn.Location = p;//把按鈕的位置與剛創建的坐標綁定在一起

                this.richTextBox1.Controls.Add(btn);    //向 某控件 中添加此按鈕

                //動態添加控件的事件,語句:
                //Control.Command += new CommandEventHandler(this.EventFun);
                btn.Click += new System.EventHandler(btn_click);//將按鈕的方法綁定到按鈕的單擊事件中b.Click是按鈕的單擊事件
            }
        }

        private void btn_click(object sender, System.EventArgs e)
        {
            Button b1 = (Button)sender;//將觸發此事件的對象轉換為該Button對象

            richTextBox1.Text += "你按了 " + b1.Name + "\n";
        }


        public List<string> Log = new List<string>();

        int i = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            i++;
            AddLog("add log " + i.ToString());

        }

        private void AddLog(string logtext)
        {
            if (Log.Count < 1000)
                Log.Add(System.DateTime.Now.ToString() + "\t" + logtext);
            else if (Log.Count == 1000)
                Log.Add(System.DateTime.Now.ToString() + " 達到日志上限,不再追加");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int len = Log.Count;
            if (len <= 0)
            {
                richTextBox1.Text += "無資料\n";
            }
            else
            {
                richTextBox1.Text += "共有 " + Log.Count.ToString() + " 筆資料, 分別是:\n";
                int i;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += Log[i] + "\n";
                }
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            string url = @"http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190339.html";
            string result = GetHtmlData(url);
            richTextBox1.Text += result + "\n";

        }

        public string GetHtmlData(string url)
        {
            try
            {
                HttpWebRequest request;
                request = (HttpWebRequest)WebRequest.Create(url);
                request.Method = "GET";
                HttpWebResponse response;
                response = (HttpWebResponse)request.GetResponse();
                Stream s;
                s = response.GetResponseStream();
                string StrDate = "";
                string strValue = "";
                StreamReader Reader = new StreamReader(s, Encoding.UTF8);
                while ((StrDate = Reader.ReadLine()) != null)
                {
                    strValue += StrDate + "\r\n";
                }
                return strValue;
            }
            catch (Exception)
            {
            }
            return "";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //為圖片生成縮略圖
            //讀取圖檔, 多一層Image結構
            string filename = @"C:\______test_files\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image2 = GetThumbnail(image, image.Width / 2, image.Height / 2);

            pictureBox1.Image = image2;
        }

        /// 為圖片生成縮略圖
        /// 原圖片的路徑
        /// 縮略圖寬
        /// 縮略圖高
        /// 
        public Image GetThumbnail(Image image, int width, int height)
        {
            Bitmap bmp = new Bitmap(width, height);
            //從Bitmap創建一個Graphics
            Graphics gr = Graphics.FromImage(bmp);
            //設置 
            gr.SmoothingMode = SmoothingMode.HighQuality;
            //下面這個也設成高質量
            gr.CompositingQuality = CompositingQuality.HighQuality;
            //下面這個設成High
            gr.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //把原始圖像繪制成上面所設置寬高的縮小圖
            Rectangle rectDestination = new Rectangle(0, 0, width, height);

            gr.DrawImage(image, rectDestination, 0, 0, image.Width, image.Height, GraphicsUnit.Pixel);
            return bmp;
        }


        private void button6_Click(object sender, EventArgs e)
        {
            //用GDI+繪制驗證碼

            DrawCahpcha(RandomGeneratorStyle.NumberAndChar, 20);

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

        public static string Generate(RandomGeneratorStyle style, int length)
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
        public void DrawCahpcha(RandomGeneratorStyle style, int length)
        {
            Bitmap bmp = new Bitmap((int)Math.Ceiling(length * 12.5), 20);//新建一個圖 片對象
            Graphics g = Graphics.FromImage(bmp);//利用該圖片對象生成“畫板”
            string strCode = Generate(style, length);//生成隨機數
            Font font = new Font("Arial", 12, FontStyle.Bold | FontStyle.Italic);//設 置字體顏色
            SolidBrush brush = new SolidBrush(Color.Red);//新建一個畫刷,到這裡為止,我們 已經准備好了畫板、畫刷、和數據
            g.DrawString(strCode, font, brush, 0, 0);//關鍵的一步，進行繪制。
            //bmp.Save(curPage.Response.OutputStream, ImageFormat.Jpeg);//保存為輸出流，否則頁 面上顯示不出來
            //g.Dispose();//釋放掉該資源

            pictureBox1.Image = bmp;
        }


        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //新增資料夾
            string path = Application.StartupPath;
            string folder = textBox1.Text;
            NewFolder(folder, path);


        }

        /// <summary>
        /// 新建文件夾
        /// </summary>
        /// <param name="filename">文件夾名</param>
        /// <param name="path">文件夾路徑</param>
        public static void NewFolder(string foldername, string path)
        {
            foldername.Trim();
            //如果輸入信息為空，提示
            if (foldername == "")
            {
                MessageBox.Show("目錄名不能為空");
                return;
            }
            else
            {
                string FullName = path + "\\" + foldername;
                //如果該文件以及存在
                if (Directory.Exists(FullName))
                {
                    MessageBox.Show("該目錄已經存在，請重命名");
                    return;
                }
                else
                {
                    //新建文件夾
                    Directory.CreateDirectory(FullName);
                    MessageBox.Show("新建文件夾 完成");
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //新增文件
            string path = Application.StartupPath;
            string filename = textBox2.Text;
            NewFile(filename, path);

        }

        /// <summary>
        /// 新建文件
        /// </summary>
        /// <param name="filename">文件名</param>
        /// <param name="path">文件路徑</param>
        public static void NewFile(string filename, string path)
        {
            filename.Trim();
            if (filename == "")
            {
                MessageBox.Show("文件名不能為空~！");
            }
            else
            {
                if (File.Exists(path + "\\" + filename + ".txt"))
                {
                    MessageBox.Show("該文件名已經存在，請重命名");
                }
                else
                {
                    string FullName = path + "\\" + filename + ".txt";　　 //獲得文件完整信息
                    StreamWriter Sw = File.CreateText(FullName);
                    MessageBox.Show("新建文件 完成");
                }
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "字串 轉 拜列\n";

            string str = "this is a lion-mouse.";

            richTextBox1.Text += "字串 : " + str + "\n";

            byte[] byte_array = Encoding.ASCII.GetBytes(str);

            int len = byte_array.Length;
            richTextBox1.Text += "拜列長度 : " + len.ToString() + "\n";
            richTextBox1.Text += "拜列內容 :\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byte_array[i] + "\t" + byte_array[i].ToString("X2") + "\n";

            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string str = "this-is-a-lion-mouse";
            string[] word = str.Split('-');
            richTextBox1.Text += "原字串: " + str + "\n";
            richTextBox1.Text += "分割後, len = " + word.Length.ToString() + ", 內容:\n";
            foreach (string s in word)
            {
                richTextBox1.Text += s + "\n";
            }


        }

        private void button12_Click(object sender, EventArgs e)
        {
            //做一個跟字串一樣大的圖檔
            string str = "做一個跟字串一樣大的圖檔";
            Bitmap newBitmap = null;
            Graphics g = null;

            try
            {
                Font fontCounter = new Font("Lucida Sans Unicode", 50);

                // calculate size of the string.
                newBitmap = new Bitmap(1, 1, PixelFormat.Format32bppPArgb);
                g = Graphics.FromImage(newBitmap);
                SizeF stringSize = g.MeasureString(str, fontCounter);
                int nWidth = (int)stringSize.Width;
                int nHeight = (int)stringSize.Height;
                g.Dispose();
                newBitmap.Dispose();

                newBitmap = new Bitmap(nWidth, nHeight, PixelFormat.Format32bppPArgb);
                g = Graphics.FromImage(newBitmap);
                g.FillRectangle(new SolidBrush(Color.Pink),
                new Rectangle(0, 0, nWidth, nHeight));

                g.DrawString(str, fontCounter, new SolidBrush(Color.Black), 0, 0);

                newBitmap.Save("test.png", ImageFormat.Png);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            finally
            {
                if (null != g) g.Dispose();
                if (null != newBitmap) newBitmap.Dispose();
            }



        }

        private void button13_Click(object sender, EventArgs e)
        {
            //使用MyClassLibrary範例
            MyClass.show();
            MyClass.show("ims");

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}

