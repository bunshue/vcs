using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch4_5 : System.Web.UI.Page
{
    protected void TextBox1_TextChanged(object sender, EventArgs e)
    {
        int Num;
        Num = int.Parse(TextBox1.Text);
        if (Num % 2 == 0)
            Label1.Text = Num + "是偶數";
        else
            Label1.Text = Num + "是奇數";
    }
}