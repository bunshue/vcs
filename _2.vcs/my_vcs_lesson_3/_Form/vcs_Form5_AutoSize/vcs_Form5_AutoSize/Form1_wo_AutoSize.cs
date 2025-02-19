﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_09_Form_AutoSize
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
        }

        private void LinkLabel_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("http://www.google.com.tw/");
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("C:\\Windows\\System32\\mspaint.exe");
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("C:\\test.txt");
        }

        private void linkLabel3_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("mailto:wang_wj@myson.com.tw");
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
            MessageBox.Show("您要將變更儲存至\"Myson_Doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("您要將變更儲存至\"Myson_Doc.doc\"嗎?", "Microsoft Office Word", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning);
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
    }
}
