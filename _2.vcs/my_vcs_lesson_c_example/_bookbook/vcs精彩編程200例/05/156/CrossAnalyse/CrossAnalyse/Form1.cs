using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace CrossAnalyse
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Data.MDF";
        //string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_09_Log.LDF";   another

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            comboBox1.SelectedIndex = 0;
            comboBox2.SelectedIndex = 0;
            bindInfo();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            bindInfo();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex == 0)
                comboBox2.SelectedIndex = 0;
            else
                comboBox2.SelectedIndex = 1;
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox2.SelectedIndex == 0)
                comboBox1.SelectedIndex = 0;
            else
                comboBox1.SelectedIndex = 1;
        }

        #region 按指定的条件使用交叉表查询数据
        /// <summary>
        /// 按指定的条件使用交叉表查询数据
        /// </summary>
        protected void bindInfo()
        {
            SqlConnection sqlcon = new SqlConnection("Data Source=USER-20170504OU;Database=db_09;Uid=sa;Pwd=");
            SqlCommand sqlcom = new SqlCommand("proc_across_table", sqlcon);
            sqlcom.CommandType = CommandType.StoredProcedure;
            sqlcom.Parameters.Add("@TableName", SqlDbType.VarChar, 50).Value = "商品销售表";
            if (comboBox1.Text == comboBox2.Text)
            {
                MessageBox.Show("表头字段和分组字段不能相同！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            sqlcom.Parameters.Add("@NewColumn", SqlDbType.VarChar, 50).Value = comboBox1.Text;
            sqlcom.Parameters.Add("@GroupColumn", SqlDbType.VarChar, 50).Value = comboBox2.Text;
            sqlcom.Parameters.Add("@StatColumn", SqlDbType.VarChar, 50).Value = "订货数量";
            sqlcom.Parameters.Add("@Operator", SqlDbType.VarChar, 10).Value = "SUM";
            SqlDataAdapter myda = new SqlDataAdapter();
            myda.SelectCommand = sqlcom;
            DataSet myds = new DataSet();
            myda.Fill(myds);
            dataGridView1.DataSource = myds.Tables[0];
            dataGridView1.Columns[1].Width = 120;
        }
        #endregion
    }
}
