using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_2_1A : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string TeaName = Request.QueryString["name"];
        Response.Write("老師姓名：" + TeaName);
    }
}