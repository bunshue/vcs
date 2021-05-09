using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_8_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int X, Y;
        X = 5;
        Y = 10;
        Response.Write("「傳值呼叫」呼叫前<hr>");
        Response.Write("X=" + X + "　　　" + "Y=" + Y + "<br>");
        CallByValue(X, Y);
        Response.Write("「傳值呼叫」呼叫後<hr>");
        Response.Write("X=" + X + "　　　" + "Y=" + Y + "<br>");
    }
    static void CallByValue(int A, int B)
    {
        A = 15;
        B = 30;
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        int X, Y;
        X = 5;
        Y = 10;
        Response.Write("「傳址呼叫」呼叫前<hr>");
        Response.Write("X=" + X + "　　　" + "Y=" + Y + "<br>");
        CallByAddress(ref X, ref Y);
        Response.Write("「傳址呼叫」呼叫後<hr>");
        Response.Write("X=" + X + "　　　" + "Y=" + Y + "<br>");
    }
    static void CallByAddress(ref int A, ref int B)
    {
        A = 15;
        B = 30;
    }  
}