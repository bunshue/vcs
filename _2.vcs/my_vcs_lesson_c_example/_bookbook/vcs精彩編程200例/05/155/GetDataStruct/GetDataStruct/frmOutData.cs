using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.IO;
using Microsoft.Office.Interop.Excel;

namespace GetDataStruct
{
    public partial class frmOutData : Form
    {
        public frmOutData()
        {
            InitializeComponent();
        }
        public string OutData = "";
        public string OutTable = "";
        public string strserver = "";
        public string struser = "";
        public string strpwd = "";

        private void frmOutData_Load(object sender, EventArgs e)
        {
            groupBox1.Text = "數據表名稱：" + OutTable;
            try
            {
                using (SqlConnection con = new SqlConnection("Server=" + strserver + ";database=" + OutData + ";Uid=" + struser + ";Pwd=" + strpwd))
                {
                    string strSql = "select * from " + OutTable + "";
                    con.Open();
                    SqlDataAdapter da = new SqlDataAdapter(strSql, con);
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

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
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
                saveFileDialog1.Filter = "EXCEL(*.xls)|*.xls";
                if (saveFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    savePath = saveFileDialog1.FileName;
                    ExportData(dataGridView1, savePath);
                }
            }
        }
    }
}
