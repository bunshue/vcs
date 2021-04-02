using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace EncryptAccess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                string strPath = Application.StartupPath + "\\db_09.mdb";

                string ConStr = "Provider=Microsoft.Jet.OLEDB.4.0;Jet OLEDB:DataBase Password='" + this.textBox1.Text + "';User Id=admin;Data source=" + strPath;
                OleDbConnection oleCon = new OleDbConnection(ConStr);
                OleDbDataAdapter oleDap = new OleDbDataAdapter("select * from 帳目", oleCon);
                DataSet ds = new DataSet();
                oleDap.Fill(ds, "帳目");
                this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
                oleCon.Close();
                oleCon.Dispose();
            }
            catch(Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }
    }
}