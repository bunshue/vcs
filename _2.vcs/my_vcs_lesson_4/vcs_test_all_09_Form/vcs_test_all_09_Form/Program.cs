using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_test_all_09_Form
{
    static class Program
    {
        /// <summary>
        /// 應用程式的主要進入點。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            
            Application.Run(new Form1());

            //Application.Run(new Form3());   //程式開啟時 開啟另一個表單
        }
    }
}
