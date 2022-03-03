using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_JumpNewForm
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
            //Application.Run(new Form1()); //原本

            //Application.Run中不要有任何窗體名稱,這樣主程序就是空的,在主程序運行前先運行你想打開的Form1窗體
            new Form1().Show();
            Application.Run();
        }
    }
}
