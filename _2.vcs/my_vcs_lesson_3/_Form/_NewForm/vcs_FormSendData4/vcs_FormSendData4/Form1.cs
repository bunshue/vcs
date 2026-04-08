using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData4
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
            int x_st = 10;
            int y_st = 10;
            int W = 500;
            int H = 200;
            int dx = W + 10;
            int dy = H + 40;

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0+30);
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);

            label2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            richTextBox2.Size = new Size(W, H);
            richTextBox2.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 30);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
            label1.Text = "來自表單2的訊息";
            label2.Text = "發給表單2的訊息";

            this.Size = new Size(W + 40, H * 2 + 130);
            this.Text = "vcs_FormSendData4 表單 1";
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

    }
}
