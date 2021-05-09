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
    protected void ListBox1_SelectedIndexChanged(object sender, EventArgs e)
    {
        string Temp = "";
        int i;
        //用迴圈從 ListBox1 由前至後逐一讀取各項目
        for (i = 0; i <= ListBox1.Items.Count - 1; i++)
        //若 Selected 屬性為 True，表示使用者已選擇此項
        {
            if (ListBox1.Items[i].Selected)
                Temp += ListBox1.Items[i].Value + " ";
        }
        Label1.Text = Temp;
    }
}