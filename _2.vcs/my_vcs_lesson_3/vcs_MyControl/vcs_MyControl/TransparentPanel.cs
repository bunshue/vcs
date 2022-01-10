using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

//C# 透明背景Panel, 透明圖像, PitureBox透明效果
//1、自定義透明 背景Panel控件：在項目中添加類 TransparentPanel.cs
//2、F5編譯運行一次 後，可在工具欄找到控件TransparentPanel。
//之後添加控件到窗體Form, 設置其Image屬性，為帶有透明度信息的*.png圖像即可看到示意圖中的透明效果。

using System.Windows.Forms;
using System.Drawing;

namespace vcs_MyControl
{
    public class TransparentPanel : Control
    {
        public TransparentPanel() { }

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            //不進行背景的繪制
        }

        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams cp = base.CreateParams;
                cp.ExStyle |= 0x00000020; //WS_EX_TRANSPARENT
                return cp;
            }
        }

        protected override void OnPaint(System.Windows.Forms.PaintEventArgs e)
        {
            //繪制panel的背景圖像
            if (BackgroundImage != null) e.Graphics.DrawImage(this.BackgroundImage, new Point(0, 0));
        }

        ////為控件添加自定義屬性值num1
        //private int num1 = 1;

        //[Bindable(true), Category("自定義屬性欄"), DefaultValue(1), Description("此處為自定義屬性Attr1的說明信息！")]
        //public int Attr1
        //{
        //    get { return num1; }
        //    set { this.Invalidate(); }
        //}
    }
}
