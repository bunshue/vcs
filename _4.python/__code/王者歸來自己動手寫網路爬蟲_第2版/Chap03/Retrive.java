

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.commons.httpclient.Header;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpException;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.methods.PostMethod;

public class Retrive{
	private static HttpClient httpClient = new HttpClient();
	// 設定代理服務器
	static {
		// 設定代理服務器的IP地址和通訊埠
		//httpClient.getHostConfiguration().setProxy("172.17.18.84", 8080);
	}

	public static boolean downloadPage(String path) throws HttpException,
			IOException {
		InputStream input = null;
		OutputStream output = null;
		// 得到post方法
		PostMethod postMethod = new PostMethod(path);
		// 設定post方法的參數
		/*
		 * NameValuePair[] postData = new NameValuePair[2]; postData[0] = new
		 * NameValuePair("name","lietu"); postData[1] = new
		 * NameValuePair("password","*****");
		 * postMethod.addParameters(postData);
		 */
		// 執行，傳回狀態碼
		int statusCode = httpClient.executeMethod(postMethod);
		// 針對狀態碼進行處理 (簡單起見，只處理傳回值為200的狀態碼)
		if (statusCode == HttpStatus.SC_OK) {
			input = postMethod.getResponseBodyAsStream();
			//得到檔案名
			String filename = path.substring(path.lastIndexOf('/')+1);
			//獲得檔案輸出流
			output = new FileOutputStream(filename);
			//輸出到檔案
			int tempByte = -1;
			while((tempByte=input.read())>0){
				output.write(tempByte);
			}
			//關閉輸入輸出流
			if(input!=null){
				input.close();
			}
			if(output!=null){
				output.close();
			}
			return true;
		}
		//若需要轉向，則進行轉向操作
		if ((statusCode == HttpStatus.SC_MOVED_TEMPORARILY) || (statusCode == HttpStatus.SC_MOVED_PERMANENTLY) || (statusCode == HttpStatus.SC_SEE_OTHER) || (statusCode == HttpStatus.SC_TEMPORARY_REDIRECT)) {
		    //讀取新的URL地址
			Header header = postMethod.getResponseHeader("location");
			if(header!=null){
				String newUrl = header.getValue();
				if(newUrl==null||newUrl.equals("")){
					newUrl="/";
					//使用post轉向
					PostMethod redirect = new PostMethod(newUrl);
					//發送請求，做進一步處理。。。。。
				}
			}
		}
		return false;
	}

	/**
	 * 測試程式碼
	 */
	public static void main(String[] args) {
		// 抓取lietu首頁,輸出
		try {
			Retrive.downloadPage("http://www.lietu.com");
		} catch (HttpException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
