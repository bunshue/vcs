using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_Wallpaper2
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool SystemParametersInfo(uint uiAction, uint uiParam, String pvParam, uint fWinIni);

        private const uint SPI_SETDESKWALLPAPER = 0x14;
        private const uint SPIF_UPDATEINIFILE = 0x1;
        private const uint SPIF_SENDWININICHANGE = 0x2;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            DisplayPicture(filename, true);     // Display the picture on the desktop.

            richTextBox1.Text += "將檔案 : " + filename + " 設定成桌布, 完成\n";
        }

        // Display the file on the desktop.
        private void DisplayPicture(string filename, bool update_registry)
        {
            //richTextBox1.Text += "將檔案 : " + filename + " 設定成桌布\n";

            // If we should update the registry,
            // set the appropriate flags.
            uint flags = 0;
            if (update_registry)
            {
                flags = SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE;
            }

            // Set the desktop background to this file.
            if (!SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, filename, flags))
            {
                richTextBox1.Text += "*** SystemParametersInfo failed.\n";
            }
        }
    }
}
