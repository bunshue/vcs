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

            //得到原始大小的圖像
            SourceBitmap = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            //得到縮放后的圖像
            MyBitmap = new Bitmap(SourceBitmap, this.pictureBox1.Width, this.pictureBox1.Height);

            pictureBox1.Image = MyBitmap;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //一. 以上下反轉的方式顯示圖像.

            //原理: 計算圖像位置和高度后以高度的一半為軸進行對換上下半邊的圖像.

            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
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
            //  二. 以上下對接的方式顯示圖像

            //  原理: 首先將圖像分為上下兩部分, 然后分別顯示.


            try
            {
                int width = this.pictureBox1.Width; //圖像寬度
                int height = this.pictureBox1.Height; //圖像高度
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
            //三. 以四周擴散的方式顯示圖像

            //原理: 首先設置圖像顯示的位置, 然后按高度和寬度的比例循環輸出, 直到高度和寬度為原始大小.

            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                //取得Graphics對象
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始為全灰色
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
            //四. 以分塊效果顯示圖像

            //原理: 首先將圖分為幾塊, 再使用 Bitmap 類的 Clone方法從原圖指定的塊中復制圖像, 最后將這些塊依次顯示出來便可

            Graphics g = this.panel1.CreateGraphics();
            g.Clear(Color.White);
            int width = MyBitmap.Width;
            int height = MyBitmap.Height;
            //定義將圖片切分成四個部分的區域
            RectangleF[] block ={
  new RectangleF(0,0,width/2,height/2),
  new RectangleF(width/2,0,width/2,height/2),
  new RectangleF(0,height/2,width/2,height/2),
  new RectangleF(width/2,height/2,width/2,height/2)};
            //分別克隆圖片的四個部分
            Bitmap[] MyBitmapBlack ={
  MyBitmap.Clone(block[0],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[1],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[2],System.Drawing.Imaging.PixelFormat.DontCare),
  MyBitmap.Clone(block[3],System.Drawing.Imaging.PixelFormat.DontCare)};
            //繪制圖片的四個部分，各部分繪制時間間隔為0.5秒
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
            //五. 以淡入淡出效果顯示圖像

            //原理: 使用 ImageAttrributes 類的 SetColorMatrix() 方法設置顏色, 調整矩陣實現淡出的效果. 此類還可以對顏色進行校正, 調暗, 調亮和移除等.

            try
            {
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray);
                int width = MyBitmap.Width;
                int height = MyBitmap.Height;
                ImageAttributes attributes = new ImageAttributes();
                ColorMatrix matrix = new ColorMatrix();
                //創建淡入顏色矩陣
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
                //從0到1進行修改色彩變換矩陣主對角線上的數值
                //使三種基準色的飽和度漸增
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
                //創建淡出顏色矩陣
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
                //從1到0進行修改色彩變換矩陣主對角線上的數值
                //依次減少每種色彩分量
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
            //六. 以左右對接的方式顯示圖像

            //原理: 首先將圖像分為左右兩部分, 然后分別顯示.

            //以左右對接方式顯示圖像
            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始為全灰色
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
            //七. 以左右反轉的方式顯示圖像
            //原理: 計算圖像位置和高度后以寬度的一半為軸進行對換左右半邊的圖像./
            //以左右反轉方式顯示圖像
            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始為全灰色
                for (int j = -height / 2; j <= height / 2; j++)
                {
                    g.Clear(Color.Gray); //初始為全灰色
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
            //七、以左右反轉的方式顯示圖像
            //原理：計算圖像位置和高度后以寬度的一半為軸進行對換左右半邊的圖像。
            //以左右反轉方式顯示圖像
            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始為全灰色
                for (int j = -height / 2; j <= height / 2; j++)
                {
                    g.Clear(Color.Gray); //初始為全灰色
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
            //八、以從上向下拉伸的方式顯示圖像
            //原理：將圖像的寬度不變每次顯示圖像的一部分, 直到將圖片完全顯示。
            //以從上向下拉伸方式顯示圖像
            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                Graphics g = this.panel1.CreateGraphics();
                g.Clear(Color.Gray); //初始為全灰色
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
            //九、以從左向右拉伸的方式顯示圖像
            //原理：將圖像的高度不變每次顯示圖像的一部分, 直到將圖片完全顯示。
            //以從左向右拉伸方式顯示圖像
            try
            {
                int width = this.MyBitmap.Width; //圖像寬度
                int height = this.MyBitmap.Height; //圖像高度
                Graphics g = this.panel1.CreateGraphics(); g.Clear(Color.Gray); //初始為全灰色
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
            //十、以任意角度旋轉圖像
            //原理：主要使用了 graphics 類提供的 rotatetransform() 方法對圖像進行旋轉。
            //以任意角度旋轉顯示圖像
            Graphics g = this.panel1.CreateGraphics();
            float myangle = 0;//旋轉的角度
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
            //原理：主要使用了 graphics 類提供的 fillellipse() 方法和 texturebrush() 方法。
            //橢圓顯示圖像
            this.panel1.Refresh();
            Graphics g = this.panel1.CreateGraphics();
            TextureBrush mybrush = new TextureBrush(MyBitmap);
            g.FillEllipse(mybrush, this.panel1.ClientRectangle);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //十二、以不同的透明度顯示圖像.
            //原理：graphics 類的 fromargb() 方法。
            //以不同的透明度顯示圖像
            Graphics g = this.panel1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;
            TextureBrush mybrush = new TextureBrush(MyBitmap);
            g.FillRectangle(mybrush, this.panel1.ClientRectangle);
            for (int i = 0; i < 255; i++)
            {
                //由透明變為不透明
                g.FillRectangle(new SolidBrush(Color.FromArgb(i, Color.DarkSlateGray)), this.panel1.ClientRectangle);
                System.Threading.Thread.Sleep(100);
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //十三、以不同分辨率顯示圖像
            //原理：bitmap 類的 setresolution 方法。
            //以不同的分辨率顯示圖像
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
            //十四、以不同翻轉方式顯示圖像
            //原理：bitmap 類的 rotatefip()方法。
            //以不同翻轉方式顯示圖像
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
