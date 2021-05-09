using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_1_3B : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string UserName;
        string Password;
        UserName = "";
        Password = "12345";
        if (UserName == "")
        {
            Response.Write("對不起，你沒有輸入帳號");
            Response.End();  //強迫結束
        }
        if (Password == "")
        {
            Response.Write("對不起，你沒有輸入密碼");
            Response.End();  //強迫結束
        }
        Response.Write(UserName + "請記住您註冊的密碼：" + Password);
    }

}