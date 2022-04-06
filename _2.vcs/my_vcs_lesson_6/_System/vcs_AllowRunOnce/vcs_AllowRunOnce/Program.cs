using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

using System.Diagnostics;
using System.Threading;

namespace vcs_AllowRunOnce
{
    static class Program
    {
        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            //原本是這3行
            //Application.EnableVisualStyles();
            //Application.SetCompatibleTextRenderingDefault(false);
            //Application.Run(new Form1());

            //改成

            Process[] processes = Process.GetProcessesByName(Application.CompanyName);
            if (processes.Length > 1)
            {
                MessageBox.Show("應用程序已經在運行中。");
                Thread.Sleep(1000);
                System.Environment.Exit(1);
            }
            else
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new Form1());
            }

        }
    }
}
