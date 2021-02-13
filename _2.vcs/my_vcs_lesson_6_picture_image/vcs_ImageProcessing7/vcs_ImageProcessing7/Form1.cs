using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageProcessing7
{
    public partial class Form1 : Form
    {
        Image myImage;

        public Form1()
        {
            InitializeComponent();
        }

        // Display the initial image.
        private void Form1_Load(object sender, EventArgs e)
        {
            //讀取圖檔
            string filename = @"C:\______test_files\picture1.jpg";

            myImage = Image.FromFile(filename);
            pictureBox1.Image = myImage;
        }

        //百葉窗效果
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                Bitmap myBitmap = (Bitmap)this.pictureBox1.Image.Clone();   //用pictureBox背景的复本实例化Bitmap类
                int intWidth = myBitmap.Width;							//记录图片的宽度
                int intHeight = myBitmap.Height / 20;						//记录图片的指定高度
                Graphics myGraphics = this.CreateGraphics();				//创建窗体的Graphics类
                myGraphics.Clear(Color.WhiteSmoke);						//用指定的颜色清除窗体背景
                Point[] myPoint = new Point[30];							//定义数组
                for (int i = 0; i < 30; i++)									//记录百叶窗各节点的位置
                {
                    myPoint[i].X = 0;
                    myPoint[i].Y = i * intHeight;
                }
                Bitmap bitmap = new Bitmap(myBitmap.Width, myBitmap.Height);	//实例化Bitmap类
                //通过调用Bitmap对象的SetPixel方法重新设置图像的像素点颜色，从而实现百叶窗效果
                for (int m = 0; m < intHeight; m++)
                {
                    for (int n = 0; n < 20; n++)
                    {
                        for (int j = 0; j < intWidth; j++)
                        {
                            bitmap.SetPixel(myPoint[n].X + j, myPoint[n].Y + m, myBitmap.GetPixel(myPoint[n].X + j, myPoint[n].Y + m));//获取当前象素颜色值
                        }
                    }
                    this.Refresh();									//绘制无效
                    this.pictureBox1.Image = bitmap;                //显示百叶窗体的效果
                    System.Threading.Thread.Sleep(100);						//线程挂起
                }
            }
            catch { }

        }


    }
}
