using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace 網站人氣指數曲線分析
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
