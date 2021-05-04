using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace ShareAccess2000
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string strCon = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=db_09.mdb";
            OleDbConnection OleCon = new OleDbConnection(strCon);
            OleDbDataAdapter da = new OleDbDataAdapter("select * from DB_bookinfo_mr", OleCon);
            DataSet ds = new DataSet();
            da.Fill(ds, "DB_bookinfo_mr");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}