from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
OPERATOR = env.list("OPERATOR")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
GROUP_ID = env.str("GROUP_ID", "-1002176563327")  # Guruh id raqami