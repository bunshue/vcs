using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Puzzle2
{
    public partial class Form1 : Form
    {
        private Puzzle puzzle;
        private int Num = 0;
        private Image img;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            img = GamePage.img;
            pictureBox2.Image = img.GetThumbnailImage(120, 120, new Image.GetThumbnailImageAbort(delegate { return false; }), IntPtr.Zero);
            puzzle = new Puzzle(img, 600, GamePage.Dif);
            pictureBox1.Image = puzzle.Display();
        }

        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            if (puzzle.Move(e.X / (puzzle.Width / puzzle.N), e.Y / (puzzle.Width / puzzle.N)))
            {
                Num++;
                pictureBox1.Image = puzzle.Display();
                if (puzzle.Judge())
                {
                    if (MessageBox.Show("恭喜过关", "是否重新玩一把", MessageBoxButtons.OKCancel) == DialogResult.OK)
                    {
                        Num = 0;
                        puzzle.Upset();
                        pictureBox1.Image = puzzle.Display();

                    }
                    else
                    {
                        Num = 0;
                        closefather();
                        this.Close();
                    }

                }

            }
            NumLabel.Text = Num.ToString();
        }

        private void pictureBox2_MouseEnter(object sender, EventArgs e)
        {
            pictureBox1.Image = img;
        }

        private void pictureBox2_MouseLeave(object sender, EventArgs e)
        {
            pictureBox1.Image = puzzle.Display();
        }


        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            closefather();
        }
        public delegate void childclose();
        public event childclose closefather;
    }
}

