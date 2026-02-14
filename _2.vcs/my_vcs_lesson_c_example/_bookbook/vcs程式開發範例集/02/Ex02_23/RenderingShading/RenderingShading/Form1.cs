using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace RenderingShading
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {           
           listView1.BackgroundImageTiled = true;
            listView1.View = View.LargeIcon;
            listView1.LargeImageList = imageList1;
         //   listView1.BackgroundImage = imageList1.Images[1];

            string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";
            SqlConnection con = new SqlConnection(cnstr);//"server=(local);integrated security=sspi;database=db_02");
            con.Open();
            SqlCommand com = new SqlCommand("select * from tb_06", con);
            listView1.Items.Clear();
            SqlDataReader dr = com.ExecuteReader();
            while (dr.Read())
            {
                ListViewItem lv = new ListViewItem(dr[1].ToString(),0);
                listView1.Items.Add(lv);
            }
            dr.Close();
            con.Close();
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void listView1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }        
    }
}