using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageList
{
    public partial class Form1 : Form
    {
        // 宣告 num 整數變數用來記錄目前的圖片索引編號，0表示第1張
        int num = 0;

        // 建立 photo 字串陣列用來存放照片的名稱
        // 陣列元素索引範圍photo[0]~photo[4]
        string[] photo = new string[] { "ggb1", "ggb2", "ggb3", "ggb4", "ggb5" };

        int index = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // 五張圖放入imageList影像清單控制項內 
            for (int i = 0; i <= photo.GetUpperBound(0); i++)
            {
                imageList1.Images.Add(new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_scenery\" + photo[i] + ".jpg"));
            }

            // 設定影像清單中個別影像大小, 只能設定 1~256
            imageList1.ImageSize = new Size(250, 180);
            // 設定影像的色彩數目為Depth32Bit，以便呈現較佳的畫質
            imageList1.ColorDepth = ColorDepth.Depth32Bit;
            // 呼叫ShowPic()方法，以便在pictureBox1顯示目前的圖片
            ShowPic();

            // 設定影像清單中個別影像大小, 只能設定 1~256
            imageList2.ImageSize = new Size(256, 256);
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_01.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_02.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_03.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_04.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_05.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_06.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_07.png"));
            imageList2.Images.Add(Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_icon\vista\Vista_icons_08.png"));

            button4.ImageList = imageList2;
            richTextBox1.Text += "目前共有 " + imageList2.Images.Count.ToString() + " 張圖片可用\n";
        }

        // 定義ShowPic()方法，可在pictureBox1顯示目前的圖片
        // 在lblShow顯示目前的圖片名稱
        void ShowPic()
        {
            // 在pictureBox1上顯示imageList1內第 num 張圖片
            pictureBox1.Image = imageList1.Images[num];
            lblShow.Text = "圖片名稱：" + photo[num];
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lblShow.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0);
            button0.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0 + 40 * 1);
            button1.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0 + 40 * 2);
            button2.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0 + 40 * 3);
            button3.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0 + 40 * 4);
            button4.Location = new Point(x_st + dx * 3 + 40, y_st + dy * 0 + 40 * 5);

            richTextBox1.Size = new Size(300, 680);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1180, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //第一張
            num = 0;
            ShowPic();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //上一張
            num--;  // num圖片索引編號減1，表示顯示上一張
            // 若num圖片索引編號小於1，則另num由最後一張開始
            if (num < 0)
            {
                num = photo.GetUpperBound(0);
            }
            ShowPic();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //下一張
            num++;  // num圖片索引編號加1，表示顯示下一張
            // 若num圖片索引編號大於最後一張圖的索引編號
            // 則另num為0，表示由第一張開始顯示
            if (num > photo.GetUpperBound(0))
            {
                num = 0;
            }
            ShowPic();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //最末張
            // 另num由最後一張索引編號開始
            num = photo.GetUpperBound(0);
            ShowPic();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            pictureBox1.Image = imageList2.Images[index];

            button4.ImageIndex = index;
            index++;
            if (index >= imageList2.Images.Count)
            {
                index = 0;
            }
        }
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


