package test.com.lietu.filter;

import java.io.InputStream;
import java.sql.Connection;
import java.sql.Driver;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import org.jdom.Document;
import org.jdom.Element;
import org.jdom.input.SAXBuilder;

import com.bitmechanic.spindle.XmlElement;

public class getSpiderData {

	/**
	 * ÀC¤ç«þÀCÁB¸Ò«þÀC¤ç«þÀC¼ä¡AÀC¤ç«þÀC¤ç«þÀC¤ç«þÀCÁB¥ë«þÀC¤ç«þÀC¤ç«þÀC¹®¹F«þÀC¤ç«þ
	 * @param args
	 */
	private Connection con = null;
	public getSpiderData(){
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
	
	public XmlElement[] getXml(String configFile)
	{			
		ArrayList  al = new ArrayList();
		SAXBuilder builder = new SAXBuilder();
		try{
			String sql = "select url,type,class,rank from spider";
			PreparedStatement pstmt = con.prepareStatement(sql);
					
			ResultSet result = pstmt.executeQuery();			
			while (result.next()) {
				
					String url = result.getString(1);
					String type = result.getString(2);			
					String classs = result.getString(3);
					String rank = result.getString(4);
					System.out.println("\nurl:"+url+"\ntype:"+type+"\nrank:"+rank);	
//					XmlElement xel = new XmlElement(url,type,classs,rank);					
//					al.add(xel);	
			}
			result.close();
			pstmt.close();
			if (con != null) {
				con.close();
				System.out.println("Close Success!");
			}	
		}catch(Exception e)
		{
			e.printStackTrace();			
		}	
		return  (XmlElement[]) al.toArray(new XmlElement[al.size()]);	
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
