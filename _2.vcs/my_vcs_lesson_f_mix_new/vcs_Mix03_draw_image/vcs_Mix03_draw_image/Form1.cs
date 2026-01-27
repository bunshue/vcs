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
//using System.Drawing.Imaging;   //for ColorMatrix, ImageAttributes
using System.Drawing.Drawing2D;  // for GraphicsPath
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;

namespace vcs_Mix03_draw_image
{
    public partial class Form1 : Form
    {
        Bitmap bitmap1;
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
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
            dx = 200 + 5;
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

            pictureBox1.Size = new Size(600, 600);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1360, 710);
            this.Text = "vcs_Mix03_draw_image";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        //測試矩陣旋轉 ST
        PointF RotationMatrix(PointF pt, double theta)
        {
            float xx = (float)(Math.Cos(theta) * pt.X - Math.Sin(theta) * pt.Y);
            float yy = (float)(Math.Sin(theta) * pt.X + Math.Cos(theta) * pt.Y);

            return new PointF(xx, yy);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //測試矩陣旋轉
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 10);
            Point point1a = new Point(0, 0);
            Point point2a = new Point(500, 0);
            //g.DrawLine(p, point1a, point2a);

            p = new Pen(Color.Green, 10);

            double theta = Math.PI / 6;
            PointF point1aa = RotationMatrix(point1a, theta);
            PointF point2aa = RotationMatrix(point2a, theta);
            //g.DrawLine(p, point1aa, point2aa);
            richTextBox1.Text += "point1aa=" + point1aa + "\n";
            richTextBox1.Text += "point2aa=" + point2aa + "\n";

            PointF[] curvePoints = new PointF[8];    //一維陣列內有 8 個Point
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i].X = 50 * i;
                curvePoints[i].Y = 0;
            }
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 10);
            g.DrawLines(grayPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i] = RotationMatrix(curvePoints[i], theta);
            }

            g.DrawLines(redPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                g.FillEllipse(Brushes.Red, curvePoints[i].X - 10, curvePoints[i].Y - 10, 20, 20);
            }

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);
            Rectangle src_area = new Rectangle(100, 100, 100, 100);//要截取的矩形區域
            Rectangle dst_area = new Rectangle(400, 50, 100, 100);//要截取的矩形區域
            //g.DrawImage(bmp, dst_area, src_area, GraphicsUnit.Pixel);
            g.DrawImage(bmp, src_area, src_area, GraphicsUnit.Pixel);

            int x_st = 100;
            int y_st = 100;
            int w = 100;
            int h = 100;
            for (int j = 0; j < h; j++)
            {
                for (int i = 0; i < w; i++)
                {
                    Color clr = bitmap1.GetPixel(x_st + i, y_st + j);
                    PointF new_pt = RotationMatrix(new PointF(x_st + i, y_st + j), theta);
                    if ((new_pt.X > 0) && (new_pt.Y > 0))
                    {
                        bitmap1.SetPixel((int)new_pt.X, (int)new_pt.Y, clr);
                    }

                }
            }

            pictureBox1.Image = bitmap1;
        }

        //測試矩陣旋轉 SP

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


            //從pictureBox開始畫圖

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類

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
    }
}
