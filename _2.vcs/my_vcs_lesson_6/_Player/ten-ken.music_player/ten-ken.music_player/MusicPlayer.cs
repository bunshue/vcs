using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using WMPLib;
using System.Media;
using System.IO;
using System.Text.RegularExpressions;
using AxWMPLib;
using System.Drawing.Drawing2D;
using CCWin;

namespace KenMusicPlayer
{
    public partial class MusicPlayer : Skin_DevExpress
    {


        public int index = 1;
        public int listIndex;
        private bool first_in = true;   //是否第一次进入歌词区域
        private bool showLrc = true;//默认显示歌词
        private int imageInd = 0;//播放的图片下标
        private List<string> imageList;//播放的图片
        private Point closePoint;//关闭按钮的位置
        private Size dfSize;//最初的位置
        private int count;//歌曲显示次数

        //声音
        SoundPlayer player = new SoundPlayer();
        Dictionary<string, string> dic = new Dictionary<string, string>();

        //播放列表
        Dictionary<string, IWMPMedia> playListDict = new Dictionary<string, IWMPMedia>();

        List<string> al = new List<string>(); //当前歌词时间表     

        IWMPMedia media;

        /*
    *下面这一大段API调用，主要是用来设置歌词窗口的滚动条的
    *但其实后面，我并没有怎么用到，只是在将滚动条滚动到底部时，用了一下
    */
        private const int WM_VSCROLL = 0x115;
        // Scroll Bar Constants
        private const int SB_HORZ = 0;
        private const int SB_VERT = 1;
        private const int SB_CTL = 2;
        private const int SB_BOTH = 3;

        // Scroll Bar Commands
        private const int SB_LINEUP = 0;
        private const int SB_LINELEFT = 0;
        private const int SB_LINEDOWN = 1;
        private const int SB_LINERIGHT = 1;
        private const int SB_PAGEUP = 2;
        private const int SB_PAGELEFT = 2;
        private const int SB_PAGEDOWN = 3;
        private const int SB_PAGERIGHT = 3;
        private const int SB_THUMBPOSITION = 4;
        private const int SB_THUMBTRACK = 5;
        private const int SB_TOP = 6;
        private const int SB_LEFT = 6;
        private const int SB_BOTTOM = 7;
        private const int SB_RIGHT = 7;
        private const int SB_ENDSCROLL = 8;
        private const int WM_PAINT = 0x000F;


        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern bool ScrollWindow(IntPtr hWnd, int XAmount, int YAmount, ref Rectangle lpRect, ref Rectangle lpClipRect);

        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int SetScrollPos(IntPtr hwnd, int nBar, int nPos, bool bRedraw);

        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int SetScrollPos(int nBar, int nPos, bool bRedraw);

        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int GetScrollPos(IntPtr hwnd, int nBar);


        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern bool UpdateWindow(IntPtr hWnd);

        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public static extern int SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);

        public void setWord()
        {
           
        }


        public MusicPlayer()
        {
            this.StartPosition = FormStartPosition.CenterScreen;//窗口居中显示
            InitializeComponent();
        }


        private void MusicPlayer_Load(object sender, EventArgs e)
        {
            InitLoad();
        }


        /// <summary>
        ///  初始化 加载播放列表 如歌词 背景图 定时器等等
        /// </summary>
        private void InitLoad()
        {
            try
            {
                bool flag = false;
                string folder = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "bgImages");
                DirectoryInfo root = new DirectoryInfo(folder);
                FileInfo[] files = root.GetFiles();
                string fileName;
                for (int i = 0; i < files.Length; i++)
                {
                    fileName = files[i].Name.ToLower();
                    if (fileName.EndsWith(".png") || fileName.EndsWith(".jpeg") || fileName.EndsWith(".jpg"))
                    {
                        if (!flag)
                        {
                            imageList = new List<string>();
                            this.pictureBox1.Image = Image.FromFile(files[i].FullName);
                        }
                        imageList.Add(files[i].FullName);
                        flag = true;
                    }
                }

                playerType.Text = playerType.Items[0].ToString();//默认第一个
                closePoint = this.skinButtonClose.Location;
                dfSize = this.Size;
                richTextBox1.BackColor = this.TransparencyKey;
                skinComboBoxFontName.Text = skinComboBoxFontName.Items[0].ToString();//默认第一个
                skinComboBoxFontSize.Text = skinComboBoxFontSize.Items[0].ToString();//默认第一个
                ComboBoxSkinSelect.Text = ComboBoxSkinSelect.Items[0].ToString();//默认第一个
                                                                                 //this.BackPalace = Image.FromFile(ComboBoxSkinSelect.Items[0].ToString());//默认第一个

                lvDetail.AllowDrop = true;
                lvDetail.View = View.Details;
                lvDetail.DragEnter += Files_DragEnter;//对象拖拽事件
                lvDetail.DragDrop += Files_DragDrop;//拖拽操作完成事件
                                                    //wmp.OpenStateChange += WMP_OpenStateChange;
                wmp.PlayStateChange += WMP_PlayStateChange;
                timerImgs.Start();
            }
            catch (Exception ex)
            {
                Console.WriteLine("错误:" + ex.Message);
            }
        }

        /// <summary>
        /// 提供给透明歌词窗口的定时器调用的
        /// </summary>
        /// <param name="s"></param>
        public void showTmform(bool s)
        {
            //显示歌词
            if (s && showLrc)
            {               
                this.btmForm.Show();
                if (this.first_in)
                {
                    this.lrcForm.TopMost = true;
                    Point point = this.Location;
                    point.Y = point.Y + this.Height+5;
                    this.lrcForm.Location = point;
                    this.btmForm.Location = point;
                    this.lrcForm.Width = this.Width;
                    this.btmForm.Width = this.Width;                    
                }
				this.first_in = false;
            }
            else
            {
                this.first_in = true;
                this.btmForm.Hide();
            }
        }

        /// <summary>
        ///  播放时会进入这个事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void WMP_PlayStateChange(object sender, _WMPOCXEvents_PlayStateChangeEvent e)
        {
            loadLrc();
        }


        /// <summary>
        /// 拖拽操作完成事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Files_DragDrop(object sender, DragEventArgs e)
        {
            try
            {
                string fileName, fileExtension, fileSize, temp;
                FileInfo fi = null;
                ListViewItem lvi = null;
                Array array = (Array)e.Data.GetData(DataFormats.FileDrop);
                Regex regex = new Regex("(\\.mp3|\\.wav|\\.wma)");
                string filePath;
                for (int i = 0; i < array.Length; i++)
                {
                    filePath = array.GetValue(i).ToString();
                    //属于音乐文件 且列表中不存在
                    if (regex.IsMatch(filePath) &&
                        !dic.ContainsKey(filePath))
                    {
                        wmp.Ctlcontrols.stop();
                        InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, filePath);
                    }
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "错误", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }


        /// <summary>
        /// 插入播放列表 和字典集
        /// </summary>
        /// <param name="fileName"></param>
        /// <param name="fileExtension"></param>
        /// <param name="fileSize"></param>
        /// <param name="temp"></param>
        /// <param name="fi"></param>
        /// <param name="lvi"></param>
        /// <param name="filePath"></param>
        private void InsertPlayList(out string fileName, out string fileExtension, out string fileSize, out string temp, out FileInfo fileInfo, out ListViewItem listViewItem, string filePath)
        {
            fileInfo = new FileInfo(filePath);
            temp = filePath.Remove(filePath.LastIndexOf('.'));
            fileName = Path.GetFileNameWithoutExtension(filePath);
            fileExtension = Path.GetExtension(filePath);
            fileSize = (fileInfo.Length / 1024).ToString() + "KB";

            listViewItem = new ListViewItem();
            listViewItem.Text = index++.ToString();
            listViewItem.SubItems.AddRange(new string[] { fileName, fileExtension, fileSize, filePath });

            lvDetail.Items.Add(listViewItem);
            //添加到播放列表
            media = wmp.newMedia(filePath);
            //listIndex++, 
            //wmp.currentPlaylist.insertItem(media);
            wmp.currentPlaylist.appendItem(media);
            playListDict.Add(filePath, media);
            //杜绝重复项
            dic.Add(filePath, fileName);
        }

        /// <summary>
        /// 文件拖拽进入
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Files_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Link;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        /// <summary>
        /// 导入文件
        /// </summary>
        private void tsmiLoading_Click(object sender, EventArgs e)
        {
            string fileName, fileExtension, fileSize, temp;
            FileInfo fi = null;
            ListViewItem lvi = null;
            openFileDialog1.Multiselect = true;
            openFileDialog1.Filter = "mp3文件(*.mp3)|*.mp3|wav文件(*.wav)|*.wav|wma文件(*.wma)|*.wma";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //顺序播放
                wmp.settings.setMode("shuffle", false);
                foreach (string filePath in openFileDialog1.FileNames)
                {
                    if (!dic.ContainsKey(filePath))
                    {
                        InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, filePath);
                    }
                }
            }
        }

        /// <summary>
        /// 清除列表
        /// </summary>
        private void ListViewClear_Click(object sender, EventArgs e)
        {
            lvDetail.Items.Clear();
        }

        /// <summary>
        /// 播放
        /// </summary>
        private void tsmiPlayer_Click(object sender, EventArgs e)
        {
            wmp.Ctlcontrols.play();
        }

        /// <summary>
        /// 暂停
        /// </summary>
        private void tsmiWaiting_Click(object sender, EventArgs e)
        {
            wmp.Ctlcontrols.pause();
        }

        /// <summary>
        /// 停止
        /// </summary>
        private void tsmiStop_Click(object sender, EventArgs e)
        {
            wmp.Ctlcontrols.stop();
        }

        /// <summary>
        /// 退出
        /// </summary>
        private void tsmiExit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// 双击某项播放
        /// </summary>
        private void lvDetail_DoubleClick(object sender, EventArgs e)
        {
            if (lvDetail.SelectedItems.Count > 0)
            {
                wmp.currentMedia = wmp.currentPlaylist.Item[int.Parse(lvDetail.SelectedItems[0].Text) - 1];
            }
        }

        /// <summary>
        ///  循环播放
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void tsmiXunHuan_Click(object sender, EventArgs e)
        {
            //点击项
            ToolStripMenuItem currentItem = (ToolStripMenuItem)sender;

            ToolStripItemCollection items = this.tsmiSet.DropDownItems;

            ToolStripMenuItem item;
            for (int i = 0; i < items.Count; i++)
            {

                item = (ToolStripMenuItem)items[i];
                item.Checked = false;
                if (item.Name == currentItem.Name)
                {
                    item.Checked = true;
                }
            }

            wmp.settings.setMode("loop", true);
        }

        //顺序
        private void tsmiDanQu_Click(object sender, EventArgs e)
        {
            IWMPMedia currentMedia = wmp.currentMedia;
            //点击项
            ToolStripMenuItem currentItem = (ToolStripMenuItem)sender;

            ToolStripItemCollection items = this.tsmiSet.DropDownItems;

            ToolStripMenuItem item;
            for (int i = 0; i < items.Count; i++)
            {

                item = (ToolStripMenuItem)items[i];
                item.Checked = false;
                if (item.Name == currentItem.Name)
                {
                    item.Checked = true;
                }
            }
            //顺序播放
            wmp.settings.setMode("shuffle", false);
        }


        /// <summary>
        ///  图片宽高设置 
        /// </summary>
        /// <param name="imgToResize"></param>
        /// <param name="size"></param>
        /// <returns></returns>
        public static Image ResizeImage(Image imgToResize, Size size)
        {
            //获取图片宽度
            int sourceWidth = imgToResize.Width;
            //获取图片高度
            int sourceHeight = imgToResize.Height;

            float nPercent = 0;
            float nPercentW = 0;
            float nPercentH = 0;
            //计算宽度的缩放比例
            nPercentW = ((float)size.Width / (float)sourceWidth);
            //计算高度的缩放比例
            nPercentH = ((float)size.Height / (float)sourceHeight);

            if (nPercentH < nPercentW)
                nPercent = nPercentH;
            else
                nPercent = nPercentW;
            //期望的宽度
            int destWidth = (int)(sourceWidth * nPercent);
            //期望的高度
            int destHeight = (int)(sourceHeight * nPercent);

            Bitmap b = new Bitmap(destWidth, destHeight);
            Graphics g = Graphics.FromImage((System.Drawing.Image)b);
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;
            //绘制图像
            g.DrawImage(imgToResize, 0, 0, destWidth, destHeight);
            g.Dispose();
            return (System.Drawing.Image)b;
        }


        private void playerType_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (playerType.Text == "顺序播放")
            {
                //顺序播放
                wmp.settings.setMode("shuffle", false);
            }
            else if (playerType.Text == "循环播放")
            {
                wmp.settings.setMode("loop", true);
            }
            else if (playerType.Text == "随机播放")
            {
                //顺序播放
                wmp.settings.setMode("shuffle", true);
            }

        }


        /// <summary>
        /// 定时器执行的方法，每隔1秒执行一次  歌词逐行显示
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void ShowLineLrc(object sender, EventArgs e)
        {
            this.label1.Text = this.wmp.Ctlcontrols.currentPositionString;

            if (this.lrcForm == null)
            {
                this.lrcForm = new TMForm();

                Point pos = this.Location;
                pos.Y = lrcForm.Location.Y + lrcForm.Height;
                this.Location = pos;

                this.btmForm = new BTMForm();
                MusicPlayer mainForm = (MusicPlayer)this.Owner;
                btmForm.Location = pos;
                
                this.lrcForm.Owner = this;
                this.btmForm.Owner = this;
                this.btmForm.Hide();
                this.lrcForm.Show();
            }



            if (this.wmp.currentMedia == null)
            {
                this.richTextBox1.Text = "";
                return;
            }


            string durationString = this.wmp.currentMedia.durationString;
            int trackBarValue = Convert.ToInt32(this.wmp.Ctlcontrols.currentPosition);
            //this.trackBar1.Maximum = Convert.ToInt32(this.wmp.currentMedia.duration);
            //this.trackBar1.Value = Convert.ToInt32(this.wmp.Ctlcontrols.currentPosition);

            if (this.richTextBox1.Text != "歌词文件不存在" && this.richTextBox1.Text != "歌词文件内容为空")
            {
                int pos = al.IndexOf(trackBarValue.ToString());
                bool isAr = this.richTextBox1.Text.Contains("歌手:");
                bool isTi = this.richTextBox1.Text.Contains("歌名:");


                if (pos >= 0)
                {
                    int n = isAr ? 1 : 0;
                    int m = isTi ? 1 : 0;

                    int height = 28 * (this.al.Count + m + n);
                    int max = height - this.richTextBox1.Height;


                    this.richTextBox1.SelectAll();
                    this.richTextBox1.SelectionColor = Color.Black;
                    this.richTextBox1.SelectionLength = 0;/**/

                    int l = this.richTextBox1.Lines[pos + m + n].Length;
                    this.richTextBox1.Select(this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n), l);
                    this.richTextBox1.SelectionColor = Color.OrangeRed;
                    this.richTextBox1.SelectionLength = 0;
                    //this.Text = GetScrollPos(this.richTextBox1.Handle, SB_VERT).ToString() + "-" + al.Count + "-" + this.richTextBox1.Height;

                    if ((pos + m + n) * 28 <= max)
                    {
                        int start = this.richTextBox1.GetFirstCharIndexFromLine(pos + m + n);
                        this.richTextBox1.SelectionStart = start;
                        this.richTextBox1.ScrollToCaret();

                    }
                    else
                    {
                        //this.richTextBox1.Focus();
                        SendMessage(this.richTextBox1.Handle, WM_VSCROLL, SB_BOTTOM, 0);
                        UpdateWindow(this.richTextBox1.Handle);
                        //this.richTextBox1.SelectionStart = this.richTextBox1.Text.Length;
                        //this.richTextBox1.ScrollToCaret();
                    }

                    if (this.lrcForm != null)
                    {
                        string l1 = this.richTextBox1.Lines[pos + m + n];
                        string l2;
                        if ((pos + m + n) < this.richTextBox1.Lines.Length - 1)
                        {
                            l2 = this.richTextBox1.Lines[pos + m + n + 1];
                        }
                        else
                        {
                            l2 = "。。。。。";
                        }

                        this.lrcForm.setLrc(l1, l2, pos);
                        //this.lrcForm.setLrc(ArrayList al,);

                    }

                }
            }
            //this.Text = this.trackBar1.Value.ToString();
            /*if (trackBarValue >= (this.trackBar1.Maximum - 2))
            {
                this.PlayModeChange();
            }*/
        }

        /// <summary>
        /// 载入歌词
        /// </summary>
        /// <param name="lrc_filename">歌词路径名</param>
        public void loadLrc()
        {

            if (this.wmp.playState == WMPPlayState.wmppsPlaying)
            {

                IWMPMedia currentMedia = wmp.currentMedia;
                string fullPath = currentMedia.sourceURL;
                string geciPath = Path.Combine(Path.GetDirectoryName(fullPath), Path.GetFileNameWithoutExtension(fullPath) + ".lrc");

                //播放哪个资源 列表需选中
                ListView.ListViewItemCollection listViewItems = lvDetail.Items;
                lvDetail.FullRowSelect = true;
                for (int i = 0; i < listViewItems.Count; i++)
                {
                    listViewItems[i].Checked = false;
                    listViewItems[i].Selected = false;
                    listViewItems[i].BackColor = Color.White;
                    if (listViewItems[i].SubItems[4].Text == fullPath)
                    {
                        listViewItems[i].Checked = true;
                        listViewItems[i].Selected = true;
                        listViewItems[i].BackColor = Color.LightBlue;
                    }
                }

                if (!File.Exists(geciPath))
                {
                    this.richTextBox1.Text = "歌词文件内容为空";
                    return;
                }

                
                using (StreamReader sr = new StreamReader(new FileStream(geciPath, FileMode.Open), Encoding.Default))
                {
                    string tempLrc = "";
                    while (!sr.EndOfStream)
                    {
                        tempLrc = sr.ReadToEnd();
                    }

                    if (tempLrc.Trim() == "")
                    {
                        this.richTextBox1.Text = "歌词文件内容为空";
                        return;
                    }

                    tempLrc = tempLrc.Trim();
                    Regex rg = new Regex("\r*\n*\\[ver:(.*)\\]\r*\n*");
                    tempLrc = rg.Replace(tempLrc, "");
                    rg = new Regex("\r*\n*\\[al:(.*)\\]\r*\n*");
                    tempLrc = rg.Replace(tempLrc, "");
                    rg = new Regex("\r*\n*\\[by:(.*)\\]\r*\n*");
                    tempLrc = rg.Replace(tempLrc, "");
                    rg = new Regex("\r*\n*\\[offset:(.*)\\]\r*\n*");
                    tempLrc = rg.Replace(tempLrc, "");
                    rg = new Regex("\r*\n*\\[ar:(.*)\\]\r*\n*");
                    Match mtch;
                    mtch = rg.Match(tempLrc);
                    tempLrc = rg.Replace(tempLrc, "\n歌手:" + mtch.Groups[1].Value + "\n");
                    rg = new Regex("\r*\n*\\[ti:(.+?)\\]\r*\n*");   //这里注意贪婪匹配问题.+?
                    mtch = rg.Match(tempLrc);
                    tempLrc = rg.Replace(tempLrc, "\n歌名:" + mtch.Groups[1].Value + "\n");
                    rg = new Regex("\r*\n*\\[[0-9][0-9]:[0-9][0-9].[0-9][0-9]\\]");
                    MatchCollection mc = rg.Matches(tempLrc);
                    al.Clear();

                    foreach (Match m in mc)
                    {
                        string temp = m.Groups[0].Value;
                        //this.Text += temp + "+";                        
                        string mi = temp.Substring(temp.IndexOf('[') + 1, 2);
                        string se = temp.Substring(temp.IndexOf(':') + 1, 2);
                        string ms = temp.Substring(temp.IndexOf('.') + 1, 2);   //这是毫秒，其实我只精确到秒，毫秒后面并没有用
                                                                                //this.Text += mi + ":" + se + "+";
                        string time = Convert.ToInt32(mi) * 60 + Convert.ToInt32(se) + "";  //这里并没有添加毫秒
                        al.Add(time);
                    }

                    tempLrc = rg.Replace(tempLrc, "\n");
                    char[] remove = { '\r', '\n', ' ' };
                    this.richTextBox1.Text = tempLrc.TrimStart(remove);
                    this.timer1.Interval = 1000;
                    this.timer1.Tick += ShowLineLrc;
                    this.timer1.Start();
                    this.count = 0;
                }
            }

        }

        private void wmp_Enter(object sender, EventArgs e)
        {
            loadLrc();//点击播放
        }



        /// <summary>
        ///  删除选中的文件 并停止播放
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void skinButton2_Click(object sender, EventArgs e)
        {
            try
            {
                ListView.SelectedIndexCollection indexes = this.lvDetail.SelectedIndices;
                if (indexes.Count > 0)
                {
                    int index = indexes[0];
                    string path = this.lvDetail.Items[index].SubItems[4].Text;
                    IWMPPlaylist iWMPPlaylist = wmp.currentPlaylist;
                    //先移除播放列表 再移除listview列表
                    wmp.currentPlaylist.removeItem(playListDict[path]);
                    playListDict.Remove(path);
                    this.lvDetail.Items[index].Remove();
                    dic.Remove(path);
                    wmp.Ctlcontrols.stop();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("操作失败！\n" + ex.Message, "提示", MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation, MessageBoxDefaultButton.Button1);

            }
        }

        /// <summary>
        /// 列表鼠标双击事件
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void lvDetail_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            try
            {
                ListView.SelectedIndexCollection indexes = this.lvDetail.SelectedIndices;
                if (indexes.Count > 0)
                {
                    int index = indexes[0];
                    string path = this.lvDetail.Items[index].SubItems[4].Text;
                    wmp.Ctlcontrols.playItem(playListDict[path]);
                    //wmp.URL = path;//这种方式会失去播放列表【不是肉眼可见的listview列表】
                    wmp.Ctlcontrols.stop();
                    wmp.Ctlcontrols.play();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("操作失败！\n" + ex.Message, "提示", MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation, MessageBoxDefaultButton.Button1);

            }
        }

        /// <summary>
        /// 字体改变
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void skinComboBoxFontName_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.lrcForm != null)
            {
                this.lrcForm.ChangeLabelFont(this.skinComboBoxFontName.SelectedItem.ToString(), this.skinComboBoxFontSize.SelectedItem.ToString());

            }
        }

        /// <summary>
        /// 字体大小改变
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void skinComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.lrcForm != null)
            {
                this.lrcForm.ChangeLabelFont(this.skinComboBoxFontName.SelectedItem.ToString(), this.skinComboBoxFontSize.SelectedItem.ToString());

            }
        }

        /// <summary>
        /// 歌词是否显示
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void skinButton5_Click(object sender, EventArgs e)
        {
            if (this.lrcForm == null)
            {
                richTextBox2.Text += "未開啟字幕檔\n";
                return;
            }
            this.showLrc = !this.showLrc;
            this.skinButton5.Text = this.showLrc ? "关闭" : "显示";

            if (this.showLrc)
            {
                this.btmForm.Show();
                this.lrcForm.Show();
            }
            else
            {
                this.btmForm.Hide();
                this.lrcForm.Hide();
            }
                
        }

        /// <summary>
        /// 背景图片切换
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void timerImgs_Tick(object sender, EventArgs e)
        {
            if (imageInd <= imageList.Count - 2)
            {
                imageInd++;
                this.pictureBox1.Image.Dispose();
                this.pictureBox1.Image = Image.FromFile(imageList[imageInd]);
            }
            else
            {
                imageInd=0;
            }
        }


        /// <summary>
        /// 粘贴音乐到播放列表
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void lvDetail_KeyDown(object sender, KeyEventArgs e)
        {
            System.Collections.Specialized.StringCollection stringCollection = Clipboard.GetFileDropList();
            if (stringCollection != null)
            {
                string fileName, fileExtension, fileSize, temp;
                FileInfo fi = null;
                ListViewItem lvi = null;
                foreach (var item in stringCollection)
                {
                    if ((item.ToLower().EndsWith(".mp3") ||
                        item.ToLower().EndsWith(".wav") ||
                        item.ToLower().EndsWith(".wma")) && !dic.ContainsKey(item) )
                    {
                        InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, item);
                    }
                }
            }
        }

        
        //选择皮肤
        private void ComboBoxSkinSelect_SelectedIndexChanged(object sender, EventArgs e)
        {
            string bgColor = ComboBoxSkinSelect.SelectedItem.ToString();
            if (!string.IsNullOrEmpty(ComboBoxSkinSelect.SelectedItem.ToString()))
            {
                switch (bgColor)
                {
                    case "渐变黑":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_black;
                        break;
                    case "天蓝色":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_light_blue;
                        break;
                    case "墨绿色":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_green;
                        break;
                    case "蓝色":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_s_blue;
                        break;
                    case "浅灰色":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_grey;
                        break;  
                    case "亮色":
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_light;
                        break;
                    default:
                        this.BorderPalace = kenMusicPlayer.Properties.Resources.bg_black;
                        break;
                }
                /*this.UpdateStyles();
                this.Update();*/
                //this.BackPalace = Image.FromFile(ComboBoxSkinSelect.SelectedItem.ToString());
            }
        }

        /// <summary>
        /// 退出
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void skinButtonClose_Click(object sender, EventArgs e)
        {
            //this.Close();
            Application.Exit();
        }

        private void MusicPlayer_Resize(object sender, EventArgs e)
        {
            try
            {
                Size size = this.Size;
                int x = (size.Width - dfSize.Width) + closePoint.X;
                int y = closePoint.Y;//(size.Height - dfSize.Height) + closePoint.Y;
                Point point = new Point(x, y);
                this.skinButtonClose.Location = point;
            }
            catch (Exception ex)
            {
                Console.WriteLine("异常:" + ex.Message);
            }

        }


        /// <summary>
        /// 改方法也是提供给透明歌词窗口用的，用来修改半透明窗体的位置，是透明歌词窗口和半透明窗体始终重合
        /// </summary>
        /// <param name="pos"></param>
        public void moveTmform(Point pos)
        {
            this.btmForm.Location = pos;
        }
    }
}
