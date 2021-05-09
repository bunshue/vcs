using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch5_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        if (TextBox1.Text == "Lee" && TextBox2.Text == "1009")
        {
            Label1.Text = TextBox1.Text;
            MultiView1.ActiveViewIndex = 1;
        }
        else
            Response.Write("帳號或密碼有誤！");
    }

    protected void Page_Load(object sender, EventArgs e)
    {
        Label1.Text = "";
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        MultiView1.ActiveViewIndex = 0;
    }
}