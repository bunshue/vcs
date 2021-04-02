using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLPeriphery
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=master"))
            {
                try
                {
                    SqlCommand cmd = new SqlCommand();
                    cmd.Connection = con;
                    cmd.Connection.Open();
                    string str = "xp_cmdshell 'copy " + this.textBox1.Text + " ";
                    str += "" + this.textBox2.Text + "'";
                    cmd.CommandText = str;
                    cmd.ExecuteNonQuery();
                    this.label3.Text = "已成功完成訊息拷貝";
                    
                }
                catch (Exception ey) { MessageBox.Show(ey.Message); }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.label3.Text = "";
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox2.Text = this.folderBrowserDialog1.SelectedPath;
            }
        }
    }
}