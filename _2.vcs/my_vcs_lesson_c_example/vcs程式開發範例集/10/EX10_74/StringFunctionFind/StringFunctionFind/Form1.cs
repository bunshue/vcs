using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace StringFunctionFind
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + "db_Test.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("SELECT [員工生日表].[員工姓名], format([員工生日表].[出生日期],'yyyy年mm月dd日') AS 出生日期, mid([員工生日表].[出生日期],1,7) AS 出生年月 FROM 員工生日表;", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + "db_Test.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("SELECT * FROM 員工生日表;", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}