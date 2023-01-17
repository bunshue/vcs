using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ShowPicture6
{
    public partial class Form1 : Form
    {
                            string foldername = @"C:\______test_files\__pic\_書畫字圖\_peony1";

        List<String> filenames = new List<String>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Maximized;

                                                    if (Directory.Exists(foldername) == false)
                                                    {
                                                        richTextBox1.Text += "圖片資料夾不存在, 離開\n";
                                                        return;
                                                    }

                                                    // Load the list of files.
                                                    filenames = FindFiles(foldername, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);

                                                    for (int i = 0; i < filenames.Count; i++)
                                                    {
                                                        richTextBox1.Text += "get file \t" + filenames[i] + "\n";
                                                    }
                                                    richTextBox1.Text += "共有 " + filenames.Count.ToString() + " 個檔案\n";

            const int wid = 800;
            const int hgt = 300;
            const int margin = 3;
            int x = margin;
            int y = margin;
            const int num_columns = 3;
            const int xmax = num_columns * (wid + margin);

            // Find the images.
            //foreach (string filename in Directory.GetFiles(foldername, "*.jpg"))
            foreach (string filename in filenames)
            {
                Bitmap bitmap1 = new Bitmap(filename);
                int W = bitmap1.Width;
                int H = bitmap1.Height;
                richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
                PictureBox pbx = new PictureBox();
                pbx.Parent = this;
                pbx.SizeMode = PictureBoxSizeMode.Zoom;
                pbx.Image = bitmap1;
                pbx.Size = new Size(W, H);
                pbx.Location = new Point(x, y);
                x += wid + margin;
                if (x > xmax)
                {
                    x = margin;
                    y += hgt + margin;
                }
                pbx.MouseDown += pbx_MouseDown;
                pbx.MouseMove += pbx_MouseMove;
                pbx.MouseUp += pbx_MouseUp;
            }
        }

        private const int PB3_DEFAULT_POSITION_X = 600 - 10;
        private const int PB3_DEFAULT_POSITION_Y = 700;
        int pbx_position_x_old = PB3_DEFAULT_POSITION_X;
        int pbx_position_y_old = PB3_DEFAULT_POSITION_Y;

        bool flag_pbx_mouse_down = false;
        private void pbx_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pbx_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pbx_position_x_old = e.X;
            pbx_position_y_old = e.Y;

            //richTextBox1.Text += "你按了 : " + ((PictureBox)sender) + "\n";
        }

        private void pbx_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pbx_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pbx_position_x_old;
                int dy = e.Y - pbx_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                //pbx.Location = new Point(pbx.Location.X + dx, pbx.Location.Y + dy);
            }
        }

        private void pbx_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pbx_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pbx_position_x_old;
            int dy = e.Y - pbx_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            //pbx.Location = new Point(pbx.Location.X + dx, pbx.Location.Y + dy);

            //要反推回原本那個pbox
        }




                                                    // See: Search for files that match multiple patterns in C#
                                                    //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
                                                    // Search for files matching the patterns.
                                                    private List<string> FindFiles(string fname, string patterns, bool search_subdirectories)
                                                    {
                                                        // Make the result list.
                                                        List<string> files = new List<string>();

                                                        // Get the patterns.
                                                        string[] pattern_array = patterns.Split(';');

                                                        // Search.
                                                        SearchOption search_option = SearchOption.TopDirectoryOnly;
                                                        if (search_subdirectories) search_option = SearchOption.AllDirectories;
                                                        foreach (string pattern in pattern_array)
                                                        {
                                                            foreach (string filename in Directory.GetFiles(fname, pattern, search_option))
                                                            {
                                                                if (!files.Contains(filename)) files.Add(filename);
                                                            }
                                                        }

                                                        // Sort.
                                                        files.Sort();

                                                        // Return the result.
                                                        return files;
                                                    }


    }
}
