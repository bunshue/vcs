using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
public partial class ch13_3_1 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string NewDir = Server.MapPath("FileSystem\\test3");
        Directory.CreateDirectory(NewDir);
        Response.Write("您目前建立的目錄為：<br> " + NewDir);
    }
}