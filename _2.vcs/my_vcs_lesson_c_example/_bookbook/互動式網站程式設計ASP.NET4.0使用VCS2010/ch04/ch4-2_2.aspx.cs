using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch4_2_2 : System.Web.UI.Page
{
    protected void Ok1_OnClick(object sender, EventArgs e)
    {
        Label1.Text = "這是Label元件的字型屬性";
        Text1.Text = "這是TextBox元件的字型屬性";
    }
}