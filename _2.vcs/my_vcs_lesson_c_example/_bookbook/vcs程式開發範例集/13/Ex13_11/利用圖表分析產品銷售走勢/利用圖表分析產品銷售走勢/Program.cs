﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace 利用圖表分析產品銷售走勢
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
