package test.com.lietu.filter;

import java.io.InputStream;
import java.util.Properties;

public class Test {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
	 	Properties p = new Properties();
    	InputStream is=p.getClass().getResourceAsStream("/spider.properties");
    	p.load(is);
		is.close();
		String solr = p.getProperty("solr");
		System.out.println(solr);
	}

}
