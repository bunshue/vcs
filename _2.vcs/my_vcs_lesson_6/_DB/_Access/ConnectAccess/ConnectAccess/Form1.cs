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
        string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_09.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;  //sugar
            string ConStr = "Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename;     //kilo
            OleDbConnection Olecon = new OleDbConnection(ConStr);
            OleDbDataAdapter OleDat = new OleDbDataAdapter("select * from 帳目", Olecon);
            DataSet ds = new DataSet();
            OleDat.Fill(ds, "帳目");
            this.dataGridView1.DataSource = ds.Tables[0].DefaultView;   //將所有資料都匯出到dataGridView上

            //顯示資料庫的內容 ST
            richTextBox1.Text += "顯示資料庫的內容\n";
            richTextBox1.Text += "Columns = " + ds.Tables[0].Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Rows = " + ds.Tables[0].Rows.Count.ToString() + "\n";
            richTextBox1.Text += "TableName = " + ds.Tables[0].TableName + "\n";
            int i;
            int j;
            int C = ds.Tables[0].Columns.Count;
            int R = ds.Tables[0].Rows.Count;
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += ds.Tables[0].Columns[i] + "\t";
            }
            richTextBox1.Text += "\n";
            
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[j].ItemArray[i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
            //顯示資料庫的內容 SP

            Olecon.Close();
            Olecon.Dispose();
        }
    }
}

