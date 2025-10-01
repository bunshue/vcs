import pygame


# 自定义按钮
class Button:
    # msg为要在按钮中显示的文本
    def __init__(
        self, screen, centerxy, width, height, button_color, text_color, msg, size
    ):
        """初始化按钮的属性"""
        self.screen = screensize
        # 设置按钮的宽和高
        self.width, self.height = width, height
        # 设置按钮的rect对象颜色为深蓝
        self.button_color = button_color
        # 设置文本的颜色为白色
        self.text_color = text_color
        # 设置文本为默认字体，字号为20
        self.font = pygame.font.SysFont("Microsoft JhengHei", size)
        # 设置按钮大小
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # 创建按钮的rect对象，并设置按钮的中心位置
        self.rect.centerx = centerxy[0] - self.width / 2 + 2
        self.rect.centery = centerxy[1] - self.height / 2 + 2
        # 渲染图像
        self.deal_msg(msg)

    def deal_msg(self, msg):
        """将msg渲染为图像，并将其在按钮上居中"""
        # 应用render()方法将存储在msg的文本转换为图像
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # 根据文本图像创建一个rect
        self.msg_img_rect = self.msg_img.get_rect()
        # 将该rect的center属性设置为按钮的center属性
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        # 填充颜色
        self.screen.fill(elf.button_color, self.rect)
        # 将该图像绘制到屏幕
        self.screen.blit(self.msg_img, self.msg_img_rect)


# 收入统计
def text5(screen):
    # 计算price列的和
    sum_price = pi_info_tabel["price"].sum()
    # 使用系统字体
    xtfont = pygame.font.SysFont("Microsoft JhengHei", 20)
    # 重新开始按钮
    textstart = xtfont.render("共计收入：" + str(int(sum_price)) + "元", True, WHITE)
    # 获取文字图像位置
    text_rect = textstart.get_rect()
    # 设置文字图像中心点
    text_rect.centerx = 1200
    text_rect.centery = 30
    # 绘制内容
    screen.blit(textstart, text_rect)
    # 加载图像
    image = pygame.image.load("file/income.png")
    # 设置图片大小
    image = pygame.transform.scale(image, (390, 430))
    # 绘制月收入图表
    screen.blit(image, (1000, 50))
