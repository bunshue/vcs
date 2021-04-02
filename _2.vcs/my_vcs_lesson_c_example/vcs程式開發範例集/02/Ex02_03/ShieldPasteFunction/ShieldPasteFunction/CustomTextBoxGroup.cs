using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ShieldPasteFunction
{
    class CustomTextBoxGroup:TextBox 
    {
        public CustomTextBoxGroup()
        {
            this.Top = 63;//设定自定义控件上边缘与其容器的工作区上边缘之间的距离
            this.Left = 105;//设定自定义控件左边缘与其容器的工作区左边缘之间的距离
            this.Width = 178;//设定自定义控件的宽度
            this.Height = 50;//设定自定义控件的高度
        }

        protected override void WndProc(ref Message m)
        {
            const int WM_RBUTTONDOWN = 0x0204;//该变量表示鼠标右键的信息
            const int WM_GETTEXT = 0x000d;//该变量表示从文本框中获取文本的信息
            const int WM_CONTEXTMENU = 0x007B;//该变量表示右键菜单的信息
            const int WM_PASTE = 0x0302;//该变量表示有关粘贴的信息

            if(m.Msg == WM_RBUTTONDOWN || m.Msg == WM_GETTEXT || m.Msg == WM_CONTEXTMENU || m.Msg == WM_PASTE)//当当前处理的信息为鼠标右键、从文本框中获取文本、右键菜单以及粘贴信息时
            {
                return;//直接返回，不进行处理
            }
            base.WndProc(ref m);//处理下一条信息
        }
    }
}
