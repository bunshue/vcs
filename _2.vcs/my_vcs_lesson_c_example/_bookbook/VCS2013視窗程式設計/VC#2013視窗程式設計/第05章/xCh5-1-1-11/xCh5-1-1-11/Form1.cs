using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_1_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            domainUpDown1.Items.Add((textBox1.Text.Trim()));
            textBox2.Text=textBox2.Text + Environment.NewLine +textBox1.Text.Trim();
            textBox1.Text = "";
            label1.Text = "目前共有 " + domainUpDown1.Items.Count + " 個選項";
        }

        private void domainUpDown1_SelectedItemChanged(object sender, EventArgs e)
        {
            label2.Text = "目前選到的是：" + domainUpDown1.Text;
            label3.Text = "目前選到的是：" + (string)domainUpDown1.SelectedItem;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (domainUpDown1.Sorted)
            {
                domainUpDown1.Sorted = false;
            }
            else
            {
                domainUpDown1.Sorted = true;
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if (domainUpDown1.Wrap)
            {
                domainUpDown1.Wrap = false;
            }
            else
            {
                domainUpDown1.Wrap = true;
            }
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (domainUpDown1.InterceptArrowKeys)
            {
                domainUpDown1.InterceptArrowKeys = true;
            }
            else
            {
                domainUpDown1.InterceptArrowKeys = false;
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Text = "新增";
            label1.Text = "目前共有 " + domainUpDown1.Items.Count + " 個選項";
        }
    }
}
