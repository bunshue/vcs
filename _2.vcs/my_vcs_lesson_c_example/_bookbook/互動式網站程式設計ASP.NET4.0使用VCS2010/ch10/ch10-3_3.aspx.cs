using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch10_1_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        AccessDataSource2.Insert();
    }
}