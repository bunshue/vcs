using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace AccessGuideExcel
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\__db\_access\db1.mdb";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = filename;
            GetTable(filename, comboBox1);

            textBox2.Text = Application.StartupPath;
        }

        public void AccessGuideJoinExcel(string Access, string AccTable, string filename)
        {
            try
            {
                string tem_sql = "";//定義字串
                string connstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + Access + ";Persist Security Info=True";//記錄連接Access的語句
                System.Data.OleDb.OleDbConnection tem_conn = new System.Data.OleDb.OleDbConnection(connstr);//連接Access資料庫
                System.Data.OleDb.OleDbCommand tem_comm;//定義OleDbCommand類
                tem_conn.Open();//打開連接的Access資料庫
                tem_sql = "select Count(*) From " + AccTable;//設定SQL語句，取得記錄個數
                tem_comm = new System.Data.OleDb.OleDbCommand(tem_sql, tem_conn);//實例化OleDbCommand類
                int RecordCount = (int)tem_comm.ExecuteScalar();//執行SQL語句，並傳回結果
                //每個Sheet只能最多保存65536條記錄。
                tem_sql = @"select top 65535 * into [Excel 8.0;database=" + filename + @".xls].[Sheet1] from Paging";//記錄連接Excel的語句
                tem_comm = new System.Data.OleDb.OleDbCommand(tem_sql, tem_conn);//實例化OleDbCommand類
                tem_comm.ExecuteNonQuery();//執行SQL語句，將數據表的內容導入到Excel中
                tem_conn.Close();//關閉連接
                tem_conn.Dispose();//釋放資源
                tem_conn = null;
                richTextBox1.Text += "導入完成, 檔名 : " + filename + "\n";
            }
            catch
            {
                richTextBox1.Text += "導入失敗, 目前已有Sheet1頁\n";
            }
        }

        public void GetTable(string Apath, ComboBox ComBox)
        {
            //string connstr = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + Apath + ";Persist Security Info=True";  //old
            string connstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + Apath + ";Persist Security Info=True";
            System.Data.OleDb.OleDbConnection tem_OleConn = new System.Data.OleDb.OleDbConnection(connstr);
            tem_OleConn.Open();
            DataTable tem_DataTable = tem_OleConn.GetOleDbSchemaTable(System.Data.OleDb.OleDbSchemaGuid.Tables, new object[] { null, null, null, "TABLE" });
            tem_OleConn.Close();
            ComBox.Items.Clear();
            for (int i = 0; i < tem_DataTable.Rows.Count; i++)
            {
                ComBox.Items.Add(tem_DataTable.Rows[i][2]);
            }
            if (ComBox.Items.Count > 0)
                ComBox.SelectedIndex = 0;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "xls_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".xls";
            textBox3.Text = filename;

            AccessGuideJoinExcel(textBox1.Text, comboBox1.Text, textBox2.Text + "\\" + filename);
        }
    }
}
