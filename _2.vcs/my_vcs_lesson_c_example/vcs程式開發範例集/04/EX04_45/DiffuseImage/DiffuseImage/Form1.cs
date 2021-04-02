using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DiffuseImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void DiffuseEffect(string Str, Panel panel)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);//根據字串實例化Bitmap類
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, panel.Width, panel.Height);//根據大小實例化Bitmap類
            int Var_W = Var_Bitmap.Width; //圖片寬度 
            int Var_H = Var_Bitmap.Height; //圖片高度 
            Graphics g = panel.CreateGraphics();//取得Graphics對像 
            g.Clear(panel.BackColor); //初始為全灰色 
            for (int i = 0; i <= Var_W / 2; i++)
            {
                //取得高和寬的比例
                int j = Convert.ToInt32(i * (Convert.ToSingle(Var_H) / Convert.ToSingle(Var_W)));
                //設定縮小後圖片的大小
                Rectangle Var_D_Rect = new Rectangle(Var_W / 2 - i, Var_H / 2 - j, 2 * i, 2 * j);
                //取得原圖片大小
                Rectangle Var_S_Rect = new Rectangle(0, 0, Var_Bitmap.Width, Var_Bitmap.Height);
                g.DrawImage(Var_Bitmap, Var_D_Rect, Var_S_Rect, GraphicsUnit.Pixel);//按照指定的大小繪製原圖片
                System.Threading.Thread.Sleep(10);//線程序掛掉
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length > 0)//如果選擇了圖片
                DiffuseEffect(textBox1.Text.Trim(), panel1);//呼叫自定義方法完成圖片向四周的擴充
            else
                MessageBox.Show("請選擇圖片路徑。");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "*.bmp|*.BMP";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                textBox1.Text = openFileDialog1.FileName;
        }
    }
}
