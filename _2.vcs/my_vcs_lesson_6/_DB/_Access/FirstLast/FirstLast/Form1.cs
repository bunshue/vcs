using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.Linq;
using System.Data.OleDb;

namespace FirstLast
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db_database.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OleDbConnection olecn = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename);   //sugar
            //OleDbConnection olecn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename);   //kilo
            OleDbDataAdapter oledap = new OleDbDataAdapter("select * from tab_booksort", olecn);
            DataSet ds = new DataSet();
            oledap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;   //將所有資料都匯出到dataGridView上

            show_dataset_content(ds);   //顯示資料庫的內容
        }

        //顯示資料庫的內容 ST
        void show_dataset_content(DataSet ds)
        {
            richTextBox1.Text += "顯示資料庫的內容\n";

            richTextBox1.Text += "Tables.Count = " + ds.Tables.Count.ToString() + "\n";
            richTextBox1.Text += "Columns = " + ds.Tables[0].Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Rows = " + ds.Tables[0].Rows.Count.ToString() + "\n";
            richTextBox1.Text += "TableName = " + ds.Tables[0].TableName + "\n\n";

            richTextBox1.Text += "標題\n";
            int i;
            int j;
            int C = ds.Tables[0].Columns.Count;
            int R = ds.Tables[0].Rows.Count;
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += ds.Tables[0].Columns[i] + "\t";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "內容\n";
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += ds.Tables[0].Rows[j].ItemArray[i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }
        //顯示資料庫的內容 SP

        private void button1_Click(object sender, EventArgs e)
        {
            string strSql = "";
            if (comboBox1.Text == "第一名")
            {
                strSql = "select first(BookNames)as Bookname,first(author)as peo,first(sellsum)as slm from tab_booksort";
            }
            else
            {
                strSql = "select Last(BookNames) as Bookname,Last(author)as peo,Last(sellsum)as slm from tab_booksort";
            }
            OleDbConnection olecn = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename); //sugar
            //OleDbConnection olecn = new OleDbConnection("Provider=Microsoft.Jet.OLEDB.4.0;Data source=" + filename);   //kilo
            OleDbDataAdapter oledap = new OleDbDataAdapter(strSql, olecn);
            DataSet ds = new DataSet();
            oledap.Fill(ds);
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}

