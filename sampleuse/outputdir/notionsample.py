from notion_client import Client



# 设置Notion API的基本信息

NOTION_API_KEY = "**************************"



# 初始化Notion客户端

notion = Client(auth=NOTION_API_KEY)



# 1. 获取父页面ID

def search_notion_pages(query):

    response = notion.search(query=query)

    return response



search_results = search_notion_pages("notion apitest1")

parent_page_id = search_results['results'][0]['id']



# 2. 准备新页面的内容

new_page_title = "新页面标题"

new_page_content = "这是新页面的内容。"



# 3. 调用API创建新页面

def create_notion_page(parent_page_id, title, content):

    response = notion.pages.create(

        parent={"page_id": parent_page_id},

        properties={'title': [{'text': {'content': '环境变量:^:'}}]},

        children=[{'type': 'code', 'code': {'caption': [], 'rich_text': [{'type': 'text', 'text': {'content': 'powershell 环境变量\n\n\n\n$env:https_proxy="http://127.0.0.1:1080"\n$env:http_proxy="http://127.0.0.1:1080"\n\nset HTTP_PROXY=http://127.0.0.1:1080\nset HTTPS_PROXY=%HTTP_PROXY%\n\n\nwsl --export Ubuntu-22.04 D:\\wsldir\\wsl-u-22.tar\n\n\n\nhttps://blog.csdn.net/CSDN_Huang1/article/details/124092336'}}], 'language': 'plain text'}}]

    )

    return response



create_page_response = create_notion_page(parent_page_id, new_page_title, new_page_content)



if 'id' in create_page_response:

    print('新页面创建成功，链接为:', f"https://www.notion.so/{create_page_response['id'].replace('-', '')}")

else:

    print('新页面创建失败:', create_page_response)


