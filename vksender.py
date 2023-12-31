import vk_api
import random

user_login = ''
user_password = ''
app_id = '2685278' #оставляем этот

def captcha_handler(captcha):
    # Решение капчи
    captcha_solution = input("Введите решение капчи: ")
    return captcha.try_again(captcha_solution)

vk_session = vk_api.VkApi(login=user_login, password=user_password, app_id=app_id, captcha_handler=captcha_handler)
try:
    vk_session.auth()
except vk_api.exceptions.Captcha as captcha_exception:
    print(f"Captcha needed: {captcha_exception}")
    pass


message = "С новым годом! 🎉 Пусть этот год принесет счастья, удачи и отличного настроения!"

# target_user_ids = [533859410, 687457291, 650065272, 557896984, 635186900, 521047825, 412793926, 624544361, 561259196, 639851366,
#                    535132685, 570217827, 360176010, 283167735, 561816046, 208089228, 680214220, 519288592, 616457800, 616017797,
#                    219296836, 613441379, 671462649, 480087663, 677821944, 683333929, 613873279, 551509680, 417180564, 463663936,
#                    562247695, 674383258, 619582096, 475817109, 591220404, 631973753, 675238131, 235702178, 611057264, 476326328,
#                    113340897, 304391647, 500123063, 561315921, 609741879, 590953928, 362276625, 612817851, 544092121, 568590003]

user_id = friends = vk_session.method('friends.get', {'order': 'hints', 'fields': 'id'})

for frined in user_id["items"]:
    try:
        random_id = random.randint(1, 100000)
        vk_session.method('messages.send', {'user_id': frined["id"], 'message': message, 'random_id': random_id})
        print(f"Сообщение успешно отправлено пользователю с ID {frined["id"]}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения пользователю с ID {frined["id"]}: {e}")
        continue

print("Завершено.")


