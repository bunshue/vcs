

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TestString {
	/** �h���ϥΪ��ܤ��ݭn���s�sĶ���h��F���F�A����W�c�I�s�ണ�@�Ĳv */
	public static final String patternString1 = "[^\\s]*((<\\s*[aA]\\s+(href\\s*=[^>]+\\s*)>)(.*)</[aA]>).*";
	public static final String patternString2 = ".*(<\\s*[aA]\\s+(href\\s*=[^>]+\\s*)>(.*)</[aA]>).*";
	public static final String patternString3 = ".*href\\s*=\\s*(\"|'|)http://.*";
	public static Pattern pattern1 = Pattern.compile(patternString1,
			Pattern.DOTALL);
	public static Pattern pattern2 = Pattern.compile(patternString2,
			Pattern.DOTALL);
	public static Pattern pattern3 = Pattern.compile(patternString3,
			Pattern.DOTALL);

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		/** ���ժ���� */
		String ss = "�o�O����<a href=http://www.google.cn>www.google.cn</a>�u���O���դF";
		/** �x�s���R�X�Ӫ�url,��set�q�Y�ص{�ץh���A�u�O�r���W�A�ܩ�y�q���N�n�ݭn�Ҽ{�ܦh�F */
		Set<String> set = new HashSet<String>();
		/** �ѪRurl���x�s�bset�� */
		parseUrl(set, ss);
		/** �w��ѪR�X�Ӫ�url���B�z */
		System.out.println(replaceHtml(set, ss));

	}

	/** ���C��url�[�Wtarget�ݩ� */
	public static String replaceHtml(Set<String> set, String var) {
		String result = null;
		/** �̦n���n��Ѽƭק� */
		result = var;
		Iterator<String> ite = set.iterator();
		while (ite.hasNext()) {
			String url = ite.next();
			if (url != null) {
				result = result.replaceAll(url, url + "  target=\"_blank\"");

			}
		}
		return result;
	}

	public static void parseUrl(Set<String> set, String var) {
		Matcher matcher = null;
		String result = null;
		// ���]�̵u��a�����챵�� <a href=http://www.a.cn></a>�h�p��L�����׬�28
		if (var != null && var.length() > 28) {
			matcher = pattern3.matcher(var);
			// �T�w�y�l�̥]�t���챵
			if (matcher != null && matcher.matches()) {
				matcher = pattern1.matcher(var);
				String aString = null;
				String bString = null;

				while (matcher != null && matcher.find()) {
					if (matcher.groupCount() > 3) {
						bString = matcher.group(matcher.groupCount() - 3);// �o��group�]�t�Ҧ��ŦX���h���r��
						aString = matcher.group(matcher.groupCount() - 2);// �o��group�]�turl��html����
						String url1 = matcher.group(matcher.groupCount() - 1);// �̫�@��group�N�Ourl
						set.add(url1);// �N��쪺url�x�s�_��
						bString = bString.replaceAll(aString, "");// �h���w�g��쪺url��html����
					}

				}
				if (bString != null) {
					parseUrl(set, bString);// �~��`�����R�U�@��url
				}

			}
		}

	}

}
