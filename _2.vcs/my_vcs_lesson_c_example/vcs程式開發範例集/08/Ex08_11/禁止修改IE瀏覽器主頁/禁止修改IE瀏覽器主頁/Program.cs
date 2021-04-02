using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace 禁止修改IE瀏覽器主頁
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
