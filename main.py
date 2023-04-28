import ddddocr
import os

ocr = ddddocr.DdddOcr()

# 获取脚本文件所在目录
dir_path = 'D:/OcrRequest/'

with open(os.path.join(dir_path, 'code.jpg',), 'rb') as f:
    img_bytes = f.read()

res = ocr.classification(img_bytes)

print("res", res)

# 将响应结果保存到文件
with open(os.path.join(dir_path, "ocr_response.json"), "w", encoding="utf-8") as f:
    f.write(res)

print('create ocr_response.json')

# import requests
# import json

# # 设置请求参数
# url = 'https://api.ocr.space/parse/image'
# headers = {'apikey': 'K89882185488957'}
# payload = {
#     'language': 'eng',
#     'OCREngine': 2,
# }
# files = {'image': ('code.jpg', open('./code.jpg', 'rb'))}

# # 发送请求
# response = requests.post(url, headers=headers, data=payload, files=files)

# # 输出响应结果
# print(response.text)

# # 解析响应结果并格式化为 JSON 字符串
# response_json = json.loads(response.text)
# parsed_text = response_json['ParsedResults'][0]['ParsedText']
# # response_str = json.dumps(response_json, indent=4, ensure_ascii=False)

# # 将响应结果保存到文件
# with open("ocr_response.json", "w", encoding="utf-8") as f:
#     f.write(parsed_text)

# print(parsed_text)
