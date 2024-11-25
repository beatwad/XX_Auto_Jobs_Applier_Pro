import sys
import importlib
from typing import Any
from string import Template
from typing import Any
from src.resume_builder.gpt_resume import LLMResumer
from src.resume_builder.gpt_resume_job_description import LLMResumeJobDescription
from src.resume_builder.config import global_config

class ResumeGenerator:
    def __init__(self):
        pass
    
    def set_resume_object(self, resume_object):
         self.resume_object = resume_object

    def create_resume(self, gpt_resume_generator: Any, style_path: str, job_description_text: str, temp_html_path):
        gpt_resume_generator.set_job_description_from_text(job_description_text)
        self._create_resume(gpt_resume_generator, style_path, temp_html_path)
    
    def _create_resume(self, gpt_resume_generator: Any, style_path, temp_html_path):
        template = Template(global_config.html_template)
        message = template.substitute(markdown=gpt_resume_generator.generate_html_resume(), style_path=style_path)
        with open(temp_html_path, 'w', encoding='utf-8') as temp_file:
            temp_file.write(message)


def load_module(module_path: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module