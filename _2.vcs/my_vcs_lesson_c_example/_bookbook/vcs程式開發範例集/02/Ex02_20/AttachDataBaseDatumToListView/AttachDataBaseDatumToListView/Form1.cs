using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace AttachDataBaseDatumToListView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

            SqlConnection con = new SqlConnection(cnstr);//"server=(local);integrated security=sspi;database=db_02");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_02",con);
            SqlDataReader dr = com.ExecuteReader();
            listView1.View = View.Details;
            listView1.FullRowSelect = true;
           
            while (dr.Read())
            {
                ListViewItem lv = new ListViewItem(dr[0].ToString());
                lv.SubItems.Add(dr[1].ToString());
                lv.SubItems.Add(dr[2].ToString());
                listView1.Items.Add(lv);
            }
            dr.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

    }
}