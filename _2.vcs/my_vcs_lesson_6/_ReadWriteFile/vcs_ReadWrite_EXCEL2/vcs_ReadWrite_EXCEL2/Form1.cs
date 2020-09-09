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
            //Excel數據導入到dataGridView
            //http://weisico.com/program/2018/0531/370.html

            string path = "c:\\______test_files\\__RW\\_excel\\vcs_ReadWrite_EXCEL2.xls";

            try
            {
                string tableName = GetExcelFirstTableName(path);
                //设置T_Sql
                string TSql = "SELECT  * FROM [" + tableName + "]";
                //读取数据
                DataTable table = ExcelToDataSet(path, TSql).Tables[0];
                dataGridView1.DataSource = table;
            }
            catch (Exception ex)
            { MessageBox.Show(ex.Message); }


        }


        /// <summary>
        /// 动态取Excel表名
        /// </summary>
        /// <param name="fullPath">文件路径</param>
        /// <returns></returns>
        public static string GetExcelFirstTableName(string fullPath)
        {
            string tableName = null;
            if (File.Exists(fullPath))
            {
                using (OleDbConnection conn = new OleDbConnection("Provider=Microsoft.Jet." +
                "OLEDB.4.0;Extended Properties=Excel 8.0;Data Source=" + fullPath))
                {
                    conn.Open();
                    tableName = conn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, null).Rows[0][2].ToString().Trim();
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
