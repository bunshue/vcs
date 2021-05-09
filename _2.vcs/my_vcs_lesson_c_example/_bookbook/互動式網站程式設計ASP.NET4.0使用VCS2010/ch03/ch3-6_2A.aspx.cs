using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_2A : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int A;
        A = int.Parse(TextBox1.Text);
        if ((A % 2) == 0)
            TextBox2.Text = "偶數";
        else
            TextBox2.Text = "奇數";
    }
}