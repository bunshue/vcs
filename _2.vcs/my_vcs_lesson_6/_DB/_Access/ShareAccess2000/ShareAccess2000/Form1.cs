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
        string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09b.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string strCon = @"Provider=Microsoft.ACE.OLEDB.12.0;Data source='" + filename + "'";
            OleDbConnection OleCon = new OleDbConnection(strCon);
            OleDbDataAdapter da = new OleDbDataAdapter("select * from DB_bookinfo_mr", OleCon);
            DataSet ds = new DataSet();
            da.Fill(ds, "DB_bookinfo_mr");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}