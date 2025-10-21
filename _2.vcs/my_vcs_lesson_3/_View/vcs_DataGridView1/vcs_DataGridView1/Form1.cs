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

        void show_item_location2()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 600;
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

            richTextBox1.Size = new Size(200, 600);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

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
            dataGridView1.ColumnCount = 2;
            dataGridView1.Columns[0].Name = "中文名";
            dataGridView1.Columns[0].Width = 200;//設置欄位寬度
            dataGridView1.Columns[1].Name = "體重";
            dataGridView1.Columns[1].Width = 100;//設置欄位寬度

            //dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;//佔滿整個DGV
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.CellClick += new DataGridViewCellEventHandler(dataGridView1_CellClick);

            //填入資料
            string NAME = "米老鼠";
            string ID = "3";
            string[] row = new string[] { NAME, ID };
            dataGridView1.Rows.Add(row);
            dataGridView1.Rows.Add(new Object[] { "班尼牛", 48 });
            dataGridView1.Rows.Add(new Object[] { "跳跳虎", 33 });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建立DGV 1

            //建立二個DataColumn並設定相關欄位屬性

            DataColumn column1 = new DataColumn("ProductName");
            column1.DataType = System.Type.GetType("System.String");
            column1.AllowDBNull = true; //是否可以空白
            column1.Caption = "產品名稱";
            column1.DefaultValue = "日蝕GST";

            DataColumn column2 = new DataColumn("Price");
            column2.DataType = System.Type.GetType("System.Decimal");
            column2.AllowDBNull = true;
            column2.Caption = "價格";
            column2.DefaultValue = 0;

            DataTable table = new DataTable("Product");

            //將欄位加入表格中
            table.Columns.Add(column1);//添加欄位
            table.Columns.Add(column2);//添加欄位

            //建立二個DataRow並給定其對應欄位內容值
            DataRow row;
            row = table.NewRow();
            row["ProductName"] = "Mitsubishi Eclipse GST";
            row["Price"] = 1200000;
            table.Rows.Add(row);

            row = table.NewRow();
            row["ProductName"] = "Tigra";
            row["Price"] = 800000;
            table.Rows.Add(row);

            dataGridView1.DataSource = table;

            dataGridView1.AutoResizeColumns();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            dataGridView1.Columns.Add("Fruit", "水果");//添加欄位
            dataGridView1.Columns.Add("Price", "价格");//添加欄位
            dataGridView1.Columns[0].Width = 200;//設置欄位寬度
            dataGridView1.Columns[1].Width = 150;//設置欄位寬度
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter; //設置對其方式   此欄置中對齊

            //添加元素
            dataGridView1.Rows.Add(new string[] { "蘋果", 30.ToString() });
            dataGridView1.Rows.Add(new string[] { "橘子", 40.ToString() });
            dataGridView1.Rows.Add(new string[] { "梨子", 33.ToString() });
            dataGridView1.Rows.Add(new string[] { "水蜜桃", 31.ToString() });
        }

        private void button3_Click(object sender, EventArgs e)
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
            dataGridView1.DataSource = Points;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //可以用F2修改 DataGridView 的內容
            //可以用Tab跳欄
            //由DataTable建立DataGridView
            //似乎蠻符合DrAP之所需

            // Make the DataTable object.
            DataTable dt = new DataTable("動物資料表");

            // Add columns to the DataTable.
            dt.Columns.Add("英文名", System.Type.GetType("System.String"));
            dt.Columns.Add("中文名", System.Type.GetType("System.String"));
            dt.Columns.Add("體重", System.Type.GetType("System.Int32"));

            // Make all columns required.
            for (int i = 0; i < dt.Columns.Count; i++)
            {
                dt.Columns[i].AllowDBNull = false;
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
            dataGridView1.DataSource = dt;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //多了檢查DataGridView輸入資料內容
            //多了 DataError 事件

            // Make the DataTable object.
            DataTable dt = new DataTable("動物資料表");

            // Add columns to the DataTable.
            dt.Columns.Add("英文名", System.Type.GetType("System.String"));
            dt.Columns.Add("中文名", System.Type.GetType("System.String"));
            dt.Columns.Add("體重", System.Type.GetType("System.Int32"));

            // Make all columns required.
            for (int i = 0; i < dt.Columns.Count; i++)
            {
                dt.Columns[i].AllowDBNull = false;
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
            dataGridView1.DataSource = dt;
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

        private void button6_Click(object sender, EventArgs e)
        {
            show_item_location2();

            //設定DGV
            dataGridView1.ColumnCount = 5;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            dataGridView1.Name = "dataGridView1";
            //dataGridView1.Location = new Point(8, 8);
            //dataGridView1.Size = new Size(500, 250);
            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            dataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single;
            dataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            dataGridView1.GridColor = Color.Black;
            dataGridView1.RowHeadersVisible = false;

            dataGridView1.Columns[0].Name = "Release Date";
            dataGridView1.Columns[1].Name = "Track";
            dataGridView1.Columns[2].Name = "Title";
            dataGridView1.Columns[3].Name = "Artist";
            dataGridView1.Columns[4].Name = "Album";
            dataGridView1.Columns[4].DefaultCellStyle.Font = new Font(dataGridView1.DefaultCellStyle.Font, FontStyle.Italic);

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.MultiSelect = false;
            dataGridView1.Dock = DockStyle.Fill;

            //dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);

            //填入資料
            string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" };
            string[] row1 = { "1960", "6", "Fools Rush In", "Frank Sinatra", "Nice 'N' Easy" };
            string[] row2 = { "11/11/1971", "1", "One of These Days", "Pink Floyd", "Meddle" };
            string[] row3 = { "1988", "7", "Where Is My Mind?", "Pixies", "Surfer Rosa" };
            string[] row4 = { "5/1981", "9", "Can't Find My Mind", "Cramps", "Psychedelic Jungle" };
            string[] row5 = { "6/10/2003", "13", "Scatterbrain. (As Dead As Leaves.)", "Radiohead", "Hail to the Thief" };
            string[] row6 = { "6/30/1992", "3", "Dress", "P J Harvey", "Dry" };

            dataGridView1.Rows.Add(row0);
            dataGridView1.Rows.Add(row1);
            dataGridView1.Rows.Add(row2);
            dataGridView1.Rows.Add(row3);
            dataGridView1.Rows.Add(row4);
            dataGridView1.Rows.Add(row5);
            dataGridView1.Rows.Add(row6);

            dataGridView1.Rows.Add(new Object[] { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" });

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
            */

            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

            //DataGridViewRowCollection rows = dataGridView1.Rows;
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "在DataGridView控件做下拉式列表\n";

            //創建列對象
            DataGridViewComboBoxColumn dgvc = new DataGridViewComboBoxColumn();
            dgvc.Items.Add("蘋果");//向集合中添加元素
            dgvc.Items.Add("芒果");//向集合中添加元素
            dgvc.Items.Add("鴨梨");//向集合中添加元素
            dgvc.Items.Add("橘子");//向集合中添加元素
            dgvc.HeaderText = "水果";//設置列標題文本

            dataGridView1.Columns.Add(dgvc);//將列添加到集合
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //DataGridView 顯示序號
            //多了 RowPostPaint

            //設定 DGV
            dataGridView1.ColumnCount = 6;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            dataGridView1.Name = "dataGridView1";
            //dataGridView1.Location = new Point(8, 8);
            dataGridView1.Size = new Size(500, 250);
            dataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.DisplayedCellsExceptHeaders;
            dataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.Single;
            dataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.Single;
            dataGridView1.GridColor = Color.Black;
            dataGridView1.RowHeadersVisible = false;

            dataGridView1.Columns[0].Name = "Number";
            dataGridView1.Columns[1].Name = "Release Date";
            dataGridView1.Columns[2].Name = "Track";
            dataGridView1.Columns[3].Name = "Title";
            dataGridView1.Columns[4].Name = "Artist";
            dataGridView1.Columns[5].Name = "Album";
            dataGridView1.Columns[5].DefaultCellStyle.Font = new Font(dataGridView1.DefaultCellStyle.Font, FontStyle.Italic);

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.MultiSelect = false;
            dataGridView1.Dock = DockStyle.Fill;

            //dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(songsDataGridView_CellFormatting);

            //填入資料
            string[] row0 = { "", "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" };
            string[] row1 = { "", "1960", "6", "Fools Rush In", "Frank Sinatra", "Nice 'N' Easy" };
            string[] row2 = { "", "11/11/1971", "1", "One of These Days", "Pink Floyd", "Meddle" };
            string[] row3 = { "", "1988", "7", "Where Is My Mind?", "Pixies", "Surfer Rosa" };
            string[] row4 = { "", "5/1981", "9", "Can't Find My Mind", "Cramps", "Psychedelic Jungle" };
            string[] row5 = { "", "6/10/2003", "13", "Scatterbrain. (As Dead As Leaves.)", "Radiohead", "Hail to the Thief" };
            string[] row6 = { "", "6/30/1992", "3", "Dress", "P J Harvey", "Dry" };

            dataGridView1.Rows.Add(row0);
            dataGridView1.Rows.Add(row1);
            dataGridView1.Rows.Add(row2);
            dataGridView1.Rows.Add(row3);
            dataGridView1.Rows.Add(row4);
            dataGridView1.Rows.Add(row5);
            dataGridView1.Rows.Add(row6);

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
            */

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

        class Images
        {
            public Image Im { get; set; }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //DataGridView顯示圖片
            dataGridView1.DataSource = new List<Images>()//绑定到图片集合
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

        private void button10_Click(object sender, EventArgs e)
        {
            //建立DataTable資料並匯出到DataGridView
            DataTable dt = new DataTable();
            dt.TableName = "書籍資料";

            DataColumn dc = new DataColumn();
            dc.ColumnName = "NNNN";
            dc.DataType = typeof(int);
            dc.AllowDBNull = false;
            dc.Unique = true;       //設定 唯一值, 不能重複

            DataColumn dc2 = new DataColumn();
            dc2.ColumnName = "BBBB";
            dc2.DataType = typeof(string);

            DataColumn dc3 = new DataColumn();
            dc3.ColumnName = "AAAA";
            dc3.DataType = typeof(string);

            dt.Columns.AddRange(new DataColumn[] { dc, dc2, dc3 });

            dt.Rows.Add(new object[] { "1", "書名1", "作者1" });
            dt.Rows.Add(new object[] { "2", "書名2", "作者2" });
            dt.Rows.Add(new object[] { "3", "書名3", "作者3" });
            dt.Rows.Add(new object[] { "4", "書名4", "作者4" });
            dt.Rows.Add(new object[] { "5", "書名5", "作者5" });

            dataGridView1.DataSource = dt;
            //dataGridView1.DataBind();

            int totalColumns = dt.Columns.Count;
            richTextBox1.Text += "共有資料欄位 " + totalColumns.ToString() + " 欄\n";

            int totalRows = dt.Rows.Count;
            richTextBox1.Text += "共有資料 " + totalRows.ToString() + " 筆\n";

            //讀出來
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


        private void button11_Click(object sender, EventArgs e)
        {
            DataTable dt = new DataTable();

            dt.Columns.Add("NNNN", typeof(System.String));
            dt.Columns.Add("BBBB", typeof(System.String));
            dt.Columns.Add("AAAA", typeof(System.String));

            for (int i = 0; i < 5; i++)
            {
                DataRow dr = dt.NewRow();
                dr[0] = "編號" + (i + 1).ToString();
                dr[1] = "書名" + (i + 1).ToString();
                dr[2] = "作者" + (i + 1).ToString();

                //將上述該行加入DataTable中
                dt.Rows.Add(dr);
            }

            //綁定在sorce上
            dataGridView1.DataSource = dt;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            // Get the column titles.
            SetGridColumns(dataGridView1, 4);

            // Get the data.
            SetGridContents(dataGridView1);
        }

        // Set the grid's column names from row 1.
        private void SetGridColumns(DataGridView dgv, int max_col)
        {
            richTextBox1.Text += "設定 GDV, " + max_col.ToString() + " 欄\n";
            dataGridView1.Columns.Clear();

            string title = "AAAA";
            dgv.Columns.Add("col_" + title, title);
            title = "BBBB";
            dgv.Columns.Add("col_" + title, title);
            title = "CCCC";
            dgv.Columns.Add("col_" + title, title);
            title = "DDDD";
            dgv.Columns.Add("col_" + title, title);
        }

        // Set the grid's contents.
        private void SetGridContents(DataGridView dgv)
        {
            for (int i = 0; i < 5; i++)
            {
                object[] row_values = new object[4];
                //richTextBox1.Text += "C = " + col.ToString() + "R = " + row.ToString() + " : " + values[row, col] + "\n";
                //row_values = {"aaa", "bbb", "ccc", "ddd"};
                dgv.Rows.Add(new Object[] { "aaa", "bbb", "ccc", "ddd" });
                ///dgv.Rows.Add(row_values);
            }
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

        void print_dataGridView_data(DataGridView dgv)
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

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

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
            //dataGridView1.DataSource = null;
            //dataGridView1.Invalidate();
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //顯示DGV內容
            print_dataGridView_data(dataGridView1);
        }
    }
}
