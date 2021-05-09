using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_6_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int Score = 50;
        if (Score < 60)
        {
            Response.Write("您必須補考" + "<br>");
            Response.Write("請再多加油哦！" + "<br>");
            Response.Write("希望補考能夠順利通過");
        }
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        int Score = 50;
        if (Score >= 60)
            Response.Write("及格");
        else
            Response.Write("不及格");
    }

    protected void Button3_Click(object sender, EventArgs e)
    {
        int aver = 50;
        String result;
        if (aver < 60)
            result = "要重修了";
        else if (aver >= 60 && aver < 70)
            result = "丙等生";
        else if (aver >= 70 && aver < 80)
            result = "乙等生";
        else if (aver >= 80 && aver < 90)
            result = "甲等生";
        else
            result = "優等生";
        Response.Write(result);
    }

    protected void Button4_Click(object sender, EventArgs e)
    {
        int aver = 90;
        String result;
        switch ((int)(aver / 10))
        {
            case 10:
            case 9:
                result = "優等生";
                break;
            case 8:
                result = "甲等生";
                break;
            case 7:
                result = "乙等生";
                break;
            case 6:
                result = "丙等生";
                break;
            default:
                result = "要重修了";
                break;
        }
        Response.Write(result);
    }

    protected void Button5_Click(object sender, EventArgs e)
    {
        int aver = 90;
        int vb = 100;
        string result;
        if (aver >= 80)
        {
            if (vb == 100)
                result = "你學業成績不錯，VB程式設計更是高手!!!";
            else
                result = "你學業成績不錯";
        }
        else
            result = "你學業成績還需加油!!!";
        Response.Write(result);
    }
    protected void Page_Load(object sender, EventArgs e)
    {
        double score = 60.5;
        int c;
        //處理
        c = score;
        //輸出
        Response.Write("平均成績為：" + c);
    }
}