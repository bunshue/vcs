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
using System.Text;
using System.Drawing;
using System.Windows.Forms;
using System.Drawing.Drawing2D;

namespace vcs_Paint9
{
    /// <summary>
    /// 绘图工具包括直线，矩形，铅笔，圆形，橡皮
    /// </summary>
    class DrawTools
    {
        public Graphics DrawTools_Graphics;//目标绘图板
        private Pen p;
        private Image orginalImg;//原始画布，用来保存已完成的绘图过程
        private Color drawColor = Color.Black;//绘图颜色
        private Graphics newgraphics;//中间画板
        private Image finishingImg;//中间画布，用来保存绘图过程中的痕迹

        /// <summary>
        /// 绘图颜色
        /// </summary>
        public Color DrawColor
        {
            get { return drawColor; }
            set
            {
                drawColor = value;
                p.Color = value;
            }
        }

        /// <summary>
        /// 原始画布
        /// </summary>
        public Image OrginalImg
        {
            get { return orginalImg; }
            set
            {
                finishingImg = (Image)value.Clone();
                orginalImg = (Image)value.Clone();
            }
        }


        /// <summary>
        /// 表示是否开始绘图
        /// </summary>
        public bool startDraw = false;

        /// <summary>
        /// 绘图起点
        /// </summary>
        public PointF startPointF;

        /// <summary>
        /// 初始化绘图工具
        /// </summary>
        /// <param name="g">绘图板</param>
        /// <param name="c">绘图颜色</param>
        /// <param name="img">初始画布</param>
        public DrawTools(Graphics g, Color c, Image img)
        {
            DrawTools_Graphics = g;
            drawColor = c;
            p = new Pen(c, 1);
            finishingImg = (Image)img.Clone();
            orginalImg = (Image)img.Clone();
        }

        /// <summary>
        /// 绘制直线，矩形，圆形
        /// </summary>
        /// <param name="e">鼠标参数</param>
        /// <param name="sType">绘图类型</param>
        public void Draw(MouseEventArgs e, string sType)
        {
            if (startDraw)
            {
                //为防止造成图片抖动，防止记录不必要的绘图过程中的痕迹，我们先在中间画板上将图片完成，然后在将绘制好的图片一次性画到目标画板上
                //步骤1实例化中间画板，画布为上一次绘制结束时的画布的副本（如果第一次绘制，那画布就是初始时的画布副本）
                //步骤2按照绘图样式在中间画板上进行绘制
                //步骤3将绘制结束的图片画到中间画布上
                //因为我们最终绘制结束时的图片应该是在鼠标松开时完成，所以鼠标移动中所绘制的图片都只画到中间画布上,但仍需要显示在目标画板上，否则鼠标移动过程中我们就看不到效果。
                //当鼠标松开时，才把最后的那个中间图片画到原始画布上

                Image img = (Image)orginalImg.Clone();//为防止直接改写原始画布，我们定义一个新的image去得到原始画布
                newgraphics = Graphics.FromImage(img);//实例化中间画板
                switch (sType)
                {
                    case "Line":
                        {//画直线
                            newgraphics.DrawLine(p, startPointF, new PointF(e.X, e.Y)); break;
                        }
                    case "Rect":
                        {//画矩形
                            float width = Math.Abs(e.X - startPointF.X);//确定矩形的宽
                            float heigth = Math.Abs(e.Y - startPointF.Y);//确定矩形的高
                            PointF rectStartPointF = startPointF;
                            if (e.X < startPointF.X)
                            {
                                rectStartPointF.X = e.X;
                            }
                            if (e.Y < startPointF.Y)
                            {
                                rectStartPointF.Y = e.Y;
                            }
                            newgraphics.DrawRectangle(p, rectStartPointF.X, rectStartPointF.Y, width, heigth);
                            break;
                        }
                    case "Circle":
                        {//画圆形
                            newgraphics.DrawEllipse(p, startPointF.X, startPointF.Y, e.X - startPointF.X, e.Y - startPointF.Y); break;
                        }
                    case "FillRect":
                        {//画实心矩形
                            float width = Math.Abs(e.X - startPointF.X);//确定矩形的宽
                            float heigth = Math.Abs(e.Y - startPointF.Y);//确定矩形的高
                            PointF rectStartPointF = startPointF;
                            if (e.X < startPointF.X)
                            {
                                rectStartPointF.X = e.X;
                            }
                            if (e.Y < startPointF.Y)
                            {
                                rectStartPointF.Y = e.Y;
                            }
                            newgraphics.FillRectangle(new SolidBrush(drawColor), rectStartPointF.X, rectStartPointF.Y, width, heigth);
                            break;
                        }
                    case "FillCircle":
                        {//画实心圆
                            newgraphics.FillEllipse(new SolidBrush(drawColor), startPointF.X, startPointF.Y, e.X - startPointF.X, e.Y - startPointF.Y); break;
                        }
                }
                newgraphics.Dispose();//绘图完毕释放中间画板所占资源
                newgraphics = Graphics.FromImage(finishingImg);//另建一个中间画板,画布为中间图片
                newgraphics.DrawImage(img, 0, 0);//将图片画到中间图片
                newgraphics.Dispose();
                DrawTools_Graphics.DrawImage(img, 0, 0);//将图片画到目标画板上
                img.Dispose();
            }

        }

        public void EndDraw()
        {
            startDraw = false;
            //为了让完成后的绘图过程保留下来，要将中间图片绘制到原始画布上
            newgraphics = Graphics.FromImage(orginalImg);
            newgraphics.DrawImage(finishingImg, 0, 0);
            newgraphics.Dispose();
        }

        /// <summary>
        /// 橡皮方法
        /// </summary>
        /// <param name="e">鼠标参数</param>
        public void Eraser(MouseEventArgs e)
        {
            if (startDraw)
            {
                newgraphics = Graphics.FromImage(finishingImg);
                newgraphics.FillRectangle(new SolidBrush(Color.White), e.X, e.Y, 20, 20);
                newgraphics.Dispose();
                DrawTools_Graphics.DrawImage(finishingImg, 0, 0);
            }
        }

        /// <summary>
        /// 铅笔方法
        /// </summary>
        /// <param name="e">鼠标参数</param>
        public void DrawDot(MouseEventArgs e)
        {
            if (startDraw)
            {
                newgraphics = Graphics.FromImage(finishingImg);
                PointF currentPointF = new PointF(e.X, e.Y);
                newgraphics.DrawLine(p, startPointF, currentPointF);
                startPointF = currentPointF;
                newgraphics.Dispose();
                DrawTools_Graphics.DrawImage(finishingImg, 0, 0);
            }
        }

        /// <summary>
        /// 清除变量，释放内存
        /// </summary>
        public void ClearVar()
        {
            DrawTools_Graphics.Dispose();
            finishingImg.Dispose();
            orginalImg.Dispose();
            p.Dispose();
        }

    }
}
