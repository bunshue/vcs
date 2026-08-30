namespace vcs_Draw9_Example5c_vcsh
{
    partial class Form1
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
            this.pictureBox0 = new System.Windows.Forms.PictureBox();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox0 = new System.Windows.Forms.GroupBox();
            this.nudDtheta = new System.Windows.Forms.NumericUpDown();
            this.label17 = new System.Windows.Forms.Label();
            this.txtLengthScale = new System.Windows.Forms.TextBox();
            this.label18 = new System.Windows.Forms.Label();
            this.nudLength = new System.Windows.Forms.NumericUpDown();
            this.label19 = new System.Windows.Forms.Label();
            this.nudDepth = new System.Windows.Forms.NumericUpDown();
            this.label20 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox0.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudDtheta)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudLength)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudDepth)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox0
            // 
            this.pictureBox0.BackColor = System.Drawing.Color.White;
            this.pictureBox0.Location = new System.Drawing.Point(12, 12);
            this.pictureBox0.Name = "pictureBox0";
            this.pictureBox0.Size = new System.Drawing.Size(100, 100);
            this.pictureBox0.TabIndex = 16;
            this.pictureBox0.TabStop = false;
            this.pictureBox0.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox0_Paint);
            this.pictureBox0.Resize += new System.EventHandler(this.pictureBox0_Resize);
            // 
            // pictureBox1
            // 
            this.pictureBox1.BackColor = System.Drawing.Color.White;
            this.pictureBox1.Location = new System.Drawing.Point(133, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(100, 100);
            this.pictureBox1.TabIndex = 60;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Paint += new System.Windows.Forms.PaintEventHandler(this.pictureBox1_Paint);
            this.pictureBox1.Resize += new System.EventHandler(this.pictureBox1_Resize);
            // 
            // groupBox0
            // 
            this.groupBox0.Controls.Add(this.nudDtheta);
            this.groupBox0.Controls.Add(this.label17);
            this.groupBox0.Controls.Add(this.txtLengthScale);
            this.groupBox0.Controls.Add(this.label18);
            this.groupBox0.Controls.Add(this.nudLength);
            this.groupBox0.Controls.Add(this.label19);
            this.groupBox0.Controls.Add(this.nudDepth);
            this.groupBox0.Controls.Add(this.label20);
            this.groupBox0.Location = new System.Drawing.Point(12, 131);
            this.groupBox0.Name = "groupBox0";
            this.groupBox0.Size = new System.Drawing.Size(303, 74);
            this.groupBox0.TabIndex = 78;
            this.groupBox0.TabStop = false;
            this.groupBox0.Text = "queue_breadth_first_tree";
            // 
            // nudDtheta
            // 
            this.nudDtheta.Location = new System.Drawing.Point(238, 40);
            this.nudDtheta.Maximum = new decimal(new int[] {
            360,
            0,
            0,
            0});
            this.nudDtheta.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudDtheta.Name = "nudDtheta";
            this.nudDtheta.Size = new System.Drawing.Size(42, 22);
            this.nudDtheta.TabIndex = 25;
            this.nudDtheta.Value = new decimal(new int[] {
            35,
            0,
            0,
            0});
            this.nudDtheta.ValueChanged += new System.EventHandler(this.parameter_ValueChanged);
            this.nudDtheta.KeyUp += new System.Windows.Forms.KeyEventHandler(this.nud_KeyUp);
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(158, 42);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(42, 12);
            this.label17.TabIndex = 24;
            this.label17.Text = "DTheta:";
            // 
            // txtLengthScale
            // 
            this.txtLengthScale.Location = new System.Drawing.Point(237, 16);
            this.txtLengthScale.Name = "txtLengthScale";
            this.txtLengthScale.Size = new System.Drawing.Size(43, 22);
            this.txtLengthScale.TabIndex = 23;
            this.txtLengthScale.Text = "0.75";
            this.txtLengthScale.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.txtLengthScale.TextChanged += new System.EventHandler(this.parameter_ValueChanged);
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(158, 19);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(68, 12);
            this.label18.TabIndex = 22;
            this.label18.Text = "Length Scale:";
            // 
            // nudLength
            // 
            this.nudLength.Location = new System.Drawing.Point(92, 43);
            this.nudLength.Maximum = new decimal(new int[] {
            300,
            0,
            0,
            0});
            this.nudLength.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudLength.Name = "nudLength";
            this.nudLength.Size = new System.Drawing.Size(42, 22);
            this.nudLength.TabIndex = 21;
            this.nudLength.Value = new decimal(new int[] {
            50,
            0,
            0,
            0});
            this.nudLength.ValueChanged += new System.EventHandler(this.parameter_ValueChanged);
            this.nudLength.KeyUp += new System.Windows.Forms.KeyEventHandler(this.nud_KeyUp);
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(12, 45);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(41, 12);
            this.label19.TabIndex = 20;
            this.label19.Text = "Length:";
            // 
            // nudDepth
            // 
            this.nudDepth.Location = new System.Drawing.Point(92, 19);
            this.nudDepth.Maximum = new decimal(new int[] {
            20,
            0,
            0,
            0});
            this.nudDepth.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.nudDepth.Name = "nudDepth";
            this.nudDepth.Size = new System.Drawing.Size(42, 22);
            this.nudDepth.TabIndex = 19;
            this.nudDepth.Value = new decimal(new int[] {
            10,
            0,
            0,
            0});
            this.nudDepth.ValueChanged += new System.EventHandler(this.parameter_ValueChanged);
            this.nudDepth.KeyUp += new System.Windows.Forms.KeyEventHandler(this.nud_KeyUp);
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Location = new System.Drawing.Point(12, 21);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(36, 12);
            this.label20.TabIndex = 18;
            this.label20.Text = "Depth:";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1105, 594);
            this.Controls.Add(this.groupBox0);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.pictureBox0);
            this.Name = "Form1";
            this.Text = "Form1";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Form1_FormClosed);
            this.Load += new System.EventHandler(this.Form1_Load);
            this.Resize += new System.EventHandler(this.Form1_Resize);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox0)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox0.ResumeLayout(false);
            this.groupBox0.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.nudDtheta)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudLength)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.nudDepth)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox0;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.GroupBox groupBox0;
        private System.Windows.Forms.NumericUpDown nudDtheta;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.TextBox txtLengthScale;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.NumericUpDown nudLength;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.NumericUpDown nudDepth;
        private System.Windows.Forms.Label label20;
    }
}

