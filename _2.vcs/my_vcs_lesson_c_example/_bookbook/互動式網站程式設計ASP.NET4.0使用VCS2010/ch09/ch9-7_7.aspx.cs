using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class ch9_7_7 : System.Web.UI.Page
{
    protected void GridView1_RowCommand(object sender, GridViewCommandEventArgs e)
    {
        int RowIndex = Convert.ToInt32(e.CommandArgument);
        string Stu_Name = GridView1.Rows[RowIndex].Cells[2].Text;
        int DB_Score = int.Parse(GridView1.Rows[RowIndex].Cells[4].Text);
        int SA_Score = int.Parse(GridView1.Rows[RowIndex].Cells[5].Text);
        int ASP_NET_Score = int.Parse(GridView1.Rows[RowIndex].Cells[6].Text);
        int PC_Score = int.Parse(GridView1.Rows[RowIndex].Cells[7].Text);
        int Sum = DB_Score + SA_Score + ASP_NET_Score + PC_Score;
        if (e.CommandName == "Sum")
            Label1.Text = Stu_Name + " 同學的總分為：" + Sum;
    }
}