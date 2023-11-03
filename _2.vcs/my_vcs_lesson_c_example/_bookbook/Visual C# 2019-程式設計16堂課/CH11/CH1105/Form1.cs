using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1105
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int kind, ticket;  //車票種類(kind)和票數(ticket)
        string msg, msg2;  //取得RadioButton的Text屬性值

        //共用物件：rabTicket處理車票，rabVarious處理票數
        private RadioButton rabTicket;
        private RadioButton rabVarious;

        private void btnInfo_Click(object sender, EventArgs e)
        {
            if (msg == "一般")
            {
                kind = 1_242;   //一般票價為1242
                Paymoney(kind, msg2);   //呼叫方法計算票價
            }
            else
            {
                kind = 1_635;   //商務票價1635
                Paymoney(kind, msg2);   //呼叫方法計算票價
            }
        }

        //RadioButton共用事件-車票選一般或商務
        private void rabTicket_CheckedChanged(object sender,
              EventArgs e)
        {
            //以as運算子將參數sender接收的物件轉為RadioButton
            RadioButton choiceTicket = sender as RadioButton;

            //當控制項rabNormal、rabSpecial有一個被選取
            if (choiceTicket.Checked)
            {
                //取得被選取RadioButton和Text屬性值
                rabTicket = choiceTicket;
                msg = rabTicket.Text;
            }
        }

        //RadioButton共用事件-車票買1？2？3張
        private void rabVarious_CheckedChanged(
              object sender, EventArgs e)
        {
            RadioButton number = sender as RadioButton;

            //當rabOne、rabTwo、rabThree有一個被選取
            if (number.Checked)
            {
                //取得被選取RadioButton和Text屬性值
                rabVarious = number;
                msg2 = rabVarious.Text;
            }
        }
        //方法-依接收的車票種類(kd)和票數(msg)來計算票價
        private void Paymoney(int kd, string info)
        {
            if (info == "1張")
            {
                ticket = 1;
                lblTotal.Text = $"新台幣 {kd * ticket}元";
            }
            else if (info == "2張")
            {
                ticket = 2;
                lblTotal.Text = $"新台幣 {kd * ticket}元";
            }
            else
            {
                ticket = 3;
                lblTotal.Text = $"新台幣 {kind * ticket}元";
            }
        }
    }
}