using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch3_1_2 : System.Web.UI.Page
{
    protected void Button1_Click(object sender, EventArgs e)
    {
        string Stu_Name;
        Single Chi_Score, Eng_Score, Aver;
        Stu_Name = TextBox1.Text;
        Chi_Score = int.Parse(TextBox2.Text);
        Eng_Score = int.Parse(TextBox3.Text);
        Aver = (Chi_Score + Eng_Score) / 2;
        Label1.Text = Stu_Name + "==>" + Aver + "分";
    }
}