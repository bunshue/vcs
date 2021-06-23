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
        string foldername = @"C:\______test_files\_pic";

        string strPath;
        string strInfo="";
        string[] strName=null;
        int Num = 0;
        int Count = 0;

        public Form1()
        {
            InitializeComponent();
            //strPath = System.Environment.CurrentDirectory+"\\Image";
            strPath = foldername;
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
                        strInfo += strType+ "#";
                    }
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo(strPath);
            GetAllFiles(dir);
            if (strInfo != "")
            {
                strName = strInfo.Split('#');
                Num = 0;
                showPic(Num);
                Count = strName.Length-1;
               
            }
            else
            {
                MessageBox.Show("影集里没有照片");
            }
        }

        private void showPic(int X)
        {
            this.pictureBox1.ImageLocation = strPath + "\\" + strName[X];
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Num += 1;
            if (Count >Num)
            {
                showPic(Num);
            }
            else
            {
                Num = 0;
                showPic(Num);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Num -= 1;
            if (Num>=0)
            {
                showPic(Num);
            }
            else
            {
                Num = Count-1;
                showPic(Num);
            }   
        }
    }
}