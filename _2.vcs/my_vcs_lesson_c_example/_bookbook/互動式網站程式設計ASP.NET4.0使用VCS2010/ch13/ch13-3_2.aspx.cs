using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
public partial class ch13_3_2 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string OldDir = Server.MapPath("FileSystem\\test3");
        Directory.Delete(OldDir);
        Response.Write("您已經刪除了test3資料夾");
    }
}