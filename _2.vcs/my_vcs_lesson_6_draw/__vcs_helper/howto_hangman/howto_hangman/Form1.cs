using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Thanks to Jeff Scarterfield for the skeleton drawing at:
// http://www.how-to-draw-cartoons-online.com/cartoon-skeleton.html

using System.IO;
using System.Drawing.Text;

namespace howto_hangman
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // PictureBoxes holding skeleton pictures.
        private PictureBox[] PictureBoxes;

        // The index of the current skeleton picture.
        private int CurrentPictureIndex = 0;

        // Words.
        private string[] Words;

        // The current word.
        private string CurrentWord = "";

        // Labels to show the current word's letters.
        private List<Label> LetterLabels = new List<Label>();

        // A list holding the letter buttons.
        private List<Button> KeyboardButtons;

        // Prepare to play.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Save references to the PictureBoxes in the array.
            PictureBoxes = new PictureBox[]
            {
                picSkeleton0, picSkeleton1, picSkeleton2, picSkeleton3,
                picSkeleton4, picSkeleton5, picSkeleton6
            };

            // Load the words.
            Words = File.ReadAllLines("Words.txt");

            // Make button images.
            MakeButtonImages();
        }

        // Make the button images.
        private void MakeButtonImages()
        {
            // Prepare the buttons.
            KeyboardButtons = new List<Button>();
            foreach (Control ctl in this.Controls)
            {
                if ((ctl is Button) && (!(ctl == btnNewGame)))
                {
                    // Set the button's name.
                    ctl.Name = "btn" + ctl.Text;

                    // Attach the Click event handler.
                    ctl.Click += btnKey_Click;

                    // Make the button's image.
                    MakeButtonImage(ctl as Button);

                    // Save in the Buttons list for later use.
                    KeyboardButtons.Add(ctl as Button);
                }
            }
        }

        // Give this button an image thet fits better than its letter.
        private void MakeButtonImage(Button btn)
        {
            Bitmap bm = new Bitmap(btn.ClientSize.Width, btn.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
                using (StringFormat string_format = new StringFormat())
                {
                    string_format.Alignment = StringAlignment.Center;
                    string_format.LineAlignment = StringAlignment.Center;
                    gr.DrawString(btn.Text, btn.Font, Brushes.Black,
                        btn.ClientRectangle, string_format);
                }
            }
            btn.Tag = btn.Text;
            btn.Image = bm;
            btn.Text = "";
        }

        // Prepare for a new game.
        private void btnNewGame_Click(object sender, EventArgs e)
        {
            // Delete old letter labels.
            foreach (Label lbl in LetterLabels)
            {
                flpLetters.Controls.Remove(lbl);
                lbl.Dispose();
            }

            // Pick a new word.
            Random rand = new Random();
            CurrentWord = Words[rand.Next(Words.Length)].ToUpper();
            // Console.WriteLine(CurrentWord);

            // Create new letter labels.
            LetterLabels = new List<Label>();
            foreach (char ch in CurrentWord)
            {
                Label lbl = new Label();
                flpLetters.Controls.Add(lbl);
                lbl.Tag = ch.ToString();
                lbl.Size = btnQ.Size;
                lbl.TextAlign = ContentAlignment.MiddleCenter;
                lbl.BackColor = Color.White;
                lbl.BorderStyle = BorderStyle.Fixed3D;
                LetterLabels.Add(lbl);
            }

            // Hide the won/lost labels.
            lblWon.Visible = false;
            lblLost.Visible = false;

            // Enable the letter buttons.
            foreach (Button letter_btn in KeyboardButtons) letter_btn.Enabled = true;

            // Display the first picture.
            PictureBoxes[CurrentPictureIndex].Visible = false;
            CurrentPictureIndex = 0;
            PictureBoxes[CurrentPictureIndex].Visible = true;
        }

        // A key was clicked.
        private void btnKey_Click(object sender, EventArgs e)
        {
            // Disable this button so the user can't click it again.
            Button btn = sender as Button;
            btn.Enabled = false;

            // See if this letter is in the current word.
            string ch = btn.Tag.ToString();
            if (CurrentWord.Contains(ch))
            {
                // Good guess. Display matching letters.
                bool has_won = true;
                foreach (Label lbl in LetterLabels)
                {
                    // See if this letter matches the current guess.
                    if (lbl.Tag.ToString() == ch) lbl.Text = ch.ToString();

                    // See if the user has found this letter.
                    if (lbl.Text == "") has_won = false;
                }

                // See if the user has won.
                if (has_won)
                {
                    lblWon.Visible = true;
                    foreach (Button letter_btn in KeyboardButtons) letter_btn.Enabled = false;
                }
            }
            else
            {
                // Bad guess. Show the next picture.
                PictureBoxes[CurrentPictureIndex].Visible = false;
                CurrentPictureIndex++;
                PictureBoxes[CurrentPictureIndex].Visible = true;

                // See if the user has lost.
                if (CurrentPictureIndex == PictureBoxes.Length - 1)
                {
                    lblLost.Visible = true;
                    foreach (Button letter_btn in KeyboardButtons) letter_btn.Enabled = false;
                    foreach (Label lbl in LetterLabels) lbl.Text = lbl.Tag.ToString();
                }
            }
        }
    }
}
