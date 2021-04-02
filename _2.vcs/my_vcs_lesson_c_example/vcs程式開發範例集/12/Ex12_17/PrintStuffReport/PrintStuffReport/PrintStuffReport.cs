using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace PrintStuffReport
{
    public partial class PrintStuffReport : Form
    {
        public PrintStuffReport()
        {
            InitializeComponent();
        }
        SqlConnection sqlcon = new SqlConnection("Data Source=.;Database=db_12;integrated security=sspi");
        SqlDataAdapter myda;
        DataSet myds;

        private void Form1_Load(object sender, EventArgs e)
        {
            myda = new SqlDataAdapter("select * from tb_17", sqlcon);
            myds = new DataSet();
            sqlcon.Open();
            myda.Fill(myds);
            sqlcon.Close();
            dataGridView1.DataSource = myds.Tables[0];
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ExportDataGridview(dataGridView1, true);
        }

        public bool ExportDataGridview(DataGridView dgv, bool isShowWord)
        {
            Word.Document mydoc = new Word.Document();
            Word.Table mytable;
            Word.Selection mysel;
            Object myobj;
            if (dgv.Rows.Count == 0)
                return false;
            //建立Word對像
            Word.Application word = new Word.Application();
            myobj = System.Reflection.Missing.Value;
            mydoc = word.Documents.Add(ref myobj, ref myobj, ref myobj, ref myobj);
            word.Visible = isShowWord;
            mydoc.Select();
            mysel = word.Selection;
            //將數據產生Word表格文件
            mytable = mydoc.Tables.Add(mysel.Range, dgv.RowCount, dgv.ColumnCount, ref myobj, ref myobj);
            //設定列寬
            mytable.Columns.SetWidth(30, Word.WdRulerStyle.wdAdjustNone);
            //輸出列標題數據
            for (int i = 0; i < dgv.ColumnCount; i++)
            {
                mytable.Cell(1, i + 1).Range.InsertAfter(dgv.Columns[i].HeaderText);
            }
            //輸出控制元件中的記錄
            for (int i = 0; i < dgv.RowCount - 1; i++)
            {
                for (int j = 0; j < dgv.ColumnCount; j++)
                {
                    mytable.Cell(i + 2, j + 1).Range.InsertAfter(dgv[j, i].Value.ToString());
                }
            }
            return true;
        }

    }
}
