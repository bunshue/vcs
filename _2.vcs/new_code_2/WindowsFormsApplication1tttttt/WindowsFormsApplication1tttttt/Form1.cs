using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;     //for RNGCryptoServiceProvider

namespace WindowsFormsApplication1tttttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //使用內建的Random()函數建立亂數資料
        private void button1_Click(object sender, EventArgs e)
        {
            int num_numbers;
            int min;
            int max;

            num_numbers = 20;
            min = 1;
            max = 100;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            Random rand = new Random();
            int[] rand_numbers = new int[num_numbers];
            for (int i = 0; i < num_numbers; i++)
            {
                rand_numbers[i] = rand.Next(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

        }

        //使用RNGCryptoServiceProvider函數建立亂數資料
        private void button2_Click(object sender, EventArgs e)
        {
            int num_numbers;
            int min;
            int max;

            num_numbers = 20;
            min = 1;
            max = 100;

            richTextBox1.Text += "num_numbers = " + num_numbers.ToString() + "\n";
            richTextBox1.Text += "min = " + min.ToString() + "\n";
            richTextBox1.Text += "max = " + max.ToString() + "\n";

            Random rand = new Random();
            int[] rand_numbers = new int[num_numbers];
            for (int i = 0; i < num_numbers; i++)
            {
                //rand_numbers[i] = rand.Next(min, max);    old
                rand_numbers[i] = RandomInteger(min, max);
                richTextBox1.Text += rand_numbers[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

        }

        // The random number provider.
        private RNGCryptoServiceProvider Rand = new RNGCryptoServiceProvider();

        // Return a random integer between a min and max value.
        private int RandomInteger(int min, int max)
        {
            uint scale = uint.MaxValue;
            while (scale == uint.MaxValue)
            {
                // Get four random bytes.
                byte[] four_bytes = new byte[4];
                Rand.GetBytes(four_bytes);

                // Convert that into an uint.
                scale = BitConverter.ToUInt32(four_bytes, 0);
            }

            // Add min to the scaled difference between max and min.
            return (int)(min + (max - min) * (scale / (double)uint.MaxValue));
        }

    }
}
