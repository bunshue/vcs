using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int[] price;

        private void loadButton_Click(object sender, EventArgs e)
        {
            if (openDialog.ShowDialog() == DialogResult.OK){
                System.IO.StreamReader sr = new System.IO.StreamReader(openDialog.FileName, Encoding.Default);

                menuList.Items.Clear();
                price = new int[int.Parse(sr.ReadLine())];

                for(int i=0; !sr.EndOfStream; ++i){
                    string dish = "";
                    char ch = Convert.ToChar(sr.Read());
                    for (; ch != ','; ch = Convert.ToChar(sr.Read()))
                        dish += ch;
                    menuList.Items.Add(dish);
                    price[i] = int.Parse(sr.ReadLine());
                }
                sr.Close();
            }

        }

        private void menuList_SelectedIndexChanged(object sender, EventArgs e)
        {
            priceText.Text = price[menuList.SelectedIndex].ToString();
        }
    }
}
