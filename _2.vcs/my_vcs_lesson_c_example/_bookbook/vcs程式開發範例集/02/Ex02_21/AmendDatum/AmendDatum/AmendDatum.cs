using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Data.SqlClient;//宣告與數據庫有關的命名空間

namespace AmendDatum
{
    public partial class AmendDatum : Form
    {
        SqlDataAdapter WidgetAdapter;//宣告一個數據讀取器
        DataSet WidgetSet;//宣告一個數據集
        SqlConnection WidgetConnection;//宣告一個數據庫連接對像

        //定義一個數據庫連接字串
        //private string ConnectString = "server=.;database=db_02;integrated security=sspi";
        private string ConnectString = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\db_02.mdf;Integrated Security=True;Connect Timeout=30";

        public AmendDatum()
        {
            InitializeComponent();
        }

        private void AmendDatum_Load(object sender, EventArgs e)
        {
            listView1.Dock = DockStyle.Fill;//設定listView1與其父容器的停靠模式
            listView1.Columns.Add("產品名稱", 100, HorizontalAlignment.Left);//向listView1控制元件中新增「產品名稱」列
            listView1.Columns.Add("產品說明", 200, HorizontalAlignment.Center);//向listView1控制元件中新增「產品說明」列
            WidgetConnection = new SqlConnection(ConnectString);//初始化一個數據庫連接
            string SelectString = "select 產品名稱,產品說明 from tb_WidgetApply";//定義一個數據庫查詢字串
            WidgetAdapter = new SqlDataAdapter(SelectString, WidgetConnection);//初始化數據讀取器對像
            WidgetSet = new DataSet();//初始化數據集
            WidgetAdapter.Fill(WidgetSet, "WidgetApply");//填充數據集
            for (int i = 0; i < WidgetSet.Tables["WidgetApply"].Rows.Count; i++)//循環搜尋數據集中的每一行數據
            {
                listView1.Items.Add(WidgetSet.Tables["WidgetApply"].Rows[i][0].ToString()).SubItems.Add(WidgetSet.Tables["WidgetApply"].Rows[i][1].ToString());//向listView1控制元件中新增數據
            }
            listView1.LabelEdit = true;//設定listView1的可編輯屬性為真
        }

        private void listView1_AfterLabelEdit(object sender, LabelEditEventArgs e)
        {
            WidgetConnection = new SqlConnection(ConnectString);//初始化一個數據庫連接

            if (WidgetConnection.State == ConnectionState.Closed)//當數據庫連接處於關閉狀態時
            {
                WidgetConnection.Open();//打開數據庫連接
            }

            if (e.Label != null && e.Label != "")//當選定項的文字內容存在且不為空時
            {
                string RefreshString = "update tb_WidgetApply set 產品名稱='" + e.Label + "' where 產品編號=" + e.Item + (1).ToString();//定義一個更新數據庫的字串
                SqlCommand WidgetCommand = new SqlCommand(RefreshString, WidgetConnection);//宣告一個執行SQL語句的對象
                WidgetCommand.ExecuteNonQuery();//執行SQL語句
                WidgetConnection.Close();//關閉數據庫連接
                MessageBox.Show("數據修改成功！", "提示訊息", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);//彈出訊息提示
            }
        }
    }
}
