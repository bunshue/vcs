using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Media;

namespace vcs_Metronome
{
    public partial class Form1 : Form
    {
        Bitmap steper = Properties.Resources.Bitmap__Steper00;  // 節拍器 本體
        Bitmap steper2 = Properties.Resources.Bitmap__Steper01; // 節拍器 的指針
        G2D_ImageSwing swing;   // 節拍器 指針 的物件
        int D = 1; // 累進的方向
        float Tempo = 1000; // 一拍 1 秒 = 1000 千秒
        DateTime m_start = DateTime.MinValue; // 開始的時間
        int seg = 2; // 節奏
        int segN = 0; // 節奏記數

        SoundPlayer sound01 = new SoundPlayer(Properties.Resources.sound01);
        SoundPlayer sound02 = new SoundPlayer(Properties.Resources.sound02);

        public Form1()
        {
            InitializeComponent();

            this.ClientSize = new Size(650, 550); 

            swing = new G2D_ImageSwing(steper2,
                new Point(170, 420),  // 節拍器 指針 貼到 視窗客戶區 的位置 (視窗客戶區 座標)
                new Point(25, 350));  // 節拍器 指針的旋轉點 (圖形座標)

            sound01.Play();
            
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawImage(steper, 20, 20, steper.Width, steper.Height); // 繪出 節拍器 本體

            //e.Graphics.DrawImage(steper2, 154, 47);
            swing.Draw(e.Graphics); // 繪出 節拍器 的指針
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now; // 當下的時間
            TimeSpan ts = dt - m_start; // 經過的時間
            double tm = ts.TotalMilliseconds; // 經過的時間的總千分秒數

            swing.theta = swing.theta + (float)(D * (tm / Tempo) * 40);

            if (swing.theta >= 20)
            {
                D = -1; // 改變旋轉的方向
                swing.theta = 20 - (swing.theta - 20); // 超過的角度 要補回來

                segN++;
                if (segN >= seg)
                {
                    // 發出聲音 
                    segN = 0;
                    sound02.Play();
                }
                else
                {
                    // 發出聲音
                    sound01.Play();
                }
            }
            else if (swing.theta <= -20)
            {
                D = 1;
                swing.theta = -20 + (swing.theta + 20);

                segN++;
                if (segN >= seg)
                {
                    // 發出聲音 
                    segN = 0;
                    sound02.Play();
                }
                else
                {
                    // 發出聲音
                    sound01.Play();
                }
            }

            m_start = dt;
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            m_start = DateTime.Now; // 當下的時間
            timer1.Enabled = !timer1.Enabled; // true;
            if (timer1.Enabled)  // 如果是關閉的 就開始
            {
                button1.Text = "關 閉";
                segN = 0; // 節奏記數
            }
            else
            {
                button1.Text = "開 始";
                swing.theta = 0;
                this.Invalidate();
            }
        }

        private void radioButton1_Click(object sender, EventArgs e)
        {
            RadioButton rb = (RadioButton)sender;
            if (rb == radioButton1) Tempo = 1000;
            else if (rb == radioButton2) Tempo = (60.0f / 90.0f) * 1000;
            else if (rb == radioButton3) Tempo = (60.0f / 120.0f) * 1000;
            else if (rb == radioButton4) Tempo = (60.0f / 180.0f) * 1000;
            else if (rb == radioButton5) Tempo = (60.0f / 270.0f) * 1000;
            else if (rb == radioButton6) Tempo = (60.0f / 360.0f) * 1000;
        }

        private void radioButton7_Click(object sender, EventArgs e)
        {
            RadioButton rb = (RadioButton)sender;
            if (rb == radioButton7) seg = 2;
            else if (rb == radioButton8) seg = 3;
            else if (rb == radioButton9) seg = 4;
            else if (rb == radioButton10) seg = 5;
            else if (rb == radioButton11) seg = 6;
            else if (rb == radioButton12) seg = 7;
        }
    }
}
