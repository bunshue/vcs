﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;
public partial class ch14_2B : System.Web.UI.Page
{
    OleDbConnection conn;             //宣告連線的物件
    protected void Menu1_MenuItemClick(object sender, MenuEventArgs e)
    {
        MultiView1.ActiveViewIndex = Convert.ToInt32(Menu1.SelectedValue);
    }
    protected void Page_Load(object sender, EventArgs e)
    {
        Show_Record1();    //呼叫設定系碼[顯示科系代碼表]
        Show_Record2();    //呼叫課程管理[顯示課程管理表]
    }

    void Con_DB()    //連接資料庫之副程式
    {
        string dbpath = "C:\\Inetpub\\wwwroot\\ASPNET\\ch14\\App_Data\\DBMS1.mdb";       //宣告資料庫所在的路徑變數
        string Source;                     //宣告連線的字串
        Source = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source=" + dbpath;
        conn = new OleDbConnection(Source);       //連線
        conn.Open();                              //開啟資料庫
    }

    void Show_Record1()  //設定系碼[顯示科系代碼表]
    {
        Con_DB();    //呼叫連接資料庫之副程式
        // 開啟資料庫
        string SelectCmd;
        SelectCmd = "select * from 科系代碼資料表 order by 系碼 ASC";
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

    void Show_Record2()  //課程管理[顯示課程管理表]
    {
        Con_DB();    //呼叫連接資料庫之副程式
        // 開啟資料庫
        string SelectCmd;
        SelectCmd = "select * from 課程資料表 order by 課號 ASC";
        //宣告物件
        OleDbDataAdapter DtApter;
        DataSet DtSet;
        DtApter = new OleDbDataAdapter(SelectCmd, conn);
        DtSet = new DataSet();
        //讀取資料表
        DtApter.Fill(DtSet, "Table");
        GridView2.DataSource = DtSet.Tables["Table"];
        GridView2.DataBind();
        conn.Close();        //關閉資料庫
    }

    //一、設定系碼[查詢功能]   
    protected void Button1_Click(object sender, EventArgs e)
    {
        ID = TextBox1.Text;
        Con_DB();   //呼叫連接資料庫之副程式
        string SelectCmd;
        SelectCmd = "select * from 科系代碼資料表 Where 系碼='" + ID + "'";
        OleDbCommand Cmd = new OleDbCommand(SelectCmd, conn);
        OleDbDataReader reader;
        reader = Cmd.ExecuteReader();
        //顯示資料表欄位的所有資料
        while (reader.Read())
        {
            TextBox1.Text = reader["系碼"].ToString();
            TextBox2.Text = reader["系名"].ToString();
            TextBox3.Text = reader["系主任"].ToString();
        }
        conn.Close();                       // 關閉資料庫  
    }


    //一、設定系碼[新增功能]
    protected void Button2_Click(object sender, EventArgs e)
    {
        Con_DB();    //呼叫連接資料庫之副程式
        string InsertCmd;
        InsertCmd = "Insert Into 科系代碼資料表(系碼,系名,系主任) Values('" + TextBox1.Text.Trim() + "','" + TextBox2.Text.Trim() + "','" + TextBox3.Text.Trim() + "')";
        OleDbCommand cmd = new OleDbCommand(InsertCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();                              // 關閉資料庫
        Response.Write("新增成功！");
        Show_Record1();
    }

    //一、設定系碼[修改功能]
    protected void Button3_Click(object sender, EventArgs e)
    {
        Con_DB();    //呼叫連接資料庫之副程式
        string UpdateCmd;
        UpdateCmd = "UPDATE 科系代碼資料表 SET 系碼='" + TextBox1.Text.Trim() + "',系名='" + TextBox2.Text.Trim() + "' ,系主任='" + TextBox3.Text.Trim() + "' WHERE 系碼='" + TextBox1.Text.Trim() + "'";
        OleDbCommand cmd = new OleDbCommand(UpdateCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();
        Response.Write("修改成功！");
        Show_Record1();
    }
    //一、設定系碼[刪除功能]
    protected void Button4_Click(object sender, EventArgs e)
    {
        ID = TextBox1.Text;
        Con_DB();    //呼叫連接資料庫之副程式
        string DeleteCmd;
        DeleteCmd = "Delete From 科系代碼資料表 WHERE 系碼='" + ID + "'";
        OleDbCommand cmd = new OleDbCommand(DeleteCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();
        Response.Write("刪除成功！");
        Show_Record1();
    }

    //二、課程管理[查詢功能]
    protected void Button5_Click(object sender, EventArgs e)
    {
        ID = TextBox4.Text;
        Con_DB();   //呼叫連接資料庫之副程式
        string SelectCmd;
        SelectCmd = "select * from 課程資料表 Where 課號='" + ID + "'";
        OleDbCommand Cmd = new OleDbCommand(SelectCmd, conn);
        OleDbDataReader reader;
        reader = Cmd.ExecuteReader();
        //顯示資料表欄位的所有資料
        while (reader.Read())
        {
            TextBox4.Text = reader["課號"].ToString();
            TextBox5.Text = reader["課名"].ToString();
            DropDownList1.Text = reader["學分數"].ToString();
            if (reader["必選修"] == "必")
            {
                RadioButton1.Checked = true;
                RadioButton2.Checked = false;
            }
            else
            {
                RadioButton1.Checked = false;
                RadioButton2.Checked = true;
            }
        }
        conn.Close();                       // 關閉資料庫
    }

    //二、課程管理[新增功能]    
    protected void Button6_Click(object sender, EventArgs e)
    {
        Con_DB();   //呼叫連接資料庫之副程式                          
        string sp;
        string InsertCmd;
        if (RadioButton1.Checked == true)
            sp = "必";
        else
            sp = "選";
        InsertCmd = "Insert Into 課程資料表(課號,課名,學分數,必選修) Values('" + TextBox4.Text.Trim() + "','" + TextBox5.Text.Trim() + "','" + DropDownList1.Text.Trim() + "','" + sp + "')";
        OleDbCommand cmd = new OleDbCommand(InsertCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();                         // 關閉資料庫
        Response.Write("新增成功！");
        Show_Record2();
    }

    //二、課程管理[修改功能]
    protected void Button7_Click(object sender, EventArgs e)
    {
        Con_DB();   //呼叫連接資料庫之副程式                          
        string sp;
        string UpdateCmd;
        if (RadioButton1.Checked == true)
            sp = "必";
        else
            sp = "選";
        UpdateCmd = "UPDATE 課程資料表 SET 課號='" + TextBox4.Text.Trim() + "',課名='" + TextBox5.Text.Trim() + "' ,學分數='" + DropDownList1.Text.Trim() + "', 必選修='" + sp + "' WHERE 課號='" + TextBox4.Text.Trim() + "'";
        OleDbCommand cmd = new OleDbCommand(UpdateCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();                         // 關閉資料庫
        Response.Write("新增成功！");
        Show_Record2();
    }
    //二、課程管理[刪除功能]
    protected void Button8_Click(object sender, EventArgs e)
    {
        ID = TextBox4.Text;
        Con_DB();   //呼叫連接資料庫之副程式
        string DeleteCmd;
        DeleteCmd = "Delete From 課程資料表 WHERE 課號='" + ID + "'";
        OleDbCommand cmd = new OleDbCommand(DeleteCmd, conn);
        cmd.ExecuteNonQuery();
        conn.Close();
        Response.Write("刪除成功！");
        Show_Record2();
    }
}