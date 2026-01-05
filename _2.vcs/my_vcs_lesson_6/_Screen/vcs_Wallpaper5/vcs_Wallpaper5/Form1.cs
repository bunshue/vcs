using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;//for DllImport, MarshalAs

namespace vcs_Wallpaper5
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

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(790, 295);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1250, 880);
            this.Text = "vcs_Wallpaper5";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //設定桌面圖片

            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

            //設定桌布 + 更新registry
            //DisplayPicture(filename, true);     // Display the picture on the desktop.

            //設定桌布 + 不更新registry
            DisplayPicture(filename, false);     // Display the picture on the desktop.

            richTextBox1.Text += "將檔案 : " + filename + " 設定成桌布, 完成\n";
        }


        // Display the file on the desktop.
        private void DisplayPicture(string filename, bool update_registry)
        {
            //richTextBox1.Text += "將檔案 : " + filename + " 設定成桌布\n";
            try
            {
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
            catch (Exception ex)
            {
                MessageBox.Show("Error displaying picture " + filename + ".\n" + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


