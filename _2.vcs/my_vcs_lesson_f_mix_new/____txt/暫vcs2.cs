


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



        //將屬標限制在表單內
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Cursor.Clip = new Rectangle(this.Location, this.Size); //控制鼠標在窗口範圍內
        }





richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

dgv1
            //// Make the columns autosize.
            //foreach (DataGridViewColumn col in dataGridView1.Columns)
            //    col.AutoSizeMode = DataGridViewAutoSizeColumnMode.AllCells;

------------------------------------------------------------
------------------------------------------------------------

                    axWindowsMediaPlayer1.Ctlcontrols.playItem(playListDict[path]);		playItem ??

指名播放某項
                axWindowsMediaPlayer1.currentMedia = axWindowsMediaPlayer1.currentPlaylist.Item[int.Parse(lvDetail.SelectedItems[0].Text) - 1];

            IWMPMedia currentMedia = axWindowsMediaPlayer1.currentMedia;


        public int index = 1;
        public int listIndex;
        private bool first_in = true;   //是否第一次進入歌詞區域
        private bool showLrc = true;//預設顯示歌詞
        private int index = 0;//播放的圖片下標
														private List<string> imageList;//播放的圖片
        private Point closePoint;//關閉按鈕的位置
        private Size dfSize;//最初的位置


        //聲音
        SoundPlayer player = new SoundPlayer();
        Dictionary<string, string> dic = new Dictionary<string, string>();

        //播放列表
        Dictionary<string, IWMPMedia> playListDict = new Dictionary<string, IWMPMedia>();

						List<string> al = new List<string>(); //當前歌詞時間表     

        IWMPMedia media;


        /// <summary>
        ///  刪除選中的檔案 並停止播放
        private void skinButton2_Click(object sender, EventArgs e)
        {
            try
            {
                ListView.SelectedIndexCollection indexes = this.lvDetail.SelectedIndices;
                if (indexes.Count > 0)
                {
                    int index = indexes[0];
                    string path = this.lvDetail.Items[index].SubItems[4].Text;
					
                    IWMPPlaylist iWMPPlaylist = axWindowsMediaPlayer1.currentPlaylist;
                    //先移除播放列表 再移除listview列表
                    axWindowsMediaPlayer1.currentPlaylist.removeItem(playListDict[path]);
					
                    playListDict.Remove(path);
                    this.lvDetail.Items[index].Remove();
                    dic.Remove(path);
                }
            }
        }
		
------------------------------------------------------------
------------------------------------------------------------

var urlFormat = @"

http://maps.google.com/maps/api/staticmap?center={0},           
 
    {1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
https://maps.googleapis.com/maps/api/staticmap?parameters

------------------------------------------------------------
------------------------------------------------------------

http://maps.google.com/maps/api/staticmap?parameters

https://maps.googleapis.com/maps/api/staticmap?parameters


如何抓取Google Static Map

https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284
&key=AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY




AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY



        private const string mapurl = "http://maps.google.com/mapdata?latitude_e6={0}&longitude_e6={1}&zm={2}&w={3}&h={4}&cc=&min_priority=2";

string.Format(mapurl, this.Latitude, this.Longitude, this.Zoom, this.Width.Value, this.Height.Value)
			
			url : http://maps.google.com/mapdata?latitude_e6=100&longitude_e6=123&zm=200&w=640&h=480&cc=&min_priority=2



------------------------------------------------------------
------------------------------------------------------------

範例網址：
http://maps.google.com/mapdata?Point=b&Point.latitude_e6=23000944&Point.longitude_e6=120180160&Point.iconid=17&Point=e&zm=33900&w=113&h=113&cc=&min_priority=3&client=internal-mobilefe&zl=7

參數說明：
Point=b和Point=e：代表一個點的開始和結尾
Point.latitude_e6：緯度 (無小數點，小數取到第六位)
Point.longitude_e6：經度(無小數點，小數取到第六位)
w：取得的圖片寬度
h：取得的圖片高度
cc：目前好像沒用
min_priority：試著去改過，不過好像沒什麼作用
client：照著輸入即可
zl：縮放比例 (0~17)
zm：應該是Zoom Meter，計算方式為 (zl + 1) * w 




http://maps.google.com/mapdata?latitude_e6=51600117&longitude_e6=
 4293842485&zm=9600&w=600&h=400&cc=&min_priority=2
 
 
------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------


//C# WinForm窗口最小化到系統托盤2


1.設置WinForm窗體屬性showinTask=false
2.加notifyicon控件notifyIcon1，為控件notifyIcon1的屬性Icon添加一個icon圖標。
3.添加窗體最小化事件(首先需要添加事件引用)：


this.SizeChanged += new System.EventHandler(this.Form1_SizeChanged);
//上面一行是主窗體InitializeComponent()方法中需要添加的引用
private void Form1_SizeChanged(object sender, EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.Hide();
this.notifyIcon1.Visible=true;
}
}

4.添加點擊圖標事件(首先需要添加事件引用)：

private void notifyIcon1_Click(object sender, EventArgs e)
{
this.Visible = true;
this.WindowState = FormWindowState.Normal;
this.notifyIcon1.Visible = false;
}

5.可以給notifyIcon添加右鍵菜單：
主窗體中拖入一個ContextMenu控件NicontextMenu，點中控件，在上下文菜單中添加菜單，notifyIcon1的ContextMenu行為中選中NicontextMenu 作為上下文菜單。
代碼如下：

this.notifyIcon1 = new System.Windows.Forms.NotifyIcon(this.components);
this.NicontextMenu = new System.Windows.Forms.ContextMenu();
this.menuItem_Hide = new System.Windows.Forms.MenuItem();

this.menuItem_Show = new System.Windows.Forms.MenuItem();
this.menuItem_Aubot = new System.Windows.Forms.MenuItem();
this.menuItem_Exit = new System.Windows.Forms.MenuItem();
this.notifyIcon1.ContextMenu = this.NicontextMenu;
this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject( "NotifyIcon.Icon ")));
this.notifyIcon1.Text = " ";
this.notifyIcon1.Visible = true;
this.notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
this.notifyIcon1.Click += new System.EventHandler(this.notifyIcon1_Click);
this.NicontextMenu.MenuItems.AddRange(
new System.Windows.Forms.MenuItem[]
{
this.menuItem_Hide,
this.menuItem_Show,
this.menuItem_Aubot,
this.menuItem_Exit
}
);
//
// menuItem_Hide
//
this.menuItem_Hide.Index = 0;
this.menuItem_Hide.Text = "隱藏 ";
this.menuItem_Hide.Click += new System.EventHandler(this.menuItem_Hide_Click);
//
// menuItem_Show
//
this.menuItem_Show.Index = 1;
this.menuItem_Show.Text = "顯示 ";
this.menuItem_Show.Click += new System.EventHandler(this.menuItem_Show_Click);
//
// menuItem_Aubot
//
this.menuItem_Aubot.Index = 2;
this.menuItem_Aubot.Text = "關於 ";
this.menuItem_Aubot.Click += new System.EventHandler(this.menuItem_Aubot_Click);
//
// menuItem_Exit
//
this.menuItem_Exit.Index = 3;
this.menuItem_Exit.Text = "退出 ";
this.menuItem_Exit.Click += new System.EventHandler(this.menuItem_Exit_Click);
protected override void OnClosing(CancelEventArgs e)
{
this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
protected override void OnClosing(CancelEventArgs e)
{
//this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
private void CloseCtiServer()
{
timer.Enabled = false;
DJ160API.DisableCard();
this.NotifyIcon.Visible = false;
this.Close();
this.Dispose();
Application.Exit();
}
private void HideCtiServer()
{
this.Hide();
}
private void ShowCtiServer()
{
this.Show();
this.WindowState = FormWindowState.Normal;
this.Activate();
}
private void CtiManiForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Show_Click(object sender, System.EventArgs e)
{
this.ShowCtiServer();
}
private void menuItem_Aubot_Click(object sender, System.EventArgs e)
{
}
private void menuItem_Exit_Click(object sender, System.EventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Hide_Click(object sender, System.EventArgs e)
{
this.HideCtiServer();
}
private void CtiManiForm_SizeChanged(object sender, System.EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.HideCtiServer();
}
}
private void notifyIcon1_DoubleClick(object sender,System.EventArgs e)
{
this.ShowCtiServer();
}


------------------------------------------------------------
------------------------------------------------------------








把一個ENUM的內容用foreach加到一個combobox裡
點選combobox的項目 套用之

用以測googlemap之各種地圖 圖標



逐步解說：使用 C 撰寫複合控制項#


複合控制項提供可以建立及重複使用自訂圖形介面的方法。 複合控制項基本上是具有視覺表示的元件。 因此，它可能包含一或多個 Windows Forms 控制項、元件或程式碼區塊，可以藉由驗證使用者輸入、修改顯示屬性，或執行作者需要的其他工作來擴充功能。 複合控制項可以放在 Windows Forms 上，與其他控制項的方式相同。 在本逐步解說的第一個部分中，您可以建立簡單的複合控制項，稱為 ctlClock。 在逐步解說的第二個部分中，您透過繼承擴充 ctlClock 的功能。
建立專案

當您建立新的專案時，您會指定其名稱以設定根命名空間、組件名稱和專案名稱，並且確定預設元件將會在正確的命名空間中。
建立 ctlClockLib 控制項程式庫和 ctlClock 控制項



    在 Visual Studio 中，建立新的Windows Forms 控制項程式庫專案，並將它命名為ctlClockLib。

    專案名稱，ctlClockLib，預設也會指派給根命名空間。 根命名空間是用來限定組件中的元件名稱。 例如，如果兩個組件提供元件，名為 ctlClock，您可以使用 ctlClockLib.ctlClock. 指定您的 ctlClock 元件

    在方案總管中，以滑鼠右鍵按一下 [ UserControl1]，然後按一下 [重新命名]。 將檔案名稱變更為 ctlClock.cs。 當系統詢問您是否要重新命名程式碼元素 "UserControl1" 的所有參考時，請按一下 [ 是] 按鈕。




    注意

    依預設，複合控制項繼承自系統提供的 UserControl 類別。 UserControl類別提供所有複合控制項所需的功能，並可執行標準方法和屬性。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將 Windows 控制項和元件新增至複合控制項

視覺化介面是複合控制項不可或缺的一部分。 這個視覺化介面是藉由將一或多個 Windows 控制項新增至設計工具介面來實作。 在下列示範中，您將 Windows 控制項合併到您的複合控制項，並且撰寫程式碼來實作功能。
將標籤和計時器新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖設計工具]。

    在 [ 工具箱] 中，展開 [ 通用控制項 ] 節點，然後按兩下 [ 標籤]。

    Label系統會將名 label1 為的控制項新增至設計工具介面上的控制項。

    在設計工具中，按一下 [ label1]。 在 [屬性] 視窗中設定下列屬性。
    屬性 	變更為
    名稱 	lblDisplay
    Text 	(blank space)
    TextAlign 	MiddleCenter
    字型。大小 	14

    在 [工具箱] 中展開 [元件] 節點，然後再按兩下 [計時器]。

    Timer因為是元件，所以在執行時間沒有視覺標記法。 因此，它不會與控制項一起出現在設計工具介面上，而是在 元件設計 工具中 (設計工具介面底部的紙匣) 。

    在元件設計工具中，按一下 [ timer1]，然後將屬性設定為 1000 ，並 Enabled 將屬性設定 Interval 為 true 。

    Interval屬性控制元件刻度的頻率 Timer 。 每次 timer1 走動時，它會執行 timer1_Tick 事件中的程式碼。 間隔代表刻度之間的毫秒數。

    在 元件設計工具中，按兩下 [ timer1 ] 以移至的 timer1_Tick 事件 ctlClock 。

    修改程式碼，使它類似下列程式碼範例。 請確定將存取修飾詞從 private 變更為 protected。
    C#

protected void timer1_Tick(object sender, System.EventArgs e)
{
    // Causes the label to display the current time.
    lblDisplay.Text = DateTime.Now.ToLongTimeString();
}

此程式碼會造成目前時間在 lblDisplay 中顯示。 因為 timer1 的間隔設為 1000，每一千毫秒便會發生此事件，因此每秒會更新目前時間。

修改方法為可使用 virtual關鍵字覆寫。 如需詳細資訊，請參閱以下的「從使用者控制項繼承」一節。
C#

    protected virtual void timer1_Tick(object sender, System.EventArgs e)

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將屬性新增至複合控制項

您的時鐘控制項現在會封裝 Label 控制項和 Timer 元件，每個都有自己的一組固有屬性。 雖然這些控制項的個別屬性無法供控制項的後續使用者存取，但是您可以建立並公開自訂屬性，方法是撰寫適當的程式碼區塊。 在下列程序中，您會將屬性新增至控制項，讓使用者變更背景與文字的色彩。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖程式碼]。

    控制項的程式 代碼編輯器 隨即開啟。

    尋找 public partial class ctlClock 陳述式。 在左大括號 ({) 底下，輸入下列程式碼。
    C#

private Color colFColor;
private Color colBColor;

這些陳述式會建立私用變數，您將用來儲存您即將建立之屬性的值。

在步驟2的變數宣告底下，輸入或貼上下列程式碼。
C#

    // Declares the name and type of the property.
    public Color ClockBackColor
    {
        // Retrieves the value of the private variable colBColor.
        get
        {
            return colBColor;
        }
        // Stores the selected value in the private variable colBColor, and
        // updates the background color of the label control lblDisplay.
        set
        {
            colBColor = value;
            lblDisplay.BackColor = colBColor;
        }
    }
    // Provides a similar set of instructions for the foreground color.
    public Color ClockForeColor
    {
        get
        {
            return colFColor;
        }
        set
        {
            colFColor = value;
            lblDisplay.ForeColor = colFColor;
        }
    }

    上述程式碼會製作兩個自訂屬性，ClockForeColor 和 ClockBackColor，以供此控制項的後續使用者使用。 get 和 set 陳述式提供屬性值的儲存和擷取，以及用來實作適合該屬性之功能的程式碼。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

測試控制項

控制項不是獨立應用程式；它們必須裝載在容器中。 測試控制項的執行階段行為，並且使用 UserControl 測試容器執行其屬性。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。
若要測試控制項

    按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。

    在測試容器的屬性方格中，尋找 ClockBackColor 屬性，然後選取屬性以顯示色彩調色盤。

    按一下它以選擇色彩。

    控制項的背景色彩會變更為您所選取的色彩。

    使用類似的一連串事件，確認 ClockForeColor 屬性是否如預期運作。

    在本節和先前的章節中，您已經知道元件和 Windows 控制項如何與程式碼合併並且封裝，以複合控制項的形式提供自訂功能。 您已經了解如何在您的複合控制項中公開屬性，以及如何在完成之後測試您的控制項。 在下一節中，您將學習如何使用 ctlClock 做為基底，建構繼承的複合控制項。

繼承自複合控制項

在先前章節中，您了解如何將 Windows 控制項、元件和程式碼合併成可重複使用的複合控制項。 複合控制項現在可以做為建置其他控制項的基底。 從基底類別衍生類別的處理序稱為「繼承」。 在本節中，您將建立稱為 ctlAlarmClock 的複合控制項。 這個控制項將會從其父控制項 (ctlClock) 衍生。 您將學習藉由覆寫父方法並且新增新方法和屬性，來擴充 ctlClock 的功能。

建立繼承的控制項的第一個步驟是從其父代衍生。 這個動作會建立新的控制項，其中具有父控制項的所有屬性、方法和圖形特性，但是也可以做為基底，以新增新的或修改功能。
若要建立繼承的控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，指向 [新增]，然後按一下 [使用者控制項]。

    [ 加入新專案 ] 對話方塊隨即開啟。

    選取繼承的使用者控制項範本。

    在 [名稱] 方塊中，輸入 ctlAlarmClock.cs 然後按一下 [新增]。

    [繼承選取器] 對話方塊隨即出現。

    在 [元件名稱] 底下，按兩下 [ctlClock]。

    在方案總管中，流覽目前的專案。

    注意

    名為 ctlAlarmClock.cs 的檔案已新增至目前的專案。

新增警示屬性

屬性會以新增至複合控制項的相同方式，新增至繼承的控制項。 您現在會使用屬性宣告語法將兩個屬性新增至您的控制項︰AlarmTime，它將會儲存警示停止之日期和時間的值，以及 AlarmSet，它將會指示是否已設定警示。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖程式碼]。

    尋找 public class 陳述式。 請注意，您的控制項繼承自ctlClockLib.ctlClock。 在左大括號 ({) 陳述式底下，輸入下列程式碼。
    C#

    private DateTime dteAlarmTime;
    private bool blnAlarmSet;
    // These properties will be declared as public to allow future
    // developers to access them.
    public DateTime AlarmTime
    {
        get
        {
            return dteAlarmTime;
        }
        set
        {
            dteAlarmTime = value;
        }
    }
    public bool AlarmSet
    {
        get
        {
            return blnAlarmSet;
        }
        set
        {
            blnAlarmSet = value;
        }
    }

加入至控制項的圖形化介面

繼承的控制項具有視覺化介面，與它所繼承的控制項相同。 它擁有與其父控制項相同的組成控制項，但是無法使用組成控制項的屬性，除非特別公開。 您可以使用新增至任何複合控制項的相同方式，新增至繼承的複合控制項的圖形化介面。 若要繼續新增至警示時鐘的視覺化介面，您要新增標籤控制項，該控制項會在警示響起時閃爍。
若要新增標籤控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    ctlAlarmClock 的設計工具隨即在主視窗中開啟。

    按一下控制項的顯示部分，並檢視 [屬性] 視窗。

    注意

    所有屬性顯示時，它們會以灰色顯示。 這表示這些屬性是 lblDisplay 的原生屬性，而且無法修改或在 [屬性] 視窗中存取。 根據預設，包含在複合控制項中的控制項是 private，而且其屬性無法使用任何方法存取。

    注意

    如果您想要讓複合控制項的後續使用者可以存取其內部控制項，請將它們宣告為 public 或 protected。 這可讓您使用適當的程式碼，設定及修改包含在複合控制項中的控制項屬性。

    Label將控制項新增至複合控制項。

    使用滑鼠，將 Label 控制項緊接在 [顯示] 方塊下方。 在 [屬性] 視窗中設定下列屬性。
    屬性 	設定
    名稱 	lblAlarm
    Text 	報警！
    TextAlign 	MiddleCenter
    Visible 	false

新增警示功能

在先前的程序中，您新增屬性和控制項，在您的複合控制項中啟用警示功能。 在此程序中，您將會新增程式碼以比較目前時間與警示時間，如果它們相同，則讓警示閃爍。 藉由覆寫 ctlClock 的 timer1_Tick 方法，並且將額外程式碼新增至其中，您就可以擴充 ctlAlarmClock 的功能，同時保留 ctlClock 的所有固有功能。
若要覆寫 ctlClock 的 timer1_Tick 方法

    在 [程式碼編輯器] 中，尋找 private bool blnAlarmSet; 陳述式。 緊接著在其下新增下列陳述式。
    C#

private bool blnColorTicker;

在 [程式碼編輯器] 中，在類別結尾尋找右大括號 (})。 緊接在大括號之前，新增下列程式碼。
C#

    protected override void timer1_Tick(object sender, System.EventArgs e)
    {
        // Calls the Timer1_Tick method of ctlClock.
        base.timer1_Tick(sender, e);
        // Checks to see if the alarm is set.
        if (AlarmSet == false)
            return;
        else
            // If the date, hour, and minute of the alarm time are the same as
            // the current time, flash an alarm.
        {
            if (AlarmTime.Date == DateTime.Now.Date && AlarmTime.Hour ==
                DateTime.Now.Hour && AlarmTime.Minute == DateTime.Now.Minute)
            {
                // Sets lblAlarmVisible to true, and changes the background color based on
                // the value of blnColorTicker. The background color of the label
                // will flash once per tick of the clock.
                lblAlarm.Visible = true;
                if (blnColorTicker == false)
                {
                    lblAlarm.BackColor = Color.Red;
                    blnColorTicker = true;
                }
                else
                {
                    lblAlarm.BackColor = Color.Blue;
                    blnColorTicker = false;
                }
            }
            else
            {
                // Once the alarm has sounded for a minute, the label is made
                // invisible again.
                lblAlarm.Visible = false;
            }
        }
    }

    新增這個程式碼會完成幾項工作。 override 陳述式會指示控制項使用這個方法來取代繼承自基底控制項的方法。 呼叫這個方法時，它會呼叫它藉由叫用 base.timer1_Tick 陳述式覆寫的方法，確保併入原始控制項的所有功能在此控制項中重現。 接著，它會執行其他程式碼以併入警示功能。 發生警示時，閃爍標籤控制項就會出現。

    警示時鐘控制項已接近完成。 唯一剩餘的事項是實作將它關閉的方式。 若要這樣做，您要將程式碼新增至 lblAlarm_Click 方法。

若要實作關閉方法

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    設計工具隨即開啟。

    將按鈕新增至控制項。 將按鈕的屬性設定如下。
    屬性 	值
    名稱 	btnAlarmOff
    Text 	停用警示

    在設計工具中，按兩下 [btnAlarmOff]。

    [程式碼編輯器] 隨即開啟至 private void btnAlarmOff_Click 行。

    修改此方法，使它類似下列程式碼。
    C#

    private void btnAlarmOff_Click(object sender, System.EventArgs e)
    {
        // Turns off the alarm.
        AlarmSet = false;
        // Hides the flashing label.
        lblAlarm.Visible = false;
    }

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

在表單上使用繼承的控制項

您可以用測試基類控制項的相同方式來測試繼承的控制項，請 ctlClock 按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。

若要使用控制項，您必須將它裝載在表單上。 如同標準複合控制項，繼承的複合控制項無法獨立存在，而且必須裝載在表單或其他容器。 由於 ctlAlarmClock 有更深入的功能，需要額外的程式碼來進行測試。 在此程序中，您將撰寫一個簡單的程式來測試 ctlAlarmClock 的功能。 您將撰寫程式碼以設定及顯示 ctlAlarmClock 的 AlarmTime 屬性，然後測試其固有功能。
若要建置控制項並且新增至測試表單

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，然後按一下 [建立]。

    將新的Windows Forms 應用程式專案加入至方案，並為其命名測試。

    在方案總管中，以滑鼠右鍵按一下測試專案的 [參考] 節點。 按一下 [加入參考]以顯示 [加入參考] 對話方塊。 按一下標籤為 [專案] 的索引標籤。 您的 ctlClockLib 專案會列在 [專案名稱] 底下。 按兩下專案以將參考新增至測試專案。

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [建立]。

    在 [工具箱] 中，展開 [ctlClockLib 元件] 節點。

    按兩下 [ctlAlarmClock] 以將 ctlAlarmClock 的複本新增至表單。

    在 [工具箱] 中，找出並按兩下 [ DateTimePicker ]，將控制項新增 DateTimePicker 至表單，然後按兩下 [標籤] 來加入 Label 控制項。

    使用滑鼠將控制項放置在表單上方便的位置。

    以下列方式設定這些控制項的屬性。
    控制 	屬性 	值
    label1 	Text 	(blank space)
    	名稱 	lblTest
    dateTimePicker1 	名稱 	dtpTest
    	格式 	Time

    在設計工具中，按兩下 [dtpTest]。

    [程式碼編輯器] 隨即開啟至 private void dtpTest_ValueChanged。

    修改此程式碼，使它類似下列程式碼。
    C#

    private void dtpTest_ValueChanged(object sender, System.EventArgs e)
    {
        ctlAlarmClock1.AlarmTime = dtpTest.Value;
        ctlAlarmClock1.AlarmSet = true;
        lblTest.Text = "Alarm Time is " +
            ctlAlarmClock1.AlarmTime.ToShortTimeString();
    }

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [設定為啟動 Project。

    在 [偵錯] 功能表上，按一下 [開始偵錯] 。

    測試程式隨即啟動。 請注意，目前的時間會在控制項中 ctlAlarmClock 更新，而開始時間則顯示在控制項中 DateTimePicker 。

    DateTimePicker按一下該小時的分鐘顯示位置。

    使用鍵盤，將分鐘值設定為大於 ctlAlarmClock 顯示的目前時間一分鐘。

    警示設定的時間會在 lblTest 中顯示。 等候顯示的時間達到警示設定時間。 當顯示的時間達到警示設定時間，則 lblAlarm 會閃爍。

    按一下 btnAlarmOff 來關閉警示。 您現在可以重設警示。

本文涵蓋了許多重要概念。 您已經了解藉由將控制項和元件合併成複合控制項容器，來建立複合控制項。 您已經了解將屬性新增至您的控制項，以及撰寫程式碼來實作自訂功能。 在最後一節中，您會了解透過繼承擴充指定複合控制項的功能，並且藉由覆寫這些方法來變更主方法的功能。
另請參閱

    各種自訂控制項
    如何：在選擇工具箱項目對話方塊中顯示控制項
    逐步解說：使用 Visual C# 繼承自 Windows Form 控制項

建議的內容

    定義控制項屬性 - Windows Forms .NET Framework

    開發自訂控制項 - Windows Forms .NET Framework

    瞭解 Windows 表單控制項。 具體來說，您將學習如何結合現有的控制項、延伸現有的控制項，以及撰寫您自己的自訂控制項。
    使用 FlowLayoutPanel 排列控制項 - Windows Forms .NET Framework

    學習如何使用 FlowLayoutPanel 控制項和 TableLayoutPanel 控制項，以提供直覺的方式來排列 Windows Forms 專案中的控制項。
    AutoSize 在 TableLayoutPanel 控制項中的行為 - Windows Forms .NET Framework

本文內容

    建立專案
    將 Windows 控制項和元件新增至複合控制項
    將屬性新增至複合控制項
    測試控制項

    舊版文件
    部落格
    參與
    隱私權與 Cookie
    使用規定
    商標
    © Microsoft 2022




------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------






client.DownloadFile(url, filename);
string data = client1.DownloadString(url_file1);          //抓網頁資料到記憶體
client2.DownloadFile(url_file2, filename_local);          //抓網頁資料到本地檔案
string xml = client3.DownloadString(url_weather);        //抓資料

MemoryStream image_stream = new MemoryStream(client.DownloadData(url));

byte[] bd = client.DownloadData(sURL);






Stream stream = client.OpenRead(URLAddress);


client.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");









using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream

namespace vcs_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //for Romeo and Sugar    3072
            //ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            //ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //加入這段語法忽略憑證
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            */

            string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

            using ( client1 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //richTextBox1.Text += data + "\n";
                    richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
            //string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            using ( client2 = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    //string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                    int pos1 = url_file2.LastIndexOf('/');
                    int pos2 = url_file2.LastIndexOf('.');
                    string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
                    richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

                    richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
            using (  = new ())     // Create a web client
            {
                try  // Get the response string from the URL.
                {
                    // Get the response string from the URL.
                    //richTextBox1.Text += "data\n" + xml + "\n";
                    richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
                }
                catch (WebException ex)
                {
                    MessageBox.Show("WebException\t" + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Unknown error\t" + ex.Message);
                }
            }
            Application.DoEvents();

            string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
            richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
            try
            {
                //圖片下載並存檔
                DownloadImage(img_src_url);
                richTextBox1.Text += "圖片下載並存檔\tOK\n";
                Application.DoEvents();

                //圖片下來並顯示
                Image img = GetPicture(img_src_url);
                pictureBox1.Image = img;
                richTextBox1.Text += "圖片下來並顯示\tOK\n";
                Application.DoEvents();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "*** Download Error" + "\n";
                richTextBox1.Text += "*** " + ex.Message + "\n";
            }
            Application.DoEvents();


            //下載COVID-19資料

            // Compose the local data file name.
            string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            string url = "https://covidtracking.com/api/v1/states/daily.csv";

            richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
            Application.DoEvents();

            DownloadFile(url, filename_covid19a);


            richTextBox1.Text += "Loading case data...\n";
            Application.DoEvents();

            // Compose the local data file name.
            string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

            // Download today's data.
            url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
            DownloadFile(url, filename_covid19b);
        }

        // Download the indicated file.
        private void DownloadImage(string url)
        {
            //richTextBox1.Text += "下載圖片 : " + url + "\n";

            // Make a .
             client = new ();

            /*
            int pos = url.LastIndexOf('/');
            string filename = url.Substring(pos + 1);
            */

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');
            string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
            richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

            // Use one of the following.
            // For .NET Framework 4.5 and later:
            //ServicePointManager.SecurityProtocol =
            //    SecurityProtocolType.Tls12;
            // For .NET Framework 4.0 through 4.4:
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Download the file.
            client.DownloadFile(url, filename);
        }

        // Download a file from the internet.
        // Get the picture at a given URL.
        private Image GetPicture(string url)
        {
            try
            {
                 client = new ();

                // Use one of the following.
                //ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
                ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

                MemoryStream image_stream = new MemoryStream(client.DownloadData(url));
                return Image.FromStream(image_stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
                return null;
            }
        }

        private void DownloadFile(string url, string filename)
        {
            try
            {
                // Make a .
                 client = new ();

                // Download the file.
                client.DownloadFile(url, filename);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            finally
            {
                if (!File.Exists(filename))
                {
                    richTextBox1.Text += "下載 : " + filename + "\tNG\n";
                }
                else
                {
                    richTextBox1.Text += "下載 : " + filename + "\tOK\n";
                }
            }
        }

    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}




using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;    //for MemoryStream

namespace vcs_
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}

private void Form1_Load(object sender, EventArgs e)
{
// Allow TLS 1.1 and TLS 1.2 protocols for file download.
//for Sugar     3840 Romeo也可用
ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

//for Romeo and Sugar    3072
//ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
//ServicePointManager.SecurityProtocol = (SecurityProtocolType)3840;
//richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";
}

private void button1_Click(object sender, EventArgs e)
{
/*
//加入這段語法忽略憑證
ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
*/

string url_file1 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
//string url_file = @"http://antwrp.gsfc.nasa.gov/apod/";

using ( client1 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
//richTextBox1.Text += data + "\n";
richTextBox1.Text += "抓網頁資料到記憶體\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string url_file2 = @"http://snowball.tartarus.org/otherlangs/english_cpp.txt";
//string url_file2 = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
using ( client2 = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
//string filename_local = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
int pos1 = url_file2.LastIndexOf('/');
int pos2 = url_file2.LastIndexOf('.');
string filename_local = url_file2.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url_file2.Substring(pos2);
richTextBox1.Text += "下載檔案, 本地檔案檔名 : " + filename_local + "\n";

richTextBox1.Text += "抓網頁資料到本地檔案\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string url_weather = @"http://api.openweathermap.org/data/2.5/weather?q=Hsinchu&mode=xml&units=imperial&APPID=e8edf79325ae8948a635efd0e076a8bc";
using (  = new ())     // Create a web client
{
try  // Get the response string from the URL.
{
// Get the response string from the URL.
//richTextBox1.Text += "data\n" + xml + "\n";
richTextBox1.Text += "抓網頁查詢資料到記憶體\tOK\n";
}
catch (WebException ex)
{
MessageBox.Show("WebException\t" + ex.Message);
}
catch (Exception ex)
{
MessageBox.Show("Unknown error\t" + ex.Message);
}
}
Application.DoEvents();

string img_src_url = @"https://apod.nasa.gov/apod/image/2103/VolcanoStars_Vella_1080.jpg";
richTextBox1.Text += "圖片所在網址 : " + img_src_url + "\n";
try
{
//圖片下載並存檔
DownloadImage(img_src_url);
richTextBox1.Text += "圖片下載並存檔\tOK\n";
Application.DoEvents();

//圖片下來並顯示
Image img = GetPicture(img_src_url);
pictureBox1.Image = img;
richTextBox1.Text += "圖片下來並顯示\tOK\n";
Application.DoEvents();
}
catch (Exception ex)
{
richTextBox1.Text += "*** Download Error" + "\n";
richTextBox1.Text += "*** " + ex.Message + "\n";
}
Application.DoEvents();


//下載COVID-19資料

// Compose the local data file name.
string filename_covid19a = "state_data" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
string url = "https://covidtracking.com/api/v1/states/daily.csv";

richTextBox1.Text += "LoadData \tURL : " + url + "\tfile : " + filename_covid19a + "\n";
Application.DoEvents();

DownloadFile(url, filename_covid19a);


richTextBox1.Text += "Loading case data...\n";
Application.DoEvents();

// Compose the local data file name.
string filename_covid19b = "cases" + DateTime.Now.ToString("yyyy_MM_dd") + ".csv";

// Download today's data.
url = "https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv";
DownloadFile(url, filename_covid19b);
}

// Download the indicated file.
private void DownloadImage(string url)
{
//richTextBox1.Text += "下載圖片 : " + url + "\n";

// Make a Web
 client = new ();

/*
int pos = url.LastIndexOf('/');
string filename = url.Substring(pos + 1);
*/

int pos1 = url.LastIndexOf('/');
int pos2 = url.LastIndexOf('.');
string filename = url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
richTextBox1.Text += "下載圖片, 本地圖片檔名 : " + filename + "\n";

// Use one of the following.
// For .NET Framework 4.5 and later:
//ServicePointManager.SecurityProtocol =
//    SecurityProtocolType.Tls12;
// For .NET Framework 4.0 through 4.4:
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

// Download the file.
}

// Download a file from the internet.
// Get the picture at a given URL.
private Image GetPicture(string url)
{
try
{
 client = new ();

// Use one of the following.
//ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12;
ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

return Image.FromStream(image_stream);
}
catch (Exception ex)
{
richTextBox1.Text += "Error downloading picture " + url + '\n' + ex.Message + "\n";
return null;
}
}

private void DownloadFile(string url, string filename)
{
try
{
// Make a Web
 client = new ();

// Download the file.
}
catch (Exception ex)
{
MessageBox.Show(ex.Message, "Download Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
}
finally
{
if (!File.Exists(filename))
{
richTextBox1.Text += "下載 : " + filename + "\tNG\n";
}
else
{
richTextBox1.Text += "下載 : " + filename + "\tOK\n";
}
}
}

}

public class Protocols
{
public const SecurityProtocolType
protocol_SystemDefault = 0,
protocol_Ssl3 = (SecurityProtocolType)48,
protocol_Tls = (SecurityProtocolType)192,
protocol_Tls11 = (SecurityProtocolType)768,
protocol_Tls12 = (SecurityProtocolType)3072;
}

}


------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------





------------------------------------------------------------
------------------------------------------------------------








 


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



進程

我們可以把計算機中每一個運行的應用程序當作是一個進程



線程

每一個進程是由多個線程組成的。
單線程：讓程序做多件事時，會引發卡死 假死狀態。
多線程：讓一個程序同時處理多個事情，後台運行程序，提高程序的運行效率。
前台線程：只有所有的前台線程都關閉才能完成程序關閉。(winform多窗口時)
後台線程：只要所有的前台線程結束，後台線程自動結束。

 1 //實例化Thread類，並傳入一個指向線程所要運行的方法。（這時線程已經產生，但還沒有運行）
 2 //調用Thread類的Start方法，標記線程可以被CPU執行了，但具體執行事件由CPU決定。
 3 Thread th = new Thread(Test); //創建一個線程去執行這個方法。
 4 th.IsBackground = true; //將線程設置為後台線程，前台關閉後 線程結束。
 5 th.Start(); //標記准備就緒，可以隨意被執行，具體什麼時候執行由CPU決定。
 6 //在.net下是不允許跨線程訪問的。
 7 //有時候需要手動釋放線程 關閉時 判斷線程是否關閉 
 8 if (th != null)
 9 {
10     th.Abort(); //結束這個線程 不能再Start()
11 }
12 Thread.Sleep(3000); //睡眠3秒後執行
13 //線程執行帶參數方法
14 Thread.Start("123")； object類型參數 在start後括號寫參數

//多用於大量數據時，多分一個線程去搜索數據，然後存儲到緩存裡，頁面再用異步獲取緩存中的數據。












BTW, if the HtmlNode has a “ID”, like “<div id='post_list'>value</div>”, call GetElementbyId() is OK for getting the HtmlNode, then get the value by HtmlNode.InnerText or HtmlNode.Attribute.

Please see the following C# code snippet.

Code snippet:

 //get HtmlAgilityPack.HtmlDocument object   
 HtmlDocument doc = new HtmlDocument();  
 //load HTML   
doc.LoadHtml(pageSource);         
//get HtmlNode by ID   
 HtmlNode navNode = doc.GetElementbyId("post_list");	//測這個


 

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.Text.RegularExpressions;
using HtmlAgilityPack;

namespace RegexPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            string pageUrl = "http://top.baidu.com/buzz.php?p=top_keyword";
            WebClient wc = new WebClient();
            byte[] pageSourceBytes = wc.DownloadData(new Uri(pageUrl));
            string pageSource = Encoding.GetEncoding("gb2312").GetString(pageSourceBytes);

            //Regex searchKeyRegex = new Regex("<td class=\"key\">.*?target=\"_blank\">(?<keyWord>.*?)</a></td>");
            //MatchCollection mc = searchKeyRegex.Matches(pageSource);
            //List<string> keyWordList = new List<string>();
            //foreach(Match m in mc)
            //{
            //    keyWordList.Add(m.Groups["keyWord"].Value);
            //}

            HtmlDocument doc = new HtmlDocument();
            doc.LoadHtml(pageSource);

            HtmlNodeCollection keyNodes = doc.DocumentNode.SelectNodes("//td[@class='key']/a[@ target='_blank']");
            List<string> keyWords = new List<string>();
            foreach (HtmlNode keyNode in keyNodes)
            {
                keyWords.Add(keyNode.InnerText);
            }

            //HtmlDocument doc = new HtmlDocument();
            //doc.LoadHtml(pageSource);

            //HtmlNode ulNode = doc.DocumentNode.SelectSingleNode("//ul[@class='hotnews']");

            //HtmlNodeCollection liNodes = ulNode.SelectNodes("li");

            //List<string> topList = new List<string>();
            //List<string> subList = new List<string>();

            //foreach (HtmlNode liNode in liNodes)
            //{
            //    if (liNode.Attributes["class"] != null && liNode.Attributes["class"].Value == "top")
            //    {
            //        topList.Add(liNode.InnerText);
            //    }
            //    else
            //    {
            //        if (subList.Count < topList.Count)
            //        {
            //            subList.Add(liNode.InnerText);
            //        }
            //        else
            //        {
            //            subList[subList.Count - 1] = subList[subList.Count - 1] + liNode.InnerText;
            //        }
            //    }
            //}

            return;

            //Regex hotTopNewsRegex = new Regex("class=\"a3\".*?>(?<hotNews>.*)<");
            //MatchCollection topMc = hotTopNewsRegex.Matches(pageSource);

            //List<string> hotNewsList = new List<string>();
            //foreach (Match m in topMc)
            //{
            //    hotNewsList.Add(m.Groups["hotNews"].Value);
            //}


            //Regex replaceRegex = new Regex("</?font.*?>");
            //for (int i = 0; i < hotNewsList.Count;i++ )
            //{
            //    hotNewsList[i] = replaceRegex.Replace(hotNewsList[i], "");
            //}

            //Regex hotSubNewsRegex = new Regex("(?s)class=\"top\"(?<subNews>.*?)class=\"top\"");
            //MatchCollection subMc = hotSubNewsRegex.Matches(pageSource);
            //int temp = subMc.Count;

            //List<string> subNewsList = new List<string>();
            //foreach (Match m in subMc)
            //{
            //    subNewsList.Add(m.Groups["subNews"].Value);
            //}
        }
    }
}


Another code snippet

Download specified number of pictures from “ http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15” and save to local files.

	using System;  
	using System.Collections.Generic;  
	using System.Linq;  
	using System.Text;  
	using System.Net;  
	using System.Text.RegularExpressions;  
	using HtmlAgilityPack;  
	using System.IO;  
	  
	namespace RegexPractice  
	{  
	    public class Util  
	    {  
	  
	        //Get byte[] format page source    
	        public static byte[] GetPageSourceBytes(string url)  
	        {  
	            WebClient wc = new WebClient();  
	            byte[] pageSourceBytes = wc.DownloadData(new Uri(url));  
	            return pageSourceBytes;  
	        }  
	  
	        //get string format page source    
	        public static string GetPageSource(string url, string encodingType)  
	        {  
	            byte[] pageSourceBytes = GetPageSourceBytes(url);  
	            string pageSource = Encoding.GetEncoding(encodingType).GetString(pageSourceBytes);  
	            return pageSource;  
	        }  
	  
	        //Save image to local file    
	        public static void SavaImagesToFile(string url,string dirPath,string fileName)  
	        {  
	            if(!Directory.Exists(dirPath))  
	            {  
	                Directory.CreateDirectory(dirPath);  
	            }  
	            WebClient wc = new WebClient();  
	            wc.DownloadFile(url, Path.Combine(dirPath, fileName + Guid.NewGuid().ToString()));  
	        }  
	    }  
	  
	    public class ImageInfo  
	    {  
	        public string Title;  
	        public string SrcPath;  
	  
	
	    class Program  
	    {  
	        static void Main(string[] args)  
	        {  
							            int sumCount = 100;  
							            string baseUrl = "http://browse.deviantart.com/customization/wallpaper/widescreen/?order=15";  
							  
							            List<ImageInfo> imageInfoList = new List<ImageInfo>();  
							            imageInfoList = GetSumImageInfoList(sumCount, baseUrl);  
							  
							            foreach (ImageInfo imageInfo in imageInfoList)  
							            {  
							                Util.SavaImagesToFile(imageInfo.SrcPath, @"c:\Images", GetValidFilename(imageInfo.Title));  
							            }  
							  
							            return;  
							        }  
							  
							        static string GetValidFilename(string filename)  
							        {  
							            foreach (char c in Path.GetInvalidFileNameChars())  
							            {  
							                filename = filename.Replace(c, '_');  
							            }  
							            return filename;  
							        }  
							  
							        static List<ImageInfo> GetSumImageInfoList(int sum, string baseUri)  
							        {  
							            List<ImageInfo> resultList = new List<ImageInfo>();  
							            int c = (sum - 1) / 24 + 1;  
							            for (int i = 0; i < c; i++)  
							            {  
							                int offset = i * 24;  
							                string url = string.Format("{0}&offset={1}", baseUri, offset);  
							                List<ImageInfo> curResultList = ImageInfo.GetImageInfoList(url);  
							                foreach (ImageInfo imageInfo in curResultList)  
							                {  
							                    if (resultList.Count < sum)  
							                    {  
							                        resultList.Add(imageInfo);  
							                    }  
							                }  
							            }  
							            return resultList;  
							        }             
	        
	        
	        
	    }  
	 }  


 




richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



