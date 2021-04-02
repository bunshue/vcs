using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SelfDefiningScrollBar
{
    public partial class SelfDefiningScrollBar : Form
    {
        public SelfDefiningScrollBar()
        {
            InitializeComponent();
        }

        private static int oldValue = 0;//定义全局静态变量用来保存滚动条的初始值
        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            float currentValue = Math.Abs(vScrollBar1.Value - oldValue);//该变量表示当前滚动条中的值
            float temp = ScrollBarPercentage(richTextBox1.Height + 50); //为临时变量temp赋值
            if(vScrollBar1.Value > oldValue) //当向下滚动时
            {
                richTextBox1.Top -= (int)(temp * currentValue);//定义RichTextBox控件的上边距与其工作区容器上边距间的距离
            }
            else if(vScrollBar1.Value < oldValue)//当滚动条向上滚动时
            {
                richTextBox1.Top += (int)(temp * currentValue);//定义RichTextBox控件的上边距与其工作区容器上边距间的距离
            }
            oldValue = vScrollBar1.Value;//设置oldValue值为滚动条的当前值

        }
        private float ScrollBarPercentage(float height)
        {
            float divisor = (float)(20);//将整型转化为浮点型
            float wholeValue = height - vScrollBar1.Height;//获取滚动条的全值
            return (wholeValue / divisor);//获取滚动条移动时每移动一部分所占的百分比
        }
    }
}
