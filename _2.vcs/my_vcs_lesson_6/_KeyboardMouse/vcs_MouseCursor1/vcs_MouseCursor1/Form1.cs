using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Reflection;

namespace vcs_MouseCursor1
{
    public partial class Form1 : Form
    {
        private const int Wid = 75;
        private const int Hgt = 70;
        private const int BmWid = 32;

        public Form1()
        {
            InitializeComponent();
        }

        // Display samples of the cursors.
        private void Form1_Load(object sender, EventArgs e)
        {
            //this.Cursor = Cursors.WaitCursor;

            ShowCursor("AppStarting", Cursors.AppStarting);
            ShowCursor("Arrow", Cursors.Arrow);
            ShowCursor("Cross", Cursors.Cross);
            ShowCursor("Default", Cursors.Default);
            ShowCursor("Hand", Cursors.Hand);
            ShowCursor("Help", Cursors.Help);
            ShowCursor("HSplit", Cursors.HSplit);
            ShowCursor("IBeam", Cursors.IBeam);
            ShowCursor("No", Cursors.No);
            ShowCursor("NoMove2D", Cursors.NoMove2D);
            ShowCursor("NoMoveHoriz", Cursors.NoMoveHoriz);
            ShowCursor("NoMoveVert", Cursors.NoMoveVert);
            ShowCursor("PanEast", Cursors.PanEast);
            ShowCursor("PanNE", Cursors.PanNE);
            ShowCursor("PanNorth", Cursors.PanNorth);
            ShowCursor("PanNorth", Cursors.PanNW);
            ShowCursor("PanSE", Cursors.PanSE);
            ShowCursor("PanSouth", Cursors.PanSouth);
            ShowCursor("PanSW", Cursors.PanSW);
            ShowCursor("PanWest", Cursors.PanWest);
            ShowCursor("SizeAll", Cursors.SizeAll);
            ShowCursor("SizeNESW", Cursors.SizeNESW);
            ShowCursor("SizeNS", Cursors.SizeNS);
            ShowCursor("SizeNWSE", Cursors.SizeNWSE);
            ShowCursor("SizeWE", Cursors.SizeWE);
            ShowCursor("UpArrow", Cursors.UpArrow);
            ShowCursor("VSplit", Cursors.VSplit);
            ShowCursor("WaitCursor", Cursors.WaitCursor);

        }

        // Display a cursor.
        private void ShowCursor(string cursor_name, Cursor the_cursor)
        {
            // Make a Panel to hold the Label and PictureBox.
            Panel pan = new Panel();
            pan.Size = new Size(Wid, Hgt);
            pan.Cursor = the_cursor;
            flowLayoutPanel1.Controls.Add(pan);

            // Display the cursor's name in a Label.
            Label lbl = new Label();
            lbl.AutoSize = false;
            lbl.Text = cursor_name;
            lbl.Size = new Size(Wid, 13);
            lbl.TextAlign = ContentAlignment.MiddleCenter;
            lbl.Location = new Point(0, 0);
            pan.Controls.Add(lbl);

            // Draw the cursor onto a Bitmap.
            Bitmap bm = new Bitmap(BmWid, BmWid);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                the_cursor.Draw(gr, new Rectangle(0, 0, BmWid, BmWid));
            }

            // Display the Bitmap in a PictureBox.
            PictureBox pic = new PictureBox();
            pic.Location = new Point((Wid - BmWid) / 2, 15);
            pic.BorderStyle = BorderStyle.Fixed3D;
            pic.ClientSize = new Size(BmWid, BmWid);
            pic.Image = bm;
            pan.Controls.Add(pic);
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            switch ((int)numericUpDown1.Value)
            {
                case 0: this.Cursor = Cursors.Default; lb_cursor.Text = "Default : 取得預設游標，通常為箭號游標。"; break;
                case 1: this.Cursor = Cursors.Arrow; lb_cursor.Text = "Arrow : 取得箭號游標。"; break;
                case 2: this.Cursor = Cursors.AppStarting; lb_cursor.Text = "AppStarting : 取得應用程式啟動時出現的游標。"; break;
                case 3: this.Cursor = Cursors.Cross; lb_cursor.Text = "Cross : 取得十字型游標。"; break;
                case 4: this.Cursor = Cursors.Hand; lb_cursor.Text = "Hand : 取得手狀游標，通常在游標停留在 Web 連結上方時使用。"; break;
                case 5: this.Cursor = Cursors.Help; lb_cursor.Text = "Help : 取得由箭號和問號組成的說明游標"; break;
                case 6: this.Cursor = Cursors.HSplit; lb_cursor.Text = "HSplit : 取得當滑鼠位在水平分割列上時出現的游標"; break;
                case 7: this.Cursor = Cursors.IBeam; lb_cursor.Text = "IBeam : 取得 I 型游標，這個游標用來顯示當按一下滑鼠時文字游標出現的位置。"; break;
                case 8: this.Cursor = Cursors.No; lb_cursor.Text = "No : 取得指示目前作業的特定區域無效的游標"; break;
                case 9: this.Cursor = Cursors.NoMove2D; lb_cursor.Text = "NoMove2D : 取得當滑鼠不移動，但視窗可以水平和垂直方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 10: this.Cursor = Cursors.NoMoveHoriz; lb_cursor.Text = "NoMoveHoriz : 取得當滑鼠不移動，但視窗可以水平方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 11: this.Cursor = Cursors.NoMoveVert; lb_cursor.Text = "NoMoveVert : 取得當滑鼠不移動，但視窗可以垂直方向捲動時，滑鼠滾輪作業期間出現的游標。"; break;
                case 12: this.Cursor = Cursors.PanEast; lb_cursor.Text = "PanEast : 取得當滑鼠移動，而且視窗可水平捲動至右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 13: this.Cursor = Cursors.PanNE; lb_cursor.Text = "PanNE : 取得當滑鼠移動，而且視窗可水平和垂直捲動至上方和右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 14: this.Cursor = Cursors.PanNorth; lb_cursor.Text = "PanNorth : 取得當滑鼠移動，而且視窗可垂直捲動至上方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 15: this.Cursor = Cursors.PanNW; lb_cursor.Text = "PanNW : 取得當滑鼠移動，而且視窗可水平和垂直捲動至上方和左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 16: this.Cursor = Cursors.PanSE; lb_cursor.Text = "PanSE : 取得當滑鼠移動，而且視窗可水平和垂直捲動至下方和右方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 17: this.Cursor = Cursors.PanSouth; lb_cursor.Text = "PanSouth : 取得當滑鼠移動，而且視窗可垂直捲動至下方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 18: this.Cursor = Cursors.PanSW; lb_cursor.Text = "PanSW : 取得當滑鼠移動，而且視窗可水平和垂直捲動至下方和左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 19: this.Cursor = Cursors.PanWest; lb_cursor.Text = "PanWest : 取得當滑鼠移動而且視窗可水平捲動至左方時，滑鼠滾輪作業期間出現的游標。"; break;
                case 20: this.Cursor = Cursors.SizeAll; lb_cursor.Text = "SizeAll : 取得四頭調整大小游標，它是由四個連結的箭號 (分別指向北、南、東和西) 所組成。"; break;
                case 21: this.Cursor = Cursors.SizeNESW; lb_cursor.Text = "SizeNESW : 取得雙頭斜線 (東北/西南) 調整大小游標。"; break;
                case 22: this.Cursor = Cursors.SizeNS; lb_cursor.Text = "SizeNS : 取得雙頭垂直 (北/南) 調整大小游標。"; break;
                case 23: this.Cursor = Cursors.SizeNWSE; lb_cursor.Text = "SizeNWSE : 取得雙頭斜線 (西北/東南) 調整大小游標。"; break;
                case 24: this.Cursor = Cursors.SizeWE; lb_cursor.Text = "SizeWE : 取得雙頭水平 (西/東) 調整大小游標。"; break;
                case 25: this.Cursor = Cursors.UpArrow; lb_cursor.Text = "UpArrow : 取得向上箭號游標，通常用來辨認插入點。"; break;
                case 26: this.Cursor = Cursors.VSplit; lb_cursor.Text = "VSplit : 取得當滑鼠位在垂直分割列上方時出現的游標。"; break;
                case 27: this.Cursor = Cursors.WaitCursor; lb_cursor.Text = "WaitCursor : 取得等待游標，其形狀通常為沙漏形狀。"; break;
                default: this.Cursor = Cursors.Default; lb_cursor.Text = "XXXXXXXXXXX"; break;
            }
        }


    }
}
