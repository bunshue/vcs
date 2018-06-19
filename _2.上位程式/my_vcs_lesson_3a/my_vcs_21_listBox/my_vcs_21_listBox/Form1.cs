using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_21_listBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string[] itemStr = { "ListBox項目1", "ListBox項目2", "ListBox項目3", "ListBox項目4", "ListBox項目5", "ListBox項目6", "ListBox項目7", "ListBox項目8", "ListBox項目9" };
            foreach (string str in itemStr)
                listBox1.Items.Add(str);

            listBox1.SelectedIndex = 3;

            label1.Text = "第四項是：" + listBox1.SelectedItem;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(textBox1.Text.Length >0)
                listBox1.Items.Add(textBox1.Text);
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            //把選到的項目顯示到textBox裡面。
        }
    }
}
