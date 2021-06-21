using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace vcs_GetHardwareInfo
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}