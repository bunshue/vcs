using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ShieldRightKeyCarte
{
    class CustomTextBoxGroup:TextBox 
    {
        public CustomTextBoxGroup()
        {
            this.Top = 75;//设定自定义控件上边缘与其容器的工作区上边缘之间的距离
            this.Left = 115;//设定自定义控件左边缘与其容器的工作区左边缘之间的距离
            this.Width = 180;//设定自定义控件的宽度
            this.Height = 50;//设定自定义控件的高度
        }

        #region 本程序中需声明的变量
        private const int WM_RBUTTONDOWN = 0x0204;//该变量表示鼠标右键的信息
        private const int WM_GETTEXT = 0x000d;//该变量表示从文本框中获取文本的信息
        private const int WM_CONTEXTMENU = 0x007B;//该变量表示右键菜单的信息
        #endregion

        protected override void WndProc(ref Message m)
        {
            if(m.Msg == WM_RBUTTONDOWN || m.Msg == WM_GETTEXT || m.Msg == WM_CONTEXTMENU)//当当前处理的信息为鼠标右键、从文本框中获取文本、右键菜单以及复制信息时
            {
                return;//直接返回，不进行处理
            }
            base.WndProc(ref m);//处理下一条信息
        }
    }
}
