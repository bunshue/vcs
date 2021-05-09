using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_1_2 : System.Web.UI.Page
{
    protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        if (DropDownList1.SelectedValue == "1")
            Response.Redirect("http://www.ntu.edu.tw");
        else if (DropDownList1.SelectedValue == "2")
            Response.Redirect("http://www.ntust.edu.tw");
        else if (DropDownList1.SelectedValue == "3")
            Response.Redirect("http://www.ntnu.edu.tw");
    }
}