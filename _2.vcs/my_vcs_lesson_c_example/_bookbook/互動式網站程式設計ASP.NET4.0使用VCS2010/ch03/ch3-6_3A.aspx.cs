using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_3A : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        Response.Write("題目：利用亂數函數投擲骰子100次" + "<br>");
    }
    protected void Button1_Click(object sender, EventArgs e)
    {
        Random r = new Random();
        int[] A = new int[7];
        int i, j, Point_Num;
        for (i = 1; i <= 100; i++)
        {
            Point_Num = r.Next(1, 7);
            A[Point_Num] = A[Point_Num] + 1;
        }
        for (j = 1; j <= 6; j++)
            Response.Write(j + "點" + "　" + A[j] + "次" + "<br>");
    }
}