using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;

public partial class ch8_4 : System.Web.UI.Page
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
        SelectCmd = "select * from 學生資料表";
        //宣告物件
        OleDbDataAdapter DtApter = new OleDbDataAdapter(SelectCmd, conn);
        DataSet DtSet = new DataSet();
        //讀取資料表
        DtApter.Fill(DtSet, "學生資料表");
        new_grid.DataSource = DtSet;
        new_grid.DataBind();
        conn.Close();         //關閉資料庫
    }
}