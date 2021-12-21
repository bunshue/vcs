using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Text;

namespace vcs_Oscilloscope
{
    public partial class UCOscilloscope : UserControl
    {
        int m_width;
        int m_height;

        float m_yPositionOfNoWafer;
        float m_yPositionOfWafer;

        int m_maxValue;
        int m_lineWidth;

        int m_Ratio;
        Color m_lineColor;

        List<int> m_mappingDatas;

        public int Ratio
        {
            get { return m_Ratio; }
            set { m_Ratio = value; }
        }

        public List<int> MappingDatas
        {
            get { return m_mappingDatas; }
            set
            {
                m_mappingDatas = value;
                this.Invalidate();
            }
        }
        public Color LineColor
        {
            get { return m_lineColor; }
            set { m_lineColor = value; }
        }
        public int MaxValue
        {
            get { return m_maxValue; }
            set { m_maxValue = value; }
        }

        public int LineWidth
        {
            get { return m_lineWidth; }
            set { m_lineWidth = value; }
        }

        public UCOscilloscope()
        {
            InitializeComponent();

            SetStyle(ControlStyles.UserPaint |
                     ControlStyles.DoubleBuffer |
                     ControlStyles.ResizeRedraw |
                     ControlStyles.AllPaintingInWmPaint |
                     ControlStyles.SupportsTransparentBackColor,
                     true);
            m_lineColor = Color.BlueViolet;
            m_lineWidth = 2;
            m_Ratio = 50;
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            if (!Visible || !IsHandleCreated) return;

            // Draw simple text, don't waste time with luxus render:
            e.Graphics.TextRenderingHint = TextRenderingHint.SingleBitPerPixelGridFit;

            CalculateLocals();

            if (MappingDatas != null && MappingDatas.Count > 0)
            {
                DrawOscilloscope(e.Graphics);
            }

            base.OnPaint(e);
        }

        private void DrawOscilloscope(Graphics graphics)
        {
            Pen pen = new Pen(m_lineColor, m_lineWidth);
            Brush brush = new SolidBrush(m_lineColor);

            int max = m_mappingDatas[m_mappingDatas.Count - 1];
            m_Ratio = (max + m_mappingDatas[0] * 2) / m_width;
            // Draw Wafer data
            for (int i = 1, j = 0; i < m_mappingDatas.Count; i += 2, j++)
            {
                float xStart = m_mappingDatas[i - 1];
                float xEnd = m_mappingDatas[i];
                graphics.DrawLine(pen, xStart / m_Ratio, m_yPositionOfWafer,
                    xEnd / m_Ratio, m_yPositionOfWafer);
                graphics.DrawString((j + 1).ToString(), Control.DefaultFont, brush,
                    (xStart / m_Ratio) - 2, m_yPositionOfNoWafer + 1);
            }

            // Draw No Wafer data
            graphics.DrawLine(pen, 0, m_yPositionOfNoWafer,
                    m_mappingDatas[0] / m_Ratio, m_yPositionOfNoWafer);
            for (int i = 2; i < m_mappingDatas.Count; i += 2)
            {
                float xStart = m_mappingDatas[i - 1];
                float xEnd = m_mappingDatas[i];
                graphics.DrawLine(pen, xStart / m_Ratio, m_yPositionOfNoWafer,
                    xEnd / m_Ratio, m_yPositionOfNoWafer);
            }
            graphics.DrawLine(pen, m_mappingDatas[m_mappingDatas.Count - 1] / m_Ratio, m_yPositionOfNoWafer,
                    m_width, m_yPositionOfNoWafer);

            // Draw vertical line
            for (int i = 1; i < m_mappingDatas.Count; i += 2)
            {
                float X1 = m_mappingDatas[i - 1];
                float X2 = m_mappingDatas[i];
                graphics.DrawLine(pen, X1 / m_Ratio, m_yPositionOfWafer,
                    X1 / m_Ratio, m_yPositionOfNoWafer);
                graphics.DrawLine(pen, X2 / m_Ratio, m_yPositionOfWafer,
                    X2 / m_Ratio, m_yPositionOfNoWafer);
            }

            pen.Dispose();
            brush.Dispose();
        }

        private void CalculateLocals()
        {
            // Calculate help variables
            m_width = this.ClientRectangle.Width;
            m_height = this.ClientRectangle.Height;

            m_yPositionOfNoWafer = (m_height / 2) + (m_height / 5);
            m_yPositionOfWafer = (m_height / 2) - (m_height / 5);
        }
    }
}
