

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
	// �]�w�N�z�A�Ⱦ�
	static {
		// �]�w�N�z�A�Ⱦ���IP�a�}�M�q�T��
		//httpClient.getHostConfiguration().setProxy("172.17.18.84", 8080);
	}

	public static boolean downloadPage(String path) throws HttpException,
			IOException {
		InputStream input = null;
		OutputStream output = null;
		// �o��post��k
		PostMethod postMethod = new PostMethod(path);
		// �]�wpost��k���Ѽ�
		/*
		 * NameValuePair[] postData = new NameValuePair[2]; postData[0] = new
		 * NameValuePair("name","lietu"); postData[1] = new
		 * NameValuePair("password","*****");
		 * postMethod.addParameters(postData);
		 */
		// ����A�Ǧ^���A�X
		int statusCode = httpClient.executeMethod(postMethod);
		// �w�窱�A�X�i��B�z (²��_���A�u�B�z�Ǧ^�Ȭ�200�����A�X)
		if (statusCode == HttpStatus.SC_OK) {
			input = postMethod.getResponseBodyAsStream();
			//�o���ɮצW
			String filename = path.substring(path.lastIndexOf('/')+1);
			//��o�ɮ׿�X�y
			output = new FileOutputStream(filename);
			//��X���ɮ�
			int tempByte = -1;
			while((tempByte=input.read())>0){
				output.write(tempByte);
			}
			//������J��X�y
			if(input!=null){
				input.close();
			}
			if(output!=null){
				output.close();
			}
			return true;
		}
		//�Y�ݭn��V�A�h�i����V�ާ@
		if ((statusCode == HttpStatus.SC_MOVED_TEMPORARILY) || (statusCode == HttpStatus.SC_MOVED_PERMANENTLY) || (statusCode == HttpStatus.SC_SEE_OTHER) || (statusCode == HttpStatus.SC_TEMPORARY_REDIRECT)) {
		    //Ū���s��URL�a�}
			Header header = postMethod.getResponseHeader("location");
			if(header!=null){
				String newUrl = header.getValue();
				if(newUrl==null||newUrl.equals("")){
					newUrl="/";
					//�ϥ�post��V
					PostMethod redirect = new PostMethod(newUrl);
					//�o�e�ШD�A���i�@�B�B�z�C�C�C�C�C
				}
			}
		}
		return false;
	}

	/**
	 * ���յ{���X
	 */
	public static void main(String[] args) {
		// ���lietu����,��X
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
