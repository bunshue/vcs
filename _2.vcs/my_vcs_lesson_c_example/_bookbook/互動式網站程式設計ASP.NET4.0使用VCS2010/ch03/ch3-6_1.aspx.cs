using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        Single A, B, C, D;
        A = 20;         //將20指定給A
        B = 40;         //將40指定給B
        C = A + B;      //將A與B的值相加後，再指定給C
        D = A / B;     //將A與B的值相除後，再指定給D
        Response.Write("C=" + C);
        Response.Write("<br>");
        Response.Write("D=" + D);
    }
    protected void Page_Load(object sender, EventArgs e)
    {

    }
}