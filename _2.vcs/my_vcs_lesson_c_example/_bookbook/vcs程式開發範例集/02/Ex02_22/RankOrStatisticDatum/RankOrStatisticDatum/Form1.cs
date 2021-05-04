using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace RankOrStatisticDatum
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            getScoure("select * from tb_05");
        }
        public void getScoure(string strName)
        {
            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02");
            con.Open();
            SqlCommand com = new SqlCommand(strName, con);
            SqlDataReader dr = com.ExecuteReader();
            listView1.View = View.Details;
            listView1.GridLines = true;
            listView1.FullRowSelect = true;
            listView1.Items.Clear();
          
            while (dr.Read())
            {
                ListViewItem lv = new ListViewItem(dr[0].ToString());
                lv.SubItems.Add(dr[1].ToString());
                lv.SubItems.Add(dr[2].ToString());
                listView1.Items.Add(lv);
            }
            dr.Close();
            con.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            getScoure("select * from tb_05  order by 銷售數量 asc");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            getScoure("select * from tb_05 order by 銷售數量 desc");
        }
 

     
  

    }
}