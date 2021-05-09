using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_1A : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int Score = 60;
        if (Score == 60)
            Response.Write(Score + "分剛好及格了");
    }
}