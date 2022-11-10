namespace Bottom_Control
{
    partial class Form2
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.daButton1 = new Bottom_Control.DAButton();
            this.plC_Open_Time1 = new Bottom_Control.设置控件.PLC_Open_Time();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.daButton2 = new Bottom_Control.DAButton();
            this.daButton3 = new Bottom_Control.DAButton();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.daButton3);
            this.groupBox1.Controls.Add(this.daButton2);
            this.groupBox1.Controls.Add(this.daButton1);
            this.groupBox1.Location = new System.Drawing.Point(12, 21);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(639, 567);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "PC";
            // 
            // daButton1
            // 
            this.daButton1.BackColor = System.Drawing.Color.Transparent;
            this.daButton1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daButton1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daButton1.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.daButton1.DownBack = null;
            this.daButton1.Location = new System.Drawing.Point(35, 54);
            this.daButton1.MouseBack = null;
            this.daButton1.Name = "daButton1";
            this.daButton1.NormlBack = null;
            this.daButton1.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daButton1.PLC_Address = "20";
            this.daButton1.PLC_Contact = "Y";
            this.daButton1.PLC_Enable = true;
            this.daButton1.Size = new System.Drawing.Size(100, 100);
            this.daButton1.TabIndex = 0;
            this.daButton1.Text = "連接PLC";
            this.daButton1.UseVisualStyleBackColor = false;
            // 
            // plC_Open_Time1
            // 
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.ModBusIP = "192.168.3.20";
            this.plC_Open_Time1.siemensPLCS = HslCommunication.Profinet.SiemensPLCS.S200Smart;
            // 
            // richTextBox1
            // 
            this.richTextBox1.Location = new System.Drawing.Point(667, 21);
            this.richTextBox1.Name = "richTextBox1";
            this.richTextBox1.Size = new System.Drawing.Size(352, 567);
            this.richTextBox1.TabIndex = 2;
            this.richTextBox1.Text = "";
            // 
            // daButton2
            // 
            this.daButton2.BackColor = System.Drawing.Color.Transparent;
            this.daButton2.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daButton2.Backdrop_ON = System.Drawing.Color.Lime;
            this.daButton2.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.daButton2.DownBack = null;
            this.daButton2.Location = new System.Drawing.Point(35, 216);
            this.daButton2.MouseBack = null;
            this.daButton2.Name = "daButton2";
            this.daButton2.NormlBack = null;
            this.daButton2.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daButton2.PLC_Address = "20";
            this.daButton2.PLC_Contact = "Y";
            this.daButton2.PLC_Enable = true;
            this.daButton2.Size = new System.Drawing.Size(100, 100);
            this.daButton2.TabIndex = 1;
            this.daButton2.Text = "發送命令";
            this.daButton2.UseVisualStyleBackColor = false;
            // 
            // daButton3
            // 
            this.daButton3.BackColor = System.Drawing.Color.Transparent;
            this.daButton3.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daButton3.Backdrop_ON = System.Drawing.Color.Lime;
            this.daButton3.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.daButton3.DownBack = null;
            this.daButton3.Location = new System.Drawing.Point(35, 382);
            this.daButton3.MouseBack = null;
            this.daButton3.Name = "daButton3";
            this.daButton3.NormlBack = null;
            this.daButton3.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daButton3.PLC_Address = "20";
            this.daButton3.PLC_Contact = "Y";
            this.daButton3.PLC_Enable = true;
            this.daButton3.Size = new System.Drawing.Size(100, 100);
            this.daButton3.TabIndex = 2;
            this.daButton3.Text = "接收";
            this.daButton3.UseVisualStyleBackColor = false;
            // 
            // Form2
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1031, 600);
            this.Controls.Add(this.richTextBox1);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form2";
            this.Text = "Form2";
            this.Load += new System.EventHandler(this.Form2_Load);
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private 设置控件.PLC_Open_Time plC_Open_Time1;
        private DAButton daButton1;
        private System.Windows.Forms.GroupBox groupBox1;
        private DAButton daButton3;
        private DAButton daButton2;
        private System.Windows.Forms.RichTextBox richTextBox1;
    }
}