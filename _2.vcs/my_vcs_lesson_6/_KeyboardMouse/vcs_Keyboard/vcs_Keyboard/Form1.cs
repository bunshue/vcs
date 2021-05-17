using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_Keyboard
{
    public partial class Form1 : Form
    {
        Label[] labelList = new Label[27]; // A ~ Z和空白鍵
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // 在27個按鍵的 Tag 放入 代表的 KeyCode
            label1.Tag = Keys.Q; label2.Tag = Keys.W; label3.Tag = Keys.E;
            label4.Tag = Keys.R; label5.Tag = Keys.T; label6.Tag = Keys.Y;
            label7.Tag = Keys.U; label8.Tag = Keys.I; label9.Tag = Keys.O;
            label10.Tag = Keys.P; label11.Tag = Keys.A; label12.Tag = Keys.S;
            label13.Tag = Keys.D; label14.Tag = Keys.F; label15.Tag = Keys.G;
            label16.Tag = Keys.H; label17.Tag = Keys.J; label18.Tag = Keys.K;
            label19.Tag = Keys.L; label20.Tag = Keys.Z; label21.Tag = Keys.X;
            label22.Tag = Keys.C; label23.Tag = Keys.V; label24.Tag = Keys.B;
            label25.Tag = Keys.N; label26.Tag = Keys.M; label27.Tag = Keys.Space;

            // 以陣列 取代 在27個 label 元件
            labelList[0] = label1; labelList[1] = label2; labelList[2] = label3;
            labelList[3] = label4; labelList[4] = label5; labelList[5] = label6;
            labelList[6] = label7; labelList[7] = label8; labelList[8] = label9;
            labelList[9] = label10; labelList[10] = label11; labelList[11] = label12;
            labelList[12] = label13; labelList[13] = label14; labelList[14] = label15;
            labelList[15] = label16; labelList[16] = label17; labelList[17] = label18;
            labelList[18] = label19; labelList[19] = label20; labelList[20] = label21;
            labelList[21] = label22; labelList[22] = label23; labelList[23] = label24;
            labelList[24] = label25; labelList[25] = label26; labelList[26] = label27;

            lb_result.Text = "";
        }

        // 有鍵盤按鍵被按下
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            for (int i = 0; i < labelList.Length; i++)
            {
                if (e.KeyCode == (Keys)labelList[i].Tag)
                {
                    labelList[i].BackColor = Color.Red; // 將被按下的按鍵 變為紅色
                }
            }
            if (e.KeyCode == Keys.Return)
                lb_result.Text += "\n";
            else if (e.KeyCode == Keys.Space)
                lb_result.Text += " ";
            else
                lb_result.Text += e.KeyCode;
        }

        // 有鍵盤按鍵被放開
        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            for (int i = 0; i < labelList.Length; i++)
            {
                if (e.KeyCode == (Keys)labelList[i].Tag)
                    labelList[i].BackColor = Color.Pink; // 將被放開的按鍵 變為粉紅色
            }
        }


    }
}

