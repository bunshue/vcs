

import java.io.DataOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

import org.apache.commons.httpclient.DefaultHttpMethodRetryHandler;
import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.HttpException;
import org.apache.commons.httpclient.HttpStatus;
import org.apache.commons.httpclient.methods.GetMethod;
import org.apache.commons.httpclient.params.HttpMethodParams;

public class DownLoadFile {
	/**
	 * 根據 url 和網頁類型產生需要儲存的網頁的檔案名 去除掉 url 中非檔案名字符
	 */
	public  String getFileNameByUrl(String url,String contentType)
	{
		//remove http://
		url=url.substring(7);
		//text/html類型
		if(contentType.indexOf("html")!=-1)
		{
			url= url.replaceAll("[\\?/:*|<>\"]", "_")+".html";
			return url;
		}
		//如application/pdf類型
		else
		{
          return url.replaceAll("[\\?/:*|<>\"]", "_")+"."+
          contentType.substring(contentType.lastIndexOf("/")+1);
		}	
	}

	/**
	 * 儲存網頁字節陣列到本機檔案 filePath 為要儲存的檔案的相對地址
	 */
	private void saveToLocal(byte[] data, String filePath) {
		try {
			DataOutputStream out = new DataOutputStream(new FileOutputStream(
					new File(filePath)));
			for (int i = 0; i < data.length; i++)
				out.write(data[i]);
			out.flush();
			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	/* 下載 url 指向的網頁 */
	public String downloadFile(String url) {
		String filePath = null;
		/* 1.產生 HttpClinet 對象並設定參數 */
		HttpClient httpClient = new HttpClient();
		// 設定 Http 連接逾時 5s
		httpClient.getHttpConnectionManager().getParams().setConnectionTimeout(
				5000);

		/* 2.產生 GetMethod 對象並設定參數 */
		GetMethod getMethod = new GetMethod(url);
		// 設定 get 請求逾時 5s
		getMethod.getParams().setParameter(HttpMethodParams.SO_TIMEOUT, 5000);
		// 設定請求重試處理
		getMethod.getParams().setParameter(HttpMethodParams.RETRY_HANDLER,
				new DefaultHttpMethodRetryHandler());

		/* 3.執行 HTTP GET 請求 */
		try {
			int statusCode = httpClient.executeMethod(getMethod);
			// 判斷存取的狀態碼
			if (statusCode != HttpStatus.SC_OK) {
				System.err.println("Method failed: "
						+ getMethod.getStatusLine());
				filePath = null;
			}

			/* 4.處理 HTTP 響應內容 */
			byte[] responseBody = getMethod.getResponseBody();// 讀取為字節陣列
			// 根據網頁 url 產生儲存時的檔案名
			filePath = "temp\\"
					+ getFileNameByUrl(url, getMethod.getResponseHeader(
							"Content-Type").getValue());
			saveToLocal(responseBody, filePath);
		} catch (HttpException e) {
			// 發生致命的例外，可能是協定不對或者傳回的內容有問題
			System.out.println("Please check your provided http address!");
			e.printStackTrace();
		} catch (IOException e) {
			// 發生網絡例外
			e.printStackTrace();
		} finally {
			// 釋放連接
			getMethod.releaseConnection();
		}
		return filePath;
	}
}
