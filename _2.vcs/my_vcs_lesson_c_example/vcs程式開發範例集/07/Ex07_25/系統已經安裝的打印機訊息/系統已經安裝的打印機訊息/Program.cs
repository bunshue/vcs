using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace 系統已經安裝的打印機訊息
{
    static class Program
    {
        /// <summary>
        /// 運用程序的主入口點。
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
