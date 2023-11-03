package ip;

public class IPTest {

	public static void main(String[] args) {
		// 指定純真資料庫的檔案名，所在檔案夾
		IPSeeker ip = new IPSeeker("QQWry.Dat", "c:\\qqwry");
		// 測試IP 58.20.43.13
		System.out.println(ip.getIPLocation("58.20.43.13").getCountry() + ":"
				+ ip.getIPLocation("58.20.43.13").getArea());
	}
}
