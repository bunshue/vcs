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
            progressBar1.Value = 66;

            numericUpDown2.Minimum = 0;
            numericUpDown2.Maximum = 1;
            numericUpDown2.DecimalPlaces = 2;
            numericUpDown2.Increment = 0.01m;
            numericUpDown2.Value = 0.75m;

            notifyIcon1.Text = "Notify Icon Example";
            notifyIcon1.Icon = new Icon(@"C:\_git\vcs\_1.data\______test_files1\_material\ims.ico");
            notifyIcon1.ContextMenuStrip = this.contextMenuStrip1;

            // Handle the DoubleClick event to activate the form.
            notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
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
            Process.Start(@"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt");
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            Process.Start("mailto:david@insighteyes.com");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            MessageBox.Show("一個空的程式，介紹會用到的元件。");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            MessageBox.Show("取得： TrackBar = " + trackBar1.Value + "   NumericUpDown = " + numericUpDown1.Value + "\nComboBox = " + comboBox1.SelectedIndex);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            MessageBox.Show("您要將變更儲存至\"vcs_doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("您要將變更儲存至\"vcs_doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
            if (result == DialogResult.Yes)
                MessageBox.Show("您選了Yes");
            else if (result == DialogResult.No)
                MessageBox.Show("您選了No");
            else if (result == DialogResult.Cancel)
                MessageBox.Show("您選了Cancel");
            else
                MessageBox.Show("您選了其他");
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            progressBar1.Value = (int)numericUpDown1.Value;
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                MessageBox.Show("開啟檔案: " + openFileDialog1.FileName);
            else
                MessageBox.Show("未選擇檔案");
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
