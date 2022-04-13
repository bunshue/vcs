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

        public enum USE24HR
        {
            NO = 0,
            YES = 1,
        }

        private USE24HR flag_use_24_hr = USE24HR.YES;
        private Color Color_foreground = Color.Black;
        private Color Color_background = Color.Pink;

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

        // ContentAlignment is an enumeration defined in the System.Drawing
        // namespace that specifies the alignment of content on a drawing
        // surface.
        private ContentAlignment alignmentValue = ContentAlignment.MiddleLeft;

        [
        Category("Alignment"),
        Description("Specifies the alignment of text.")
        ]
        public ContentAlignment TextAlignment
        {

            get
            {
                return alignmentValue;
            }
            set
            {
                alignmentValue = value;

                // The Invalidate method invokes the OnPaint method described
                // in step 3.
                Invalidate();
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            StringFormat style = new StringFormat();
            style.Alignment = StringAlignment.Near;
            switch (alignmentValue)
            {
                case ContentAlignment.MiddleLeft:
                    style.Alignment = StringAlignment.Near;
                    break;
                case ContentAlignment.MiddleRight:
                    style.Alignment = StringAlignment.Far;
                    break;
                case ContentAlignment.MiddleCenter:
                    style.Alignment = StringAlignment.Center;
                    break;
            }

            // Call the DrawString method of the System.Drawing class to write
            // text. Text and ClientRectangle are properties inherited from
            // Control.
            e.Graphics.DrawString(
                Text + DateTime.Now.ToString(),
                Font,
                new SolidBrush(ForeColor),
                ClientRectangle, style);
        }



    }
}
