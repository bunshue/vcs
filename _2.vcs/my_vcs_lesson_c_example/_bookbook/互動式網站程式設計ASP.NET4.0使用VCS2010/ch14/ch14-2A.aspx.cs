using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Data;
using System.Data.OleDb;
public partial class ch14_2A : System.Web.UI.Page
{
    OleDbConnection conn;             //宣告連線的物件
    protected void Menu1_MenuItemClick(object sender, MenuEventArgs e)
    {
        MultiView1.ActiveViewIndex = Convert.ToInt32(Menu1.SelectedValue);
    }
    protected void Page_Load(object sender, EventArgs e)
    {
        Show_Record1();   //呼叫設定系碼[顯示科系代碼表]
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

    //設定系碼[查詢功能]   
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


    //設定系碼[新增功能]
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

    //設定系碼[修改功能]
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
    //設定系碼[刪除功能]
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
}