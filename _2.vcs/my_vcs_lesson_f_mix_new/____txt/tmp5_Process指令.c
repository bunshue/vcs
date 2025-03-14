C#通用類庫--DOS常用命令

using System.Diagnostics;
using System.Runtime.InteropServices;

namespace Ecan
{
    public class EcanDOS
    {
        //引入API函數
        [DllImportAttribute("user32.dll")]
        private static extern int FindWindow(string ClassName, string WindowName);
        [DllImport("user32.dll")]
        private static extern int ShowWindow(int handle, int cmdShow);
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        private static extern int mciSendString(string lpstrCommand, string lpstrReturnstring, int uReturnLength, int hwndCallback);

        private const int SW_HIDE = 0;//API參數表示隱藏窗口
        private const int SW_SHOW = 5;//API參數表示用當前的大小和位置顯示窗口

//彈出光驅()
        {
            mciSendString("set CDAudio door open", null, 127, 0);
        }

//關閉光驅()
        {
            mciSendString("set CDAudio door closed", null, 127, 0);
        }

//打開C盤()
        {
            Process.Start("c:\\");
        }

//打開D盤()
        {
            Process.Start("d:\\");
        }

//打開E盤()
        {
            Process.Start("e:\\");
        }

//打開F盤()
        {
            Process.Start("f:\\");
        }

//打開指定盤(string hardpath)
        {
            Process.Start(hardpath);
        }

//打開Word()
        {
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE11\winword.exe");
        }

//打開Excel()
        {
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE11\excel.exe");
        }

//打開Access()
        {
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE11\msaccess.exe");
        }

//打開PowerPoint()
        {
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE11\powerpnt.exe");
        }

//打開OutLook()
        {
            Process.Start(@"C:\Program Files\Microsoft Office\OFFICE11\outlook.exe");
        }

//打開記事本()
        {
            Process.Start("notepad.exe");
        }

//打開計算器()
        {
            Process.Start("calc.exe");
        }

//打開DOS命令窗口()
        {
            Process.Start("cmd.exe");
        }

//打開注冊表()
        {
            Process.Start("regedit.exe");
        }

//打開畫圖板()
        {
            Process.Start("mspaint.exe");
        }

//打開寫字板()
        {
            Process.Start("write.exe");
        }

//打開播放器()
        {
            Process.Start("mplayer2.exe");
        }

//打開資源管理器()
        {
            Process.Start("explorer.exe");
        }

//打開任務管理器()
        {
            Process.Start("taskmgr.exe");
        }

//打開事件查看器()
        {
            Process.Start("eventvwr.exe");
        }

//打開系統信息()
        {
            Process.Start("winmsd.exe");
        }

//打開備份還原()
        {
            Process.Start("ntbackup.exe");
        }

//打開Windows版本()
        {
            Process.Start("winver.exe");
        }

//打開控制面板()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");
        }

//打開控制面板輔助選項鍵盤()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,1");
        }

//打開控制面板輔助選項聲音()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,2");
        }

//打開控制面板輔助選項顯示()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,3");
        }

//打開控制面板輔助選項鼠標()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,4");
        }

//打開控制面板輔助選項常規()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL access.cpl,,5");
        }

//打開控制面板添加新硬件向導()
        {
            Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL sysdm.cpl @1");
        }

//打開控制面板添加新打印機向導()
        {
            Process.Start("rundll32.exe", "shell32.dll,SHHelpShortcuts_RunDLL AddPrinter");
        }

//打開控制面板添加刪除程序安裝卸載面板()
        {
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,1");
        }

//打開控制面板添加刪除程序安裝Windows面板()
        {
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,2");
        }

//打開控制面板添加刪除程序啟動盤面板()
        {
            Process.Start("rundll32.exe", "shell32.dll,shell32.dll,Control_RunDLL appwiz.cpl,,3");
        }

//打開建立快捷方式對話框()
        {
            Process.Start("rundll32.exe", " appwiz.cpl,NewLinkHere %1");
        }

//打開日期時間選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL timedate.cpl,,0");
        }

//打開時區選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL timedate.cpl,,1");
        }

//建立公文包()
        {
            Process.Start("rundll32.exe", " syncui.dll,Briefcase_Create");
        }

//打開復制軟碟窗口()
        {
            Process.Start("rundll32.exe", " diskcopy.dll,DiskCopyRunDll");
        }

//打開新建撥號連接()
        {
            Process.Start("rundll32.exe", " rnaui.dll,RnaWizard");
        }

//打開顯示屬性背景()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,0");
        }

//打開顯示屬性屏幕保護()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,1");
        }

//打開顯示屬性外觀()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,2");
        }

//打開顯示屬性屬性()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL desk.cpl,,3");
        }

//打開格式化對話框()
        {
            Process.Start("rundll32.exe", " shell32.dll,SHFormatDrive");
        }

//打開控制面板游戲控制器一般()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL joy.cpl,,0");
        }

//打開控制面板游戲控制器進階()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL joy.cpl,,1");
        }

//打開控制面板鍵盤屬性速度()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL main.cpl @1");
        }

//打開控制面板鍵盤屬性語言()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL main.cpl @1,,1");
        }

//打開Windows打印機檔案夾()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL main.cpl @2");
        }

//打開Windows字體檔案夾()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL main.cpl @3");
        }

//打開控制面板輸入法屬性()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL main.cpl @4");
        }

//打開添加新調制解調器向導()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL modem.cpl,,add");
        }

//打開控制面板多媒體屬性音頻()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl,,0");
        }

//打開控制面板多媒體屬性視頻()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl,,1");
        }

//打開控制面板多媒體屬性MIDI()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl,,2");
        }

//打開控制面板多媒體屬性CD音樂()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl,,3");
        }

//打開控制面板多媒體屬性設備()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl,,4");
        }

//打開控制面板聲音()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL mmsys.cpl @1");
        }

//打開控制面板網絡()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL netcpl.cpl");
        }

//打開控制面板密碼()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL password.cpl");
        }

//打開控制面板電源管理()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL powercfg.cpl");
        }

//打開控制面板區域設置屬性區域設置()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL intl.cpl,,0");
        }

//打開控制面板區域設置屬性數字選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL intl.cpl,,1");
        }

//打開控制面板區域設置屬性貨幣選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL intl.cpl,,2");
        }

//打開控制面板區域設置屬性時間選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL intl.cpl,,3");
        }

//打開控制面板區域設置屬性日期選項()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL intl.cpl,,4");
        }

//打開ODBC數據源管理器()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL odbccp32.cpl");
        }

//打開控制面板系統屬性常規()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL sysdm.cpl,,0");
        }

//打開控制面板系統屬性設備管理器()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL sysdm.cpl,,1");
        }

//打開控制面板系統屬性硬件配置()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL sysdm.cpl,,2");
        }

//打開控制面板系統屬性性能()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL sysdm.cpl,,3");
        }

        /*shutdown -s -t 3600 -f 
        一小時后強行關機 用強行主要怕有些程序卡住 關不了機 
        -s 關機 
        -r重啟 
        -f強行 
        -t 時間 
        -a 取消關機 
        -l 注銷 
        -i 顯示用戶界面 具體是什么試試就知道了*/

//關閉并重啟計算機()
        {
            Process.Start("shutdown.exe", "-r");
        }

//關閉計算機()
        {
            Process.Start("shutdown.exe", "-s -f");
        }
        //重載關閉計算機函數，可以設定倒計時
//關閉計算機(string time)
        {
            string s = "-s -t " + time;
            Process.Start("shutdown.exe", s);
        }

//注銷計算機()
        {
            Process.Start("shutdown.exe", "-l");
        }

//撤銷關閉計算機()
        {
            Process.Start("shutdown.exe", "-a");
        }

//打開桌面主旨面板()
        {
            Process.Start("rundll32.exe", " shell32.dll,Control_RunDLL themes.cpl");
        }

//打開網址(string address)
        {
            Process.Start(address);
        }

//運行程序(string name)
        {
            Process.Start(name);
        }

//顯示任務欄()
        {
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_SHOW);
        }

//隱藏任務欄()
        {
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_HIDE);
        }

//發送郵件(string address)
        {
            string s = "mailto:" + address;
            Process.Start(s);
        }

//發送郵件()
        {
            Process.Start("mailto:feiyangqingyun@163.com");
        }

        public string 獲取系統文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.System);
            return s;
        }

//打開系統文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.System);
            Process.Start(s);
        }

        public string 獲取ProgramFiles目錄()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFiles);
            return s;
        }

//打開ProgramFiles目錄()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.ProgramFiles);
            Process.Start(s);
        }

        public string 獲取邏輯桌面()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            return s;
        }

//打開邏輯桌面()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            Process.Start(s);
        }

        public string 獲取啟動程序組()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Startup);
            return s;
        }

//打開啟動程序組()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Startup);
            Process.Start(s);
        }

        public string 獲取Cookies文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Cookies);
            return s;
        }

//打開Cookies文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.Cookies);
            Process.Start(s);
        }

        public string 獲取Internet歷史文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.History);
            return s;
        }

//打開Internet歷史文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.History);
            Process.Start(s);
        }

        public string 獲取我的電腦文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyComputer);
            return s;
        }

//打開我的電腦文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyComputer);
            Process.Start(s);
        }

        public string 獲取MyMusic文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyMusic);
            return s;
        }

//打開MyMusic文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyMusic);
            Process.Start(s);
        }

        public string 獲取MyPictures文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyPictures);
            return s;
        }

//打開MyPictures文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.MyPictures);
            Process.Start(s);
        }

        public string 獲取StartMenu文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.StartMenu);
            return s;
        }

//打開StartMenu文件夾()
        {
            string s = Environment.GetFolderPath(Environment.SpecialFolder.StartMenu);
            Process.Start(s);
        }       
    }
}

