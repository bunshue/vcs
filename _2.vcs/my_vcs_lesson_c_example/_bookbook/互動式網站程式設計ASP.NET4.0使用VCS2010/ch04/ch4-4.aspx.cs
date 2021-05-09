using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch4_4 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        string Username;
        string Password;
        Username = TextBox1.Text;
        Password = TextBox2.Text;
        if (Username == "Benson" && Password == "123456")
            Response.Write("您是合法使用者！");
    }
}