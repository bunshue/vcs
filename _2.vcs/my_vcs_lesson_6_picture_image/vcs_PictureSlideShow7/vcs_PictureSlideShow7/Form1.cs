using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo

namespace vcs_PictureSlideShow7
{
    public partial class Form1 : Form
    {
        private List<string> imageList;//播放的圖片

        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            InitLoad();

            int W = 1920;
            int H = 1080;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);
            //this.BackgroundImage = bitmap1;
            //this.pictureBox1.Image = bitmap1;

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.Black);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
        }

        /// <summary>
        ///  初始化 載入播放列表 如歌詞 背景圖 定時器等等
        /// </summary>
        private void InitLoad()
        {
            try
            {
                bool flag = false;
                string foldername = @"C:\______test_files\__pic\_書畫字圖\_peony1";

                DirectoryInfo di = new DirectoryInfo(foldername);
                FileInfo[] fi = di.GetFiles();
                string fileName;
                for (int i = 0; i < fi.Length; i++)
                {
                    fileName = fi[i].Name.ToLower();
                    if (fileName.EndsWith(".png") || fileName.EndsWith(".jpeg") || fileName.EndsWith(".jpg"))
                    {
                        if (!flag)
                        {
                            imageList = new List<string>();
                            //this.pictureBox1.Image = Image.FromFile(fi[i].FullName);
                        }
                        imageList.Add(fi[i].FullName);
                        flag = true;
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("錯誤:" + ex.Message);
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.X)
            {
                Application.Exit();
            }
        }

        int index = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //richTextBox1.Text += "(" + index.ToString() + "/" + imageList.Count.ToString() + ") ";
            int len = imageList.Count;
            //richTextBox1.Text += "目前共有 " + len.ToString() + " 張圖片\n";

            Random r = new Random();
            index = r.Next(len);

            Image image = Image.FromFile(imageList[index]); // 產生一個Image物件
            int w = image.Width;
            int h = image.Height;

            //w = w * 3 / 2;
            //h = h * 3 / 2;

            int i;
            for (i = 1; i <= 10; i++)
            {
                if ((w / i < 1920 * 7 / 10) && (h / i < 1080 * 7 / 10))
                {
                    break;

                }

            }
            w = w / i;
            h = h / i;
            //Random r = new Random();
            //w += r.Next(100);
            //h += r.Next(100);

            int x = (1920 - w) / 2 + r.Next(-200, 200);
            int y = (1080 - h) / 2 + r.Next(-200, 200);
            g.DrawImage(image, x, y, w, h);
            g.DrawRectangle(new Pen(Color.White, 10), x, y, w, h);

            //g.DrawImage(image, 10, 50, image.Width, image.Height);

            this.BackgroundImage = bitmap1;
            this.Invalidate();

            if (index < (len - 1))
                index++;
            else
                index = 0;
        }
    }
}
