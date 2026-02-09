using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinTrackBar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 建立photo陣列用來存放圖片名稱
        string[] photo = new string[] { "企鵝", "沙漠", "無尾熊", "菊花", "鬱金香" };

        // === 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            // 圖片隨控制項大小伸縮
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            // 圖片控制項顯示photo[0]元素的圖檔
            pictureBox1.Image = new Bitmap("../../../images/" + photo[0] + ".jpg");
            label1.Text = "圖片名稱：" + photo[0];
            // 指定滑桿的最小值，剛好為陣列索引下限
            trackBar1.Minimum = 0;
            // 指定滑桿的最大值，剛好為陣列索引上限
            trackBar1.Maximum = photo.GetUpperBound(0);
        }

        // === 滑桿捲動時會執行
        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            int index = trackBar1.Value;  // 取得滑桿的位置值，用來當陣列索引
            // 顯示photo陣列中第index張圖片
            pictureBox1.Image = new Bitmap("../../../images/" + photo[index] + ".jpg");
            label1.Text = "圖片名稱：" + photo[index];
        }
    }
}
