using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

/*
        idx	英文名	中文名	體重
第 1筆 :  1	mouse	米老鼠	3
第 2筆 :  2	ox	    班尼牛	48
第 3筆 :  3	tiger	跳跳虎	33
第 4筆 :  4	rabbit	彼得兔	8
第 5筆 :  5	dragon	逗逗龍	38
第 6筆 :  6	snake	貪吃蛇	16
第 7筆 :  7	horse	草泥馬	31
第 8筆 :  8	goat	喜羊羊	29
第 9筆 :  9	monkey	山道猴	22
第10筆 : 10	chicken	肯德雞	5
第11筆 : 11	dog	    布丁狗	17
第12筆 : 12	pig	    佩佩豬	42
*/

namespace vcs_DataGridView1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            dataGridView1.CellMouseClick += new DataGridViewCellMouseEventHandler(dataGridView1_CellMouseClick);
            dataGridView1.RowHeaderMouseClick += new DataGridViewCellMouseEventHandler(dataGridView1_RowHeaderMouseClick);
        }

        private void dataGridView1_CellMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            //標題行上點擊右鍵，出現快捷菜單。
            //只有在 CellMouseClick 事件中才能響應右鍵
            // 判斷是否右鍵點擊
            if (e.Button == MouseButtons.Right)
            {
                // 得到點擊所在的行和列信息。相關函數查 MSDN
                DataGridView.HitTestInfo hitinfo = dataGridView1.HitTest(e.X, e.Y);
                // 如果 RowIndex < 0,就是標題行了。 
                if (hitinfo.RowIndex < 0)
                {
                    // 如果你只要指定的列顯示菜單，則加入對 hitinfo.ColumnIndex 的判斷
                    //contextMenuStrip1.Show(MousePosition.X, MousePosition.Y);
                    richTextBox1.Text += "標題行上點擊右鍵，出現快捷菜單\n";
                }
            }
        }

        private void dataGridView1_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                //加入顯示右鍵彈出菜單
                richTextBox1.Text += "標題行上點擊右鍵，出現快捷菜單   無用\n";
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 140;
            dy = 70;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            dataGridView1.Size = new Size(800, 320);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(800, 320);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 740);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            richTextBox1.Text += "CellClick\n";
            if (dataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex].Value != null)
            {
                dataGridView1.CurrentRow.Selected = true;
                string name = dataGridView1.Rows[e.RowIndex].Cells["Name"].FormattedValue.ToString();
                string id = dataGridView1.Rows[e.RowIndex].Cells["Id"].FormattedValue.ToString();

                richTextBox1.Text += "取得資料:\t" + name + "\t" + id + "\n";
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //設定DGV
            dataGridView1.ColumnCount = 3;
            dataGridView1.Columns[0].Name = "英文名";
            dataGridView1.Columns[0].Width = 200;//設置欄位寬度
            dataGridView1.Columns[1].Name = "中文名";
            dataGridView1.Columns[1].Width = 100;//設置欄位寬度
            dataGridView1.Columns[2].Name = "體重";
            dataGridView1.Columns[2].Width = 100;//設置欄位寬度

            //dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;//佔滿整個DGV
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.CellClick += new DataGridViewCellEventHandler(dataGridView1_CellClick);

            //填入資料
            string ENAME = "mouse";
            string CNAME = "米老鼠";
            string WEIGHT = "3";
            string[] row = new string[] { ENAME, CNAME, WEIGHT };
            dataGridView1.Rows.Add(row);

            dataGridView1.Rows.Add(new Object[] { "ox", "班尼牛", 48 });
            dataGridView1.Rows.Add(new Object[] { "tiger", "跳跳虎", 33 });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            dataGridView1.Columns.Clear();

            //設定DGV
            dataGridView1.Columns.Add("英文名", "英文名");
            dataGridView1.Columns.Add("中文名", "中文名");
            dataGridView1.Columns.Add("體重", "體重");

            dataGridView1.Rows.Add(new Object[] { "mouse", "米老鼠", "3" });
            dataGridView1.Rows.Add(new Object[] { "ox", "班尼牛", "48" });
            dataGridView1.Rows.Add(new Object[] { "tiger", "跳跳虎", "33" });
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //設定DGV
            dataGridView1.Columns.Add("英文名", "英文名");//添加欄位
            dataGridView1.Columns.Add("中文名", "中文名");//添加欄位
            dataGridView1.Columns.Add("體重", "體重");//添加欄位
            dataGridView1.Columns[0].Width = 200;//設置欄位寬度
            dataGridView1.Columns[1].Width = 200;//設置欄位寬度
            dataGridView1.Columns[2].Width = 150;//設置欄位寬度
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter; //設置對其方式   此欄置中對齊

            //
            dataGridView1.Rows.Add(new string[] { "mouse", "米老鼠", 3.ToString() });
            dataGridView1.Rows.Add(new string[] { "ox", "班尼牛", 48.ToString() });
            dataGridView1.Rows.Add(new string[] { "tiger", "跳跳虎", 33.ToString() });
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //設定DGV
            dataGridView1.ColumnCount = 3;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            dataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single;
            dataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            dataGridView1.GridColor = Color.Black;
            dataGridView1.RowHeadersVisible = false;

            dataGridView1.Columns[0].Name = "英文名";
            dataGridView1.Columns[1].Name = "中文名";
            dataGridView1.Columns[2].Name = "體重";
            dataGridView1.Columns[2].DefaultCellStyle.Font = new Font(dataGridView1.DefaultCellStyle.Font, FontStyle.Italic);

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.MultiSelect = false;
            //dataGridView1.Dock = DockStyle.Fill;

            //dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);

            //填入資料
            string[] row0 = { "mouse", "米老鼠", "3" };
            string[] row1 = { "ox", "班尼牛", "48" };
            string[] row2 = { "tiger", "跳跳虎", "33" };
            string[] row3 = { "rabbit", "彼得兔", "8" };
            dataGridView1.Rows.Add(row0);
            dataGridView1.Rows.Add(row1);
            dataGridView1.Rows.Add(row2);
            dataGridView1.Rows.Add(row3);

            dataGridView1.Rows.Add(new Object[] { "dragon", "逗逗龍", "38" });

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 1;
            dataGridView1.Columns[1].DisplayIndex = 2;
            dataGridView1.Columns[2].DisplayIndex = 0;
            */

            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

            //DataGridViewRowCollection rows = dataGridView1.Rows;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //DataGridView 顯示序號
            //多了 RowPostPaint

            //設定DGV
            dataGridView1.ColumnCount = 4;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            dataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single;
            dataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            dataGridView1.GridColor = Color.Black;
            dataGridView1.RowHeadersVisible = false;

            dataGridView1.Columns[0].Name = "編號";
            dataGridView1.Columns[1].Name = "英文名";
            dataGridView1.Columns[2].Name = "中文名";
            dataGridView1.Columns[3].Name = "體重";
            dataGridView1.Columns[3].DefaultCellStyle.Font = new Font(dataGridView1.DefaultCellStyle.Font, FontStyle.Italic);

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.MultiSelect = false;
            //dataGridView1.Dock = DockStyle.Fill;

            //dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);

            //填入資料
            string[] row0 = { "", "mouse", "米老鼠", "3" };
            string[] row1 = { "", "ox", "班尼牛", "48" };
            string[] row2 = { "", "tiger", "跳跳虎", "33" };
            string[] row3 = { "", "rabbit", "彼得兔", "8" };
            dataGridView1.Rows.Add(row0);
            dataGridView1.Rows.Add(row1);
            dataGridView1.Rows.Add(row2);
            dataGridView1.Rows.Add(row3);

            dataGridView1.Rows.Add(new Object[] { "", "dragon", "逗逗龍", "38" });

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 1;
            dataGridView1.Columns[1].DisplayIndex = 2;
            dataGridView1.Columns[2].DisplayIndex = 0;
            */

            //自動畫上編號
            dataGridView1.RowPostPaint += new DataGridViewRowPostPaintEventHandler(dataGridView1_RowPostPaint);
        }

        private void dataGridView1_RowPostPaint(object sender, DataGridViewRowPostPaintEventArgs e)
        {
            var dgv = sender as DataGridView;
            if (dgv != null)
            {
                Rectangle rect = new Rectangle(e.RowBounds.Location.X, e.RowBounds.Location.Y, dgv.RowHeadersWidth - 4, e.RowBounds.Height);
                TextRenderer.DrawText(e.Graphics, (e.RowIndex + 1).ToString(), dgv.RowHeadersDefaultCellStyle.Font, rect, dgv.RowHeadersDefaultCellStyle.ForeColor, TextFormatFlags.VerticalCenter | TextFormatFlags.Right);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            // 建立DataTable
            DataTable dt = new DataTable("動物資料表");

            //建立二個DataColumn並設定相關欄位屬性
            DataColumn column1 = new DataColumn("英文名");
            column1.DataType = System.Type.GetType("System.String");
            column1.AllowDBNull = true; //是否可以空白
            column1.Caption = "英文名";
            column1.DefaultValue = "----";

            DataColumn column2 = new DataColumn("中文名");
            column2.DataType = System.Type.GetType("System.String");
            column2.AllowDBNull = true; //是否可以空白
            column2.Caption = "中文名";
            column2.DefaultValue = "----";

            DataColumn column3 = new DataColumn("體重");
            column3.DataType = System.Type.GetType("System.Decimal");
            column3.AllowDBNull = true; //是否可以空白
            column3.Caption = "體重";
            column3.DefaultValue = 0;

            //將欄位加入表格中
            dt.Columns.Add(column1);//添加欄位
            dt.Columns.Add(column2);//添加欄位
            dt.Columns.Add(column3);//添加欄位

            //建立二個DataRow並給定其對應欄位內容值
            DataRow row;
            row = dt.NewRow();
            row["英文名"] = "mouse";
            row["中文名"] = "米老鼠";
            row["體重"] = 3;
            dt.Rows.Add(row);

            row = dt.NewRow();
            row["英文名"] = "ox";
            row["中文名"] = "班尼牛";
            row["體重"] = 48;
            dt.Rows.Add(row);

            dataGridView1.DataSource = dt;//設定DGV的資料來源為DataTable
            dataGridView1.AutoResizeColumns();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //可以用F2修改 DataGridView 的內容
            //可以用Tab跳欄
            //由DataTable建立DataGridView
            //似乎蠻符合DrAP之所需

            //多了檢查DataGridView輸入資料內容
            //多了 DataError 事件

            //建立DataTable
            DataTable dt = new DataTable("動物資料表");

            //將欄位加入表格中
            dt.Columns.Add("英文名", System.Type.GetType("System.String"));
            dt.Columns.Add("中文名", System.Type.GetType("System.String"));
            dt.Columns.Add("體重", System.Type.GetType("System.Int32"));

            // Make all columns required.
            for (int i = 0; i < dt.Columns.Count; i++)
            {
                dt.Columns[i].AllowDBNull = false; //是否可以空白
            }

            // 單一性
            DataColumn[] unique_cols = 
            {
                dt.Columns["英文名"],
                dt.Columns["中文名"]
            };
            dt.Constraints.Add(new UniqueConstraint(unique_cols));

            // Add items to the table.
            dt.Rows.Add(new object[] { "mouse", "米老鼠", 3 });
            dt.Rows.Add(new object[] { "ox", "班尼牛", 48 });
            dt.Rows.Add(new object[] { "tiger", "跳跳虎", 33 });
            dt.Rows.Add(new object[] { "rabbit", "彼得兔", 8 });

            // Make the DataGridView use the DataTable as its data source.
            dataGridView1.DataSource = dt;//設定DGV的資料來源為DataTable
            dataGridView1.DataError += new DataGridViewDataErrorEventHandler(dataGridView1_DataError);
        }

        // An error in the data occurred.
        private void dataGridView1_DataError(object sender, DataGridViewDataErrorEventArgs e)
        {
            // Don't throw an exception when we're done.
            e.ThrowException = false;

            // Display an error message.
            richTextBox1.Text += "輸入資料錯誤, 欄位 : " + dataGridView1.Columns[e.ColumnIndex].HeaderText + "\t原因 : " + e.Exception.Message + "\n";

            // If this is true, then the user is trapped in this cell.
            e.Cancel = false;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立DataTable資料並匯出到DataGridView

            //建立DataTable
            DataTable dt = new DataTable();
            dt.TableName = "動物資料";

            DataColumn dc = new DataColumn();
            dc.ColumnName = "編號";
            dc.DataType = typeof(int);
            dc.AllowDBNull = false; //是否可以空白
            dc.Unique = true;       //設定 唯一值, 不能重複
            DataColumn dc2 = new DataColumn();
            dc2.ColumnName = "英文名";
            dc2.DataType = typeof(string);
            DataColumn dc3 = new DataColumn();
            dc3.ColumnName = "中文名";
            dc3.DataType = typeof(string);

            //將欄位加入表格中
            dt.Columns.AddRange(new DataColumn[] { dc, dc2, dc3 });

            dt.Rows.Add(new object[] { "1", "mouse", "米老鼠" });
            dt.Rows.Add(new object[] { "2", "ox", "班尼牛" });
            dt.Rows.Add(new object[] { "3", "tiger", "跳跳虎" });
            dt.Rows.Add(new object[] { "4", "rabbit", "彼得兔" });
            dt.Rows.Add(new object[] { "5", "dragon", "逗逗龍" });

            show_DataTable_content(dt);//顯示 DataTable 的內容

            dataGridView1.DataSource = dt;//設定DGV的資料來源為DataTable
            //dataGridView1.DataBind();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立DataTable
            DataTable dt = new DataTable();

            //將欄位加入表格中
            dt.Columns.Add("編號", typeof(System.String));
            dt.Columns.Add("英文名", typeof(System.String));
            dt.Columns.Add("中文名", typeof(System.String));

            DataRow dr = dt.NewRow();
            dr[0] = "1";
            dr[1] = "mouse";
            dr[2] = "米老鼠";

            //將上述該行加入DataTable中
            dt.Rows.Add(dr);

            show_DataTable_content(dt);//顯示 DataTable 的內容

            dataGridView1.DataSource = dt;//設定DGV的資料來源為DataTable
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //DT轉DGV
            richTextBox1.Text += "將List的資料連結到 DataGridView 裏\n";

            List<Point> Points = new List<Point>();
            Points.Clear();
            int i;
            for (i = 0; i < 10; i++)
            {
                int i_st = i;
                int j_st = i * i;
                Points.Add(new Point(i_st, j_st));
            }
            dataGridView1.DataSource = Points;//設定DGV的資料來源為List<Point>
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "在DataGridView控件做下拉式列表\n";

            //創建列對象
            DataGridViewComboBoxColumn dgvc = new DataGridViewComboBoxColumn();
            dgvc.Items.Add("米老鼠");//向集合中添加元素
            dgvc.Items.Add("班尼牛");//向集合中添加元素
            dgvc.Items.Add("跳跳虎");//向集合中添加元素
            dgvc.Items.Add("彼得兔");//向集合中添加元素
            dgvc.HeaderText = "動物資料表";//設置列標題文本

            dataGridView1.Columns.Add(dgvc);//將列添加到集合
        }

        class Images
        {
            public Image Im { get; set; }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //DataGridView顯示圖片
            dataGridView1.DataSource = new List<Images>()//绑定到图片集合//設定DGV的資料來源為List<圖片>
            { 
                new Images(){Im=Image.FromFile("..//..//images//1.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//2.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//3.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//4.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//5.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//6.bmp")},
                new Images(){Im=Image.FromFile("..//..//images//7.bmp")}
            };
            dataGridView1.Columns[0].HeaderText = "图片";//设置列文本
            dataGridView1.Columns[0].Width = 70;//设置列宽度
            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {
                dataGridView1.Rows[i].Height = 70;//设置行高度
            }

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
            //DGV 隔行換色
            for (int i = 0; i < dataGridView1.Rows.Count; i++)
            {
                if (i % 2 == 0)
                {
                    dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.LightYellow;   //隔行更換背景色
                }
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //DGV 刪除
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != this.dataGridView1.Rows.Count - 1)
            {
                this.dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //DGV 跳至最後一行顯示
            dataGridView1.FirstDisplayedScrollingRowIndex = dataGridView1.RowCount - 1;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //清除DGV資料
            dataGridView1.Rows.Clear();         //刪除row資料, 留下標題

            //dataGridView1.Columns.Clear();    //刪除標題

            //clear
            //dataGridView1.DataSource = null;//設定DGV的資料來源為無, 即清除
            //dataGridView1.Invalidate();
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //顯示DGV內容
            show_DataGridView_content(dataGridView1);
        }

        void show_DataGridView_content(DataGridView dgv)
        {
            int r;
            int c;
            int rows = dgv.RowCount;
            int cols = dgv.ColumnCount;
            richTextBox1.Text += "ROWS = " + rows.ToString() + "\n";
            richTextBox1.Text += "COLS = " + cols.ToString() + "\n";
            richTextBox1.Text += "Content:\n";

            for (r = 0; r < rows; r++)
            {
                richTextBox1.Text += "r = " + r.ToString() + "\t";
                for (c = 0; c < cols; c++)
                {
                    //richTextBox1.Text += dataGridView1[c, r].Value + "\t";
                    DataGridViewCell dgvCell = dgv[c, r];
                    richTextBox1.Text += dgvCell.Value + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        void show_DataTable_content(DataTable dt)
        {
            richTextBox1.Text += "顯示 DataTable 的內容\n";

            int i;
            int j;
            int C = dt.Columns.Count;
            int R = dt.Rows.Count;

            richTextBox1.Text += "共有資料欄位 " + C.ToString() + " 欄\n";
            richTextBox1.Text += "共有資料 " + R.ToString() + " 筆\n";
            richTextBox1.Text += "TableName = " + dt.TableName + "\n\n";
            richTextBox1.Text += "欄位名稱 : ";
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i] + "\t";
            }
            richTextBox1.Text += "\n";

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
    }
}
