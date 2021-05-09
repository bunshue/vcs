using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_3 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        Response.Write("求1+2+3+...+10的程式");
        int i, sum;
        sum = 0;
        for (i = 1; i <= 10; i++)
            sum = sum + i;
        Response.Write("總和是：" + sum);
    }
}