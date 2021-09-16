using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh1_1_3_11
{
    public partial class Form1 : Form
    {
        Label Label1 = new Label();
        Label Label2 = new Label();
        TextBox TextBoxOutput = new TextBox();
        TextBox TextBoxInput = new TextBox();
        GroupBox EventsGroupBox = new GroupBox();
        Button ButtonClear = new Button();
        LinkLabel LinkLabelDrag = new LinkLabel();

        CheckBox CheckBoxToggleAll = new CheckBox();
        CheckBox CheckBoxMouse = new CheckBox();
        CheckBox CheckBoxMouseEnter = new CheckBox();
        CheckBox CheckBoxMouseMove = new CheckBox();
        CheckBox CheckBoxMousePoints = new CheckBox();
        CheckBox CheckBoxMouseDrag = new CheckBox();
        CheckBox CheckBoxMouseDragOver = new CheckBox();
        CheckBox CheckBoxKeyboard = new CheckBox();
        CheckBox CheckBoxKeyUpDown = new CheckBox();

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

        }

        private void button1_Click(object sender, EventArgs e)
        {
           
        }
    }
}


