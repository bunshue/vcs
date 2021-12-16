using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataTable1
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
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

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

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0+50);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立DataTable 1
            //1.創建表實例
            DataTable dt = new DataTable();
            dt=create_data_table1(dt);

            show_data_table(dt);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt=create_data_table2(dt);

            show_data_table(dt);
        }

        DataTable create_data_table1(DataTable dt)
        {
            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.創建新行
            DataRow dr1 = dt.NewRow();
            DataRow dr2 = dt.NewRow();
            DataRow dr3 = dt.NewRow();

            //4.為新行賦值 並 添加到DataTable
            dr1[0] = "1";
            dr1[1] = "david";
            dr1[2] = "100";
            dt.Rows.Add(dr1);

            dr2[0] = "5";
            dr2[1] = "john";
            dr2[2] = "80";
            dt.Rows.Add(dr2);

            dr3[0] = "12";
            dr3[1] = "mary";
            dr3[2] = "92";
            dt.Rows.Add(dr3);

            return dt;
        }

        DataTable create_data_table2(DataTable dt)
        {
            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.添加新行
            dt.Rows.Add("1", "david", "100");
            dt.Rows.Add("5", "john", "80");
            dt.Rows.Add("12", "mary", "92");
            return dt;
        }

        void show_data_table(DataTable dt)
        {
            int rows = dt.Rows.Count;
            int cols = dt.Columns.Count;

            //richTextBox1.Text += "直行 = " + cols.ToString() + "\n";
            //richTextBox1.Text += "橫列 = " + rows.ToString() + "\n";

            int i;
            int j;

            for (i = 0; i < cols; i++)
            {
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }
            richTextBox1.Text += "\n";

            for (j = 0; j < rows; j++)
            {
                for (i = 0; i < cols; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i] + "\t";
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table2(dt);

            show_data_table(dt);

            string xml_data = DataTableToXml(dt);
            richTextBox1.Text += "DataTable轉XML\n" + xml_data + "\n";
        }

        public string DataTableToXml(DataTable dt)
        {
            StringBuilder strXml = new StringBuilder();
            strXml.AppendLine("<XmlTable>");
            for (int i = 0; i < dt.Rows.Count; i++)
            {
                strXml.AppendLine("<rows>");
                for (int j = 0; j < dt.Columns.Count; j++)
                {
                    strXml.AppendLine("<" + dt.Columns[j].ColumnName + ">" + dt.Rows[i][j] + "</" + dt.Columns[j].ColumnName + ">");
                }
                strXml.AppendLine("</rows>");
            }
            strXml.AppendLine("</XmlTable>");
            return strXml.ToString();
        }


        private void button3_Click(object sender, EventArgs e)
        {
            DataTable dt = null;
            dt = new DataTable();
            dt.Columns.Add("A", typeof(bool));
            dt.Columns.Add("B", typeof(bool));
            dt.Columns.Add("C", typeof(bool));
            dt.Rows.Add(checkBox1.Checked, checkBox2.Checked, checkBox3.Checked);

            string result = string.Format("A: {0}\r\nB: {1}\r\nC: {2}", dt.Rows[0]["A"], dt.Rows[0]["B"], dt.Rows[0]["C"]);
            richTextBox1.Text += result + "\n";
            show_data_table(dt);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int i;
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();
            dt = create_data_table2(dt);

            richTextBox1.Text += "原DataTable :\n";
            show_data_table(dt);

            richTextBox1.Text += "由 姓名 項列出資料\n";
            int rows = dt.Rows.Count;
            for (i = 0; i < rows; i++)
            {
                richTextBox1.Text += "找到\t" + dt.Rows[i]["姓名"].ToString() + "\n";
            }

            richTextBox1.Text += "刪除第1項後DataTable :\n";
            dt.Rows.RemoveAt(1);
            show_data_table(dt);

            richTextBox1.Text += "由 姓名 項列出資料\n";
            rows = dt.Rows.Count;
            for (i = 0; i < rows; i++)
            {
                richTextBox1.Text += "找到\t" + dt.Rows[i]["姓名"].ToString() + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //DataTable用法

            DataTable dt = new DataTable();

            richTextBox1.Text += "建立DataTable, 填入資料\n";

            dt = create_datatable_data();


            richTextBox1.Text += "顯示DataTable資料a\n";
            int i;
            for (i = 0; i < 10; i++)
            {
                richTextBox1.Text += dt.Rows[i][0].ToString() + "\n";

            }

            richTextBox1.Text += "顯示DataTable資料b\n";
            ShowData(dt);
        }

        public DataTable create_datatable_data()
        {
            DataTable table = new DataTable();
            table.Columns.Add("Col");
            string data = string.Empty;
            for (int i = 0; i < 10; i++)
            {
                data = "DT資料 " + i.ToString();
                table.Rows.Add(data);
                richTextBox1.Text += "加入資料 : " + data + "\n";
            }
            return table;
        }

        public List<object> GetSomeDatas()
        {
            List<object> result = new List<object>();
            DataTable dt = new DataTable();
            dt = create_datatable_data();
            foreach (DataRow row in dt.Rows)
            {
                result.Add(row[0]);
            }
            return result;
        }

        public void ShowData(DataTable dt)
        {
            List<object> datas = GetSomeDatas();

            richTextBox1.Text += "共有資料 : " + datas.Count.ToString() + " 筆\n";

            foreach (object item in datas)
            {
                richTextBox1.Text += "顯示資料 : " + item + "\n";
            }
        }


        private void button9_Click(object sender, EventArgs e)
        {
            //DataTable用法
            int i;
            int j;
            DataTable dt = new DataTable();

            DataColumn column1 = new DataColumn();//创建数据列对象
            column1.DataType = System.Type.GetType("System.String");   //设置数据类型
            column1.ColumnName = "姓名"; //设置列名称
            dt.Columns.Add(column1);//添加数据列

            DataColumn column2 = new DataColumn();//创建数据列对象
            column2.DataType = System.Type.GetType("System.String");   //设置数据类型
            column2.ColumnName = "英文"; //设置列名称
            dt.Columns.Add(column2);//添加数据列

            DataColumn column3 = new DataColumn();//创建数据列对象
            column3.DataType = System.Type.GetType("System.String");   //设置数据类型
            column3.ColumnName = "數學"; //设置列名称
            dt.Columns.Add(column3);//添加数据列

            Random r = new Random();

            for (i = 0; i < 10; i++)
            {
                DataRow dr;//创建数据行变量
                dr = dt.NewRow();//得到数据行对象
                dr["姓名"] = "姓名" + i.ToString();  //设置内容
                dr["英文"] = r.Next(90, 100).ToString();  //设置内容
                dr["數學"] = r.Next(70, 100).ToString();  //设置内容
                dt.Rows.Add(dr);//添回数据行
                //Method(dt);//显示数据表中内容
            }

            int len1 = dt.Columns.Count;
            int len2 = dt.Rows.Count;

            richTextBox1.Text += "len1 = " + len1.ToString() + "\n";
            richTextBox1.Text += "len2 = " + len2.ToString() + "\n";

            for (i = 0; i < len1; i++)
            {
                richTextBox1.Text += dt.Columns[i].ToString() + "\t";
            }
            richTextBox1.Text += "\n";

            for (j = 0; j < len2; j++)
            {
                for (i = 0; i < len1; i++)
                {
                    richTextBox1.Text += dt.Rows[j][i].ToString() + "\t";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "構建DataTable，給列名添加公式\n";

            //計算公式
            string expression1 = "a+b*(c-d)";
            string expression2 = "a+b-c-d";

            //構建DataTable
            DataTable dt = new DataTable();
            dt.Columns.Add("a", typeof(int));
            dt.Columns.Add("b", typeof(int));
            dt.Columns.Add("c", typeof(int));
            dt.Columns.Add("d", typeof(int));
            dt.Columns.Add("e1", typeof(int));//公式列
            dt.Columns.Add("e2", typeof(int));//公式列

            //添加公式
            dt.Columns["e1"].Expression = expression1;
            dt.Columns["e2"].Expression = expression2;

            //添加一行並賦值
            DataRow row = dt.Rows.Add();
            row["a"] = 1;
            row["b"] = 2;
            row["c"] = 4;
            row["d"] = 3;

            dt.BeginLoadData();
            dt.EndLoadData();

            for (int i = 0; i < dt.Columns.Count; i++)
            {
                Console.Write(dt.Columns[i].ColumnName + "\t");
                richTextBox1.Text += dt.Columns[i].ColumnName + "\t";
            }

            Console.WriteLine();
            richTextBox1.Text += "\n";

            for (int i = 0; i < dt.Columns.Count; i++)
            {
                Console.Write(row[i].ToString() + "\t");
                richTextBox1.Text += row[i].ToString() + "\t";
            }

            richTextBox1.Text += "\n";



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

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }
}

