using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_05_Print3
{
    public partial class Form1 : Form
    {
        //使用DGV1 ST
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
        //使用DGV1 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //使用DGV1 ST
            intRows = Convert.ToInt32(textBox1.Text);

            add_datagridview(dataGridView1);

            //設置欄位寬度
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

            //使用DGV1 SP

        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 280 + 10;

            groupBox0.Size = new Size(200, 280);
            groupBox1.Size = new Size(200, 280);
            groupBox2.Size = new Size(200, 280);
            groupBox3.Size = new Size(200, 280);
            groupBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            groupBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            groupBox4.Size = new Size(410, 70);
            groupBox4.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            dataGridView1.Size = new Size(410, 400);
            dataGridView1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            groupBox5.Size = new Size(410, 100);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1+100);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1300, 750);
            this.Text = "vcs_test_all_05_Print3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button00_Click(object sender, EventArgs e)
        {

        }

        private void button01_Click(object sender, EventArgs e)
        {

        }

        private void button02_Click(object sender, EventArgs e)
        {

        }

        private void button03_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

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

            for (int i = 0; i < 23; i++)
            {
                dgv.Rows.Add(new Object[] { (i + 1).ToString("D4"), "班尼牛", 48 });
            }
        }

        //設置打印內容
        private void printDocument_dgv_PrintPage(object sender, System.Drawing.Printing.PrintPageEventArgs e)
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

        private void bt_dgv_print_Click(object sender, EventArgs e)
        {
            printPreviewDialog_dgv.ShowDialog();
        }

        // 設置分頁
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

        //------------------------------------------------------------  # 60個

        private void bt_dgv_print2_Click(object sender, EventArgs e)
        {

        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/



