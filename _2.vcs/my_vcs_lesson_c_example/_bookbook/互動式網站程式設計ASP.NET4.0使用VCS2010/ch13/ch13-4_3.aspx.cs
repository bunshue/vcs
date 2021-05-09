using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.IO;
public partial class ch13_4_3 : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        string Path = Server.MapPath("FileSystem\\text3文字檔.txt");
        // 建立FileInfo物件
        FileInfo FileInfo = new FileInfo(Path);
        if (FileInfo.Exists)
        {
            FileInfo.Delete();   // 刪除檔案
            Response.Write("已經刪除指定的檔案");
        }
        else
            Response.Write("您所指定的檔案不存在，故無法執行刪除動作！");
    }
}