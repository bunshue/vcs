

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.Queue;
public class LinkQueue {
	//已存取的 url 集合
	private static Set visitedUrl = new HashSet();
	//待存取的 url 集合
	private static Queue unVisitedUrl = new PriorityQueue();

	//獲得URL隊列
	public static Queue getUnVisitedUrl() {
		return unVisitedUrl;
	}
    //增加到存取過的URL隊列中
	public static void addVisitedUrl(String url) {
		visitedUrl.add(url);
	}
    //移除存取過的URL
	public static void removeVisitedUrl(String url) {
		visitedUrl.remove(url);
	}
    //未存取的URL出隊列
	public static Object unVisitedUrlDeQueue() {
		return unVisitedUrl.poll();
	}

	// 保證每個 url 只被存取一次
	public static void addUnvisitedUrl(String url) {
		if (url != null && !url.trim().equals("")
 && !visitedUrl.contains(url)
				&& !unVisitedUrl.contains(url))
			unVisitedUrl.add(url);
	}
    //獲得已經存取的URL數目
	public static int getVisitedUrlNum() {
		return visitedUrl.size();
	}
    //判斷未存取的URL隊列中是否為空
	public static boolean unVisitedUrlsEmpty() {
		return unVisitedUrl.isEmpty();
	}

}
