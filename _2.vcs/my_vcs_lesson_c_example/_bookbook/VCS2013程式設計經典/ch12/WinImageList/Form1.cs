using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinImageList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 宣告 num 整數變數用來記錄目前的圖片索引編號，0表示第1張
        int num = 0;

        // 建立 photo 字串陣列用來存放照片的名稱
        // 陣列元素索引範圍photo[0]~photo[4]
        string[] photo = new string[] { "企鵝", "沙漠", "無尾熊", "菊花", "鬱金香" };

        // 定義ShowPic()方法，可在pictureBox1顯示目前的圖片
        // 在lblShow顯示目前的圖片名稱
        void ShowPic()
        {
            // 在pictureBox1上顯示imageList1內第 num 張圖片
            pictureBox1.Image = imageList1.Images[num];
            lblShow.Text = "圖片名稱：" + photo[num];
        }

        // === 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            //將"企鵝.jpg", "沙漠.jpg", "無尾熊.jpg", "菊花.jpg", "鬱金香.jpg"
            // 五張圖放入imageList影像清單控制項內 
            for (int i = 0; i <= photo.GetUpperBound(0); i++)
            {
                imageList1.Images.Add(new Bitmap(photo[i] + ".jpg"));
            }
            // 設定影像清單中個別影像大小為寬250, 高180
            imageList1.ImageSize = new Size(250, 180);
            // 設定影像的色彩數目為Depth32Bit，以便呈現較佳的畫質
            imageList1.ColorDepth = ColorDepth.Depth32Bit;
            // 呼叫ShowPic()方法，以便在pictureBox1顯示目前的圖片
            ShowPic();
        }

        // ===  按 [第一張] 鈕執行
        private void btnFirst_Click(object sender, EventArgs e)
        {
            num = 0;
            ShowPic();
        }

        // === 按 [上一張] 鈕執行
        private void btnPrev_Click(object sender, EventArgs e)
        {
            num--;  // num圖片索引編號減1，表示顯示上一張
            // 若num圖片索引編號小於1，則另num由最後一張開始
            if (num < 0)
            {
                num = photo.GetUpperBound(0);
            }
            ShowPic();
        }

        // ===  按 [下一張] 鈕執行
        private void btnNext_Click(object sender, EventArgs e)
        {
            num++;  // num圖片索引編號加1，表示顯示下一張
            // 若num圖片索引編號大於最後一張圖的索引編號
            // 則另num為0，表示由第一張開始顯示
            if (num > photo.GetUpperBound(0))
            {
                num = 0;
            }
            ShowPic();
        }

        // === 按 [最末張] 鈕執行
        private void btnLast_Click(object sender, EventArgs e)
        {
            // 另num由最後一張索引編號開始
            num = photo.GetUpperBound(0);
            ShowPic();
        }
    }
}
