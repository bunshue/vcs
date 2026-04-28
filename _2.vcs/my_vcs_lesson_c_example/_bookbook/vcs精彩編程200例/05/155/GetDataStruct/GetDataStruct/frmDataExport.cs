using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Data.SqlClient;

namespace GetDataStruct
{
    public partial class frmDataExport : Form
    {
        public string OutData = "";
        public string OutTable = "";
        public string strserver = "";
        public string struser = "";
        public string strpwd = "";

        public frmDataExport()
        {
            InitializeComponent();
        }

        private void frmDataExport_Load(object sender, EventArgs e)
        {
            //導出表結構
       }

        private void SaveAs() //導出成Excel
        {
            richTextBox1.Text += "匯出到 EXCEL\n";
            /*
            SaveFileDialog saveFileDialog = new SaveFileDialog();
            saveFileDialog.Filter = "Execl files (*.xls)|*.xls";
            saveFileDialog.FilterIndex = 0;
            saveFileDialog.RestoreDirectory = true;
            saveFileDialog.CreatePrompt = true;
            saveFileDialog.Title = "Export Excel File To";
            saveFileDialog.ShowDialog();
            */
            string tmp_excel_filename = "tmp_aaaa.xls";
            FileStream filestream = File.Open(tmp_excel_filename, FileMode.Create);
            StreamWriter sw = new StreamWriter(filestream, System.Text.Encoding.GetEncoding(-0));
            string str = "";
            try
            {
                //寫標題
                for (int i = 0; i < dataGridView1.ColumnCount; i++)
                {
                    if (i > 0)
                    {
                        str += "\t";
                    }
                    str += dataGridView1.Columns[i].HeaderText;
                }
                sw.WriteLine(str);
                //寫內容
                for (int j = 0; j < dataGridView1.Rows.Count; j++)
                {
                    string tempStr = "";
                    for (int k = 0; k < dataGridView1.Columns.Count; k++)
                    {
                        if (k > 0)
                        {
                            tempStr += "\t";
                        }
                        tempStr += dataGridView1.Rows[j].Cells[k].Value.ToString();
                    }
                    sw.WriteLine(tempStr);
                }
                sw.Close();
            }
            catch (Exception e)
            {
                MessageBox.Show(e.ToString());
            }
            finally
            {
                sw.Close();
            }
        }

        public void ExportData(DataGridView srcDgv, string fileName)//導出數據,傳入一個datagridview和一個文件路徑
        {
            string type = fileName.Substring(fileName.IndexOf(".") + 1);//獲得數據類型
            if (type.Equals("xls", StringComparison.CurrentCultureIgnoreCase))//Excel文檔
            {
                SaveAs();
            }

            //保存Word文件
            if (type.Equals("doc", StringComparison.CurrentCultureIgnoreCase))
            {

                richTextBox1.Text += "匯出到 WORD\n";

                object path = fileName;
                Object none = System.Reflection.Missing.Value;
                Microsoft.Office.Interop.Word.Application wordApp = new Microsoft.Office.Interop.Word.Application();
                Microsoft.Office.Interop.Word.Document document = wordApp.Documents.Add(ref none, ref none, ref none, ref none);
                //建立表格
                Microsoft.Office.Interop.Word.Table table = document.Tables.Add(document.Paragraphs.Last.Range, srcDgv.Rows.Count + 1, srcDgv.Columns.Count, ref none, ref none);
                try
                {
                    for (int i = 0; i < srcDgv.Columns.Count; i++)//設置標題
                    {
                        table.Cell(1, i + 1).Range.Text = srcDgv.Columns[i].HeaderText;
                    }
                    for (int i = 0; i < srcDgv.Rows.Count; i++)//填充數據
                    {
                        for (int j = 0; j < srcDgv.Columns.Count; j++)
                        {

                            table.Cell(i + 2, j + 1).Range.Text = srcDgv[j, i].Value.ToString();
                        }
                    }
                    document.SaveAs(ref path, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none);
                }
                finally
                {
                    wordApp.Quit(ref none, ref none, ref none);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string savePath = "";
            if (radioButton1.Checked == true)
            {
                saveFileDialog1.Filter = "WORD(*.doc)|*.doc";
                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    savePath = saveFileDialog1.FileName;
                    ExportData(dataGridView1, savePath);
                }
            }

            if (radioButton2.Checked == true)
            {
                SaveAs();
            }
        }




        string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);
            richTextBox1.Text += cnstr + "\n";

            //讀取資料庫至DGV
            try
            {
                using (SqlConnection cn = new SqlConnection(cnstr))  // 建立資料庫連接對象cn
                {
                    SqlDataAdapter da = new SqlDataAdapter(sqlstr, cn);  // 建立資料庫適配器對象da
                    DataSet ds = new DataSet();  // 建立數據集ds, 準備給da用來填充數據(Table格式)
                    da.Fill(ds);  // da將查詢的結果填充至數據集ds, 不指定TableName
                    //da.Fill(ds, "table");  // da將查詢的結果填充至數據集ds, 指定TableName為"table"
                    dgv.DataSource = ds.Tables[0].DefaultView;  // DGV設置數據源
                    //dgv.DataSource = ds.Tables[0];  // DGV設置數據源, same
                    richTextBox1.Text += "取得資料 : " + ds.Tables[0].Rows.Count.ToString() + " 筆\n";

                    /*
                    //也可改成用 DataTable
                    DataTable dt = new DataTable();//创建数据表
                    da.Fill(dt);//填充数据表
                    dgv.DataSource = dt;
                    */
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {

            // 資料庫檔案
            string db_filename = "animals1_db.mdf";
            // 查詢字串
            string sqlstr = "SELECT * FROM animals1_table";

            sql_read_database(db_filename, sqlstr, dataGridView1);


        }

        private void button4_Click(object sender, EventArgs e)
        {
            //匯出到 WORD
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //匯出到 EXCEL

        }
    }
}
