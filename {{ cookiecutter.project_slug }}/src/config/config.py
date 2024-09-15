from pydantic_settings import BaseSettings
from functools import cached_property
from google.cloud import secretmanager


class Config(BaseSettings):

    PROJECT_NAME: str = "{{ cookiecutter.project_slug }}"
    PROJECT_NUMBER: str = ""
    PROJECT_ID: str = ""
    DATASET_ID: str = ""
    VERSION: str = "0.0.1"

    @cached_property
    def OPENAI_API_KEY(self):
        return self.access_secret("OPENAI_API_KEY")

    def access_secret(self, secret_name):
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{self.PROJECT_NUMBER}/secrets/{secret_name}/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")


config = Config()
