using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CH1003
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        /* 滑鼠事件順序 MouseEnter > Mouse > Mouse Hover
           當按鈕無作用，對滑鼠事件也會無反應 */

        //滑鼠靠近控制項
        private void btnStandard_MouseEnter(object sender,
              EventArgs e)
        {
            lblShow.Text = "FlatStyle : Standard, 滑鼠靠近了...";
        }

        //移動滑鼠
        private void btnFlat_MouseMove(object sender,
              MouseEventArgs e)
        {
            lblShow.Text = "FlatStyle : Flat, 滑鼠移動了...";
        }

        //控制項有滑鼠停留
        private void btnPopup_MouseHover(object sender,
              EventArgs e)
        {
            lblShow.Text = "FlatStyle : Popup, 滑鼠停留在控制項...";
        }

        //依據輸人數值顯示屬性FlatStyle
        private void btnOK_Click(object sender, EventArgs e)
        {
            //取得文字方塊輸入的字串轉為byte型別
            byte style = byte.Parse(txtNumber.Text);
            //依據輸入數值來讓某個按鈕有作用(Enable為true)
            if (style == 1)
                btnStandard.Enabled = true;
            else if (style == 2)
                btnFlat.Enabled = true;
            else
                btnPopup.Enabled = true;
        }
    }
}
