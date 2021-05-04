using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.Odbc;

namespace ODBC_SQL_Server
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OdbcConnection odbcCon = new OdbcConnection("DSN=MrHywork;uid=sa;pwd=");
            try
            {
                OdbcDataAdapter odbcDat = new OdbcDataAdapter("SELECT * from 帳單", odbcCon);
                DataTable dt = new DataTable("帳單");
                odbcDat.Fill(dt);
                this.dataGridView1.DataSource = dt.DefaultView;
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}