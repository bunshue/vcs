using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageFormat, ImageLockMode, Encoder, ImageCodecInfo
using System.Drawing.Drawing2D;  // for GraphicsPath
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;


namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        //Point一維陣列
        Point[] pts = new Point[6];    //一維陣列內有6個Point
        int find_point_index = -1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            int x_st = 400;
            int y_st = 80;
            int dy = 50;
            pts[0] = new Point(x_st + 0, y_st + dy * 0);
            pts[1] = new Point(x_st + 0, y_st + dy * 1);
            pts[2] = new Point(x_st + 0, y_st + dy * 2);
            pts[3] = new Point(x_st + 0, y_st + dy * 3);
            pts[4] = new Point(x_st + 0, y_st + dy * 4);
            pts[5] = new Point(x_st + 0, y_st + dy * 5);
        }

        /*
        //直接寫一個OnPaint在此, 取代Form1_Paint
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.ClientSize.Width - 10, this.ClientSize.Height - 10);
        }
        */

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 160 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            pictureBox1.Size = new Size(600, 600);
            pictureBox1.Location = new Point(x_st + dx * 2 + 180, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 7 - 40, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(1450, 710);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                        filenames.Add(fullname);
                    }
                }
            }
        }

        // See: Search for files that match multiple patterns in C#
        //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
        // Search for files matching the patterns.
        private List<string> FindFiles(string dir_name, string patterns, bool search_subdirectories)
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
                foreach (string filename in Directory.GetFiles(dir_name, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //撈出所有圖片檔 並存成一個List 1

            //撈出所有圖片檔 並存成一個List
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            filenames.Clear();

            GetAllFiles(foldername);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //撈出所有圖片檔 並存成一個List 2

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";

            filenames.Clear();

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
        }


        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string dir_name = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony2";

            // The list of files we will pick from.
            List<string> FileNames = new List<string>();

            // Load the list of files.
            if (Directory.Exists(dir_name))
            {
                FileNames = FindFiles(dir_name, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);
            }
            else
            {
                FileNames = new List<string>();
            }

            for (int i = 0; i < FileNames.Count; i++)
            {
                richTextBox1.Text += "get file \t" + FileNames[i] + "\n";
            }

            Random Rand = new Random();

            // Repeat until we succeed or run out of files.
            for (; ; )
            {
                // Pick a random image.
                int file_num = Rand.Next(FileNames.Count);

                // Try to use that image.
                try
                {
                    richTextBox1.Text += "使用圖片 : " + FileNames[file_num] + "\n";
                    // Set the desktop picture.
                    //DisplayPicture(FileNames[file_num], checkBox1.Checked);
                    break;
                }
                catch
                {
                    // This file doesn't work. Remove it from the list.
                    FileNames.RemoveAt(file_num);

                    // If there are no more files, stop trying.
                    if (FileNames.Count == 0)
                    {
                        break;
                    }
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //從pictureBox開始畫圖

            int[] gray = new int[220];

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            //g.DrawLines(Pens.Red, gray.ToArray());

            //g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 0, 0, 440, 256);

            Point[] curvePoints = new Point[220];    //一維陣列內有 8 個Point

            int i;
            for (i = 0; i < 220; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = i * 2;
            }


            // Draw lines between original points to screen.
            g.DrawLines(Pens.Red, curvePoints);   //畫直線
            // Draw curve to screen.
            //gc.DrawCurve(redPen, curvePoints); //畫曲線


        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawString("點選表單中的紅點", new Font("標楷體", 16), new SolidBrush(Color.Black), pts[0].X - 65, pts[0].Y - 50);
            //e.Graphics.DrawRectangle(Pens.Red, 100, 100, 300, 300);
            foreach (Point pt in pts)
            {
                e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);
            }
        }

        bool flag_mouse_down = false;
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            Point pt = FindPointAt(e.X, e.Y);
            if (pt == new Point(9999, 9999))
            {
                richTextBox1.Text += "找不到\n";
            }
            else
            {
                flag_mouse_down = true;
                richTextBox1.Text += "找到 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")\n";
                int index = get_index(pt);
                richTextBox1.Text += index.ToString() + "\n";
                find_point_index = index;
            }
        }

        private Point FindPointAt(int X, int Y)
        {
            foreach (Point pt in pts)
            {
                float dx = pt.X - X;
                float dy = pt.Y - Y;
                if (dx * dx + dy * dy <= 20 * 20)
                {
                    return pt;
                }
            }
            return new Point(9999, 9999);
        }

        int get_index(Point point)
        {
            int len = pts.Length;
            int index = 0;
            for (index = 0; index < len; index++)
            {
                if (point == pts[index])
                {
                    return index;
                }
            }
            return -1;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                update_pts(find_point_index, e.Location);
                this.Invalidate();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;
        }

        void update_pts(int index, Point point)
        {
            int len = pts.Length;
            if ((index < 0) || index >= len)
            {
                richTextBox1.Text += index.ToString();
                //richTextBox1.Text += "XXXXXXX\n";
                return;
            }
            pts[index] = point;
        }
    }
}
