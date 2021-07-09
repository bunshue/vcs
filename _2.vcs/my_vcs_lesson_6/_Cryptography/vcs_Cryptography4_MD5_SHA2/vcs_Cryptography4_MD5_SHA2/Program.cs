using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace vcs_Cryptography4_MD5_SHA2
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
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
