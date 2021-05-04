using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace SingMatchWeb
{
    public partial class score1 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnAdd_Click(object sender, EventArgs e)
        {
            SqlDataSource1.InsertParameters["編號"].DefaultValue = txtNo.Text;
            SqlDataSource1.InsertParameters["音色50"].DefaultValue = txtTone.Text;
            SqlDataSource1.Insert();
            btnCls_Click(sender, e);
        }

        protected void btnCls_Click(object sender, EventArgs e)
        {
            txtNo.Text = "";
            txtTone.Text = "";
        }
    }
}