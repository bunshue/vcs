using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Net.NetworkInformation;
using System.Data.OleDb;

namespace ConnectExcel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                string strOdbcCon = @"Provider=Microsoft.Jet.OLEDB.4.0;Persist Security Info=False;Data Source=.\2006年圖書銷售情況.xls;Extended Properties=Excel 8.0";
                OleDbConnection OleDB = new OleDbConnection(strOdbcCon);
                OleDbDataAdapter OleDat = new OleDbDataAdapter("select * from [BookSell$]", OleDB);
                DataTable dt = new DataTable();
                OleDat.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }

        }
    }
}