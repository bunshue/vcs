using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace CircumgyrateImage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void CircumgyrateEffect(string Str, Panel panel)
        {
            Bitmap tem_Bitmap = new Bitmap(Str);//透過字串實例化Bitmap類
            Bitmap Var_Bitmap = new Bitmap(tem_Bitmap, panel.Width, panel.Height);//透過panel按件的大小實例化Bitmap類
            
            Graphics g = panel.CreateGraphics();//實例化panel控制元件的Graphics類
            float Var_Angle = 0;//設定圖片的旋轉角度
            while (Var_Angle <= 360)//使圖片旋轉360度
            {
                TextureBrush Var_Brush = new TextureBrush(Var_Bitmap);//實例化TextureBrush類
                panel.Refresh();//使工作區無效
                Var_Brush.RotateTransform(Var_Angle);//以指定角度旋轉圖片
                //繪製旋轉後的圖片
                g.FillRectangle(Var_Brush, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height);
                Var_Angle += 2f;//增加旋轉的角度
                System.Threading.Thread.Sleep(30);//掛掉目前線程
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "*.bmp|*.BMP";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                textBox1.Text = openFileDialog1.FileName;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text.Length > 0)//如果有圖片路徑
                CircumgyrateEffect(textBox1.Text.Trim(), panel1);//呼叫自定義方法
            else
                MessageBox.Show("請選擇圖片路徑。");
        }
    }
}
