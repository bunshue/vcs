using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading;

namespace vcs_ScreenCapture2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Hide();//隱藏當前窗體
            Thread.Sleep(50);//讓線程睡眠一段時間，窗體消失需要一點時間
            Form2 f2 = new Form2();
            Bitmap CatchBmp = new Bitmap(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height);//新建一個和屏幕大小相同的圖片
            Graphics g = Graphics.FromImage(CatchBmp);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));//保存全屏圖片
            f2.BackgroundImage = CatchBmp;//將Catch窗體的背景設為全屏時的圖片
            if (f2.ShowDialog() == DialogResult.OK)
            {//如果Catch窗體結束,就將剪貼板中的圖片放到信息發送框中
                IDataObject iData = Clipboard.GetDataObject();
                DataFormats.Format myFormat = DataFormats.GetFormat(DataFormats.Bitmap);
                if (iData.GetDataPresent(DataFormats.Bitmap))
                {
                    richTextBox1.Paste(myFormat);
                    Clipboard.Clear();//清除剪貼板中的對象
                }
                this.Show();//重新顯示窗體
            }


        }
    }
}
