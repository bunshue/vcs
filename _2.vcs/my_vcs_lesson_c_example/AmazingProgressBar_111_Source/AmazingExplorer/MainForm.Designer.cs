namespace AmazingExplorer
{
    partial class MainForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.minTextBox = new System.Windows.Forms.TextBox();
            this.minButton = new System.Windows.Forms.Button();
            this.maxButton = new System.Windows.Forms.Button();
            this.maxTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.valueButton = new System.Windows.Forms.Button();
            this.valueTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.origGroupBox = new System.Windows.Forms.GroupBox();
            this.rotateButton = new System.Windows.Forms.Button();
            this.heightButton = new System.Windows.Forms.Button();
            this.heightTextBox = new System.Windows.Forms.TextBox();
            this.label15 = new System.Windows.Forms.Label();
            this.widthButton = new System.Windows.Forms.Button();
            this.widthTextBox = new System.Windows.Forms.TextBox();
            this.label14 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.styleComboBox = new System.Windows.Forms.ComboBox();
            this.label7 = new System.Windows.Forms.Label();
            this.foreColorButton = new System.Windows.Forms.Button();
            this.foreColorLabel = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.backColorButton = new System.Windows.Forms.Button();
            this.backColorLabel = new System.Windows.Forms.Label();
            this.marqueeSpeedButton = new System.Windows.Forms.Button();
            this.marqueeSpeedTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.endColorLabel = new System.Windows.Forms.Label();
            this.endColorButton = new System.Windows.Forms.Button();
            this.label8 = new System.Windows.Forms.Label();
            this.startColorLabel = new System.Windows.Forms.Label();
            this.startColorButton = new System.Windows.Forms.Button();
            this.label10 = new System.Windows.Forms.Label();
            this.wallColorLabel = new System.Windows.Forms.Label();
            this.wallColorButton = new System.Windows.Forms.Button();
            this.label11 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.wallSizeTextBox = new System.Windows.Forms.TextBox();
            this.wallSizeButton = new System.Windows.Forms.Button();
            this.mazeStyleComboBox = new System.Windows.Forms.ComboBox();
            this.label12 = new System.Windows.Forms.Label();
            this.newGroupBox = new System.Windows.Forms.GroupBox();
            this.borderRoundCheckBox = new System.Windows.Forms.CheckBox();
            this.infoLabel = new System.Windows.Forms.Label();
            this.borderGradientCheckBox = new System.Windows.Forms.CheckBox();
            this.gradientComboBox = new System.Windows.Forms.ComboBox();
            this.label18 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.rowCountButton = new System.Windows.Forms.Button();
            this.regenButton = new System.Windows.Forms.Button();
            this.rowCountTextBox = new System.Windows.Forms.TextBox();
            this.label16 = new System.Windows.Forms.Label();
            this.borderSizeTextBox = new System.Windows.Forms.TextBox();
            this.borderSizeButton = new System.Windows.Forms.Button();
            this.borderColorLabel = new System.Windows.Forms.Label();
            this.borderColorButton = new System.Windows.Forms.Button();
            this.label17 = new System.Windows.Forms.Label();
            this.valueGroupBox = new System.Windows.Forms.GroupBox();
            this.plus3RadioButton = new System.Windows.Forms.RadioButton();
            this.plus2RadioButton = new System.Windows.Forms.RadioButton();
            this.plus1RadioButton = new System.Windows.Forms.RadioButton();
            this.stopRadioButton = new System.Windows.Forms.RadioButton();
            this.minus1RadioButton = new System.Windows.Forms.RadioButton();
            this.minus2RadioButton = new System.Windows.Forms.RadioButton();
            this.minus3RadioButton = new System.Windows.Forms.RadioButton();
            this.autoModeTimer = new System.Windows.Forms.Timer(this.components);
            this.amazing = new GAW.AmazingProgressBar();
            this.origGroupBox.SuspendLayout();
            this.newGroupBox.SuspendLayout();
            this.valueGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.Location = new System.Drawing.Point(32, 184);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(64, 22);
            this.label1.TabIndex = 17;
            this.label1.Text = "Mi&nimum:";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // minTextBox
            // 
            this.minTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.minTextBox.Location = new System.Drawing.Point(104, 184);
            this.minTextBox.Name = "minTextBox";
            this.minTextBox.Size = new System.Drawing.Size(64, 22);
            this.minTextBox.TabIndex = 18;
            this.minTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // minButton
            // 
            this.minButton.Location = new System.Drawing.Point(176, 184);
            this.minButton.Name = "minButton";
            this.minButton.Size = new System.Drawing.Size(48, 22);
            this.minButton.TabIndex = 19;
            this.minButton.Text = "Set";
            this.minButton.UseVisualStyleBackColor = true;
            this.minButton.Click += new System.EventHandler(this.minButton_Click);
            // 
            // maxButton
            // 
            this.maxButton.Location = new System.Drawing.Point(176, 208);
            this.maxButton.Name = "maxButton";
            this.maxButton.Size = new System.Drawing.Size(48, 22);
            this.maxButton.TabIndex = 22;
            this.maxButton.Text = "Set";
            this.maxButton.UseVisualStyleBackColor = true;
            this.maxButton.Click += new System.EventHandler(this.maxButton_Click);
            // 
            // maxTextBox
            // 
            this.maxTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.maxTextBox.Location = new System.Drawing.Point(104, 208);
            this.maxTextBox.Name = "maxTextBox";
            this.maxTextBox.Size = new System.Drawing.Size(64, 22);
            this.maxTextBox.TabIndex = 21;
            this.maxTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label2
            // 
            this.label2.Location = new System.Drawing.Point(32, 208);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(64, 22);
            this.label2.TabIndex = 20;
            this.label2.Text = "Ma&ximum:";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // valueButton
            // 
            this.valueButton.Location = new System.Drawing.Point(176, 232);
            this.valueButton.Name = "valueButton";
            this.valueButton.Size = new System.Drawing.Size(48, 22);
            this.valueButton.TabIndex = 25;
            this.valueButton.Text = "Set";
            this.valueButton.UseVisualStyleBackColor = true;
            this.valueButton.Click += new System.EventHandler(this.valueButton_Click);
            // 
            // valueTextBox
            // 
            this.valueTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.valueTextBox.Location = new System.Drawing.Point(104, 232);
            this.valueTextBox.Name = "valueTextBox";
            this.valueTextBox.Size = new System.Drawing.Size(64, 22);
            this.valueTextBox.TabIndex = 24;
            this.valueTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label3
            // 
            this.label3.Location = new System.Drawing.Point(32, 232);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(64, 22);
            this.label3.TabIndex = 23;
            this.label3.Text = "&Value:";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // origGroupBox
            // 
            this.origGroupBox.Controls.Add(this.rotateButton);
            this.origGroupBox.Controls.Add(this.heightButton);
            this.origGroupBox.Controls.Add(this.heightTextBox);
            this.origGroupBox.Controls.Add(this.label15);
            this.origGroupBox.Controls.Add(this.widthButton);
            this.origGroupBox.Controls.Add(this.widthTextBox);
            this.origGroupBox.Controls.Add(this.label14);
            this.origGroupBox.Controls.Add(this.maxTextBox);
            this.origGroupBox.Controls.Add(this.maxButton);
            this.origGroupBox.Controls.Add(this.label3);
            this.origGroupBox.Controls.Add(this.label2);
            this.origGroupBox.Controls.Add(this.minButton);
            this.origGroupBox.Controls.Add(this.minTextBox);
            this.origGroupBox.Controls.Add(this.valueTextBox);
            this.origGroupBox.Controls.Add(this.label4);
            this.origGroupBox.Controls.Add(this.label1);
            this.origGroupBox.Controls.Add(this.styleComboBox);
            this.origGroupBox.Controls.Add(this.label7);
            this.origGroupBox.Controls.Add(this.valueButton);
            this.origGroupBox.Controls.Add(this.foreColorButton);
            this.origGroupBox.Controls.Add(this.foreColorLabel);
            this.origGroupBox.Controls.Add(this.label6);
            this.origGroupBox.Controls.Add(this.backColorButton);
            this.origGroupBox.Controls.Add(this.backColorLabel);
            this.origGroupBox.Controls.Add(this.marqueeSpeedButton);
            this.origGroupBox.Controls.Add(this.marqueeSpeedTextBox);
            this.origGroupBox.Controls.Add(this.label5);
            this.origGroupBox.Location = new System.Drawing.Point(16, 8);
            this.origGroupBox.Name = "origGroupBox";
            this.origGroupBox.Size = new System.Drawing.Size(232, 264);
            this.origGroupBox.TabIndex = 0;
            this.origGroupBox.TabStop = false;
            // 
            // rotateButton
            // 
            this.rotateButton.Location = new System.Drawing.Point(104, 112);
            this.rotateButton.Name = "rotateButton";
            this.rotateButton.Size = new System.Drawing.Size(120, 22);
            this.rotateButton.TabIndex = 26;
            this.rotateButton.Text = "Rotate 90 deg";
            this.rotateButton.UseVisualStyleBackColor = true;
            this.rotateButton.Click += new System.EventHandler(this.rotateButton_Click);
            // 
            // heightButton
            // 
            this.heightButton.Location = new System.Drawing.Point(176, 88);
            this.heightButton.Name = "heightButton";
            this.heightButton.Size = new System.Drawing.Size(48, 22);
            this.heightButton.TabIndex = 10;
            this.heightButton.Text = "Set";
            this.heightButton.UseVisualStyleBackColor = true;
            this.heightButton.Click += new System.EventHandler(this.heightButton_Click);
            // 
            // heightTextBox
            // 
            this.heightTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.heightTextBox.Location = new System.Drawing.Point(104, 88);
            this.heightTextBox.Name = "heightTextBox";
            this.heightTextBox.Size = new System.Drawing.Size(64, 22);
            this.heightTextBox.TabIndex = 9;
            this.heightTextBox.TextAlignChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label15
            // 
            this.label15.Location = new System.Drawing.Point(32, 88);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(64, 22);
            this.label15.TabIndex = 8;
            this.label15.Text = "Height:";
            this.label15.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // widthButton
            // 
            this.widthButton.Location = new System.Drawing.Point(176, 64);
            this.widthButton.Name = "widthButton";
            this.widthButton.Size = new System.Drawing.Size(48, 22);
            this.widthButton.TabIndex = 7;
            this.widthButton.Text = "Set";
            this.widthButton.UseVisualStyleBackColor = true;
            this.widthButton.Click += new System.EventHandler(this.widthButton_Click);
            // 
            // widthTextBox
            // 
            this.widthTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.widthTextBox.Location = new System.Drawing.Point(104, 64);
            this.widthTextBox.Name = "widthTextBox";
            this.widthTextBox.Size = new System.Drawing.Size(64, 22);
            this.widthTextBox.TabIndex = 6;
            this.widthTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label14
            // 
            this.label14.Location = new System.Drawing.Point(32, 64);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(64, 22);
            this.label14.TabIndex = 5;
            this.label14.Text = "Width:";
            this.label14.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label4
            // 
            this.label4.Location = new System.Drawing.Point(32, 16);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(64, 22);
            this.label4.TabIndex = 0;
            this.label4.Text = "&Style:";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // styleComboBox
            // 
            this.styleComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.styleComboBox.FormattingEnabled = true;
            this.styleComboBox.Items.AddRange(new object[] {
            "Block",
            "Continuous",
            "Marquee"});
            this.styleComboBox.Location = new System.Drawing.Point(104, 16);
            this.styleComboBox.Name = "styleComboBox";
            this.styleComboBox.Size = new System.Drawing.Size(120, 21);
            this.styleComboBox.TabIndex = 1;
            this.styleComboBox.SelectedIndexChanged += new System.EventHandler(this.styleComboBox_SelectedIndexChanged);
            // 
            // label7
            // 
            this.label7.Location = new System.Drawing.Point(32, 136);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(64, 24);
            this.label7.TabIndex = 11;
            this.label7.Text = "&Fore color:";
            this.label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // foreColorButton
            // 
            this.foreColorButton.Location = new System.Drawing.Point(176, 136);
            this.foreColorButton.Name = "foreColorButton";
            this.foreColorButton.Size = new System.Drawing.Size(48, 22);
            this.foreColorButton.TabIndex = 13;
            this.foreColorButton.Text = "Select";
            this.foreColorButton.UseVisualStyleBackColor = true;
            this.foreColorButton.Click += new System.EventHandler(this.foreColorButton_Click);
            // 
            // foreColorLabel
            // 
            this.foreColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.foreColorLabel.Location = new System.Drawing.Point(104, 136);
            this.foreColorLabel.Name = "foreColorLabel";
            this.foreColorLabel.Size = new System.Drawing.Size(64, 22);
            this.foreColorLabel.TabIndex = 12;
            // 
            // label6
            // 
            this.label6.Location = new System.Drawing.Point(32, 160);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(64, 24);
            this.label6.TabIndex = 14;
            this.label6.Text = "&Back color:";
            this.label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // backColorButton
            // 
            this.backColorButton.Location = new System.Drawing.Point(176, 160);
            this.backColorButton.Name = "backColorButton";
            this.backColorButton.Size = new System.Drawing.Size(48, 22);
            this.backColorButton.TabIndex = 16;
            this.backColorButton.Text = "Select";
            this.backColorButton.UseVisualStyleBackColor = true;
            this.backColorButton.Click += new System.EventHandler(this.backColorButton_Click);
            // 
            // backColorLabel
            // 
            this.backColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.backColorLabel.Location = new System.Drawing.Point(104, 160);
            this.backColorLabel.Name = "backColorLabel";
            this.backColorLabel.Size = new System.Drawing.Size(64, 22);
            this.backColorLabel.TabIndex = 15;
            // 
            // marqueeSpeedButton
            // 
            this.marqueeSpeedButton.Location = new System.Drawing.Point(176, 40);
            this.marqueeSpeedButton.Name = "marqueeSpeedButton";
            this.marqueeSpeedButton.Size = new System.Drawing.Size(48, 22);
            this.marqueeSpeedButton.TabIndex = 4;
            this.marqueeSpeedButton.Text = "Set";
            this.marqueeSpeedButton.UseVisualStyleBackColor = true;
            this.marqueeSpeedButton.Click += new System.EventHandler(this.marqueeSpeedButton_Click);
            // 
            // marqueeSpeedTextBox
            // 
            this.marqueeSpeedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.marqueeSpeedTextBox.Location = new System.Drawing.Point(104, 40);
            this.marqueeSpeedTextBox.Name = "marqueeSpeedTextBox";
            this.marqueeSpeedTextBox.Size = new System.Drawing.Size(64, 22);
            this.marqueeSpeedTextBox.TabIndex = 3;
            this.marqueeSpeedTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label5
            // 
            this.label5.Location = new System.Drawing.Point(8, 40);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(88, 22);
            this.label5.TabIndex = 2;
            this.label5.Text = "Marq&uee speed:";
            this.label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // endColorLabel
            // 
            this.endColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.endColorLabel.Location = new System.Drawing.Point(96, 88);
            this.endColorLabel.Name = "endColorLabel";
            this.endColorLabel.Size = new System.Drawing.Size(64, 22);
            this.endColorLabel.TabIndex = 8;
            // 
            // endColorButton
            // 
            this.endColorButton.Location = new System.Drawing.Point(168, 88);
            this.endColorButton.Name = "endColorButton";
            this.endColorButton.Size = new System.Drawing.Size(48, 22);
            this.endColorButton.TabIndex = 9;
            this.endColorButton.Text = "Select";
            this.endColorButton.UseVisualStyleBackColor = true;
            this.endColorButton.Click += new System.EventHandler(this.endColorButton_Click);
            // 
            // label8
            // 
            this.label8.Location = new System.Drawing.Point(8, 88);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(80, 24);
            this.label8.TabIndex = 7;
            this.label8.Text = "End color:";
            this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // startColorLabel
            // 
            this.startColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.startColorLabel.Location = new System.Drawing.Point(96, 64);
            this.startColorLabel.Name = "startColorLabel";
            this.startColorLabel.Size = new System.Drawing.Size(64, 22);
            this.startColorLabel.TabIndex = 5;
            // 
            // startColorButton
            // 
            this.startColorButton.Location = new System.Drawing.Point(168, 64);
            this.startColorButton.Name = "startColorButton";
            this.startColorButton.Size = new System.Drawing.Size(48, 22);
            this.startColorButton.TabIndex = 6;
            this.startColorButton.Text = "Select";
            this.startColorButton.UseVisualStyleBackColor = true;
            this.startColorButton.Click += new System.EventHandler(this.startColorButton_Click);
            // 
            // label10
            // 
            this.label10.Location = new System.Drawing.Point(8, 64);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(80, 24);
            this.label10.TabIndex = 4;
            this.label10.Text = "Start color:";
            this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // wallColorLabel
            // 
            this.wallColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.wallColorLabel.Location = new System.Drawing.Point(96, 160);
            this.wallColorLabel.Name = "wallColorLabel";
            this.wallColorLabel.Size = new System.Drawing.Size(64, 22);
            this.wallColorLabel.TabIndex = 17;
            // 
            // wallColorButton
            // 
            this.wallColorButton.Location = new System.Drawing.Point(168, 160);
            this.wallColorButton.Name = "wallColorButton";
            this.wallColorButton.Size = new System.Drawing.Size(48, 22);
            this.wallColorButton.TabIndex = 18;
            this.wallColorButton.Text = "Select";
            this.wallColorButton.UseVisualStyleBackColor = true;
            this.wallColorButton.Click += new System.EventHandler(this.wallColorButton_Click);
            // 
            // label11
            // 
            this.label11.Location = new System.Drawing.Point(8, 160);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(80, 24);
            this.label11.TabIndex = 16;
            this.label11.Text = "&Wall color:";
            this.label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label9
            // 
            this.label9.Location = new System.Drawing.Point(8, 136);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(80, 22);
            this.label9.TabIndex = 13;
            this.label9.Text = "Wall &size:";
            this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // wallSizeTextBox
            // 
            this.wallSizeTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.wallSizeTextBox.Location = new System.Drawing.Point(96, 136);
            this.wallSizeTextBox.Name = "wallSizeTextBox";
            this.wallSizeTextBox.Size = new System.Drawing.Size(64, 22);
            this.wallSizeTextBox.TabIndex = 14;
            this.wallSizeTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // wallSizeButton
            // 
            this.wallSizeButton.Location = new System.Drawing.Point(168, 136);
            this.wallSizeButton.Name = "wallSizeButton";
            this.wallSizeButton.Size = new System.Drawing.Size(48, 22);
            this.wallSizeButton.TabIndex = 15;
            this.wallSizeButton.Text = "Set";
            this.wallSizeButton.UseVisualStyleBackColor = true;
            this.wallSizeButton.Click += new System.EventHandler(this.wallSizeButton_Click);
            // 
            // mazeStyleComboBox
            // 
            this.mazeStyleComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.mazeStyleComboBox.FormattingEnabled = true;
            this.mazeStyleComboBox.Items.AddRange(new object[] {
            "SingleRight",
            "SingleLeft",
            "SingleUp",
            "SingleDown",
            "SplitConvergeHorizontal",
            "SplitConvergeVertical",
            "SplitDivergeHorizontal",
            "SplitDivergeVertical"});
            this.mazeStyleComboBox.Location = new System.Drawing.Point(96, 16);
            this.mazeStyleComboBox.Name = "mazeStyleComboBox";
            this.mazeStyleComboBox.Size = new System.Drawing.Size(120, 21);
            this.mazeStyleComboBox.TabIndex = 1;
            this.mazeStyleComboBox.SelectedIndexChanged += new System.EventHandler(this.mazeStyleComboBox_SelectedIndexChanged);
            // 
            // label12
            // 
            this.label12.Location = new System.Drawing.Point(8, 16);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(80, 22);
            this.label12.TabIndex = 0;
            this.label12.Text = "Maze style:";
            this.label12.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // newGroupBox
            // 
            this.newGroupBox.Controls.Add(this.borderRoundCheckBox);
            this.newGroupBox.Controls.Add(this.infoLabel);
            this.newGroupBox.Controls.Add(this.borderGradientCheckBox);
            this.newGroupBox.Controls.Add(this.gradientComboBox);
            this.newGroupBox.Controls.Add(this.label18);
            this.newGroupBox.Controls.Add(this.label13);
            this.newGroupBox.Controls.Add(this.rowCountButton);
            this.newGroupBox.Controls.Add(this.regenButton);
            this.newGroupBox.Controls.Add(this.rowCountTextBox);
            this.newGroupBox.Controls.Add(this.label16);
            this.newGroupBox.Controls.Add(this.borderSizeTextBox);
            this.newGroupBox.Controls.Add(this.borderSizeButton);
            this.newGroupBox.Controls.Add(this.borderColorLabel);
            this.newGroupBox.Controls.Add(this.borderColorButton);
            this.newGroupBox.Controls.Add(this.label17);
            this.newGroupBox.Controls.Add(this.label10);
            this.newGroupBox.Controls.Add(this.mazeStyleComboBox);
            this.newGroupBox.Controls.Add(this.label12);
            this.newGroupBox.Controls.Add(this.startColorButton);
            this.newGroupBox.Controls.Add(this.label9);
            this.newGroupBox.Controls.Add(this.startColorLabel);
            this.newGroupBox.Controls.Add(this.wallSizeTextBox);
            this.newGroupBox.Controls.Add(this.label8);
            this.newGroupBox.Controls.Add(this.wallSizeButton);
            this.newGroupBox.Controls.Add(this.endColorButton);
            this.newGroupBox.Controls.Add(this.wallColorLabel);
            this.newGroupBox.Controls.Add(this.endColorLabel);
            this.newGroupBox.Controls.Add(this.wallColorButton);
            this.newGroupBox.Controls.Add(this.label11);
            this.newGroupBox.Location = new System.Drawing.Point(264, 8);
            this.newGroupBox.Name = "newGroupBox";
            this.newGroupBox.Size = new System.Drawing.Size(224, 328);
            this.newGroupBox.TabIndex = 1;
            this.newGroupBox.TabStop = false;
            // 
            // borderRoundCheckBox
            // 
            this.borderRoundCheckBox.Location = new System.Drawing.Point(152, 240);
            this.borderRoundCheckBox.Name = "borderRoundCheckBox";
            this.borderRoundCheckBox.Size = new System.Drawing.Size(64, 48);
            this.borderRoundCheckBox.TabIndex = 27;
            this.borderRoundCheckBox.Text = "Border round corners";
            this.borderRoundCheckBox.UseVisualStyleBackColor = true;
            this.borderRoundCheckBox.CheckedChanged += new System.EventHandler(this.borderRoundCheckBox_CheckedChanged);
            // 
            // infoLabel
            // 
            this.infoLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.infoLabel.Location = new System.Drawing.Point(8, 296);
            this.infoLabel.Name = "infoLabel";
            this.infoLabel.Size = new System.Drawing.Size(208, 23);
            this.infoLabel.TabIndex = 28;
            this.infoLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // borderGradientCheckBox
            // 
            this.borderGradientCheckBox.Location = new System.Drawing.Point(80, 240);
            this.borderGradientCheckBox.Name = "borderGradientCheckBox";
            this.borderGradientCheckBox.Size = new System.Drawing.Size(64, 48);
            this.borderGradientCheckBox.TabIndex = 26;
            this.borderGradientCheckBox.Text = "Border gradient coloring";
            this.borderGradientCheckBox.UseVisualStyleBackColor = true;
            this.borderGradientCheckBox.CheckedChanged += new System.EventHandler(this.borderGradientCheckBox_CheckedChanged);
            // 
            // gradientComboBox
            // 
            this.gradientComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.gradientComboBox.FormattingEnabled = true;
            this.gradientComboBox.Items.AddRange(new object[] {
            "None",
            "Rows",
            "Columns",
            "Flow"});
            this.gradientComboBox.Location = new System.Drawing.Point(96, 40);
            this.gradientComboBox.Name = "gradientComboBox";
            this.gradientComboBox.Size = new System.Drawing.Size(120, 21);
            this.gradientComboBox.TabIndex = 3;
            this.gradientComboBox.SelectedIndexChanged += new System.EventHandler(this.gradientComboBox_SelectedIndexChanged);
            // 
            // label18
            // 
            this.label18.Location = new System.Drawing.Point(8, 40);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(80, 22);
            this.label18.TabIndex = 2;
            this.label18.Text = "Gradient type:";
            this.label18.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // label13
            // 
            this.label13.Location = new System.Drawing.Point(8, 112);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(80, 22);
            this.label13.TabIndex = 10;
            this.label13.Text = "&Row count:";
            this.label13.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // rowCountButton
            // 
            this.rowCountButton.Location = new System.Drawing.Point(168, 112);
            this.rowCountButton.Name = "rowCountButton";
            this.rowCountButton.Size = new System.Drawing.Size(48, 22);
            this.rowCountButton.TabIndex = 12;
            this.rowCountButton.Text = "Set";
            this.rowCountButton.UseVisualStyleBackColor = true;
            this.rowCountButton.Click += new System.EventHandler(this.rowCountButton_Click);
            // 
            // regenButton
            // 
            this.regenButton.Location = new System.Drawing.Point(8, 240);
            this.regenButton.Name = "regenButton";
            this.regenButton.Size = new System.Drawing.Size(64, 48);
            this.regenButton.TabIndex = 25;
            this.regenButton.Text = "New Maze";
            this.regenButton.UseVisualStyleBackColor = true;
            this.regenButton.Click += new System.EventHandler(this.regenButton_Click);
            // 
            // rowCountTextBox
            // 
            this.rowCountTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.rowCountTextBox.Location = new System.Drawing.Point(96, 112);
            this.rowCountTextBox.Name = "rowCountTextBox";
            this.rowCountTextBox.Size = new System.Drawing.Size(64, 22);
            this.rowCountTextBox.TabIndex = 11;
            this.rowCountTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // label16
            // 
            this.label16.Location = new System.Drawing.Point(8, 184);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(80, 22);
            this.label16.TabIndex = 19;
            this.label16.Text = "Border size:";
            this.label16.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // borderSizeTextBox
            // 
            this.borderSizeTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.borderSizeTextBox.Location = new System.Drawing.Point(96, 184);
            this.borderSizeTextBox.Name = "borderSizeTextBox";
            this.borderSizeTextBox.Size = new System.Drawing.Size(64, 22);
            this.borderSizeTextBox.TabIndex = 20;
            this.borderSizeTextBox.TextChanged += new System.EventHandler(this.TextBox_TextChanged);
            // 
            // borderSizeButton
            // 
            this.borderSizeButton.Location = new System.Drawing.Point(168, 184);
            this.borderSizeButton.Name = "borderSizeButton";
            this.borderSizeButton.Size = new System.Drawing.Size(48, 22);
            this.borderSizeButton.TabIndex = 21;
            this.borderSizeButton.Text = "Set";
            this.borderSizeButton.UseVisualStyleBackColor = true;
            this.borderSizeButton.Click += new System.EventHandler(this.borderSizeButton_Click);
            // 
            // borderColorLabel
            // 
            this.borderColorLabel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.borderColorLabel.Location = new System.Drawing.Point(96, 208);
            this.borderColorLabel.Name = "borderColorLabel";
            this.borderColorLabel.Size = new System.Drawing.Size(64, 22);
            this.borderColorLabel.TabIndex = 23;
            // 
            // borderColorButton
            // 
            this.borderColorButton.Location = new System.Drawing.Point(168, 208);
            this.borderColorButton.Name = "borderColorButton";
            this.borderColorButton.Size = new System.Drawing.Size(48, 22);
            this.borderColorButton.TabIndex = 24;
            this.borderColorButton.Text = "Select";
            this.borderColorButton.UseVisualStyleBackColor = true;
            this.borderColorButton.Click += new System.EventHandler(this.borderColorButton_Click);
            // 
            // label17
            // 
            this.label17.Location = new System.Drawing.Point(8, 208);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(80, 24);
            this.label17.TabIndex = 22;
            this.label17.Text = "Border color:";
            this.label17.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // valueGroupBox
            // 
            this.valueGroupBox.Controls.Add(this.plus3RadioButton);
            this.valueGroupBox.Controls.Add(this.plus2RadioButton);
            this.valueGroupBox.Controls.Add(this.plus1RadioButton);
            this.valueGroupBox.Controls.Add(this.stopRadioButton);
            this.valueGroupBox.Controls.Add(this.minus1RadioButton);
            this.valueGroupBox.Controls.Add(this.minus2RadioButton);
            this.valueGroupBox.Controls.Add(this.minus3RadioButton);
            this.valueGroupBox.Location = new System.Drawing.Point(16, 280);
            this.valueGroupBox.Name = "valueGroupBox";
            this.valueGroupBox.Size = new System.Drawing.Size(232, 56);
            this.valueGroupBox.TabIndex = 2;
            this.valueGroupBox.TabStop = false;
            this.valueGroupBox.Text = " Change Value automatically ";
            // 
            // plus3RadioButton
            // 
            this.plus3RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.plus3RadioButton.Location = new System.Drawing.Point(184, 24);
            this.plus3RadioButton.Name = "plus3RadioButton";
            this.plus3RadioButton.Size = new System.Drawing.Size(40, 24);
            this.plus3RadioButton.TabIndex = 13;
            this.plus3RadioButton.TabStop = true;
            this.plus3RadioButton.Text = ">>>";
            this.plus3RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.plus3RadioButton.UseVisualStyleBackColor = true;
            this.plus3RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // plus2RadioButton
            // 
            this.plus2RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.plus2RadioButton.Location = new System.Drawing.Point(152, 24);
            this.plus2RadioButton.Name = "plus2RadioButton";
            this.plus2RadioButton.Size = new System.Drawing.Size(32, 24);
            this.plus2RadioButton.TabIndex = 12;
            this.plus2RadioButton.TabStop = true;
            this.plus2RadioButton.Text = ">>";
            this.plus2RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.plus2RadioButton.UseVisualStyleBackColor = true;
            this.plus2RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // plus1RadioButton
            // 
            this.plus1RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.plus1RadioButton.Location = new System.Drawing.Point(128, 24);
            this.plus1RadioButton.Name = "plus1RadioButton";
            this.plus1RadioButton.Size = new System.Drawing.Size(24, 24);
            this.plus1RadioButton.TabIndex = 11;
            this.plus1RadioButton.TabStop = true;
            this.plus1RadioButton.Text = ">";
            this.plus1RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.plus1RadioButton.UseVisualStyleBackColor = true;
            this.plus1RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // stopRadioButton
            // 
            this.stopRadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.stopRadioButton.Location = new System.Drawing.Point(104, 24);
            this.stopRadioButton.Name = "stopRadioButton";
            this.stopRadioButton.Size = new System.Drawing.Size(24, 24);
            this.stopRadioButton.TabIndex = 10;
            this.stopRadioButton.TabStop = true;
            this.stopRadioButton.Text = "--";
            this.stopRadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.stopRadioButton.UseVisualStyleBackColor = true;
            this.stopRadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // minus1RadioButton
            // 
            this.minus1RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.minus1RadioButton.Location = new System.Drawing.Point(80, 24);
            this.minus1RadioButton.Name = "minus1RadioButton";
            this.minus1RadioButton.Size = new System.Drawing.Size(24, 24);
            this.minus1RadioButton.TabIndex = 9;
            this.minus1RadioButton.TabStop = true;
            this.minus1RadioButton.Text = "<";
            this.minus1RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.minus1RadioButton.UseVisualStyleBackColor = true;
            this.minus1RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // minus2RadioButton
            // 
            this.minus2RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.minus2RadioButton.Location = new System.Drawing.Point(48, 24);
            this.minus2RadioButton.Name = "minus2RadioButton";
            this.minus2RadioButton.Size = new System.Drawing.Size(32, 24);
            this.minus2RadioButton.TabIndex = 8;
            this.minus2RadioButton.TabStop = true;
            this.minus2RadioButton.Text = "<<";
            this.minus2RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.minus2RadioButton.UseVisualStyleBackColor = true;
            this.minus2RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // minus3RadioButton
            // 
            this.minus3RadioButton.Appearance = System.Windows.Forms.Appearance.Button;
            this.minus3RadioButton.Location = new System.Drawing.Point(8, 24);
            this.minus3RadioButton.Name = "minus3RadioButton";
            this.minus3RadioButton.Size = new System.Drawing.Size(40, 24);
            this.minus3RadioButton.TabIndex = 7;
            this.minus3RadioButton.TabStop = true;
            this.minus3RadioButton.Text = "<<<";
            this.minus3RadioButton.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.minus3RadioButton.UseVisualStyleBackColor = true;
            this.minus3RadioButton.CheckedChanged += new System.EventHandler(this.speedChange);
            // 
            // autoModeTimer
            // 
            this.autoModeTimer.Interval = 1000;
            this.autoModeTimer.Tick += new System.EventHandler(this.autoModeTimer_Tick);
            // 
            // amazing
            // 
            this.amazing.BorderColor = System.Drawing.Color.Red;
            this.amazing.BorderGradient = false;
            this.amazing.BorderRoundCorners = false;
            this.amazing.BorderSize = 0;
            this.amazing.Gradient = GAW.AmazingProgressBar.GradientType.None;
            this.amazing.GradientEndColor = System.Drawing.Color.Lime;
            this.amazing.GradientStartColor = System.Drawing.Color.PaleGreen;
            this.amazing.Location = new System.Drawing.Point(24, 352);
            this.amazing.MarqueeAnimationSpeed = 1000;
            this.amazing.Maximum = 183;
            this.amazing.MazeStyle = GAW.AmazingProgressBar.MazeStyleType.SingleRight;
            this.amazing.Name = "amazing";
            this.amazing.RowCount = 4;
            this.amazing.Size = new System.Drawing.Size(456, 32);
            this.amazing.Step = 1;
            this.amazing.Style = System.Windows.Forms.ProgressBarStyle.Continuous;
            this.amazing.TabIndex = 3;
            this.amazing.UnusedColor = System.Drawing.SystemColors.Control;
            this.amazing.Value = 31;
            this.amazing.WallColor = System.Drawing.Color.Black;
            this.amazing.WallSize = 1;
            this.amazing.MazeChanged += new System.EventHandler(this.amazing_MazeChanged);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(505, 403);
            this.Controls.Add(this.amazing);
            this.Controls.Add(this.valueGroupBox);
            this.Controls.Add(this.newGroupBox);
            this.Controls.Add(this.origGroupBox);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainForm";
            this.Text = "AmazingProgressBar Explorer";
            this.SizeChanged += new System.EventHandler(this.MainForm_SizeChanged);
            this.origGroupBox.ResumeLayout(false);
            this.origGroupBox.PerformLayout();
            this.newGroupBox.ResumeLayout(false);
            this.newGroupBox.PerformLayout();
            this.valueGroupBox.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private GAW.AmazingProgressBar amazing;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox minTextBox;
        private System.Windows.Forms.Button minButton;
        private System.Windows.Forms.Button maxButton;
        private System.Windows.Forms.TextBox maxTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button valueButton;
        private System.Windows.Forms.TextBox valueTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.GroupBox origGroupBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox styleComboBox;
        private System.Windows.Forms.Label foreColorLabel;
        private System.Windows.Forms.Button foreColorButton;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label backColorLabel;
        private System.Windows.Forms.Button backColorButton;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label endColorLabel;
        private System.Windows.Forms.Button endColorButton;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Label startColorLabel;
        private System.Windows.Forms.Button startColorButton;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox marqueeSpeedTextBox;
        private System.Windows.Forms.Button marqueeSpeedButton;
        private System.Windows.Forms.Label wallColorLabel;
        private System.Windows.Forms.Button wallColorButton;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox wallSizeTextBox;
        private System.Windows.Forms.Button wallSizeButton;
        private System.Windows.Forms.ComboBox mazeStyleComboBox;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.GroupBox newGroupBox;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.TextBox rowCountTextBox;
        private System.Windows.Forms.Button rowCountButton;
        private System.Windows.Forms.Button widthButton;
        private System.Windows.Forms.TextBox widthTextBox;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Button heightButton;
        private System.Windows.Forms.TextBox heightTextBox;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.GroupBox valueGroupBox;
        private System.Windows.Forms.Timer autoModeTimer;
        private System.Windows.Forms.Label borderColorLabel;
        private System.Windows.Forms.Button borderColorButton;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Button regenButton;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.TextBox borderSizeTextBox;
        private System.Windows.Forms.Button borderSizeButton;
        private System.Windows.Forms.ComboBox gradientComboBox;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.RadioButton minus3RadioButton;
        private System.Windows.Forms.RadioButton plus3RadioButton;
        private System.Windows.Forms.RadioButton plus2RadioButton;
        private System.Windows.Forms.RadioButton plus1RadioButton;
        private System.Windows.Forms.RadioButton stopRadioButton;
        private System.Windows.Forms.RadioButton minus1RadioButton;
        private System.Windows.Forms.RadioButton minus2RadioButton;
        private System.Windows.Forms.Button rotateButton;
        private System.Windows.Forms.CheckBox borderGradientCheckBox;
        private System.Windows.Forms.Label infoLabel;
        private System.Windows.Forms.CheckBox borderRoundCheckBox;
    }
}

