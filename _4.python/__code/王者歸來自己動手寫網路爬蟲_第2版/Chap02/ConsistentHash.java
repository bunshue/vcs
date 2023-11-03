
import java.util.Collection;
import java.util.SortedMap;
import java.util.TreeMap;

public class ConsistentHash<T> {
	 private final HashFunction hashFunction;// hash算法
	 private final int numberOfReplicas;// 虛擬節點數目
	 private final SortedMap<Integer, T> circle = new TreeMap<Integer, T>();
	 public ConsistentHash(HashFunction hashFunction, int numberOfReplicas,
	     Collection<T> nodes){ // 實體節點
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

	 public T get(Object key) {// 關鍵算法
	   if (circle.isEmpty()) {
	     return null;
	   }
	   // 計算hash值
	   int hash = hashFunction.hash(key);
	   // 如果不包括這個hash值
	   if (!circle.containsKey(hash)) {
	     SortedMap<Integer, T> tailMap = circle.tailMap(hash);
	     hash = tailMap.isEmpty() ? circle.firstKey() : tailMap.firstKey();
	   }
	   return circle.get(hash);
	 }
}
	 
