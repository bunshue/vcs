using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace UseImageList
{
    public partial class Frm_Main : Form
    {
        DataTable dt = new DataTable();//创建数据表对象

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.LargeIcon;//设置显示方式
            listView1.LargeImageList = imageList1;//设置ImageList属性
            DataColumn column = new DataColumn();//创建数据列对象
            column.DataType = System.Type.GetType("System.String");   //设置数据类型
            column.ColumnName = "userName";//设置列名称
            dt.Columns.Add(column);//添加数据列
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DataRow dr;//创建数据行变量
            dr = dt.NewRow();//得到数据行对象
            dr["userName"] = this.txt_UserName.Text;//设置内容
            dt.Rows.Add(dr);//添回数据行
            Method(dt);//显示数据表中内容


            richTextBox1.Text += "add user : " + dr["userName"] + "\n";
        }

        /// <summary>
        /// 显示数据表中内容
        /// </summary>
        /// <param name="dt">数据表对象</param>
        private void Method(DataTable dt)
        {
            listView1.Items.Clear();//清空控件中所有数据项
            for (int j = 0; j < dt.Rows.Count; j++)
            {
                if (j % 2 == 0)
                {
                    //添加数据项和图像
                    listView1.Items.Add(dt.Rows[j][0].ToString(), 0);
                }
                else
                {
                    //添加数据项和图像
                    listView1.Items.Add(dt.Rows[j][0].ToString(), 1);
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();//关闭窗体
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            //DataTable測試

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
                Method(dt);//显示数据表中内容
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
    }
}


