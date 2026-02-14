using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;//聲明與數據庫操作有關的命名空間

namespace ModifiedNexusVersion
{
    public partial class ModifiedNexusVersion : Form
    {
        public ModifiedNexusVersion()
        {
            InitializeComponent();
        }

        SqlCommand NexusCommand;//聲明一個執行SQL語句的對象
        SqlConnection NexusConnection;//聲明一個數據庫連接對像

        //定義一個數據庫連接字符串
        //private static string ConnectString = "server=.;database=db_02;integrated security=sspi";
        private static string ConnectString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

        private void ModifiedNexusVersion_Load(object sender, EventArgs e)
        {
            treeView1.LabelEdit = true;//設置treeView1的可編輯屬性為true
            NexusConnection = new SqlConnection(ConnectString);//初始化一個數據庫連接對像
            NexusConnection.Open();//打開數據庫連接
            string SelectString = "select 產品編號,產品名稱 from tb_WidgetApply";//定義一個數據庫查詢字符串
            NexusCommand = new SqlCommand(SelectString, NexusConnection);//初始化執行SQL語句對像
            SqlDataReader NexusReader = NexusCommand.ExecuteReader();//定義一個數據讀取器
            treeView1.Nodes.Clear();//清空treeView1原有的數據內容
            TreeNode root = treeView1.Nodes.Add("產品名稱");//為treeView1控件添加根節點
            while (NexusReader.Read())//開始讀取數據中的內容
            {
                TreeNode tempNode = new TreeNode(NexusReader[1].ToString());//將數據庫中的數據字段變換為treeView控件的節點
                root.Nodes.Add(tempNode);//向根節點上添加數據庫字段
            }
            NexusReader.Close();//關閉數據讀取器
            root.ExpandAll();//展開treeView1中的所有節點
            NexusConnection.Close();//關閉數據庫連接
        }

        private void treeView1_AfterLabelEdit(object sender, NodeLabelEditEventArgs e)
        {
            if (e.Label != null && e.Label != "")//當選定項的內容存在且不為空時
            {
                NexusConnection.Open();//打開數據庫連接
                string RefreshString = "update tb_WidgetApply set 產品名稱='" + e.Label + "' where 產品編號=" + (e.Node.Index + 1).ToString();//定義一個數據庫連接字段
                NexusCommand = new SqlCommand(RefreshString, NexusConnection);//定義一個執行SQL語句的對象
                NexusCommand.ExecuteNonQuery();//執行SQL語句
                NexusConnection.Close();//關閉數據庫連接
                MessageBox.Show("修改成功！", "提示信息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出修改成功的提示信息
            }
        }
    }
}
