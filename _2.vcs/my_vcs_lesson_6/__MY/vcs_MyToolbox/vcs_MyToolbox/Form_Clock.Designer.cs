namespace vcs_MyToolbox
{
    partial class Form_Clock
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置 Managed 資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器
        /// 修改這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form_Clock));
            this.timer_clock = new System.Windows.Forms.Timer(this.components);
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.timer_display = new System.Windows.Forms.Timer(this.components);
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.bt_stopwatch_3 = new System.Windows.Forms.Button();
            this.bt_stopwatch_2 = new System.Windows.Forms.Button();
            this.bt_stopwatch_1 = new System.Windows.Forms.Button();
            this.digitalDisplayControl1 = new Owf.Controls.DigitalDisplayControl();
            this.timer_stopwatch = new System.Windows.Forms.Timer(this.components);
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // timer_clock
            // 
            this.timer_clock.Enabled = true;
            this.timer_clock.Interval = 1000;
            this.timer_clock.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.radioButton3);
            this.groupBox1.Controls.Add(this.radioButton2);
            this.groupBox1.Controls.Add(this.radioButton1);
            this.groupBox1.Location = new System.Drawing.Point(10, 10);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(100, 150);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(17, 102);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(47, 16);
            this.radioButton3.TabIndex = 2;
            this.radioButton3.Text = "倒數";
            this.radioButton3.UseVisualStyleBackColor = true;
            this.radioButton3.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(17, 68);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(47, 16);
            this.radioButton2.TabIndex = 1;
            this.radioButton2.Text = "碼表";
            this.radioButton2.UseVisualStyleBackColor = true;
            this.radioButton2.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Checked = true;
            this.radioButton1.Location = new System.Drawing.Point(17, 31);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(47, 16);
            this.radioButton1.TabIndex = 0;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "時鐘";
            this.radioButton1.UseVisualStyleBackColor = true;
            this.radioButton1.CheckedChanged += new System.EventHandler(this.radioButton_CheckedChanged);
            // 
            // timer_display
            // 
            this.timer_display.Tick += new System.EventHandler(this.timer_display_Tick);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.bt_stopwatch_3);
            this.groupBox2.Controls.Add(this.bt_stopwatch_2);
            this.groupBox2.Controls.Add(this.bt_stopwatch_1);
            this.groupBox2.Location = new System.Drawing.Point(120, 182);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(230, 102);
            this.groupBox2.TabIndex = 13;
            this.groupBox2.TabStop = false;
            // 
            // bt_stopwatch_3
            // 
            this.bt_stopwatch_3.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_stopwatch_3.BackgroundImage")));
            this.bt_stopwatch_3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_stopwatch_3.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_stopwatch_3.Location = new System.Drawing.Point(154, 25);
            this.bt_stopwatch_3.Name = "bt_stopwatch_3";
            this.bt_stopwatch_3.Size = new System.Drawing.Size(60, 60);
            this.bt_stopwatch_3.TabIndex = 21;
            this.bt_stopwatch_3.UseVisualStyleBackColor = true;
            this.bt_stopwatch_3.Click += new System.EventHandler(this.bt_stopwatch_3_Click);
            // 
            // bt_stopwatch_2
            // 
            this.bt_stopwatch_2.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_stopwatch_2.BackgroundImage")));
            this.bt_stopwatch_2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_stopwatch_2.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_stopwatch_2.Location = new System.Drawing.Point(81, 25);
            this.bt_stopwatch_2.Name = "bt_stopwatch_2";
            this.bt_stopwatch_2.Size = new System.Drawing.Size(60, 60);
            this.bt_stopwatch_2.TabIndex = 20;
            this.bt_stopwatch_2.UseVisualStyleBackColor = true;
            this.bt_stopwatch_2.Click += new System.EventHandler(this.bt_stopwatch_2_Click);
            // 
            // bt_stopwatch_1
            // 
            this.bt_stopwatch_1.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("bt_stopwatch_1.BackgroundImage")));
            this.bt_stopwatch_1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.bt_stopwatch_1.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_stopwatch_1.Location = new System.Drawing.Point(9, 25);
            this.bt_stopwatch_1.Name = "bt_stopwatch_1";
            this.bt_stopwatch_1.Size = new System.Drawing.Size(60, 60);
            this.bt_stopwatch_1.TabIndex = 17;
            this.bt_stopwatch_1.UseVisualStyleBackColor = true;
            this.bt_stopwatch_1.Click += new System.EventHandler(this.bt_stopwatch_1_Click);
            // 
            // digitalDisplayControl1
            // 
            this.digitalDisplayControl1.BackColor = System.Drawing.Color.Transparent;
            this.digitalDisplayControl1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.digitalDisplayControl1.DigitColor = System.Drawing.Color.Purple;
            this.digitalDisplayControl1.DigitText = "88:88:88.88";
            this.digitalDisplayControl1.Location = new System.Drawing.Point(120, 20);
            this.digitalDisplayControl1.Name = "digitalDisplayControl1";
            this.digitalDisplayControl1.Size = new System.Drawing.Size(400, 100);
            this.digitalDisplayControl1.TabIndex = 1;
            this.digitalDisplayControl1.DoubleClick += new System.EventHandler(this.digitalDisplayControl1_DoubleClick);
            // 
            // timer_stopwatch
            // 
            this.timer_stopwatch.Enabled = true;
            this.timer_stopwatch.Interval = 78;
            // 
            // Form_Clock
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(693, 530);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.digitalDisplayControl1);
            this.Name = "Form_Clock";
            this.Text = "Form_Clock";
            this.Load += new System.EventHandler(this.Form_Clock_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.Form_Clock_Paint);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.Form_Clock_MouseDown);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.Form_Clock_MouseMove);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.Form_Clock_MouseUp);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private Owf.Controls.DigitalDisplayControl digitalDisplayControl1;
        private System.Windows.Forms.Timer timer_clock;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.Timer timer_display;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button bt_stopwatch_3;
        private System.Windows.Forms.Button bt_stopwatch_2;
        private System.Windows.Forms.Button bt_stopwatch_1;
        private System.Windows.Forms.Timer timer_stopwatch;
    }
}