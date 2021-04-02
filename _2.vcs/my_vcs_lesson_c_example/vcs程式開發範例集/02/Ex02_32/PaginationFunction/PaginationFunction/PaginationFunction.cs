using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Data.SqlClient;//引用與數據庫操作有關的命名空間

namespace PaginationFunction
{
    public partial class PaginationFunction : Form
    {
        public PaginationFunction()
        {
            InitializeComponent();
        }
        private static string ConnectString = "server=.;database=pubs;integrated security=sspi";//定義數據庫連接字符串
        private SqlConnection PaginationConnection;//定義數據庫連接對像
        private SqlDataAdapter PaginationAdapter;//定義填充數據集對像
        private DataSet PaginationSet = new DataSet();//定義存儲數據的集合
        private DataTable PageTable = new DataTable();//定義一個數據表
        private page Page = new page();//定義一個具有分頁功能的類

        private void PaginationFunction_Load(object sender, EventArgs e)
        {
            DataSet PageSet = new DataSet();// 定義一個存儲數據的集合
            PaginationConnection = new SqlConnection(ConnectString);//初始化數據庫連接對像
            string selectString = "select emp_id as 用戶編號,fname as 用戶姓名,hire_date as 工作時間 from employee";//定義一個查詢字符串變量
            PageSet.Clear();//清空數據集中原有內容
            FillDataTable(selectString, ref PageSet);//型數據表中填充數據

            Page.ItemsPerPage = 8;//設定每頁顯示多少行
            Page.SetDataSet(PageSet, out PageTable);//設置當前數據集中的內容
            display(PageTable);//顯示數據

        }

        public bool FillDataTable(string sqlStr, ref DataSet TargetDataSet)
        {
            try
            {
                PaginationConnection = new SqlConnection(ConnectString);//初始化數據庫連接對像
                PaginationAdapter = new SqlDataAdapter(sqlStr, PaginationConnection);//初始化數據讀取對像
                PaginationAdapter.Fill(TargetDataSet);//填充數據集
                return true;//返回值為true
            }
            catch (Exception ex)//捕獲異常
            {
                MessageBox.Show(ex.Message);//顯示異常信息
                return false;//返回值為false
            }
            finally
            {
                PaginationConnection.Close();//關閉數據庫連接
            }
        }

        private void display(DataTable PageTable)
        {
            if (PageTable != null)//當數據表中存在記錄時
            {
                ListData.Rows.Clear();//清空DataGridView中原有的數據
                object[] item = new object[PageTable.Columns.Count];//定義一個object類型的數組
                for (int i = 0; i < PageTable.Rows.Count; i++)//循環遍歷數據表中的每一行數據
                {
                    for (int j = 0; j < PageTable.Columns.Count; j++)//循環遍歷數據表中每一列數據
                    {
                        item[j] = PageTable.Rows[i][j];//保存數據表中的數據內容
                    }
                    ListData.Rows.Add(item);//向DataGridView中添加數據
                }
            }
        }

        private void fistpage_Click(object sender, EventArgs e)
        {
            PageTable = null;//清空數據表中原有內容
            Page.GoToFirstPage(out PageTable);//跳轉到首頁
            display(PageTable);//顯示數據
        }

        private void PreviousPage_Click(object sender, EventArgs e)
        {
            PageTable = null;//清空數據表中原有內容
            Page.GoToPreviousPage(out PageTable);//跳轉到上一頁
            display(PageTable);//顯示數據
        }

        private void nextpage_Click(object sender, EventArgs e)
        {
            PageTable = null;//清空數據表中原有內容
            Page.GoToNextPage(out PageTable);//跳轉到下一列
            display(PageTable);//顯示數據
        }

        private void LastPage_Click(object sender, EventArgs e)
        {
            PageTable = null;//清空數據表中原有內容
            Page.GoToLastPage(out PageTable);//跳轉到尾頁
            display(PageTable);//顯示數據
        }
    }
}
