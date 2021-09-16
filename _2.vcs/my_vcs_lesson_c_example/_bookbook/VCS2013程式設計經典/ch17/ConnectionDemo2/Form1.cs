using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace ConnectionDemo2
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
                    "AttachDbFilename=|DataDirectory|Northwind.mdf;" +
                    "Integrated Security=True";
                cn.Open();
                if (cn.State == ConnectionState.Open)
                {
                    MessageBox.Show("資料庫已連接", "目前狀態");
                }
            }
        }
    }
}
    
