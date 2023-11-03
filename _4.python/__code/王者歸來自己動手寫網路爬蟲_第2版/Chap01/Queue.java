

import java.util.LinkedList;
/**
 * 隊列，儲存將要存取的URL
 */
public class Queue {
	//使用鏈結串列實現隊列
	private LinkedList queue = new LinkedList();
    //入隊列
	public void enQueue(Object t) {
		queue.addLast(t);
	}
    //出隊列
	public Object deQueue() {
		return queue.removeFirst();
	}
    //判斷隊列是否為空
	public boolean isQueueEmpty() {
		return queue.isEmpty();
	}
    //判斷隊列是否包含t
	public boolean contians(Object t) {
		return queue.contains(t);
	}

	public boolean empty() {
		return queue.isEmpty();
	}

}
