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
            InitLoad();
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
                string foldername = @"C:\______test_files\__pic\_peony1";

                DirectoryInfo root = new DirectoryInfo(foldername);
                FileInfo[] files = root.GetFiles();
                string fileName;
                for (int i = 0; i < files.Length; i++)
                {
                    fileName = files[i].Name.ToLower();
                    if (fileName.EndsWith(".png") || fileName.EndsWith(".jpeg") || fileName.EndsWith(".jpg"))
                    {
                        if (!flag)
                        {
                            imageList = new List<string>();
                            this.pictureBox1.Image = Image.FromFile(files[i].FullName);
                        }
                        imageList.Add(files[i].FullName);
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
