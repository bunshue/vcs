using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace vcs_Puzzle2
{
    public partial class Menu : Form
    {
        string puzzle_filename = @"../../img/picture.jpg";

        public Menu()
        {
            InitializeComponent();
            GamePage.img = Image.FromFile(puzzle_filename);
            Control.CheckForIllegalCrossThreadCalls = false;
        }

        private void Menu_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            GamePage.Dif = Puzzle.Diff.simple;
            this.Hide();
            Form1 ff = new Form1();
            ff.closefather += new vcs_Puzzle2.Form1.childclose(this.closethis);
            ff.Show();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            GamePage.Dif = Puzzle.Diff.ordinary;
            this.Hide();
            Form1 ff = new Form1();
            ff.closefather += new vcs_Puzzle2.Form1.childclose(this.closethis);
            ff.Show();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            GamePage.Dif = Puzzle.Diff.difficulty;
            this.Hide();
            Form1 ff = new Form1();
            ff.closefather += new vcs_Puzzle2.Form1.childclose(this.closethis);
            ff.Show();
        }

        public void closethis()
        {
            this.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            if (ofd.ShowDialog() == DialogResult.OK)
            {
                GamePage.img = Image.FromFile(ofd.FileName).GetThumbnailImage(600, 600, new Image.GetThumbnailImageAbort(delegate { return false; }), IntPtr.Zero);
            }
        }
    }
}

