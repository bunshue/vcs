using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_FormSendData5
{
    public partial class Form1 : Form
    {
        Form2 f2 = new Form2("ddddd");
        public static Image imgPhoto = null;
        public static string filename = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird\AB_red.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            imgPhoto = Image.FromStream(fs);
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            //button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            pictureBox1.Size = new Size(310, 440);
            pictureBox1.Location = new Point(10 + 310 + 10, 10);

            richTextBox1.Size = new Size(300, 230);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(680, 500);
            this.Text = "vcs_FormSendData5 1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(100, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            f2.Show();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //f2.listView1.Items.Clear();

            for (int i = 0; i < 5; i++)
            {
                ListViewItem lt = new ListViewItem("AAAA");
                lt.SubItems.Add("BBBB");
                lt.SubItems.Add("CCCC");
                f2.listView1.Items.Add(lt);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
