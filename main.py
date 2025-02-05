import os
from tqdm import tqdm
from volcenginesdkarkruntime import Ark

# 设置 API Key 环境变量
os.environ["ARK_API_KEY"] = "你的api key"

# 初始化 Ark 客户端
client = Ark(base_url="https://ark.cn-beijing.volces.com/api/v3")

# 非流式请求
def non_stream_request(word, save_filename):
    try:
        completion = client.chat.completions.create(
            model="你的model id",
            messages=[
                {"role": "system", "content": "你是豆包，是由字节跳动开发的AI人工智能助手"},
                {"role": "user", "content": f"请采用词源联想、词根词缀联想、词形联想、发音联想、场景联想、相关词汇联想、短语联想等方式，给出记忆英文单词{word}的方法。"}
            ]
        )
        response_content = completion.choices[0].message.content
        with open(save_filename, 'w', encoding='utf-8') as file:
            file.write(response_content)
    except Exception as e:
        print(f"非流式请求出错: {e}")

def read_and_process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in tqdm(lines, desc="处理单词进度", unit="个"):
        word = line.strip()
        save_filename = f"./words/{word}.md"
        if not os.path.exists(save_filename):
            non_stream_request(word, save_filename)


if __name__ == "__main__":
    file_path = 'words.txt'
    read_and_process_file(file_path)