using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace FoodWebAp
{
    public partial class Default1 : System.Web.UI.Page
    {
        protected void DetailsView1_ItemInserting
    (object sender, DetailsViewInsertEventArgs e)
        {
            FileUpload fileUpload1 =
             (FileUpload)DetailsView1.FindControl("FileUpload1");
            SqlDataSource1.InsertParameters["圖示"].DefaultValue =
             fileUpload1.FileName;
            if (fileUpload1.HasFile)
            {
                fileUpload1.SaveAs(Server.MapPath("images") + "\\" +
                 fileUpload1.FileName);
            }
        }

        protected void GridView1_RowUpdating
         (object sender, GridViewUpdateEventArgs e)
        {
            FileUpload fileUpload2 = (FileUpload)GridView1.Rows[e.RowIndex].
             Cells[4].FindControl("FileUpload2");
            TextBox txtImg = (TextBox)GridView1.Rows[e.RowIndex].Cells[4].
             FindControl("txtImg");
            if (fileUpload2.HasFile)
            {
                SqlDataSource1.UpdateParameters["圖示"].DefaultValue =
                 fileUpload2.FileName;
                fileUpload2.SaveAs(Server.MapPath("images") + "\\" +
                 fileUpload2.FileName);
            }
            else
            {
                SqlDataSource1.UpdateParameters["圖示"].DefaultValue =
                 txtImg.Text;
            }
        }
        protected void GridView1_RowDeleting(object sender,
         GridViewDeleteEventArgs e)
        {
            Image image1 = (Image)GridView1.Rows[e.RowIndex].Cells[4].
             FindControl("Image1");
            try
            {
                System.IO.File.Delete(Server.MapPath(image1.ImageUrl));
            }
            catch (Exception ex)
            {

            }
        }

    }
}