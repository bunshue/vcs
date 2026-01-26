using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_test_all_08_SetTabs
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            // Set the ListBox tabs.
            SetListBoxTabs(listBox1, new int[] { 120, 170, 220 });
            SetListBoxTabs(listBox1, new int[] { 120, 170, 220 });

            // Set the TextBox tabs.
            SetTextBoxTabs(textBox1, new int[] { 120, 170, 220 });

            // Set the TextBox tabs.
            SetRichTextBoxTabs(richTextBox1, new int[] { 120, 170, 220 });

            // Make some data.
            // Source: http://www.thesupercars.org/fastest-cars/fastest-cars-in-the-world-top-10-list.
            AddData("SSC Ultimate Aero", 257, 1183, 654400);
            AddData("Bugatti Veyron", 253, 1001, 1700000);
            AddData("Saleen S7 Twin-Turbo", 248, 750, 555000);
            AddData("Koenigsegg CCX", 245, 806, 545568);
            AddData("McLaren F1", 240, 637, 970000);
            AddData("Ferrari Enzo", 217, 660, 670000);
            AddData("Jaguar XJ220", 217, 542, 650000);
            AddData("Pagani Zonda F", 215, 650, 667321);
            AddData("Lamborghini Murcielago LP640", 211, 640, 430000);
            AddData("Porsche Carrera GT", 205, 612, 440000);


            /*
            for (int i = 0; i < 10; i++)
            {
                string txt = "";
                txt = i.ToString() + "\t" + (i * i).ToString() + "\t" + (i * i * i).ToString();
                richTextBox1.Text += txt + "\n";

            }
            */
        }

        void show_item_location()
        {
            int W = 600;
            int H = 150;
            int dd = 25;
            int x_st = 10;
            int y_st = 10;
            int dx = W + 10;
            int dy = H + 10 + dd;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            listBox1.Size = new Size(600, 150);
            listBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + dd);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            textBox1.Size = new Size(600, 150);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + dd);

            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            textBox2.Size = new Size(600, 150);
            textBox2.Location = new Point(x_st + dx * 0, y_st + dy * 2 + dd);

            label3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            richTextBox1.Size = new Size(600, 150);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 3 + dd);

            this.Size = new Size(700, 790);
            this.Text = "vcs_test_all_08_SetTabs";
        }

        // Add some data to all three controls.
        private void AddData(string name, int mph, int hp, decimal price)
        {
            // Build a tab-delimited string.
            string txt = name + "\t" + mph.ToString() + " mph\t" +
                hp.ToString() + " hp\t" + price.ToString("C");

            // Display in the ListBox and first TextBox.
            listBox1.Items.Add(txt);
            textBox1.Text += txt + "\r\n";

            richTextBox1.Text += txt + "\r\n";

            // Display formatted.
            textBox2.Text +=
                string.Format("{0,-30}{1,7} mph{2,7} hp{3,15:C}\r\n",
                name, mph, hp, price);

            /*
            richTextBox1.Text +=
                string.Format("{0,-30}{1,7} mph{2,7} hp{3,15:C}\r\n",
                name, mph, hp, price);
            */

        }

        // Set tab stops inside a ListBox.
        private void SetListBoxTabs(ListBox lst, IEnumerable<int> tabs)
        {
            // Make sure the control will use them.
            lst.UseTabStops = true;
            lst.UseCustomTabOffsets = true;

            // Get the control's tab offset collection.
            ListBox.IntegerCollection offsets = listBox1.CustomTabOffsets;

            // Define the tabs.
            foreach (int tab in tabs)
            {
                offsets.Add(tab);
            }
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, Int32 wParam, int[] lParam);
        private const uint EM_SETTABSTOPS = 0xCB;

        // Set tab stops inside a TextBox.
        private void SetTextBoxTabs(TextBox txt, int[] tabs)
        {
            SendMessage(txt.Handle, EM_SETTABSTOPS, tabs.Length, tabs);
        }

        // Set tab stops inside a RichTextBox.
        private void SetRichTextBoxTabs(RichTextBox rtb, int[] tabs)
        {
            SendMessage(rtb.Handle, EM_SETTABSTOPS, tabs.Length, tabs);
        }
    }
}
