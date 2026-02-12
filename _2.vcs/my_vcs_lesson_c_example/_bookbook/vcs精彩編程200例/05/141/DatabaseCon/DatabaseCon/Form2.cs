using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.Sql;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DatabaseCon
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }
        public static string strServer = "";

        private void Form2_Load(object sender, EventArgs e)
        {
            listBox1.Items.Clear();//清空列表
            //枚举本地网络中的SQL Server所有可用实例
            SqlDataSourceEnumerator instance = SqlDataSourceEnumerator.Instance;
            DataTable table = instance.GetDataSources();//获取所有数据源，并存储到DataTable中
            foreach (DataRow row in table.Rows)//遍历获取到的数据源
            {
                listBox1.Items.Add(row["ServerName"]);//向列表中添加遍历到的服务器名
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndices.Count == 0)
            {
                MessageBox.Show("请选择要连接的服务器！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                this.Close();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            strServer = listBox1.Text;
        }
    }
}
