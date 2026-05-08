using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;    //讀取Access需使用OLEDB

namespace AccessGuideExcel
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
            string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\_db_oledb\db1.mdb";
            string excel_filename = "tmp_xls_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";
            try
            {
                string table_name = "Paging";

                string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + db_filename + ";Persist Security Info=True";//記錄連接Access的語句
                OleDbConnection cn = new OleDbConnection(cnstr);//連接Access資料庫
                cn.Open();
                string sqlstr = "SELECT COUNT(*) FROM " + table_name;//設定SQL語句，取得記錄個數
                OleDbCommand cmd = new OleDbCommand(sqlstr, cn);//實例化OleDbCommand類
                int RecordCount = (int)cmd.ExecuteScalar();//執行SQL語句，並傳回結果

                //每個Sheet只能最多保存65536條記錄。
                sqlstr = @"SELECT TOP 65535 * into [Excel 8.0;database=" + excel_filename + @".xls].[Sheet1] FROM Paging";//記錄連接Excel的語句
                cmd = new OleDbCommand(sqlstr, cn);//實例化OleDbCommand類
                cmd.ExecuteNonQuery();//執行SQL語句，將數據表的內容導入到Excel中
                cn.Close();//關閉連接
                cn.Dispose();//釋放資源
                cn = null;
                richTextBox1.Text += "導入完成, 檔名 : " + excel_filename + "\n";
            }
            catch
            {
                richTextBox1.Text += "導入失敗, 目前已有Sheet1頁\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //GetTable

            string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\_db_oledb\db1.mdb";
            richTextBox1.Text += "資料庫檔案 : " + db_filename + "\n";

            string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + db_filename + ";Persist Security Info=True";
            OleDbConnection cn = new OleDbConnection(cnstr);
            cn.Open();
            DataTable tem_DataTable = cn.GetOleDbSchemaTable(OleDbSchemaGuid.Tables, new object[] { null, null, null, "TABLE" });
            cn.Close();

            richTextBox1.Text += "Access資料庫的表名 個數" + tem_DataTable.Rows.Count.ToString() + "\n";
            for (int i = 0; i < tem_DataTable.Rows.Count; i++)
            {
                richTextBox1.Text += "加入 Access資料庫的表名 : " + tem_DataTable.Rows[i][2] + "\n";
            }
        }


        //debug

        private void button3_Click(object sender, EventArgs e)
        {
            string db_filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\_db_oledb\db1.mdb";
            richTextBox1.Text += "資料庫檔案 : " + db_filename + "\n";

            string cnstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + db_filename + ";Persist Security Info=True";
            OleDbConnection cn = new OleDbConnection(cnstr);
            cn.Open();

            string sqlstr = "SELECT * FROM Paging";

            // 建構DataSet及其組成分子
            DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
            OleDbDataAdapter da = new OleDbDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
            // da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
            da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
            //dataGridView1.DataSource = ds.Tables["table"];  // DGV設置數據源, same
            dataGridView1.DataSource = ds.Tables[0];  // DGV設置數據源
            richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";
        }
    }
}
