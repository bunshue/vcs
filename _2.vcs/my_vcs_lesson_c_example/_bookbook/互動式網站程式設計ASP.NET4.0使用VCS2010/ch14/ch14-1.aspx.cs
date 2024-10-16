﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;
public partial class ch14_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        if (TextBox1.Text != "")
        {
            //宣告資料庫所在的路徑變數
            string dbpath = "C:\\Inetpub\\wwwroot\\ASPNET\\ch14\\App_Data\\DBMS.mdb";
            string Source;                    //宣告連線的字串
            Source = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dbpath;
            OleDbConnection conn;            //宣告連線的物件
            conn = new OleDbConnection(Source);       //連線
            conn.Open();                              //開啟資料庫
            // 開啟資料庫
            string SelectCmd;
            SelectCmd = TextBox1.Text;
            //宣告物件
            OleDbDataAdapter DtApter;
            DataSet DtSet;
            DtApter = new OleDbDataAdapter(SelectCmd, conn);
            DtSet = new DataSet();
            //讀取資料表
            DtApter.Fill(DtSet, "Table");
            GridView1.DataSource = DtSet.Tables["Table"];
            GridView1.DataBind();
            conn.Close();        //關閉資料庫
        }
        else
            Response.Write("您尚未撰寫SQL指令！");
    }
}