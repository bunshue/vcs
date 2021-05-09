using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch6_6 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void CustomValidator1_ServerValidate(object source, ServerValidateEventArgs args)
    {
        if ((Convert.ToInt32(args.Value) % 2) != 0)  //判斷是否為奇數
        {
            args.IsValid = true;   //是奇數
            TextBox1.Text = args.Value + "是奇數";
        }
        else
            args.IsValid = false;  //是偶數
    }
    protected void Button1_Click(object sender, EventArgs e)
    {

    }
}