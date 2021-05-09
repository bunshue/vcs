using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
public partial class ch13_4_2 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string Path = Server.MapPath("FileSystem\\text3文字檔.txt");
        // 建立FileInfo物件
        FileInfo FileInfo = new FileInfo(Path);
        if (FileInfo.Exists)
            Response.Write("檔案：" + Path + "　已經存在!");
        else
            Response.Write("檔案" + Path + "　不存在!");
    }
}