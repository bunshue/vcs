using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class testPictures : Form
    {
        public testPictures()
        {
            InitializeComponent();
        }

        private void btnReset_Click(object sender, EventArgs e)
        {
            // 顯示圖片
            ptbDisplay.Image = /*System.Drawing.*/Image.FromFile(".\\Pictures\\Koala.jpg");
        }

        int i = 0; //必須宣告為實體變數

        private void btnChange_Click(object sender, EventArgs e)
        {
            // 變換圖片
            /*
            string path = ".\\Pictures\\";  //圖像檔之儲存目錄的相對路徑

            switch (i) {
                case 0:
                    path += "Chrysanthemum.jpg";
                    break;
                case 1:
                    path += "Desert.jpg";
                    break;
                case 2:
                    path += "Hydrangeas.jpg";
                    break;
                case 3:
                    path += "Jellyfish.jpg";
                    break;
                case 4:
                    path += "Koala.jpg";
                    break;
                case 5:
                    path += "Lighthouse.jpg";
                    break;
                case 6:
                    path += "Penguins.jpg";
                    break;
                case 7:
                    path += "Tulips.jpg";
                    break;
                case 8:
                    path += "Smile Time.jpg";
                    break;
            }

            ptbDisplay.Image = Image.FromFile(path);
            i++; //依序顯示
            if (i >= 9) i = 0; //循環顯示
            */

            ptbDisplay.Image = imageList1.Images[i];
            i++;  //依序顯示
            if (i >= imageList1.Images.Count) i = 0; //循環顯示
            
        }

        private void ptbDisplay_Click(object sender, EventArgs e)
        {

        }
    }
}
