package test.com.lietu.filter;

import java.io.IOException;
import java.io.InputStream;
//import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class TestgetXml {

	/**
	 * ÀC¤ç«þÀC¤ç«þÀC¤ç«þÀC¤ç«þÀC?ÀC¤ç«þspider.xmlÀC¤ç«þÀC¤ç«þÀC¤ç«þÂàÀCªã¨ìÀC¤ç«þÛpÀC¤ç«þÀC?
	 * @param args
	 */
	private Connection con = null;
	public TestgetXml(){
		try{
			Properties properties = new Properties();
			InputStream is = this.getClass().getResourceAsStream("/mysqldb.properties");
			properties.load(is);
			is.close();
			String driver = properties.getProperty("driver");
			System.out.println(driver);
			String dburl = properties.getProperty("dburl");
			System.out.println(dburl);
			String user = properties.getProperty("user");
			System.out.println(user);
			String password = properties.getProperty("password");
			System.out.println(password);
			Driver drv = (Driver)Class.forName(driver).newInstance();
			DriverManager.registerDriver(drv);
			con = DriverManager.getConnection(dburl,user,password);			
		}catch(Exception err){err.printStackTrace();}
	}
	public void getXml(String configFile)
	{
//    	ArrayList  al = new ArrayList();
		SAXBuilder builder = new SAXBuilder();
		try{
			InputStream is = getClass().getResourceAsStream("/"+configFile);
			Document doc = builder.build(is);
			Element eleroot = doc.getRootElement();
			List  list = eleroot.getChildren("website");
			
			for(int i=0;i<list.size();i++)
			{
				Element item = (Element) list.get(i);
				
				Element urls = item.getChild("url");
				String url = urls.getText();
				System.out.println("url:"+url);
				Element types = item.getChild("type");
				String type = types.getText();
				System.out.println("type:"+type);
				Element classes = item.getChild("class");
				String classs = classes.getText();
				System.out.println("class:"+classs);
				Element ranks = item.getChild("rank");
				int rank = Integer.parseInt(ranks.getText());				
				System.out.println("rank:"+rank);
				
				String sql = "insert into spider(url,type,class,rank) values (?,?,?,?)";
				PreparedStatement pstmt = con.prepareStatement(sql);								
				pstmt.setString(1, url);
				pstmt.setString(2, type);
				pstmt.setString(3, classs);
				pstmt.setInt(4, rank);	
				pstmt.executeUpdate();
				pstmt.close();
				Thread.sleep(100);
			}
			if (con != null) {
				con.close();
				System.out.println("Close Success!");
				}						
			
		}catch(Exception e)
		{
			e.printStackTrace();
			
		}/*catch(JDOMException e)
		{
			e.printStackTrace();
			
		}	*/			
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new TestgetXml().getXml("config/spider.xml");
	}

}
