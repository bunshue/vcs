using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class CSP : System.Web.UI.Page
{
    int total;
    protected void Page_Load(object sender, EventArgs e)
    {
        total = int.Parse(Session["A"].ToString()) + int.Parse(Session["B"].ToString());
        Session["C"] = "C#回傳的結果為：" + total.ToString();
        Label1.Text = total.ToString();
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        Response.Redirect("Default.aspx");
    }
}