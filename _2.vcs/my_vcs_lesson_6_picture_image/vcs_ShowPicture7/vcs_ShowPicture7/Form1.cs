using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ShowPicture7
{
    public partial class Form1 : Form
    {
        bool debug_mode = false;

        //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";

        // The list of files we will pick from.
        private List<string> FileNames = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (Directory.Exists(foldername) == false)
            {
                richTextBox1.Text += "圖片資料夾不存在, 離開\n";
                return;
            }

            //this.WindowState = FormWindowState.Maximized;

            show_item_location();

            this.TopMost = true;

            FileNames.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_01.jpg");
            FileNames.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_02.jpg");
            FileNames.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_03.jpg");
            FileNames.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_04.jpg");
            FileNames.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_05.jpg");
        }

        void show_item_location()
        {
            this.Location = new Point(0, 50);
            if (debug_mode == false)
            {
                this.Size = new Size(200, 280);
                richTextBox1.Visible = false;
            }
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            int len = FileNames.Count;
            if (len <= 0)
            {
                richTextBox1.Text += "無圖片, 離開\n";
                return;
            }

            Random r = new Random();
            int selected_index = r.Next(len);

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename = FileNames[selected_index];
            Form2 f2 = new Form2(filename);
            f2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int cnt = 50;
            for (int i = 0; i < cnt; i++)
            {
                button1_Click(sender, e);
                Application.DoEvents();
                System.Threading.Thread.Sleep(50);
            }
        }
    }
}
