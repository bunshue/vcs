using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh2_2_61
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

            this.ClientSize = new Size(552, 510);

            Label1.Location = new Point(232, 12);
            Label1.Size = new Size(98, 14);
            Label1.AutoSize = true;
            Label1.Text = "引發的事件清單：";

            Label2.Location = new Point(13, 12);
            Label2.Size = new Size(95, 14);
            Label2.AutoSize = true;
            Label2.Text = "使用者輸入區：";

            this.Controls.Add(Label1);
            this.Controls.Add(Label2);

            TextBoxInput.Location = new Point(13, 34);
            TextBoxInput.Size = new Size(200, 200);
            TextBoxInput.AllowDrop = true;
            TextBoxInput.AutoSize = false;
            TextBoxInput.Cursor = Cursors.Cross;
            TextBoxInput.Multiline = true;
            TextBoxInput.TabIndex = 1;

            TextBoxOutput.Location = new Point(232, 34);
            TextBoxOutput.Size = new Size(308, 440);
            TextBoxOutput.Multiline = true;
            TextBoxOutput.ReadOnly = true;
            TextBoxOutput.ScrollBars = ScrollBars.Vertical;
            TextBoxOutput.TabIndex = 15;
            TextBoxOutput.WordWrap = false;

            this.Controls.Add(TextBoxInput);
            this.Controls.Add(TextBoxOutput);

            LinkLabelDrag.AllowDrop = true;
            LinkLabelDrag.AutoSize = true;
            LinkLabelDrag.Location = new Point(13, 240);
            LinkLabelDrag.Size = new Size(175, 14);
            LinkLabelDrag.TabIndex = 2;
            LinkLabelDrag.TabStop = true;
            LinkLabelDrag.Text = "點選這裡可進行滑鼠拖曳";
            LinkLabelDrag.Links.Add(new LinkLabel.Link(0, LinkLabelDrag.Text.Length));

            this.Controls.Add(LinkLabelDrag);

            CheckBoxToggleAll.AutoSize = true;
            CheckBoxToggleAll.Location = new Point(7, 20);
            CheckBoxToggleAll.Size = new Size(122, 17);
            CheckBoxToggleAll.TabIndex = 4;
            CheckBoxToggleAll.Text = "切換所有的事件設定";

            CheckBoxMouse.AutoSize = true;
            CheckBoxMouse.Location = new Point(7, 45);
            CheckBoxMouse.Size = new Size(137, 17);
            CheckBoxMouse.TabIndex = 5;
            CheckBoxMouse.Text = "Mouse and Click 事件";

            CheckBoxMouseEnter.AutoSize = true;
            CheckBoxMouseEnter.Location = new Point(26, 69);
            CheckBoxMouseEnter.Margin = new Padding(3, 3, 3, 1);
            CheckBoxMouseEnter.Size = new Size(151, 17);
            CheckBoxMouseEnter.TabIndex = 6;
            CheckBoxMouseEnter.Text = "Mouse Enter/Hover/Leave";

            CheckBoxMouseMove.AutoSize = true;
            CheckBoxMouseMove.Location = new Point(26, 89);
            CheckBoxMouseMove.Margin = new Padding(3, 2, 3, 3);
            CheckBoxMouseMove.Size = new Size(120, 17);
            CheckBoxMouseMove.TabIndex = 7;
            CheckBoxMouseMove.Text = "Mouse Move 事件";

            CheckBoxMousePoints.AutoSize = true;
            CheckBoxMousePoints.Location = new Point(26, 112);
            CheckBoxMousePoints.Margin = new Padding(3, 3, 3, 1);
            CheckBoxMousePoints.Size = new Size(141, 17);
            CheckBoxMousePoints.TabIndex = 8;
            CheckBoxMousePoints.Text = "Draw Mouse Points";

            CheckBoxMouseDrag.AutoSize = true;
            CheckBoxMouseDrag.Location = new Point(26, 135);
            CheckBoxMouseDrag.Margin = new Padding(3, 1, 3, 3);
            CheckBoxMouseDrag.Size = new Size(151, 17);
            CheckBoxMouseDrag.TabIndex = 9;
            CheckBoxMouseDrag.Text = "Mouse Drag && Drop 事件";

            CheckBoxMouseDragOver.AutoSize = true;
            CheckBoxMouseDragOver.Location = new Point(44, 159);
            CheckBoxMouseDragOver.Size = new Size(142, 17);
            CheckBoxMouseDragOver.TabIndex = 10;
            CheckBoxMouseDragOver.Text = "Mouse Drag Over 事件";

            CheckBoxKeyboard.AutoSize = true;
            CheckBoxKeyboard.Location = new Point(8, 184);
            CheckBoxKeyboard.Size = new Size(103, 17);
            CheckBoxKeyboard.TabIndex = 11;
            CheckBoxKeyboard.Text = "鍵盤事件";

            CheckBoxKeyUpDown.AutoSize = true;
            CheckBoxKeyUpDown.Location = new Point(26, 207);
            CheckBoxKeyUpDown.Margin = new Padding(3, 3, 3, 1);
            CheckBoxKeyUpDown.Size = new Size(133, 17);
            CheckBoxKeyUpDown.TabIndex = 12;
            CheckBoxKeyUpDown.Text = "Key Up && Down 事件";

            EventsGroupBox.Location = new Point(13, 265);
            EventsGroupBox.Size = new Size(200, 235);
            EventsGroupBox.Text = "事件篩選設定：";
            EventsGroupBox.TabStop = true;
            EventsGroupBox.TabIndex = 3;
            EventsGroupBox.Controls.Add(CheckBoxMouseEnter);
            EventsGroupBox.Controls.Add(CheckBoxToggleAll);
            EventsGroupBox.Controls.Add(CheckBoxMousePoints);
            EventsGroupBox.Controls.Add(CheckBoxKeyUpDown);
            EventsGroupBox.Controls.Add(CheckBoxMouseDragOver);
            EventsGroupBox.Controls.Add(CheckBoxMouseDrag);
            EventsGroupBox.Controls.Add(CheckBoxMouseMove);
            EventsGroupBox.Controls.Add(CheckBoxKeyboard);
            EventsGroupBox.Controls.Add(CheckBoxMouse);

            this.Controls.Add(EventsGroupBox);

            ButtonClear.Location = new Point(232, 480);
            ButtonClear.Size = new Size(308, 23);
            ButtonClear.TabIndex = 16;
            ButtonClear.Text = "清除事件清單";

            this.Controls.Add(ButtonClear);

            ButtonClear.Click += new EventHandler(ButtonClear_Click);
            TextBoxInput.KeyDown += new KeyEventHandler(TextBoxInput_KeyDown);
            TextBoxInput.KeyPress += new KeyPressEventHandler(TextBoxInput_KeyPress);
            TextBoxInput.KeyUp += new KeyEventHandler(TextBoxInput_KeyUp);
            TextBoxInput.Click += new EventHandler(TextBoxInput_Click);
            TextBoxInput.DoubleClick += new EventHandler(TextBoxInput_DoubleClick);
            TextBoxInput.MouseClick += new MouseEventHandler(TextBoxInput_MouseClick);
            TextBoxInput.MouseDoubleClick += new MouseEventHandler(TextBoxInput_MouseDoubleClick);
            TextBoxInput.MouseDown += new MouseEventHandler(TextBoxInput_MouseDown);
            TextBoxInput.MouseUp += new MouseEventHandler(TextBoxInput_MouseUp);
            TextBoxInput.MouseEnter += new EventHandler(TextBoxInput_MouseEnter);
            TextBoxInput.MouseHover += new EventHandler(TextBoxInput_MouseHover);
            TextBoxInput.MouseLeave += new EventHandler(TextBoxInput_MouseLeave);
            TextBoxInput.MouseWheel += new MouseEventHandler(TextBoxInput_MouseWheel);
            TextBoxInput.MouseMove += new MouseEventHandler(TextBoxInput_MouseMove);
            TextBoxInput.MouseCaptureChanged += new EventHandler(TextBoxInput_MouseCaptureChanged);
            TextBoxInput.DragEnter += new DragEventHandler(TextBoxInput_DragEnter);
            TextBoxInput.DragDrop += new DragEventHandler(TextBoxInput_DragDrop);
            TextBoxInput.DragOver += new DragEventHandler(TextBoxInput_DragOver);
            TextBoxInput.DragLeave += new EventHandler(TextBoxInput_DragLeave);

            LinkLabelDrag.MouseDown += new MouseEventHandler(LinkLabelDrag_MouseDown);
            LinkLabelDrag.GiveFeedback += new GiveFeedbackEventHandler(LinkLabelDrag_GiveFeedback);

            CheckBoxToggleAll.CheckedChanged += new EventHandler(CheckBoxToggleAll_CheckedChanged);
            CheckBoxMouse.CheckedChanged += new EventHandler(CheckBoxMouse_CheckedChanged);
            CheckBoxMouseDrag.CheckedChanged += new EventHandler(CheckBoxMouseDrag_CheckedChanged);
            CheckBoxMouseEnter.CheckedChanged += new EventHandler(CheckBoxMouseMove_CheckedChanged);
            CheckBoxMouseMove.CheckedChanged += new EventHandler(CheckBoxMouseMove_CheckedChanged);
            CheckBoxKeyboard.CheckedChanged += new EventHandler(CheckBoxKeyboard_CheckedChanged);

            CheckAllChildCheckBoxes(this, true);
        }

        // 使用遞迴演算法將所有位於Form1物件中的CheckBox物件都勾選 
        private void CheckAllChildCheckBoxes(Control parent, bool value)
        {
            CheckBox box;
            foreach (Control currentControl in parent.Controls)
            {
                if (currentControl is CheckBox)
                {
                    box = (CheckBox)currentControl;
                    box.Checked = value;
                }

                // 如果控制項中還有控制項時，遞迴呼叫
                // 遞迴演算法，請參前面章節的說明
                if (currentControl.Controls.Count > 0)
                {
                    CheckAllChildCheckBoxes(currentControl, value);
                }
            }
        }


        // 將訊息由TextBoxOutput物件中呈現出來
        private void ShowEventMessage(string line)
        {
            TextBoxOutput.AppendText(line);
            TextBoxOutput.AppendText(Environment.NewLine);
        }

        private void ButtonClear_Click(object sender, EventArgs e)
        {
            TextBoxOutput.Clear();
        }

        private void TextBoxInput_KeyDown(object sender, KeyEventArgs e)
        {
            if (CheckBoxKeyUpDown.Checked)
            {
                ShowEventMessage("KeyDown: " + e.KeyData.ToString());
            }
        }

        private void TextBoxInput_KeyUp(object sender, KeyEventArgs e)
        {
            if (CheckBoxKeyUpDown.Checked)
            {
                ShowEventMessage("KeyUp: " + e.KeyData.ToString());
            }
        }

        private void TextBoxInput_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (CheckBoxKeyboard.Checked)
            {
                if (Char.IsWhiteSpace(e.KeyChar))
                {
                    ShowEventMessage("KeyPress: 空白鍵");
                }
                else
                {
                    ShowEventMessage("KeyPress: " + e.KeyChar.ToString());
                }
            }
        }

        private void TextBoxInput_Click(object sender, EventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("Click 事件");
            }
        }

        private void TextBoxInput_DoubleClick(object sender, EventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("DoubleClick 事件");
            }
        }

        private void TextBoxInput_MouseClick(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("MouseClick: " + e.Button.ToString() + " 鍵 " + e.Location.ToString());
            }
        }

        private void TextBoxInput_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("MouseDoubleClick: " + e.Button.ToString() + " 鍵 " + e.Location.ToString());
            }
        }

        private void TextBoxInput_MouseDown(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("MouseDown: " + e.Button.ToString() + " 鍵 " + e.Location.ToString());
            }
        }

        private void TextBoxInput_MouseUp(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("MouseUp: " + e.Button.ToString() + " 鍵 " + e.Location.ToString());
            }
        }

        private void TextBoxInput_MouseEnter(object sender, EventArgs e)
        {
            if (CheckBoxMouseEnter.Checked)
            {
                ShowEventMessage("MouseEnter 事件");
            }
        }

        private void TextBoxInput_MouseHover(object sender, EventArgs e)
        {
            if (CheckBoxMouseEnter.Checked)
            {
                ShowEventMessage("MouseHover 事件");
            }
        }

        private void TextBoxInput_MouseLeave(object sender, EventArgs e)
        {
            if (CheckBoxMouseEnter.Checked)
            {
                ShowEventMessage("MouseLeave 事件");
            }
        }

        private void TextBoxInput_MouseWheel(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouse.Checked)
            {
                ShowEventMessage("MouseWheel: 捲動的距離 " + e.Delta.ToString() + "  " + e.Location.ToString());
            }
        }

        private void TextBoxInput_MouseMove(object sender, MouseEventArgs e)
        {
            if (CheckBoxMouseMove.Checked)
            {
                ShowEventMessage("MouseMove: " + e.Button.ToString() + " " + e.Location.ToString());
            }

            if (CheckBoxMousePoints.Checked)
            {
                Graphics g = TextBoxInput.CreateGraphics();
                g.FillRectangle(Brushes.Black, e.Location.X, e.Location.Y, 1, 1);
                g.Dispose();
            }
        }

        private void TextBoxInput_MouseCaptureChanged(object sender, EventArgs e)
        {
            if (CheckBoxMouseDrag.Checked)
            {
                ShowEventMessage("MouseCaptureChanged 事件");
            }
        }

        private void TextBoxInput_DragEnter(object sender, DragEventArgs e)
        {
            if (CheckBoxMouseDrag.Checked)
            {
                Point pt = new Point(e.X, e.Y);
                ShowEventMessage("DragEnter: " + CovertKeyStateToString(e.KeyState) + " 位於 " + pt.ToString());
            }
        }

        private void TextBoxInput_DragDrop(object sender, DragEventArgs e)
        {
            if (CheckBoxMouseDrag.Checked)
            {
                Point pt = new Point(e.X, e.Y);
                ShowEventMessage("DragDrop: " + CovertKeyStateToString(e.KeyState) + " 位於 " + pt.ToString());
            }
        }

        private void TextBoxInput_DragOver(object sender, DragEventArgs e)
        {
            if (CheckBoxMouseDragOver.Checked)
            {
                Point pt = new Point(e.X, e.Y);
                ShowEventMessage("DragOver: " + CovertKeyStateToString(e.KeyState) + " 位於 " + pt.ToString());
            }

            // Allow if drop data is of type string.
            if (!e.Data.GetDataPresent(typeof(String)))
            {
                e.Effect = DragDropEffects.None;
            }
            else
            {
                e.Effect = DragDropEffects.Copy;
            }
        }

        private void TextBoxInput_DragLeave(object sender, EventArgs e)
        {
            if (CheckBoxMouseDrag.Checked)
            {
                ShowEventMessage("DragLeave 事件");
            }
        }

        private string CovertKeyStateToString(int keyState)
        {
            string keyString = "None";
            // 決定哪一滑鼠按鍵被按下
            if ((keyState & 1) == 1)
            {
                keyString = "Left";
            }
            else if ((keyState & 2) == 2)
            {
                keyString = "Right";
            }
            else if ((keyState & 16) == 16)
            {
                keyString = "Middle";
            }
            // 是否搭配其他的modifiers
            if ((keyState & 4) == 4)
            {
                keyString += "+SHIFT";
            }
            if ((keyState & 8) == 8)
            {
                keyString += "+CTRL";
            }
            if ((keyState & 32) == 32)
            {
                keyString += "+ALT";
            }
            return keyString;
        }

        private void CheckBoxToggleAll_CheckedChanged(object sender, EventArgs e)
        {
            if (sender is CheckBox)
            {
                CheckAllChildCheckBoxes(this, ((CheckBox)sender).Checked);
            }
        }

        private void CheckBoxMouse_CheckedChanged(object sender, EventArgs e)
        {
            ConfigureCheckBoxSettings();
        }

        private void CheckBoxMouseDrag_CheckedChanged(object sender, EventArgs e)
        {
            ConfigureCheckBoxSettings();
        }

        private void CheckBoxKeyboard_CheckedChanged(object sender, EventArgs e)
        {
            ConfigureCheckBoxSettings();
        }

        private void CheckBoxMouseMove_CheckedChanged(object sender, EventArgs e)
        {
            ConfigureCheckBoxSettings();
        }

        // CheckBox物件勾選狀態的切換
        private void ConfigureCheckBoxSettings()
        {
            // CheckBoxMouse是最上層的Check Box物件
            if (!CheckBoxMouse.Checked)
            {
                CheckBoxMouseEnter.Enabled = false;
                CheckBoxMouseMove.Enabled = false;
                CheckBoxMouseDrag.Enabled = false;
                CheckBoxMouseDragOver.Enabled = false;
                CheckBoxMousePoints.Enabled = false;
            }
            else
            {
                CheckBoxMouseEnter.Enabled = true;
                CheckBoxMouseMove.Enabled = true;
                CheckBoxMouseDrag.Enabled = true;
                CheckBoxMousePoints.Enabled = true;

                // 依上層控制項的勾選狀態，調整其項下的控制項的狀態
                if (!CheckBoxMouseDrag.Checked)
                {
                    CheckBoxMouseDragOver.Enabled = false;
                }
                else
                {
                    CheckBoxMouseDragOver.Enabled = true;
                }
            }

            if (!CheckBoxKeyboard.Checked)
            {
                CheckBoxKeyUpDown.Enabled = false;
            }
            else
            {
                CheckBoxKeyUpDown.Enabled = true;
            }
        }

        private void LinkLabelDrag_MouseDown(object sender, MouseEventArgs e)
        {
            string data = "樣本資料";

            // 開始拖放作業。
            LinkLabelDrag.DoDragDrop(data, DragDropEffects.All);
        }

        // 當開始拖放作業時，將引發 GiveFeedback 事件。
        // 使用 GiveFeedback 事件後，拖曳事件的來源可以修改滑鼠指標的外觀，
        // 以便在拖放作業期間為使用者提供視覺化回應。
        private void LinkLabelDrag_GiveFeedback(object sender, GiveFeedbackEventArgs e)
        {
            if ((e.Effect & DragDropEffects.Copy) == DragDropEffects.Copy)
            {
                LinkLabelDrag.Cursor = Cursors.HSplit;
            }
            else
            {
                LinkLabelDrag.Cursor = Cursors.Default;
            }
        }
    }
}
