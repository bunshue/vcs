using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SingMatchWeb
{
    public partial class inquireForm : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void GridView1_RowDataBound(object sender, GridViewRowEventArgs e)
        {
            if (e.Row.RowType == DataControlRowType.DataRow)
            {
                int total = 0;
                total = Convert.ToInt16(e.Row.Cells[2].Text) + Convert.ToInt16(e.Row.Cells[3].Text) +
                        Convert.ToInt16(e.Row.Cells[4].Text);
                e.Row.Cells[5].Text = total.ToString();
           }
       }
    }
}