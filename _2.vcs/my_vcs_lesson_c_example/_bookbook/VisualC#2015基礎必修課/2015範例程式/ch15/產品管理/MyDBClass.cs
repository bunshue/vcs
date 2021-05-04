using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data;          //使用DataSet必須引用
using System.Data.SqlClient;//使用SqlConnection, SqlCommand, SqlDataAdapter必須引用
using System.Windows.Forms; //使用MessageBox.Show方法必須引用

namespace 產品管理
{
    class MyDBClass
    {
        //宣告cnStr連線字串置於事件處理函式外，以提供給其他事件處理函式共用
        String cnStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\Database1.mdf;Integrated Security=True;Connect Timeout=30";
        //GetCategory()方法可傳回產品類別的DataTable
        public DataTable  GetCategory()
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT * From 產品類別", cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            return  ds.Tables[0];
        }
        //GetProduct()方法可依傳入的類別編號來傳回指定的產品資料的DataTable
        public DataTable GetProduct(int CategoryId)
        {
            SqlConnection cn = new SqlConnection(cnStr);
            SqlDataAdapter da = new SqlDataAdapter("SELECT 產品編號,品名,單價,說明 From 產品資料 WHERE 類別編號=" + CategoryId, cn);
            DataSet ds = new DataSet();
            da.Fill(ds);
            return ds.Tables[0];
        }
        //Edit()方法可依傳入的SQL陳述式對指定的資料表進行新增、修改、刪除
        public void Edit(string SqlCmd)
        {
            try
            {
                SqlConnection cn = new SqlConnection(cnStr);
                cn.Open();
                SqlCommand cmd = new SqlCommand();
                cmd.CommandText = SqlCmd;
                cmd.Connection = cn;
                cmd.ExecuteNonQuery();
                cn.Close();      
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
