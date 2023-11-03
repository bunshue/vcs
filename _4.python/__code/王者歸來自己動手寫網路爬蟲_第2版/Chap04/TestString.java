

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TestString {
	/** 多次使用的話不需要重新編譯正則表達式了，對於頻繁呼叫能提昇效率 */
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
		/** 測試的資料 */
		String ss = "這是測試<a href=http://www.google.cn>www.google.cn</a>真的是測試了";
		/** 儲存分析出來的url,用set從某種程度去重，只是字面上，至於語義那就要需要考慮很多了 */
		Set<String> set = new HashSet<String>();
		/** 解析url並儲存在set裡 */
		parseUrl(set, ss);
		/** 針對解析出來的url做處理 */
		System.out.println(replaceHtml(set, ss));

	}

	/** 給每個url加上target屬性 */
	public static String replaceHtml(Set<String> set, String var) {
		String result = null;
		/** 最好不要對參數修改 */
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
		// 假設最短的a標籤鏈接為 <a href=http://www.a.cn></a>則計算他的長度為28
		if (var != null && var.length() > 28) {
			matcher = pattern3.matcher(var);
			// 確定句子裡包含有鏈接
			if (matcher != null && matcher.matches()) {
				matcher = pattern1.matcher(var);
				String aString = null;
				String bString = null;

				while (matcher != null && matcher.find()) {
					if (matcher.groupCount() > 3) {
						bString = matcher.group(matcher.groupCount() - 3);// 這個group包含所有符合正則的字串
						aString = matcher.group(matcher.groupCount() - 2);// 這個group包含url的html標籤
						String url1 = matcher.group(matcher.groupCount() - 1);// 最後一個group就是url
						set.add(url1);// 將找到的url儲存起來
						bString = bString.replaceAll(aString, "");// 去掉已經找到的url的html標籤
					}

				}
				if (bString != null) {
					parseUrl(set, bString);// 繼續循環分析下一個url
				}

			}
		}

	}

}
