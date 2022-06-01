using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;

//移動控件但不改變大小

namespace vcs_test_all_01_Control
{
    public class MoveControl
    {
        #region Constructors
        public MoveControl(Control ctrl)
        {
            currentControl = ctrl;
            AddEvents();
        }
        #endregion

        #region Fields
        private Control currentControl; //傳入的控件
        private Point pPoint; //上個鼠標坐標
        private Point cPoint; //當前鼠標坐標
        FrameControl fc;//邊框控件
        #endregion

        #region Properties

        #endregion

        #region Methods
        /// <summary>
        /// 掛載事件
        /// </summary>
        private void AddEvents()
        {
            currentControl.MouseClick += new MouseEventHandler(MouseClick);
            currentControl.MouseDown += new MouseEventHandler(MouseDown);
            currentControl.MouseMove += new MouseEventHandler(MouseMove);
            currentControl.MouseUp += new MouseEventHandler(MouseUp);
        }

        /// <summary>
        /// 繪制拖拉時的黑色邊框
        /// </summary>
        public static void DrawDragBound(Control ctrl)
        {
            ctrl.Refresh();
            Graphics g = ctrl.CreateGraphics();
            int width = ctrl.Width;
            int height = ctrl.Height;
            Point[] ps = new Point[5]{new Point(0,0),new Point(width -1,0),
                new Point(width -1,height -1),new Point(0,height-1),new Point(0,0)};
            g.DrawLines(new Pen(Color.Black), ps);
        }

        #endregion

        #region Events
        /// <summary>
        /// 鼠標單擊事件：用來顯示邊框
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        protected void MouseClick(object sender, MouseEventArgs e)
        {
            this.currentControl.Parent.Refresh();//刷新父容器，清除掉其他控件的邊框
            this.currentControl.BringToFront();
            fc = new FrameControl(this.currentControl);
            this.currentControl.Parent.Controls.Add(fc);
            fc.Visible = true;
            fc.Draw();
        }

        /// <summary>
        /// 鼠標按下事件：記錄當前鼠標相對窗體的坐標
        /// </summary>
        void MouseDown(object sender, MouseEventArgs e)
        {
            pPoint = Cursor.Position;
        }

        /// <summary>
        /// 鼠標移動事件：讓控件跟著鼠標移動
        /// </summary>
        void MouseMove(object sender, MouseEventArgs e)
        {
            Cursor.Current = Cursors.SizeAll; //當鼠標處于控件內部時，顯示光標樣式為SizeAll
            //當鼠標左鍵按下時才觸發
            if (e.Button == MouseButtons.Left)
            {
                MoveControl.DrawDragBound(this.currentControl);
                if (fc != null) fc.Visible = false; //先隱藏
                cPoint = Cursor.Position;//獲得當前鼠標位置
                int x = cPoint.X - pPoint.X;
                int y = cPoint.Y - pPoint.Y;
                currentControl.Location = new Point(currentControl.Location.X + x, currentControl.Location.Y + y);
                pPoint = cPoint;
            }
        }

        /// <summary>
        /// 鼠標彈起事件：讓自定義的邊框出現
        /// </summary>
        void MouseUp(object sender, MouseEventArgs e)
        {
            this.currentControl.Refresh();
            if (fc != null)
            {
                fc.Visible = true;
                fc.Draw();
            }
        }
        #endregion
    }
}