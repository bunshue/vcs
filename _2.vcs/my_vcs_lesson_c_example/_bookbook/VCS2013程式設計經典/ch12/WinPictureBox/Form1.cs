using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinPictureBox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
            // 建立photo陣列用來存放圖片名稱
            string[] photo = new string[] { "企鵝", "沙漠", "無尾熊", "菊花", "鬱金香" };
            // 將photo陣列所有元素放入cboPhotoName清單內當清單的選項
            cboPhotoName.Items.AddRange(photo);
            cboPhotoName.SelectedIndex = 0;  // 清單預設顯示第1個選項
            pic.BorderStyle =  BorderStyle.Fixed3D ;
            // 圖片隨控制項大小伸縮
            pic.SizeMode = PictureBoxSizeMode.StretchImage;
        }
        // 當清單被選取時執行
        private void cboPhotoName_SelectedIndexChanged(object sender, EventArgs e)
        {
            // 圖片方塊顯示清單項目所選的圖片
            pic.Image = new Bitmap(cboPhotoName.Text + ".jpg");
        }
    }
}
