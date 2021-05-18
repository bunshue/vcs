using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics; // for Stopwatch 碼表

namespace vcs_GameControl1
{
    public partial class Form1 : Form
    {
        Stopwatch sw = new Stopwatch(); // 碼表
        double time_Last = 0;  // 記錄上一個畫面的碼表時間
        double elapsedTime;    // 從 上一個畫面 到 這一個畫面 所經過的時間

        // 各個元件的宣告 要寫在這裡 ↓↓↓↓↓↓↓↓
        G2D_Image_Plane image_Plane;  // <==== 示範

        public Form1()
        {
            InitializeComponent();

            this.ClientSize = new Size(800, 600); // Form1 的寬高設定
        }

        // Form1 第一次上載時 要初始化 各個遊戲元件、並且按下碼表，開始計時
        private void Form1_Load(object sender, EventArgs e)
        {
            // 各個元件初始化 要寫在這裡 ↓↓↓↓↓↓↓↓
            image_Plane = new G2D_Image_Plane(this, Properties.Resources.plane, new Point(400, 300));    // <==== 示範

            // 碼表開始動作
            sw.Reset(); // 碼表歸零
            sw.Start(); // 開始計時
        }

        // Form1 定時更新
        private void Form1_Update()
        {
            TimeSpan ts = TimeSpan.FromMilliseconds(sw.ElapsedMilliseconds); // 碼表經過的時間
            double time_Now = ts.TotalMilliseconds;  // 這一個畫面的碼表時間
            elapsedTime = time_Now - time_Last;  // 從 上一個畫面 到 這一個畫面 經過的時間

            // 各個元件 更新函數 的呼叫 都寫在這裡 ↓↓↓↓↓↓↓↓
            image_Plane.Update(elapsedTime);    // <==== 示範

            time_Last = time_Now; // 這一個畫面的碼表時間 就是下一個畫面 的 上一個畫面的碼表時間
        }

        // Form1 定時重畫
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias; // 反鋸齒繪出
            
            // 各個元件 繪出函數 的呼叫 都寫在這裡 ↓↓↓↓↓↓↓↓
            image_Plane.Draw(e.Graphics);     // <==== 示範
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Form1_Update();     // Form1 定時更新
            this.Invalidate();  // Form1 定時重畫
        }
    }
}
