using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_2_1_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip1.AutoPopDelay = 5000;
            toolTip1.InitialDelay = 500;
            toolTip1.OwnerDraw = true;
            toolTip1.ReshowDelay = 10;

            button1.Text = "我是Button 1";
            button1.AutoSize = true;
            toolTip1.SetToolTip(button1, "請叫我Visual C#");

            button2.Text = "我是Button 2";
            button2.AutoSize = true;
            toolTip1.SetToolTip(button2, "請叫我Visual Basic 2013");

            button3.Text = "我是Button 3";
            button3.AutoSize = true;
            toolTip1.SetToolTip(button3, "請叫我Visual F#");

            Text = "OwnerDraw屬性的範例";
        }

        private void toolTip1_Popup(object sender, PopupEventArgs e)
        {
            if (e.AssociatedControl == button2)
            {
                using (Font f = new Font("Tahoma", 12))
                {
                    e.ToolTipSize = TextRenderer.MeasureText(
                        toolTip1.GetToolTip(e.AssociatedControl), f);
                }
            }
        }

        private void toolTip1_Draw(object sender, DrawToolTipEventArgs e)
        {
            if (e.AssociatedControl == button1)
            {
                // 繪製標準的背景
                e.DrawBackground();

                // 繪製3 D的框
                e.Graphics.DrawLines(SystemPens.ControlLightLight, new Point[] {
                    new Point (0, e.Bounds.Height - 1), 
                    new Point (0, 0), 
                    new Point (e.Bounds.Width - 1, 0)
                });
                e.Graphics.DrawLines(SystemPens.ControlDarkDark, new Point[] {
                    new Point (0, e.Bounds.Height - 1), 
                    new Point (e.Bounds.Width - 1, e.Bounds.Height - 1), 
                    new Point (e.Bounds.Width - 1, 0)
                });

                // 客製化文字的格式
                TextFormatFlags sf = TextFormatFlags.VerticalCenter |
                                     TextFormatFlags.HorizontalCenter |
                                     TextFormatFlags.NoFullWidthCharacterBreak;

                // 繪製文字
                e.DrawText(sf);
            }
            
            else if (e.AssociatedControl == button2)
            {
                // 繪製客製化的背景
                e.Graphics.FillRectangle(SystemBrushes.ActiveCaption, e.Bounds);

                // 繪製標準的框
                e.DrawBorder();

                // 繪製客製化的文字
                using (StringFormat sf = new StringFormat())
                {
                    sf.Alignment = StringAlignment.Center;
                    sf.LineAlignment = StringAlignment.Center;
                    sf.HotkeyPrefix = System.Drawing.Text.HotkeyPrefix.None;
                    sf.FormatFlags = StringFormatFlags.NoWrap;
                    using (Font f = new Font("Tahoma", 9))
                    {
                        e.Graphics.DrawString(e.ToolTipText, f,
                            SystemBrushes.ActiveCaptionText, e.Bounds, sf);
                    }
                }
            }
           
            else if (e.AssociatedControl == button3)
            {
                e.DrawBackground();
                e.DrawBorder();
                e.DrawText();
            }
        }
    }
}
