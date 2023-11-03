package ip;

import java.io.UnsupportedEncodingException;
import java.util.StringTokenizer;
import org.apache.log4j.Level;

/**
 * �u�����A���Ѥ@�Ǥ�K����k
 */
public class Util {

	private static StringBuilder sb = new StringBuilder();

	/**
	 * �qip���r��Φ��o��r�`�}�C�Φ�
	 * 
	 * @param ip
	 *            �r��Φ���ip
	 * @return �r�`�}�C�Φ���ip
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
			LogFactory.log("�qip���r��Φ��o��r�`�}�C�Φ���ܥX��", Level.ERROR, e);
		}
		return ret;
	}

	/**
	 * @param ip
	 *            ip���r�`�}�C�Φ�
	 * @return �r��Φ���ip
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
	 * �ھڬY�ظѽX�覡�N�r�`�}�C�ഫ���r��
	 * 
	 * @param b
	 *            �r�`�}�C
	 * @param offset
	 *            �n�ഫ���_�l��m
	 * @param len
	 *            �n�ഫ������
	 * @param encoding
	 *            �ѽX�覡
	 * @return �p�Gencoding���䴩�A�Ǧ^�@�ӯʬٸѽX���r��
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
