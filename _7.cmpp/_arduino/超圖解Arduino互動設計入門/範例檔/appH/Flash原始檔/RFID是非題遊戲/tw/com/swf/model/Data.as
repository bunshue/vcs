package tw.com.swf.model
{
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.events.EventDispatcher;
	import flash.events.Event;

	public class Data extends EventDispatcher
	{
		public static const DATA_READY:String = "dataReady";
		// 存放問題的陣列
		private var _quizArray:Array = [];
		// 存放標籤的陣列
		private var _tagArray:Array = [];
		// 存放讀取RFID標籤的延遲時間值，預設為1500ms
		private var _delay:int = 1500;
		private var quizLoader:URLLoader = new URLLoader();
		
		// 載入指定的XML檔
		public function Data(url:String)
		{
			quizLoader.addEventListener(Event.COMPLETE, onQuizLoaded);
			loadQuiz(url);
		}

		private function onQuizLoaded(e:Event):void
		{
			processQuiz(e.target.data);
			dispatchEvent(new Event(DATA_READY));
			quizLoader.removeEventListener(Event.COMPLETE, onQuizLoaded);
		}

		private function processQuiz(str:String):void
		{
			var quiz:XML = new XML(str);
			var q:XMLList = quiz..q;
			var tag:XMLList = quiz..t;
			var totalQ = q.length();
			var totalTags = tag.length();
			// 讀取延遲時間設定值
			_delay = int(quiz.RFID.@delay);
			
			// 取出XML題目檔裡的每一題，將題目與解答存入_quizArray陣列。
			for (var i:int = 0; i < totalQ; i++)
			{
				var objQ:Object = {};
				objQ.txt = q[i]. @ txt;
				objQ.ans = Number(q[i]. @ ans);
				_quizArray[i] = objQ;
			}
			
			// 取出XML題目檔裡的RFID值，將編碼與答案編號存入_tagArray陣列。
			for (i = 0; i < totalTags; i++)
			{
				var objT:Object = {};
				objT.id = tag[i]. @ id;
				objT.ans = Number(tag[i]. @ ans);
				_tagArray[i] = objT;
			}
		}

		private function loadQuiz(url:String):void
		{
			try
			{
				quizLoader.load(new URLRequest(url));
			}
			catch (e:Error)
			{
				trace("無法載入題目檔！");
			}
		}
		
		public function get quizArray():Array {
			return _quizArray;
		}
		
		public function get tagArray():Array {
			return _tagArray;
		}
		
		public function get delay():int {
			return _delay;
		}
	}
}