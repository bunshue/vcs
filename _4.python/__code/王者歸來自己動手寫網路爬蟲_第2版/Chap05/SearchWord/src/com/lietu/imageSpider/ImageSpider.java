package com.lietu.imageSpider;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

import org.htmlparser.Node;
import org.htmlparser.lexer.Lexer;
import org.htmlparser.lexer.Page;
import org.htmlparser.util.ParserException;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.IndexReader;
import org.apache.solr.client.solrj.SolrServer;
import org.apache.solr.client.solrj.impl.CommonsHttpSolrServer;
import org.apache.solr.client.solrj.response.UpdateResponse;
import org.apache.solr.client.solrj.util.ClientUtils;

public class ImageSpider {

	//http://58.68.128.229/
	public static int validBBS() throws Exception{
	    SolrServer server;
	    String solrUrl = "http://localhost:8080/indexbbs/";
	    server = new CommonsHttpSolrServer( solrUrl );
	    
		String dir = "D:/search/resin-3.0.25/solrbbs/data/index";
		IndexReader ir = IndexReader.open(dir);
		int maxDoc = ir.maxDoc();
		int count=0;
		for(int iNum = maxDoc -1; iNum>=0 && count<10 ;iNum--)
		{
	      if (!ir.isDeleted(iNum)) {
	    	  Document doc = ir.document(iNum);
	    	  String url = doc.getField("url").stringValue();
	          
	    	  //if(!isValid(url))
	    	  {
	    		  System.out.println(url);
	    		  String q = "url:"+ClientUtils.escapeQueryChars(url);
	    		  UpdateResponse res = server.deleteByQuery( q );// delete everything!
	    		  
	    		  System.out.println(res.getStatus());
	    		  ++count;
	    	  }
	      }
		}
		server.commit( true, true );
		return count;
	}
}
