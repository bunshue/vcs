# Bottom_Control 
                                                           關于說明  
1: 無代碼訪問PLC的控件 通過Visual Studio 拖拽控件設置相應的參數就可以訪問PLC簡單易用 適用于工業開發作為底層減少項目代碼量提高穩定性  正在全力開發  
2:視頻展示鏈接：https://pan.baidu.com/s/12TFRdkp64Kqo6_oK1gdbNw 提取碼: lo33  
3:項目控件使用視頻展示 https://pan.baidu.com/s/1Sd7JBtRMBqxguB0ZFbR3Zg 提取碼： pkve   
![image](https://user-images.githubusercontent.com/60955669/109391193-d1d9f980-7950-11eb-9e46-09c125089a27.png)

                                                           使用步驟 
1：先拖拽plC_Open_Time1控件   
2：設置好相應的PLC參數  
3：然后拖拽出DAButton1控件  
4：設置好PLC類型參數  
5：在FORM窗口的Load 事件添加上plC_Open_Time1.Enabled = true;  
6：plC_Open_Time1.Start(); 以上代碼   

                                                           注意  
 1：plC_Open_Time1控件只能使用一次  否則報錯    
 2: 清理解決方案會導致plC_Open_Time1控件出現錯誤（已修復）   
 3:有些控件需要配合SQL 數據庫使用前要熟知 否則出現報錯導致項目崩潰不負責  
 
                                                   關于用戶自定義控件   
 1:控件類型分為Bit位線圈操作類型與字雙字操作類型   
 2:分別繼承類基Button_base TextBox_base實現了就可以設置相應的參數  
 3:控件操作PLC--Bit位 通過實例化Button_PLC類 調用plc(this)方法 方可 反之字操作類型實例化TextBox_PLC類型  
 4:每個控件都自帶 System.Windows.Forms.Timer類型的定時器作為刷新UI  
 5:西門子S200 smart 訪問V區 輸入方式為DB 1.0 這樣就是訪問VB0
 
 
  關于轉換成Dll引用到其他項目的方法：  
1.先把項目轉換成類庫然后編譯     
2.編譯成功后去項目的DEbug文件夾把全部dll引導到你的項目  
3.然后找到Bottom_Control.dll拖拽到IDE拖拽控件處更待IDE更新就可以拖拽控件方式  
4.可以引用完成后直接清理解決方案然后重新生產的方法  