using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_PictureSlideShow4
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files\__pic\_MU";
        string strInfo = "";
        string[] strName = null;
        int Num = 0;
        int Count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = Color.Black;

            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
            this.ActiveControl = this.pictureBox1;//选中pictureBox1，不然没法触发事件

            DirectoryInfo dir = new DirectoryInfo(foldername);

            GetAllFiles(dir);
            if (strInfo != "")
            {
                strName = strInfo.Split('#');
                Num = 0;
                showPicture(Num);
                Count = strName.Length - 1;
            }
            else
            {
                MessageBox.Show("無圖片");
            }
        }

        void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if ((e.KeyCode == Keys.Escape) || (e.KeyCode == Keys.X))
            {
                Application.Exit();
            }
        }

        public void GetAllFiles(DirectoryInfo dir)
        {
            FileSystemInfo[] fileinfo = dir.GetFileSystemInfos();
            foreach (FileSystemInfo i in fileinfo)
            {
                if (i is DirectoryInfo)
                {
                    GetAllFiles((DirectoryInfo)i);
                }
                else
                {
                    string str = i.FullName;
                    int b = str.LastIndexOf("\\");
                    string strType = str.Substring(b + 1);
                    if (strType.Substring(strType.Length - 3) == "jpg" || strType.Substring(strType.Length - 3) == "bmp")
                    {
                        strInfo += strType + "#";
                    }
                }
            }
        }

        private void showPicture(int N)
        {
            //this.pictureBox1.ImageLocation = strPath + "\\" + strName[N];
            //richTextBox1.Text +=strPath + "\\" + strName[N]+"\n";

            //讀取圖檔, 多一層Image結構
            string filename = foldername + "\\" + strName[N];
            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;

            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;
            int w = image.Width;
            int h = image.Height;

            if ((w > W) || (h > H))
            {
                pictureBox1.Size = new Size(W, H);
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.Location = new Point(0, 0);


            }
            else
            {
                pictureBox1.Size = new Size(w, h);
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                pictureBox1.Location = new Point((W - w) / 2, (H - h) / 2);
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Num++;
            if (Num >= Count)
            {
                Num = 0;
            }
            showPicture(Num);
        }
    }
}

