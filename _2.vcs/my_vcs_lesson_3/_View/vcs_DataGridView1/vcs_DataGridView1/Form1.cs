using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            dataGridView1.Size = new Size(800, 320);
            dataGridView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_info.Location = new Point(dataGridView1.Location.X + dataGridView1.Size.Width - bt_info.Size.Width, dataGridView1.Location.Y + dataGridView1.Size.Height - bt_info.Size.Height);

            richTextBox1.Size = new Size(800, 320);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 780);
            this.Text = "vcs_DataGridView1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            //清除DGV資料
            //dataGridView1.Rows.Clear();         //刪除row資料, 留下標題

            dataGridView1.Columns.Clear();    //刪除標題

            //clear
            //dataGridView1.DataSource = null;//設定DGV的資料來源為無, 即清除
            //dataGridView1.Invalidate();
        }

        private void bt_info_Click(object sender, EventArgs e)
        {
            /*
            richTextBox1.Text += dataGridView1.CurrentRow.Cells + "\n";
            richTextBox1.Text += dataGridView1.CurrentRow.Cells[0].Value + "\n";
            richTextBox1.Text += dataGridView1.CurrentRow.Cells[1].Value + "\n";
            richTextBox1.Text += dataGridView1.CurrentRow.Cells[2].Value + "\n";
            */
            //顯示DGV內容
            show_DataGridView_content(dataGridView1);
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

        private void dataGridView1_CellClick(object sender, DataGridViewCellEventArgs e)
        {
            richTextBox1.Text += "CellClick\n";
            richTextBox1.Text += e.ColumnIndex.ToString() + "\n";
            richTextBox1.Text += e.RowIndex.ToString() + "\n";
            if (e.RowIndex > -1)
            {
                if (dataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex].Value != null)
                {
                    dataGridView1.CurrentRow.Selected = true;
                    richTextBox1.Text += dataGridView1.Rows[e.RowIndex].Cells[e.ColumnIndex].Value + "\n";

                    //string name = dataGridView1.Rows[e.RowIndex].Cells["Name"].FormattedValue.ToString();
                    //string id = dataGridView1.Rows[e.RowIndex].Cells["Id"].FormattedValue.ToString();
                    //richTextBox1.Text += "取得資料:\t" + name + "\t" + id + "\n";
                }
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            dataGridView1.Columns.Clear();

            //設定DGV
            dataGridView1.ColumnCount = 3;
            dataGridView1.Columns[0].Name = "英文名";
            dataGridView1.Columns[0].Width = 100;//設置欄位寬度
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
            dataGridView1.Columns.Add("英文名", "英文名");//添加欄位
            dataGridView1.Columns.Add("中文名", "中文名");//添加欄位
            dataGridView1.Columns.Add("體重", "體重");//添加欄位
            dataGridView1.Columns[0].Width = 100;//設置欄位寬度
            dataGridView1.Columns[1].Width = 100;//設置欄位寬度
            dataGridView1.Columns[2].Width = 100;//設置欄位寬度
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter; //設置對其方式   此欄置中對齊

            dataGridView1.Rows.Add(new string[] { "mouse", "米老鼠", 3.ToString() });
            dataGridView1.Rows.Add(new string[] { "ox", "班尼牛", 48.ToString() });
            dataGridView1.Rows.Add(new string[] { "tiger", "跳跳虎", 33.ToString() });
        }

        private void button2_Click(object sender, EventArgs e)
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

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
        {
            Load_DataGridView_Data1();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Load_DataGridView_Data2();
        }


        void Load_DataGridView_Data1()
        {
            //設定DGV
            dataGridView1.AllowUserToAddRows = false;
            dataGridView1.AllowUserToDeleteRows = false;
            dataGridView1.ColumnCount = 4;
            dataGridView1.Columns[0].Name = "Item";
            dataGridView1.Columns[0].Width = 100;//設置欄位寬度
            dataGridView1.Columns[1].Name = "PriceEach";
            dataGridView1.Columns[1].Width = 100;//設置欄位寬度
            dataGridView1.Columns[2].Name = "Quantity";
            dataGridView1.Columns[2].Width = 100;//設置欄位寬度
            dataGridView1.Columns[3].Name = "Total";
            dataGridView1.Columns[3].Width = 100;//設置欄位寬度

            // Make some data items.
            dataGridView1.Rows.Add(new object[] { "Pencils, dozen", 1.24m, 4 });
            dataGridView1.Rows.Add(new object[] { "Paper, ream", 3.75m, 3 });
            dataGridView1.Rows.Add(new object[] { "Cookies, box", 2.17m, 12 });
            dataGridView1.Rows.Add(new object[] { "Notebook", 1.95m, 2 });
            dataGridView1.Rows.Add(new object[] { "Pencil sharpener", 12.95m, 1 });
            dataGridView1.Rows.Add(new object[] { "Paper clips, 100", 0.75m, 1 });

            // Define a column style at run time.
            DataGridViewCellStyle cell_style = new DataGridViewCellStyle();
            cell_style.BackColor = Color.LightGreen;
            cell_style.Alignment = DataGridViewContentAlignment.MiddleRight;
            cell_style.Format = "C2";
            dataGridView1.Columns[3].DefaultCellStyle = cell_style;

            // Calculate totals.
            CalculateTotals();
        }

        // Calculate the total costs and highlight totals greater than $9.99.
        private void CalculateTotals()
        {
            // Make a style for values greater than $9.99.
            DataGridViewCellStyle highlight_style = new DataGridViewCellStyle();
            highlight_style.ForeColor = Color.Red;
            highlight_style.BackColor = Color.Yellow;
            highlight_style.Font = new Font(dataGridView1.Font, FontStyle.Bold);

            // Calculate the total costs.
            foreach (DataGridViewRow row in dataGridView1.Rows)
            {
                // Calculate total cost.
                decimal total_cost = (decimal)row.Cells["PriceEach"].Value * (int)row.Cells["Quantity"].Value;

                // Display the value.
                row.Cells["Total"].Value = total_cost;

                // Highlight the cell if the vcalue is big.
                if (total_cost > 9.99m)
                {
                    row.Cells["Total"].Style = highlight_style;
                }
            }
        }

        void Load_DataGridView_Data2()
        {
            //設定DGV
            dataGridView1.AllowUserToAddRows = false;
            dataGridView1.AllowUserToDeleteRows = false;
            dataGridView1.ColumnCount = 4;
            dataGridView1.Columns[0].Name = "Item";
            dataGridView1.Columns[0].Width = 100;//設置欄位寬度
            dataGridView1.Columns[1].Name = "PriceEach";
            dataGridView1.Columns[1].Width = 100;//設置欄位寬度
            dataGridView1.Columns[2].Name = "Quantity";
            dataGridView1.Columns[2].Width = 100;//設置欄位寬度
            dataGridView1.Columns[3].Name = "Total";
            dataGridView1.Columns[3].Width = 100;//設置欄位寬度

            // Make some data items.
            OrderItem[] order_items = 
            {
                new OrderItem("Pencils, dozen", 1.24m, 4),
                new OrderItem("Cookies, box", 2.17m, 1),
                new OrderItem("Notebook", 1.95m, 2),
                new OrderItem("Paper, ream", 3.75m, 3),
                new OrderItem("Pencil sharpener", 12.95m, 1),
                new OrderItem("Paper clips, 100", 0.75m, 1),
            };

            // Add the items to the DataGridView.
            AddOrderItems(order_items);

            // Define a column style at run time.
            DataGridViewCellStyle cell_style = new DataGridViewCellStyle();
            cell_style.BackColor = Color.LightGreen;
            cell_style.Alignment = DataGridViewContentAlignment.MiddleRight;
            cell_style.Format = "C2";
            dataGridView1.Columns[3].DefaultCellStyle = cell_style;
        }

        // Add the items to the DataGridView.
        private void AddOrderItems(OrderItem[] order_items)
        {
            foreach (OrderItem item in order_items)
            {
                dataGridView1.Rows.Add(new object[]
                {
                    item.Description,item.UnitPrice,item.Quantity,item.TotalCost
                }
                );
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //建立DGV 6, 使用 CellFormatting
            SetupDataGridView();
            PopulateDataGridView();

            /*
            //新增
            this.dataGridView1.Rows.Add();

            //刪除
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != this.dataGridView1.Rows.Count - 1)
            {
                this.dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }

            //清除
            this.dataGridView1.Rows.Clear();
            */
        }

        private void dataGridView1_CellFormatting(object sender, System.Windows.Forms.DataGridViewCellFormattingEventArgs e)
        {
            if (e != null)
            {
                if (this.dataGridView1.Columns[e.ColumnIndex].Name == "Release Date")
                {
                    if (e.Value != null)
                    {
                        try
                        {
                            e.Value = DateTime.Parse(e.Value.ToString())
                                .ToLongDateString();
                            e.FormattingApplied = true;
                        }
                        catch (FormatException)
                        {
                            Console.WriteLine("{0} is not a valid date.", e.Value.ToString());
                        }
                    }
                }
            }
        }

        private void SetupDataGridView()
        {
            dataGridView1.ColumnCount = 5;

            dataGridView1.ColumnHeadersDefaultCellStyle.BackColor = Color.Navy;
            dataGridView1.ColumnHeadersDefaultCellStyle.ForeColor = Color.White;
            dataGridView1.ColumnHeadersDefaultCellStyle.Font = new Font(dataGridView1.Font, FontStyle.Bold);

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

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dataGridView1.MultiSelect = false;

            dataGridView1.CellFormatting += new DataGridViewCellFormattingEventHandler(dataGridView1_CellFormatting);
        }

        private void PopulateDataGridView()
        {
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

            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
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

        private void button11_Click(object sender, EventArgs e)
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

        private void button12_Click(object sender, EventArgs e)
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

        private void button13_Click(object sender, EventArgs e)
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

        private void button14_Click(object sender, EventArgs e)
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
            int R = dataGridView1.Rows.Count;  // 列數, 包含標題列
            for (int i = 0; i < R; i++)
            {
                dataGridView1.Rows[i].Height = 70;//设置行高度
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
            //DGV 改行列背景色
            int R = dataGridView1.Rows.Count;  // 列數, 包含標題列
            for (int i = 0; i < R; i++)
            {
                if (i % 3 == 0)
                {
                    dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.LightPink;  // 更換背景色, 列
                }
                else if (i % 3 == 1)
                {
                    dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.LightGreen;  // 更換背景色, 列
                }
                else
                {
                    dataGridView1.Rows[i].DefaultCellStyle.BackColor = Color.LightBlue;  // 更換背景色, 列
                }
            }
            /*
            int C = dataGridView1.Columns.Count;
            for (int i = 0; i < C; i++)
            {
                if (i % 3 == 0)
                {
                    dataGridView1.Columns[i].DefaultCellStyle.BackColor = Color.Red;  // 更換背景色, 欄
                }
                else if (i % 3 == 1)
                {
                    dataGridView1.Columns[i].DefaultCellStyle.BackColor = Color.Green;  // 更換背景色, 欄
                }
                else
                {
                    dataGridView1.Columns[i].DefaultCellStyle.BackColor = Color.Blue;  // 更換背景色, 欄
                }
            }
            */
            /* 一樣
            int R1 = dataGridView1.RowCount;
            int C1 = dataGridView1.ColumnCount;
            richTextBox1.Text += "欄數 : " + C1.ToString() + "\n";
            richTextBox1.Text += "列數 : " + R1.ToString() + " (包含標題)\n";

            int R2 = dataGridView1.Rows.Count;
            int C2 = dataGridView1.Columns.Count;
            richTextBox1.Text += "欄數 : " + C2.ToString() + "\n";
            richTextBox1.Text += "列數 : " + R2.ToString() + " (包含標題)\n";
            */
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //DGV 刪除
            int R = dataGridView1.Rows.Count;  // 列數, 包含標題列
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != (R - 1))
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
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        void show_DataGridView_content(DataGridView dgv)
        {
            richTextBox1.Text += "顯示 DataGridView 的內容\n";
            int R = dgv.RowCount;
            int C = dgv.ColumnCount;
            richTextBox1.Text += "欄數 : " + C.ToString() + "\n";
            richTextBox1.Text += "列數 : " + R.ToString() + " (包含標題)\n";
            richTextBox1.Text += "內容 :\n";

            for (int r = 0; r < (R - 1); r++)
            {
                richTextBox1.Text += "第" + (r + 1).ToString() + "筆 :\t";
                for (int c = 0; c < C; c++)
                {
                    //richTextBox1.Text += dataGridView1[c, r].Value + "\t";
                    //dataGridView1.Rows[r].Cells[c].Style.BackColor = Color.Red; 改變背景色
                    DataGridViewCell dgvCell = dgv[c, r];
                    richTextBox1.Text += dgvCell.Value;
                    if (c == (C - 1))
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += "\t";
                }
            }
        }

        void show_DataTable_content(DataTable dt)
        {
            richTextBox1.Text += "顯示 DataTable 的內容\n";
            int R = dt.Rows.Count;
            int C = dt.Columns.Count;
            richTextBox1.Text += "欄數 : " + C.ToString() + "\n";
            richTextBox1.Text += "列數 : " + R.ToString() + " (包含標題)\n";
            richTextBox1.Text += "TableName = " + dt.TableName + "\n";
            richTextBox1.Text += "欄位名稱 : ";
            for (int i = 0; i < C; i++)
            {
                richTextBox1.Text += dt.Columns[i] + "\t";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "內容\n";
            for (int j = 0; j < R; j++)
            {
                for (int i = 0; i < C; i++)
                {
                    richTextBox1.Text += dt.Rows[j].ItemArray[i];
                    if (i == (C - 1))
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += "\t";
                }
            }
        }

        //繪製單元格事件
        private void dataGridView1_CellPainting(object sender, DataGridViewCellPaintingEventArgs e)
        {
            //richTextBox1.Text += "------------------------------\n";  // 30個
            int R = dataGridView1.Rows.Count;  // 列數, 包含標題列
            //richTextBox1.Text += "欄數 : " + dataGridView1.Columns.Count.ToString() + "\t";
            //richTextBox1.Text += "列數 : " + dataGridView1.Rows.Count.ToString() + ", 包含標題列\n";
            //richTextBox1.Text += "列 : " + e.RowIndex.ToString() + "\t欄 : " + e.ColumnIndex.ToString() + "\n";
            //richTextBox1.Text += "CellBounds : " + e.CellBounds.ToString() + "\n";
            //richTextBox1.Text += "CellStyle : " + e.CellStyle.ToString() + "\n";
            //richTextBox1.Text += "CellStyle.Font : " + e.CellStyle.Font.ToString() + "\n";
            //richTextBox1.Text += "CellStyle.BackColor : " + e.CellStyle.BackColor.ToString() + "\n";

            if (e.Value != null)
            {
                //richTextBox1.Text += "Value : " + e.Value.ToString() + "\n";
                if (e.Value.ToString() == "48")
                {
                    e.CellStyle.BackColor = Color.Lime;
                }
            }

            //richTextBox1.Text += "Value2 : " + dataGridView1.Rows[e.RowIndex - 1].Cells[e.ColumnIndex - 1].Value.ToString() + "\n";

            /*
            dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value
            dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value.ToString()
            dataGridView1.Rows[e.RowIndex - 1].Cells[e.ColumnIndex].Value.ToString()
            */

            /* 印出DGV的內容
            int R = dataGridView1.RowCount;
            int C = dataGridView1.ColumnCount;
            richTextBox1.Text += "欄數 : " + C.ToString() + "\n";
            richTextBox1.Text += "列數 : " + R.ToString() + " (包含標題)\n";
            richTextBox1.Text += "內容 :\n";

            for (int r = 0; r < (R - 1); r++)
            {
                richTextBox1.Text += "第" + (r + 1).ToString() + "筆 :\t";
                for (int c = 0; c < C; c++)
                {
                    //richTextBox1.Text += "R = " + r.ToString() + ", C = " + c.ToString() + "\n";
                    richTextBox1.Text += dataGridView1.Rows[r].Cells[c].Value.ToString();
                    if (c == (C - 1))
                        richTextBox1.Text += "\n";
                    else
                        richTextBox1.Text += "\t";
                }
            }
            */


            /*
            richTextBox1.Text += "A";
            // 对第1列相同单元格进行合并     
            if (e.ColumnIndex == 2 && e.RowIndex != -1 || e.ColumnIndex == 3 && e.RowIndex != -1)
            {
                richTextBox1.Text += "B";
                //Brush datagridBrush = new SolidBrush(dataGridView1.GridColor);
                //SolidBrush groupLineBrush = new SolidBrush(e.CellStyle.BackColor);
                Brush datagridBrush = new SolidBrush(Color.Red);
                SolidBrush groupLineBrush = new SolidBrush(Color.Red);
                using (Pen datagridLinePen = new Pen(datagridBrush))
                {
                    // 清除单元格
                    e.Graphics.FillRectangle(groupLineBrush, e.CellBounds);
                    if (e.RowIndex < dataGridView1.Rows.Count - 1 && dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value != null && dataGridView1.Rows[e.RowIndex + 1].Cells[e.ColumnIndex].Value.ToString() != e.Value.ToString())
                    {
                        //绘制底边线
                        e.Graphics.DrawLine(datagridLinePen, e.CellBounds.Left, e.CellBounds.Bottom - 1, e.CellBounds.Right, e.CellBounds.Bottom - 1);
                        // 画右边线
                        e.Graphics.DrawLine(datagridLinePen, e.CellBounds.Right - 1, e.CellBounds.Top, e.CellBounds.Right - 1, e.CellBounds.Bottom);
                    }
                    else
                    {
                        // 画右边线
                        e.Graphics.DrawLine(datagridLinePen, e.CellBounds.Right - 1, e.CellBounds.Top, e.CellBounds.Right - 1, e.CellBounds.Bottom);
                    }
                    //对最后一条记录只画底边线
                    if (e.RowIndex == dataGridView1.Rows.Count - 1)
                    {
                        //绘制底边线
                        e.Graphics.DrawLine(datagridLinePen, e.CellBounds.Left, e.CellBounds.Bottom - 1, e.CellBounds.Right, e.CellBounds.Bottom - 1);
                    }
                    // 填写单元格内容，相同的内容的单元格只填写第一个                        
                    if (e.Value != null)
                    {
                        if (e.RowIndex > 0 && dataGridView1.Rows[e.RowIndex - 1].Cells[e.ColumnIndex].Value.ToString() == e.Value.ToString())
                        {
                        }
                        else
                        {
                            //绘制单元格内容
                            e.Graphics.DrawString(e.Value.ToString(), e.CellStyle.Font, Brushes.Black, e.CellBounds.X + 2, e.CellBounds.Y + 5, StringFormat.GenericDefault);
                        }
                    }
                    e.Handled = true;
                }
            }
            */
        }
    }

    public class OrderItem
    {
        public string Description;
        public int Quantity;
        public decimal UnitPrice, TotalCost;
        public OrderItem(string new_description, decimal new_unitprice, int new_quantity)
        {
            Description = new_description;
            UnitPrice = new_unitprice;
            Quantity = new_quantity;

            // Calculate total.
            TotalCost = UnitPrice * Quantity;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

 */


