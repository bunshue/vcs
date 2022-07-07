using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;    //for Assembly
using System.Diagnostics;   //for FileVersionInfo

namespace vcs_Assembly
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
            dy = 80;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //Get APP Info
            string result = appInfo();
            richTextBox1.Text += result + "\n";
        }

        public static string appInfo()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fvi = FileVersionInfo.GetVersionInfo(assembly.Location);
            string result = "File Version: " + fvi.FileVersion
                + Environment.NewLine + "Company Name: " + fvi.CompanyName
                + Environment.NewLine + "Comments: " + fvi.Comments
                + Environment.NewLine + "Product Name: " + fvi.ProductName
                + Environment.NewLine + "Copyright: " + fvi.LegalCopyright
                + Environment.NewLine + "File Name: " + fvi.FileName
                + Environment.NewLine + "Original File Name: " + fvi.OriginalFilename
                + Environment.NewLine + "Product Version: " + fvi.ProductVersion
                + Environment.NewLine + "Special build: " + fvi.SpecialBuild
                + Environment.NewLine + "" + fvi.CompanyName;
            return result;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀取exe版本號
            //讀取exe版本號

            string filename = @"C:\______test_files\_material\_dll\AForge.Video.dll";

            Assembly currentAssembly = Assembly.LoadFile(filename);
            //Assembly updatedAssembly = Assembly.LoadFile(updatedAssemblyPath);

            AssemblyName currentAssemblyName = currentAssembly.GetName();
            //AssemblyName updatedAssemblyName = updatedAssembly.GetName();

            richTextBox1.Text += currentAssembly.GetName() + "\n";



        }

        private void button2_Click(object sender, EventArgs e)
        {
            //通過exe文件獲得版本

            //通過exe文件獲得版本

            //string path = @"C:\Program Files (x86)\ArcGIS\Desktop10.8\bin\ArcMap.exe";
            string path = @"vcs_Assembly.exe";

            richTextBox1.Text += "版本 : " + GetVersion(path) + "\n";
        }

        public string GetVersion(string path)
        {
            string version = string.Empty;
            FileVersionInfo file = FileVersionInfo.GetVersionInfo(path);
            //版本号显示为“主版本号.次版本号.内部版本号.专用部件号”。
            //version = String.Format("{0}.{1}.{2}.{3}", file.FileMajorPart, file.FileMinorPart, file.FileBuildPart, file.FilePrivatePart);
            //使用文件版本信息
            version = file.FileVersion;
            return version;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得目前應用程式版本
            richTextBox1.Text += "本程式版本資訊 : " + "Ver：" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得NOTEPAD版本資訊
            richTextBox1.Text += "取得NOTEPAD版本資訊 : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }
    }
}
