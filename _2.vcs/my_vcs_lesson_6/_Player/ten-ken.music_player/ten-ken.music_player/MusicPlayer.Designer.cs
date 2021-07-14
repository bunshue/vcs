using System.Windows.Forms;

namespace KenMusicPlayer
{
    partial class MusicPlayer
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MusicPlayer));
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.tsmiFile = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiLoading = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiClear = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiXuanXiang = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiPlayer = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiWaiting = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiStop = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiSet = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiDanQu = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiXunHuan = new System.Windows.Forms.ToolStripMenuItem();
            this.tsmiExit = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileDialog1 = new System.Windows.Forms.OpenFileDialog();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.panel1 = new System.Windows.Forms.Panel();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.lvDetail = new System.Windows.Forms.ListView();
            this.columnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.columnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.panel3 = new System.Windows.Forms.Panel();
            this.label2 = new System.Windows.Forms.Label();
            this.lrcShow = new System.Windows.Forms.Label();
            this.ComboBoxSkinSelect = new CCWin.SkinControl.SkinComboBox();
            this.skinComboBoxFontSize = new CCWin.SkinControl.SkinComboBox();
            this.skinComboBoxFontName = new CCWin.SkinControl.SkinComboBox();
            this.skinButton3 = new CCWin.SkinControl.SkinButton();
            this.skinButton5 = new CCWin.SkinControl.SkinButton();
            this.skinButton4 = new CCWin.SkinControl.SkinButton();
            this.panel2 = new System.Windows.Forms.Panel();
            this.playerType = new CCWin.SkinControl.SkinComboBox();
            this.skinButton2 = new CCWin.SkinControl.SkinButton();
            this.skinButton1 = new CCWin.SkinControl.SkinButton();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.timerImgs = new System.Windows.Forms.Timer(this.components);
            this.skinButtonClose = new CCWin.SkinControl.SkinButton();
            this.richTextBox2 = new System.Windows.Forms.RichTextBox();
            this.menuStrip1.SuspendLayout();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.panel3.SuspendLayout();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiFile,
            this.tsmiXuanXiang,
            this.tsmiSet,
            this.tsmiExit});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(833, 25);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            this.menuStrip1.Visible = false;
            // 
            // tsmiFile
            // 
            this.tsmiFile.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiLoading,
            this.tsmiClear});
            this.tsmiFile.Name = "tsmiFile";
            this.tsmiFile.Size = new System.Drawing.Size(57, 21);
            this.tsmiFile.Text = "文件(&F)";
            // 
            // tsmiLoading
            // 
            this.tsmiLoading.Name = "tsmiLoading";
            this.tsmiLoading.Size = new System.Drawing.Size(160, 22);
            this.tsmiLoading.Text = "导入音乐文件(&L)";
            this.tsmiLoading.Click += new System.EventHandler(this.tsmiLoading_Click);
            // 
            // tsmiClear
            // 
            this.tsmiClear.Name = "tsmiClear";
            this.tsmiClear.Size = new System.Drawing.Size(160, 22);
            this.tsmiClear.Text = "清空(&C)";
            this.tsmiClear.Click += new System.EventHandler(this.ListViewClear_Click);
            // 
            // tsmiXuanXiang
            // 
            this.tsmiXuanXiang.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiPlayer,
            this.tsmiWaiting,
            this.tsmiStop});
            this.tsmiXuanXiang.Name = "tsmiXuanXiang";
            this.tsmiXuanXiang.Size = new System.Drawing.Size(59, 21);
            this.tsmiXuanXiang.Text = "选项(&X)";
            this.tsmiXuanXiang.Visible = false;
            // 
            // tsmiPlayer
            // 
            this.tsmiPlayer.Name = "tsmiPlayer";
            this.tsmiPlayer.Size = new System.Drawing.Size(118, 22);
            this.tsmiPlayer.Text = "播放(&B)";
            this.tsmiPlayer.Click += new System.EventHandler(this.tsmiPlayer_Click);
            // 
            // tsmiWaiting
            // 
            this.tsmiWaiting.Name = "tsmiWaiting";
            this.tsmiWaiting.Size = new System.Drawing.Size(118, 22);
            this.tsmiWaiting.Text = "暂停(&W)";
            this.tsmiWaiting.Click += new System.EventHandler(this.tsmiWaiting_Click);
            // 
            // tsmiStop
            // 
            this.tsmiStop.Name = "tsmiStop";
            this.tsmiStop.Size = new System.Drawing.Size(118, 22);
            this.tsmiStop.Text = "停止(&S)";
            this.tsmiStop.Click += new System.EventHandler(this.tsmiStop_Click);
            // 
            // tsmiSet
            // 
            this.tsmiSet.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.tsmiDanQu,
            this.tsmiXunHuan});
            this.tsmiSet.Name = "tsmiSet";
            this.tsmiSet.Size = new System.Drawing.Size(58, 21);
            this.tsmiSet.Text = "设置(&S)";
            // 
            // tsmiDanQu
            // 
            this.tsmiDanQu.Checked = true;
            this.tsmiDanQu.CheckOnClick = true;
            this.tsmiDanQu.CheckState = System.Windows.Forms.CheckState.Checked;
            this.tsmiDanQu.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Text;
            this.tsmiDanQu.Name = "tsmiDanQu";
            this.tsmiDanQu.Size = new System.Drawing.Size(139, 22);
            this.tsmiDanQu.Text = "顺序播放(&D)";
            this.tsmiDanQu.Click += new System.EventHandler(this.tsmiDanQu_Click);
            // 
            // tsmiXunHuan
            // 
            this.tsmiXunHuan.CheckOnClick = true;
            this.tsmiXunHuan.Name = "tsmiXunHuan";
            this.tsmiXunHuan.Size = new System.Drawing.Size(139, 22);
            this.tsmiXunHuan.Text = "循环播放(&X)";
            this.tsmiXunHuan.Click += new System.EventHandler(this.tsmiXunHuan_Click);
            // 
            // tsmiExit
            // 
            this.tsmiExit.Name = "tsmiExit";
            this.tsmiExit.Size = new System.Drawing.Size(58, 21);
            this.tsmiExit.Text = "退出(&E)";
            this.tsmiExit.Click += new System.EventHandler(this.tsmiExit_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.splitContainer1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(4, 34);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1021, 529);
            this.panel1.TabIndex = 3;
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.lvDetail);
            this.splitContainer1.Panel1.Controls.Add(this.panel3);
            this.splitContainer1.Panel1.Controls.Add(this.panel2);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.richTextBox2);
            this.splitContainer1.Panel2.Controls.Add(this.pictureBox1);
            this.splitContainer1.Panel2.Controls.Add(this.label1);
            this.splitContainer1.Size = new System.Drawing.Size(1021, 529);
            this.splitContainer1.SplitterDistance = 252;
            this.splitContainer1.TabIndex = 0;
            // 
            // lvDetail
            // 
            this.lvDetail.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeader1,
            this.columnHeader2});
            this.lvDetail.Dock = System.Windows.Forms.DockStyle.Fill;
            this.lvDetail.FullRowSelect = true;
            this.lvDetail.HideSelection = false;
            this.lvDetail.Location = new System.Drawing.Point(0, 28);
            this.lvDetail.MultiSelect = false;
            this.lvDetail.Name = "lvDetail";
            this.lvDetail.Scrollable = false;
            this.lvDetail.ShowGroups = false;
            this.lvDetail.Size = new System.Drawing.Size(252, 441);
            this.lvDetail.TabIndex = 8;
            this.lvDetail.UseCompatibleStateImageBehavior = false;
            this.lvDetail.View = System.Windows.Forms.View.Details;
            this.lvDetail.KeyDown += new System.Windows.Forms.KeyEventHandler(this.lvDetail_KeyDown);
            this.lvDetail.MouseClick += new System.Windows.Forms.MouseEventHandler(this.lvDetail_MouseDoubleClick);
            // 
            // columnHeader1
            // 
            this.columnHeader1.Text = "序号";
            this.columnHeader1.Width = 92;
            // 
            // columnHeader2
            // 
            this.columnHeader2.Text = "文件名";
            this.columnHeader2.Width = 168;
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.label2);
            this.panel3.Controls.Add(this.lrcShow);
            this.panel3.Controls.Add(this.ComboBoxSkinSelect);
            this.panel3.Controls.Add(this.skinComboBoxFontSize);
            this.panel3.Controls.Add(this.skinComboBoxFontName);
            this.panel3.Controls.Add(this.skinButton3);
            this.panel3.Controls.Add(this.skinButton5);
            this.panel3.Controls.Add(this.skinButton4);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.panel3.Location = new System.Drawing.Point(0, 469);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(252, 60);
            this.panel3.TabIndex = 3;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("宋体", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.label2.ForeColor = System.Drawing.Color.SandyBrown;
            this.label2.Location = new System.Drawing.Point(106, 38);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 12);
            this.label2.TabIndex = 19;
            this.label2.Text = "皮肤:";
            // 
            // lrcShow
            // 
            this.lrcShow.AutoSize = true;
            this.lrcShow.Font = new System.Drawing.Font("宋体", 9F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(134)));
            this.lrcShow.ForeColor = System.Drawing.Color.DarkOrange;
            this.lrcShow.Location = new System.Drawing.Point(11, 38);
            this.lrcShow.Name = "lrcShow";
            this.lrcShow.Size = new System.Drawing.Size(38, 12);
            this.lrcShow.TabIndex = 19;
            this.lrcShow.Text = "歌词:";
            // 
            // ComboBoxSkinSelect
            // 
            this.ComboBoxSkinSelect.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.ComboBoxSkinSelect.FormattingEnabled = true;
            this.ComboBoxSkinSelect.Items.AddRange(new object[] {
            "渐变黑",
            "天蓝色",
            "墨绿色",
            "浅灰色",
            "蓝色",
            "亮色"});
            this.ComboBoxSkinSelect.Location = new System.Drawing.Point(147, 32);
            this.ComboBoxSkinSelect.Name = "ComboBoxSkinSelect";
            this.ComboBoxSkinSelect.Size = new System.Drawing.Size(72, 23);
            this.ComboBoxSkinSelect.TabIndex = 18;
            this.ComboBoxSkinSelect.WaterText = "";
            this.ComboBoxSkinSelect.SelectedIndexChanged += new System.EventHandler(this.ComboBoxSkinSelect_SelectedIndexChanged);
            // 
            // skinComboBoxFontSize
            // 
            this.skinComboBoxFontSize.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.skinComboBoxFontSize.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.skinComboBoxFontSize.FormattingEnabled = true;
            this.skinComboBoxFontSize.Items.AddRange(new object[] {
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30",
            "31"});
            this.skinComboBoxFontSize.Location = new System.Drawing.Point(171, 5);
            this.skinComboBoxFontSize.Name = "skinComboBoxFontSize";
            this.skinComboBoxFontSize.Size = new System.Drawing.Size(42, 23);
            this.skinComboBoxFontSize.TabIndex = 18;
            this.skinComboBoxFontSize.WaterText = "";
            this.skinComboBoxFontSize.SelectedIndexChanged += new System.EventHandler(this.skinComboBox1_SelectedIndexChanged);
            // 
            // skinComboBoxFontName
            // 
            this.skinComboBoxFontName.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.skinComboBoxFontName.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.skinComboBoxFontName.FormattingEnabled = true;
            this.skinComboBoxFontName.Items.AddRange(new object[] {
            "楷体",
            "宋体",
            "华文行楷"});
            this.skinComboBoxFontName.Location = new System.Drawing.Point(49, 5);
            this.skinComboBoxFontName.Name = "skinComboBoxFontName";
            this.skinComboBoxFontName.Size = new System.Drawing.Size(67, 23);
            this.skinComboBoxFontName.TabIndex = 18;
            this.skinComboBoxFontName.WaterText = "";
            this.skinComboBoxFontName.SelectedIndexChanged += new System.EventHandler(this.skinComboBoxFontName_SelectedIndexChanged);
            // 
            // skinButton3
            // 
            this.skinButton3.BackColor = System.Drawing.Color.Transparent;
            this.skinButton3.BaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.skinButton3.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButton3.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButton3.DownBack = null;
            this.skinButton3.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.skinButton3.Location = new System.Drawing.Point(123, 4);
            this.skinButton3.MouseBack = null;
            this.skinButton3.Name = "skinButton3";
            this.skinButton3.NormlBack = null;
            this.skinButton3.Size = new System.Drawing.Size(42, 23);
            this.skinButton3.TabIndex = 18;
            this.skinButton3.Text = "大小";
            this.skinButton3.UseVisualStyleBackColor = false;
            // 
            // skinButton5
            // 
            this.skinButton5.BackColor = System.Drawing.Color.Transparent;
            this.skinButton5.BaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.skinButton5.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButton5.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButton5.DownBack = null;
            this.skinButton5.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.skinButton5.Font = new System.Drawing.Font("宋体", 8.5F);
            this.skinButton5.Location = new System.Drawing.Point(48, 33);
            this.skinButton5.MouseBack = null;
            this.skinButton5.Name = "skinButton5";
            this.skinButton5.NormlBack = null;
            this.skinButton5.Size = new System.Drawing.Size(47, 21);
            this.skinButton5.TabIndex = 18;
            this.skinButton5.Text = "显示";
            this.skinButton5.UseVisualStyleBackColor = false;
            this.skinButton5.Click += new System.EventHandler(this.skinButton5_Click);
            // 
            // skinButton4
            // 
            this.skinButton4.BackColor = System.Drawing.Color.Transparent;
            this.skinButton4.BaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.skinButton4.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButton4.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButton4.DownBack = null;
            this.skinButton4.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.skinButton4.Font = new System.Drawing.Font("宋体", 8.5F);
            this.skinButton4.Location = new System.Drawing.Point(3, 5);
            this.skinButton4.MouseBack = null;
            this.skinButton4.Name = "skinButton4";
            this.skinButton4.NormlBack = null;
            this.skinButton4.Size = new System.Drawing.Size(41, 21);
            this.skinButton4.TabIndex = 18;
            this.skinButton4.Text = "字体";
            this.skinButton4.UseVisualStyleBackColor = false;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.playerType);
            this.panel2.Controls.Add(this.skinButton2);
            this.panel2.Controls.Add(this.skinButton1);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Top;
            this.panel2.Location = new System.Drawing.Point(0, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(252, 28);
            this.panel2.TabIndex = 2;
            // 
            // playerType
            // 
            this.playerType.DrawMode = System.Windows.Forms.DrawMode.OwnerDrawFixed;
            this.playerType.FormattingEnabled = true;
            this.playerType.Items.AddRange(new object[] {
            "顺序播放",
            "随机播放",
            "循环播放"});
            this.playerType.Location = new System.Drawing.Point(76, 3);
            this.playerType.Name = "playerType";
            this.playerType.Size = new System.Drawing.Size(143, 23);
            this.playerType.TabIndex = 18;
            this.playerType.WaterText = "";
            this.playerType.SelectedIndexChanged += new System.EventHandler(this.playerType_SelectedIndexChanged);
            // 
            // skinButton2
            // 
            this.skinButton2.BackColor = System.Drawing.Color.Transparent;
            this.skinButton2.BaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.skinButton2.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButton2.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButton2.DownBack = null;
            this.skinButton2.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.skinButton2.Location = new System.Drawing.Point(34, 3);
            this.skinButton2.MouseBack = null;
            this.skinButton2.Name = "skinButton2";
            this.skinButton2.NormlBack = null;
            this.skinButton2.Size = new System.Drawing.Size(23, 23);
            this.skinButton2.TabIndex = 18;
            this.skinButton2.Text = "-";
            this.skinButton2.UseVisualStyleBackColor = false;
            this.skinButton2.Click += new System.EventHandler(this.skinButton2_Click);
            // 
            // skinButton1
            // 
            this.skinButton1.BackColor = System.Drawing.Color.Transparent;
            this.skinButton1.BaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.skinButton1.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButton1.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButton1.DownBack = null;
            this.skinButton1.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.skinButton1.Location = new System.Drawing.Point(3, 3);
            this.skinButton1.MouseBack = null;
            this.skinButton1.Name = "skinButton1";
            this.skinButton1.NormlBack = null;
            this.skinButton1.Size = new System.Drawing.Size(22, 23);
            this.skinButton1.TabIndex = 18;
            this.skinButton1.Text = "+";
            this.skinButton1.UseVisualStyleBackColor = false;
            this.skinButton1.Click += new System.EventHandler(this.tsmiLoading_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(0, 0);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(448, 486);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 8;
            this.pictureBox1.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Italic);
            this.label1.ForeColor = System.Drawing.Color.Tomato;
            this.label1.Location = new System.Drawing.Point(0, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 25);
            this.label1.TabIndex = 2;
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.label1.Visible = false;
            // 
            // timerImgs
            // 
            this.timerImgs.Interval = 3500;
            this.timerImgs.Tick += new System.EventHandler(this.timerImgs_Tick);
            // 
            // skinButtonClose
            // 
            this.skinButtonClose.BackColor = System.Drawing.Color.Transparent;
            this.skinButtonClose.BaseColor = System.Drawing.Color.DeepSkyBlue;
            this.skinButtonClose.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.skinButtonClose.ControlState = CCWin.SkinClass.ControlState.Normal;
            this.skinButtonClose.DownBack = null;
            this.skinButtonClose.DownBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.skinButtonClose.Font = new System.Drawing.Font("宋体", 10F);
            this.skinButtonClose.ForeColor = System.Drawing.Color.Salmon;
            this.skinButtonClose.Location = new System.Drawing.Point(790, 7);
            this.skinButtonClose.MouseBack = null;
            this.skinButtonClose.MouseBaseColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.skinButtonClose.Name = "skinButtonClose";
            this.skinButtonClose.NormlBack = null;
            this.skinButtonClose.Size = new System.Drawing.Size(25, 21);
            this.skinButtonClose.TabIndex = 18;
            this.skinButtonClose.Text = "X";
            this.skinButtonClose.UseVisualStyleBackColor = false;
            this.skinButtonClose.Click += new System.EventHandler(this.skinButtonClose_Click);
            // 
            // richTextBox2
            // 
            this.richTextBox2.Location = new System.Drawing.Point(455, 5);
            this.richTextBox2.Name = "richTextBox2";
            this.richTextBox2.Size = new System.Drawing.Size(307, 481);
            this.richTextBox2.TabIndex = 9;
            this.richTextBox2.Text = "";
            // 
            // MusicPlayer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1029, 567);
            this.CloseDownBack = null;
            this.CloseMouseBack = null;
            this.CloseNormlBack = null;
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.skinButtonClose);
            this.Controls.Add(this.menuStrip1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MusicPlayer";
            this.ShadowColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(0)))));
            this.ShadowWidth = 6;
            this.ShowIcon = false;
            this.Text = "音乐播放器";
            this.TitleColor = System.Drawing.Color.White;
            this.Load += new System.EventHandler(this.MusicPlayer_Load);
            this.Resize += new System.EventHandler(this.MusicPlayer_Resize);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            this.splitContainer1.Panel2.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem tsmiFile;
        private System.Windows.Forms.ToolStripMenuItem tsmiLoading;
        private System.Windows.Forms.ToolStripMenuItem tsmiClear;
        private System.Windows.Forms.ToolStripMenuItem tsmiXuanXiang;
        private System.Windows.Forms.ToolStripMenuItem tsmiPlayer;
        private System.Windows.Forms.ToolStripMenuItem tsmiWaiting;
        private System.Windows.Forms.ToolStripMenuItem tsmiStop;
        private System.Windows.Forms.ToolStripMenuItem tsmiExit;
        private System.Windows.Forms.OpenFileDialog openFileDialog1;
        private System.Windows.Forms.ToolStripMenuItem tsmiSet;
        private System.Windows.Forms.ToolStripMenuItem tsmiDanQu;
        private System.Windows.Forms.ToolStripMenuItem tsmiXunHuan;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private AxWMPLib.AxWindowsMediaPlayer wmp;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel panel2;

        //透明歌词
        private TMForm lrcForm;
        //半透明窗口
        private BTMForm btmForm;
        private CCWin.SkinControl.SkinButton skinButton1;
        private CCWin.SkinControl.SkinButton skinButton2;
        private CCWin.SkinControl.SkinComboBox playerType;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.Panel panel3;
        private CCWin.SkinControl.SkinComboBox skinComboBoxFontName;
        private CCWin.SkinControl.SkinButton skinButton3;
        private CCWin.SkinControl.SkinButton skinButton4;
        private CCWin.SkinControl.SkinComboBox skinComboBoxFontSize;
        private CCWin.SkinControl.SkinButton skinButton5;
        private System.Windows.Forms.Label lrcShow;
        private System.Windows.Forms.ListView lvDetail;
        private System.Windows.Forms.ColumnHeader columnHeader1;
        private System.Windows.Forms.ColumnHeader columnHeader2;
        private System.Windows.Forms.Timer timerImgs;
        private System.Windows.Forms.Label label2;
        private CCWin.SkinControl.SkinComboBox ComboBoxSkinSelect;
        private KenRichTextBox richTextBox1;
        private CCWin.SkinControl.SkinButton skinButtonClose;
        private RichTextBox richTextBox2;
    }
}