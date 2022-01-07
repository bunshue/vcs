using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode
using System.Drawing.Imaging;   //for ColorAdjustType

namespace vcs_ShowPicture4
{
    public partial class Form1 : Form
    {
        private Bitmap SourceBitmap;
        private Bitmap MyBitmap;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            //得到原始大小的图像
            SourceBitmap = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //得到缩放后的图像
            MyBitmap = new Bitmap(SourceBitmap, this.pictureBox1.Width, this.pictureBox1.Height);

            pictureBox1.Image = MyBitmap;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //一. 以上下反转的方式显示图像.

            //原理: 计算图像位置和高度后以高度的一半为轴进行对换上下半边的图像.

            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray);
                for (int i = -width / 2; i <= width / 2; i++)
                {
                    g.Clear(Color.Gray);
                    int j = Convert.ToInt32(i * (Convert.ToSingle(height) / Convert.ToSingle(width)));
                    Rectangle DestRect = new Rectangle(0, height / 2 - j, width, 2 * j);
                    Rectangle SrcRect = new Rectangle(0, 0, MyBitmap.Width, MyBitmap.Height);
                    g.DrawImage(MyBitmap, DestRect, SrcRect, GraphicsUnit.Pixel);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //  二. 以上下对接的方式显示图像

            //  原理: 首先将图像分为上下两部分, 然后分别显示.


            try
            {
                int width = this.pictureBox1.Width; //图像宽度
                int height = this.pictureBox1.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray);
                Bitmap bitmap = new Bitmap(width, height);
                int x = 0;
                while (x <= height / 2)
                {
                    for (int i = 0; i <= width - 1; i++)
                    {
                        bitmap.SetPixel(i, x, MyBitmap.GetPixel(i, x));
                    }
                    for (int i = 0; i <= width - 1; i++)
                    {
                        bitmap.SetPixel(i, height - x - 1, MyBitmap.GetPixel(i, height - x - 1));
                    }
                    x++;
                    this.panel1.Refresh();
                    g.DrawImage(bitmap, 0, 0);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //三. 以四周扩散的方式显示图像

            //原理: 首先设置图像显示的位置, 然后按高度和宽度的比例循环输出, 直到高度和宽度为原始大小.

            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                //取得Graphics对象
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始为全灰色
                for (int i = 0; i <= width / 2; i++)
                {
                    int j = Convert.ToInt32(i * (Convert.ToSingle(height) / Convert.ToSingle(width)));
                    Rectangle DestRect = new Rectangle(width / 2 - i, height / 2 - j, 2 * i, 2 * j);
                    Rectangle SrcRect = new Rectangle(0, 0, MyBitmap.Width, MyBitmap.Height);
                    g.DrawImage(MyBitmap, DestRect, SrcRect, GraphicsUnit.Pixel);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //四. 以分块效果显示图像

            //原理: 首先将图分为几块, 再使用 Bitmap 类的 Clone方法从原图指定的块中复制图像, 最后将这些块依次显示出来便可

            Graphics g = this.panel1.CreateGraphics();
            g.Clear(Color.White);
            int width = MyBitmap.Width;
            int height = MyBitmap.Height;
            //定义将图片切分成四个部分的区域
            RectangleF[] block ={
  new RectangleF(0,0,width/2,height/2),
  new RectangleF(width/2,0,width/2,height/2),
  new RectangleF(0,height/2,width/2,height/2),
  new RectangleF(width/2,height/2,width/2,height/2)};
            //分别克隆图片的四个部分
            Bitmap[] MyBitmapBlack ={
  MyBitmap.Clone(block[0],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[1],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[2],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[3],System.Drawing.Imaging.PixelFormat.DontCare)};
            //绘制图片的四个部分，各部分绘制时间间隔为0.5秒
            g.DrawImage(MyBitmapBlack[0], 0, 0);
            System.Threading.Thread.Sleep(1000);
            g.DrawImage(MyBitmapBlack[1], width / 2, 0);
            System.Threading.Thread.Sleep(1000);
            g.DrawImage(MyBitmapBlack[3], width / 2, height / 2);
            System.Threading.Thread.Sleep(1000);
            g.DrawImage(MyBitmapBlack[2], 0, height / 2);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //五. 以淡入淡出效果显示图像

            //原理: 使用 ImageAttrributes 类的 SetColorMatrix() 方法设置颜色, 调整矩阵实现淡出的效果. 此类还可以对颜色进行校正, 调暗, 调亮和移除等.

            try
            {
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray);
                int width = MyBitmap.Width;
                int height = MyBitmap.Height;
                ImageAttributes attributes = new ImageAttributes();
                ColorMatrix matrix = new ColorMatrix();
                //创建淡入颜色矩阵
                matrix.Matrix00 = (float)0.0;
                matrix.Matrix01 = (float)0.0;
                matrix.Matrix02 = (float)0.0;
                matrix.Matrix03 = (float)0.0;
                matrix.Matrix04 = (float)0.0;
                matrix.Matrix10 = (float)0.0;
                matrix.Matrix11 = (float)0.0;
                matrix.Matrix12 = (float)0.0;
                matrix.Matrix13 = (float)0.0;
                matrix.Matrix14 = (float)0.0;
                matrix.Matrix20 = (float)0.0;
                matrix.Matrix21 = (float)0.0;
                matrix.Matrix22 = (float)0.0;
                matrix.Matrix23 = (float)0.0;
                matrix.Matrix24 = (float)0.0;
                matrix.Matrix30 = (float)0.0;
                matrix.Matrix31 = (float)0.0;
                matrix.Matrix32 = (float)0.0;
                matrix.Matrix33 = (float)0.0;
                matrix.Matrix34 = (float)0.0;
                matrix.Matrix40 = (float)0.0;
                matrix.Matrix41 = (float)0.0;
                matrix.Matrix42 = (float)0.0;
                matrix.Matrix43 = (float)0.0;
                matrix.Matrix44 = (float)0.0;
                matrix.Matrix33 = (float)1.0;
                matrix.Matrix44 = (float)1.0;
                //从0到1进行修改色彩变换矩阵主对角线上的数值
                //使三种基准色的饱和度渐增
                Single count = (float)0.0;
                while (count < 1.0)
                {
                    matrix.Matrix00 = count;
                    matrix.Matrix11 = count;
                    matrix.Matrix22 = count;
                    matrix.Matrix33 = count;
                    attributes.SetColorMatrix(matrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
                    g.DrawImage(MyBitmap, new Rectangle(0, 0, width, height),
                    0, 0, width, height, GraphicsUnit.Pixel, attributes);
                    System.Threading.Thread.Sleep(200);
                    count = (float)(count + 0.02);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            try
            {
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray);
                int width = MyBitmap.Width;
                int height = MyBitmap.Height;
                ImageAttributes attributes = new ImageAttributes();
                ColorMatrix matrix = new ColorMatrix();
                //创建淡出颜色矩阵
                matrix.Matrix00 = (float)0.0;
                matrix.Matrix01 = (float)0.0;
                matrix.Matrix02 = (float)0.0;
                matrix.Matrix03 = (float)0.0;
                matrix.Matrix04 = (float)0.0;
                matrix.Matrix10 = (float)0.0;
                matrix.Matrix11 = (float)0.0;
                matrix.Matrix12 = (float)0.0;
                matrix.Matrix13 = (float)0.0;
                matrix.Matrix14 = (float)0.0;
                matrix.Matrix20 = (float)0.0;
                matrix.Matrix21 = (float)0.0;
                matrix.Matrix22 = (float)0.0;
                matrix.Matrix23 = (float)0.0;
                matrix.Matrix24 = (float)0.0;
                matrix.Matrix30 = (float)0.0;
                matrix.Matrix31 = (float)0.0;
                matrix.Matrix32 = (float)0.0;
                matrix.Matrix33 = (float)0.0;
                matrix.Matrix34 = (float)0.0;
                matrix.Matrix40 = (float)0.0;
                matrix.Matrix41 = (float)0.0;
                matrix.Matrix42 = (float)0.0;
                matrix.Matrix43 = (float)0.0;
                matrix.Matrix44 = (float)0.0;
                matrix.Matrix33 = (float)1.0;
                matrix.Matrix44 = (float)1.0;
                //从1到0进行修改色彩变换矩阵主对角线上的数值
                //依次减少每种色彩分量
                Single count = (float)1.0;
                while (count > 0.0)
                {
                    matrix.Matrix00 = (float)count;
                    matrix.Matrix11 = (float)count;
                    matrix.Matrix22 = (float)count;
                    matrix.Matrix33 = (float)count;
                    attributes.SetColorMatrix(matrix, ColorMatrixFlag.Default, ColorAdjustType.Bitmap);
                    g.DrawImage(MyBitmap, new Rectangle(0, 0, width, height),
                    0, 0, width, height, GraphicsUnit.Pixel, attributes);
                    System.Threading.Thread.Sleep(20);
                    count = (float)(count - 0.01);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //六. 以左右对接的方式显示图像

            //原理: 首先将图像分为左右两部分, 然后分别显示.

            //以左右对接方式显示图像
            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始为全灰色
                Bitmap bitmap = new Bitmap(width, height);
                int x = 0;
                while (x <= width / 2)
                {
                    for (int i = 0; i <= height - 1; i++)
                    {
                        bitmap.SetPixel(x, i, MyBitmap.GetPixel(x, i));
                    }
                    for (int i = 0; i <= height - 1; i++)
                    {
                        bitmap.SetPixel(width - x - 1, i,
                        MyBitmap.GetPixel(width - x - 1, i));
                    }
                    x++;
                    this.panel1.Refresh();
                    g.DrawImage(bitmap, 0, 0);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //七. 以左右反转的方式显示图像
            //原理: 计算图像位置和高度后以宽度的一半为轴进行对换左右半边的图像./
            //以左右反转方式显示图像
            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始为全灰色
                for (int j = -height / 2; j <= height / 2; j++)
                {
                    g.Clear(Color.Gray); //初始为全灰色
                    int i = Convert.ToInt32(j * (Convert.ToSingle(width) / Convert.ToSingle(height)));
                    Rectangle DestRect = new Rectangle(width / 2 - i, 0, 2 * i, height);
                    Rectangle SrcRect = new Rectangle(0, 0, MyBitmap.Width, MyBitmap.Height);
                    g.DrawImage(MyBitmap, DestRect, SrcRect, GraphicsUnit.Pixel);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch
            {

            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //七、以左右反转的方式显示图像
            //原理：计算图像位置和高度后以宽度的一半为轴进行对换左右半边的图像。
            //以左右反转方式显示图像
            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始为全灰色
                for (int j = -height / 2; j <= height / 2; j++)
                {
                    g.Clear(Color.Gray); //初始为全灰色
                    int i = Convert.ToInt32(j * (Convert.ToSingle(width) / Convert.ToSingle(height)));
                    Rectangle destrect = new Rectangle(width / 2 - i, 0, 2 * i, height);
                    Rectangle srcrect = new Rectangle(0, 0, MyBitmap.Width, MyBitmap.Height);
                    g.DrawImage(MyBitmap, destrect, srcrect, GraphicsUnit.Pixel);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }
        private void button10_Click(object sender, EventArgs e)
        {
            //八、以从上向下拉伸的方式显示图像
            //原理：将图像的宽度不变每次显示图像的一部分, 直到将图片完全显示。
            //以从上向下拉伸方式显示图像
            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始为全灰色
                for (int y = 1; y <= height; y++)
                {
                    Bitmap bitmap = MyBitmap.Clone(new Rectangle(0, 0, width, y), System.Drawing.Imaging.PixelFormat.Format24bppRgb);
                    g.DrawImage(bitmap, 0, 0);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }
        private void button11_Click(object sender, EventArgs e)
        {
            //九、以从左向右拉伸的方式显示图像
            //原理：将图像的高度不变每次显示图像的一部分, 直到将图片完全显示。
            //以从左向右拉伸方式显示图像
            try
            {
                int width = this.MyBitmap.Width; //图像宽度
                int height = this.MyBitmap.Height; //图像高度
                Graphics g = this.panel1.CreateGraphics(); g.Clear(Color.Gray); //初始为全灰色
                for (int x = 1; x <= width; x++)
                {
                    Bitmap bitmap = MyBitmap.Clone(new Rectangle(0, 0, x, height), System.Drawing.Imaging.PixelFormat.Format24bppRgb);

                    g.DrawImage(bitmap, 0, 0);
                    System.Threading.Thread.Sleep(10);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "信息提示");
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //十、以任意角度旋转图像
            //原理：主要使用了 graphics 类提供的 rotatetransform() 方法对图像进行旋转。
            //以任意角度旋转显示图像
            Graphics g = this.panel1.CreateGraphics();
            float myangle = 0;//旋转的角度
            while (myangle < 360)
            {
                TextureBrush mybrush = new TextureBrush(MyBitmap);
                this.panel1.Refresh();
                mybrush.RotateTransform(myangle);
                g.FillRectangle(mybrush, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                myangle += 0.5f;
                System.Threading.Thread.Sleep(50);
            }
        }
        private void button13_Click(object sender, EventArgs e)
        {
            //原理：主要使用了 graphics 类提供的 fillellipse() 方法和 texturebrush() 方法。
            //椭圆显示图像
            this.panel1.Refresh();
            Graphics g = this.panel1.CreateGraphics();
            TextureBrush mybrush = new TextureBrush(MyBitmap);
            g.FillEllipse(mybrush, this.panel1.ClientRectangle);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //十二、以不同的透明度显示图像.
            //原理：graphics 类的 fromargb() 方法。
            //以不同的透明度显示图像
            Graphics g = this.panel1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;
            TextureBrush mybrush = new TextureBrush(MyBitmap);
            g.FillRectangle(mybrush, this.panel1.ClientRectangle);
            for (int i = 0; i < 255; i++)
            {
                //由透明变为不透明
                g.FillRectangle(new SolidBrush(Color.FromArgb(i, Color.DarkSlateGray)), this.panel1.ClientRectangle);
                System.Threading.Thread.Sleep(100);
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //十三、以不同分辨率显示图像
            //原理：bitmap 类的 setresolution 方法。
            //以不同的分辨率显示图像
            Graphics g = this.panel1.CreateGraphics();
            for (int i = 10; i < this.panel1.Height; i += 2)
            {
                g.Clear(Color.Gray);
                MyBitmap.SetResolution(i, i);
                g.DrawImage(MyBitmap, 0, 0);
                System.Threading.Thread.Sleep(100);
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //十四、以不同翻转方式显示图像
            //原理：bitmap 类的 rotatefip()方法。
            //以不同翻转方式显示图像
            Graphics g = this.panel1.CreateGraphics();
            for (int i = 0; i < 17; i++)
            {
                switch (i)
                {
                    case 0:
                        MyBitmap.RotateFlip(RotateFlipType.RotateNoneFlipX);
                        break;
                    case 1:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate180FlipNone);
                        break;
                    case 2:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate180FlipX);
                        break;
                    case 3:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate180FlipXY);
                        break;
                    case 4:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate180FlipY);
                        break;
                    case 5:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate270FlipNone);
                        break;
                    case 6:
                        MyBitmap.RotateFlip(RotateFlipType.Rotate270FlipX);
                        break;
                }
            }
        }
    }
}

