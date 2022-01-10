using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Windows.Forms;
using System.Drawing;

namespace WindowsFormsApplication1216a
{
    public class TransparentPanel : Control
    {
        public TransparentPanel() { }

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            //不進行背景的繪制
        }

        protected override CreateParams CreateParams
        {
            get
            {
                CreateParams cp = base.CreateParams;
                cp.ExStyle |= 0x00000020; //WS_EX_TRANSPARENT
                return cp;
            }
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 0, 0, this.Width - 1, this.Height - 1);

            e.Graphics.FillRectangle(Brushes.Lime, 0, 0, m_value * this.Width / (m_MaxValue - m_MinValue), this.Height - 1);

            e.Graphics.DrawString(m_value.ToString(), new Font("標楷體", 30), new SolidBrush(Color.Blue), new PointF(0, 20));

        }

        //為控件添加自定義屬性值
        private Boolean drawGaugeBackground = true;
        private Single m_value;
        private Single m_MaxValue = 100;
        private Single m_MinValue = 0;
        [System.ComponentModel.Browsable(true), System.ComponentModel.Category("自定義屬性欄"), System.ComponentModel.Description("說明信息 : The value.")]
        public Single Value
        {
            get
            {
                return m_value;
            }
            set
            {
                if (m_value != value)
                {
                    m_value = Math.Min(Math.Max(value, m_MinValue), m_MaxValue);

                    if (this.DesignMode)
                    {
                        drawGaugeBackground = true;
                    }


                    /*
                    for (Int32 counter = 0; counter < NUMOFRANGES - 1; counter++)
                    {
                        if ((m_RangeStartValue[counter] <= m_value)
                        && (m_value <= m_RangeEndValue[counter])
                        && (m_RangeEnabled[counter]))
                        {
                            if (!m_valueIsInRange[counter])
                            {
                                if (ValueInRangeChanged != null)
                                {
                                    ValueInRangeChanged(this, new ValueInRangeChangedEventArgs(counter));
                                }
                            }
                        }
                        else
                        {
                            m_valueIsInRange[counter] = false;
                        }
                    }
                    */
                    Refresh();
                }
            }
        }

        [System.ComponentModel.Browsable(true),
        System.ComponentModel.Category("自定義屬性欄"),
        System.ComponentModel.Description("說明信息 : The minimum value to show on the scale.")]
        public Single MinValue
        {
            get
            {
                return m_MinValue;
            }
            set
            {
                if ((m_MinValue != value)
                && (value < m_MaxValue))
                {
                    m_MinValue = value;
                    drawGaugeBackground = true;
                    Refresh();
                }
            }
        }

        [System.ComponentModel.Browsable(true),
        System.ComponentModel.Category("自定義屬性欄"),
        System.ComponentModel.Description("說明信息 : The maximum value to show on the scale.")]
        public Single MaxValue
        {
            get
            {
                return m_MaxValue;
            }
            set
            {
                if ((m_MaxValue != value)
                && (value > m_MinValue))
                {
                    m_MaxValue = value;
                    drawGaugeBackground = true;
                    Refresh();
                }
            }
        }


        /*
        [System.ComponentModel.Bindable(true),
        System.ComponentModel.Category("自定義屬性欄"),
        System.ComponentModel.DefaultValue(1),
        System.ComponentModel.Description("此處為自定義屬性Attr1的說明信息！")]
        */
    }
}

