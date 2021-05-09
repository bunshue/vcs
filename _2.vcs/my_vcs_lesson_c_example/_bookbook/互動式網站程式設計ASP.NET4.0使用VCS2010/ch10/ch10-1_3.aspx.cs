using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch10_1_1 : System.Web.UI.Page
{
    protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
    {
        Label1.Text = "您剛才選取：" + DropDownList1.SelectedItem.Text + " 同學";
    }
}