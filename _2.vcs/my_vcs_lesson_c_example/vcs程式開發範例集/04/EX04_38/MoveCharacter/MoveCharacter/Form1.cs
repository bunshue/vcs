using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace MoveCharacter
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        Point CPoint;//記錄滑鼠游標在父容器中的初始位置
        bool isDown = false;//判斷是否可以移動文字
        int tem_x = 0;//記錄滑鼠游標移動文字後的X位置
        int tem_y = 0;//記錄滑鼠游標移動文字後的Y位置

        private void label1_MouseDown(object sender, MouseEventArgs e)
        {
            CPoint = new Point(e.X, e.Y);//取得滑鼠游標在文字上按下時的位置
            tem_x = e.X;//記錄X座標
            tem_y = e.Y;//記錄X座標
            isDown = true;//文字可能移動
        }

        private void label1_MouseMove(object sender, MouseEventArgs e)
        {
            bool tem_b = false;//判斷是否超出邊界
            if (e.Button == MouseButtons.Left && isDown == true)//如果目前按下的是滑鼠游標左鍵，而且文字可以移動
            {
                //如果文字在移動範圍內
                if (label1.Left <= 0 || label1.Top <= 0 || label1.Left >= (panel1.Width - label1.Width) || label1.Top >= (panel1.Height - label1.Height))
                {
                    if (label1.Left <= 0)//如果文字超出左邊界
                        if (e.X > tem_x)//如果文字還向右移動
                            tem_b = true;//文字移動
                    if (label1.Top <= 0)//如果文字超出上邊界
                        if (e.Y > tem_y)//如果文字還向下移動
                            tem_b = true;//文字移動
                    if (label1.Left >= (panel1.Width - label1.Width))//如果文字超出右邊界
                        if (e.X < tem_x)//如果文字還向左移動
                            tem_b = true;//文字移動
                    if (label1.Top >= (panel1.Height - label1.Height))//如果文字超出下邊界
                        if (e.Y < tem_y)//如果文字還向上移動
                            tem_b = true;//文字移動
                    if (tem_b == false)//如果文字超出邊界
                        return;//退出本次操作
                }
                Point myPosittion = new Point(label1.Left + e.X - CPoint.X, label1.Top + e.Y - CPoint.Y);//移動Label控制元件
                label1.Location = myPosittion;//設定目前控制元件在視窗容器上的位置
            }
            tem_x = e.X;//記錄移動後的X位置
            tem_y = e.Y;//記錄移動後的Y位置
        }
    }
}
