using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Printing;
using System.Drawing.Drawing2D;
using System.Runtime.InteropServices;   //计算屏幕像素大小和mm大小引用

//參考 https://blog.csdn.net/zhangsongshan/article/details/4840889
//不用 SetProperty

namespace vcs_Form9_RulerAndGrid
{
    public partial class Form1 : Form
    {
        public Control useControl;
        private TextBox lineX = new TextBox();
        private TextBox lineY = new TextBox();
        private TextBox rectangleX = new TextBox();
        private TextBox rectangleY = new TextBox();
        Pen penG = new Pen(Color.Black);
        Pen penL = new Pen(Color.Red);
        Font font = new Font("宋体", 8);

        public Panel panel1 = new Panel();
        //每毫米占的像素数
        float pxwidth;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            panel1.Left = 21;
            panel1.Top = 21;
            panel1.Width = RulerWidth - 42;
            panel1.Height = RulerHeight - 42;
            panel1.BackColor = Color.White;
            panel1.MouseMove += new MouseEventHandler(panel1_MouseMove);
            panel1.MouseUp += new MouseEventHandler(panel1_MouseUp);
            panel1.Paint += new PaintEventHandler(panel1_Paint);
            lineX.Width = 1;
            lineX.Height = 14;
            lineX.Top = 6;
            lineX.BackColor = Color.Red;
            lineX.Multiline = true;
            lineX.Visible = false;
            this.Controls.Add(lineX);
            lineY.Width = 14;
            lineY.Height = 1;
            lineY.Left = 6;
            lineY.BackColor = Color.Red;
            lineY.Multiline = true;
            lineY.Visible = false;
            this.Controls.Add(lineY);
            rectangleX.Height = 6;
            rectangleX.Top = 14;
            rectangleX.BackColor = Color.Black;
            rectangleX.Multiline = true;
            rectangleX.Visible = false;
            this.Controls.Add(rectangleX);
            rectangleY.Width = 6;
            rectangleY.Left = 14;
            rectangleY.BackColor = Color.Black;
            rectangleY.Multiline = true;
            rectangleY.Visible = false;
            this.Controls.Add(rectangleY);
            this.Controls.Add(panel1);
            Calcsale();


        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics PenGraphics = e.Graphics;
            InitializeGraph(PenGraphics);


        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            DrawGrid();
        }

        private void useControl_MouseClick(object sender, MouseEventArgs e)
        {

        }

        private void ChangePanelSize()
        {
            panel1.Width = RulerWidth - 42;
            panel1.Height = RulerHeight - 42;
        }

        private void panel1_MouseMove(object sender, MouseEventArgs e)
        {
            if (useControl != null)
            {
                panel1.Cursor = Cursors.Cross;
            }
            else
            {
                panel1.Cursor = Cursors.Default;
            }
            lineX.Left = e.X + 21;
            lineX.Visible = true;
            lineY.Top = e.Y + 21;
            lineY.Visible = true;
        }

        private void panel1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                /*
                SetProperty sp = new SetProperty();
                sp.rad = this;
                sp.ShowDialog();
                */
            }
            else
            {
                if (useControl != null)
                {
                    useControl.MouseClick += new MouseEventHandler(useControl_MouseClick);
                    useControl.Top = e.Y;
                    useControl.Left = e.X;
                    panel1.Controls.Add(useControl);
                    panel1.Cursor = Cursors.Default;
                    rectangleX.Left = e.X + 21;
                    rectangleX.Width = useControl.Width;
                    rectangleX.Visible = true;
                    rectangleY.Top = e.Y + 21;
                    rectangleY.Height = useControl.Height;
                    rectangleY.Visible = true;
                    useControl = null;
                }
            }
        }



        [Browsable(true), Category("直尺尺寸"), Description("直尺长")]
        public int RulerWidth
        {
            get
            {
                return this.Width;
            }
            set
            {
                this.Width = value;
                this.Refresh();
                ChangePanelSize();
            }
        }


        [Browsable(true), Category("直尺尺寸"), Description("直尺宽")]
        public int RulerHeight
        {
            get
            {
                return this.Height;
            }
            set
            {
                this.Height = value;
                this.Refresh();
                ChangePanelSize();
            }
        }

        //定义一个显示刻度的单位的属性，单位是毫米或英寸
        public enum scaletype
        {
            centimeter = 0, inch = 1
        }
        scaletype usescale = scaletype.centimeter;
        [Browsable(true), Category("用户属性"), Description("设置显示单位，厘米或英寸")]
        public scaletype Unit
        {
            get
            {
                return usescale;
            }
            set
            {
                usescale = value;
                this.Refresh();
            }
        }
        //定义网格显示多少刻度的值
        public enum GridUnitValue
        {
            One = 1, Two = 2, Three = 3, Four = 4, Five = 5
        }
        GridUnitValue useGirdUnit = GridUnitValue.Five;
        [Browsable(true), Category("用户属性"), Description("设置每格网格所占的刻度数")]
        public GridUnitValue GridUnit
        {
            get
            {
                return useGirdUnit;
            }
            set
            {
                useGirdUnit = value;
                this.Refresh();
            }
        }
        //定义一个按比例放大/缩小刻度的属性，该属性是缩放的系数
        float c = 1.0f;
        [Browsable(true), Category("用户属性"), Description("设置显示比例")]
        public float Coefficient
        {
            get
            {
                return c;
            }
            set
            {
                c = value;
                this.Refresh();
            }
        }

        [DllImport("gdi32.dll")]
        public static extern int GetDeviceCaps(IntPtr hdc, int Index);
        /// <summary>
        /// 计算精度 确保在不同分辨率的机子上刻度的准确性
        /// </summary>
        private void Calcsale()
        {
            PictureBox p = new PictureBox();
            Graphics g = Graphics.FromHwnd(p.Handle);
            IntPtr hdc = g.GetHdc();
            //GetDeviceCaps(hdc, 4)方法中，第二个参数意义：4毫米为单位屏幕宽度，6毫米为单位屏幕高度，8像素为单位的屏幕宽度10像素为单位的屏幕高度
            int width = GetDeviceCaps(hdc, 4);
            int pix = GetDeviceCaps(hdc, 8);
            pxwidth = pix / width;
        }

        //定义一个设置横轴起始刻度值的属性
        private double checkPaperWidth = 0;
        [Browsable(true), Category("用户属性"), Description("设置刻度尺横轴刻度的起始值")]
        public double StartX
        {
            get
            {
                return checkPaperWidth;
            }
            set
            {
                checkPaperWidth = value;
                this.Refresh();
            }
        }

        //定义一个设置纵轴起始刻度值的属性
        private double checkPaperHeight = 0;
        [Browsable(true), Category("用户属性"), Description("设置刻度尺纵轴刻度的起始值")]
        public double StartY
        {
            get
            {
                return checkPaperHeight;
            }
            set
            {
                checkPaperHeight = value;
                this.Refresh();
            }
        }

        //定义一个当控件内部图形发生变化的时候触发的事件
        public delegate void PaperChangeHandle();
        private PaperChangeHandle PaperChanged;
        [Browsable(true), Category("用户事件"), Description("当控件内部图形发生变化的时候触发")]
        public event PaperChangeHandle OnPaperChanged
        {
            add
            {
                PaperChanged += value;
            }
            remove
            {
                PaperChanged -= value;
            }
        }

        private void InitializeGraph(Graphics Gph)
        {
            //画竖线
            //Gph.DrawLine(penG, 20, 20, 20, height - 20);
            //Gph.DrawLine(penG, height - 20, 20, height - 20, height - 20);
            //画横线
            //Gph.DrawLine(penG, 20, 20, width - 20, 20);
            //Gph.DrawLine(penG, 20, width - 20, width - 20, height - 20);

            Rectangle curRect = new Rectangle(20, 20, RulerWidth - 40, RulerHeight - 40);
            Gph.DrawRectangle(penG, curRect);

            SetXAxis(ref Gph);
            SetYAxis(ref Gph);
        }

        ///<summary>
        /// 设置画图板横轴的刻度。
        ///</summary>
        ///<param name="objGraphics"></param>
        private void SetXAxis(ref Graphics objGraphics)
        {
            int x1 = 20;
            int y1 = 5;
            int x2 = 20;
            int y2 = 20;
            //刻度步长
            float scale = 0;
            float Scale = scale;
            // 判断当前的刻度数目标记
            int iCount = 0;
            double X = checkPaperWidth;
            // 设置横轴的刻度
            for (int i = 0; Scale <= RulerWidth - 40; i++)
            {
                if (iCount == 10)
                {
                    // 画出长刻度 长 15象素
                    objGraphics.DrawLine(penG, (x1 + Scale), y1, (x2 + Scale), y2);
                    objGraphics.DrawLine(penG, (x1 + Scale), RulerHeight - 5, (x2 + Scale), RulerHeight - 20);
                    iCount = 0;

                    // 标出刻度上的数字
                    X += 10;
                    objGraphics.DrawString(X.ToString(), font, new SolidBrush(Color.Black), (x1 + Scale - 15), 0);
                    objGraphics.DrawString(X.ToString(), font, new SolidBrush(Color.Black), (x1 + Scale - 15), RulerHeight - 10);
                }
                else if (iCount == 5)
                {
                    // 画中间刻度 长 9象素
                    objGraphics.DrawLine(penG, (x1 + Scale), y1 + 6, (x2 + Scale), y2);
                    objGraphics.DrawLine(penG, (x1 + Scale), RulerHeight - 11, (x2 + Scale), RulerHeight - 20);
                }
                else
                {
                    // 画短刻度 长 6象素
                    objGraphics.DrawLine(penG, (x1 + Scale), (y1 + 9), (x2 + Scale), y2);
                    objGraphics.DrawLine(penG, (x1 + Scale), RulerHeight - 14, (x2 + Scale), RulerHeight - 20);
                }

                iCount++;
                if (usescale == scaletype.centimeter)
                {
                    scale += pxwidth;
                    Scale = scale * c;
                }
                else
                {
                    scale += 2.54f * pxwidth;
                    Scale = scale * c;
                }
            }
        }
        /// <summary>
        /// 设置画图板纵轴的刻度。
        /// </summary>
        /// <param name="objGraphics"></param>
        private void SetYAxis(ref Graphics objGraphics)
        {
            int x1 = 5;
            int y1 = 20;
            int x2 = 20;
            int y2 = 20;
            int iCount = 0;
            float scale = 0;
            float Scale = scale;
            double Y = checkPaperHeight;
            //设置刻度上面显示数字垂直显示
            StringFormat stringFormat = new StringFormat();
            stringFormat.FormatFlags = StringFormatFlags.DirectionVertical;

            for (int i = 0; Scale <= RulerHeight - 40; i++)
            {
                if (iCount == 10)
                {
                    // 画出长刻度 长 15象素
                    objGraphics.DrawLine(penG, x1, (y1 + Scale), x2, (y2 + Scale));
                    objGraphics.DrawLine(penG, RulerWidth - 20, (y1 + Scale), RulerWidth - 5, (y2 + Scale));
                    iCount = 0;

                    //  标出刻度上的数字
                    Y += 10;
                    objGraphics.DrawString(Y.ToString(), font, new SolidBrush(Color.Black), 0, Scale + 8, stringFormat);
                    objGraphics.DrawString(Y.ToString(), font, new SolidBrush(Color.Black), RulerWidth - 14, Scale + 8, stringFormat);
                }
                else if (iCount == 5)
                {
                    // 画出短刻度 长 9象素
                    objGraphics.DrawLine(penG, (x1 + 6), (y1 + Scale), x2, (y2 + Scale));
                    objGraphics.DrawLine(penG, RulerWidth - 20, (y1 + Scale), RulerWidth - 11, (y2 + Scale));
                }
                else
                {
                    // 画出短刻度 长 6象素
                    objGraphics.DrawLine(penG, (x1 + 9), (y1 + Scale), x2, (y2 + Scale));
                    objGraphics.DrawLine(penG, RulerWidth - 20, (y1 + Scale), RulerWidth - 14, (y2 + Scale));
                }
                iCount++;
                if (usescale == scaletype.centimeter)
                {
                    scale += pxwidth;
                    Scale = scale * c;
                }
                else
                {
                    scale += 2.54f * pxwidth;
                    Scale = scale * c;
                }
            }
        }
        private void DrawGrid()
        {
            Pen p = new Pen(Color.Gray, 1);
            p.DashStyle = DashStyle.Dot;
            p.DashPattern = new float[] { 1, pxwidth * Convert.ToInt32(GridUnit) - 1 };
            Graphics gg = panel1.CreateGraphics();
            for (int i = 0; i < (RulerWidth - 40) / pxwidth; i++)
            {
                gg.DrawLine(p, -1, (pxwidth * i * (float)(Convert.ToInt32(GridUnit)) - 1), (panel1.Width), (pxwidth * i * (float)(Convert.ToInt32(GridUnit)) - 1));
            }

        }
    }
}
