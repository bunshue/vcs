using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.DirectoryServices;

namespace 获取网络中所有工作组名称
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DirectoryEntry MainGroup = new DirectoryEntry("WinNT:");
            foreach (DirectoryEntry domain in MainGroup.Children)
            {
                listBox1.Text = "";
                listBox1.Items.Add(domain.Name);
            }   
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}