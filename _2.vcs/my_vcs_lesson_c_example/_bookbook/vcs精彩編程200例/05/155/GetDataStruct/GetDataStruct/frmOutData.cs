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
using Microsoft.Office.Interop.Excel;

namespace GetDataStruct
{
    public partial class frmOutData : Form
    {
        public string OutData = "";
        public string OutTable = "";
        public string strserver = "";
        public string struser = "";
        public string strpwd = "";

        public frmOutData()
        {
            InitializeComponent();
        }

        private void frmOutData_Load(object sender, EventArgs e)
        {
            //導出數據

            string table_name = "animals1_table";

            richTextBox1.Text += "數據表名稱：" + table_name + "\n";

            try
            {
                using (SqlConnection con = new SqlConnection("Server=" + strserver + ";database=" + OutData + ";Uid=" + struser + ";Pwd=" + strpwd))
                {
                    string sqlstr = "select * from " + table_name + "";
                    con.Open();
                    SqlDataAdapter da = new SqlDataAdapter(sqlstr, con);
                    System.Data.DataTable dt = new System.Data.DataTable();
                    da.Fill(dt);
                    this.dataGridView1.DataSource = dt.DefaultView;
                    con.Close();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "警告", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        public void ExportData(DataGridView srcDgv, string fileName)//導出數據,傳入一個datagridview和一個文件路徑
        {
            string type = fileName.Substring(fileName.IndexOf(".") + 1);//獲得數據類型
            if (type.Equals("xls", StringComparison.CurrentCultureIgnoreCase))//Excel文檔
            {
                Microsoft.Office.Interop.Excel.Application excel = new Microsoft.Office.Interop.Excel.Application();
                try
                {
                    excel.DisplayAlerts = false;
                    excel.Workbooks.Add(true);
                    excel.Visible = false;
                    for (int i = 0; i < srcDgv.Columns.Count; i++)//設置標題
                    {
                        excel.Cells[2, i + 1] = srcDgv.Columns[i].HeaderText;
                    }
                    for (int i = 0; i < srcDgv.Rows.Count; i++)//填充數據
                    {
                        for (int j = 0; j < srcDgv.Columns.Count; j++)
                        {
                            if (srcDgv[j, i].ValueType.ToString() == "System.Byte[]")
                            {
                                excel.Cells[i + 3, j + 1] = "System.Byte[]";
                            }
                            else
                            {
                                excel.Cells[i + 3, j + 1] = srcDgv[j, i].Value;
                            }
                        }
                    }
                    excel.Workbooks[1].SaveCopyAs(fileName);//保存
                }
                finally
                {
                    excel.Quit();
                }
                return;
            }

            //保存Word文件
            if (type.Equals("doc", StringComparison.CurrentCultureIgnoreCase))
            {
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
                            string a = srcDgv[j, i].ValueType.ToString();
                            if (a == "System.Byte[]")
                            {
                                PictureBox pp = new PictureBox();
                                byte[] pic = (byte[])(srcDgv[j, i].Value); //將數據庫中的圖片轉換成二進制流
                                MemoryStream ms = new MemoryStream(pic);	//將字節數組存入到二進制流中
                                pp.Image = Image.FromStream(ms);           //二進制流Image控件中顯示
                                pp.Image.Save(@"C:\wxk.bmp");               //將圖片存入到指定的路徑
                                object aaa = table.Cell(i + 2, j + 1).Range;
                                wordApp.Selection.ParagraphFormat.Alignment = Microsoft.Office.Interop.Word.WdParagraphAlignment.wdAlignParagraphCenter;
                                wordApp.Selection.InlineShapes.AddPicture(@"C:\wxk.bmp", ref none, ref none, ref aaa);
                                pp.Dispose();
                            }
                            else
                            {
                                table.Cell(i + 2, j + 1).Range.Text = srcDgv[j, i].Value.ToString();
                            }
                        }
                    }
                    document.SaveAs(ref path, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none, ref none);
                    document.Close(ref none, ref none, ref none);
                    if (File.Exists(@"C:\wxk.bmp"))
                    {
                        File.Delete(@"C:\wxk.bmp");
                    }
                }
                finally
                {
                    wordApp.Quit(ref none, ref none, ref none);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //word
            string doc_filename = "tmp_aaaa.doc";
            ExportData(dataGridView1, doc_filename);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //excel
            string excel_filename = "tmp_aaaa.xls";
            ExportData(dataGridView1, excel_filename);
        }

        //debug -------------------------------------------------------------------------------------------------------------

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
    }
}
