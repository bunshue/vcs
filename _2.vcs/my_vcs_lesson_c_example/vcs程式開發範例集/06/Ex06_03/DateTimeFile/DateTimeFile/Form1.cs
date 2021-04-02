using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;
namespace DateTimeFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dateTimePicker1.Value = DateTime.Parse("17:05:00");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.ShowDialog();
            textBox1.Text = folderBrowserDialog1.SelectedPath;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.ShowDialog();
            textBox2.Text = folderBrowserDialog1.SelectedPath;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
           if(DateTime.Now.ToLongTimeString()==dateTimePicker1.Value.ToLongTimeString())
           {
               if(textBox1.Text !="" && textBox2.Text != "")
               {
                   if(Directory.Exists(textBox2.Text+"\\"+DateTime.Now.Month.ToString())==false)
                   {
                       Directory.CreateDirectory(textBox2.Text+"\\"+DateTime.Now.Month.ToString()+"月");
                   }
                   CopyDirectory(textBox1.Text, textBox2.Text + "\\" + DateTime.Now.Month.ToString()+"\\"+DateTime.Now.Date.ToShortDateString());
               }
           }     
        }

        //private void button3_Click(object sender, EventArgs e)
        //{
        //    MessageBox.Show(dateTimePicker1.Value.ToLongTimeString());
        //}
        private void CopyDirectory(string sourcePath , string destPath)
        {
            DirectoryInfo dir = new DirectoryInfo(sourcePath);
            FileSystemInfo[] fileinfo = dir.GetFileSystemInfos();
            foreach (FileSystemInfo i in fileinfo)
            {
                if (i is DirectoryInfo)
                {
                   Directory.CreateDirectory(destPath+"\\"+i.Name);
                   CopyDirectory(sourcePath+"\\"+i.Name, destPath + "\\" + i.Name);
                }
                else
                {
                    if (File.Exists(destPath + "\\" + i.Name) == false)
                    {
                        File.Copy(i.FullName, destPath + "\\" + i.Name);
                    }
                }
            }
        }
    }
}