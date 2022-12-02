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
            this.button1 = new System.Windows.Forms.Button();
            this.daButton1 = new Bottom_Control.DAButton();
            this.plC_Open_Time1 = new Bottom_Control.设置控件.PLC_Open_Time();
            this.richTextBox1 = new System.Windows.Forms.RichTextBox();
            this.daDataGridView_TO_PLCE1 = new Bottom_Control.基本控件.DADataGridView_TO_PLCE();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.daDataGridView_TO_PLCE1);
            this.groupBox1.Controls.Add(this.button1);
            this.groupBox1.Controls.Add(this.daButton1);
            this.groupBox1.Location = new System.Drawing.Point(12, 21);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(639, 567);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "PC";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(125, 25);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(96, 42);
            this.button1.TabIndex = 1;
            this.button1.Text = "測試";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // daButton1
            // 
            this.daButton1.BackColor = System.Drawing.Color.Transparent;
            this.daButton1.Backdrop_OFF = System.Drawing.Color.FromArgb(((int)(((byte)(74)))), ((int)(((byte)(131)))), ((int)(((byte)(229)))));
            this.daButton1.Backdrop_ON = System.Drawing.Color.Lime;
            this.daButton1.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.daButton1.DownBack = null;
            this.daButton1.Location = new System.Drawing.Point(24, 25);
            this.daButton1.MouseBack = null;
            this.daButton1.Name = "daButton1";
            this.daButton1.NormlBack = null;
            this.daButton1.Pattern = Bottom_Control.Button_pattern.selector_witch;
            this.daButton1.PLC_Address = "20";
            this.daButton1.PLC_Contact = "Y";
            this.daButton1.PLC_Enable = true;
            this.daButton1.Size = new System.Drawing.Size(83, 77);
            this.daButton1.TabIndex = 0;
            this.daButton1.Text = "連接PLC";
            this.daButton1.UseVisualStyleBackColor = false;
            // 
            // plC_Open_Time1
            // 
            this.plC_Open_Time1.Interval = 500;
            this.plC_Open_Time1.Mitsubishi_Open = true;
            this.plC_Open_Time1.MitsubishiIP = "192.168.3.39";
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
            // daDataGridView_TO_PLCE1
            // 
            this.daDataGridView_TO_PLCE1.DataGridView_Name = new string[] {
        "VW0",
        "VW1",
        "VW2",
        "VW3",
        "VW4",
        "VW5",
        "VW6",
        "VW7",
        "VW8",
        "VW9"};
            this.daDataGridView_TO_PLCE1.DataGridView_numerical = new Bottom_Control.numerical_format[] {
        Bottom_Control.numerical_format.Signed_16_Bit,
        Bottom_Control.numerical_format.Signed_16_Bit,
        Bottom_Control.numerical_format.Signed_16_Bit,
        Bottom_Control.numerical_format.Signed_16_Bit,
        Bottom_Control.numerical_format.BCD_16_Bit,
        Bottom_Control.numerical_format.Unsigned_16_Bit,
        Bottom_Control.numerical_format.Binary_32_Bit,
        Bottom_Control.numerical_format.BCD_16_Bit,
        Bottom_Control.numerical_format.String_32_Bit,
        Bottom_Control.numerical_format.Binary_32_Bit};
            this.daDataGridView_TO_PLCE1.DataGridViewPLC_Time = false;
            this.daDataGridView_TO_PLCE1.Location = new System.Drawing.Point(243, 25);
            this.daDataGridView_TO_PLCE1.Name = "daDataGridView_TO_PLCE1";
            this.daDataGridView_TO_PLCE1.PLC_address = new string[] {
        "1.0",
        "1.1",
        "1.2",
        "1.3",
        "1.4",
        "1.5",
        "1.6",
        "1.7",
        "1.8",
        "1.9"};
            this.daDataGridView_TO_PLCE1.PLC_Address = "0";
            this.daDataGridView_TO_PLCE1.PLC_Contact = "D";
            this.daDataGridView_TO_PLCE1.PLC_Enable = true;
            this.daDataGridView_TO_PLCE1.Size = new System.Drawing.Size(197, 317);
            this.daDataGridView_TO_PLCE1.TabIndex = 2;
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
        private System.Windows.Forms.RichTextBox richTextBox1;
        private System.Windows.Forms.Button button1;
        private 基本控件.DADataGridView_TO_PLCE daDataGridView_TO_PLCE1;
    }
}