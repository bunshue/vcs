using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace DataReaderDemo3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch17DB.mdf;" +
                    "Integrated Security=True";
                cn.Open();
                SqlCommand cmd = new SqlCommand("SELECT * FROM 成績單", cn);
                SqlDataReader dr = cmd.ExecuteReader();
                for (int i = 0; i < dr.FieldCount; i++)
                {
                    textBox1.Text += dr.GetName(i) + "\t";
                }
                textBox1.Text += Environment.NewLine + Environment.NewLine;
                while (dr.Read())
                {
                    for (int i = 0; i < dr.FieldCount; i++)
                    {
                        textBox1.Text += dr.GetValue(i).ToString() + "\t";
                    }
                    textBox1.Text += Environment.NewLine;
                }
            }
        }
    }
}
