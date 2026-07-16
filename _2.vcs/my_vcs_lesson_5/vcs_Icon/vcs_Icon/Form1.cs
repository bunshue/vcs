using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Icon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1070, 750);
            this.Text = "vcs_Icon";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //使用程式圖標 icon  運行時顯示自己定義的圖標
            this.Icon = new Icon(@"D:\_git\vcs\_1.data\______test_files1\_icon\唐.ico");

            Icon ico = new Icon(@"D:/_git/vcs/_1.data/______test_files1/_icon/快.ico");
            this.Icon = ico;
        }

        //------------------------------------------------------------  # 60個

        /*
        /// <summary>
        /// 實現bitmap到ico的轉換
        /// </summary>
        /// <param name="bitmap">原圖</param>
        /// <returns>轉換後的指定大小的圖標</returns>
        private Icon ConvertBitmap2Ico(Bitmap bitmap)
        {
            Bitmap icoBitmap = new Bitmap(bitmap, size);//創建制定大小的原位圖

            //獲得原位圖的圖標句柄
            IntPtr hIco = icoBitmap.GetHicon();
            //從圖標的指定WINDOWS句柄創建Icon
            Icon icon = Icon.FromHandle(hIco);

            return icon;
        }
        */

        private void button1_Click(object sender, EventArgs e)
        {
            //BMP轉ICON
            //ConvertBitmap2Ico
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


/*

需要為每個構建配置設置不同的ApplicationIcon

//用程式內容改變表單icon(this.Icon), 但還沒辦法改變程式icon(PropertyGroup/ApplicationIcon)

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_icon\尺.ico";
            //取得 Icon 物件
            Icon myIcon = Icon.FromHandle(new Bitmap(Image.FromFile(filename)).GetHicon());
            //設定表單 Icon
            this.Icon = myIcon;
或
			string filename = @"D:\_git\vcs\_1.data\______test_files1\_icon\尺.ico";
            try
            {
                //取得 Icon 物件                    
                using (Icon oIcon = new Icon(filename))
                {
                    //建立副本
                    Icon myIcon = (Icon)oIcon.Clone();
                    this.Icon = myIcon;
                }
            }
            catch (Exception ex)
            {
                //AppFunc.HandleException2(ex, "遺失圖檔!");
            }

//------------------------------------------------------------  # 60個

            //  製作 ICON 用
            // Convert the bitmap into an icon.
            //Icon icon = Icon.FromHandle(square_bm.GetHicon());
            //notifyIcon1.Icon = icon;

//------------------------------------------------------------  # 60個

bitmap1.Save(filename, ImageFormat.Icon);

*/
