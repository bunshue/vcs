package tw.com.swf
{
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.display.MovieClip;
	import flash.display.SimpleButton;
	import flash.text.TextField;
	
	import tw.com.swf.ui.Response;		// 顯示答對、答錯以及最後成績的「回應」面板
	import tw.com.swf.model.Data;		// 讀取題目XML檔案的類別程式
	import tw.com.swf.model.RFID;		// 連結Arduino，並讀取RFID值的類別程式
	import tw.com.swf.events.RFIDEvent;
	import flash.utils.Timer;
	import flash.events.TimerEvent;

	// 自訂的RFID事件，內含讀取到的標籤值。

	public class Main extends MovieClip
	{
		private var _mode:String = "mouse";	// 操作模式設定，預設為「滑鼠」。
		private var quizArray:Array = [];	// 儲存題目內容的陣列
		private var currentQ:int = 0;		// 記錄目前出題編號
		private var totalQ:int;				// 記錄題目總數
		private var d:Data;					// 讀取外部XML題目檔案的類別物件
		private var rfid:RFID;				// 讀取RFID資料的類別物件
		private var rfidEnabled:Boolean = false;	// 標示程式是否能讀取RFID的變數
		private var rfidDelay:int = 1500; 	// RFID模式，介面預設等1.5秒鐘之後，才開放感應。
		private var rfidTimer:Timer;
		
		// 使用者介面（UI）元素
		public var drQ:MovieClip;			// 出題者角色
		public var bian:MovieClip;			// 玩家角色
		public var resp:Response;			// 顯示答對、答錯以及最後成績的「回應」面板
		public var quizDialog:MovieClip;	// 顯示問題的面板
		public var btn1:MovieClip;			// 「對（O）」鈕
		public var btn0:MovieClip;			// 「錯（X）」鈕
		public var currentTxt:TextField;	// 顯示目前題目編號的文字欄位
		public var totalTxt:TextField;		// 顯示題目總數的文字欄位

		public function Main()
		{
			rfidTimer =  new Timer(rfidDelay, 1);
			rfidTimer.addEventListener(TimerEvent.TIMER_COMPLETE, onRFIDTimeUp);
		}

		// 初始化主程式，外部程式將傳入題目XML的路徑和檔名，以及操作模式（預設為滑鼠）。
		public function init(url:String, _m:String = "mouse"):void
		{
			_mode = _m; 
			// 若操作模式為Arduino，則需要初始化連線（位於RFID類別程式中）。
			if (_mode == "arduino")
			{
				if (rfid is RFID) {
					// 重新連線！
					rfid.openConnection();
				} else {
					rfid = new RFID(5331);
					rfid.addEventListener(RFIDEvent.READ_TAG, onReadTag);	// 若讀取到標籤，程式將自動執行onReadTag函數。
				}
			}
			// 設置問題的面板，在收到問題之前，先停在第一個畫面。
			quizDialog.stop();
			// 當問題資料準備好時，它將自動觸發onQuizReady函數。
			quizDialog.addEventListener(quizDialog.QUIZ_READY, onQuizReady);
			
			// 顯示答對或答錯的回應面板，一開始先隱藏它。
			resp.stop();
			resp.visible = false;
			// 當回應面板裡的「下一題」或「結束」鈕被按下時，onClickResponseButton()函數將被執行。
			resp.addEventListener(Response.CLICK_BUTTON, onClickResponseButton);
			// 當回應面板被開啟時，onResponsePop()函數將被執行。
			resp.addEventListener(Response.POP, onResponsePop);
			
			// 設置O, X作答鈕
			// 啟用元件的「按鈕」模式，此舉將令影片片段元件具備按鈕的行為。
			btn0.buttonMode = true;
			btn1.buttonMode = true;
			// 題目出現之前，暫時停止回應滑鼠，亦即，不理會游標滑入與按下的事件。
			btn0.mouseEnabled = false;
			btn1.mouseEnabled = false;
			// 設定這兩個按鈕的「按一下」處理事件
			btn0.addEventListener(MouseEvent.CLICK, doClick);
			btn1.addEventListener(MouseEvent.CLICK, doClick);

			// 若儲存問題資料的quizArray陣列內容是空的，則需要載入外部的題目XML。
			if (quizArray.length == 0)
			{
				d = new Data(url);
				d.addEventListener(Data.DATA_READY, onDataReady);
			}
			else	// 否則，就開始顯示第一題。
			{
				totalTxt.text = String(totalQ);
				showQuiz();
				quizDialog.play();
				// 停止讀取RFID標籤值
				rfidEnabled = false;
			}
		}

		// 新的問題出現在螢幕上了
		private function onQuizReady(e:Event):void
		{
			// 設定畫面上兩個角色的表情狀態
			drQ.gotoAndStop("問");
			bian.gotoAndStop("茫");
			// 啟用O與X按鈕
			btn0.mouseEnabled = true;
			btn1.mouseEnabled = true;
			// 啟動允許讀取RFID標籤值的計時器
			rfidTimer.start();
		}

		// 「回應」面板出現了
		private function onResponsePop(e:Event):void
		{
			// 啟動允許讀取RFID標籤值的計時器
			rfidTimer.start();
		}


		private function onRFIDTimeUp(e:TimerEvent):void {
			// 開放讀取RFID標籤值
			rfidEnabled = true;
		}

		private function onReadTag(e:RFIDEvent):void
		{
			/* 
				讀取標籤所代表的「意義」值，例如，答案編號0或1
				而非標籤的編碼（請參閱RFID.as檔）
			*/
			var ans:Number = Number(e.tag);

			if (rfidEnabled)
			{
				// 若目前操作的是作答畫面（亦即，出現在畫面上的不是「回應」面版）…
				if (! resp.visible)
				{
					// 檢查答案是否正確
					checkAns(ans);
				}
				else
				{
					// 出現在畫面上的是「回應」面板，用任何標籤都能觸發「下一題」或「結束」按鈕。
					if (ans != -1)
					{
						closeResponse();
					}
				}
			}
		}

		/*
			讀入並解析外部的XML題目內容後，
			需要顯示題目總數，
			並開始讓用戶作答。
		*/
		private function onDataReady(e:Event):void
		{
			// 儲存RFID標籤資料
			if (_mode == "arduino") {
				// 設定標籤的編碼和答案編號資料
				rfid.tags = d.tagArray;
				// 設定延遲時間
				rfidDelay = d.delay;
				trace("delay data: " + d.delay);
			}
			// 儲存問題資料
			quizArray = d.quizArray;
			d.removeEventListener(Data.DATA_READY, onDataReady);
			d = null;
			totalQ = quizArray.length;
			totalTxt.text = String(totalQ);
			showQuiz();
			quizDialog.play();
			// 停止讀取RFID標籤值
			rfidEnabled = false;
		}

		// 顯示題目以及題目的編號
		private function showQuiz():void
		{
			quizDialog.q_txt.text = quizArray[currentQ].txt;
			quizDialog.ans = int(quizArray[currentQ].ans);
			currentTxt.text = String(currentQ + 1);
			if (currentQ < totalQ)
			{
				currentQ++;
			}
		}

		// 處理用戶按下O和X鈕的事件
		private function doClick(e:MouseEvent):void
		{
			/*
				底下敘述中的3，代表取出按鈕名稱裡的第3個字（從0開始算起），
				亦即，"btn1"裡的1，當做用戶的作答編號。
			*/
			var n:int = int(e.target.name.charAt(3));
			btn0.mouseEnabled = false;
			btn1.mouseEnabled = false;
			// 檢查答案
			checkAns(n);
		}
		
		// 檢查答案是否正確
		private function checkAns(n:int):void
		{
			if (quizDialog.ans == n)
			{
				resp.right++;		// 增加答對的次數
				resp.gotoAndPlay("讚");
				bian.gotoAndStop("讚");
			}
			else
			{
				resp.wrong++;		// 增加答錯的次數
				resp.gotoAndPlay("蛤");
				bian.gotoAndStop("蛤");
			}
			drQ.gotoAndStop("答");
			resp.visible = true;	// 顯示「回應」面板
			rfidEnabled = false;	// 停止讀取RFID標籤值
		}
		
		private function onClickResponseButton(e:Event):void {
			closeResponse();
		}
	
		/*
			當用戶按下「回應」面板裡的「下一題」或「結束」鈕，將觸發執行底下的函數。
		*/
		private function closeResponse():void
		{
			var s:String = resp.status;

			if (s == "玩")		// 若目前的狀態是「玩」
			{
				if (currentQ != totalQ)		// 若尚有題目，則顯示新題目。
				{
					resp.visible = false;
					quizDialog.play();
					showQuiz();
				}
				else						// 否則，顯示「成績」畫面
				{
					resp.gotoAndPlay("完");
				}
				rfidEnabled = false;
			}
			else			// 若目前的狀態是「完」，代表顯示的是「成績」畫面
			{
				if (_mode == "arduino") {
					rfid.closeConnection();
				}
				currentQ = 0;
				prevScene();	// 回到上一個場景（開始畫面）
			}
		}
	}
}