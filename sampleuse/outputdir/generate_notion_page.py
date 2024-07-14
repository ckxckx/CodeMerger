from masscode_db import DB, Snippet



import json

from notion_code_languages import mapping_masscode_to_notion





from notion_pages import *



from typing import Optional, Callable





import pickle

from typer import Typer

    

app = Typer()













def iterate_process(db: DB, func: Callable):

    for snippet in db.snippets:

        func(snippet)



def dosth1(snippet: Snippet):

    print(snippet.updatedAt)



    print(snippet.name)

    for c in snippet.content:

        print(c.label)

        # print(c.value)

    # psnippet.content)



@app.command()

def get_page_id(keyword:str):

    '''

    python ./generate_notion_page.py  get-page-id "masscode-ckxprivate-windows-20240713"

    '''

    search_results = search_notion_pages(keyword)

    assert len(search_results["results"]) >=1

    # from IPython import embed; embed()

    page_id = search_results['results'][0]['id']

    print(f"page_id: {page_id}")

    return page_id

    

@app.command()

def filter_company_masscode_db(parent_page_key_word: str, select_notes_after_timestamp:int):

    '''

    python ./generate_notion_page.py filter-company-masscode-db "masscode-ckxcompany-windows-20240209-20240713" 1707440400000

    '''





    with open(r"D:\codebase\masscodetonotion\dbcompany.json", "r") as f:

        db_dict = json.load(f)



    db = DB.model_validate(db_dict)



    npmc_list: List[NotionPageForMasscode] = []



    for snippet in db.snippets:

        if snippet.createdAt < select_notes_after_timestamp:

            continue

        

        note_name = snippet.name

        if note_name == None:

            note_name = "code snippet 未命名"

        

        is_snippet_content_unique = False

        if len(snippet.content) ==1:

            is_snippet_content_unique = True



        for c in snippet.content:



            if is_snippet_content_unique:

                note_label = ""

            else:

                note_label = c.label

            note_language = mapping_masscode_to_notion[c.language.value]

            npmc = NotionPageForMasscode(

                note_name=note_name,

                note_label = note_label,

                note_content = c.value,

                note_language = note_language,

            )

            npmc_list.append(npmc)



    print(len(npmc_list))



    parent_page_id = get_page_id(parent_page_key_word)

    

    suc_count = 0



    fail_count = 0



    

    with open("session3.pkl", "wb") as f:

        pickle.dump(npmc_list, f)

    for npmc in npmc_list:

        npmc.isdone = False

        try:

            npmc.create_notion_page_at(parent_page_id)

            npmc.isdone = True

            suc_count+=1

            print(f"# of suc: {suc_count}")

        except:

            npmc.isdone = False

            fail_count+=1

            print(f"# of fail: {fail_count}")



    

    print(f"遍历完成\n# of suc: {suc_count}\n # of fail: {fail_count}")

    npmc_fail_list = []

    for npmc in npmc_list:

        if npmc.isdone == False:

            npmc_fail_list.append(npmc)



    with open("session4.pkl", "wb") as f:

        pickle.dump(npmc_fail_list, f)





@app.command()

def sync_masscode_to_notion(parent_page_key_word: str, select_notes_after_timestamp:int):

    '''

    python ./generate_notion_page.py sync-masscode-to-notion "masscode-ckxprivate-windows-20240713" 0

    '''



    with open("db.json", "r") as f:

        db_dict = json.load(f)



    db = DB.model_validate(db_dict)



    npmc_list: List[NotionPageForMasscode] = []



    for snippet in db.snippets:

        if snippet.createdAt < select_notes_after_timestamp:

            continue

        

        note_name = snippet.name

        if note_name == None:

            note_name = "code snippet 未命名"

        

        is_snippet_content_unique = False

        if len(snippet.content) ==1:

            is_snippet_content_unique = True



        for c in snippet.content:



            if is_snippet_content_unique:

                note_label = ""

            else:

                note_label = c.label

            note_language = mapping_masscode_to_notion[c.language.value]

            npmc = NotionPageForMasscode(

                note_name=note_name,

                note_label = note_label,

                note_content = c.value,

                note_language = note_language,

            )

            npmc_list.append(npmc)





    parent_page_id = get_page_id(parent_page_key_word)



    kk = npmc_list[:10]



    



    # import pickle



    # pickle.dumps(kk)



    # from IPython import embed; embed()



    suc_count = 0



    fail_count = 0



    

    with open("session1.pkl", "wb") as f:

        pickle.dump(npmc_list, f)

    for npmc in npmc_list:

        npmc.isdone = False

        try:

            npmc.create_notion_page_at(parent_page_id)

            npmc.isdone = True

            suc_count+=1

            print(f"# of suc: {suc_count}")

        except:

            npmc.isdone = False

            fail_count+=1

            print(f"# of fail: {fail_count}")



    

    print(f"遍历完成\n# of suc: {suc_count}\n # of fail: {fail_count}")

    npmc_fail_list = []

    for npmc in npmc_list:

        if npmc.isdone == False:

            npmc_fail_list.append(npmc)



    with open("session2.pkl", "wb") as f:

        pickle.dump(npmc_fail_list, f)









from typing import cast

@app.command()

def test_fail():

    '''

    test:

86720592-f3d4-4ea5-96dd-ee96e0d4fd02



    formal:

a831f412-9b4e-4611-9c26-87baadb959f1

    '''

    with open("session4.pkl", "rb") as f:

        npmc_fail_list = pickle.load(f)

        nfl = cast(List[NotionPageForMasscode], npmc_fail_list)

        elist = []

        for item in nfl:

            print(item.note_name)

            print(f"字数：{len(item.note_content)}")

            print("*"*99+"\n"+"*"*99)

            print(item.note_content)



            input()

            # try:

            #     item.create_notion_page_at("86720592-f3d4-4ea5-96dd-ee96e0d4fd02")

            # except Exception as e:

            #     print("sth wrong:")

            #     elist.append(e)

            #     print(e)

            # pass

    from IPython import embed; embed()

    

# try:

#     nfl[0].create_notion_page_at("86720592-f3d4-4ea5-96dd-ee96e0d4fd02")

# except Exception as e:

#     print(e)



@app.command()

def liststh():

    print("list sth")



if __name__ == "__main__":

    

    app()