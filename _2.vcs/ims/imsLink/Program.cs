using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace imsLink
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
            try
            {
                Application.Run(new Form1());
            }
            catch (Exception ex)
            {
                //richTextBox1.Text += "xxx錯誤訊息c : " + ex.Message + "\n";
            }

        }
    }
}
