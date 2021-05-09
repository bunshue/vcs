using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_3C : System.Web.UI.Page
{

    protected void Button1_Click(object sender, EventArgs e)
    {
        int  A  = 2;
        int I  = 1;
        while (A <= 1000)
        {
            A *= 2;
            I += 1;
        }
        Response.Write("2的 " + I + "次方才會大於1,000");
    }
}