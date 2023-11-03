package com.lietu.rtf.model;

import java.util.Date;

import com.lietu.rtf.IRtfDocumentInfo;

	public  class RtfDocumentInfo implements IRtfDocumentInfo
	{

		// ----------------------------------------------------------------------
		public RtfDocumentInfo()
		{
		} // RtfDocumentInfo

		// ----------------------------------------------------------------------
		public int getId()
		{
			 return this.id;
			
		} // Id

		public void setId(int id)
		{
			this.id=id;
			
		}
		// ----------------------------------------------------------------------
		public int getVersion()
		{
			return this.version; 
			
		}
		public void setVersion(int version)
		{
			this.version=version;
		}

		// ----------------------------------------------------------------------
		public int getRevision()
		{
			 return this.revision; 
		} // Revision

		public void setRevision(int revision)
		{
			 this.revision=revision; 
		}
		// ----------------------------------------------------------------------
		public String getTitle()
		{
			 return this.title;
		} // Title

		public void setTitle(String title)
		{
			 this.title=title;
			
		} 
		// ----------------------------------------------------------------------
		public String getSubject()
		{
			 return this.subject; 
			
		} // Subject

		public void setSubject(String subject)
		{
			 this.subject=subject; 
			
		}
		// ----------------------------------------------------------------------
		public String getAuthor()
		{
			return this.author;
		} // Author

		public void setAuthor(String author)
		{
			 this.author=author;
		}
		// ----------------------------------------------------------------------
		public String getManager()
		{
			return this.manager; 
			
		} // Manager

		// ----------------------------------------------------------------------
		public void setManager(String manager)
		{
			this.manager=manager; 
			
		}
		// ----------------------------------------------------------------------
		public String getCompany()
		{
			return this.company; 
		
		} // Company
		public void setCompany(String company)
		{
			 this.company=company; 
			
		} 
		
		// ----------------------------------------------------------------------
		public String getOperator()
		{
			 return this.operatorName;
			
		} // Operator
		public void setOperator(String operatorName)
		{
			 this.operatorName=operatorName;
			
		}
		// ----------------------------------------------------------------------
		public String getCategory()
		{
			return this.category;
			
		} // Category

		public void setCategory(String category)
		{
			this.category=category;
			
		}
		// ----------------------------------------------------------------------
		public String getKeywords()
		{
			 return this.keywords;
			
		} // Keywords
		public void setKeywords(String keywords)
		{
			 this.keywords = keywords; 
		}
		
		
		// ----------------------------------------------------------------------
		public String getComment()
		{
			return this.comment; 
			
		} // Comment

		public void setComment(String comment)
		{
			 this.comment = comment; 
		}
		// ----------------------------------------------------------------------
		public String getDocumentComment()
		{
			return this.documentComment; 
			
		} // DocumentComment

		public void setDocumentComment(String documentComment)
		{
			 this.documentComment=documentComment; 
			
		} 
		// ----------------------------------------------------------------------
		public String getHyperLinkbase()
		{
			return this.hyperLinkbase; 
			
		} // HyperLinkbase
		public void setHyperLinkbase(String hyperLinkbase)
		{
			this.hyperLinkbase=hyperLinkbase; 
			
		} 
		// ----------------------------------------------------------------------
		public Date getCreationTime()
		{
			 return this.creationTime; 
			
		} // CreationTime
		public void setCreationTime(Date creationTime )
		{
			this.creationTime=creationTime;
		}
		// ----------------------------------------------------------------------
		public Date getRevisionTime()
		{
		return this.revisionTime;
			
		} // RevisionTime

		public void setRevisionTime(Date revisionTime)
		{
			this.revisionTime=revisionTime;
		}
		// ----------------------------------------------------------------------
		public Date getPrintTime()
		{
			return this.printTime;
			
		} // PrintTime

		public void setPrintTime(Date printTime)
		{
			this.printTime=printTime;
			
		}
		// ----------------------------------------------------------------------
		public Date getBackupTime()
		{
			return this.backupTime; 
		} // BackupTime

		public void setBackupTime(Date backupTime)
		{
			 this.backupTime=backupTime; 
		}
		// ----------------------------------------------------------------------
		public int getNumberOfPages()
		{
			return this.numberOfPages;
		
		} // NumberOfPages

		public void setNumberOfPages(int numberOfPages)
		{
			 this.numberOfPages=numberOfPages;
		
		}
		// ----------------------------------------------------------------------
		public int getNumberOfWords()
		{
			return this.numberOfWords;
		} // NumberOfWords

		public void setNumberOfWords(int numberOfWords)
		{
			this.numberOfWords=numberOfWords;
		} 
		// ----------------------------------------------------------------------
		public int getNumberOfCharacters()
		{
			 return this.numberOfCharacters;
			
		} // NumberOfCharacters

		public void setNumberOfCharacters(int numberOfCharacters)
		{
			 this.numberOfCharacters=numberOfCharacters;
			
		}
		// ----------------------------------------------------------------------
		public int getEditingTimeInMinutes()
		{
			return this.editingTimeInMinutes;
			
		} // EditingTimeInMinutes

		public void setEditingTimeInMinutes(int editingTimeInMinutes)
		{
			 this.editingTimeInMinutes=editingTimeInMinutes;
			
		}
		// ----------------------------------------------------------------------
		public void Reset()
		{
			this.id = 0;
			this.version = 0;
			this.revision = 0;
			this.title = null;
			this.subject = null;
			this.author = null;
			this.manager = null;
			this.company = null;
			this.operatorName = null;
			this.category = null;
			this.keywords = null;
			this.comment = null;
			this.documentComment = null;
			this.hyperLinkbase = null;
			this.creationTime = null;
			this.revisionTime = null;
			this.printTime = null;
			this.backupTime = null;
			this.numberOfPages = 0;
			this.numberOfWords = 0;
			this.numberOfCharacters = 0;
			this.editingTimeInMinutes = 0;
		} // Reset

		// ----------------------------------------------------------------------
		public String toString()
		{
			return "RTFDocInfo";
		} // ToString

		// ----------------------------------------------------------------------
		// members
		private int id;
		private int version;
		private int revision;
		private String title;
		private String subject;
		private String author;
		private String manager;
		private String company;
		private String operatorName;
		private String category;
		private String keywords;
		private String comment;
		private String documentComment;
		private String hyperLinkbase;
		private Date creationTime;
		private Date revisionTime;
		private Date printTime;
		private Date backupTime;
		private int numberOfPages;
		private int numberOfWords;
		private int numberOfCharacters;
		private int editingTimeInMinutes;
		
		

	} // interface IRtfDocumentInfo
