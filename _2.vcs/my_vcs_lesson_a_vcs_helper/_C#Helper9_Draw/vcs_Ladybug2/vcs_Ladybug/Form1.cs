using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


//感覺上原本的不會閃爍~~~~~~~~~~~~
 

namespace vcs_Ladybug
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        Bitmap bitmap1; // 圖形

        public PointF pos = new Point(50, 50);  // 座標
        public double Angle_Offset = 90; //-Math.PI / 2;  // 開始的旋轉矯正徑度
        public PointF Wander_Center = new Point(1920 / 2, 1080 / 2); // 漫遊的中心點
        public double Wander_Radius = 200; // 漫遊的半徑距離
        public int Speed = 5; // 漫遊的速度

        double Angle = 0; // 目前的旋轉角度
        //Random rd = new Random(); // 亂數

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename2 = @"C:\______test_files\__RW\_png\ladybug.png";
            bitmap1 = new Bitmap(filename2);

            Update();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            //button1.Location = new Point(1920 - 300 - 10 - 80, 0);
            richTextBox1.Size = new Size(300, 1040);
            richTextBox1.Location = new Point(1920 - 300 - 10, 0);
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            //gc.Wander_Center = new PointF(1920 / 4, 1080 / 4);
            Update();
            this.Invalidate();
            //richTextBox1.Text += "(" + gc.pos.X.ToString() + ", " + gc.pos.Y.ToString() + ") ";
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.ResetTransform();
            Draw(e.Graphics);


            float xx = Wander_Center.X;
            float yy = Wander_Center.Y;
            float rr = 10;
            e.Graphics.DrawEllipse(Pens.Red, xx - rr / 2, yy - rr / 2, rr, rr);

            rr = (float)Wander_Radius * 5;
            e.Graphics.DrawEllipse(Pens.Red, xx - rr / 2, yy - rr / 2, rr, rr);

            rr = (float)Wander_Radius * 1;
            e.Graphics.DrawEllipse(Pens.Red, xx - rr / 2, yy - rr / 2, rr, rr);
        }

        public void Update()
        {
            Random random = new Random(); // 亂數
            // NPC 和 漫遊中心點 的 夾角向量
            PointF vectorToCenter = new PointF(Wander_Center.X - pos.X, Wander_Center.Y - pos.Y);
            // NPC 和 漫遊中心點 的距離
            double len = Math.Sqrt((Wander_Center.X - pos.X) * (Wander_Center.X - pos.X) +
                                   (Wander_Center.Y - pos.Y) * (Wander_Center.Y - pos.Y));

            //richTextBox1.Text += "len = " + len.ToString();
            if (len > 5 * Wander_Radius) // 在 5 倍 的漫遊半徑距離 外
            {
                richTextBox1.Text += " A";
                // NPC 和 漫遊中心點 的角度
                double Yaw2 = Math.Atan2(vectorToCenter.Y, vectorToCenter.X);

                // Yaw2 和 NPC 角度 的 角度差
                double diff = Yaw2 - Angle;

                Angle = Angle + diff; // 一次就 矯正 回來
            }
            else if (len > Wander_Radius) // 在 漫遊的半徑距離 外
            {
                richTextBox1.Text += " B";
                // NPC 和 漫遊中心點 的角度
                double Yaw2 = Math.Atan2(vectorToCenter.Y, vectorToCenter.X);

                // Yaw2 和 NPC 角度 的 角度差
                double diff = Yaw2 - Angle;

                // 欲矯正的角度
                double r;
                r = 0.01 * Math.PI * len / Wander_Radius; // NPC 和 漫遊中心點 距離愈遠 矯正的角度愈大

                if (diff < -r) diff = -r; // 慢慢把 角度差 矯正回來
                else if (diff > r) diff = r;

                Angle = Angle + (diff + (random.NextDouble() * 0.001)); // 再加一點點 亂數
            }
            else // 在 漫遊的半徑距離 內
            {
                richTextBox1.Text += " C";
                double rate = random.NextDouble() * 0.06 - 0.03; // 一些 亂數 改變 角度
                Angle += rate;
            }

            while (Angle < -Math.PI)
            {
                Angle += Math.PI * 2; // 確定  Angle 是在 -Math.PI ~ Math.PI 之間
            }
            while (Angle > Math.PI)
            {
                Angle -= Math.PI * 2;
            }

            pos.X += (float)(Speed * Math.Cos(Angle)); // NPC 新的座標
            pos.Y += (float)(Speed * Math.Sin(Angle));
        }

        public void Draw(Graphics G)
        {
            G.ResetTransform();  // 重設 畫布的轉換矩陣
            G.TranslateTransform(pos.X, pos.Y); // 平移 畫布 的中心點
            G.RotateTransform((float)(Angle_Offset + (Angle * 180.0 / Math.PI))); // 旋轉 畫布 
            G.DrawImage(bitmap1, 0 - bitmap1.Width / 2, 0 - bitmap1.Height / 2, bitmap1.Width, bitmap1.Height); //繪出 圖形
            G.ResetTransform(); // 重設 畫布的轉換矩陣
        }
    }
}


