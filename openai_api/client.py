import time
from openai import OpenAI

from app import settings

client = OpenAI(
    api_key=settings.API_OPEN_AI
)

def get_car_ai_bio(model, brand, year):
    # Configuração da chave de API
    time.sleep(1)
  

    # Prompt para o OpenAI
    message = """Crie uma descrição de venda com no máximo 250 caracteres para {}, {}, {}."""
    message = message.format(model, brand, year)

    # Chamada à API usando a nova interface (a partir de openai >= 1.0.0)
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo'
    )

    # Retorna o texto gerado
    return response.choices[0].message.content
