

import java.util.LinkedList;
/**
 * ���C�A�x�s�N�n�s����URL
 */
public class Queue {
	//�ϥ��쵲��C��{���C
	private LinkedList queue = new LinkedList();
    //�J���C
	public void enQueue(Object t) {
		queue.addLast(t);
	}
    //�X���C
	public Object deQueue() {
		return queue.removeFirst();
	}
    //�P�_���C�O�_����
	public boolean isQueueEmpty() {
		return queue.isEmpty();
	}
    //�P�_���C�O�_�]�tt
	public boolean contians(Object t) {
		return queue.contains(t);
	}

	public boolean empty() {
		return queue.isEmpty();
	}

}
