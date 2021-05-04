using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.SqlClient;

namespace ImageListLogon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        DataTable dt = new DataTable();
        private void button1_Click(object sender, EventArgs e)
        {
            DataRow dr;
            dr = dt.NewRow();
            dr["userName"] = this.textBox1.Text;
            dt.Rows.Add(dr);
            Method(dt);
           
        }

        private void Method(DataTable dt)
        {
            listView1.Items.Clear();
            for (int j = 0; j < dt.Rows.Count; j++)
            {
                if (j % 2 == 0)
                {
                    listView1.Items.Add(dt.Rows[j][0].ToString(), 0);//新增頭像1
                }
                else
                {
                    listView1.Items.Add(dt.Rows[j][0].ToString(), 1);
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.View = View.LargeIcon;
            listView1.LargeImageList = imageList1;
            DataColumn column = new DataColumn();
            column.DataType = System.Type.GetType("System.String");
            column.ColumnName = "userName";
            dt.Columns.Add(column);
            Method(dt);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}