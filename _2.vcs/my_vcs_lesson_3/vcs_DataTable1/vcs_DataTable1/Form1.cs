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

            show_data_table(dt);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立DataTable 2
            //1.創建表實例
            DataTable dt = new DataTable();

            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.添加新行
            dt.Rows.Add("1", "david", "100");
            dt.Rows.Add("5", "john", "80");
            dt.Rows.Add("12", "mary", "92");

            show_data_table(dt);
        }

        void show_data_table(DataTable dt)
        {
            int rows = dt.Rows.Count;
            int cols = dt.Columns.Count;

            richTextBox1.Text += "直行 = " + cols.ToString() + "\n";
            richTextBox1.Text += "橫列 = " + rows.ToString() + "\n";

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

            //2.建立表結構
            dt.Columns.Add("座號");
            dt.Columns.Add("姓名");
            dt.Columns.Add("分數");

            //3.添加新行
            dt.Rows.Add("1", "david", "100");
            dt.Rows.Add("5", "john", "80");
            dt.Rows.Add("12", "mary", "92");

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

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

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

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }
}

