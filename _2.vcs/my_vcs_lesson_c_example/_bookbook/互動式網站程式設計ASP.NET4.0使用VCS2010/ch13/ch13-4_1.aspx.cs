using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
public partial class ch13_4_1 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string Path = Server.MapPath("FileSystem\\text3文字檔.txt");
        // 建立FileInfo物件
        FileInfo FileInfo = new FileInfo(Path);
        // 建立文字檔案
        FileInfo.CreateText();
        Response.Write("您目前建立的檔案為：<br> " + Path);
    }
}