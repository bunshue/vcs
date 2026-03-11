using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
拉一個 ToolTip
加入動作
toolTip1_Popup()和toolTip1_Draw()
*/

namespace vcs_ToolTip2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip0.AutoPopDelay = 5000;
            toolTip0.InitialDelay = 10;
            toolTip0.ReshowDelay = 500;
            toolTip0.IsBalloon = true;
            toolTip0.ToolTipIcon = ToolTipIcon.Info;
            toolTip0.ToolTipTitle = "小提示";
            toolTip0.ShowAlways = true;

            toolTip0.SetToolTip(textBox0, "textBox1預設的文字");
            toolTip0.SetToolTip(button00, "button00預設的文字");
            toolTip0.SetToolTip(button01, "button01預設的文字");
            toolTip0.SetToolTip(button02, "button02預設的文字");

            //6060

            toolTip1.AutoPopDelay = 5000;
            toolTip1.InitialDelay = 500;
            toolTip1.OwnerDraw = true;
            toolTip1.ReshowDelay = 10;

            button10.Text = "我是Button 1";
            button10.AutoSize = true;
            toolTip1.SetToolTip(button10, "請叫我Visual C#");

            button11.Text = "我是Button 2";
            button11.AutoSize = true;
            toolTip1.SetToolTip(button11, "請叫我Visual Basic 2013");

            button12.Text = "我是Button 3";
            button12.AutoSize = true;
            toolTip1.SetToolTip(button12, "請叫我Visual F#");

            Text = "OwnerDraw屬性的範例";
        }


        private void button00_Click(object sender, EventArgs e)
        {
            //設定
            toolTip0.SetToolTip(textBox0, textBox0.Text);
        }

        private void button01_Click(object sender, EventArgs e)
        {
            //取得
            textBox0.Text = toolTip0.GetToolTip(textBox0);
        }

        private void button02_Click(object sender, EventArgs e)
        {
            //全部移除
            toolTip0.RemoveAll();
        }

        private void textBox0_TextChanged(object sender, EventArgs e)
        {
            try
            {
                if (textBox0.Text != "")
                {
                    Convert.ToInt32(textBox0.Text);
                }
            }
            catch (Exception ex)
            {
                toolTip0.ToolTipIcon = ToolTipIcon.Error;
                toolTip0.Show("請輸入數字 ！", textBox0, 2000);
            }
        }

        //6060

        private void toolTip1_Popup(object sender, PopupEventArgs e)
        {
            if (e.AssociatedControl == button11)
            {
                using (Font f = new Font("Tahoma", 12))
                {
                    e.ToolTipSize = TextRenderer.MeasureText(toolTip1.GetToolTip(e.AssociatedControl), f);
                }
            }
        }

        private void toolTip1_Draw(object sender, DrawToolTipEventArgs e)
        {
            if (e.AssociatedControl == button10)
            {
                // 繪製標準的背景
                e.DrawBackground();

                // 繪製3 D的框
                e.Graphics.DrawLines(SystemPens.ControlLightLight, new Point[]
                {
                    new Point (0, e.Bounds.Height - 1), 
                    new Point (0, 0), 
                    new Point (e.Bounds.Width - 1, 0)
                });

                e.Graphics.DrawLines(SystemPens.ControlDarkDark, new Point[]
                {
                    new Point (0, e.Bounds.Height - 1), 
                    new Point (e.Bounds.Width - 1, e.Bounds.Height - 1), 
                    new Point (e.Bounds.Width - 1, 0)
                });

                // 客製化文字的格式
                TextFormatFlags sf = TextFormatFlags.VerticalCenter | TextFormatFlags.HorizontalCenter | TextFormatFlags.NoFullWidthCharacterBreak;

                // 繪製文字
                e.DrawText(sf);
            }
            else if (e.AssociatedControl == button11)
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
                        e.Graphics.DrawString(e.ToolTipText, f, SystemBrushes.ActiveCaptionText, e.Bounds, sf);
                    }
                }
            }
            else if (e.AssociatedControl == button12)
            {
                e.DrawBackground();
                e.DrawBorder();
                e.DrawText();
            }
        }

    }
}
