using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_2_1 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        Session["Teacher_name"] = "Lee_Chun_Hsiung";
        Response.Write("<a href=ch7-2.1A.aspx?name=" + Session["Teacher_name"] + ">我的授課老師" + "</a>");
    }
}