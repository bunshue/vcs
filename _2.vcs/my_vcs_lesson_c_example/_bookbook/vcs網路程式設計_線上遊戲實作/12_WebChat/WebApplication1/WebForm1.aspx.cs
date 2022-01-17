using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Collections;//集合物件

namespace WebApplication1
{
    public partial class WebForm1 : System.Web.UI.Page
    {
        //登入與登出 
        protected void Button1_Click(object sender, EventArgs e)
        {
            if (Button1.Text == "上線")                          //嘗試上線
            {
                if (TextBox2.Text != "")                        //有寫名字
                {
                    Session[TextBox2.Text] = TextBox2.Text;     //記錄上線名稱
                    Application.Lock();                         //鎖定網站公用變數
                    Hashtable L = (Hashtable)Application["L"];  //取得線上名單
                    L.Add(Session[TextBox2.Text], DateTime.Now); //加自己到線上名單(名稱，時間)
                    Application.UnLock();               //解除鎖定
                    Button1.Text = "離線";              //已上線顯示功能為離線
                }
            }
            else
            {
                Application.Lock();                        //鎖定網站公用變數
                Hashtable L = (Hashtable)Application["L"]; //取得線上名單
                L.Remove(Session[TextBox2.Text]);          //移除名單中的我
                Application.UnLock();                      //解除鎖定
                Session[TextBox2.Text] = null;             //清除上線名稱
                Button1.Text = "上線";                     //已離線示功能為上線
            }
        }
        //發言 
        protected void Button2_Click(object sender, EventArgs e)
        {
            if (!(Session[TextBox2.Text] == null))              //已上線
            {
                Application.Lock();                             //鎖定網站公用變數
                Queue Q = (Queue)Application["Q"];              //取得目前發言內容
                Q.Enqueue(TextBox2.Text + ":" + TextBox3.Text); //加入我的發言
                while (Q.Count > 5)                             //保存五筆資料
                {
                    Q.Dequeue();                                //刪除最舊的資料
                }
                Application.UnLock();                           //解除鎖定
            }
        }
        //定時更新 
        protected void Timer1_Tick(object sender, EventArgs e)
        {
            //更新發言
            Queue Q = (Queue)Application["Q"]; //取得目前發言內容
            TextBox1.Text = "";                //清除看板
            foreach (var i in Q)
            {
                TextBox1.Text += i + "\r\n";   //一一顯示留言
            }
            //更新線上名單
            Application.Lock();                         //鎖定網站公用變數
            Hashtable L = (Hashtable)Application["L"];  //取得線上名單
            if (!(Session[TextBox2.Text] == null))      //已上線
            {
                if (L[Session[TextBox2.Text]] == null)  //如果我不在名單內
                {
                    L.Add(Session[TextBox2.Text], DateTime.Now); //重新上線我自己
                }
                else
                {
                    L[Session[TextBox2.Text]] = DateTime.Now;    //打卡更新時間
                }
            }
            Application.UnLock();                       //解除鎖定
            ListBox1.Items.Clear();                     //清除名單顯示
            //在ListBox中一一顯示名單
            foreach (var i in L.Keys)
            {
                ListBox1.Items.Add(i.ToString());
            }
        }
    }
}