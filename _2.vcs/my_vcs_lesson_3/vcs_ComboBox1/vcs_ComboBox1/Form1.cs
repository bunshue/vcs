using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ComboBox1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Add colors and pictures to the ComboBoxes.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Colors.
            Color[] colors =
            {
                Color.Red,
                Color.Orange,
                Color.Yellow,
                Color.Green,
                Color.Blue,
                Color.Indigo,
                Color.Purple,
            };
            cboColor.DisplayColorSamples(colors);
            cboColor.SelectedIndex = 0;

            // Faces.
            Image[] images = 
            {
                Properties.Resources.face1,
                Properties.Resources.face2,
                Properties.Resources.face3,
                Properties.Resources.face4,
            };
            cboFace.DisplayImages(images);
            cboFace.SelectedIndex = 0;
            cboFace.DropDownHeight = 200;


            //從陣列抓資料到combobox清單內
            Cursor[] cursorList = new Cursor[] {  // 系統內建的全部滑鼠游標圖形 
                                                   Cursors.AppStarting, Cursors.Arrow, Cursors.Cross,
                                                   Cursors.Default, Cursors.Hand, Cursors.Help,
                                                   Cursors.HSplit, Cursors.IBeam, Cursors.No,
                                                   Cursors.NoMove2D, Cursors.NoMoveHoriz, Cursors.NoMoveVert,
                                                   Cursors.PanEast, Cursors.PanNE, Cursors.PanNorth,
                                                   Cursors.PanNW, Cursors.PanSE, Cursors.PanSouth,
                                                   Cursors.PanSW, Cursors.PanWest, Cursors.SizeAll,
                                                   Cursors.SizeNESW, Cursors.SizeNS, Cursors.SizeNWSE,
                                                   Cursors.SizeWE, Cursors.UpArrow, Cursors.VSplit, Cursors.WaitCursor};


            foreach (Cursor cursor in cursorList)
            {
                comboBox1.Items.Add(cursor);  // 加入到 comboBox1 清單內
            }
        }
    }
}
