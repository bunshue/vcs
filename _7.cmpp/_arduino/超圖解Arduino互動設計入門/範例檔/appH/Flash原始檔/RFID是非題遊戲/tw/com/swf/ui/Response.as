package tw.com.swf.ui {
	import flash.display.MovieClip;
	import flash.display.SimpleButton;
	import flash.events.Event;
	import flash.events.MouseEvent;
	
	public class Response extends MovieClip {
		public static const POP:String = "pop";
		public static const CLICK_BUTTON:String = "clickButton";
		public var nexQ_btn:SimpleButton;
		public var END_btn:SimpleButton;
		
		public var right:int = 0;	// 紀錄正確作答的次數
		public var wrong:int = 0;	// 紀錄錯誤作答的次數
		
		/*
		標示面板的顯示狀態，若還有題目，面板的狀態是「玩」；
		若已經沒有題目，面板的狀態是「完」。
		*/
		private var _status:String = "玩";	
		
		public function Response() {
			this.addEventListener(Event.ADDED, init);
		}
		
		private function init(e:Event):void {
			// 設定「下一題」和「結束」鈕的事件處理程式
			nexQ_btn.addEventListener(MouseEvent.CLICK, doClick);
			END_btn.addEventListener(MouseEvent.CLICK, doClick);
			/* 
			  當此面板顯示在畫面上時，面板內部的時間軸將觸發"POP"事件，
			  事件程式將藉此更新面板的狀態。
			*/
			addEventListener(POP, updateMyStatus);
			removeEventListener(Event.ADDED, init);
		}
		
		private function doClick(e:MouseEvent):void {
			dispatchEvent(new Event(CLICK_BUTTON));
		}
		
		private function updateMyStatus(e:Event):void {
			// 如果面板呈現的影格標籤名稱不是"結束"，代表還有題目。
			if (this.currentFrameLabel != "結束") {
				_status = "玩";
			} else {
				_status = "完";
			}
		}
		
		// 提供外部程式讀取「面板狀態（status）」值
		public function get status():String {
			return _status;
		}
		
	}
	
}
