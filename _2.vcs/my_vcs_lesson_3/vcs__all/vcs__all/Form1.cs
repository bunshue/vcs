using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process

namespace vcs__all
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

            progressBar1.Value = 66;

            numericUpDown2.Minimum = 0;
            numericUpDown2.Maximum = 1;
            numericUpDown2.DecimalPlaces = 2;
            numericUpDown2.Increment = 0.01m;
            numericUpDown2.Value = 0.75m;

            notifyIcon1.Text = "Notify Icon Example";
            notifyIcon1.Icon = new Icon(@"D:\_git\vcs\_1.data\______test_files1\_material\ims.ico");
            notifyIcon1.ContextMenuStrip = this.contextMenuStrip1;

            // Handle the DoubleClick event to activate the form.
            notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
        }

        void show_item_location()
        {
            int W = 360;
            int H = 200;
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 70;
            dx = W + 10;
            dy = H + 10;

            groupBox0.Size = new Size(W, H);
            groupBox1.Size = new Size(W, H);
            groupBox2.Size = new Size(W, H);
            groupBox3.Size = new Size(W, H);
            groupBox4.Size = new Size(W, H);
            groupBox5.Size = new Size(W, H);
            groupBox6.Size = new Size(W, H);
            groupBox7.Size = new Size(W, H);
            groupBox8.Size = new Size(W, H);
            groupBox9.Size = new Size(W, H);
            groupBox10.Size = new Size(W, H);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            groupBox4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            groupBox5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            groupBox6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox7.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            groupBox8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            groupBox9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox10.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            richTextBox1.Size = new Size(W, H * 2 - 30);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1510, 920);
            this.Text = "vcs__all";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void LinkLabel_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("http://www.google.com.tw/");
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("C:\\Windows\\System32\\mspaint.exe");
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start(@"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt");
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("mailto:david@insighteyes.com");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "一個空的程式，介紹會用到的元件。\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得： TrackBar = " + trackBar1.Value + "   NumericUpDown = " + numericUpDown1.Value + "\nComboBox = " + comboBox1.SelectedIndex + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("您要將變更儲存至\"vcs_doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("您要將變更儲存至\"vcs_doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
            {
                MessageBox.Show("您選了Yes");
            }
            else if (result == DialogResult.No)
            {
                MessageBox.Show("您選了No");
            }
            else if (result == DialogResult.Cancel)
            {
                MessageBox.Show("您選了Cancel");
            }
            else
            {
                MessageBox.Show("您選了其他");
            }
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            progressBar1.Value = (int)numericUpDown1.Value;
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                richTextBox1.Text += "開啟檔案: " + openFileDialog1.FileName + "\n";
            else
                richTextBox1.Text += "未選擇檔案" + "\n";
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void notifyIcon1_DoubleClick(object Sender, EventArgs e)
        {
            Close();
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            numericUpDown3.Value = trackBar2.Value;
        }

        private void numericUpDown3_ValueChanged(object sender, EventArgs e)
        {
            trackBar2.Value = (Int32)numericUpDown3.Value;
        }

    }
}
