using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch7_1_3A : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        double Chi_Score = 77.5;
        int Eng_Score = 90;
        double Math_Score = 85;
        double Total, Aver;
        Response.Write("您的國文成績：" + Chi_Score + "<br>");
        Response.Write("您的英文成績：" + Eng_Score + "<br>");
        Response.Write("您的數學成績：" + Math_Score + "<br>");
        Response.End();  //強迫網頁結束
        Total = Chi_Score + Eng_Score + Math_Score;
        Aver = Total / 3;
        Response.Write("您的總分：" + Total);
        Response.Write("您的平均成績：" + Aver);
    }
}