//======================================================================
//
//        Copyright (C) 2008 stg609    
//        All rights reserved 
//       
//        命名空间:  绘图程序
//        CLR版本:   2.0.50727.42
//        创建年份:  2008
// 
//        created by stg609 at  03/29/2008 22:02:01
//        本人博客：http://stg609.cnblogs.com
//        由于水平有限，所写代码若有不足，欢迎大家到我博客交流
//        
//        注:转载请保留此信息
//
//======================================================================

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging;
using System.IO;
using System.Threading;

namespace vcs_Paint9
{
    public partial class Draw : Form
    {
        public Draw()
        {
            InitializeComponent();
        }
        private DrawTools dt;
        private string sType;//绘图样式
        private string sFileName;//打开的文件名
        private bool bReSize = false;//是否改变画布大小
        private Size DefaultPicSize;//储存原始画布大小，用来新建文件时使用


        //pbimg＂鼠标按下＂事件处理方法
        private void pbImg_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (dt != null)
                {
                    dt.startDraw = true;//相当于所选工具被激活，可以开始绘图
                    dt.startPointF = new PointF(e.X, e.Y);
                }
            }
        }

        //pbimg＂鼠标移动＂事件处理方法
        private void pbImg_MouseMove(object sender, MouseEventArgs e)
        {
            Thread.Sleep(6);//减少cpu占用率
            mousePostion.Text = e.Location.ToString();
            if (dt.startDraw)
            {
                switch (sType)
                {
                    case "Dot": dt.DrawDot(e); break;
                    case "Eraser": dt.Eraser(e); break;
                    default: dt.Draw(e, sType); break;

                }
            }
        }

        //pbimg＂鼠标松开＂事件处理方法
        private void pbImg_MouseUp(object sender, MouseEventArgs e)
        {
            if (dt != null)
            {
                dt.EndDraw();
            }
        }

        //＂窗体加载＂事件处理方法
        private void Form1_Load(object sender, EventArgs e)
        {
            SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            Bitmap bmp = new Bitmap(pbImg.Width, pbImg.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.FillRectangle(new SolidBrush(pbImg.BackColor), new Rectangle(0, 0, pbImg.Width, pbImg.Height));
            g.Dispose();
            dt = new DrawTools(this.pbImg.CreateGraphics(), colorHatch1.HatchColor, bmp);//实例化工具类
            DefaultPicSize = pbImg.Size;

        }

        //＂打开文件＂事件处理方法
        private void openPic_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();//实例化文件打开对话框
            ofd.Filter = "JPG|*.jpg|Bmp|*.bmp|所有文件|*.*";//设置对话框打开文件的括展名
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                Bitmap bmpformfile = new Bitmap(ofd.FileName);//获取打开的文件
                panel2.AutoScrollPosition = new Point(0,0);//将滚动条复位
                pbImg.Size = bmpformfile.Size;//调整绘图区大小为图片大小

                reSize.Location = new Point(bmpformfile.Width, bmpformfile.Height);//reSize为我用来实现手动调节画布大小用的
                //因为我们初始时的空白画布大小有限，"打开"操作可能引起画板大小改变，所以要将画板重新传入工具类
                dt.DrawTools_Graphics = pbImg.CreateGraphics();

                Bitmap bmp = new Bitmap(pbImg.Width, pbImg.Height);
                Graphics g = Graphics.FromImage(bmp);
                g.FillRectangle(new SolidBrush(pbImg.BackColor), new Rectangle(0, 0, pbImg.Width, pbImg.Height));//不使用这句话，那么这个bmp的背景就是透明的
                g.DrawImage(bmpformfile, 0, 0,bmpformfile.Width,bmpformfile.Height);//将图片画到画板上
                g.Dispose();//释放画板所占资源
                //不直接使用pbImg.Image = Image.FormFile(ofd.FileName)是因为这样会让图片一直处于打开状态，也就无法保存修改后的图片；详见http://www.wanxin.org/redirect.php?tid=3&goto=lastpost
                bmpformfile.Dispose();//释放图片所占资源
                g = pbImg.CreateGraphics();
                g.DrawImage(bmp, 0, 0);
                g.Dispose();
                dt.OrginalImg = bmp;
                bmp.Dispose();
                sFileName = ofd.FileName;//储存打开的图片文件的详细路径，用来稍后能覆盖这个文件
                ofd.Dispose();

            }
        }

        //＂保存＂事件处理方法
        private void savePic_Click(object sender, EventArgs e)
        {
            if (sFileName != null)
            {

                if (MessageBox.Show("是否要保存文件？", "系统提示", MessageBoxButtons.YesNo) == DialogResult.Yes)
                {
                    dt.OrginalImg.Save(sFileName);
                }
            }
            else
            {
                SaveFileDialog sfd = new SaveFileDialog();
                sfd.Filter = "JPG(*.jpg)|*.jpg|BMP(*.bmp)|*.bmp";
                if (sfd.ShowDialog() == DialogResult.OK)
                {
                    dt.OrginalImg.Save(sfd.FileName);
                    sFileName = sfd.FileName;
                }
            }

        }

        //窗体移动最小化等造成的pbimg＂重画＂事件处理方法
        private void pbImg_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            g.DrawImage(dt.OrginalImg, 0, 0);
            //g.Dispose();切不可使用,这个Graphics是系统传入的变量，不是我们自己创建的，如果dispose就会出错

        }

        //＂绘图工具选用＂事件处理方法
        private void tool_Click(object sender, EventArgs e)
        {
            ToolStripButton tsb = sender as ToolStripButton;
            if (tsb != null)
            {
                sType = tsb.Name;
                currentDrawType.Text = tsb.Text;
                if (sType == "Eraser")
                {
                    //pbImg.Cursor = new Cursor(Application.StartupPath + @"\img\pb.cur");
                    pbImg.Cursor = new Cursor(Application.StartupPath + @"\img\pb.cur");
                }
                else
                {
                    pbImg.Cursor = Cursors.Cross;
                }
            }
        }

        //＂清除图像＂事件处理方法
        private void clearPic_Click(object sender, EventArgs e)
        {
            Bitmap newpic = new Bitmap(pbImg.Width, pbImg.Height);
            Graphics g = Graphics.FromImage(newpic);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, pbImg.Width, pbImg.Height);
            g.Dispose();
            g = pbImg.CreateGraphics();
            g.DrawImage(newpic, 0, 0);
            g.Dispose();
            dt.OrginalImg = newpic;
        }

        //＂另存为＂事件处理方法
        private void SaveAs_Click(object sender, EventArgs e)
        {
            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "JPG(*.jpg)|*.jpg|BMP(*.bmp)|*.bmp";
            if (sfd.ShowDialog() == DialogResult.OK)
            {
                dt.OrginalImg.Save(sfd.FileName);
                sFileName = sfd.FileName;
            }
        }

        //＂退出＂事件处理方法
        private void Quit_Click(object sender, EventArgs e)
        {
            dt.ClearVar();
            Application.Exit();
        }

        //＂颜色改变＂事件处理方法
        private void colorHatch1_ColorChanged(object sender, ColorHatch.ColorChangedEventArgs e)
        {
            dt.DrawColor = e.GetColor;
        }


        private void reSize_MouseDown(object sender, MouseEventArgs e)
        {
            bReSize = true;//当鼠标按下时，说明要开始调节大小
        }

        private void reSize_MouseMove(object sender, MouseEventArgs e)
        {
            if (bReSize)
            {
                reSize.Location = new Point(reSize.Location.X + e.X, reSize.Location.Y + e.Y);

            }
        }

        private void reSize_MouseUp(object sender, MouseEventArgs e)
        {
            bReSize = false;//大小改变结束
            //调节大小可能造成画板大小超过屏幕区域，所以事先要设置autoScroll为true.
            //但是滚动条的出现反而增加了我们的难度，因为滚动条上下移动并不会自动帮我们调整图片的坐标。
            //这是因为GDI绘图的坐标系不只一个，好像有三个，没有仔细了解，一个是屏幕坐标，一个是客户区坐标，还个是文档坐标。
            //滚动条的上下移动改变的是文档的坐标，但是客户区坐标不变，而location属性就属于客户区坐标，所以我们直接计算会出现错误
            //这时我们就需要知道文档坐标与客户区坐标的偏移量，这就是AutoScrollPostion可以提供的

            pbImg.Size = new Size(reSize.Location.X - (this.panel2.AutoScrollPosition.X), reSize.Location.Y - (this.panel2.AutoScrollPosition.Y));
            dt.DrawTools_Graphics = pbImg.CreateGraphics();//因为画板的大小被改变所以必须重新赋值

            //另外画布也被改变所以也要重新赋值
            Bitmap bmp = new Bitmap(pbImg.Width, pbImg.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, pbImg.Width, pbImg.Height);
            g.DrawImage(dt.OrginalImg, 0, 0);
            g.Dispose();
            g = pbImg.CreateGraphics();
            g.DrawImage(bmp, 0, 0);
            g.Dispose();
            dt.OrginalImg = bmp;

            bmp.Dispose();
        }

        private void BuildNewPic_Click(object sender, EventArgs e)
        {

            pbImg.Size = DefaultPicSize;
            this.panel2.AutoScrollPosition = new Point(0, 0);
            Bitmap bmp = new Bitmap(DefaultPicSize.Width, DefaultPicSize.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.FillRectangle(new SolidBrush(Color.White), 0, 0, DefaultPicSize.Width, DefaultPicSize.Height);
            g.Dispose();
            g = pbImg.CreateGraphics();
            g.DrawImage(bmp, 0, 0);
            g.Dispose();
            reSize.Location = new Point(DefaultPicSize.Width, DefaultPicSize.Height);
            dt.OrginalImg = bmp;
            sFileName = null;
        }

        private void AttributePic_Click(object sender, EventArgs e)
        {
            MessageBox.Show("图像高:" + pbImg.Height + " px ,图像宽:" + pbImg.Width+" px", "图像属性");
        }

    }
}