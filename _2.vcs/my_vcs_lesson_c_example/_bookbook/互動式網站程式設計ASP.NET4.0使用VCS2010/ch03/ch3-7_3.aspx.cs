using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_7_3 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        int[] A = new int[5];
        int i, sum;
        A[0] = 50; A[1] = 60; A[2] = 70; A[3] = 80; A[4] = 90;
        sum = A[0] + A[1] + A[2] + A[3] + A[4];
        Label1.Text = "總和為：" + sum;
    }

    protected void Button2_Click(object sender, EventArgs e)
    {
        int[] A = new int[5];
        int i, sum = 0;
        A[0] = 50; A[1] = 60; A[2] = 70; A[3] = 80; A[4] = 90;
        for (i = 0; i <= 4; i++)
            sum = sum + A[i];
        Label1.Text = "總和為：" + sum;
    }
}