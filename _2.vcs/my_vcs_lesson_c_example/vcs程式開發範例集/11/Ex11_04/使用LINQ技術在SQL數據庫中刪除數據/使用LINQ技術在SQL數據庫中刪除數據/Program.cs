using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace 使用LINQ技術在SQL數據庫中刪除數據
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
