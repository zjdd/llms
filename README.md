# LLM 模块

## Install

### 下载 Text generation web UI
1. clone 项目
```
git clone https://github.com/oobabooga/text-generation-webui
```

2. install conda
```
curl -sL "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > "Miniconda3.sh"
bash Miniconda3.sh
```

3. 环境准备
```
conda create -n textgen python=3.10.9
conda activate textgen
```

4. 安装环境
```
pip install torch torchvision torchaudio
pip install -r requirements.txt
```

### 下载模型参数
放在 text-generation-webui/models/ 目录下

#### llama-2-7b-chat
链接: https://pan.baidu.com/s/1XGovdZ7OFZdFwfWoKW85ww 提取码: tf1j 

### Chinese-Llama-7b


## Start

```bash
cd text-generation-webui
python server.py --model Llama2-Chinese-7b-Chat --api --extensions openai --listen

cd ..
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

## api docs
http://{server ip}:8001/docs