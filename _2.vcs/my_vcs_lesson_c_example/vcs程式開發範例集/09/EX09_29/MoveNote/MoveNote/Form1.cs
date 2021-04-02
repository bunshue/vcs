using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace MoveNote
{
    public partial class Form1 : Form
    {
        static int Num = 0;
        int Count = 0;
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void button6_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Resultinfo(Num);
            using (SqlCommand cmd = new SqlCommand("select Count(*) from using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLDelete
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = this.textBox1.Text;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    showinfo();
                    MessageBox.Show("刪除成功");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
                catch
                {
                    MessageBox.Show("SQL語句有誤");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
            }
        }

        private void showinfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }    
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }
    }
}", con))
            {
                con.Open();
                Count = Convert.ToInt32(cmd.ExecuteScalar());
                con.Close();
            }
        }

        private DataSet DtReslut(int i)
        {
            using (SqlDataAdapter da = new SqlDataAdapter())
            {
                da.SelectCommand = new SqlCommand("select * from using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLDelete
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = this.textBox1.Text;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    showinfo();
                    MessageBox.Show("刪除成功");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
                catch
                {
                    MessageBox.Show("SQL語句有誤");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
            }
        }

        private void showinfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }    
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }
    }
}", con);
                DataSet ds = new DataSet();
                da.Fill(ds, i, i + 1, "using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace SQLDelete
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09");
        private void button1_Click(object sender, EventArgs e)
        {
            using (SqlCommand cmd = new SqlCommand())
            {
                try
                {
                    con.Open();
                    cmd.Connection = con;
                    cmd.CommandText = this.textBox1.Text;
                    cmd.ExecuteNonQuery();
                    con.Close();
                    showinfo();
                    MessageBox.Show("刪除成功");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
                catch
                {
                    MessageBox.Show("SQL語句有誤");
                    this.textBox1.Focus();
                    this.textBox1.SelectAll();
                }
            }
        }

        private void showinfo()
        {
            using (SqlConnection con = new SqlConnection("server=.;pwd=;uid=sa;database=db_09"))
            {
                DataTable dt = new DataTable();
                SqlDataAdapter da = new SqlDataAdapter("select * from 員工表", con);
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }    
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            showinfo();
        }
    }
}");
                return ds;
            }
        }


        private void Resultinfo(int j)
        {
            DataSet dsNew = DtReslut(j);
            this.textBox1.Text = dsNew.Tables[0].Rows[0][0].ToString();
            this.textBox2.Text = dsNew.Tables[0].Rows[0][1].ToString();
            this.textBox4.Text = dsNew.Tables[0].Rows[0][2].ToString();
            this.textBox5.Text = dsNew.Tables[0].Rows[0][3].ToString();
        }



        private void button1_Click(object sender, EventArgs e)
        {
            Num = 0;
            Resultinfo(Num);
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Num -= 1;
            if (Num >= 0)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是首條記錄");
                Num = 0;
                return; ;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Num += 1;
            if (Num < Count)
            {
                Resultinfo(Num);
            }
            else
            {
                MessageBox.Show("現已是末條記錄");
                Num = Count - 1;
                return;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Num = Count;
            Resultinfo(Num - 1);
        }

    }
}