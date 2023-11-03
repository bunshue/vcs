package ip;

import java.io.UnsupportedEncodingException;
import java.util.StringTokenizer;
import org.apache.log4j.Level;

/**
 * 工具類，提供一些方便的方法
 */
public class Util {

	private static StringBuilder sb = new StringBuilder();

	/**
	 * 從ip的字串形式得到字節陣列形式
	 * 
	 * @param ip
	 *            字串形式的ip
	 * @return 字節陣列形式的ip
	 */
	public static byte[] getIpByteArrayFromString(String ip) {
		byte[] ret = new byte[4];
		StringTokenizer st = new StringTokenizer(ip, ".");
		try {
			ret[0] = (byte) (Integer.parseInt(st.nextToken()) & 0xFF);
			ret[1] = (byte) (Integer.parseInt(st.nextToken()) & 0xFF);
			ret[2] = (byte) (Integer.parseInt(st.nextToken()) & 0xFF);
			ret[3] = (byte) (Integer.parseInt(st.nextToken()) & 0xFF);
		} catch (Exception e) {
			LogFactory.log("從ip的字串形式得到字節陣列形式顯示出錯", Level.ERROR, e);
		}
		return ret;
	}

	/**
	 * @param ip
	 *            ip的字節陣列形式
	 * @return 字串形式的ip
	 */
	public static String getIpStringFromBytes(byte[] ip) {
		sb.delete(0, sb.length());
		sb.append(ip[0] & 0xFF);
		sb.append('.');
		sb.append(ip[1] & 0xFF);
		sb.append('.');
		sb.append(ip[2] & 0xFF);
		sb.append('.');
		sb.append(ip[3] & 0xFF);
		return sb.toString();
	}

	/**
	 * 根據某種解碼方式將字節陣列轉換成字串
	 * 
	 * @param b
	 *            字節陣列
	 * @param offset
	 *            要轉換的起始位置
	 * @param len
	 *            要轉換的長度
	 * @param encoding
	 *            解碼方式
	 * @return 如果encoding不支援，傳回一個缺省解碼的字串
	 */
	public static String getString(byte[] b, int offset, int len,
			String encoding) {
		try {
			return new String(b, offset, len, encoding);
		} catch (UnsupportedEncodingException e) {
			return new String(b, offset, len);
		}
	}
}
