from typer import Typer

app = Typer()
import os

class metadata:
    start_line  = "## CODEMERGER START ##"
    file_path_line = "## FILE: {file} ##\n"
    end_line = "## CODEMERGER END ##\n\n"

    def dumps(self, file_path, content):
        out = "\n".join([self.start_line, self.file_path_line.format(file=file_path), content,self.end_line])
        return out



def merge_files_with_metadata(directory, inputfile_related_path_list,output_file):
    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:

                # from IPython import embed; embed()
                if file in inputfile_related_path_list:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as infile:
                        lines = infile.readlines()
                        out = metadata().dumps(file,"\n".join(lines))
                        outfile.write(out)
                        # outfile.write(f"## CODEMERGER START ##""## CODEMERGER START ##")
                        # outfile.write(f"## FILE: {file} ##\n")
                        # outfile.writelines(lines)
                        # outfile.write(f"## CODEMERGER END ##")
                        # outfile.write("\n\n")

# if __name__ == "__main__":
#     source_directory = "path/to/source_directory"
#     output_file = "combined_file.txt"
#     merge_files_with_metadata(source_directory, output_file)
#     print(f"Files from {source_directory} have been merged into {output_file}.")


def load_from_config_file(configfile:str):
    with open(configfile,"r") as f:
        content = f.read()
        paths = content.split("\n")
        result = []
        for p in paths:
            if p !="":
                result.append(p)
        return result

from typing import List

def process_paths(inputfile_list: List[str]) -> str:
    # 如果输入列表为空，返回空字符串
    if not inputfile_list:
        return ""

    # 分割第一个路径为片段
    common_path_parts = os.path.split(inputfile_list[0])

    # 遍历所有路径
    for path in inputfile_list[1:]:
        path_parts = os.path.split(path)
        # 保留公共的片段
        common_path_parts = [part for part in common_path_parts if part in path_parts]

    # 返回公共路径
    ccc = os.path.join(*common_path_parts)
    # 返回公共路径
    # ccc = '/'.join(common_path_parts)
    print(ccc)
    # from IPython import embed; embed()
    out_list = []

    for item in inputfile_list:
        r = item.split(ccc)[1]
        if r.startswith("\\"):
            r = r[1:]
        out_list.append(r)


    return ccc, out_list

@app.command()
def merge(configfile:str, outputfile_path:str):
    '''
    python ./codemerger.py merge inputfiles outputfile_path

    python ./codemerger.py merge inputfiles ./outfile.txt

    '''
    inputfile_list = load_from_config_file(configfile)
    greatest_common_root, inputfile_related_path_list = process_paths(inputfile_list)
    merge_files_with_metadata(greatest_common_root, inputfile_related_path_list, outputfile_path)

    

    pass

from pathlib import Path

import shutil
import os
from pydantic import BaseModel
class fileobj(BaseModel):
    file_path:str
    content:str

@app.command()
def split(file_to_split:Path, output_directory:Path):
    '''
    python ./codemerger.py split ./outfile.txt outputdir

    python ./codemerger.py split file_to_split output_directory
    '''
    with open(file_to_split, "r") as f:
        content = f.read()
    
    
    contentlist = content.split(metadata().start_line+"\n")
    fos = []
    for content_with_meta in contentlist:
        if content_with_meta == "":
            continue
        # print(content_with_meta)
        # input()
        assert content_with_meta.startswith("## FILE: ")
        lines = content_with_meta.split("\n")
        fileline = lines[0]
        ttt = fileline.split("##")[1]
        ttt = ttt.strip()
        assert ttt.startswith("FILE: ")
        filepath = ttt.split("FILE: ")[1]
        filepath = filepath.strip()
        print(filepath)

        assert lines[-3].startswith(metadata().end_line[:-2])
        content = "\n".join(lines[2:-3])
        fo = fileobj(content=content, file_path=filepath)
        fos.append(fo)
        

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for fo in fos:
        absfilepath = os.path.join(output_directory,fo.file_path)
        with open(absfilepath,"w") as f:
            f.write(fo.content)



    pass


if __name__ == "__main__":
    app()