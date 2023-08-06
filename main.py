from fastapi import FastAPI
from datetime import datetime
from typing import List
import requests


class Handler:
    HOST = '0.0.0.0:5000'
    MODELS = ['llama-2-7b-chat', 'Llama2-Chinese-7b-Chat']
    DEFAULT_MODEL = 'Llama2-Chinese-7b-Chat'

    def __init__(self):
        self.start_time = datetime.now()
        self.current_model = self.DEFAULT_MODEL
    
    def _model_api(self, request):
        response = requests.post(f'http://{self.HOST}/api/v1/model', json=request)
        return response.json()

    def _model_load(self, model_id):
        return self._model_api({'action': 'load', 'model_name': model_id, 'loader': 'Transformers'})
    
    def start_llm(self, model_id: str, bit_8: bool = False):
        return self.shift_llm(model_id)

    def stop_llm(self, model_id: str):
        if model_id not in self.MODELS:
            return f'Error: There is no model: {model_id}'

    def shift_llm(self, model_id: str):
        if model_id not in self.MODELS:
            return f'Error: There is no model: {model_id}'
        response = self._model_load(model_id)
        if 'error' in response:
            return 'Error'
        else:
            self.start_time = datetime.now()
            self.current_model = model_id
            return 'Success'
        
    def get_llm_state(self, model_id: str):
        if model_id not in self.MODELS:
            return f'Error: There is no model: {model_id}'
        deploy_state = (model_id == self.current_model)
        return {
            'type': model_id,
            'deploy_state': deploy_state,
            'start_time': str(self.start_time) if deploy_state else '',
            'deploy_time': str(datetime.now() - self.start_time) if deploy_state else '',
        }
    
    def infer(self, messages: List[dict]):
        import openai
        openai.api_key="sk-111111111111111111111111111111111111111111111111"
        openai.api_base="http://0.0.0.0:5001/v1"

        response = openai.ChatCompletion.create(
            model=self.current_model,
            messages=messages,
            stream=True,
            temparature=0
        )
        return response


app = FastAPI()
handler = Handler()

    
@app.post("/start_llm/")
def start_llm(model_id: str, bit_8: bool = False):
    return {'code': handler.start_llm(model_id, bit_8)}


@app.post("/stop_llm/")
def stop_llm(model_id: str):
    return {'code': handler.stop_llm(model_id)}


@app.post("/shift_llm/")
def shift_llm(model_id: str):
    return {'code': handler.shift_llm(model_id)}


@app.get("/llm_state/")
def get_llm_state(model_id: str):
    return handler.get_llm_state(model_id)


@app.post("/inference/")
def infer(messages: List[dict]):
    return handler.infer(messages)