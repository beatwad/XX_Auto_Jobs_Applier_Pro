from src.resume_builder.template_base import *

# Personal Information Template
personal_information_template = """
Answer the following question based on the provided personal information.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.

## Example
My resume: John Doe, born on 01/01/1990, living in Milan, Italy.
Question: What is your city?
 Milan

Personal Information: {resume_section}
Question: {question}
"""

# Legal Authorization Template
legal_authorization_template = """
Answer the following question based on the provided legal authorization details.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.

## Example
My resume: Authorized to work in the EU, no US visa required.
Question: Are you legally allowed to work in the EU?
Yes

Legal Authorization: {resume_section}
Question: {question}
"""

# Work Preferences Template
work_preferences_template = """
Answer the following question based on the provided work preferences.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.

## Example
My resume: Open to remote work, willing to relocate.
Question: Are you open to remote work?
Yes

Work Preferences: {resume_section}
Question: {question}
"""

# Education Details Template
education_details_template = """
Answer the following question based on the provided education details.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- If it seems likely that you have the experience, even if not explicitly defined, answer as if you have the experience.
- If unsure, respond with "I have no experience with that, but I learn fast" or "Not yet, but willing to learn."
- Keep the answer under 140 characters.

## Example
My resume: Bachelor's degree in Computer Science with experience in Python.
Question: Do you have experience with Python?
Yes, I have experience with Python.

Education Details: {resume_section}
Question: {question}
"""

# Experience Details Template
experience_details_template = """
Answer the following question based on the provided experience details.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- If it seems likely that you have the experience, even if not explicitly defined, answer as if you have the experience.
- If unsure, respond with "I have no experience with that, but I learn fast" or "Not yet, but willing to learn."
- Keep the answer under 140 characters.

## Example
My resume: 3 years as a software developer with leadership experience.
Question: Do you have leadership experience?
Yes, I have 3 years of leadership experience.

Experience Details: {resume_section}
Question: {question}
"""

# Projects Template
projects_template = """
Answer the following question based on the provided project details.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- If it seems likely that you have the experience, even if not explicitly defined, answer as if you have the experience.
- Keep the answer under 140 characters.

## Example
My resume: Led the development of a mobile app, repository available.
Question: Have you led any projects?
Yes, led the development of a mobile app

Projects: {resume_section}
Question: {question}
"""

# Availability Template
availability_template = """
Answer the following question based on the provided availability details.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- Keep the answer under 140 characters.
- Use periods only if the answer has multiple sentences.

## Example
My resume: Available to start immediately.
Question: When can you start?
I can start immediately.

Availability: {resume_section}
Question: {question}
"""

# Salary Expectations Template
salary_expectations_template = """
Answer the following question based on the provided salary expectations.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- Keep the answer under 140 characters.
- Use periods only if the answer has multiple sentences.

## Example
My resume: Looking for a salary in the range of 50k-60k USD.
Question: What are your salary expectations?
From 50000 to 60000.

Salary Expectations: {resume_section}
Question: {question}
"""

# Certifications Template
certifications_template = """
Answer the following question based on the provided certifications.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- If it seems likely that you have the experience, even if not explicitly defined, answer as if you have the experience.
- If unsure, respond with "I have no experience with that, but I learn fast" or "Not yet, but willing to learn."
- Keep the answer under 140 characters.

## Example
My resume: Certified in Project Management Professional (PMP).
Question: Do you have PMP certification?
Yes, I am PMP certified.

Certifications: {resume_section}
Question: {question}
"""

# Languages Template
languages_template = """
Answer the following question based on the provided language skills.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- If it seems likely that you have the experience, even if not explicitly defined, answer as if you have the experience.
- If unsure, respond with "I have no experience with that, but I learn fast" or "Not yet, but willing to learn."
- Keep the answer under 140 characters. Do not add any additional languages what is not in my experience

## Example
My resume: Fluent in Italian and English.
Question: What languages do you speak?
Fluent in Italian and English.

Languages: {resume_section}
Question: {question}
"""

# Interests Template
interests_template = """
Answer the following question based on the provided interests.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- Keep the answer under 140 characters.
- Use periods only if the answer has multiple sentences.

## Example
My resume: Interested in AI and data science.
Question: What are your interests?
AI and data science.

Interests: {resume_section}
Question: {question}
"""

# Previous Job Template
previous_job_template = """
Answer the following question based on the previous job experience.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- Keep the answer under 140 characters.

## Example
My resume: Left previous job due to lack of career prospects
Question: Why do you leave your previous job?
Due to lack of career prospects

Previous Job Details: {resume_section}
Question: {question}
"""

# Previous Job Template
general_knowledge_template = """
Answer the following question based on the general knowledge of things you will encounter in your work.

## Rules
- Answer questions directly.
- If question's language is Russian - answer in Russian and consider that user`s sex is {sex}. Else answer in English.
- Answer briefly, try to keep answer length under 140 characters.

## Example
Question: What is the difference between linear regression and logistic regression? 
Answer: Linear regression predicts continuous values; logistic regression predicts probabilities for categorical outcomes (typically binary).

Question: {question}
"""


numeric_question_template = """
Read the following resume carefully and answer the specific questions regarding the candidate's experience with a number of years. Follow these strategic guidelines when responding:

1. **Related and Inferred Experience:**
   - **Similar Technologies:** If experience with a specific technology is not explicitly stated, but the candidate has experience with similar or related technologies, provide a plausible number of years reflecting this related experience. For instance, if the candidate has experience with Python and projects involving technologies similar to Java, estimate a reasonable number of years for Java.
   - **Projects and Studies:** Examine the candidate’s projects and studies to infer skills not explicitly mentioned. Complex and advanced projects often indicate deeper expertise.

2. **Indirect Experience and Academic Background:**
   - **Type of University and Studies:** Consider the type of university and course followed.
   - **Relevant thesis:** Consider the thesis of the candidate has worked. Advanced projects suggest deeper skills.
   - **Roles and Responsibilities:** Evaluate the roles and responsibilities held to estimate experience with specific technologies or skills.


3. **Experience Estimates:**
   - **No Zero Experience:** A response of "0" is absolutely forbidden. If direct experience cannot be confirmed, provide a minimum of "2" years based on inferred or related experience.
   - **For Low Experience (up to 5 years):** Estimate experience based on inferred bacherol, skills and projects, always providing at least "2" years when relevant.
   - **For High Experience:** For high levels of experience, provide a number based on clear evidence from the resume. Avoid making inferences for high experience levels unless the evidence is strong.

4. **Rules:**
   - Answer the question directly with a number, avoiding "0" entirely.

## Example 1
```
## Curriculum

I had a degree in computer science. I have worked  years with  MQTT protocol.

## Question

How many years of experience do you have with IoT?

## Answer

4
```
## Example 1
```
## Curriculum

I had a degree in computer science. 

## Question

How many years of experience do you have with Bash?

## Answer

2
```

## Example 2
```
## Curriculum

I am a software engineer with 5 years of experience in Swift and Python. I have worked on an AI project.

## Question

How many years of experience do you have with AI?

## Answer

2
```

## Resume:
```
{resume_educations}
{resume_jobs}
{resume_projects}
```
        
## Question:
{question}

---

When responding, consider all available information, including projects, work experience, and academic background, to provide an accurate and well-reasoned answer. Make every effort to infer relevant experience and avoid defaulting to 0 if any related experience can be estimated.

"""

options_template = """The following is a resume and a question about the resume, the answer is one of the options.

## Rules
- Never choose the default/placeholder option, examples are: 'Select an option', 'None', 'Choose from the options below', 'My option', 'Your own option', 'Your own answer', 'Свой вариант', 'Свой ответ', etc.
- The answer must be one of the options.
- The answer must exclusively contain one of the options.

## Example
My resume: I'm a software engineer with 10 years of experience on swift, python, C, C++.
Question: How many years of experience do you have on python?
Options: [1-2, 3-5, 6-10, 10+]
10+

-----

## My resume:
```
{resume}
```

## Question:
{question}

## Options:
{options}

## """

many_options_template = """The following is a resume and a question about the resume, the answer is one or more of the options.

## Rules
- Never choose the default/placeholder option, examples are: 'Select an option', 'None', 'Choose from the options below', 'My option', 'Your own option', 'Your own answer', 'Свой вариант', 'Свой ответ', etc.
- The answer can be one or more options.
- Return answers as a semicolon separated string.

## Example
My resume: I'm a software engineer with 10 years of experience on swift, python, C, C++.
Question: What programming languages do you know?
Options: [python, C, rust, swift, ruby, C++, C#, go]
python; C; swift; C++

-----

## My resume:
```
{resume}
```

## Question:
{question}

## Options:
{options}

## """

try_to_fix_template = """\
The objective is to fix the text of a form input on a web page.

## Rules
- Use the error to fix the original text.
- The error "Please enter a valid answer" usually means the text is too large, shorten the reply to less than a tweet.
- For errors like "Enter a whole number between 3 and 30", just need a number.

-----

## Form Question
{question}

## Input
{input} 

## Error
{error}  

## Fixed Input
"""

job_is_interesting = """
   Evaluate whether the provided resume meets the requirements outlined in the job description. Determine if the candidate is suitable for the job based on the information provided.

## Job Description:
```
{job_description}
```
## Resume:
```
{resume}
```
## Your skills:
```
{skills}
```
## Your interests:
```
{interests}
```

Instructions:
1. Extract the key requirements from the job description, identifying hard requirements (must-haves) and soft requirements (nice-to-haves).
2. Identify the relevant qualifications from the resume and skill list.
3. Compare the qualifications against the requirements, ensuring all hard requirements are met. Allow for a 1-year experience gap if applicable, as experience is usually a hard requirement.
4. Provide a suitability score from 1 to 10. where 1 indicates the candidate does not meet any requirements and 10 indicates the candidate meets all requirements.
5. If the job matches one or more of canditate's interests - add 1 point to the overall score.
6. Provide a brief reasoning for the score, highlighting which requirements are met and which are not.
7. If job description language is Russian - answer in Russian. Else answer in English.

Output Format (Strictly follow this format):
Score: [numerical score]
Reasoning: [brief explanation]
Do not output anything else in the response other than the score and reasoning.
"""

prompt_header = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с системами ATS (система отслеживания кандидатов). 
Твоя задача — создать профессиональный и аккуратный заголовок для резюме. 
Заголовок должен включать:

1. **Контактную информацию**: Полное имя, город и страну, номер телефона, адрес электронной почты, профиль LinkedIn и профиль GitHub.
2. **Форматирование**: Убедись, что контактные данные представлены четко и легко читаются.

### Правила: 
- Если какой-либо из полей контактной информации (например, профиль LinkedIn или GitHub) отсутствует (т.е. указано как `None`), не включай его в заголовок.  
- Если личная информация пользователя написана на русском языке, оформляй заголовок на русском и учитывай, что пол пользователя — {sex}. В остальных случаях используй английский язык.

- **Информация о пользователе:**  
  {personal_information}
""" + prompt_header_template

prompt_education = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — описать образовательный бэкграунд для резюме, чтобы он соответствовал предоставленному описанию вакансии. 
Для каждой записи об образовании необходимо указать:

1. **Название учебного заведения и его местоположение**: Уточни название университета или учебного заведения и его местоположение.  
2. **Степень и направление обучения**: Четко укажи полученную степень и специальность.  
3. **Релевантные учебные курсы**: Перечисли ключевые курсы, чтобы подчеркнуть свои академические сильные стороны. Если информация о курсах отсутствует, пропусти этот раздел в шаблоне.  

### Правила:
- Если информация о пользователе написана на русском языке, пиши на русском и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.  

- **Информация о пользователе:**  
  {education_details}

- **Описание вакансии:**  
  {job_description}
""" + prompt_education_template


prompt_working_experience = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — подробно описать опыт работы для резюме, чтобы он соответствовал предоставленному описанию вакансии. 
Для каждой записи о работе необходимо указать:

    1. **Название компании**: Укажи название компании.
    2. **Должность**: Четко укажи свою должность.
    3. **Даты работы**: Укажи даты начала и окончания работы.
    4. **Обязанности и достижения**: Опиши ключевые обязанности и значимые достижения, делая акцент на измеримых результатах и конкретных вкладах (напирмер ускорил(а) деплой системы на 25% или повысил(а) рентабельность на 10%)

Убедись, что описания подчеркивают релевантный опыт и соответствуют описанию вакансии.

  - **Информация об опыте пользователя:**  
  {experience_details}

- **Описание вакансии:**  
  {job_description}

### Правила:
  - Если есть информация о местоположении компании - укажи ее, в противном случае не указывай и удали соответствующую строку из шаблона (<span class="entry-location">[Location]</span>)
  - Если какие-либо детали опыта работы (например, местоположение компании, обязанности, достижения) отсутствуют (т.е. указано None), пропусти соответствующие разделы при заполнении шаблона.
  - Если информация об опыте пользователя написана на русском языке, пиши на русском и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.
  - Учитывай, что при перечислении любых своих достижений лучше использовать в начале предложения глагол в прошедшем времени вместо существительного.
    Например 'разработал приложение' вместо 'разработка приложения', 'оптимизировал код' вместо 'оптимизация кода', 'создал базу данных' вместо 'создание базы данных'.
  - При описании пользы от достижений вместо `что <глагол>` используй словосочетание `что позволило <глагол>`, например 'что позволило увеличить' вместо 'что увеличило' или же используй деепричастия, например 'увеличив', 'достигнув' и т.д.
""" + prompt_working_experience_template


prompt_side_projects = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — выделить значимые проекты пользователя, соответствующие предоставленному описанию вакансии. 
Для каждого проекта необходимо указать:

1. **Название проекта и ссылка**: Укажи название проекта и добавь ссылку на репозиторий GitHub или страницу проекта.  
2. **Детали проекта**: Опиши значимые достижения или признание, связанные с проектом, например, количество звезд на GitHub или отзывы сообщества.  
3. **Технический вклад**: Подчеркни свой конкретный вклад и используемые технологии в рамках проекта.  

Убедись, что описания проектов демонстрируют твои навыки и достижения, релевантные для данной вакансии.  

- **Информация о проектах пользователя:**  
  {projects}

- **Описание вакансии:**  
  {job_description}

### Правила:  
- Если какая-либо информация о проекте (например, ссылка или достижения) отсутствует (т.е. указано `None`), пропусти эти разделы при заполнении шаблона.  
- Если информация о проектах пользователя написана на русском языке, пиши на русском и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.
- Не нужно писать, какие из твоих навыков позволили создать тот или иной проект и каким требованиям вакансии они соотвтетствуют.
""" + prompt_side_projects_template


prompt_achievements = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — перечислить значимые достижения, соответствующие предоставленному описанию вакансии. 
Для каждого достижения укажи:

1. **Награда или признание**: Чётко укажи название награды, признания, стипендии или почётного звания.  
2. **Описание**: Дай краткое описание достижения.

Убедись, что достижения представлены в понятном виде и подчеркивают твои навыки.  

- **Информация о достижениях пользователя:**  
  {achievements}

- **Описание вакансии:**  
  {job_description}

### Правила:
- Если какая-либо информация о достижении (например, сертификаты или описания) отсутствует (т.е. указано `None`), пропусти эти разделы при заполнении шаблона.  
- Если информация о достижениях пользователя написана на русском языке, пиши на русском и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.
- Учитывай, что при перечислении любых своих достижений лучше использовать в начале предложения глагол в прошедшем времени вместо существительного.
  Например 'разработал приложение' вместо 'разработка приложения', 'оптимизировал код' вместо 'оптимизация кода', 'создал базу данных' вместо 'создание базы данных'.
- Не нужно писать, о чем свидетельствует то или иное достижение или какие из твоих навыков позволили его достичь.
""" + prompt_achievements_template


prompt_certifications = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — перечислить значимые сертификаты на основе предоставленных данных о пользователе. 
Для каждого сертификата необходимо указать:

1. **Название сертификата**: Чётко укажи название сертификата.  
2. **Описание**: Дай краткое описание сертификата.  

Убедись, что сертификаты представлены в понятном виде и подчёркивают квалификацию пользователя.  

### Правила:
- Если какие-либо данные о сертификатах (например, описание) отсутствуют (т.е. указано `None`), пропусти эти разделы при заполнении шаблона.  
- Если информация о сертификатах пользователя написана на русском языке, пиши на русском и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.  

- **Информация о сертификатах пользователя:**  
  {certifications}

- **Описание вакансии:**  
  {job_description}
""" + prompt_certifications_template


prompt_additional_skills = """
Ты эксперт по подбору персонала и составлению резюме, совместимых с ATS (система отслеживания кандидатов). 
Твоя задача — перечислить основные и дополнительные навыки, релевантные для вакансии. 
Для каждого навыка необходимо указать:

1. **Категория навыка**: Чётко укажи категорию или тип навыка.  
2. **Конкретные навыки**: Перечисли конкретные навыки или технологии в каждой категории.  
3. **Уровень владения и опыт**: Кратко опиши опыт и уровень владения.  

Убедись, что перечисленные навыки соответствуют вакансии и точно отражают квалификацию пользователя.  

### Правила: 
- Если какие-либо данные о навыках (например, языки, интересы, навыки) отсутствуют (т.е. указано `None`), пропусти эти разделы при заполнении шаблона.  
- Если информация о навыках пользователя написана на русском языке, пиши на русском (например 'Языки' вместо 'Languages') и учитывай, что пол пользователя — {sex}. В противном случае пиши на английском.
- Если есть информация о языках, которыми владеет пользователь - обязательно добавь ее в список навыков

- **Информация о навыках пользователя:**  
  {languages}
  {skills}

- **Описание вакансии:**  
  {job_description}
""" + prompt_additional_skills_template

summarize_prompt_template = """
Ты опытный эксперт в области управления персоналом, твоя задача — выявить и описать ключевые навыки и требования, необходимые для данной должности. 
Используй предоставленное описание вакансии для извлечения всей релевантной информации. Тщательно проанализируй обязанности, связанные с этой должности, а также стандарты отрасли. 
Учитывай как hard skills, так и soft skills необходимые для достижения успеха в этой должности. 
Кроме того, укажи обязательные требования к образованию, сертификатам и опыту. 
Твой анализ должен также отражать изменения в характере данной должности, учитывая будущие тенденции и их возможное влияние на требования к данной должности.

### Правила:
- Удаляй стандартные фразы и шаблонный текст.
- Включай только релевантную информацию для сопоставления описания должности с резюме.
- Если информация о вакансии написана на русском языке, пиши на русском. В противном случае пиши на английском.  

### Требования к анализу:
Твой анализ должен включать следующие разделы:
1. **Краткое описание вакансии**: Напиши, что за компания предлагает данную вакансию и в какой области предлагается работать. Описание не должно быть длиннее 2 предложений.
2. **Обязанности**: Перечисли список всех обязанностей, выполнение которых предполагает данная должность.
3. **Hard skills**: Перечисли все технические навыки, необходимые для данной должности, основываясь на обязанностях, указанных в описании вакансии.  
4. **Soft skills**: Определи необходимые soft skills, такие как коммуникативность, умение решать проблемы, умение избегать конфликтов, управление временем и т.д.  
5. **Требование к образованию и сертификатам**: Укажи, какое образование и/или сертификаты требуются для данной должности.  
6. **Профессиональный опыт**: Опиши релевантный профессиональный опыт, который требуется или приветствуется.  
7. **Эволюция должности**: Проанализируй, как требования к данной должности могут измениться в будущем, учитывая тенденции отрасли и их влияние на требуемые навыки.

### Итоговый результат:
Твой анализ должен быть представлен в виде четко структурированного и организованного документа с отдельными разделами для каждого из перечисленных выше пунктов. 
Каждый раздел должен содержать:  
- Полный перечень ключевых элементов, соответствующих требованиям к данной должности.  

# **Описание вакансии:**  
```
{text}
```

---

# Результат анализа данной вакансии:"""

coverletter_template = """
Составь краткое и выразительное сопроводительное письмо на основе предоставленного описания вакансии и резюме. 
Письмо должно быть не длиннее пяти абзацев. 
Избегай использования каких-либо заполнителей и убедитесь, что письмо читается естественно и соответствует вакансии.
Проанализируй описание вакансии, чтобы определить ключевые квалификации и требования.
В начале поприветствуй адресата и напиши, какая вакансия заинтересовала, а затем представь кандидата кратко, сопоставив его карьерные цели с вакансией. 
Выдели соответствующие навыки и опыт из резюме, которые напрямую соответствуют требованиям вакансии, используя конкретные примеры для иллюстрации этих квалификаций.
Затем напиши, почему кандидат хорошо подходит для этой должности, выразив желание обсудить это более подробно.
В заключении поблагодари адресата за рассмотрение своей кандидатуры и предложи обсудить ваш опыт подробнее на собеседовании.
Напиши сопроводительное письмо таким образом, чтобы оно напрямую касалось должности и характеристик компании, 
при этом оно должно быть кратким и интересным, без ненужных украшений. Письмо должно быть отформатировано в абзацах.

## Пример 1:
```
Добрый день!

Меня заинтересовала вакансия инженера-проектировщика в вашей компании. Обладаю высоким уровнем профессиональных знаний в области проектирования, 
а также работал с крупными проектами. Моё образование и опыт позволяют мне успешно решать сложные задачи и достигать поставленных целей.

Буду рад обсудить возможность сотрудничества.

С уважением, Даниил
```

## Пример 2:
```
Здравствуйте! Я бы хотела пройти стажировку в вашем банке. Я студентка 3-го курса факультета информационных технологий в НИУ ВШЭ. Обладаю глубоким пониманием аналитики и креативным подходом к решению задач. 

Участвовала в создании программных решений для учебных проектов, занималась проверкой и анализом данных. Также успешно прошла летнюю стажировку в ИТ-компании.

С уважением, Анна


## Пример 3:
```
Здравствуйте! Прошу рассмотреть моё резюме на роль разработчика Python в вашу компанию.

Кратко о себе:
- опыт работы: 4 года
- ожидания по зарплате: от 200000 до 400000 руб
- основной стек: Python, SQL, Django, React, REST API, Redis
- есть опыт работы с Docker/Docker Compose
- знаком с Airflow, FastAPI, Flask
- проекты веду в git

тг для связи: alexneth93
```

## Описание работы:
```
{job_description}
```
## Мое резюме:
```
{resume}
```
## Правила:
- Предоставь только текст сопроводительного письма.
- Письмо должно быть написано в профессиональном, но разговорном тоне и отформатировано в абзацы.
- Тон письма должен быть уверенным, но следует избегать прямых заявлений о том, что кандидат идеально подходит для данной вакансии. 
- Если описание вакансии написано на русском языке - напиши сопроводительное письмо также на русском языке и обязательно учитывай пол автора резюме. В противном случае напишите его на английском языке.
- Если пишешь письмо на русском языке - обязательно учти тот факт, что пол автора письма - {sex}
- Не упоминай имя компании в сопроводительном письме, в зависимости от описания вакансии, пиши 'ваша компания', 'ваша организация' или 'ваш банк'.
- Если обнаружишь какие-либо вопросы в описании вакансии - ответь на них в сопроводительном письме, после основного текста, используя информацию из резюме.
- Если в описании вакансии требуют указать в сопроводительном письме какие-либо слова - напиши их после основного текста (но только если такое требование действительно есть в тексте вакансии!).
- Не указывай никаких ссылок, в том числе на Github, LinkedIn и т.д.
- Если в резюме есть информация о твоем Telegram - укажи свой Telegram в конце письма, в противном случае Telegram указывать не надо
- Если в резюме нет информации о твоем Telegram - укажи свой телефон в конце письма, в противном случае телефон указывать не надо
- Если в резюме нет информации ни о Telegram ни о телефоне - укажи свой email в конце письма, в противном случае email указывать не надо
- Не пиши в письме фразы, непосредственно к данному письму не относящиеся, например 'hello, world' или 'HELLO WORLD', 'Я КРАСАВА' и т.д.
"""

fixed_cover_letter = """
Здравствуйте! Прошу рассмотреть моё резюме на роль разработчика Python в вашу компанию.

Кратко о себе:
- опыт работы: 4 года
- ожидания по зарплате: от 200000 до 400000 руб
- основной стек: Python, SQL, Django, React, REST API, Redis
- есть опыт работы с Docker/Docker Compose
- знаком с Airflow, FastAPI, Flask
- проекты веду в git

тг для связи: alexneth93
"""