using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;

namespace SetPrintRange
{
    public partial class Frm_Main : Form
    {
        int intPage = 0;//总页数
        int intRows = 30;//每页行数
        int EndRows = 0;//最后一页行数
        int currentpageindex = 1;//当前打印页
        Pen myPen = new Pen(Color.Black);
        Font myFont = new Font("宋体", 9);//字体
        Brush myBrush = new SolidBrush(Color.Black);//画刷
        int PrintPageHeight = 1169;//打印的默认高度
        int PrintPageWidth = 827;//打印的默认宽度
        int topmargin = 60; //顶边距 
        int rowgap = 32;//行高 
        int leftmargin = 50;//左边距 
        int rightmargin = 50;//右边距
        int buttommargin = 80;//底边距 
        int columnWidth1 = 57;//第一列宽度
        int columnWidth2 = 335;//第二列宽度
        int page = 0;//打印指定的页
        ArrayList list = new ArrayList();//记录打印范围
        int m = 0;//定义打印范围的索引值

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //txt_Range.Text = "1,2,3-5";
            txt_Range.Text = "1-2";

            add_datagridview(dataGridView1);

            int R = dataGridView1.Rows.Count;
            EndRows = (R - 2) % intRows;//去掉标题和最后一行的空行
            if (EndRows > 0)
            {
                //计算页数
                intPage = Convert.ToInt32((R - 2) / intRows) + 1;
            }
            else
            {
                //计算页数
                intPage = Convert.ToInt32((R - 2) / intRows);
            }
            richTextBox1.Text += "資料總數 : " + (R - 2).ToString() + " 行\n";
            richTextBox1.Text += "總頁數 : " + intPage.ToString() + " 頁\n";
        }

        //标识全部打印
        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_All.Checked)
            {
                txt_Range.Enabled = false;
            }
        }

        //标识打印指定页
        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_Range.Checked)
            {
                txt_Range.Enabled = true;
                txt_Range.Focus();
            }
        }

        //打印
        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "打印1\n";
            try
            {
                if (rb_Range.Checked)//頁碼範圍
                {
                    richTextBox1.Text += "打印2 頁碼範圍 : " + txt_Range.Text + "\n";
                    if (txt_Range.Text == "")
                    {
                        MessageBox.Show("请指定要打印的页码！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        return;
                    }
                    else if (txt_Range.Text.IndexOf(",") == -1)
                    {
                        richTextBox1.Text += "aaaa\n";
                        if (txt_Range.Text.IndexOf("-") != -1)
                        {
                            richTextBox1.Text += "aaaa1111\n";
                            string[] strSubPages = txt_Range.Text.Split('-');//分割字符串
                            int intStart = Convert.ToInt32(strSubPages[0].ToString());//得到开始页码
                            int intEnd = Convert.ToInt32(strSubPages[1].ToString());//得到结束页码
                            for (int j = intStart; j <= intEnd; j++)
                            {
                                list.Add(j);//记录页码
                            }
                            list.Sort();//排序
                        }
                        else
                        {
                            richTextBox1.Text += "2222\n";
                            richTextBox1.Text += "2222 : " + int.Parse(txt_Range.Text) + "\n";
                            list.Add(int.Parse(txt_Range.Text));//记录页码
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "bbbb\n";
                        string[] strPages = txt_Range.Text.Split(',');//分割字符串
                        for (int i = 0; i < strPages.Length; i++)
                        {
                            int intStart = Convert.ToInt32(strPages[0].ToString());//得到开始页码
                            int intEnd = Convert.ToInt32(strPages[1].ToString());//得到结束页码
                            for (int j = intStart; j <= intEnd; j++)
                            {
                                list.Add(j);//记录页码
                            }
                            list.Sort();//对list集合中的元素排序
                        }
                    }
                }


                //ArrayList list = new ArrayList();//记录打印范围
                richTextBox1.Text += "打印頁數 : " + list.Count.ToString() + ", 分別是 :\n";
                for (int i = 0; i < list.Count; i++)
                {
                    richTextBox1.Text += list[i] + " ";
                }
                richTextBox1.Text += "\n";

                richTextBox1.Text += "打印3 彈出打印預覽對話框1111\n";
                printPreviewDialog1.ShowDialog();//弹出打印预览对话框
                richTextBox1.Text += "打印3 彈出打印預覽對話框2222\n";
            }
            catch (Exception ex)//捕获异常
            {
                MessageBox.Show(ex.Message, "提示");//弹出消息对话框
            }
        }

        //对打印文档进行设置
        private void printDocument1_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
        {
            int R = dataGridView1.Rows.Count;
            richTextBox1.Text += "printDocument1_PrintPage, R = " + R.ToString() + "\n";

            if (R > 0)
            {
                PrintPageWidth = e.PageBounds.Width;//获取打印线张的宽度
                PrintPageHeight = e.PageBounds.Height;//获取打印线张的高度

                // 绘制边框线
                e.Graphics.DrawLine(myPen, leftmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, topmargin);
                e.Graphics.DrawLine(myPen, leftmargin, topmargin, leftmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(myPen, leftmargin, PrintPageHeight - topmargin - buttommargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);
                e.Graphics.DrawLine(myPen, PrintPageWidth - leftmargin - rightmargin, topmargin, PrintPageWidth - leftmargin - rightmargin, PrintPageHeight - topmargin - buttommargin);

                if (rb_All.Checked)
                {
                    //打印全部                    

                    int intPrintRows = currentpageindex * intRows;//每页最后一个记录的索引

                    richTextBox1.Text += "打印全部, currentpageindex = " + currentpageindex.ToString() + "\n";
                    richTextBox1.Text += "打印全部, intRows = " + intRows.ToString() + "\n";
                    richTextBox1.Text += "打印全部, intPrintRows = " + intPrintRows.ToString() + "\n";

                    int j = 0;
                    for (int i = 0 + (intPrintRows - 30); i < intPrintRows; i++)
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
                            e.Graphics.DrawLine(Pens.Green, leftmargin + columnWidth1, topmargin + j * rowgap,
                                leftmargin + columnWidth1, PrintPageHeight - topmargin - buttommargin);
                            e.Graphics.DrawLine(Pens.Blue, leftmargin + columnWidth1 + columnWidth2,
                                topmargin + j * rowgap, leftmargin + columnWidth1 + columnWidth2,
                                PrintPageHeight - topmargin - buttommargin);

                            e.Graphics.DrawString("共 " + intPage + " 页   第 " +
                                currentpageindex + " 页", myFont, myBrush, PrintPageWidth - 200,
                                (int)(PrintPageHeight - buttommargin / 2));
                            j++;
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
                }
                else
                {
                    //打印指定的一页
                    richTextBox1.Text += "打印指定的一页 page = " + page.ToString() + "\n";
                    if (page != 0)
                    {
                        if (page <= intPage)
                        {
                            int intPrintRows = page * intRows;
                            int j = 0;
                            for (int i = 0 + (intPrintRows - 30); i < intPrintRows; i++)
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
                                    e.Graphics.DrawLine(Pens.Green, leftmargin + columnWidth1, topmargin + j * rowgap,
                                        leftmargin + columnWidth1, PrintPageHeight - topmargin - buttommargin);
                                    e.Graphics.DrawLine(Pens.Blue, leftmargin + columnWidth1 + columnWidth2, topmargin +
                                        j * rowgap, leftmargin + columnWidth1 + columnWidth2, PrintPageHeight - topmargin - buttommargin);

                                    e.Graphics.DrawString("共 " + intPage + " 页   第 " + page + " 页", myFont,
                                        myBrush, PrintPageWidth - 500, (int)(PrintPageHeight - buttommargin / 2));
                                    j++;
                                }
                            }
                        }
                        page = 0;
                    }
                    else
                    {
                        //打印指定的多页
                        richTextBox1.Text += "打印指定的多页\n";
                        if (m < list.Count)
                        {
                            int startPage = Convert.ToInt32(list[m].ToString());
                            int intPrintRows = startPage * intRows;
                            int j = 0;
                            for (int i = 0 + (intPrintRows - 30); i < intPrintRows; i++)
                            {
                                if (i <= R - 2)
                                {
                                    e.Graphics.DrawString(dataGridView1.Rows[i].Cells[0].Value.ToString(),
                                        myFont, myBrush, leftmargin + 5, topmargin + j * rowgap + 5);
                                    e.Graphics.DrawString(dataGridView1.Rows[i].Cells[1].Value.ToString(),
                                        myFont, myBrush, leftmargin + columnWidth1 + 5, topmargin + j * rowgap + 5);
                                    e.Graphics.DrawString(dataGridView1.Rows[i].Cells[2].Value.ToString(),
                                        myFont, myBrush, leftmargin + columnWidth1 + columnWidth2 + 5, topmargin + j * rowgap + 5);

                                    e.Graphics.DrawLine(myPen, leftmargin, topmargin + j * rowgap + 1,
                                        PrintPageWidth - leftmargin - rightmargin, topmargin + j * rowgap + 1);
                                    e.Graphics.DrawLine(myPen, leftmargin + columnWidth1, topmargin + j * rowgap,
                                        leftmargin + columnWidth1, PrintPageHeight - topmargin - buttommargin);
                                    e.Graphics.DrawLine(myPen, leftmargin + columnWidth1 + columnWidth2,
                                        topmargin + j * rowgap, leftmargin + columnWidth1 + columnWidth2,
                                        PrintPageHeight - topmargin - buttommargin);

                                    e.Graphics.DrawString("共 " + intPage + " 页   第 " + startPage + " 页",
                                        myFont, myBrush, PrintPageWidth - 200, (int)(PrintPageHeight - buttommargin / 2));
                                    j++;
                                }
                            }
                            m++;//下一页的页码
                            if (startPage < Convert.ToInt32(list[list.Count - 1].ToString()))//如果当前页不是最后一页
                            {
                                e.HasMorePages = true;//打印副页
                            }
                            else
                            {
                                e.HasMorePages = false;//不打印副页
                                startPage = Convert.ToInt32(list[0].ToString());//当前打印的页编号设为设置的第一页
                            }
                        }
                    }
                }
            }
            else
            {
                richTextBox1.Text += "無資料\n";
            }
        }

        void add_datagridview(DataGridView dgv)
        {
            dgv.Columns.Clear();

            //設定DGV
            dgv.ColumnCount = 3;
            dgv.Columns[0].Name = "英文名";
            dgv.Columns[0].Width = 100;//設置欄位寬度
            dgv.Columns[1].Name = "中文名";
            dgv.Columns[1].Width = 100;//設置欄位寬度
            dgv.Columns[2].Name = "體重";
            dgv.Columns[2].Width = 100;//設置欄位寬度

            for (int i = 0; i < 100; i++)
            {
                dgv.Rows.Add(new Object[] { (i + 1).ToString("D4"), "班尼牛", 48 });
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
    }
}


