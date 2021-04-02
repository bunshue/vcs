using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace EstimateDataRepeat
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //連接資料庫的字串
        string connstr = "Provider=SQLOLEDB;Data Source=.; Integrated Security = SSPI;Persist Security Info=False;Initial Catalog=db_09";
        public int isHomologyNote(string Table, string term1, string term2, string Value1, string Value2)
        {
            string tem_sql = "";//定義字串變數
            System.Data.OleDb.OleDbConnection tem_conn = new System.Data.OleDb.OleDbConnection(connstr);//連接資料庫
            System.Data.OleDb.OleDbCommand tem_comm;//定義OleDbCommand類
            tem_conn.Open();//打開資料庫的連接
            //設定SQL語句，尋找要新增的記錄
            tem_sql = "select top 1 * From " + Table + " where " + term1 + " = '" + Value1 + "' and " + term2 + " = '" + Value2 + "'";
            tem_comm = new System.Data.OleDb.OleDbCommand(tem_sql, tem_conn);//執行SQL語句
            int RecordCount = 0;//定義變數
            if (tem_comm.ExecuteScalar() == null)//如果查詢為空
                RecordCount = 0;
            else
                RecordCount = (int)tem_comm.ExecuteScalar();//傳回尋找結果的個數
            tem_conn.Close();//關閉連接
            tem_comm.Dispose();//釋放資源
            tem_conn.Dispose();//釋放資源
            return RecordCount;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (isHomologyNote("tb_BasicTable", "Number", "Name", textBox1.Text, textBox2.Text) > 0)//如果查詢結果大於0
                MessageBox.Show("已有重複記錄");//彈出提示框
            else//可以對該記錄進行新增
                MessageBox.Show("無記錄，可以新增");
        }
    }
}
