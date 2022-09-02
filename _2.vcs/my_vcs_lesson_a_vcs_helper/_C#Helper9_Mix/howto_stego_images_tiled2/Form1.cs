using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace howto_stego_images_tiled2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Hide and then recover the image.
        private void btnGo_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;
            int num_bits = (int)nudHiddenBits.Value;

            // Hide the image3.
            Bitmap combined;
            combined = HideResizedTiledImages(
                (Bitmap)picMainOriginal.Image,
                (Bitmap)picHiddenOriginal1.Image,
                (Bitmap)picHiddenOriginal2.Image,
                (Bitmap)picHiddenOriginal3.Image,
                (Bitmap)picHiddenOriginal4.Image,
                num_bits);
            picCombined.Image = combined;

            // Recover the hidden images.
            Bitmap hidden1, hidden2, hidden3, hidden4;
            RecoverResizedTiledImages(combined, out hidden1,
                out hidden2, out hidden3, out hidden4, num_bits);
            picHiddenRecovered1.Image = hidden1;
            picHiddenRecovered2.Image = hidden2;
            picHiddenRecovered3.Image = hidden3;
            picHiddenRecovered4.Image = hidden4;

            Cursor = Cursors.Default;
        }

        // Hide bm_hidden inside bm_visible and return the result.
        public Bitmap HideImage(Bitmap bm_visible, Bitmap bm_hidden, int hidden_bits)
        {
            int shift = (8 - hidden_bits);
            int visible_mask = 0xFF << hidden_bits;
            int hidden_mask = 0xFF >> shift;
            Bitmap bm_combined = new Bitmap(bm_visible.Width, bm_visible.Height);
            for (int x = 0; x < bm_visible.Width; x++)
            {
                for (int y = 0; y < bm_visible.Height; y++)
                {
                    Color clr_visible = bm_visible.GetPixel(x, y);
                    Color clr_hidden = bm_hidden.GetPixel(x, y);
                    int r = (clr_visible.R & visible_mask) + ((clr_hidden.R >> shift) & hidden_mask);
                    int g = (clr_visible.G & visible_mask) + ((clr_hidden.G >> shift) & hidden_mask);
                    int b = (clr_visible.B & visible_mask) + ((clr_hidden.B >> shift) & hidden_mask);
                    bm_combined.SetPixel(x, y, Color.FromArgb(255, r, g, b));
                }
            }
            return bm_combined;
        }

        // Recover a hidden image.
        public Bitmap RecoverImage(Bitmap bm_combined, int hidden_bits)
        {
            int shift = (8 - hidden_bits);
            int hidden_mask = 0xFF >> shift;
            Bitmap bm_hidden = new Bitmap(bm_combined.Width, bm_combined.Height);
            for (int x = 0; x < bm_combined.Width; x++)
            {
                for (int y = 0; y < bm_combined.Height; y++)
                {
                    Color clr_combined = bm_combined.GetPixel(x, y);
                    int r = (clr_combined.R & hidden_mask) << shift;
                    int g = (clr_combined.G & hidden_mask) << shift;
                    int b = (clr_combined.B & hidden_mask) << shift;
                    bm_hidden.SetPixel(x, y, Color.FromArgb(255, r, g, b));
                }
            }
            return bm_hidden;
        }

        // Hide the four hidden images inside bm_visible and return the result.
        public Bitmap HideTiledImages(Bitmap bm_visible,
            Bitmap hidden1, Bitmap hidden2, Bitmap hidden3,
            Bitmap hidden4, int hidden_bits)
        {
            // Tile the hidden images onto a
            // bitmap sized to fit the visible image.
            Bitmap bm = (Bitmap)bm_visible.Clone();
            int wid = bm.Width / 2;
            int hgt = bm.Height / 2;

            using (Graphics gr = Graphics.FromImage(bm))
            {
                Rectangle rect = new Rectangle(0, 0, wid, hgt);
                gr.DrawImage(hidden1, rect);

                rect.X += wid;
                gr.DrawImage(hidden2, rect);

                rect.X = 0;
                rect.Y += hgt;
                gr.DrawImage(hidden3, rect);

                rect.X += wid;
                gr.DrawImage(hidden4, rect);
            }

            // Hide the combined image in the main image.
            return HideImage(bm_visible, bm, hidden_bits);
        }

        // Recover four hidden images.
        public void RecoverTiledImages(Bitmap bm_combined,
            out Bitmap hidden1, out Bitmap hidden2,
            out Bitmap hidden3, out Bitmap hidden4, int hidden_bits)
        {
            // Recover the tiled image.
            Bitmap bm = RecoverImage(bm_combined, hidden_bits);

            // Pull out the pieces.
            int wid = bm_combined.Width / 2;
            int hgt = bm_combined.Height / 2;
            Rectangle dest = new Rectangle(0, 0, wid, hgt);

            Rectangle source = new Rectangle(0, 0, wid, hgt);
            hidden1 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden1))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X += wid;
            hidden2 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden2))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X = 0;
            source.Y += hgt;
            hidden3 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden3))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }

            source.X += wid;
            hidden4 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden4))
            {
                gr.DrawImage(bm, dest, source, GraphicsUnit.Pixel);
            }
        }

        // Hide the four hidden images inside bm_visible and return the result.
        public Bitmap HideResizedTiledImages(Bitmap bm_visible,
            Bitmap hidden1, Bitmap hidden2, Bitmap hidden3,
            Bitmap hidden4, int hidden_bits)
        {
            // Resize the hidden images to fit.
            int wid = bm_visible.Width / 2;
            int hgt = bm_visible.Height / 2;
            Rectangle dest = new Rectangle(0, 0, wid, hgt);

            Bitmap bm1 = new Bitmap(wid, hgt);
            Rectangle source = new Rectangle(0, 0,
                hidden1.Width, hidden1.Height);
            using (Graphics gr = Graphics.FromImage(bm1))
            {
                gr.DrawImage(hidden1, dest, source, GraphicsUnit.Pixel);
            }

            Bitmap bm2 = new Bitmap(wid, hgt);
            source = new Rectangle(0, 0,
                hidden2.Width, hidden2.Height);
            using (Graphics gr = Graphics.FromImage(bm2))
            {
                gr.DrawImage(hidden2, dest, source, GraphicsUnit.Pixel);
            }

            Bitmap bm3 = new Bitmap(wid, hgt);
            source = new Rectangle(0, 0,
                hidden3.Width, hidden3.Height);
            using (Graphics gr = Graphics.FromImage(bm3))
            {
                gr.DrawImage(hidden3, dest, source, GraphicsUnit.Pixel);
            }

            Bitmap bm4 = new Bitmap(wid, hgt);
            source = new Rectangle(0, 0,
                hidden4.Width, hidden4.Height);
            using (Graphics gr = Graphics.FromImage(bm4))
            {
                gr.DrawImage(hidden4, dest, source, GraphicsUnit.Pixel);
            }

            // Hide the resized images.
            Bitmap combined = HideTiledImages(bm_visible,
                bm1, bm2, bm3, bm4, hidden_bits);

            // Hide the sizes of the original images in the result.
            int[] sizes =
            {
                hidden1.Width, hidden1.Height,
                hidden2.Width, hidden2.Height,
                hidden3.Width, hidden3.Height,
                hidden4.Width, hidden4.Height,
            };
            byte[] bytes = IntArrayToByteArray(sizes);
            int x = 0, y = 0;
            EncodeBytes(ref x, ref y, combined, bytes);

            return combined;
        }

        // Convert an int[] into a byte[].
        private byte[] IntArrayToByteArray(int[] ints)
        {
            byte[] result = new byte[ints.Length * sizeof(int)];
            Buffer.BlockCopy(ints, 0, result, 0, result.Length);
            return result;
        }

        // Convert a byte[] into an int[].
        private int[] ByteArrayToIntArray(byte[] bytes)
        {
            int[] result = new int[bytes.Length / sizeof(int)];
            Buffer.BlockCopy(bytes, 0, result, 0, bytes.Length);
            return result;
        }

        // Recover four resized tiled images.
        public void RecoverResizedTiledImages(Bitmap bm_combined,
            out Bitmap hidden1, out Bitmap hidden2,
            out Bitmap hidden3, out Bitmap hidden4, int hidden_bits)
        {
            // Get the image sizes.
            int x = 0, y = 0;
            byte[] bytes = DecodeBytes(ref x, ref y,
                4 * 2 * sizeof(int), bm_combined);
            int[] sizes = ByteArrayToIntArray(bytes);

            // Recover the resized tiled images.
            Bitmap bm1, bm2, bm3, bm4;
            RecoverTiledImages(bm_combined, out bm1,
                out bm2, out bm3, out bm4, hidden_bits);

            // Restore the images' original sizes.
            Rectangle dest;
            int wid = bm_combined.Width / 2;
            int hgt = bm_combined.Height / 2;
            Rectangle source = new Rectangle(0, 0, wid, hgt);
            int index = 0;

            wid = sizes[index++];
            hgt = sizes[index++];
            dest = new Rectangle(0, 0, wid, hgt);
            hidden1 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden1))
            {
                gr.DrawImage(bm1, dest, source, GraphicsUnit.Pixel);
            }

            wid = sizes[index++];
            hgt = sizes[index++];
            dest = new Rectangle(0, 0, wid, hgt);
            hidden2 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden2))
            {
                gr.DrawImage(bm2, dest, source, GraphicsUnit.Pixel);
            }

            wid = sizes[index++];
            hgt = sizes[index++];
            dest = new Rectangle(0, 0, wid, hgt);
            hidden3 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden3))
            {
                gr.DrawImage(bm3, dest, source, GraphicsUnit.Pixel);
            }

            wid = sizes[index++];
            hgt = sizes[index++];
            dest = new Rectangle(0, 0, wid, hgt);
            hidden4 = new Bitmap(wid, hgt);
            using (Graphics gr = Graphics.FromImage(hidden4))
            {
                gr.DrawImage(bm4, dest, source, GraphicsUnit.Pixel);
            }
        }

        // Encode the message in the bitmap's bytes.
        private Bitmap EncodeMesssage(Bitmap bm, string message)
        {
            // Get the message as an array of bytes.
            byte[] message_bytes = System.Text.Encoding.UTF8.GetBytes(message);

            // Encode the bytes.
            return EncodeMesssageBytes(bm, message_bytes);
        }

        // Encode an array of bytes in the bitmap's bytes.
        private Bitmap EncodeMesssageBytes(Bitmap bm, byte[] message_bytes)
        {
            // Make sure it will fit.
            int message_length = message_bytes.Length;
            int space_available = bm.Width * bm.Height;
            if (message_length + 4 > space_available)
                throw new InvalidDataException(
                    "Message length " + message_bytes.Length +
                    " is too long. This image can hold only " +
                    space_available + " bytes.");

            int total_length = message_length + 4;

            // Make the result Bitmap.
            Bitmap result = bm.Clone() as Bitmap;

            // Records the location of the next pixel.
            int x = 0, y = 0;

            // Encode the message's length.
            byte[] length_bytes = BitConverter.GetBytes(message_length);
            EncodeBytes(ref x, ref y, result, length_bytes);

            // Encode the message.
            EncodeBytes(ref x, ref y, result, message_bytes);

            // Return the result.
            return result;
        }

        // Encode the bytes starting at pixel (row, col).
        private void EncodeBytes(ref int x, ref int y, Bitmap bm, byte[] bytes)
        {
            // Encode the bytes.
            for (int i = 0; i < bytes.Length; i++)
                EncodeByte(ref x, ref y, bm, bytes[i]);
        }

        // Encode a single byte at pixel (row, col).
        private void EncodeByte(ref int x, ref int y, Bitmap bm, byte b)
        {
            // Encode the byte's bits 3 at a time.
            EncodeBits(ref x, ref y, bm, b, 0, 1, 2, 3, 0);
            EncodeBits(ref x, ref y, bm, b, 4, 5, 6, 7, 1);
        }

        // Encode four bits. Values pos1 through pos4 give the
        // positions from the left of the bits in b to encode.
        // Value dest_bit gives the bit in the pixel that should
        // hold the values. It should be 0 or 1.
        private void EncodeBits(ref int x, ref int y, Bitmap bm,
            byte b, int pos1, int pos2, int pos3, int pos4, int dest_bit)
        {
            // Get the pixel's color.
            Color color = bm.GetPixel(x, y);

            // A mask to set the bit we are setting.
            byte only_1 = (byte)(0x01 << dest_bit);

            // A mask to clear all bits except the bit we're setting.
            byte clear_1 = (byte)(only_1 ^ 0xFF);

            // Add the bits to the color components.
            byte alpha, red, green, blue;
            pos1 -= dest_bit;
            byte bit1 = (byte)((b >> pos1) & only_1);
            alpha = (byte)((color.A & clear_1) | bit1);

            pos2 -= dest_bit;
            byte bit2 = (byte)((b >> pos2) & only_1);
            red = (byte)((color.R & clear_1) | bit2);

            pos3 -= dest_bit;
            byte bit3 = (byte)((b >> pos3) & only_1);
            green = (byte)((color.G & clear_1) | bit3);

            pos4 -= dest_bit;
            byte bit4 = (byte)((b >> pos4) & only_1);
            blue = (byte)((color.B & clear_1) | bit4);

            // Update the pixel.
            bm.SetPixel(x, y, Color.FromArgb(alpha, red, green, blue));

            // Move to the next pixel.
            if (dest_bit == 1) NextRowCol(ref x, ref y, bm);
        }

        // Increment row and col to the next pixel in the image.
        private void NextRowCol(ref int x, ref int y, Bitmap bm)
        {
            x++;
            if (x >= bm.Width)
            {
                x = 0;
                y++;
            }
        }

        // Decode the message in the bitmap.
        private string DecodeMesssage(Bitmap bm)
        {
            // Get the message bytes.
            byte[] message_bytes = DecodeMesssageBytes(bm);
            string result = System.Text.Encoding.UTF8.GetString(message_bytes);
            return result;
        }

        // Decode the message in the bitmap.
        private byte[] DecodeMesssageBytes(Bitmap bm)
        {
            // Decode the message's length.
            const int int_len = 4;
            int x = 0, y = 0;
            byte[] length_bytes = DecodeBytes(ref x, ref y, int_len, bm);
            int message_length = BitConverter.ToInt32(length_bytes, 0);

            // Get the message bytes.
            byte[] message_bytes = DecodeBytes(ref x, ref y, message_length, bm);
            return message_bytes;
        }

        // Decode the indicated number of bytes from the image.
        private byte[] DecodeBytes(ref int x, ref int y, int num_bytes, Bitmap bm)
        {
            byte[] bytes = new byte[num_bytes];
            for (int i = 0; i < num_bytes; i++)
                bytes[i] = DecodeByte(ref x, ref y, bm);
            return bytes;
        }

        // Decode a single byte starting at pixel (row, col).
        private byte DecodeByte(ref int x, ref int y, Bitmap bm)
        {
            // Decode the byte's bits 3 at a time.
            byte b = 0;
            DecodeBits(ref x, ref y, bm, ref b, 0, 1, 2, 3, 0);
            DecodeBits(ref x, ref y, bm, ref b, 4, 5, 6, 7, 1);
            return b;
        }

        // Decode four bits. Values pos1, pos2, and pos3 give the
        // positions from the left of the bits in b to decode.
        // Value dest_bit gives the bit in the pixel that should
        // hold the values. It should be 0 or 1.
        private void DecodeBits(ref int x, ref int y, Bitmap bm,
            ref byte b, int pos1, int pos2, int pos3, int pos4, int dest_bit)
        {
            // Get the pixel's color.
            Color color = bm.GetPixel(x, y);

            // A mask to get the bit we're using.
            byte only_1 = (byte)(0x01 << dest_bit);

            // Get the encoded bits from the color components.
            byte bit1 = (byte)(color.A & only_1);
            pos1 -= dest_bit;
            b |= (byte)(bit1 << pos1);

            byte bit2 = (byte)(color.R & only_1);
            pos2 -= dest_bit;
            b |= (byte)(bit2 << pos2);

            byte bit3 = (byte)(color.G & only_1);
            pos3 -= dest_bit;
            b |= (byte)(bit3 << pos3);

            byte bit4 = (byte)(color.B & only_1);
            pos4 -= dest_bit;
            b |= (byte)(bit4 << pos4);

            // Move to the next pixel.
            if (dest_bit == 1) NextRowCol(ref x, ref y, bm);
        }

        // Return a byte as a string containing 0s and 1s.
        private string ByteToBits(byte b)
        {
            byte mask = 1;
            string result = "";
            for (int i = 0; i < 8; i++)
            {
                if ((b & mask) == 0) result = "0" + result;
                else result = "1" + result;
                mask <<= 1;
            }
            return result;
        }

        // Return a byte array as a string containing 0s and 1s.
        private string BytesToBits(byte[] bytes)
        {
            string result = "";
            for (int i = 0; i < bytes.Length; i++)
            {
                result += ByteToBits(bytes[i]) + " ";
            }
            return result;
        }
    }
}
