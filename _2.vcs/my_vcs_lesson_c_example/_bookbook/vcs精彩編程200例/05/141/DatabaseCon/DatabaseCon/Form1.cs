using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.OleDb;
using System.Data.SqlClient;
using System.IO;

namespace DatabaseCon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public static string strCon = "";
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox6.Text = "(local)";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "*.mdb(Access数据库文件)|*.mdb|*.xls(Excel文件)|*.xls|*.*(所有文件)|*.*";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form2 frm = new Form2();
            frm.ShowDialog();
            textBox6.Text = Form2.strServer;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                if (textBox1.Text != "")
                {
                    FileInfo FInfo = new FileInfo(textBox1.Text);
                    string strExtention = FInfo.Extension;
                    if (strExtention.ToLower() == ".mdb")
                    {
                        if (textBox2.Text != "")
                        {
                            strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";UID=" + textBox2.Text + ";PWD=" + textBox3.Text + ";";
                        }
                        else
                        {
                            strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";";
                        }
                    }
                    else if (strExtention.ToLower() == ".xls")
                    {
                        strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";Extended Properties=Excel 8.0;";
                    }
                }
                OleDbConnection oledbcon = new OleDbConnection(strCon);
                try
                {
                    oledbcon.Open();
                    richTextBox1.Clear();
                    richTextBox1.Text = strCon + "\n连接成功……";
                }
                catch
                {
                    richTextBox1.Text = "连接失败";
                }
            }
            else if (radioButton2.Checked == true)
            {
                if (checkBox1.Checked == true)
                {
                    strCon = "Data Source=" + textBox6.Text + ";Initial Catalog =" + comboBox1.Text + ";Integrated Security=SSPI;";
                }
                else if (checkBox2.Checked == true)
                {
                    strCon = "Data Source=" + textBox6.Text + ";Database=" + comboBox1.Text + ";Uid=" + textBox5.Text + ";Pwd=" + textBox4.Text + ";";
                }
                SqlConnection sqlcon = new SqlConnection(strCon);
                try
                {
                    sqlcon.Open();
                    richTextBox1.Clear();
                    richTextBox1.Text = strCon + "\n连接成功……";
                }
                catch
                {
                    richTextBox1.Text = "连接失败";
                }
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
            {
                textBox1.Enabled = textBox2.Enabled = textBox3.Enabled=button1.Enabled  = true;
                radioButton2.Checked = false;
                textBox4.Enabled = textBox5.Enabled = textBox6.Enabled = button2.Enabled 
                    = checkBox1.Enabled = checkBox2.Enabled = comboBox1.Enabled = false;
            }
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked)
            {
                radioButton1.Checked = false;
                textBox1.Enabled = textBox2.Enabled = textBox3.Enabled = button1.Enabled = textBox4.Enabled = textBox5.Enabled = false;
                textBox6.Enabled = button2.Enabled = checkBox1.Enabled = checkBox2.Enabled = comboBox1.Enabled = true;
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                checkBox2.Checked = false;
                textBox4.Enabled = textBox5.Enabled = false;
                string str = "server=" + textBox6.Text + ";database=master;Integrated Security=SSPI;";
                comboBox1.DataSource = getTable(str);
                comboBox1.DisplayMember = "name";
                comboBox1.ValueMember = "name";
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            checkBox1.Checked = false;
            textBox4.Enabled = textBox5.Enabled = true;
            textBox5.Focus();
        }

        private DataTable getTable(string str)
        {
            try
            {
                SqlConnection sqlcon = new SqlConnection(str);
                SqlDataAdapter da = new SqlDataAdapter("select name from sysdatabases ", sqlcon);
                DataTable dt = new DataTable("sysdatabases");
                da.Fill(dt);
                return dt;
            }
            catch
            {
                return null;
            }
        }

        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
                textBox4.Focus();
        }

        private void textBox4_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
            {
                button4_Click(sender, e);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string str = "server=" + textBox6.Text + ";database=master;Uid=" + textBox5.Text + ";Pwd=" + textBox4.Text + ";";
            comboBox1.DataSource = getTable(str);
            comboBox1.DisplayMember = "name";
            comboBox1.ValueMember = "name";
        }
    }
}
