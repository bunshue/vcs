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

            /* 第 2, 18 章 */
            //Application.Run(new Form1());   //有Class應用範例

            /* 第 8, 9 章 */
            //Application.Run(new Multi_1DArray());

            /* 第 9 章 */
            //Application.Run(new matchNumbers());        //1A1B猜數字遊戲

            /* 第 10 章 */
            Application.Run(new testPictures());
            //Application.Run(new memory());

            /* 第 11 章 */
            //Application.Run(new TwoDArray());

            /* 第 12 章 */
            //Application.Run(new jaggedArray());     //有點多

            /* 第 13 章 */
            //Application.Run(new CallByRef());

            /* 第 14 章 */
            //Application.Run(new ScoreFile());

            /* 第 15 章 */
            //Application.Run(new ListBoxDemo());
            //Application.Run(new SimpleEditor());

            /* 第 16 章 */
            //Application.Run(new mouseevent());
            //Application.Run(new keyevent());

            /* 第 18 章 */
            //Application.Run(new Form1());
            //Application.Run(new DateForm());
            //Application.Run(new PersonForm());
            //Application.Run(new MyForm());

            /* 第 19 章 */
            //Application.Run(new Ch19Test());
            //Application.Run(new StudentForm());
            //Application.Run(new TeacherForm());
            //Application.Run(new MainForm());

            /* 第 20 章 */
            //Application.Run(new ShapeManagerForm());

            //Application.Run(new MessageBoxForm());
            //Application.Run(new Midterm());
        }
    }
}
