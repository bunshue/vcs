using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;

namespace howto_steganography
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The unmodified and modified pictures.
        private Bitmap 
            OriginalImage = null,
            EncodedImage = null,
            MarkedImage = null;

        // Exit.
        private void mnuFileExit_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        // Load a picture.
        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdImage.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    OriginalImage = new Bitmap(ofdImage.FileName);
                    MarkedImage = null;
                    EncodedImage = null;
                    radOriginal.Checked = true;
                    picImage.Image = OriginalImage;
                    mnuFileSave.Enabled = false;
                    btnEncode.Enabled = true;
                    btnDecode.Enabled = true;

                    // Size to show the whole picture.
                    int wid = Math.Max(this.ClientSize.Width,
                        picImage.Bounds.Right + picImage.Left);
                    int hgt = Math.Max(this.ClientSize.Height,
                        picImage.Bounds.Bottom + picImage.Left);
                    this.ClientSize = new Size(wid, hgt);
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message);
                }
            }
        }

        // Save the modified picture.
        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            if (EncodedImage == null)
            {
                MessageBox.Show("You have not added a message to the image.");
            }
            else
            {
                if (sfdImage.ShowDialog() == DialogResult.OK)
                {
                    try
                    {
                        FileInfo file_info = new FileInfo(sfdImage.FileName);
                        switch (file_info.Extension)
                        {
                            case ".png":
                                EncodedImage.Save(sfdImage.FileName, ImageFormat.Png);
                                break;
                            case ".bmp":
                                EncodedImage.Save(sfdImage.FileName, ImageFormat.Bmp);
                                break;
                            case ".gif":
                                EncodedImage.Save(sfdImage.FileName, ImageFormat.Gif);
                                break;
                            case ".tiff":
                            case ".tif":
                                EncodedImage.Save(sfdImage.FileName, ImageFormat.Tiff);
                                break;
                            case ".jpg":
                            case ".jpeg":
                                EncodedImage.Save(sfdImage.FileName, ImageFormat.Jpeg);
                                break;
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }
                }
            }
        }

        // Encode the message in the picture.
        private void btnEncode_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();

            // Copy the original message.
            EncodedImage = (Bitmap)OriginalImage.Clone();
            MarkedImage = (Bitmap)OriginalImage.Clone();

            // Encode.
            try
            {
                EncodeMessageInImage(EncodedImage, MarkedImage,
                    txtPassword.Text, txtMessage.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            // Display the results.
            radMarked.Checked = true;
            picImage.Image = MarkedImage;

            mnuFileSave.Enabled = true;
            this.Cursor = Cursors.Default;
        }

        // Encode a message into an image.
        private void EncodeMessageInImage(Bitmap bm, Bitmap visible_bm, string password, string message)
        {
            // Initialize a random number generator.
            Random rand = new Random(NumericPassword(password));

            // Create a new HashSet.
            HashSet<string> used_positions = new HashSet<string>();

            // Encode the message length.
            byte[] bytes = BitConverter.GetBytes(message.Length);
            for (int i=0; i < bytes.Length; i++)
            {
                EncodeByte(bm, visible_bm, rand, bytes[i], used_positions);
            }

            // Encode the message.
            char[] chars = message.ToCharArray();
            for (int i = 0; i < chars.Length; i++)
            {
                EncodeByte(bm, visible_bm, rand, (byte)chars[i], used_positions);
            }
        }

        // Encode a byte in the picture.
        private void EncodeByte(Bitmap bm, Bitmap visible_bm, Random rand,
            byte value, HashSet<string> used_positions)
        {
            for (int i = 0; i < 8; i++)
            {
                // Pick a position for the ith bit.
                int row, col, pix;
                PickPosition(bm, rand, used_positions, out row, out col, out pix);

                // Get the color's pixel components.
                Color clr = bm.GetPixel(row, col);
                byte r = clr.R;
                byte g = clr.G;
                byte b = clr.B;

                // Get the next bit to store.
                int bit = 0;
                if ((value & 1) == 1) bit = 1;
                
                // Update the color.
                switch (pix)
                {
                    case 0:
                        r = (byte)((r & 0xFE) | bit);
                        break;
                    case 1:
                        g = (byte)((g & 0xFE) | bit);
                        break;
                    case 2:
                        b = (byte)((b & 0xFE) | bit);
                        break;
                }
                clr = Color.FromArgb(clr.A, r, g, b);
                bm.SetPixel(row, col, clr);

                // Display a red pixel.
                visible_bm.SetPixel(row, col, Color.Red);

                // Move to the next bit in the value.
                value >>= 1;
            }
        }

        // Pick an unused (r, c, pixel) combination.
        private void PickPosition(Bitmap bm, Random rand,
            HashSet<string> used_positions,
            out int row, out int col, out int pix)
        {
            for ( ; ; )
            {
                // Pick random r, c, and pix.
                row = rand.Next(0, bm.Width);
                col = rand.Next(0, bm.Height);
                pix = rand.Next(0, 3);

                // See if this location is available.
                string key = 
                    row.ToString() + "/" +
                    col.ToString() + "/" +
                    pix.ToString();
                if (!used_positions.Contains(key)) 
                {
                    used_positions.Add(key);
                    return;
                }
            }
        }

        // Convert a string password into a numeric value.
        private int NumericPassword(string password)
        {
            // Initialize the shift values to different non-zero values.
            int shift1 = 3;
            int shift2 = 17;

            // Process the message.
            char[] chars = password.ToCharArray();
            int value = 0;
            for (int i = 1; i < password.Length; i++)
            {
                // Add the next letter.
                int ch_value = (int)chars[i];
                value ^= (ch_value << shift1);
                value ^= (ch_value << shift2);

                // Change the shifts.
                shift1 = (shift1 + 7) % 19;
                shift2 = (shift2 + 13) % 23;
            }
            return value;            
        }

        // Display the appropriate image.
        private void radOriginal_CheckedChanged(object sender, EventArgs e)
        {
            picImage.Image = OriginalImage;
        }
        private void radEncoded_CheckedChanged(object sender, EventArgs e)
        {
            picImage.Image = EncodedImage;
        }
        private void radMarked_CheckedChanged(object sender, EventArgs e)
        {
            picImage.Image = MarkedImage;
        }

        // Decode the message in the picture.
        private void btnDecode_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            txtMessage.Text = "";
            Application.DoEvents();

            // Decode.
            try
            {
                txtMessage.Text = DecodeMessageInImage(OriginalImage, txtPassword.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            this.Cursor = Cursors.Default;
        }

        // Decode the message hidden in a picture.
        private string DecodeMessageInImage(Bitmap bm, string password)
        {
            // Initialize a random number generator.
            Random rand = new Random(NumericPassword(password));

            // Create a new HashSet.
            HashSet<string> used_positions = new HashSet<string>();

            // Make a byte array big enough to hold the message length.
            int len = 0;
            byte[] bytes = BitConverter.GetBytes(len);

            // Decode the message length.
            for (int i = 0; i < bytes.Length; i++)
            {
                bytes[i] = DecodeByte(bm, rand, used_positions);
            }
            len = BitConverter.ToInt32(bytes, 0);

            // Sanity check.
            if (len > 10000)
            {
                throw new InvalidDataException(
                    "Message length " + len.ToString() +
                    " is too big to make sense. Invalid password.");
            }

            // Decode the message bytes.
            char[] chars = new char[len];
            for (int i = 0; i < chars.Length; i++)
            {
                chars[i] = (char)DecodeByte(bm, rand, used_positions);
            }
            return new string(chars);
        }

        // Decode a byte.
        private byte DecodeByte(Bitmap bm, Random rand, HashSet<string> used_positions)
        {
            byte value = 0;
            byte value_mask = 1;
            for (int i = 0; i < 8; i++)
            {
                // Find the position for the ith bit.
                int row, col, pix;
                PickPosition(bm, rand, used_positions, out row, out col, out pix);

                // Get the color component value.
                byte color_value = 0;
                switch (pix)
                {
                    case 0:
                        color_value = bm.GetPixel(row, col).R;
                        break;
                    case 1:
                        color_value = bm.GetPixel(row, col).G;
                        break;
                    case 2:
                        color_value = bm.GetPixel(row, col).B;
                        break;
                }

                // Set the next bit if appropriate.
                if ((color_value & 1) == 1)
                {
                    // Set the bit.
                    value = (byte)(value | value_mask);
                }

                // Move to the next bit.
                value_mask <<= 1;
            }

            return value;
        }
    }
}
