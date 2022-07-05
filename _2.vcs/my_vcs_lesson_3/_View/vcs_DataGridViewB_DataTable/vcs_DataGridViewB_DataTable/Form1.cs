using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataGridViewB_DataTable
{
    public partial class Form1 : Form
    {
        DataTable dt;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立DataTable資料並匯出到DataGridView
            //DataTable dt = new DataTable();
            dt = new DataTable();
            dt.TableName = "書籍資料";

            DataColumn dc = new DataColumn();
            dc.ColumnName = "編號";
            dc.DataType = typeof(int);
            dc.AllowDBNull = false;
            dc.Unique = true;       //設定 唯一值, 不能重複

            DataColumn dc2 = new DataColumn();
            dc2.ColumnName = "書名";
            dc2.DataType = typeof(string);

            DataColumn dc3 = new DataColumn();
            dc3.ColumnName = "作者/譯者";
            dc3.DataType = typeof(string);

            dt.Columns.AddRange(new DataColumn[] { dc, dc2, dc3 });

            dt.Rows.Add(new object[] { "1", "Python 技術者們：實踐!帶你一步一腳印由初學到精通(第二版)", "施威銘研究室" });
            dt.Rows.Add(new object[] { "2", "Visual C#網路程式設計：線上遊戲實作", "張逸中 李美億" });
            dt.Rows.Add(new object[] { "3", "OpenCV 3 學習手冊", "賴屹民" });
            dt.Rows.Add(new object[] { "4", "OpenCV 3 學習手冊", "賴屹民" });
            dt.Rows.Add(new object[] { "5", "OpenCV 3 學習手冊", "賴屹民" });
            dt.Rows.Add(new object[] { "6", "OpenCV 3 學習手冊", "賴屹民" });
            dt.Rows.Add(new object[] { "7", "OpenCV 3 學習手冊", "賴屹民" });
            dt.Rows.Add(new object[] { "8", "OpenCV 3 學習手冊", "賴屹民" });

            dataGridView1.DataSource = dt;
            //dataGridView1.DataBind();

            int totalColumns = dt.Columns.Count;
            richTextBox1.Text += "共有資料欄位 " + totalColumns.ToString() + " 欄\n";

            int totalRows = dt.Rows.Count;
            richTextBox1.Text += "共有資料 " + totalRows.ToString() + " 筆\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //顯示 DataTable 的內容
            show_dataset_content(dt);
        }

        //顯示 DataTable 的內容
        void show_dataset_content(DataTable dt)
        {
            richTextBox1.Text += "顯示 DataTable 的內容\n";
            if (dt == null)
            {
                richTextBox1.Text += "無資料\n";
                return;
            }

            richTextBox1.Text += "Columns = " + dt.Columns.Count.ToString() + "\n";
            richTextBox1.Text += "Rows = " + dt.Rows.Count.ToString() + "\n";
            richTextBox1.Text += "TableName = " + dt.TableName + "\n\n";

            richTextBox1.Text += "標題\n";
            int i;
            int j;
            int C = dt.Columns.Count;
            int R = dt.Rows.Count;
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i] + "\t";
            }
            richTextBox1.Text += "\n\n";

            richTextBox1.Text += "內容\n";
            for (j = 0; j < R; j++)
            {
                for (i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j].ItemArray[i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();

            dt.Columns.Add("name", typeof(System.String));
            dt.Columns.Add("sex", typeof(System.String));
            dt.Columns.Add("age", typeof(System.String));

            for (int i = 0; i < 10; i++)
            {
                DataRow dr = dt.NewRow();
                dr[0] = "aaaa";
                dr[1] = "bbbb";
                dr[2] = "cccc";

                //將上述該行加入DataTable中
                dt.Rows.Add(dr);
            }

            //綁定在sorce上
            dataGridView1.DataSource = dt;
        }
    }
}

