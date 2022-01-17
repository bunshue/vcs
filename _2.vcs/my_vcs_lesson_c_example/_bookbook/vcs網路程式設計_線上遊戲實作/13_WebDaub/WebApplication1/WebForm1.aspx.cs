using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {   
        //資訊定時接收
        protected void Timer1_Tick(object sender, EventArgs e)
        {
            if (H1.Value.Length > 0)
            {
                if (TextBox2.Text != "")                  //如有設定發送對象
                {
                    Application[TextBox2.Text] = H1.Value;//送出
                    H1.Value = "";                        //清除資訊
                }
            }
            if (TextBox1.Text != "")                                 //如有設定身分
            {
                if (Application[TextBox1.Text] != null)              //如有訊息送達
                {
                    H2.Value = Application[TextBox1.Text].ToString();//接收資訊送至網頁
                    Application[TextBox1.Text] = null;               //清除訊息
                }
            }
        }
    }
}