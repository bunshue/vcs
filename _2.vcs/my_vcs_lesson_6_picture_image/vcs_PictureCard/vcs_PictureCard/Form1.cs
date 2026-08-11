using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Card deck from:
// http://www.thehouseofcards.com/img/misc/Deck-72x100x16.gif

namespace vcs_PictureCard
{
    public partial class Form1 : Form
    {
        // Basic deck information.
        // The 5th suite is for the back, jokers, etc.
        private const int NumSuits = 5;
        private const int NumRanks = 13;
        private int CardWidth;
        private int CardHeight;
        int W = 936;
        int H = 500;

        // The suits in their order in the file.
        private enum Suits
        {
            紅心,
            方塊,
            梅花,
            黑桃,
            其他,
        }

        // PictureBoxes holding card images.
        private PictureBox[,] Pics = null;

        public Form1()
        {
            InitializeComponent();
        }

        // Load the cards.
        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            // Load the card images.
            LoadCardImages();

            // Arrange the card PictureBoxes.
            ArrangeCards();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273 + 210, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        // Load the card PictureBoxes.
        private void LoadCardImages()
        {
            CardWidth = W / NumRanks;
            CardHeight = H / NumSuits;
            int x0 = 0;
            int y0 = 0;
            int dx = CardWidth;
            int dy = CardHeight;
            Pics = new PictureBox[NumRanks, NumSuits];
            int y = y0;
            for (int suit = 0; suit < NumSuits; suit++)
            {
                int x = x0;
                for (int rank = 0; rank < NumRanks; rank++)
                {
                    Pics[rank, suit] = LoadCard(rank, suit, x, y);
                    x += dx;
                }
                y += dy;
            }
        }

        // Load a single card from the deck.
        private PictureBox LoadCard(int rank, int suit, int x, int y)
        {
            // Get the image.
            PictureBox pic = new PictureBox();
            Bitmap bm = LoadCardImage(rank, suit, x, y);

            // Make the PictureBox.
            pic.Image = bm;
            pic.SizeMode = PictureBoxSizeMode.AutoSize;
            pic.BorderStyle = BorderStyle.Fixed3D;
            pic.Location = new Point(0, 0);
            pic.Parent = this;
            pic.MouseEnter += pic_MouseEnter;
            pic.MouseLeave += pic_MouseLeave;

            // Give the PictureBox a Card object so
            // we can tell what card it is.
            pic.Tag = new Card(rank, suit, bm);

            return pic;
        }

        // Return the image for a card.
        private Bitmap LoadCardImage(int rank, int suit, int x, int y)
        {
            Bitmap bm = new Bitmap(CardWidth, CardHeight);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                Rectangle dest_rect = new Rectangle(0, 0, CardWidth, CardHeight);
                Rectangle src_rect = new Rectangle(x, y, CardWidth, CardHeight);
                gr.DrawImage(Properties.Resources.cards, dest_rect, src_rect, GraphicsUnit.Pixel);
            }
            return bm;
        }

        // Arrange the card PictureBoxes.
        private void ArrangeCards()
        {
            // Display the deck.
            const int margin = 4;
            int y = margin;
            for (int suit = 0; suit < NumSuits; suit++)
            {
                int x = margin;
                for (int rank = 0; rank < NumRanks; rank++)
                {
                    Pics[rank, suit].Location = new Point(x, y);
                    x += Pics[0, 0].Width + margin;
                }
                y += Pics[0, 0].Height + margin;
            }
        }

        // Display the card's information.
        private void pic_MouseEnter(object sender, EventArgs e)
        {
            // Get the card information.
            PictureBox pic = sender as PictureBox;
            Card card = pic.Tag as Card;
            Suits suit = (Suits)card.Suit;
            int rank = card.Rank + 1;
            Text = suit.ToString() + " " + rank.ToString();
            //richTextBox1.Text += rank.ToString() + " of " + suit.ToString() + "\n";
        }

        // Clear the cardf information.
        private void pic_MouseLeave(object sender, EventArgs e)
        {
            Text = "";
        }
    }

    public class Card
    {
        public int Rank;
        public int Suit;
        public Bitmap Picture;

        public Card(int rank, int suit, Bitmap picture)
        {
            Rank = rank;
            Suit = suit;
            Picture = picture;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

