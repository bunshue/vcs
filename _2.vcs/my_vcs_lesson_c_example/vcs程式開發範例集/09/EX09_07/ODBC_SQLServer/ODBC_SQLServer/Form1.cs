using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.Odbc;

namespace ODBC_SQLServer
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
                string odbcConStr = "driver=SQL Server;server=.;UID=sa;PWD=;database=db_09";
                OdbcConnection odbcCon = new OdbcConnection(odbcConStr);
                OdbcDataAdapter da = new OdbcDataAdapter("select * from 帳單", odbcCon);
                DataTable dt = new DataTable();
                da.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;

            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }

        }
    }
}