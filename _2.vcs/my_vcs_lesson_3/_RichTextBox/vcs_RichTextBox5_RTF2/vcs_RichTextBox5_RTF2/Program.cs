using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_RichTextBox5_RTF2
{
    static class Program
    {
        /// <summary>
        /// 應用程序的主入口點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}
