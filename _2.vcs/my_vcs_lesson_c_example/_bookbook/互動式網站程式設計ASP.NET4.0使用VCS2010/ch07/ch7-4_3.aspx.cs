using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;


public partial class ch7_4_3 : System.Web.UI.Page
{
    static string GCount(int Counter)
    {
        int i, SCounter;
        string cimg = "";
        SCounter = Counter;
        string Str = Convert.ToString(SCounter);
        for (i = 0; i <= Str.Length - 1; i++)
        { 
            //載入數字的圖片            
            cimg = cimg + "<IMG SRC=images/" + Str.Substring(i, 1) + ".bmp>";
        } 
        return cimg;
    }

    protected void Page_Load(object sender, EventArgs e)
    {
        //圖形化計數器                    
        Application["ArriveCounter"] = Convert.ToInt32(Application["ArriveCounter"]) + 1;
        //顯示圖形化計數器的函數    
        Response.Write("《這是一個圖形化計數器》" + "<br>");
        Response.Write("你是本站的第" + GCount(Convert.ToInt32(Application["ArriveCounter"])) + "位貴賓");
    }
}

