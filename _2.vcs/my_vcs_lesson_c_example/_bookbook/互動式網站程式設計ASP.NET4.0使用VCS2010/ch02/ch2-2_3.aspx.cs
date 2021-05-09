using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch2_2_3 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        Button1.Text = "按鈕";
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        int a, b, average;
        a = 60;
        b = 70;
        average = (a + b) / 2;
        Response.Write("平均成績" + average);
    }
}