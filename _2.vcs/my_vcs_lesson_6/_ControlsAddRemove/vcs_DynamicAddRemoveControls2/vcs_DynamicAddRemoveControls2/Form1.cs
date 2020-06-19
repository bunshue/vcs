using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DynamicAddRemoveControls2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Button[,] btn = new Button[3, 3];
        Font font = new Font("微軟正黑體", 12);

        private void button1_Click(object sender, EventArgs e)
        {
            btn = new Button[3, 3];
            for (int x = 0; x < btn.GetLength(0); x++)
            {
                for (int y = 0; y < btn.GetLength(1); y++)
                {
                    btn[x, y] = new Button();
                    btn[x, y].Size = new Size(100, 100);
                    btn[x, y].Text = "";
                    btn[x, y].Location = new Point(50 + x * 100, 50 + y * 100);
                    btn[x, y].Font = font;
                    btn[x, y].Name = "( " + x.ToString() + ", " + y.ToString() + ")";
                    btn[x, y].Click += ButtonsClick;
                    //panel.Controls.Add(btn[x, y]);
                    this.Controls.Add(btn[x, y]);
                }
            }



        }

        private void ButtonsClick(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            richTextBox1.Text += "你按了 " + btn.Name + "\n";

            if (btn.BackColor != Color.Pink)
                btn.BackColor = Color.Pink;
            else
                btn.BackColor = SystemColors.ControlLight;

            /*
            if (btn.Text == "" && count < 9)
            {
                btn.Text = nowIndex == true ? symbol2 : symbol1;
                nowIndex = !nowIndex;
                label.Text = nowIndex == true ? "玩家二，請選擇。" : "玩家一，請選擇。";
                Check();
                count++;
                if (count == 9)
                {
                    label.Text = "GameOver!";
                    GameOver("GameOver");
                }
                Console.WriteLine(count);
            }
            */
        }



    }
}
