using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace PagesPrint
{
    public partial class Frm_Main : Form
    {
        int intPage = 0;//总页数
        int intRows = 0;//每页行数
        int EndRows = 0;//最后一页行数
        int currentpageindex = 1;//当前打印页
        Pen myPen = new Pen(Color.Black);
        Font myFont = new Font("宋体", 9);//字体
        Brush myBrush = new SolidBrush(Color.Black);//画刷
        int PrintPageHeight = 1169;//打印的默认高度
        int PrintPageWidth = 827;//打印的默认宽度
        int topmargin = 60; //顶边距 
        int rowgap = 0;//行高 
        int leftmargin = 50;//左边距 
        int rightmargin = 50;//右边距
        int buttommargin = 80;//底边距 
        int columnWidth1 = 57;//第一列宽度
        int columnWidth2 = 335;//第二列宽度

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            intRows = Convert.ToInt32(textBox1.Text);

            // 資料庫檔案
            string db_filename = "db_TomeTwo.MDF";
            // 查詢字串
            string sqlstr = "SELECT * FROM 員工表";

            sqlstr = "SELECT 学生姓名,所学专业,家庭住址 FROM tb_Student";

            sql_read_database(db_filename, sqlstr, dataGridView1);

            //设置每列的宽度
            dataGridView1.Columns[0].Width = 57;
            dataGridView1.Columns[1].Width = 260;
            dataGridView1.Columns[2].Width = 280;

            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "資料總數 : " + R.ToString() + " 行\n";

            EndRows = (R - 2) % intRows;//去掉标题和最后一行的空行
            if (EndRows > 0)
            {
                intPage = Convert.ToInt32((R - 2) / intRows) + 1;
            }
            else
            {
                intPage = Convert.ToInt32((R - 2) / intRows);
            }
            richTextBox1.Text += "总页数：" + intPage + "页\n";
        }

        //设置分页
        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (textBox1.Text != "")
            {
                if (e.KeyChar == 13)
                {
                    int R = dataGridView1.Rows.Count;
                    richTextBox1.Text += "資料總數 : " + R.ToString() + " 行\n";

                    intRows = Convert.ToInt32(textBox1.Text);
                    EndRows = (R - 2) % intRows;//去掉标题和最后一行的空行
                    if (EndRows > 0)
                    {
                        intPage = Convert.ToInt32((R - 2) / intRows) + 1;
                    }
                    else
                    {
                        intPage = Convert.ToInt32((R - 2) / intRows);
                    }
                    richTextBox1.Text += "每頁行數 : " + intRows.ToString() + " 行\n";
                    richTextBox1.Text += "總頁數 : " + intPage.ToString() + " 頁\n";
                }
            }
        }

        //打印
        private void button1_Click(object sender, EventArgs e)
        {
            printPreviewDialog1.ShowDialog();
        }

        //设置打印内容
        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "printDocument1_PrintPage, R = " + R.ToString() + "\n";

            if (R > 0)
            {
                PrintPageWidth = e.PageBounds.Width;//获取打印线张的宽度
                PrintPageHeight = e.PageBounds.Height;//获取打印线张的高度

                //myPen
                e.Graphics.DrawLine(Pens.Red, leftmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, topmargin);
                e.Graphics.DrawLine(Pens.Green, leftmargin, topmargin, leftmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(Pens.Blue, leftmargin, PrintPageHeight - topmargin - buttommargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(Pens.Cyan, PrintPageWidth - leftmargin - rightmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);

                //#region 打印
                int intPrintRows = currentpageindex * intRows;//当前页最后一条记录的索引
                //计算行高度
                rowgap = Convert.ToInt32((PrintPageHeight - topmargin - buttommargin - 5 * intRows) / intRows) + 3;
                int j = 0;//记录正在打印的行数
                for (int i = 0 + (intPrintRows - intRows); i < intPrintRows; i++)
                {
                    if (i <= R - 2)
                    {
                        richTextBox1.Text += "i = " + i.ToString() + "\t" + dataGridView1.Rows[i].Cells[0].Value.ToString() + "\t" +
    dataGridView1.Rows[i].Cells[1].Value.ToString() + "\t" +
    dataGridView1.Rows[i].Cells[2].Value.ToString() + "\n";

                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[0].Value.ToString(),
                            myFont, myBrush, leftmargin + 5, topmargin + j * rowgap + 5);
                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[1].Value.ToString(),
                            myFont, myBrush, leftmargin + columnWidth1 + 5, topmargin + j * rowgap + 5);
                        e.Graphics.DrawString(dataGridView1.Rows[i].Cells[2].Value.ToString(),
                            myFont, myBrush, leftmargin + columnWidth1 + columnWidth2 + 5, topmargin + j * rowgap + 5);

                        //myPen
                        e.Graphics.DrawLine(Pens.Red, leftmargin, topmargin + j * rowgap + 1,
                            PrintPageWidth - leftmargin - rightmargin, topmargin + j * rowgap + 1);
                        e.Graphics.DrawLine(Pens.Green, leftmargin + columnWidth1, topmargin +
                            j * rowgap, leftmargin + columnWidth1, PrintPageHeight - topmargin - buttommargin);
                        e.Graphics.DrawLine(Pens.Blue, leftmargin + columnWidth1 + columnWidth2,
                            topmargin + j * rowgap, leftmargin + columnWidth1 + columnWidth2, PrintPageHeight - topmargin - buttommargin);

                        e.Graphics.DrawString("共 " + intPage + " 页   第 " + currentpageindex
                            + " 页", myFont, myBrush, PrintPageWidth - 200, (int)(PrintPageHeight - buttommargin / 2));
                        j++;//记数器
                    }
                }
                currentpageindex++;//下一页的页码
                if (currentpageindex <= intPage)//如果当前页不是最后一页
                {
                    e.HasMorePages = true;//打印副页
                }
                else
                {
                    e.HasMorePages = false;//不打印副页
                    currentpageindex = 1;//当前打印的页编号设为1
                }
                //#endregion
            }
        }

        void sql_read_database(string db_filename, string sqlstr, DataGridView dgv)
        {
            string db_cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\{0};Integrated Security=True;Connect Timeout=30";

            // 連接字串
            string cnstr = string.Format(db_cnstr, db_filename);

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
    }
}
