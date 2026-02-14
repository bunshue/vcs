using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace UsageBindingControlAchieveSelect
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_Land", con);
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {
                this.listBox1.Items.Add(dr[1].ToString());
            }
            dr.Close();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem.ToString() != null)
            {
                textBox2.Text = listBox1.SelectedItem.ToString();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
        }

        private void listBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem.ToString() != null)
            {
                textBox2.Text = listBox1.SelectedItem.ToString();
            }
        }
    }
}
