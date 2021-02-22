using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace WindowsFormsApplication1
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
            //Application.Run(new Form1());

            /* 第 3 章 */
            //Application.Run(new ch3Test());

            /* 第 4 章 */
            Application.Run(new ThreeNumbers());

            /* 第 5 章 */
            //Application.Run(new clock());
            //Application.Run(new LocalVar());
            //Application.Run(new InstanceVar());

            /* 第 5, 6 章 */
            //Application.Run(new guessNumber());

            /* 第 6 章 */
            //Application.Run(new FiveNumbers());
            //Application.Run(new order());

            /* 第 7 章 */
            //Application.Run(new addnum());

            /* 第 7, 8 章 */
            //Application.Run(new digitsystem());

            /* 第 7 章 */
            //Application.Run(new double_loop());

            /* 第 8, 9 章 */
            //Application.Run(new Multi_1DArray());

            /* 第 9 章 */
            //Application.Run(new matchNumbers());

            /* 第 10 章 */
            //Application.Run(new testPictures());
            //Application.Run(new memory());

            /* 第 11 章 */
            //Application.Run(new TwoDArray());

            /* 第 12 章 */
            //Application.Run(new jaggedArray());

            /* 第 13 章 */
            //Application.Run(new Function());
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
