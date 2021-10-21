using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DataTable
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //構建DataTable，給列名添加公式

            //計算公式
            string expression1 = "a+b*(c-d)";
            string expression2 = "a+b-c-d";

            //構建table
            DataTable table = new DataTable();
            table.Columns.Add("a", typeof(int));
            table.Columns.Add("b", typeof(int));
            table.Columns.Add("c", typeof(int));
            table.Columns.Add("d", typeof(int));
            table.Columns.Add("e1", typeof(int));//公式列
            table.Columns.Add("e2", typeof(int));//公式列

            //添加公式
            table.Columns["e1"].Expression = expression1;
            table.Columns["e2"].Expression = expression2;


            //添加一行並賦值
            DataRow row = table.Rows.Add();
            row["a"] = 1;
            row["b"] = 2;
            row["c"] = 4;
            row["d"] = 3;

            table.BeginLoadData();
            table.EndLoadData();

            for (int i = 0; i < table.Columns.Count; i++)
            {
                //Console.Write(table.Columns[i].ColumnName + "\t");
                richTextBox1.Text += table.Columns[i].ColumnName + "\t";
            }

            //Console.WriteLine();
            richTextBox1.Text += "\n";

            for (int i = 0; i < table.Columns.Count; i++)
            {
                Console.Write(row[i].ToString() + "\t");
                richTextBox1.Text += row[i].ToString() + "\t";
            }

            richTextBox1.Text += "\n";

            /*
            //使用DataTable的Compute()方法

            DataTable table = new DataTable();
            string value = table.Compute("1+2*(4-3)", "").ToString();
            Console.WriteLine(value);
            */


            //可以把 DataTable 直接轉給 DataGridView 顯示
            //dataGridView1.DataSource = dt.DefaultView;
        }
    }
}
