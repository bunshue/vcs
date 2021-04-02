using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Text.RegularExpressions;
using System.Data.SqlClient;
namespace ProcedureNumber
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox3_Validating(object sender, CancelEventArgs e)
        {
            try
            {
                int x = Int32.Parse(textBox3.Text);

                if (x < 60 && x > 20)
                {
                    errorage.SetError(this.textBox3, "");
                }
                else
                {
                    errorage.SetError(this.textBox3, "數值應在20-60之間");
                }
            }
            catch
            {
                errorage.SetError(this.textBox3, "應為整數");
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            AutoID();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (ifNull())
            {
                if (info())
                {
                    if (IDCard(this.textBox4.Text))
                    {

                        InsertInfo();

                    }
                    else
                    { MessageBox.Show("身份證號格式不正確"); }
                }
            }
            else
            {
                MessageBox.Show("請將訊息新增完整");
            }
        }
        //
        public bool IDCard(string ID)
        {
            if (!Regex.IsMatch(ID, @"^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$"))  //15ID
            {
                if (Regex.IsMatch(ID,
                @"^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{4}$"))  //18ID
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        //
        private bool info()
        {
            for (int i = 0; i < this.textBox5.Text.Length; i++)
            {
                if (!char.IsNumber(this.textBox5.Text[i]))
                {
                    if (this.textBox5.Text[i] != '.')
                    {
                        MessageBox.Show("工資訊息有誤");
                        return false;
                    }
                }

            }
            return true;
        }

        private bool ifNull()
        {
            foreach (Control Con in this.Controls)
            {
                if (Con is TextBox)
                {
                    if (Con.Text == "")
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        private void NullValue()
        {
            foreach (Control Con in this.Controls)
            {
                if (Con is TextBox)
                {
                    Con.Text = "";

                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void AutoID()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                con.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = "select Max(tb_ID) from 員工個人訊息";
                cmd.Connection = con;
                string str = cmd.ExecuteScalar().ToString();
                if (str == "")
                    this.textBox1.Text = "P1001";
                else
                {

                    this.textBox1.Text = "P" + Convert.ToString(Convert.ToInt32(str.Substring(1)) + 1);

                }
            }
        }

        private void InsertInfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                con.Open();
                SqlCommand cmd = new SqlCommand();
                string strSql = "insert into 員工個人訊息 values ('" + this.textBox1.Text + "','" + this.textBox2.Text + "','" + this.textBox3.Text + "','" + this.textBox5.Text + "','" + this.textBox4.Text + "')";
                cmd.CommandText = strSql;
                cmd.Connection = con;
                cmd.ExecuteNonQuery();
                con.Close();
                MessageBox.Show("成功新增訊息");
                NullValue();
            }
            AutoID();
        }

    }
}