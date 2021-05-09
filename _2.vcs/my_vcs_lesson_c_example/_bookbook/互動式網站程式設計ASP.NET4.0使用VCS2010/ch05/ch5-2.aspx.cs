using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch5_1 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        string Temp = "";
        int i;
        for (i = 0; i <= CheckBoxList1.Items.Count - 1; i++)
        {
            if (CheckBoxList1.Items[i].Selected)
                Temp += CheckBoxList1.Items[i].Value + "<br/>";
        }
        TextBox1.Text = Temp;
    }
}