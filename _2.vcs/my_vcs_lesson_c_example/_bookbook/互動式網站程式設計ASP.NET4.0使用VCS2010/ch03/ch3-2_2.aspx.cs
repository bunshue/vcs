using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_2_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int MyVar;   //宣告變數
        MyInt = 10;  //使用到未宣告的變數將會產生錯誤
        MyVar = 20;  //使用宣告過的變數就沒有錯誤
    }
}