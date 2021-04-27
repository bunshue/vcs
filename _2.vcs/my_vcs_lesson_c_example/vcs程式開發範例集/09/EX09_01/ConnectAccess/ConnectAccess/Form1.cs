using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace ConnectAccess
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\__RW\_mdb\db_09.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string ConStr = "Provider=Microsoft.Jet.OLEDB.4.0;Data source='" + filename + "'";     old
            string ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Data source='" + filename + "'";
            OleDbConnection oleCon = new OleDbConnection(ConStr);
            OleDbDataAdapter oleDap = new OleDbDataAdapter("select * from 帳目", oleCon);
            DataSet ds = new DataSet();
            oleDap.Fill(ds, "帳目");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
            oleCon.Close();
            oleCon.Dispose();
        }
    }
}