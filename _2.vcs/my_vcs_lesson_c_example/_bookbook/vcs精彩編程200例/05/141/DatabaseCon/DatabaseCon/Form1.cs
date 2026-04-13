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
        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        string filename = @"D:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Data.MDF";

        public static string cnstr = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox6.Text = "(local)";
            textBox1.Text = filename;
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                //Access 或 EXCEL
                if (textBox1.Text != "")
                {
                    FileInfo FInfo = new FileInfo(textBox1.Text);
                    string strExtention = FInfo.Extension;
                    if (strExtention.ToLower() == ".mdb")
                    {
                        if (textBox2.Text != "")
                        {
                            cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";UID=" + textBox2.Text + ";PWD=" + textBox3.Text + ";";
                        }
                        else
                        {
                            cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";";
                        }
                    }
                    else if (strExtention.ToLower() == ".xls")
                    {
                        cnstr = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + textBox1.Text + ";Extended Properties=Excel 8.0;";
                    }
                }
                OleDbConnection oledbcon = new OleDbConnection(cnstr);
                try
                {
                    oledbcon.Open();
                    richTextBox1.Clear();
                    richTextBox1.Text = cnstr + "\n连接成功……";
                }
                catch
                {
                    richTextBox1.Text = "连接失败";
                }
            }
            else if (radioButton2.Checked == true)
            {
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                string cnstr = "server=" + textBox6.Text + ";database=master;Integrated Security=SSPI;";
                comboBox1.DataSource = getTable(cnstr);
                comboBox1.DisplayMember = "name";
                comboBox1.ValueMember = "name";
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
        }

        private DataTable getTable(string cnstr)
        {
            try
            {
                SqlConnection sqlcon = new SqlConnection(cnstr);
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
            {
                textBox4.Focus();
            }
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
            // 這種 cnstr Uid Pwd 應該都沒有用了
            string cnstr = "server=" + textBox6.Text + ";database=master;Uid=" + textBox5.Text + ";Pwd=" + textBox4.Text + ";";
            comboBox1.DataSource = getTable(cnstr);
            comboBox1.DisplayMember = "name";
            comboBox1.ValueMember = "name";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";
            string db_filename = "db_09_Data.MDF";
            string cnstr = string.Format(db_cnstr, db_filename);  // 資料庫連線參數, 連接字串
            richTextBox2.Text += "cnstr : " + cnstr + "\n";

            comboBox1.DataSource = getTable(cnstr);
            comboBox1.DisplayMember = "name";
            comboBox1.ValueMember = "name";
            comboBox1.Enabled = true;
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }
    }
}
