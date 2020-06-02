using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

namespace WindowsFormsApplication1eeee
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DataTable TableValue = ImportExcel("Table1");
            dataGridView1.DataSource = TableValue;
            richTextBox1.Text += "dataGridView W = " + dataGridView1.Width.ToString() + ", H = " + dataGridView1.Height.ToString() + "\n";
            richTextBox1.Text += "dataGridView R = " + dataGridView1.RowCount.ToString() + ", C = " + dataGridView1.ColumnCount.ToString() + "\n";

            richTextBox1.Text += "RowCount = " + dataGridView1.RowCount.ToString() + "\n";
            richTextBox1.Text += "ColumnCount = " + dataGridView1.ColumnCount.ToString() + "\n";
            richTextBox1.Text += "CurrentRow = " + dataGridView1.CurrentRow.Index.ToString() + "\n";
            //richTextBox1.Text += "CurrentRow = " + ds.Tables[0]. + "\n";

            richTextBox1.Text += "CurrentRow0 = " + dataGridView1.Columns[0].Name + "\n";
            richTextBox1.Text += "CurrentRow1 = " + dataGridView1.Columns[1].Name + "\n";
            //richTextBox1.Text += "CurrentRow2 = " + dataGridView1.Columns[2].Name + "\n";

            int i, j;
            for (j = 0; j < dataGridView1.RowCount; j++)
            {
                for (i = 0; i < dataGridView1.ColumnCount; i++)
                {
                    richTextBox1.Text += dataGridView1[i, j].Value + "\t";


                }
                richTextBox1.Text += "\n";

            }
            richTextBox1.Text += "\n";



        }

        public DataTable ImportExcel(string SheetName)
        {
            string windowFilter = "Excel files|*.xlsx";
            string windowTitle = "匯入Excel資料";

            OpenFileDialog openFileDialogFunction = new OpenFileDialog();
            openFileDialogFunction.Filter = windowFilter; //開窗搜尋副檔名
            openFileDialogFunction.Title = windowTitle; //開窗標題

            DataTable dataTable = new DataTable();

            if (openFileDialogFunction.ShowDialog() == DialogResult.OK)
            {
                //定義OleDb======================================================
                //1.檔案位置
                string FilePath = openFileDialogFunction.FileName;

                //2.提供者名稱  Microsoft.Jet.OLEDB.4.0適用於2003以前版本，Microsoft.ACE.OLEDB.12.0 適用於2007以後的版本處理 xlsx 檔案
                string ProviderName = "Microsoft.ACE.OLEDB.12.0;";

                //3.Excel版本，Excel 8.0 針對Excel2000及以上版本，Excel5.0 針對Excel97。
                string ExtendedString = "'Excel 8.0;";

                //4.第一行是否為標題(;結尾區隔)
                string HDR = "No;";

                //5.IMEX=1 通知驅動程序始終將「互混」數據列作為文本讀取(;結尾區隔,'文字結尾)
                string IMEX = "0';";

                //=============================================================
                //連線字串
                string connectString =
                        "Data Source=" + FilePath + ";" +
                        "Provider=" + ProviderName +
                        "Extended Properties=" + ExtendedString +
                        "HDR=" + HDR +
                        "IMEX=" + IMEX;
                //=============================================================

                using (OleDbConnection Connect = new OleDbConnection(connectString))
                {
                    Connect.Open();
                    string queryString = "SELECT * FROM [" + SheetName + "$]";
                    try
                    {
                        using (OleDbDataAdapter dr = new OleDbDataAdapter(queryString, Connect))
                        {
                            dr.Fill(dataTable);
                            //richTextBox1.Text += 
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show("異常訊息:" + ex.Message, "異常訊息");
                    }
                }
            }

            return dataTable;
        }

    }
}
