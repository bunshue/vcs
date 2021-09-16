using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace ConnectionDemo3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (SqlConnection cn = new SqlConnection(Properties.Settings.Default.connString))
            {
                cn.Open();
                MessageBox.Show("連接資料庫：" + cn.Database, "Form1狀態");
            }
        }
    }
}
