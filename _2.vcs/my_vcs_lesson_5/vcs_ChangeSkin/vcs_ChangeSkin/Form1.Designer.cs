namespace vcs_ChangeSkin
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.skinEngine1 = new Sunisoft.IrisSkin.SkinEngine();
            this.pictureBox_move = new System.Windows.Forms.PictureBox();
            this.label11 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.button36 = new System.Windows.Forms.Button();
            this.button35 = new System.Windows.Forms.Button();
            this.groupBox8 = new System.Windows.Forms.GroupBox();
            this.label9 = new System.Windows.Forms.Label();
            this.bt_accept_button = new System.Windows.Forms.Button();
            this.bt_cancel_button = new System.Windows.Forms.Button();
            this.button15 = new System.Windows.Forms.Button();
            this.groupBox5 = new System.Windows.Forms.GroupBox();
            this.label5 = new System.Windows.Forms.Label();
            this.lb_checkbox_CheckState = new System.Windows.Forms.Label();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.label6 = new System.Windows.Forms.Label();
            this.flowLayoutPanel1 = new System.Windows.Forms.FlowLayoutPanel();
            this.flp1 = new System.Windows.Forms.Button();
            this.flp2 = new System.Windows.Forms.Button();
            this.flp3 = new System.Windows.Forms.Button();
            this.flp4 = new System.Windows.Forms.Button();
            this.flp5 = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.button16 = new System.Windows.Forms.Button();
            this.button17 = new System.Windows.Forms.Button();
            this.button18 = new System.Windows.Forms.Button();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.button1 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_move)).BeginInit();
            this.groupBox8.SuspendLayout();
            this.groupBox5.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.flowLayoutPanel1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // skinEngine1
            // 
            this.skinEngine1.@__DrawButtonFocusRectangle = true;
            this.skinEngine1.DisabledButtonTextColor = System.Drawing.Color.Gray;
            this.skinEngine1.DisabledMenuFontColor = System.Drawing.SystemColors.GrayText;
            this.skinEngine1.InactiveCaptionColor = System.Drawing.SystemColors.InactiveCaptionText;
            this.skinEngine1.SerialNumber = "";
            this.skinEngine1.SkinFile = null;
            // 
            // pictureBox_move
            // 
            this.pictureBox_move.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox_move.Image")));
            this.pictureBox_move.Location = new System.Drawing.Point(623, 428);
            this.pictureBox_move.Name = "pictureBox_move";
            this.pictureBox_move.Size = new System.Drawing.Size(116, 100);
            this.pictureBox_move.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox_move.TabIndex = 50;
            this.pictureBox_move.TabStop = false;
            // 
            // label11
            // 
            this.label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label11.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label11.Image = ((System.Drawing.Image)(resources.GetObject("label11.Image")));
            this.label11.ImageAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.label11.Location = new System.Drawing.Point(238, 301);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(218, 60);
            this.label11.TabIndex = 49;
            this.label11.Text = "Label";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label10.Location = new System.Drawing.Point(239, 381);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(226, 24);
            this.label10.TabIndex = 48;
            this.label10.Text = "按鈕圖片去背景效果";
            // 
            // button36
            // 
            this.button36.BackColor = System.Drawing.Color.Yellow;
            this.button36.Location = new System.Drawing.Point(230, 408);
            this.button36.Name = "button36";
            this.button36.Size = new System.Drawing.Size(135, 120);
            this.button36.TabIndex = 47;
            this.button36.UseVisualStyleBackColor = false;
            // 
            // button35
            // 
            this.button35.BackColor = System.Drawing.Color.Yellow;
            this.button35.Location = new System.Drawing.Point(368, 408);
            this.button35.Name = "button35";
            this.button35.Size = new System.Drawing.Size(135, 120);
            this.button35.TabIndex = 46;
            this.button35.UseVisualStyleBackColor = false;
            // 
            // groupBox8
            // 
            this.groupBox8.Controls.Add(this.label9);
            this.groupBox8.Controls.Add(this.bt_accept_button);
            this.groupBox8.Controls.Add(this.bt_cancel_button);
            this.groupBox8.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox8.Location = new System.Drawing.Point(238, 147);
            this.groupBox8.Name = "groupBox8";
            this.groupBox8.Size = new System.Drawing.Size(218, 141);
            this.groupBox8.TabIndex = 43;
            this.groupBox8.TabStop = false;
            this.groupBox8.Text = "Form1屬性";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label9.Location = new System.Drawing.Point(6, 98);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(210, 21);
            this.label9.TabIndex = 27;
            this.label9.Text = "Form1屬性設定兩按鍵";
            // 
            // bt_accept_button
            // 
            this.bt_accept_button.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_accept_button.Location = new System.Drawing.Point(6, 29);
            this.bt_accept_button.Name = "bt_accept_button";
            this.bt_accept_button.Size = new System.Drawing.Size(100, 50);
            this.bt_accept_button.TabIndex = 33;
            this.bt_accept_button.Text = "Accept Button";
            this.bt_accept_button.UseVisualStyleBackColor = true;
            // 
            // bt_cancel_button
            // 
            this.bt_cancel_button.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.bt_cancel_button.Font = new System.Drawing.Font("新細明體", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.bt_cancel_button.Location = new System.Drawing.Point(112, 30);
            this.bt_cancel_button.Name = "bt_cancel_button";
            this.bt_cancel_button.Size = new System.Drawing.Size(100, 50);
            this.bt_cancel_button.TabIndex = 34;
            this.bt_cancel_button.Text = "Cancel Button";
            this.bt_cancel_button.UseVisualStyleBackColor = true;
            // 
            // button15
            // 
            this.button15.Location = new System.Drawing.Point(29, 418);
            this.button15.Name = "button15";
            this.button15.Size = new System.Drawing.Size(173, 50);
            this.button15.TabIndex = 41;
            this.button15.Text = "關閉程式時 表單慢慢消失";
            this.button15.UseVisualStyleBackColor = true;
            // 
            // groupBox5
            // 
            this.groupBox5.Controls.Add(this.label5);
            this.groupBox5.Controls.Add(this.lb_checkbox_CheckState);
            this.groupBox5.Controls.Add(this.checkBox1);
            this.groupBox5.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox5.Location = new System.Drawing.Point(462, 259);
            this.groupBox5.Name = "groupBox5";
            this.groupBox5.Size = new System.Drawing.Size(360, 106);
            this.groupBox5.TabIndex = 45;
            this.groupBox5.TabStop = false;
            this.groupBox5.Text = "三態之CheckBox";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("新細明體", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label5.Location = new System.Drawing.Point(124, 24);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(225, 16);
            this.label5.TabIndex = 25;
            this.label5.Text = "CheckBox屬性之TreeState改True";
            // 
            // lb_checkbox_CheckState
            // 
            this.lb_checkbox_CheckState.AutoSize = true;
            this.lb_checkbox_CheckState.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.lb_checkbox_CheckState.Location = new System.Drawing.Point(23, 80);
            this.lb_checkbox_CheckState.Name = "lb_checkbox_CheckState";
            this.lb_checkbox_CheckState.Size = new System.Drawing.Size(169, 19);
            this.lb_checkbox_CheckState.TabIndex = 22;
            this.lb_checkbox_CheckState.Text = "checkbox_CheckState";
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.checkBox1.Location = new System.Drawing.Point(47, 46);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(267, 28);
            this.checkBox1.TabIndex = 24;
            this.checkBox1.Text = "點選CheckBox改變狀態";
            this.checkBox1.ThreeState = true;
            this.checkBox1.UseVisualStyleBackColor = true;
            // 
            // groupBox3
            // 
            this.groupBox3.Controls.Add(this.label6);
            this.groupBox3.Controls.Add(this.flowLayoutPanel1);
            this.groupBox3.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox3.Location = new System.Drawing.Point(462, 140);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(360, 116);
            this.groupBox3.TabIndex = 44;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "FlowLayoutPanel";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("新細明體", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.label6.Location = new System.Drawing.Point(92, 83);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(154, 24);
            this.label6.TabIndex = 22;
            this.label6.Text = "動態變大按鈕";
            // 
            // flowLayoutPanel1
            // 
            this.flowLayoutPanel1.Controls.Add(this.flp1);
            this.flowLayoutPanel1.Controls.Add(this.flp2);
            this.flowLayoutPanel1.Controls.Add(this.flp3);
            this.flowLayoutPanel1.Controls.Add(this.flp4);
            this.flowLayoutPanel1.Controls.Add(this.flp5);
            this.flowLayoutPanel1.Location = new System.Drawing.Point(12, 29);
            this.flowLayoutPanel1.Name = "flowLayoutPanel1";
            this.flowLayoutPanel1.Size = new System.Drawing.Size(336, 57);
            this.flowLayoutPanel1.TabIndex = 21;
            // 
            // flp1
            // 
            this.flp1.Location = new System.Drawing.Point(3, 3);
            this.flp1.Name = "flp1";
            this.flp1.Size = new System.Drawing.Size(55, 30);
            this.flp1.TabIndex = 0;
            this.flp1.Text = "flp1";
            this.flp1.UseVisualStyleBackColor = true;
            // 
            // flp2
            // 
            this.flp2.Location = new System.Drawing.Point(64, 3);
            this.flp2.Name = "flp2";
            this.flp2.Size = new System.Drawing.Size(55, 30);
            this.flp2.TabIndex = 1;
            this.flp2.Text = "flp2";
            this.flp2.UseVisualStyleBackColor = true;
            // 
            // flp3
            // 
            this.flp3.Location = new System.Drawing.Point(125, 3);
            this.flp3.Name = "flp3";
            this.flp3.Size = new System.Drawing.Size(55, 30);
            this.flp3.TabIndex = 2;
            this.flp3.Text = "flp3";
            this.flp3.UseVisualStyleBackColor = true;
            // 
            // flp4
            // 
            this.flp4.Location = new System.Drawing.Point(186, 3);
            this.flp4.Name = "flp4";
            this.flp4.Size = new System.Drawing.Size(55, 30);
            this.flp4.TabIndex = 3;
            this.flp4.Text = "flp4";
            this.flp4.UseVisualStyleBackColor = true;
            // 
            // flp5
            // 
            this.flp5.Location = new System.Drawing.Point(247, 3);
            this.flp5.Name = "flp5";
            this.flp5.Size = new System.Drawing.Size(55, 30);
            this.flp5.TabIndex = 4;
            this.flp5.Text = "flp5";
            this.flp5.UseVisualStyleBackColor = true;
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.button16);
            this.groupBox2.Controls.Add(this.button17);
            this.groupBox2.Controls.Add(this.button18);
            this.groupBox2.Font = new System.Drawing.Font("新細明體", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(136)));
            this.groupBox2.Location = new System.Drawing.Point(12, 174);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(205, 234);
            this.groupBox2.TabIndex = 42;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "調整所有控件大小";
            // 
            // button16
            // 
            this.button16.Location = new System.Drawing.Point(17, 105);
            this.button16.Name = "button16";
            this.button16.Size = new System.Drawing.Size(173, 50);
            this.button16.TabIndex = 9;
            this.button16.Text = "顯示所有控件資訊";
            this.button16.UseVisualStyleBackColor = true;
            // 
            // button17
            // 
            this.button17.Location = new System.Drawing.Point(17, 172);
            this.button17.Name = "button17";
            this.button17.Size = new System.Drawing.Size(173, 50);
            this.button17.TabIndex = 8;
            this.button17.Text = "所有控件大小減半";
            this.button17.UseVisualStyleBackColor = true;
            // 
            // button18
            // 
            this.button18.Location = new System.Drawing.Point(17, 39);
            this.button18.Name = "button18";
            this.button18.Size = new System.Drawing.Size(173, 50);
            this.button18.TabIndex = 7;
            this.button18.Text = "記住所有控件";
            this.button18.UseVisualStyleBackColor = true;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(830, 12);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(306, 546);
            this.richTextBox1.TabIndex = 51;
            this.richTextBox1.Text = "";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(29, 31);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(173, 50);
            this.button1.TabIndex = 10;
            this.button1.Text = "選擇下一個皮膚";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1148, 679);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.pictureBox_move);
            this.Controls.Add(this.label11);
            this.Controls.Add(this.label10);
            this.Controls.Add(this.button36);
            this.Controls.Add(this.button35);
            this.Controls.Add(this.groupBox8);
            this.Controls.Add(this.button15);
            this.Controls.Add(this.groupBox5);
            this.Controls.Add(this.groupBox3);
            this.Controls.Add(this.groupBox2);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox_move)).EndInit();
            this.groupBox8.ResumeLayout(false);
            this.groupBox8.PerformLayout();
            this.groupBox5.ResumeLayout(false);
            this.groupBox5.PerformLayout();
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.flowLayoutPanel1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private Sunisoft.IrisSkin.SkinEngine skinEngine1;
        private System.Windows.Forms.PictureBox pictureBox_move;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Button button36;
        private System.Windows.Forms.Button button35;
        private System.Windows.Forms.GroupBox groupBox8;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Button bt_accept_button;
        private System.Windows.Forms.Button bt_cancel_button;
        private System.Windows.Forms.Button button15;
        private System.Windows.Forms.GroupBox groupBox5;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label lb_checkbox_CheckState;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel1;
        private System.Windows.Forms.Button flp1;
        private System.Windows.Forms.Button flp2;
        private System.Windows.Forms.Button flp3;
        private System.Windows.Forms.Button flp4;
        private System.Windows.Forms.Button flp5;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button button16;
        private System.Windows.Forms.Button button17;
        private System.Windows.Forms.Button button18;
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
    }
}

