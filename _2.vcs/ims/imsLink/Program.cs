using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

using System.Diagnostics;   //for Process
using System.IO;    //for Path

namespace imsLink
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
                MessageBox.Show("不允許重複執行本程式", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                try
                {
                    Application.Run(new Form1());
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
                }
            }
        }
    }
}
