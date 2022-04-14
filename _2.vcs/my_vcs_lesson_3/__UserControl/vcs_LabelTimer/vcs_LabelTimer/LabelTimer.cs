using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_LabelTimer
{
    public partial class LabelTimer : UserControl
    {
        public LabelTimer()
        {
            InitializeComponent();
        }

        private void LabelTimer_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        //顯示在控件屬性的項目 : USER_size_width USER_size_height USER_use_24hr USER_Font USER_Color_Foreground USER_Color_Background

        private int size_width = 300;
        [
        Category("Alignment"),
        Description("控制項寬度")
        ]
        public int USER_size_width
        {
            get
            {
                return size_width;
            }
            set
            {
                size_width = value;
                Invalidate();
            }
        }

        private int size_height = 100;
        [
        Category("Alignment"),
        Description("控制項高度")
        ]
        public int USER_size_height
        {
            get
            {
                return size_height;
            }
            set
            {
                size_height = value;
                Invalidate();
            }
        }

        public enum USE24HR
        {
            NO = 0,
            YES = 1,
        }

        private USE24HR flag_use_24_hr = USE24HR.YES;
        [
        Category("Alignment"),
        Description("使用12小時制 或是 使用24小時制")
        ]
        public USE24HR USER_use_24hr
        {
            get
            {
                return flag_use_24_hr;
            }
            set
            {
                flag_use_24_hr = value;
                Invalidate();
            }
        }

        private Font use_font = new Font("標楷體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
        [
        Category("Alignment"),
        Description("用來顯示控制項文字的字型。")
        ]
        public Font USER_Font
        {
            get
            {
                return use_font;
            }
            set
            {
                use_font = value;
                Invalidate();
            }
        }

        private Color Color_foreground = Color.Black;
        [
        Category("Alignment"),
        Description("用來顯示文字之元件的前景色彩。")
        ]
        public Color USER_Color_Foreground
        {
            get
            {
                return Color_foreground;
            }
            set
            {
                Color_foreground = value;
                Invalidate();
            }
        }

        private Color Color_background = Color.Pink;
        [
        Category("Alignment"),
        Description("元件的背景色彩。")
        ]
        public Color USER_Color_Background
        {

            get
            {
                return Color_background;
            }
            set
            {
                Color_background = value;
                Invalidate();
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            this.Size = new Size(size_width, size_height);

            e.Graphics.Clear(Color_background);
            e.Graphics.DrawString(
                Text + DateTime.Now.ToString(),
                Font,
                new SolidBrush(Color_foreground),
                ClientRectangle);

            //g.DrawString("顯示豎排文字", new Font("標楷體", 20), new SolidBrush(Color.Black), 0, 0);
        }
    }
}


