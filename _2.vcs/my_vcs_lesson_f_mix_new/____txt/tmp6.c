



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

