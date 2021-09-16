using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

using System.Data;            	// 引用System.Data
using System.Data.SqlClient;    // 引用System.Data.SqlClient


namespace DBWebService
{
    /// <summary>
    ///WebService1 的摘要描述
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // 若要允許使用 ASP.NET AJAX 從指令碼呼叫此 Web 服務，請取消註解下列一行。
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        // 宣告cnStr資料庫連接字串，指定連接ch23DB.mdf
        private string cnStr = @"Data Source=(LocalDB)\v11.0;" +
                    "AttachDbFilename=|DataDirectory|ch23DB.mdf;" +
                    "Integrated Security=True";

        [WebMethod]
        public DataSet SelectBook()
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;
                SqlDataAdapter da = new SqlDataAdapter
                   ("SELECT * FROM 書籍", cn);
                DataSet ds = new DataSet();
                da.Fill(ds);
                return ds;
            }
        }

        [WebMethod]
        public void InsertBook(string 書號, string 書名, int 單價, int 數量)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;
                cn.Open();
                string sqlStr = "INSERT INTO 書籍(書號, 書名, 單價, 數量)"
                   + "VALUES(@BookId, @BookName, @Price, @Qty)";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter
                   ("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter
                   ("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter
                   ("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter
                   ("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();
            }
        }

        [WebMethod]
        public void UpdateBook(string 書號, string 書名, int 單價, int 數量)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;
                cn.Open();
                string sqlStr = "UPDATE 書籍 SET 書名=@BookName," +
                   "單價=@Price, 數量=@Qty WHERE 書號=@BookId";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter
                   ("@BookId", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter
                   ("@BookName", SqlDbType.NVarChar));
                cmd.Parameters.Add(new SqlParameter
                   ("@Price", SqlDbType.Int));
                cmd.Parameters.Add(new SqlParameter
                   ("@Qty", SqlDbType.Int));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.Parameters["@BookName"].Value = 書名;
                cmd.Parameters["@Price"].Value = 單價;
                cmd.Parameters["@Qty"].Value = 數量;
                cmd.ExecuteNonQuery();
            }
        }
        [WebMethod]
        public void DeleteBook(string 書號)
        {
            using (SqlConnection cn = new SqlConnection())
            {
                cn.ConnectionString = cnStr;
                cn.Open();
                string sqlStr = "DELETE FROM 書籍 WHERE 書號 = @BookId";
                SqlCommand cmd = new SqlCommand(sqlStr, cn);
                cmd.Parameters.Add(new SqlParameter
                  ("@BookId", SqlDbType.NVarChar));
                cmd.Parameters["@BookId"].Value = 書號;
                cmd.ExecuteNonQuery();
            }
        }

    }
}
