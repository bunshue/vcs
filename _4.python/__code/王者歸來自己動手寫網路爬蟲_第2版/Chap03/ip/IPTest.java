package ip;

public class IPTest {

	public static void main(String[] args) {
		// ���w�¯u��Ʈw���ɮצW�A�Ҧb�ɮק�
		IPSeeker ip = new IPSeeker("QQWry.Dat", "c:\\qqwry");
		// ����IP 58.20.43.13
		System.out.println(ip.getIPLocation("58.20.43.13").getCountry() + ":"
				+ ip.getIPLocation("58.20.43.13").getArea());
	}
}
