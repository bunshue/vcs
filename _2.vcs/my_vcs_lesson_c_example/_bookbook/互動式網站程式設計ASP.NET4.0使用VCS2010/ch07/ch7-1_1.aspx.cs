using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_1_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        Response.Write("您好嗎？");      //字串資料必須加上雙引號「""」
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        Response.Write(DateTime.Now.ToString());          //變數資料不能上雙引號「""」
    }

    protected void Button3_Click(object sender, EventArgs e)
    {
        Response.Write("現在時間是：" + DateTime.Now.ToString());   //+代表連結符號
    }
}