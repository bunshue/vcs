using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch9_7_8B : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        Session["Stu_Id"] = Request.QueryString["Stu_Id"];
        Response.Write("傳遞的值為：" + Session["Stu_Id"]);
    }
}