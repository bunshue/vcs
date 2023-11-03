
import java.util.Collection;
import java.util.SortedMap;
import java.util.TreeMap;

public class ConsistentHash<T> {
	 private final HashFunction hashFunction;// hash��k
	 private final int numberOfReplicas;// �����`�I�ƥ�
	 private final SortedMap<Integer, T> circle = new TreeMap<Integer, T>();
	 public ConsistentHash(HashFunction hashFunction, int numberOfReplicas,
	     Collection<T> nodes){ // ����`�I
	   this.hashFunction = hashFunction;
	   this.numberOfReplicas = numberOfReplicas;
	   for (T node : nodes) {
	     add(node);
	   }
	 }

	 public void add(T node) {
	   for (int i = 0; i < numberOfReplicas; i++) {
	     circle.put(hashFunction.hash(node.toString() + i), node);
	   }
	 }

	 public void remove(T node) {
	   for (int i = 0; i < numberOfReplicas; i++) {
	     circle.remove(hashFunction.hash(node.toString() + i));
	   }
	 }

	 public T get(Object key) {// �����k
	   if (circle.isEmpty()) {
	     return null;
	   }
	   // �p��hash��
	   int hash = hashFunction.hash(key);
	   // �p�G���]�A�o��hash��
	   if (!circle.containsKey(hash)) {
	     SortedMap<Integer, T> tailMap = circle.tailMap(hash);
	     hash = tailMap.isEmpty() ? circle.firstKey() : tailMap.firstKey();
	   }
	   return circle.get(hash);
	 }
}
	 
