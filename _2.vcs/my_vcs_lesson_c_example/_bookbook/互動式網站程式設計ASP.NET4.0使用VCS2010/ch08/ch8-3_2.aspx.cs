using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;

public partial class ch8_3_2 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string dbpath = "C:\\Inetpub\\wwwroot\\CS\\ch08\\App_Data\\DBMS.mdb";   //宣告資料庫所在的路徑變數
        string Source;                 //宣告連線的字串
        Source = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dbpath;
        OleDbConnection conn;          //宣告連線的物件
        conn = new OleDbConnection(Source);   //連線
        conn.Open();          //開啟資料庫

        string SelectCmd;
        int i;
        SelectCmd = "select * from 學生資料表";
        OleDbCommand Cmd = new OleDbCommand(SelectCmd, conn);
        OleDbDataReader reader;
        reader = Cmd.ExecuteReader();
        Response.Write("<table border=1 align=center>");
        //顯示資料表欄位的所有資料
        while (reader.Read())
        {
            Response.Write("<tr align=center>");
            for (i = 0; i <= reader.FieldCount - 1; i++)
                Response.Write("<td>" + reader.GetValue(i) + "</td>");
            Response.Write("</tr>");
        }
        Response.Write("</table>");
        conn.Close();         //關閉資料庫
    }
}