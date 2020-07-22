from lib import *
from requests import post

# pylint: disable=no-member

@route("/", method=["get", "post"])
def main_page():

    if request.method == POST:

        message = "Имя:\n" + request.forms.name + "\n\nПочта:\n" + request.forms.email + "\n\nСообщение:\n" + request.forms.inputEmail1
        print(message)

        # # мой id 240874713
        # # id Таиссии 418709985
        send_message(418709985, message)

    return template(
        "main",
        template_title="lemannpsychology",
        template_description="🔥Психолог Пенза🔥  Записаться на прием✍  Консультации онлайн💻 и очно🏬  ✅Индивидуальные/семейные консультации, лечение зависимостей, панических атак, депрессии✅"
    )


@route("/en")
def main_page_en():
    return template(
        "main_en",
        template_title="lemannpsychology",
        template_description="🔥Psychologist from Russia🔥  Consultations online💻 and in-person🏬  ✅Individual / family counseling✅"
    )


@route("/<file:path>")
def static(file):
    f = bottle.static_file(file, "./public")
    if f.status_code == 404:
        return template(
            "error",
            template_title="404",
        )
    return f


def send_message(receiver, message):
    # https://api.vk.com/method/messages.send?user_id=240874713&message=habrahabr&v=5.37&access_token=b21be23e01493801c89174aada70728031c62442cc214d0a741f4217c4bbf48ba2d619e494f9bd9dcc82e
    url = 'https://api.vk.com/method/messages.send'
    query = {
        "user_id" : receiver, 
        "message" : message, 
        "access_token" : "b21be23e01493801c89174aada70728031c62442cc214d0a741f4217c4bbf48ba2d619e494f9bd9dcc82e",
        "v" : 5.50
    }
    post(url, query)


if __name__ == '__main__':
    bottle.run(app=app, host="0.0.0.0", port=8080, quiet=False, reloader=True)
