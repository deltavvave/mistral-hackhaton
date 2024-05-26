# from langchain import HuggingFaceHub
# import os
# os.environ['OPENAI_API_KEY']= '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'
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


# llm_mist = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.3", model_kwargs={"temperature":0.1, "max_length":224})

from huggingface_hub import snapshot_download
from pathlib import Path
from mistral_inference.model import Transformer
from mistral_inference.generate import generate

from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from mistral_common.protocol.instruct.messages import UserMessage
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Optional, List, Mapping, Any

mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
mistral_models_path.mkdir(parents=True, exist_ok=True)

snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)

model = Transformer.from_folder(mistral_models_path)
tokenizer = MistralTokenizer.from_file(f"{mistral_models_path}/tokenizer.model.v3")
from langchain import ConversationChain



class CustomLLMMistral(LLM):
    model: Transformer
    tokenizer: MistralTokenizer

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self, prompt: str, stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None) -> str:

        completion_request = ChatCompletionRequest(messages=[UserMessage(content=prompt)])

        tokens = self.tokenizer.encode_chat_completion(completion_request).tokens

        out_tokens, _ = generate([tokens], model, max_tokens=64, temperature=0.0, eos_id=tokenizer.instruct_tokenizer.tokenizer.eos_id)
        result = tokenizer.instruct_tokenizer.tokenizer.decode(out_tokens[0])


        return result

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {"model": self.model}

llm_mistral = CustomLLMMistral(model=model, tokenizer=tokenizer)


# llm_mistral