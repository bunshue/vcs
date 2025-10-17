using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

            dataGridView1.Size = new Size(400, 540);
            dataGridView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 540);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 620);
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
        }


        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //清除DGV資料
            dataGridView1.Rows.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //顯示DGV內容
        }
    }
}
