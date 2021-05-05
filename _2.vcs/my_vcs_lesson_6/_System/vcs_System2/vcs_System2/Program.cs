using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

using System.Diagnostics;   //for Process
using System.IO;    //for Path

namespace vcs_System2
{
    static class Program
    {
        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            string MName = Process.GetCurrentProcess().MainModule.ModuleName;
            string PName = Path.GetFileNameWithoutExtension(MName);
            Process[] myProcess = Process.GetProcessesByName(PName);
            if (myProcess.Length > 1)
            {
                MessageBox.Show("本程序一次只能執行一個實例！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
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
