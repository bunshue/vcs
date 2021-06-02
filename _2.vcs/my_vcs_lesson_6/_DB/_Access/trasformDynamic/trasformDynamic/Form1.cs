using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Linq;
using System.Data.OleDb;

namespace trasformDynamic
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string strIN = "";
            if (checkBox1.Checked == true)												//如果被選取
            {
                strIN = checkBox1.Text;													//新增條件
            }
            if (checkBox2.Checked == true)												//如果被選取
            {
                if (strIN != "")														//如果條件不為空
                    strIN = strIN + "','" + checkBox2.Text;								//累加條件
                else
                    strIN = checkBox2.Text;												//新增條件
            }
            if (checkBox3.Checked == true)												//如果被選取
            {
                if (strIN != "")														//如果條件不為空
                    strIN = strIN + "','" + checkBox3.Text;								//累加條條
                else
                    strIN = checkBox3.Text;												//新增條件
            }
            if (strIN == "")															//如果條件為空
                return;
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + "..//..//dt.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("transform  sum(" + comboBox1.Text + ") as 數據 select " + comboBox3.Text + " from 部門銷售額表 where " + comboBox3.Text + "  in('" + strIN + "')  group by (" + comboBox3.Text + ")  pivot " + comboBox2.Text + "", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            OleDbConnection con = new OleDbConnection("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + "..//..//dt.mdb" + ";Persist Security Info=False");
            OleDbDataAdapter dap = new OleDbDataAdapter("select * from 部門銷售額表 ", con);
            DataSet ds = new DataSet();
            dap.Fill(ds, "table");
            dataGridView1.DataSource = ds.Tables[0].DefaultView;
        }
    }
}