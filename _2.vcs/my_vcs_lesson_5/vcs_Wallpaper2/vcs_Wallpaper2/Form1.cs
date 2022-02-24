using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.IO;
using Microsoft.Win32;

namespace vcs_Wallpaper2
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files\__pic\";
        string filename;
        int sel_picture = -1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //任選一張圖
            DirectoryInfo DInfo = new DirectoryInfo(foldername);
            FileInfo[] FInfo = DInfo.GetFiles();
            Random rand = new Random();
            sel_picture = rand.Next(FInfo.Length);

            filename = foldername + FInfo[sel_picture].Name;
            richTextBox1.Text += "sel_picture = " + sel_picture.ToString() + "filename : " + filename + "\n";

            //讀取圖檔
            pictureBox1.Image = Image.FromFile(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //設定為桌布
            if (sel_picture == -1)
                return;

            RegistryKey myRKey = Registry.CurrentUser;
            myRKey = myRKey.OpenSubKey("Control Panel\\Desktop", true);
            myRKey.SetValue("WallPaper", filename);

            richTextBox1.Text += "filename : " + filename + "\n";
            myRKey.SetValue("TitleWallPaper", "2");
            myRKey.Close();

            richTextBox1.Text += "桌面桌布已經修改！\n";
        }
    }
}
