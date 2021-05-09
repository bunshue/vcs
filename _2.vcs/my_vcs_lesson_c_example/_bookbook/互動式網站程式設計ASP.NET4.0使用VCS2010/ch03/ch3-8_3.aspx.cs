using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_8_3 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int Sum;
        Sum = MyFunction(10);   //呼叫函數
        Response.Write("1+2+...+10=" + Sum);
    }
    static int MyFunction(int N)   //被呼叫的函數
    {
        int i, total = 0;
        for (i = 1; i <= N; i++)
            total = total + i;
        return total;
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        int Result;
        int X = 10;
        Result = Total(X);
        Response.Write("遞迴函數呼叫10!=1×2×3×4×5×6×....×10=" + Result);
    }

    static int Total(int N)                //函數名稱
    {
        if (N == 0)
            return 1;
        else
            return N * Total(N - 1);        //函數自己又可以呼叫自己
    }
}