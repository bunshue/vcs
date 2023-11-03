

import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.Queue;
public class LinkQueue {
	//�w�s���� url ���X
	private static Set visitedUrl = new HashSet();
	//�ݦs���� url ���X
	private static Queue unVisitedUrl = new PriorityQueue();

	//��oURL���C
	public static Queue getUnVisitedUrl() {
		return unVisitedUrl;
	}
    //�W�[��s���L��URL���C��
	public static void addVisitedUrl(String url) {
		visitedUrl.add(url);
	}
    //�����s���L��URL
	public static void removeVisitedUrl(String url) {
		visitedUrl.remove(url);
	}
    //���s����URL�X���C
	public static Object unVisitedUrlDeQueue() {
		return unVisitedUrl.poll();
	}

	// �O�ҨC�� url �u�Q�s���@��
	public static void addUnvisitedUrl(String url) {
		if (url != null && !url.trim().equals("")
 && !visitedUrl.contains(url)
				&& !unVisitedUrl.contains(url))
			unVisitedUrl.add(url);
	}
    //��o�w�g�s����URL�ƥ�
	public static int getVisitedUrlNum() {
		return visitedUrl.size();
	}
    //�P�_���s����URL���C���O�_����
	public static boolean unVisitedUrlsEmpty() {
		return unVisitedUrl.isEmpty();
	}

}
