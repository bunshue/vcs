using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.OleDb;

namespace vcs_DataGridViewE
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

            dataGridView1.Size = new Size(600, 320);
            dataGridView1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(600, 320);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(920, 740);
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
            dataGridView1.Columns[0].Name = "Name";
            dataGridView1.Columns[0].Width = 200;
            dataGridView1.Columns[1].Name = "Id";
            dataGridView1.Columns[1].Width = 100;
            dataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            dataGridView1.CellClick += new DataGridViewCellEventHandler(dataGridView1_CellClick);

            //填入資料
            string NAME = "david";
            string ID = "123";

            for (int i = 0; i < 5; i++)
            {
                string[] row = new string[] { NAME, ID };
                dataGridView1.Rows.Add(row);
                //dataGridView1.Rows.Insert(0, dr.GetString(0), dr.GetString(1));
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 建立DGV 1
            dataGridView1.DataSource = MakeTable();
            dataGridView1.AutoResizeColumns();
        }

        public DataTable MakeTable()
        {
            DataTable table = new DataTable("Product");

            //建立三個DataColumn並設定相關欄位屬性
            DataColumn column1 = new DataColumn("ProductID");
            column1.DataType = System.Type.GetType("System.String");
            column1.AllowDBNull = false;
            column1.Caption = "產品編號";
            column1.DefaultValue = "Car001";

            DataColumn column2 = new DataColumn("ProductName");
            column2.DataType = System.Type.GetType("System.String");
            column2.AllowDBNull = true;
            column2.Caption = "產品名稱";
            column2.DefaultValue = "日蝕GST";

            DataColumn column3 = new DataColumn("Price");
            column3.DataType = System.Type.GetType("System.Decimal");
            column3.AllowDBNull = true;
            column3.Caption = "價格";
            column3.DefaultValue = 0;

            //將欄位加入表格中
            table.Columns.Add(column1);
            table.Columns.Add(column2);
            table.Columns.Add(column3);

            //建立二個DataRow並給定其對應欄位內容值
            DataRow row;
            row = table.NewRow();
            row["ProductID"] = "Car001";
            row["ProductName"] = "Mitsubishi Eclipse GST";
            row["Price"] = 1200000;
            table.Rows.Add(row);

            row = table.NewRow();
            row["ProductID"] = "Car002";
            row["ProductName"] = "Tigra";
            row["Price"] = 800000;
            table.Rows.Add(row);
            return table;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            create_dgv2();
        }

        class Fruit
        {
            public string Name { get; set; }
            public float Price { get; set; }
        }

        private List<Fruit> G_Fruit;

        void create_dgv2()
        {
            //DataGridView做加總和平均
            //在DataGridView控件中添加“合计”和“平均值”

            G_Fruit = new List<Fruit>() {//创建集合并添加元素
            new Fruit(){Name="苹果",Price=30},
            new Fruit(){Name="橘子",Price=40},
            new Fruit(){Name="鸭梨",Price=33},
            new Fruit(){Name="水蜜桃",Price=31}};
            dataGridView1.Columns.Add("Fruit", "水果");//添加列
            dataGridView1.Columns.Add("Pric", "价格");//添加列
            foreach (Fruit f in G_Fruit)//添加元素
            {
                dataGridView1.Rows.Add(new string[] 
                { 
                    f.Name,
                    f.Price.ToString()
                });
            }
            dataGridView1.Columns[0].Width = 200;//设置列宽度
            dataGridView1.Columns[1].Width = 170;//设置列宽度
            float sum = 0;//定义float类型变量
            G_Fruit.ForEach(
                (pp) =>
                {
                    sum += pp.Price;//求和
                });
            dataGridView1.Rows.Add(new string[] //在新列中显示平均值及合计信息
            { 
                "合计： "+sum.ToString()+" 元",
                "平均价格： "+(sum/G_Fruit.Count).ToString()+" 元"
            });
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //List oledb providers in DataGridView
            fill_DataGridView();
        }

        void fill_DataGridView()
        {
            OleDbEnumerator enumerator = new OleDbEnumerator();
            dataGridView1.DataSource = enumerator.GetElements();
            foreach (DataGridViewColumn col in dataGridView1.Columns)
            {
                col.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            dataGridView1.ColumnCount = 2;
            dataGridView1.Columns[0].Name = "品名";
            dataGridView1.Columns[1].Name = "單價";

            dataGridView1.Rows.Add(new Object[] { "紅茶", 25 });
            dataGridView1.Rows.Add(new Object[] { "綠茶", 25 });
            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //綁定數據集合
            dataGridView1.DataSource = new List<Fruit>()
            {
            new Fruit(){Name="蘋果",Price=30},
            new Fruit(){Name="橘子",Price=40},
            new Fruit(){Name="梨子",Price=33},
            new Fruit(){Name="水蜜桃",Price=31}
            };
            dataGridView1.Columns[0].Width = 200;
            dataGridView1.Columns[1].Width = 170;

            dataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;  //設置如何選中單元格 整行一起選取
            dataGridView1.Columns[0].DefaultCellStyle.Alignment = DataGridViewContentAlignment.MiddleCenter; //設置對其方式   此欄置中對齊
        }

        private void button6_Click(object sender, EventArgs e)
        {
            load_data();


            //int index = dataGridView1.Rows.Add();
            //dataGridView1.Rows[index].Cells[0].Value = "123456";

            string[] row0 = { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" };
            dataGridView1.Rows.Add(row0);

            //DataGridViewRowCollection rows = dataGridView1.Rows;
            //rows.Add(new Object[] { "11/22/1968", "29", "Revolution 9", "Beatles", "The Beatles [White Album]" });

        }

        void load_data()
        {
            SetupDataGridView();        //設定DGV
            PopulateDataGridView();     //填入資料
        }

        private void SetupDataGridView()
        {
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

            int i;
            for (i = 0; i < 10; i++)
            {
                dataGridView1.Rows.Add(row0);
                dataGridView1.Rows.Add(row1);
                dataGridView1.Rows.Add(row2);
                dataGridView1.Rows.Add(row3);
                dataGridView1.Rows.Add(row4);
                dataGridView1.Rows.Add(row5);
                dataGridView1.Rows.Add(row6);
            }

            /*
            //dataGridView 顯示欄排序
            dataGridView1.Columns[0].DisplayIndex = 3;
            dataGridView1.Columns[1].DisplayIndex = 4;
            dataGridView1.Columns[2].DisplayIndex = 0;
            dataGridView1.Columns[3].DisplayIndex = 1;
            dataGridView1.Columns[4].DisplayIndex = 2;
            */
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
            //DT轉DGV
            richTextBox1.Text += "將List的資料連結到 DataGridView 裏\n";

            List<Point> Points = new List<Point>();
            Points.Clear();

            int i;
            Random r = new Random();
            for (i = 0; i < 10; i++)
            {
                int i_st = r.Next(10);
                int j_st = r.Next(10);
                Points.Add(new Point(i_st, j_st));
                richTextBox1.Text += "i_st = " + i_st.ToString() + "\t" + "j_st = " + j_st.ToString() + "\n";
            }

            printList(Points);

            dataGridView1.DataSource = Points;

        }

        void printList(List<Point> pts)
        {
            int len = pts.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += pts[i].ToString() + "\n";
            }
        }


        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
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

        private void button12_Click(object sender, EventArgs e)
        {
            //DGV 刪除
            if (this.dataGridView1.SelectedRows.Count > 0 && this.dataGridView1.SelectedRows[0].Index != this.dataGridView1.Rows.Count - 1)
            {
                this.dataGridView1.Rows.RemoveAt(this.dataGridView1.SelectedRows[0].Index);
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //DGV 跳至最後一行顯示
            dataGridView1.FirstDisplayedScrollingRowIndex = dataGridView1.RowCount - 1;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //清除DGV資料
            dataGridView1.Rows.Clear();         //刪除row資料, 留下標題

            //dataGridView1.Columns.Clear();    //刪除標題

            //clear
            //dataGridView1.DataSource = null;
            //dataGridView1.Invalidate();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //顯示DGV內容
            print_dataGridView_data(dataGridView1);
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
    }
}
