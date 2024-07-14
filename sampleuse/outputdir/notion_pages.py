from pydantic import BaseModel

from typing import Optional,List

from notion_client import Client

from abc import abstractmethod



# 设置Notion API的基本信息

NOTION_API_KEY = "**************************"



# 初始化Notion客户端

notion = Client(auth=NOTION_API_KEY)





def search_notion_pages(query):

    response = notion.search(query=query)

    return response



class NotionClientTool:

    @abstractmethod

    def gen_properties(self):

        pass



    @abstractmethod

    def gen_children(self):

        pass



    def create_notion_page_at(self, parent_page_id):





        properties = self.gen_properties()

        children = self.gen_children()





        # print(properties)

        # print(children)

        

        response = notion.pages.create(

            parent = {

                "page_id": parent_page_id

            },

            properties = properties,

            children = children

        )



        if 'id' in response:

            print('新页面创建成功，链接为:', f"https://www.notion.so/{response['id'].replace('-', '')}")

        else:

            print('新页面创建失败:', response)







class NotionPageForMasscode(BaseModel, NotionClientTool):

    note_name :str

    note_label: Optional[str] =None

    note_content: str

    note_language: str

    isdone: bool = False

    def gen_properties(self)->dict:

        adict = {

            "title": [

                {

                    "text": {

                        "content": "From [masscode]: " + self.note_name+" |:^:| " + self.note_label

                    }

                }

            ]

        }

        return adict

        pass

    def gen_children(self)->List[dict]:



        alist = []



        codeblock = {

            "type": "code",

            "code": {

                "caption": [],

                    "rich_text": [{

                "type": "text",

                "text": {

                    "content": self.note_content

                }

                }],

                "language": self.note_language

            }

        }

        alist.append(codeblock)

        return alist

        pass


