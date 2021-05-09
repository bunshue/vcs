using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch5_1 : System.Web.UI.Page
{
    protected void Wizard1_FinishButtonClick(object sender, WizardNavigationEventArgs e)
    {
        Label1.Text = "您的姓名：" + TextBox2.Text;
        Label1.Text += "<br>您喜愛的課程：" + DropDownList1.Text;
        Label1.Text += "<br>帳號：" + TextBox3.Text;
        Label1.Text += "<br>密碼：" + TextBox4.Text;
    }

}