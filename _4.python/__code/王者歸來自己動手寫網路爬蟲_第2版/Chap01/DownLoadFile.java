

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
	 * �ھ� url �M�����������ͻݭn�x�s���������ɮצW �h���� url ���D�ɮצW�r��
	 */
	public  String getFileNameByUrl(String url,String contentType)
	{
		//remove http://
		url=url.substring(7);
		//text/html����
		if(contentType.indexOf("html")!=-1)
		{
			url= url.replaceAll("[\\?/:*|<>\"]", "_")+".html";
			return url;
		}
		//�papplication/pdf����
		else
		{
          return url.replaceAll("[\\?/:*|<>\"]", "_")+"."+
          contentType.substring(contentType.lastIndexOf("/")+1);
		}	
	}

	/**
	 * �x�s�����r�`�}�C�쥻���ɮ� filePath ���n�x�s���ɮת��۹�a�}
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

	/* �U�� url ���V������ */
	public String downloadFile(String url) {
		String filePath = null;
		/* 1.���� HttpClinet ��H�ó]�w�Ѽ� */
		HttpClient httpClient = new HttpClient();
		// �]�w Http �s���O�� 5s
		httpClient.getHttpConnectionManager().getParams().setConnectionTimeout(
				5000);

		/* 2.���� GetMethod ��H�ó]�w�Ѽ� */
		GetMethod getMethod = new GetMethod(url);
		// �]�w get �ШD�O�� 5s
		getMethod.getParams().setParameter(HttpMethodParams.SO_TIMEOUT, 5000);
		// �]�w�ШD���ճB�z
		getMethod.getParams().setParameter(HttpMethodParams.RETRY_HANDLER,
				new DefaultHttpMethodRetryHandler());

		/* 3.���� HTTP GET �ШD */
		try {
			int statusCode = httpClient.executeMethod(getMethod);
			// �P�_�s�������A�X
			if (statusCode != HttpStatus.SC_OK) {
				System.err.println("Method failed: "
						+ getMethod.getStatusLine());
				filePath = null;
			}

			/* 4.�B�z HTTP �T�����e */
			byte[] responseBody = getMethod.getResponseBody();// Ū�����r�`�}�C
			// �ھں��� url �����x�s�ɪ��ɮצW
			filePath = "temp\\"
					+ getFileNameByUrl(url, getMethod.getResponseHeader(
							"Content-Type").getValue());
			saveToLocal(responseBody, filePath);
		} catch (HttpException e) {
			// �o�ͭP�R���ҥ~�A�i��O��w����Ϊ̶Ǧ^�����e�����D
			System.out.println("Please check your provided http address!");
			e.printStackTrace();
		} catch (IOException e) {
			// �o�ͺ����ҥ~
			e.printStackTrace();
		} finally {
			// ����s��
			getMethod.releaseConnection();
		}
		return filePath;
	}
}
