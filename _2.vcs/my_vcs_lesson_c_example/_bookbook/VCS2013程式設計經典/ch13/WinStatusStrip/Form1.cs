using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinStatusStrip
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

        // ===  ShowPic()方法，可在pictureBox1顯示目前的圖片
        // 在toolStripStatusLabel1顯示目前的圖片名稱
        void ShowPic()
        {
            // 在pictureBox1上顯示photo[num]陣列元素的圖檔
            pictureBox1.Image = new Bitmap(photo[num] + ".jpg");
            toolStripStatusLabel1.Text = "圖片名稱：" + photo[num];
        }

        // ===  表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            ShowPic();   // 呼叫ShowPic方法在pictureBox1顯示圖片
        }

        // ===  按第一張執行
        private void 第一張ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            num = 0;
            ShowPic();
        }

        // ===  按上一張執行
        private void 上一張ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            num--;  // num圖片索引編號減1，表示顯示上一張
            // 若num圖片索引編號小於1，則另num由最後一張開始
            if (num < 0)
            {
                num = photo.GetUpperBound(0);
            }
            ShowPic();
        }

        // ===  按下一張執行
        private void 下一張ToolStripMenuItem_Click(object sender, EventArgs e)
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

        // ===  按最末張執行
        private void 最末張ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            // 另num由最後一張索引編號開始
            num = photo.GetUpperBound(0);
            ShowPic();
        }
    }
}
