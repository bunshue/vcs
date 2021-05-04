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

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 將 KnownColor 列舉的內容項目複雜到 allColors 陣列
            Array colorsArray = Enum.GetValues(typeof(KnownColor));
            KnownColor[] allColors = new KnownColor[colorsArray.Length];
            Array.Copy(colorsArray, allColors, colorsArray.Length);

            // Loop through printing out the values' names in the colors 
            // they represent.
            float y = -20;
            float x = 0;

            for (int i = 0; i < allColors.Length; i++)
            {
                // 一排 25 個
                if (i > 0 && i % 25 == 0)
                {
                    x += 150.0f;
                    y = 0.0f;
                }
                else
                {
                    // 在該排中 往下列出
                    y += 20.0F;
                }

                // 產生該顏色的塗刷
                SolidBrush aBrush =
                    new SolidBrush(Color.FromName(allColors[i].ToString()));
                e.Graphics.DrawString(allColors[i].ToString(),
                    this.Font, aBrush, x, y);

                // 釋放該塗刷
                aBrush.Dispose();
            }
        }
    }
}