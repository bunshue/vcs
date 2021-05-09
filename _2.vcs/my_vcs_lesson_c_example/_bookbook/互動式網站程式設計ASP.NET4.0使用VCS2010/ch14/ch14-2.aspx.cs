using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch14_2 : System.Web.UI.Page
{
    protected void Menu1_MenuItemClick(object sender, EventArgs e)
    {
        MultiView1.ActiveViewIndex = Convert.ToInt32(Menu1.SelectedValue);
    }
}