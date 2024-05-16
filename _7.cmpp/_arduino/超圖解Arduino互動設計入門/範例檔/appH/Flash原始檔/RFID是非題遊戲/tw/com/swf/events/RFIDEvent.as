package tw.com.swf.events {
	import flash.events.Event;
	
	public class RFIDEvent extends Event {
		public static const READ_TAG:String = "readTag";
		public var tag:*;

		public function RFIDEvent(type:String, customArg:*=null,
                                  bubbles:Boolean=false,
                                  cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
	        this.tag = customArg;
		}
		
		public override function clone():Event {
			return new RFIDEvent(type, tag, bubbles, cancelable);
      	}
     
      	public override function toString():String {
        	return formatToString("RFIDEvent", "type", "tag", "bubbles", "cancelable", "eventPhase");
        }
	}
	
}
