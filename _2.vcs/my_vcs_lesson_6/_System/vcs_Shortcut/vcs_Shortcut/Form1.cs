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

namespace vcs_Shortcut
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立 桌面捷徑 與 開始頁捷徑
            string exe_filename = @"D:\_git\vcs\_2.vcs\__ok_program\小朋友讀唐詩\小朋友讀唐詩.exe";

            WshShell sl = new WshShell();
            //桌面捷徑
            string dtpath = System.Environment.GetFolderPath(Environment.SpecialFolder.DesktopDirectory) + "\\小朋友讀唐詩.lnk";
            //開始頁捷徑
            string dtpath1 = System.Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\\程序\\小朋友讀唐詩\\小朋友讀唐詩.lnk";

            string dd = Path.GetDirectoryName(dtpath1);
            if (!Directory.Exists(dd))
            {
                Directory.CreateDirectory(dd);
            }
            IWshShortcut sc = (IWshShortcut)sl.CreateShortcut(dtpath1);
            sc.TargetPath = exe_filename;   //目標
            sc.WorkingDirectory = @"D:\_git\vcs\_2.vcs\__ok_program\小朋友讀唐詩";    //開始位置
            sc.Description = "建立運用程序的快捷方式"; //註解
            sc.Save();

            IWshShortcut sc1 = (IWshShortcut)sl.CreateShortcut(dtpath);
            sc1.TargetPath = exe_filename;  //目標
            sc1.WorkingDirectory = @"D:\_git\vcs\_2.vcs\__ok_program\小朋友讀唐詩";    //開始位置
            sc1.Description = "建立運用程序的快捷方式";    //註解
            sc1.Save();
            richTextBox1.Text += "建立快捷方式成功\n";
        }
    }
}
