using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_SelectionRectangle
{
    public partial class Form1 : Form
    {
        //方法一
        SelectionRec1 selectionRec1 = new SelectionRec1();

        //方法二
        SelectionRec2 selectionRec2 = new SelectionRec2();
        int ResizePin_Style = 1;	//0: 不隱藏, 1: 自動隱藏, 2 : 總是隱藏
        int ResizeLine_Style = 1;	//0: 實線, 1: 虛線

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            selectionRec1.ResizePinSize = 10;  //改變ResizePin圓直徑大小
            selectionRec1.Create();

            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            pictureBox1.Image = Image.FromFile(filename);


            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);


            //方法二
            //避免生成矩形框後出現的閃爍
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.ResizeRedraw | ControlStyles.AllPaintingInWmPaint, true);

            selectionRec2.Create();
            timer2.Start();

            if (ResizePin_Style == 0)
            {
                //不隐藏ResizePin
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.ResizePinNoHide);
            }
            else if (ResizePin_Style == 1)
            {
                //自动隐藏ResizePin，可随时用鼠标激活
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.ResizePinAutoHide);
            }
            else if (ResizePin_Style == 2)
            {
                //始终隐藏ResizePin
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.ResizePinAlwaysHide);
            }
            else
            {
                //不隐藏ResizePin
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.ResizePinNoHide);
            }


            if (ResizeLine_Style == 0)
            {
                //实线绘制RubberBand
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.SolidLine);
            }
            else if (ResizeLine_Style == 1)
            {
                //虚线绘制RubberBand
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.DottedLine);
            }
            else
            {
                //实线绘制RubberBand
                selectionRec2.SetRubberBandStyle(SelectionRec2.StyleFlags.SolidLine);
            }

            pictureBox2.Image = Image.FromFile(filename);
            pictureBox2.MouseDown += new MouseEventHandler(pictureBox2_MouseDown);
            pictureBox2.MouseMove += new MouseEventHandler(pictureBox2_MouseMove);
            pictureBox2.MouseUp += new MouseEventHandler(pictureBox2_MouseUp);
            pictureBox2.Paint += new PaintEventHandler(pictureBox2_Paint);
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            selectionRec1.StartPoint(pictureBox1, e);
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            selectionRec1.TrackRubberBand(pictureBox1, e);

            lb_info1.Text = "(" + e.X.ToString() + ", " + e.Y.ToString() + ")\n"
                + "x = " + selectionRec1.X.ToString() + ", y = " + selectionRec1.Y.ToString();
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            selectionRec1.EndPoint(pictureBox1, e);
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            selectionRec1.DrawRubberBand(pictureBox1, e);
        }





        //方法二

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            selectionRec2.StartPoint(this, e);//selectionRec2起始点
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            selectionRec2.TrackRubberBand(this, e);//鼠标拖拽时实时显示selectionRec2

            lb_info2.Text = "(" + e.X.ToString() + ", " + e.Y.ToString() + ")\n"
                + "x = " + selectionRec2.X.ToString() + ", y = " + selectionRec2.Y.ToString()
                + "\nW = " + selectionRec2.Width.ToString() + ", H = " + selectionRec2.Height.ToString();
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
            selectionRec2.EndPoint(this, e);//selectionRec2结束点
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            selectionRec2.DrawRubberBand(this, e);//绘制selectionRec2
        }





        private void timer2_Tick(object sender, EventArgs e)
        {
            //this.Invalidate(null, true);
            this.pictureBox2.Invalidate(selectionRec2.InvalidateRectangle(), true);//只刷新selectionRec2周围的区域

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //改變邊框顏色
            //设置：RubberBand颜色为Red；ResizePin颜色为Gold
            selectionRec2.SetRubberBandStyle(Color.Red, Color.Gold);


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用預設邊框顏色
            //加载RubberBand默认风格
            selectionRec2.LoadDefaultRubberBandStyle();

        }




    }
}
