using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_programming
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

            /* 第 12 章 */
            //Application.Run(new jaggedArray());     //有點多

            /* 第 14 章 */
            //Application.Run(new ScoreFile());   //看存成二進位檔 與 讀出二進位檔

            /* 第 16 章 */
            //Application.Run(new keyevent());

            /* 第 18 章 */
            //Application.Run(new Form1());           //有使用到 MyClass.cs

            //Application.Run(new MyForm());

            /* 第 19 章 */
            Application.Run(new MainForm());

            /* 第 20 章 */
            //Application.Run(new ShapeManagerForm());

        }
    }
}
