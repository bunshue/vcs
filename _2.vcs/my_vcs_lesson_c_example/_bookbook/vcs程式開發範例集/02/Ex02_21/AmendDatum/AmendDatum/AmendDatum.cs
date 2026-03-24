using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;

namespace AmendDatum
{
    public partial class AmendDatum : Form
    {
        SqlDataAdapter da;//宣告一個數據讀取器
        DataSet ds;//宣告一個數據集
        SqlConnection cn;//宣告一個數據庫連接對像
        SqlCommand NexusCommand;//聲明一個執行SQL語句的對象

        //定義一個數據庫連接字符串
        private string cnstr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=D:\db_02.mdf;Integrated Security=True;Connect Timeout=30";

        public AmendDatum()
        {
            InitializeComponent();
        }

        private void AmendDatum_Load(object sender, EventArgs e)
        {
            listView1.Columns.Add("產品名稱", 100, HorizontalAlignment.Left);//向listView1控制元件中新增「產品名稱」列
            listView1.Columns.Add("產品說明", 200, HorizontalAlignment.Center);//向listView1控制元件中新增「產品說明」列

            cn = new SqlConnection(cnstr);//初始化一個數據庫連接
            string sqlstr = "select 產品名稱,產品說明 from tb_WidgetApply";//定義一個數據庫查詢字串
            da = new SqlDataAdapter(sqlstr, cn);//初始化數據讀取器對像
            ds = new DataSet();//初始化數據集
            da.Fill(ds, "WidgetApply");//填充數據集
            for (int i = 0; i < ds.Tables["WidgetApply"].Rows.Count; i++)//循環搜尋數據集中的每一行數據
            {
                listView1.Items.Add(ds.Tables["WidgetApply"].Rows[i][0].ToString()).SubItems.Add(ds.Tables["WidgetApply"].Rows[i][1].ToString());//向listView1控制元件中新增數據
            }
            listView1.LabelEdit = true;//設定listView1的可編輯屬性為真


            //6060

            //修改TreeView控制元件中的節點文字

            treeView1.LabelEdit = true;//設置treeView1的可編輯屬性為true
            cn = new SqlConnection(cnstr);//初始化一個數據庫連接對像
            cn.Open();//打開數據庫連接
            sqlstr = "select 產品編號,產品名稱 from tb_WidgetApply";//定義一個數據庫查詢字符串
            NexusCommand = new SqlCommand(sqlstr, cn);//初始化執行SQL語句對像
            SqlDataReader NexusReader = NexusCommand.ExecuteReader();//定義一個數據讀取器
            treeView1.Nodes.Clear();//清空treeView1原有的數據內容
            TreeNode root = treeView1.Nodes.Add("產品名稱");//為treeView1控件添加根節點
            while (NexusReader.Read())//開始讀取數據中的內容
            {
                richTextBox1.Text += NexusReader[1].ToString() + "\n";

                TreeNode tempNode = new TreeNode(NexusReader[1].ToString());//將數據庫中的數據字段變換為treeView控件的節點
                root.Nodes.Add(tempNode);//向根節點上添加數據庫字段
            }
            NexusReader.Close();//關閉數據讀取器
            root.ExpandAll();//展開treeView1中的所有節點
            cn.Close();//關閉數據庫連接



        }

        private void listView1_AfterLabelEdit(object sender, LabelEditEventArgs e)
        {
            cn = new SqlConnection(cnstr);//初始化一個數據庫連接

            if (cn.State == ConnectionState.Closed)//當數據庫連接處於關閉狀態時
            {
                cn.Open();//打開數據庫連接
            }

            if (e.Label != null && e.Label != "")//當選定項的文字內容存在且不為空時
            {
                string RefreshString = "update tb_WidgetApply set 產品名稱='" + e.Label + "' where 產品編號=" + e.Item + (1).ToString();//定義一個更新數據庫的字串
                SqlCommand WidgetCommand = new SqlCommand(RefreshString, cn);//宣告一個執行SQL語句的對象
                WidgetCommand.ExecuteNonQuery();//執行SQL語句
                cn.Close();//關閉數據庫連接
                richTextBox1.Text += "修改成功\n";
            }
        }

        //6060

        private void treeView1_AfterLabelEdit(object sender, NodeLabelEditEventArgs e)
        {
            if (e.Label != null && e.Label != "")//當選定項的內容存在且不為空時
            {
                cn.Open();//打開數據庫連接
                string RefreshString = "update tb_WidgetApply set 產品名稱='" + e.Label + "' where 產品編號=" + (e.Node.Index + 1).ToString();//定義一個數據庫連接字段
                NexusCommand = new SqlCommand(RefreshString, cn);//定義一個執行SQL語句的對象
                NexusCommand.ExecuteNonQuery();//執行SQL語句
                cn.Close();//關閉數據庫連接
                MessageBox.Show("修改成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出修改成功的提示信息
            }

        }
    }
}

