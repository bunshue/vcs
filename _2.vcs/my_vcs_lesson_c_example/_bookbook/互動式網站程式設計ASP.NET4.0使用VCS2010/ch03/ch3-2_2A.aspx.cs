using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_2_2A : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int i, Sum; 
        for (i = 1; i <= 10; i++)
            Sum = Sun + 1;
        Response.Write("總數是：" + Sum);
    }
}