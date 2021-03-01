using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.OleDb;

namespace vcs_ReadWrite_EXCEL2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //sugar can not use this
            //Excel數據導入到dataGridView
            //http://weisico.com/program/2018/0531/370.html

            string filename = "c:\\______test_files\\__RW\\_excel\\vcs_ReadWrite_EXCEL2.xls";

            try
            {
                string tableName = GetExcelFirstTableName(filename);
                richTextBox1.Text += "tableName = " + tableName + "\n";
                //设置T_Sql
                string TSql = "SELECT  * FROM [" + tableName + "]";
                richTextBox1.Text += "TSql = " + TSql + "\n";
                //读取数据
                DataTable table = ExcelToDataSet(filename, TSql).Tables[0];
                dataGridView1.DataSource = table;

                int cols = table.Columns.Count;
                int rows = table.Rows.Count;
                richTextBox1.Text += "cols = " + cols.ToString() + "\n";
                richTextBox1.Text += "rows = " + rows.ToString() + "\n";
                int i;
                int j;
                for (i = 0; i < cols; i++)
                {
                    richTextBox1.Text += table.Columns[i] + "\t";
                }
                richTextBox1.Text += "\n";
                for (i = 0; i < rows; i++)
                {
                    for (j = 0; j < cols; j++)
                    {
                        richTextBox1.Text += table.Rows[i][j] + "\t";
                    }
                    richTextBox1.Text += "\n";
                }
                richTextBox1.Text += "\n";
            }
            catch (Exception ex)
            { MessageBox.Show(ex.Message); }


        }


        /// <summary>
        /// 动态取Excel表名
        /// </summary>
        /// <param name="fullPath">文件路径</param>
        /// <returns></returns>
        public string GetExcelFirstTableName(string fullPath)
        {
            string tableName = null;
            if (File.Exists(fullPath))
            {
                using (OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet." +
                "OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + fullPath))
                {
                    conn.Open();

                    richTextBox1.Text += "t0 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][0].ToString().Trim() + "\n";
                    richTextBox1.Text += "t1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][1].ToString().Trim() + "\n";

                    richTextBox1.Text += "s1 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s2 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[1][2].ToString().Trim() + "\n";
                    richTextBox1.Text += "s3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[2][2].ToString().Trim() + "\n";

                    richTextBox1.Text += "t3 = " + conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][3].ToString().Trim() + "\n";

                    richTextBox1.Text += "\n\n";

                    tableName = conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim();
                    richTextBox1.Text += "GetExcelFirstTableName tableName = " + tableName + "\n";
                }
            }
            return tableName;
        }


        /// <summary>
        /// 返回Excel数据源
        /// </summary>
        /// <param name="filename">文件路径</param>
        /// <param name="TSql">TSql</param>
        /// <returns>DataSet</returns>
        public static DataSet ExcelToDataSet(string filename, string TSql)
        {
            DataSet ds;
            string strCon = "Provider=Microsoft.Jet.OLEDB.4.0;Extended Properties=Excel 8.0;data source=" + filename;
            OleDbConnection myConn = new OleDbConnection(strCon);
            string strCom = TSql;
            myConn.Open();
            OleDbDataAdapter myCommand = new OleDbDataAdapter(strCom, myConn);
            ds = new DataSet();
            myCommand.Fill(ds);
            myConn.Close();
            return ds;
        }

    }
}
