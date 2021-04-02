using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;
using IWshRuntimeLibrary;
using System.IO;
namespace 建立運用程序快捷方式
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string exePath = "";
        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                exePath = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (exePath.Length == 0)
            {
                MessageBox.Show("請選擇運用程序");
            }
            else
            {
                WshShell sl = new WshShell();
                string dtpath = System.Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory) + "\\ls.lnk";
                string dtpath1 = System.Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\\程序\\用一生下載你\\shj.lnk";
                string dd = Path.GetDirectoryName(dtpath1);
                if (!Directory.Exists(dd))
                {
                    Directory.CreateDirectory(dd);
                }
                IWshShortcut sc = (IWshShortcut)sl.CreateShortcut(dtpath1);
                sc.TargetPath = exePath;
                sc.Description = "建立運用程序的快捷方式";
                sc.Save();

                IWshShortcut sc1 = (IWshShortcut)sl.CreateShortcut(dtpath);
                sc1.TargetPath = exePath;
                sc1.Description = "建立運用程序的快捷方式";
                sc1.Save();
                MessageBox.Show("建立快捷方式成功");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
