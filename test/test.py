# -*- encoding: utf-8 -*-
'''
file       :test.py
Description:
Date       :2025/03/08 10:45:10
Author     :czy
version    :v0.01
email      :1060324818@qq.com
'''

from AutoScraperX import Spider  # 确保 Spider 类已正确导入

def main():
    # 创建 Spider 实例
    spider = Spider(
        headless=True,  # 是否无头模式运行
        proxy=None,  # 可选代理设置
        timeout=10,  # 超时时间（秒）
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        wait_time=5  # 页面加载后等待时间
    )
    
    try:
        # 打开网页
        url = "https://example.com"
        spider.open_page(url)
        print(f"成功打开 {url}")
        
        # 获取网页标题
        title = spider.get_title()
        print(f"页面标题: {title}")
        
        # 等待某个元素出现（假设有 id 为 'content' 的元素）
        spider.wait_for_element("id", "content", timeout=10)
        print("元素 'content' 已出现")
        
        # 截图并保存
        spider.save_screenshot("screenshot.png")
        print("截图已保存")
        
        # 获取 cookies
        cookies = spider.get_cookies()
        print("获取的 Cookies:", cookies)
        
        # 关闭浏览器
        spider.quit()
        print("爬虫已关闭")
    
    except Exception as e:
        print(f"发生错误: {e}")
        spider.quit()

if __name__ == "__main__":
    main()