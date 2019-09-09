using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DragPicture1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //製作拖曳元件
        //定義一些全域變數幫助拖曳時計算元件位置
        #region 移動元件時相關變數
        private int _ControlPositionX, _ControlPositionY;   //元件初始位置
        private int _CursorInitialX = 0, _CursorInitialY = 0;   //滑鼠拖曳初始位置
        private bool _isMoveState = false;  //移動狀態
        #endregion

        #region MouseDown記錄滑鼠與元件位置
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (!_isMoveState)   //假如非移動狀態
            {
                _ControlPositionX = ((PictureBox)sender).Left;  //記錄視窗初始X
                _ControlPositionY = ((PictureBox)sender).Top;  //記錄視窗初始Y
                _CursorInitialX = Cursor.Position.X;    //記錄滑鼠初始X
                _CursorInitialY = Cursor.Position.Y;    //記錄滑鼠初始Y
                _isMoveState = true;    //設定為移動狀態
            }
        }
        #endregion

        #region MouseMove移動元件運算
        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (_isMoveState)    //若為移動狀態
            {
                int tX = Cursor.Position.X; //暫存目前滑鼠位置X
                int tY = Cursor.Position.Y; //暫存目前滑鼠位置Y
                // 舊視窗位置 + 滑鼠移動距離 = 新位置
                ((PictureBox)sender).Left = _ControlPositionX + (tX - _CursorInitialX); //設定視窗新位置 X
                ((PictureBox)sender).Top = _ControlPositionY + (tY - _CursorInitialY); //設定視窗新位置 Y
            }
        }
        #endregion

        #region MouseUp結束移動元件
        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            //設定非拖曳狀態
            _isMoveState = false;
        }
        #endregion
    }
}
