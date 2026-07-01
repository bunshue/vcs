using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//隱寫術 Steganography
//隱寫術就是可以將資訊以明文/密文的方式，隱藏在圖片、文字、音頻或影片等之類的檔案中。

namespace vcs_stego
{
    public partial class Form1 : Form
    {
        // A bitmap to record which pixels are used.
        private Bitmap UsedBitmap;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            do_stego();
        }

        void show_item_location()
        {
            //button
            int W = 305;
            int H = 400;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10;

            //textBox1.Text = "Welcome to the United States.";
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 50);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 50);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 50);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_stego";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void do_stego()
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;

            pictureBox2.Image = EncodeMesssage(pictureBox1.Image as Bitmap, textBox1.Text);

            pictureBox3.Image = UsedBitmap;

            //------------------------------------------------------------  # 60個

            //解碼

            string decoded_string = DecodeMesssage(pictureBox2.Image as Bitmap);
            richTextBox1.Text += "解碼 : " + decoded_string + "\n";
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
            {
                throw new InvalidDataException("Message length " + message_bytes.Length + " is too long. This image can hold only " + space_available + " bytes.");
            }

            int total_length = message_length + 4;
            //lblResult.Text = "Encoded " + total_length.ToString("N0") + " bytes";
            richTextBox1.Text += "共編碼 Encoded " + total_length.ToString("N0") + " bytes\n";

            // Make the result Bitmap.
            Bitmap result = bm.Clone() as Bitmap;
            UsedBitmap = bm.Clone() as Bitmap;

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
            {
                EncodeByte(ref x, ref y, bm, bytes[i]);
            }
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
        private void EncodeBits(ref int x, ref int y, Bitmap bm, byte b, int pos1, int pos2, int pos3, int pos4, int dest_bit)
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
            UsedBitmap.SetPixel(x, y, Color.Red);

            // Move to the next pixel.
            if (dest_bit == 1)
            {
                NextRowCol(ref x, ref y, bm);
            }
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

        //------------------------------------------------------------  # 60個

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
            {
                bytes[i] = DecodeByte(ref x, ref y, bm);
            }
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
        private void DecodeBits(ref int x, ref int y, Bitmap bm, ref byte b, int pos1, int pos2, int pos3, int pos4, int dest_bit)
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
            if (dest_bit == 1)
            {
                NextRowCol(ref x, ref y, bm);
            }
        }

        // Return a byte as a string containing 0s and 1s.
        private string ByteToBits(byte b)
        {
            byte mask = 1;
            string result = "";
            for (int i = 0; i < 8; i++)
            {
                if ((b & mask) == 0)
                {
                    result = "0" + result;
                }
                else
                {
                    result = "1" + result;
                }
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

        //------------------------------------------------------------  # 60個




    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


