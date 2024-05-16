package tw.com.swf.model
{
	import org.p43d.arduino.Arduino;
	import org.p43d.arduino.ArduinoEvent;
	import tw.com.swf.events.RFIDEvent;
	import flash.events.EventDispatcher;

	public class RFID extends EventDispatcher
	{
		private var a:Arduino;
		// 記錄每個標籤的編碼，以及它所代表的意義，例如，答案0和答案1。
		private var myTags:Array = [];
		// 記錄RFID標籤的總數
		private var totalTags:int = 0;
		private var connected:Boolean = false;

		public function RFID(port:Number = 5331)
		{
			a = new Arduino(port);// 設定serProxy軟體的埠號
			a.addEventListener(ArduinoEvent.ON_RECEIVE_DATA, receiveData);
			a.addEventListener(ArduinoEvent.ON_CONNECT, connectRFID);
			a.addEventListener(ArduinoEvent.ON_CLOSE, closed);
			a.connect();
		}
		
		// 設定標籤的資料
		public function set tags(t:Array):void {
			myTags = t;
			totalTags = t.length;
		}
		
		private function connectRFID(e:ArduinoEvent):void {
			connected = true;
		}
		
		private function closed(e:ArduinoEvent):void {
			connected = false;
		}
		
		public function closeConnection():void {
			a.disconnect();
		}
		
		public function openConnection():void {
			a.connect();
		}

		// 每當Arduino有新資料傳入時，底下的事件函數將被自動執行。
		private function receiveData(e:ArduinoEvent):void
		{
			// 讀取Arduino傳入的資料
			var tag:String = e.data;
			// 儲存標籤答案
			var ans:Number;
			// 逐一比對傳入的標籤值與程式裡的記錄
			for (var i:int = 0; i < totalTags; i++) {
				// 若找到相符的標籤
				if (tag == myTags[i].id) {
					ans = myTags[i].ans;		// 記下它所代表的答案編號
					break;
				} else {
					ans = -1;					// 沒找到標籤，用-1代表。
				}
			}
			// 輸出標籤的編碼，不用這一個。
			// this.dispatchEvent(new RFIDEvent(RFIDEvent.READ_TAG, tag));
			// 輸出標籤所代表的答案編號，採用這一個。
			this.dispatchEvent(new RFIDEvent(RFIDEvent.READ_TAG, ans));
		}
	}
}
