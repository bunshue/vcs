﻿using System;
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
            // TODO: 這行程式碼會將資料載入 'db_02_1DataSet.tb_Land' 資料表。您可以視需要進行移動或移除。
            this.tb_LandTableAdapter.Fill(this.db_02_1DataSet.tb_Land);

            SqlConnection con = new SqlConnection("server=(local);integrated security=sspi;database=db_02");
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