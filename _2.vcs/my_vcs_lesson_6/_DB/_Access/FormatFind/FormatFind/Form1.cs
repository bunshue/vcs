using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Linq;
using System.Data.OleDb;

namespace FormatFind
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_Test.FormatFind.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + filename + ";Persist Security Info=False");  //sugar
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + filename + ";Persist Security Info=False"); //kilo
            OleDbDataAdapter dap = new OleDbDataAdapter("SELECT * FROM 員工生日表;", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;   //將所有資料都匯出到dataGridView上

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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + filename + ";Persist Security Info=False");  //sugar
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + filename + ";Persist Security Info=False"); //kilo
            OleDbDataAdapter dap = new OleDbDataAdapter("SELECT [員工生日表].[員工姓名], 出生日期 as 格式化前出生日期,format([員工生日表].[出生日期],'yyyy年mm月dd日') AS 格式化後出生日期 FROM 員工生日表;", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}
