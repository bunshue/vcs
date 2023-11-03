

import java.util.Set;

public class MyCrawler {
	/**
	 * 使用種子初始化 URL 隊列
	 * @return
	 * @param seeds 種子URL
	 */ 
	private void initCrawlerWithSeeds(String[] seeds)
	{
		for(int i=0;i<seeds.length;i++)
			LinkQueue.addUnvisitedUrl(seeds[i]);
	}	
	/**
	 * 抓取過程
	 * @return
	 * @param seeds
	 */
	public void crawling(String[] seeds)
	{   //定義過濾器，分析以http://www.lietu.com開頭的鏈接
		LinkFilter filter = new LinkFilter(){
			public boolean accept(String url) {
				if(url.startsWith("http://www.lietu.com"))
					return true;
				else
					return false;
			}
		};
		//初始化 URL 隊列
		initCrawlerWithSeeds(seeds);
		//循環條件：待抓取的鏈接不空且抓取的網頁不多於1000
		while(!LinkQueue.unVisitedUrlsEmpty()&&LinkQueue.getVisitedUrlNum()<=1000)
		{
			//隊頭URL出隊列
			String visitUrl=(String)LinkQueue.unVisitedUrlDeQueue();
			if(visitUrl==null)
				continue;
			DownLoadFile downLoader=new DownLoadFile();
			//下載網頁
			downLoader.downloadFile(visitUrl);
			//該 url 放入到已存取的 URL 中
			LinkQueue.addVisitedUrl(visitUrl);
			//分析出下載網頁中的 URL
			
			Set<String> links=HtmlParserTool.extracLinks(visitUrl,filter);
			//新的未存取的 URL 入隊
			for(String link:links)
			{
					LinkQueue.addUnvisitedUrl(link);
			}
		}
	}
	//main 方法入口
	public static void main(String[]args)
	{
		MyCrawler crawler = new MyCrawler();
		crawler.crawling(new String[]{"http://www.twt.edu.cn"});
	}

}
