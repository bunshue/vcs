using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;

public partial class ch13_2 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string path1, path2;
        // 取得實際路徑
        path1 = Request.ServerVariables["PATH_INFO"];
        path2 = Server.MapPath(path1);
        Response.Write("目前執行程式所在位置：<br>" + path2);
    }
}