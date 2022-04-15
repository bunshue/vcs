/*
 * CRectTrackerCS_Demo 2.1
 * 作者：天津 赵春生
 * 制作时间：17:55 2007-06-01
 * 主页：http://timw.yeah.net or http://timw.126.com
 *	本程序代码测试环境：
 * WinXP (Professional SP2)
 * Microsoft Visual Studio 2005 (Installed Edition: C# Express)
 * Version 8.0.50727.762  (SP.050727-7600)
 * Microsoft .NET Framework
 * Version 2.0.50727
*/

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using CustomCRectTrackerCS;//导入CRectTrackerCS

namespace CRectTrackerCS2.__Demo
{
    public partial class Form1 : Form
    {
        CRectTrackerCS TestRubberBand = new CRectTrackerCS();//创建实例

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //避免生成矩形框后出现的闪烁
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer |
                    ControlStyles.ResizeRedraw |
                    ControlStyles.AllPaintingInWmPaint, true);

            //TestRubberBand.Test();
            TestRubberBand.Create();
            timer1.Start();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            TestRubberBand.StartPoint(this, e);//TestRubberBand起始点
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            TestRubberBand.EndPoint(this, e);//TestRubberBand结束点
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            TestRubberBand.TrackRubberBand(this, e);//鼠标拖拽时实时显示TestRubberBand

            //实时显示TestRubberBand的参数
            label1.Text = "RubberBand:" + " X=" + TestRubberBand.X.ToString() + " Y=" + TestRubberBand.Y.ToString()
                + " Width=" + TestRubberBand.Width.ToString() + " Height=" + TestRubberBand.Height.ToString();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            TestRubberBand.DrawRubberBand(this, e);//绘制TestRubberBand
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //this.Invalidate(null, true);
            this.Invalidate(TestRubberBand.InvalidateRectangle(), true);//只刷新TestRubberBand周围的区域
        }

        private void ResizePinNoHide_CheckedChanged(object sender, EventArgs e)
        {
            //不隐藏ResizePin
            TestRubberBand.SetRubberBandStyle(CRectTrackerCS.StyleFlags.ResizePinNoHide);
        }

        private void ResizePinAutoHide_CheckedChanged(object sender, EventArgs e)
        {
            //自动隐藏ResizePin，可随时用鼠标激活
            TestRubberBand.SetRubberBandStyle(CRectTrackerCS.StyleFlags.ResizePinAutoHide);
        }

        private void ResizePinAlwaysHide_CheckedChanged(object sender, EventArgs e)
        {
            //始终隐藏ResizePin
            TestRubberBand.SetRubberBandStyle(CRectTrackerCS.StyleFlags.ResizePinAlwaysHide);
        }

        private void SolidLine_CheckedChanged(object sender, EventArgs e)
        {
            //实线绘制RubberBand
            TestRubberBand.SetRubberBandStyle(CRectTrackerCS.StyleFlags.SolidLine);
        }

        private void DottedLine_CheckedChanged(object sender, EventArgs e)
        {
            //虚线绘制RubberBand
            TestRubberBand.SetRubberBandStyle(CRectTrackerCS.StyleFlags.DottedLine);
        }

        private void ChangeRubberBandColor_Click(object sender, EventArgs e)
        {
            //设置：RubberBand颜色为Red；ResizePin颜色为Gold
            TestRubberBand.SetRubberBandStyle(Color.Red, Color.Gold);
        }

        private void LoadDefaultsRubberBandStyle_Click(object sender, EventArgs e)
        {
            //加载RubberBand默认风格
            TestRubberBand.LoadDefaultRubberBandStyle();
        }
    }
}
