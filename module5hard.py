import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname

    def __eq__(self, other):
        return self.nickname == other.nickname

    def check_password(self, password):
        if self.password == hash(password):
            return True
        return False


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    videos = []
    users = []
    current_user = None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_video(self, title):
        for item in self.videos:
            if title in item.title:
                return item

    def get_videos(self, line):
        result = []
        for item in self.videos:
            if line.lower() in item.title.lower():
                result.append(item.title)
        return result

    def play_video(self, video):
        while video.duration > video.time_now:
            video.time_now += 1
            time.sleep(0.1)
            print(video.time_now, end=" ")
        video.time_now = 0
        print("Конец видео")

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return None
        video = self.get_video(title)
        if not video:
            return None
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return None
        self.play_video(video)

    def get_user_by_name(self, nickname):
        for item in self.users:
            if item.nickname == nickname:
                return item

    def log_in(self, nickname, password):
        user = self.get_user_by_name(nickname)
        if user and user.check_password(password):
            self.current_user = user

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user in self.users:
            print("Пользователь vasya_pupkin уже существует")
            return None
        self.users.append(user)
        self.current_user = user


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
