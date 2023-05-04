using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DirectoryInfo

namespace vcs_PictureSlideShow6
{
    public partial class Form1 : Form
    {
        private List<string> imageList;//播放的圖片

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            InitLoad();
        }

        void show_item_location()
        {
            richTextBox1.Size = new Size(300, 900);
            richTextBox1.Location = new Point(1610, 10);

            pictureBox1.Size = new Size(1500, 900);
            pictureBox1.Location = new Point(10, 10);
            pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_open_file_setup();
            bt_exit_setup();
        }

        private void bt_open_file_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";

                //filename = openFileDialog1.FileName;
                //reset_pictureBox();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        void bt_open_file_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_open_file = new Button();  // 實例化按鈕
            bt_open_file.Size = new Size(w, h);
            bt_open_file.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Blue, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, w / 4, 0, (w - 1) / 2, h - 1);
            g.DrawLine(p, (w - 1) * 3 / 4, 0, (w - 1) / 2, h - 1);
            bt_open_file.Image = bmp;

            bt_open_file.Location = new Point(this.ClientSize.Width - bt_open_file.Width, 0 + h);
            bt_open_file.Click += bt_open_file_Click;     // 加入按鈕事件

            this.Controls.Add(bt_open_file); // 將按鈕加入表單
            bt_open_file.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Name = "bt_exit";
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        /// <summary>
        ///  初始化 載入播放列表 如歌詞 背景圖 定時器等等
        /// </summary>
        private void InitLoad()
        {
            try
            {
                bool flag = false;
                //string folder = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "bgImages");
                //string folder = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "bgImages");
                string foldername = @"C:\______test_files1\__pic\_書畫字圖\_peony1";

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
                            this.pictureBox1.Image = Image.FromFile(fi[i].FullName);
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

        int index = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int len = imageList.Count;
            //richTextBox1.Text += "目前共有 " + len.ToString() + " 張圖片\n";

            this.pictureBox1.Image.Dispose();
            this.pictureBox1.Image = Image.FromFile(imageList[index]);
            //richTextBox1.Text += "index = " + index.ToString() + ", show : " + imageList[index] + "\n";

            if (index < (len - 1))
                index++;
            else
                index = 0;

        }
    }
}
