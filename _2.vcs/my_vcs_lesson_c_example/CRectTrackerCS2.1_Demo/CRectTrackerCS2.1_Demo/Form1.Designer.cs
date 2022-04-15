namespace CRectTrackerCS2.__Demo
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }

            TestRubberBand.Destroy();//ÊÍ·Å×ÊÔ´

            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.ResizePinNoHide = new System.Windows.Forms.RadioButton();
            this.ResizePinAutoHide = new System.Windows.Forms.RadioButton();
            this.ResizePinAlwaysHide = new System.Windows.Forms.RadioButton();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.DottedLine = new System.Windows.Forms.RadioButton();
            this.SolidLine = new System.Windows.Forms.RadioButton();
            this.ChangeRubberBandColor = new System.Windows.Forms.Button();
            this.LoadDefaultsRubberBandStyle = new System.Windows.Forms.Button();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.SuspendLayout();
            // 
            // timer1
            // 
            this.timer1.Interval = 560;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.ResizePinNoHide);
            this.groupBox1.Controls.Add(this.ResizePinAutoHide);
            this.groupBox1.Controls.Add(this.ResizePinAlwaysHide);
            this.groupBox1.Location = new System.Drawing.Point(8, 20);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(170, 86);
            this.groupBox1.TabIndex = 3;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "ResizePinStyle";
            // 
            // ResizePinNoHide
            // 
            this.ResizePinNoHide.AutoSize = true;
            this.ResizePinNoHide.Location = new System.Drawing.Point(6, 20);
            this.ResizePinNoHide.Name = "ResizePinNoHide";
            this.ResizePinNoHide.Size = new System.Drawing.Size(104, 16);
            this.ResizePinNoHide.TabIndex = 3;
            this.ResizePinNoHide.TabStop = true;
            this.ResizePinNoHide.Text = "ResizePinNoHide";
            this.ResizePinNoHide.UseVisualStyleBackColor = true;
            this.ResizePinNoHide.CheckedChanged += new System.EventHandler(this.ResizePinNoHide_CheckedChanged);
            // 
            // ResizePinAutoHide
            // 
            this.ResizePinAutoHide.AutoSize = true;
            this.ResizePinAutoHide.Location = new System.Drawing.Point(6, 42);
            this.ResizePinAutoHide.Name = "ResizePinAutoHide";
            this.ResizePinAutoHide.Size = new System.Drawing.Size(113, 16);
            this.ResizePinAutoHide.TabIndex = 4;
            this.ResizePinAutoHide.TabStop = true;
            this.ResizePinAutoHide.Text = "ResizePinAutoHide";
            this.ResizePinAutoHide.UseVisualStyleBackColor = true;
            this.ResizePinAutoHide.CheckedChanged += new System.EventHandler(this.ResizePinAutoHide_CheckedChanged);
            // 
            // ResizePinAlwaysHide
            // 
            this.ResizePinAlwaysHide.AutoSize = true;
            this.ResizePinAlwaysHide.Location = new System.Drawing.Point(6, 64);
            this.ResizePinAlwaysHide.Name = "ResizePinAlwaysHide";
            this.ResizePinAlwaysHide.Size = new System.Drawing.Size(124, 16);
            this.ResizePinAlwaysHide.TabIndex = 5;
            this.ResizePinAlwaysHide.TabStop = true;
            this.ResizePinAlwaysHide.Text = "ResizePinAlwaysHide";
            this.ResizePinAlwaysHide.UseVisualStyleBackColor = true;
            this.ResizePinAlwaysHide.CheckedChanged += new System.EventHandler(this.ResizePinAlwaysHide_CheckedChanged);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.DottedLine);
            this.groupBox2.Controls.Add(this.SolidLine);
            this.groupBox2.Location = new System.Drawing.Point(8, 137);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(93, 70);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "LineStyle";
            // 
            // DottedLine
            // 
            this.DottedLine.AutoSize = true;
            this.DottedLine.Location = new System.Drawing.Point(6, 42);
            this.DottedLine.Name = "DottedLine";
            this.DottedLine.Size = new System.Drawing.Size(75, 16);
            this.DottedLine.TabIndex = 7;
            this.DottedLine.TabStop = true;
            this.DottedLine.Text = "DottedLine";
            this.DottedLine.UseVisualStyleBackColor = true;
            this.DottedLine.CheckedChanged += new System.EventHandler(this.DottedLine_CheckedChanged);
            // 
            // SolidLine
            // 
            this.SolidLine.AutoSize = true;
            this.SolidLine.Location = new System.Drawing.Point(6, 20);
            this.SolidLine.Name = "SolidLine";
            this.SolidLine.Size = new System.Drawing.Size(68, 16);
            this.SolidLine.TabIndex = 6;
            this.SolidLine.TabStop = true;
            this.SolidLine.Text = "SolidLine";
            this.SolidLine.UseVisualStyleBackColor = true;
            this.SolidLine.CheckedChanged += new System.EventHandler(this.SolidLine_CheckedChanged);
            // 
            // ChangeRubberBandColor
            // 
            this.ChangeRubberBandColor.Location = new System.Drawing.Point(105, 143);
            this.ChangeRubberBandColor.Name = "ChangeRubberBandColor";
            this.ChangeRubberBandColor.Size = new System.Drawing.Size(73, 64);
            this.ChangeRubberBandColor.TabIndex = 4;
            this.ChangeRubberBandColor.Text = "Change RubberBand Color";
            this.ChangeRubberBandColor.UseVisualStyleBackColor = true;
            this.ChangeRubberBandColor.Click += new System.EventHandler(this.ChangeRubberBandColor_Click);
            // 
            // LoadDefaultsRubberBandStyle
            // 
            this.LoadDefaultsRubberBandStyle.Location = new System.Drawing.Point(8, 239);
            this.LoadDefaultsRubberBandStyle.Name = "LoadDefaultsRubberBandStyle";
            this.LoadDefaultsRubberBandStyle.Size = new System.Drawing.Size(170, 61);
            this.LoadDefaultsRubberBandStyle.TabIndex = 1;
            this.LoadDefaultsRubberBandStyle.Text = "LoadDefaults RubberBandStyle";
            this.LoadDefaultsRubberBandStyle.UseVisualStyleBackColor = true;
            this.LoadDefaultsRubberBandStyle.Click += new System.EventHandler(this.LoadDefaultsRubberBandStyle_Click);
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.groupBox1);
            this.groupBox3.Controls.Add(this.LoadDefaultsRubberBandStyle);
            this.groupBox3.Controls.Add(this.groupBox2);
            this.groupBox3.Controls.Add(this.ChangeRubberBandColor);
            this.groupBox3.Location = new System.Drawing.Point(8, 5);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(186, 414);
            this.groupBox3.TabIndex = 5;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Customize";
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(819, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(284, 484);
            this.richTextBox1.TabIndex = 12;
            this.richTextBox1.Text = "";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("·s²Ó©úÅé", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label1.Location = new System.Drawing.Point(8, 475);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 24);
            this.label1.TabIndex = 13;
            this.label1.Text = "label1";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.ClientSize = new System.Drawing.Size(1115, 531);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox3);
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.Text = "CRectTrackerCS2.1_Demo";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form1_Paint);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseDown);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseMove);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.Form1_MouseUp);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton ResizePinNoHide;
        private System.Windows.Forms.RadioButton ResizePinAutoHide;
        private System.Windows.Forms.RadioButton ResizePinAlwaysHide;
        private System.Windows.Forms.RadioButton SolidLine;
        private System.Windows.Forms.RadioButton DottedLine;
        private System.Windows.Forms.Button ChangeRubberBandColor;
        private System.Windows.Forms.Button LoadDefaultsRubberBandStyle;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Label label1;
    }
}

