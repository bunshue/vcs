# ch17_30.py
from PIL import Image, ImageDraw, ImageFont

def generate_product_image(product_img_path, background_img_path, promo_text):
    # 加載產品和背景影像
    product_img = Image.open(product_img_path).resize((200, 200))
    background_img = Image.open(background_img_path)
    # 在背景影像上放置產品影像
    background_img.paste(product_img, (50, 50), product_img)
    # 在影像上添加促銷文字
    draw = ImageDraw.Draw(background_img)
    font = ImageFont.truetype("arial.ttf", size=45)
    draw.text((50, 260), promo_text, font=font, fill="white")
    # 保存或返回影像
    background_img.save('output_promo_image.jpg')

generate_product_image('product.png', 'background.jpg', '特價促銷!')


