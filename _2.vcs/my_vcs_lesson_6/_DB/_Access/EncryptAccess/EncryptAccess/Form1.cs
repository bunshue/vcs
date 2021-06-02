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
        string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

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
                string ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Jet OLEDB:DataBase Password='" + this.textBox1.Text + "';User Id=admin;Data source=" + filename;

                OleDbConnection oleCon = new OleDbConnection(ConStr);
                OleDbDataAdapter oleDap = new OleDbDataAdapter("select * from 帳目", oleCon);
                DataSet ds = new DataSet();
                oleDap.Fill(ds, "帳目");
                this.dataGridView1.DataSource = ds.Tables[0].DefaultView;
                oleCon.Close();
                oleCon.Dispose();
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }
    }
}
