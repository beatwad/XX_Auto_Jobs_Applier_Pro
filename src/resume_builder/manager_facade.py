import os
from pathlib import Path
import tempfile
import inquirer
from src.resume_builder.config import global_config
from src.resume_builder.utils import HTML_to_PDF
import webbrowser
from loguru import logger

class FacadeManager:
    def __init__(self, api_key, style_manager, resume_generator, resume_object, log_path):
        # Ottieni il percorso assoluto della directory della libreria
        lib_directory = Path(__file__).resolve().parent
        global_config.STRINGS_MODULE_RESUME_PATH = lib_directory / "resume_prompt/main_prompt.py"
        global_config.STRINGS_MODULE_RESUME_JOB_DESCRIPTION_PATH = lib_directory / "resume_prompt/job_description_prompt.py"
        global_config.STRINGS_MODULE_NAME = "prompts"
        global_config.STYLES_DIRECTORY = lib_directory / "resume_style"
        global_config.LOG_OUTPUT_FILE_PATH = log_path
        global_config.API_KEY = api_key
        self.style_manager = style_manager
        self.style_manager.set_styles_directory(global_config.STYLES_DIRECTORY)
        self.resume_generator = resume_generator
        self.resume_generator.set_resume_object(resume_object)
        self.selected_style = None  # Proprietà per memorizzare lo stile selezionato

    def prompt_user(self, choices: list[str], message: str) -> str:
        questions = [
            inquirer.List('selection', message=message, choices=choices),
        ]
        return inquirer.prompt(questions)['selection']

    def prompt_for_url(self, message: str) -> str:
        questions = [
            inquirer.Text('url', message=message),
        ]
        return inquirer.prompt(questions)['url']

    def prompt_for_text(self, message: str) -> str:
        questions = [
            inquirer.Text('text', message=message),
        ]
        return inquirer.prompt(questions)['text']

    def choose_style(self):
        styles = self.style_manager.get_styles()
        if not styles:
            logger.warning("Нет доступных стилей")
            return None
        final_style_choice = "Create your resume style in CSS"
        formatted_choices = self.style_manager.format_choices(styles)
        formatted_choices.append(final_style_choice)
        selected_choice = self.prompt_user(formatted_choices, "Which style would you like to adopt?")
        if selected_choice == final_style_choice:
            tutorial_url = "https://github.com/feder-cr/lib_resume_builder_AIHawk/blob/main/how_to_contribute/web_designer.md"
            logger.info("\nOpening tutorial in your browser...")
            webbrowser.open(tutorial_url)
            exit()
        else:
            self.selected_style = selected_choice.split(' (')[0]


    def pdf_base64(self, gpt_resume_generator, job_description_text):
        if self.selected_style is None:
            raise ValueError("Перед созданием PDF-файла необходимо выбрать стиль.")
        
        style_path = self.style_manager.get_style_path(self.selected_style)

        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.html', encoding='utf-8') as temp_html_file:
            temp_html_path = temp_html_file.name
            self.resume_generator.create_resume(gpt_resume_generator, style_path, job_description_text, temp_html_path)
 
        pdf_base64 = HTML_to_PDF(temp_html_path)
        os.remove(temp_html_path)
        return pdf_base64
