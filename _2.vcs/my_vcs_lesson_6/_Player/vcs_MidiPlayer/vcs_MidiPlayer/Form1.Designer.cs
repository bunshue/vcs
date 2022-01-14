namespace vcs_MidiPlayer
{
    partial class Form1
    {
        /// <summary>
        /// 必需的设计器变量。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清理所有正在使用的资源。
        /// </summary>
        /// <param name="disposing">如果应释放托管资源，为 true；否则为 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows 窗体设计器生成的代码

        /// <summary>
        /// 设计器支持所需的方法 - 不要修改
        /// 使用代码编辑器修改此方法的内容。
        /// </summary>
        private void InitializeComponent()
        {
            this.button_shortPlay = new System.Windows.Forms.Button();
            this.label_volumn = new System.Windows.Forms.Label();
            this.numericUpDown_volumn = new System.Windows.Forms.NumericUpDown();
            this.numericUpDown_key = new System.Windows.Forms.NumericUpDown();
            this.label_key = new System.Windows.Forms.Label();
            this.label_chanel = new System.Windows.Forms.Label();
            this.numericUpDown_chenel = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_volumn)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_key)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_chenel)).BeginInit();
            this.SuspendLayout();
            // 
            // button_shortPlay
            // 
            this.button_shortPlay.Location = new System.Drawing.Point(90, 150);
            this.button_shortPlay.Name = "button_shortPlay";
            this.button_shortPlay.Size = new System.Drawing.Size(98, 23);
            this.button_shortPlay.TabIndex = 10;
            this.button_shortPlay.Text = "播放声音";
            this.button_shortPlay.UseVisualStyleBackColor = true;
            this.button_shortPlay.Click += new System.EventHandler(this.button_shortPlay_Click);
            // 
            // label_volumn
            // 
            this.label_volumn.AutoSize = true;
            this.label_volumn.Location = new System.Drawing.Point(31, 111);
            this.label_volumn.Name = "label_volumn";
            this.label_volumn.Size = new System.Drawing.Size(41, 12);
            this.label_volumn.TabIndex = 16;
            this.label_volumn.Text = "音量：";
            // 
            // numericUpDown_volumn
            // 
            this.numericUpDown_volumn.Location = new System.Drawing.Point(90, 109);
            this.numericUpDown_volumn.Maximum = new decimal(new int[] {
            127,
            0,
            0,
            0});
            this.numericUpDown_volumn.Name = "numericUpDown_volumn";
            this.numericUpDown_volumn.Size = new System.Drawing.Size(120, 22);
            this.numericUpDown_volumn.TabIndex = 40;
            this.numericUpDown_volumn.Value = new decimal(new int[] {
            90,
            0,
            0,
            0});
            // 
            // numericUpDown_key
            // 
            this.numericUpDown_key.Location = new System.Drawing.Point(90, 32);
            this.numericUpDown_key.Maximum = new decimal(new int[] {
            120,
            0,
            0,
            0});
            this.numericUpDown_key.Name = "numericUpDown_key";
            this.numericUpDown_key.Size = new System.Drawing.Size(120, 22);
            this.numericUpDown_key.TabIndex = 20;
            this.numericUpDown_key.Value = new decimal(new int[] {
            70,
            0,
            0,
            0});
            // 
            // label_key
            // 
            this.label_key.AutoSize = true;
            this.label_key.Location = new System.Drawing.Point(31, 34);
            this.label_key.Name = "label_key";
            this.label_key.Size = new System.Drawing.Size(41, 12);
            this.label_key.TabIndex = 13;
            this.label_key.Text = "音高：";
            // 
            // label_chanel
            // 
            this.label_chanel.AutoSize = true;
            this.label_chanel.Location = new System.Drawing.Point(31, 74);
            this.label_chanel.Name = "label_chanel";
            this.label_chanel.Size = new System.Drawing.Size(41, 12);
            this.label_chanel.TabIndex = 12;
            this.label_chanel.Text = "频道：";
            // 
            // numericUpDown_chenel
            // 
            this.numericUpDown_chenel.Location = new System.Drawing.Point(90, 68);
            this.numericUpDown_chenel.Maximum = new decimal(new int[] {
            15,
            0,
            0,
            0});
            this.numericUpDown_chenel.Name = "numericUpDown_chenel";
            this.numericUpDown_chenel.Size = new System.Drawing.Size(120, 22);
            this.numericUpDown_chenel.TabIndex = 30;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(325, 438);
            this.Controls.Add(this.button_shortPlay);
            this.Controls.Add(this.label_volumn);
            this.Controls.Add(this.numericUpDown_volumn);
            this.Controls.Add(this.numericUpDown_key);
            this.Controls.Add(this.label_key);
            this.Controls.Add(this.label_chanel);
            this.Controls.Add(this.numericUpDown_chenel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.Text = "MIDI Player";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_volumn)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_key)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown_chenel)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button_shortPlay;
        private System.Windows.Forms.Label label_volumn;
        private System.Windows.Forms.NumericUpDown numericUpDown_volumn;
        private System.Windows.Forms.NumericUpDown numericUpDown_key;
        private System.Windows.Forms.Label label_key;
        private System.Windows.Forms.Label label_chanel;
        private System.Windows.Forms.NumericUpDown numericUpDown_chenel;
    }
}

