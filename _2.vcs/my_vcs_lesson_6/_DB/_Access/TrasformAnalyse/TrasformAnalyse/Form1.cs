using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace TrasformAnalyse
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + "..//..//book.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("select * from 圖書排行", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + "..//..//book.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("transform  sum(數量) as 庫存數量 select 語言類別 from 圖書排行 where 語言類別  in( 'c','VB','java')  group by (語言類別)  pivot 分析時間", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView2.DataSource = ds.Tables[0].DefaultView;
        }
    }
}