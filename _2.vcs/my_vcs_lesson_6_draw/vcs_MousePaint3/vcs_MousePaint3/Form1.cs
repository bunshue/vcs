using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for SmoothingMode, Matrix, MatrixOrder, HatchBrush

// 滑鼠操作畫圖相關

namespace vcs_MousePaint3
{
    public partial class Form1 : Form
    {
        float angleEarth = 0;  // 地球的旋轉角度
        float angleMoon = 0;   // 月球的旋轉角度

        float deltaEarth = 1;  // 地球旋轉角度的遞增值
        float deltaMoon = 12;  // 月球旋轉角度的遞增值

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        Bitmap bitmap1; // Bitmap 影像
        Point MousePos = new Point(); //滑鼠位置

        float shearX = 0; // X 軸水平分歧因數
        float shearY = 0; // Y 軸垂直分歧因數
        Point MP; // 滑鼠游標座標

        HatchBrush myBrush1 = new HatchBrush(HatchStyle.Cross, Color.Red);
        float theta = 0; // 旋轉角度

        int EPSILON = 100; // 滑鼠 是否 點選到點 的距離 判斷 (避免 開根號)

        //pictureBox5 拖曳圖片框中的紅點 ST
        //Point一維陣列
        Point[] pts5 = new Point[6];    //一維陣列內有6個Point
        int find_point_index = -1;
        //pictureBox5 拖曳圖片框中的紅點 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            this.DoubleBuffered = true;

            pictureBox0.BackColor = Color.Black;
            bitmap1 = (Bitmap)Bitmap.FromFile(filename);


            //pictureBox5 拖曳圖片框中的紅點 ST
            int x_st = 100;
            int y_st = 80;
            int dy = 50;
            pts5[0] = new Point(x_st + 0, y_st + dy * 0);
            pts5[1] = new Point(x_st + 0, y_st + dy * 1);
            pts5[2] = new Point(x_st + 0, y_st + dy * 2);
            pts5[3] = new Point(x_st + 0, y_st + dy * 3);
            pts5[4] = new Point(x_st + 0, y_st + dy * 4);
            pts5[5] = new Point(x_st + 0, y_st + dy * 5);
            //pictureBox5 拖曳圖片框中的紅點 SP
        }

        void show_item_location()
        {
            int W = 460;
            int H = 400;
            int x_st = 10;
            int y_st = 30;
            int dx = W + 20;
            int dy = H + 50;
            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label4.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label5.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label0.Text = "太陽、地球、與月亮 (↑↓←→空白鍵)";
            label1.Text = "扭曲的影像";
            label2.Text = "切變矩陣";
            label3.Text = "畫布轉換矩陣的旋轉設定 - 繞固定點公轉";
            label4.Text = "";
            label5.Text = "";

            richTextBox1.Size = new Size(W - 200, H * 2 + 60);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
            this.Text = "vcs_MousePaint3";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void pictureBox0_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出 太陽
            e.Graphics.TranslateTransform(this.pictureBox1.ClientSize.Width / 2, this.pictureBox1.ClientSize.Height / 2);
            e.Graphics.FillEllipse(Brushes.Crimson, -100, -100, 200, 200);

            // 繪出 地球
            e.Graphics.RotateTransform(angleEarth);
            e.Graphics.TranslateTransform(200, 0);
            e.Graphics.FillEllipse(Brushes.Cyan, -20, -20, 40, 40);

            // 繪出 月球
            e.Graphics.RotateTransform(angleMoon);
            e.Graphics.TranslateTransform(40, 0);
            e.Graphics.FillEllipse(Brushes.PaleGreen, -5, -5, 10, 10);
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                Cursor = Cursors.Hand;
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                MousePos = e.Location; // 記錄滑鼠位置
                this.pictureBox1.Invalidate(); // 要求表單重畫
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            Cursor = Cursors.Default;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.pictureBox1.ClientSize.Height / 2;

            Point[] pt = new Point[3];  // 三個點座標 定義一個平形四邊形
            pt[0] = new Point(MousePos.X - bitmap1.Width / 2, MousePos.Y); // 左上
            pt[1] = new Point(MousePos.X + bitmap1.Width / 2, MousePos.Y); // 右上
            pt[2] = new Point(Cx - bitmap1.Width / 2, Cy + bitmap1.Height / 2); // 左下

            e.Graphics.DrawImage(bitmap1, pt); // 呈現原圖
        }

        private void pictureBox2_MouseClick(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            MP = e.Location; // 紀錄滑鼠游標座標
            this.pictureBox2.Invalidate();// 要求表單重畫
        }

        private void pictureBox2_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.pictureBox2.ClientSize.Width / 2;
            int Cy = this.pictureBox2.ClientSize.Height / 2;
            int D = 100; // 球本身的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D, Cy - D, 2 * D, 2 * D); //畫出開始的圓

            shearX = (MP.X - Cx) / (float)D; // X 軸水平分歧因數
            shearY = (MP.Y - Cy) / (float)D; // Y 軸水平分歧因數

            this.Text = "切變矩陣 (" + shearX.ToString() + ", " + shearY.ToString() + ")";

            Matrix A = new Matrix(); // 轉換矩陣
            A.Shear(shearX, shearY, MatrixOrder.Append);  // 乘上 切變矩陣
            A.Translate(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            e.Graphics.Transform = A;  // 畫布的矩陣 = 矩陣 A
            e.Graphics.DrawEllipse(Pens.Red, 0 - D, 0 - D, 2 * D, 2 * D); //畫出縮放後的圓
        }

        private void pictureBox3_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;

            int Cx = this.pictureBox3.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.pictureBox3.ClientSize.Height / 2;//
            int D = 20; // 球本身的半徑
            int D2 = 100; // 球旋轉的半徑

            e.Graphics.ResetTransform(); // 畫布的矩陣 = 單位矩陣
            e.Graphics.FillEllipse(Brushes.Gray, Cx - D, Cy - D, 2 * D, 2 * D); //畫出正中心圓點 
            e.Graphics.DrawEllipse(Pens.Silver, Cx - D2, Cy - D2, 2 * D2, 2 * D2); //畫出軌道

            e.Graphics.TranslateTransform(D2, 0, MatrixOrder.Append);  // 先平移到 旋轉的半徑邊緣
            e.Graphics.RotateTransform(theta, MatrixOrder.Append);  // 乘上 旋轉矩陣
            e.Graphics.TranslateTransform(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點
            e.Graphics.FillEllipse(myBrush1, 0 - D, 0 - D, 2 * D, 2 * D); //畫出旋轉的圓點 
        }

        private void pictureBox4_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        bool flag_pictureBox5_mouse_down = false;
        private void pictureBox5_MouseDown(object sender, MouseEventArgs e)
        {
            Point pt = FindPointAt(e.X, e.Y);
            if (pt == new Point(9999, 9999))
            {
                richTextBox1.Text += "找不到\n";
            }
            else
            {
                flag_pictureBox5_mouse_down = true;
                richTextBox1.Text += "找到 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")\t";
                int index = get_index(pt);
                richTextBox1.Text += "索引 : " + index.ToString() + "\n";
                find_point_index = index;
            }
        }

        private Point FindPointAt(int X, int Y)
        {
            foreach (Point pt in pts5)
            {
                float dx = pt.X - X;
                float dy = pt.Y - Y;
                if (dx * dx + dy * dy <= EPSILON)
                {
                    return pt;
                }
            }
            return new Point(9999, 9999);
        }

        int get_index(Point point)
        {
            int len = pts5.Length;
            for (int index = 0; index < len; index++)
            {
                if (point == pts5[index])
                {
                    return index;
                }
            }
            return -1;
        }

        private void pictureBox5_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox5_mouse_down == true)
            {
                update_pts(find_point_index, e.Location);
                this.pictureBox5.Invalidate();
            }
        }

        private void pictureBox5_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox5_mouse_down = false;
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawString("拖曳圖片框中的紅點", new Font("標楷體", 16), new SolidBrush(Color.Black), 20, 20);
            //e.Graphics.DrawRectangle(Pens.Red, 100, 100, 300, 300);
            foreach (Point pt in pts5)
            {
                e.Graphics.FillEllipse(Brushes.Red, pt.X - 10, pt.Y - 10, 20, 20);
            }
        }

        void update_pts(int index, Point point)
        {
            int len = pts5.Length;
            if ((index < 0) || index >= len)
            {
                richTextBox1.Text += index.ToString();
                //richTextBox1.Text += "XXXXXXX\n";
                return;
            }
            pts5[index] = point;
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            angleEarth += deltaEarth; // 地球的旋轉角度 累進
            angleEarth %= 360;

            angleMoon += deltaMoon; // 月球的旋轉角度 累進
            angleMoon %= 360;
            this.pictureBox0.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Up)
            {
                deltaEarth += 1;
            }
            else if (e.KeyData == Keys.Down)
            {
                deltaEarth -= 1;
                if (deltaEarth < 1)
                {
                    deltaEarth = 1;
                }
            }

            if (e.KeyData == Keys.Right)
            {
                deltaMoon += 1;
            }
            else if (e.KeyData == Keys.Left)
            {
                deltaMoon -= 1;
                if (deltaMoon < 1)
                {
                    deltaMoon = 1;
                }
            }

            if (e.KeyData == Keys.Space)
            {
                deltaEarth = 1;
                deltaMoon = 12;
            }
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
            theta = theta + 1; // 旋轉角度 遞增
            this.pictureBox3.Invalidate(); // 要求表單重畫
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
