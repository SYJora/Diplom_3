import string
import random

import allure
import requests

from urls import Urls


class Helper:

    @allure.step('Создать пользователя и вернуть респонс ответ')
    def creat_user_andlogin(self, data):
        response = requests.post(Urls.BASE_URL + Urls.CREATE_USER, json=data)
        return response

    @allure.step('Сгенерировать данные для логирования пользователя через апи')
    def generet_data_for_api(self):
        def generate_random_word(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        data = {
            "email": f"{generate_random_word(7)}@mail.ru",
            "password": "121345",
            "name": 'test'

        }
        return data

    @allure.step('Получение ингредиента')
    def get_ingredients(self):
        respons = requests.get(Urls.BASE_URL + Urls.LIST_INGR)
        ingr = []
        for i in range(3):
            ingr.append(respons.json()['data'][i]['_id'])
        return ingr

    @allure.step('Сделать заказ через API')
    def make_oder_api(self):
        user = Helper()
        data = user.generet_data_for_api()
        response = user.creat_user_andlogin(data)
        respons = requests.post(Urls.BASE_URL + Urls.ORDER,
                                headers={"Authorization": response.json()['accessToken']},
                                json={"ingredients": user.get_ingredients()})
        return respons