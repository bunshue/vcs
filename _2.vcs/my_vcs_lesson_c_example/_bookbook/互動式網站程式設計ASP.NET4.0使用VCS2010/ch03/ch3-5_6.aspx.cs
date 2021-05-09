using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_5_6 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int R = 5;
        Response.Write("圓的半徑是：" + R);
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        Response.Write("圓面積是：" + "圓周率*半徑^2");
    }

    protected void Button3_Click(object sender, EventArgs e)
    {
        int R = 5;
        const double PI = 3.14;
        Response.Write("圓面積是：" + PI * (Math.Pow(R, 2)));
    }

    protected void Button4_Click(object sender, EventArgs e)
    {
        int A = 3;
        int B = 5;
        Response.Write(A + B);    //結果：8
    }

    protected void Button5_Click(object sender, EventArgs e)
    {
        string A = "3";
        string B = "5";
        Response.Write(A + B);    //結果：35
    }
}