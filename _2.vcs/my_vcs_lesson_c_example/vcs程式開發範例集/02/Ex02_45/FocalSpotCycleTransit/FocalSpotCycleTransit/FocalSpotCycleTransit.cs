using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace FocalSpotCycleTransit
{
    public partial class FocalSpotCycleTransit : Form
    {
        public FocalSpotCycleTransit()
        {
            InitializeComponent();
        }
        private void AllControl_Enter(object sender, EventArgs e)
        {
            ((TextBox)sender).BackColor = Color.CornflowerBlue;//當當前控件成為活動控件時設置它的背景顏色為藍色
        }

        private void AllControl_Leave(object sender, EventArgs e)
        {
            ((TextBox)sender).BackColor = Color.White;//當當前控件成為不活動控件時設置它的背景顏色為白色
        }

        private void AllControl_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyValue == 13) //當按下「Enter」鍵時
            {
                int n = Convert.ToInt32(((TextBox)sender).Tag.ToString());//獲取控件標識
                Clear_Control(this.Controls, n, 6); //進入下一個控件
            }
        }
        #region  遍歷指定的控件
        /// <summary>
        /// 遍歷指定的控件
        /// </summary>
        /// <param Con="ControlCollection">可視化控件</param>
        /// <param n="int">控件標識</param>
        /// <param m="int">最大標識</param>
        public void Clear_Control(Control.ControlCollection Con, int n, int m)
        {
            int tem_n = 0;//初始化一個int型變量
            foreach (Control C in Con)//遍歷可視化組件中的所有控件
            {
                if (C.GetType().Name == "TextBox")  //判斷是否為TextBox控件
                {
                    if (n == m)//當循環至最後一個控件時
                        tem_n = 1;//設置控件標識的值為1
                    else //當沒有循環到最後一個控件時
                        tem_n = n + 1;//使控件的標識值遞增1
                    if (Convert.ToInt32(((TextBox)C).Tag.ToString()) == tem_n)//當與當前控件關聯的數據對像為下一個控件時
                        ((TextBox)C).Focus();//為當前控件設置焦點
                }
            }
        }
        #endregion

        private void FocalSpotCycleTransit_Load(object sender, EventArgs e)
        {

        }

    }
}
