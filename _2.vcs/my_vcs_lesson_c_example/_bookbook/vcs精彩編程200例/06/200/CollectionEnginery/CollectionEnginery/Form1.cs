using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.IO;

namespace CollectionEnginery
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public static SqlConnection My_con;  //定义一个SqlConnection类型的公共变量My_con，用于判断数据库是否连接成功

        public static string M_str_sqlcon = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_DB\data\CollectionEnginery.mdf;Integrated Security=True;Connect Timeout=30";

        StreamReader SReader;

        #region  建立数据库连接
        /// <summary>
        /// 建立数据库连接.
        /// </summary>
        /// <returns>返回SqlConnection对象</returns>
        public static SqlConnection getcon()
        {
            My_con = new SqlConnection(M_str_sqlcon);   //用SqlConnection对象与指定的数据库相连接
            My_con.Open();  //打开数据库连接
            return My_con;  //返回SqlConnection对象的信息
        }
        #endregion

        #region  创建DataSet对象
        /// <summary>
        /// 创建一个DataSet对象
        /// </summary>
        /// <param name="M_str_sqlstr">SQL语句</param>
        /// <param name="M_str_table">表名</param>
        /// <returns>返回DataSet对象</returns>
        public DataSet getDataSet(string SQLstr, string tableName)
        {
            getcon();   //打开与数据库的连接
            SqlDataAdapter SQLda = new SqlDataAdapter(SQLstr, My_con);  //创建一个SqlDataAdapter对象，并获取指定数据表的信息
            DataSet My_DataSet = new DataSet(); //创建DataSet对象
            SQLda.Fill(My_DataSet, tableName);  //通过SqlDataAdapter对象的Fill()方法，将数据表信息添加到DataSet对象中
            con_close();    //关闭数据库的连接
            return My_DataSet;  //返回DataSet对象的信息
        }
        #endregion

        #region  关闭数据库连接
        /// <summary>
        /// 关闭于数据库的连接.
        /// </summary>
        public void con_close()
        {
            if (My_con.State == ConnectionState.Open)   //判断是否打开与数据库的连接
            {
                My_con.Close();   //关闭数据库的连接
                My_con.Dispose();   //释放My_con变量的所有空间
            }
        }
        #endregion

        private void Form1_Load(object sender, EventArgs e)
        {
            DataSet dataSet = new DataSet();
            dataSet = getDataSet("select * from tb_Collection", "tb_Collection");
            dataGridView1.DataSource = dataSet.Tables[0];
            dataGridView1.Columns[0].HeaderText = "编号";
            dataGridView1.Columns[0].Width = 40;
            dataGridView1.Columns[1].HeaderText = "书名";
            dataGridView1.Columns[1].Width = 140;
            dataGridView1.Columns[2].HeaderText = "条形码";
            dataGridView1.Columns[2].Width = 80;
            dataGridView1.Columns[3].HeaderText = "累加值";
            dataGridView1.Columns[3].Width = 80;
            dataGridView1.Columns[4].HeaderText = "总计";
            dataGridView1.Columns[4].Width = 40;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string tem_str = "";//记录当前行
            string tem_code = "";//条形码号
            string tem_mark = "";//个数
            string tem_s = " ";
            StreamReader var_SRead = new StreamReader(Application.StartupPath + "\\AddData.dat");//实例化StreamReader，并打开指定的文件
            while (true)//读取dat文件中的所有行
            {
                tem_str = var_SRead.ReadLine();//记录dat文件指定行的数据
                tem_code = tem_str.Substring(0, tem_str.IndexOf(Convert.ToChar(tem_s))).Trim();//获取当前行的条形码
                tem_mark = tem_str.Substring(tem_str.IndexOf(Convert.ToChar(tem_s)), tem_str.Length - tem_str.IndexOf(Convert.ToChar(tem_s)) - 1).Trim();//获取当前条形码的个数
                for (int i = 0; i < dataGridView1.RowCount - 1; i++)//在dataGridView1控件中查找相应的条形码
                {
                    if (dataGridView1.Rows[i].Cells[2].Value.ToString().Trim() == tem_code)//如查找到
                    {
                        dataGridView1.Rows[i].Cells[3].Value = tem_mark.ToString();//显示当前要添加的个数
                        dataGridView1.Rows[i].Cells[4].Value = Convert.ToInt32(dataGridView1.Rows[i].Cells[4].Value) + Convert.ToInt32(tem_mark);//计算当前条形码的总数
                    }
                }
                if (var_SRead.EndOfStream)//如果查询到文件尾
                {
                    break;//退出循环
                }
            }
            var_SRead.Close();//释放所有资源
        }
    }
}
