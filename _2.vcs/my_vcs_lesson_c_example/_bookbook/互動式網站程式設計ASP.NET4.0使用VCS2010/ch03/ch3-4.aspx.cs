using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_4 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        // ===設計一個求圓面積與圓周長的程式===
        //宣告變數
        double A;                      //宣告「圓面積」變數
        double L;                      //宣告「圓周長」變數
        int R;                         //宣告「半徑」變數
        const double PI = 3.14;        //宣告「圓周率」為.14的常數
        R = 3;                         //初值設定
        //處理
        A = PI * (Math.Pow(R, 2));      //計算圓面積
        L = 2 * PI * R;                //計算圓周長
        //輸出
        Response.Write("圓面積=" + A);
        Response.Write("<br/>");       //換行
        Response.Write("圓周長=" + L);
    }
}