using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch4_4_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        Label1.Text = "您剛才按了==>按鈕控制項";
    }

    protected void LinkButton1_Click(object sender, EventArgs e)
    {
        Label1.Text = "您剛才按了==>超連結按鈕控制項";
    }
}