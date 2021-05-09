using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_8_1 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        MytestSub();  //呼叫副程式
    }
    void MytestSub()  //被呼叫的副程式
    {
        Response.Write("副程式測試");
    }
}