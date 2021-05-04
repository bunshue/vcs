using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 映射網絡驅動器
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           this.comboBox2.DataSource = Environment.GetLogicalDrives();
           this.comboBox1.DataSource = DirName();
        }

        private string[] DirName()
        {
            int j = 0;
            string[] str = new string[26];
            for (int i = 65; i <91;i++ )
            {
                str [j]= Convert.ToChar(i).ToString()+":";
                j++;
            }
            return str;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.folderBrowserDialog1.SelectedPath;
            }
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (ConDir(this.comboBox1.Text, this.textBox1.Text))
            {
                MessageBox.Show("已映射成功！！！");
            }
        }

        private bool ConDir(string Name, string Path)
        {
            try
            {
                System.Diagnostics.ProcessStartInfo psi = new System.Diagnostics.ProcessStartInfo();
                psi.FileName = @"cmd.exe";
                psi.Arguments = @"/c net use " + Name + " " + Path + "";
                psi.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
                System.Diagnostics.Process.Start(psi);
                return true;
            }
            catch (Exception ey)
            {
                return false;
            }

        }
    }
}