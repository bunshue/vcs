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


//用using就好  不用 參考/加入參考 romeo

namespace read_excel_romeo
{
    public partial class Form1 : Form
    {
        //配置Excel的OleDb連接字符串
        public const string OledbConnString = "Provider = Microsoft.Jet.OLEDB.4.0 ; Data Source = {0};Extended Properties='Excel 8.0;HDR=Yes;IMEX=1;'"; //Excel的 OleDb 連接字符串

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //C# Excel文件導入操作
            string filename = @"C:\______test_files\__RW\_excel\excel_test_data.xls";
            DataTable excelTbl = this.GetExcelTable(filename);  //調用函數獲取Excel中的信息
            if (excelTbl == null)
            {
                return;
            }

            dataGridView1.DataSource = excelTbl;


        }

        /// 
        /// 獲取Excel文件中的信息，保存到一個DataTable中
        /// 

        /// 文件路徑
        /// 返回生成的DataTable
        private DataTable GetExcelTable(string path)
        {
            try
            {
                //獲取excel數據
                DataTable dt1 = new DataTable("excelTable");
                string strConn = string.Format(OledbConnString, path);
                OleDbConnection conn = new OleDbConnection(strConn);
                conn.Open();
                DataTable dt = conn.GetSchema("Tables");
                //判斷excel的sheet頁數量，查詢第1頁
                if (dt.Rows.Count > 0)
                {
                    string selSqlStr = string.Format("select * from [{0}]", dt.Rows[0]["TABLE_NAME"]);
                    OleDbDataAdapter oleDa = new OleDbDataAdapter(selSqlStr, conn);
                    oleDa.Fill(dt1);
                }
                conn.Close();
                return dt1;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Excel轉換DataTable出錯：" + ex.Message);
                return null;
            }
        }

    }
}
