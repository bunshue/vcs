using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                        //for StreamReader, SearchOption

namespace vcs_test_all_06_DirectoryFile2
{
    public partial class Form1 : Form
    {
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
            x_st = 12;
            y_st = 12;
            dx = 170;
            dy = 60;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            string foldername = @"C:\______test_files";

            SearchOption search_option;
            search_option = SearchOption.TopDirectoryOnly;
            // Look for graphic files.
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            string[] patterns = { "*.*" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(foldername, pattern, search_option))
                {
                    richTextBox1.Text += filename + "\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(多層)
            //string foldername = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\陳一郎_紅燈碼頭\";
            //string foldername = @"C:\dddddddddd\_music_from_yt";
            string foldername = @"C:\______test_files";
            
            SearchOption search_option;
            search_option = SearchOption.AllDirectories;
            // Look for graphic files.
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            string[] patterns = { "*.*" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(foldername, pattern, search_option))
                {
                    richTextBox1.Text += filename + "\n";
                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得資料夾下的所有檔案
            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = Directory.GetFiles(@"C:\______test_files", "*.*", SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += filename + "\n";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            string foldername = @"C:\______test_files";

            foreach (string filename in Directory.GetFileSystemEntries(foldername))
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的TXT檔案(一層)
            string foldername = @"C:\______test_files";

            foreach (string filename in Directory.GetFileSystemEntries(foldername, "*.txt"))
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //搜尋子目錄內的所有檔案
            string foldername = @"C:\______test_files";

            int cnt = 0;
            DirectoryInfo dir = new DirectoryInfo(foldername);
            richTextBox1.Text += "搜尋子目錄內的所有檔案, 子目錄 : " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            cnt = 0;
            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                //richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
                richTextBox1.Text += d + "\n";
            }

            FileInfo[] aaaa = dir.GetFiles();
            cnt = 0;
            richTextBox1.Text += "子目錄 " + dir.Name + " 下的檔案 :\n";
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                //richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
                richTextBox1.Text += b + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得一層檔案
            string foldername = @"C:\______test_files";

            DirectoryInfo dir = new DirectoryInfo(foldername);
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += file.Name + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            string foldername = @"C:\______test_files";

            string[] files = Directory.GetFiles(foldername);
            for (int i = 0; i < files.Length; i++)
            {
                richTextBox1.Text += files[i] + "\n";
                //textBox2.Lines = files;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

    }
}
