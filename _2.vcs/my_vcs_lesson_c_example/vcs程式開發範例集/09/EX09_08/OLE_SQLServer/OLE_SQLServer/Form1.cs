using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.Odbc;
using System.Data.OleDb;

namespace OLE_SQLServer
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
                string strOledbCon = "Provider=SQLOLEDB;Data Source=.; Integrated Security = SSPI;Persist Security Info=False;Initial Catalog=db_09";
                using (OleDbConnection OledbCon = new OleDbConnection())
                {
                    OledbCon.ConnectionString = strOledbCon;
                    OledbCon.Open();
                    OleDbDataAdapter OledbDat = new OleDbDataAdapter("select top 1 * from 帳單", strOledbCon);
                    DataTable dt = new DataTable();
                    OledbDat.Fill(dt);
                    this.textBox1.Text = dt.Rows[0][0].ToString().Trim();
                    this.textBox2.Text = dt.Rows[0][1].ToString().Trim();
                    this.textBox3.Text = dt.Rows[0][3].ToString().Trim();
                    this.textBox4.Text = dt.Rows[0][4].ToString().Trim();
                }
            }
            catch (Exception y)
            {
                MessageBox.Show(y.Message);
            }
           
        }
    }
}