using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace ViewBoobooInDataSet
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=true;database=db_03");
            con.Open();
            SqlCommand com = new SqlCommand("select Count(*)from tb_01", con);
            MaxValue = (int)com.ExecuteScalar();
            con.Close();
        }
        public void Find(int first, int next)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=true;database=db_03");
            con.Open();
            DataTable dt = new DataTable();
            SqlDataAdapter da = new SqlDataAdapter("select * from tb_01", con);
            da.Fill(first, next, dt);
            if (dt.Rows[0][1].ToString() == "")
            {
                textBox1.Text = "";
                errorProvider1.SetError(textBox1, "用戶名綁定有空項");
            }
            else
            {
                errorProvider1.SetError(textBox1, "");
                textBox1.Text = dt.Rows[0][1].ToString();
            }
        }
        int MaxValue = 0;//表示表中的記錄
        int State = 1;//狀態記錄
        private void button1_Click(object sender, EventArgs e)
        {
            if (MaxValue > 0)
            {
                Find(0, 1);
                State = 1;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (State < MaxValue)
            {
                Find(State, State + 1);
                State = State + 1;
            }
        }
    }
}
