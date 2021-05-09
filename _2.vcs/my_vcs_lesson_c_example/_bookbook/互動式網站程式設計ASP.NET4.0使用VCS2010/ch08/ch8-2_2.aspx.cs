using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;

public partial class ch8_2_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        string dbpath = "C:\\Inetpub\\wwwroot\\CS\\ch08\\App_Data\\DBMS.mdb";   //宣告資料庫所在的路徑變數
        string Source;                 //宣告連線的字串
        Source = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dbpath;
        OleDbConnection conn;          //宣告連線的物件
        conn = new OleDbConnection(Source);   //連線
        conn.Open();          //開啟資料庫
        Response.Write("<H2> ASP.NET 連線Access測試 </H2>");
        Response.Write("<HR>");
        Response.Write("<H3> 成功連結到Access的伺服器 </H3>");
        conn.Close();         //關閉資料庫
    }
}