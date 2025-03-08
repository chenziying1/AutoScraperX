from setuptools import setup, find_packages

setup(
    name="common_spider_tool",  # 你的库名称
    version="0.1.0",  # 版本号
    author="czy",
    author_email="1060324818@qq.com",
    description="A common spider tool based on Selenium",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/common_spider_tool",  # 你的 GitHub 地址（需替换）
    packages=find_packages(),
    install_requires=[
        "selenium",
        "beautifulsoup4",
        "undetected-chromedriver",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
