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

namespace Wallpaper
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\______test_files\_pic\";

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            //string strPath = Application.StartupPath.Substring(0, Application.StartupPath.Substring(0,Application.StartupPath.LastIndexOf("\\")).LastIndexOf("\\")) + @"\Image\";
            DirectoryInfo DInfo = new DirectoryInfo(foldername);
            FileInfo[] FInfo = DInfo.GetFiles();
            Random rand = new Random();
            int i = rand.Next(FInfo.Length);
            RegistryKey myRKey=Registry.CurrentUser; 
            myRKey=myRKey.OpenSubKey("Control Panel\\Desktop",true );
            myRKey.SetValue("WallPaper", foldername + FInfo[i].Name);

            richTextBox1.Text += "filename : " + foldername + FInfo[i].Name + "\n";
            myRKey.SetValue("TitleWallPaper","2");
            myRKey.Close();
            MessageBox.Show("桌面桌布已經修改！", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}