using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch9_7_3 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        GridView1.Sort(DropDownList1.SelectedValue, SortDirection.Ascending);
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        GridView1.Sort(DropDownList1.SelectedValue, SortDirection.Descending);
    }
}