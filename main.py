import telebot
import os
import random
import json

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

users = {}

test_questions = [
    {"q": "Выбери правильный вариант: She ___ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "goes", "level": "A1", "topic": "grammar"},
    {"q": "Переведи слово: CAT", "options": ["собака", "кошка", "птица", "рыба"], "answer": "кошка", "level": "A1", "topic": "words"},
    {"q": "Выбери правильный вариант: I ___ TV when you called.", "options": ["watch", "watched", "was watching", "am watching"], "answer": "was watching", "level": "B1", "topic": "grammar"},
    {"q": "Что означает фраза: Could you give me a hand?", "options": ["Дай руку", "Помоги мне", "Подожди", "Уходи"], "answer": "Помоги мне", "level": "B1", "topic": "phrases"},
    {"q": "Переведи слово: AMBIGUOUS", "options": ["ясный", "неоднозначный", "сложный", "простой"], "answer": "неоднозначный", "level": "B2", "topic": "words"},
    {"q": "Выбери правильный вариант: If I ___ rich, I would travel the world.", "options": ["am", "was", "were", "be"], "answer": "were", "level": "B2", "topic": "grammar"},
    {"q": "Что означает: To beat around the bush?", "options": ["Бить по кустам", "Говорить прямо", "Ходить вокруг да около", "Прятаться"], "answer": "Ходить вокруг да около", "level": "B2", "topic": "phrases"},
    {"q": "Выбери правильный вариант: The report ___ by tomorrow.", "options": ["will finish", "will be finished", "is finishing", "finishes"], "answer": "will be finished", "level": "C1", "topic": "grammar"},
    {"q": "Переведи слово: EPHEMERAL", "options": ["вечный", "мгновенный", "кратковременный", "постоянный"], "answer": "кратковременный", "level": "C1", "topic": "words"},
    {"q": "Что означает: To read between the lines?", "options": ["Читать медленно", "Понимать скрытый смысл", "Пропускать строки", "Читать вслух"], "answer": "Понимать скрытый смысл", "level": "C1", "topic": "phrases"},
]

lessons = {
    "A1": {
        "words": [("cat","кошка"),("dog","собака"),("house","дом"),("water","вода"),("food","еда")],
        "grammar": [("I am happy","Я счастлив"),("She is a teacher","Она учитель"),("We go to school","Мы идём в школу")],
        "phrases": [("Hello!","Привет!"),("Thank you","Спасибо"),("Goodbye","До свидания")]
    },
    "B1": {
        "words": [("achieve","достигать"),("improve","улучшать"),("suggest","предлагать"),("require","требовать")],
        "grammar": [("I was watching TV","Я смотрел ТВ"),("She has been working","Она работала"),("They had finished","Они закончили")],
        "phrases": [("Could you give me a hand?","Не могли бы вы помочь?"),("I was wondering if...","Я хотел спросить..."),("As far as I know","Насколько я знаю")]
    },
    "B2": {
        "words": [("ambiguous","неоднозначный"),("relevant","актуальный"),("significant","значительный"),("establish","устанавливать")],
        "grammar": [("If I were you...","Если бы я был вами..."),("The work will be done","Работа будет сделана"),("Having finished work...","Закончив работу...")],
        "phrases": [("To beat around the bush","Ходить вокруг да около"),("Hit the nail on the head","Попасть в точку"),("Break the ice","Растопить лёд")]
    }
}

def get_user(uid):
    if uid not in users:
        users[uid] = {"level": None, "weak": [], "score": {"grammar": 0, "words": 0, "phrases": 0}, "total": {"grammar": 0, "words": 0, "phrases": 0}}
    return users[uid]

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    users[uid] = {"level": None, "weak": [], "score": {"grammar": 0, "words": 0, "phrases": 0}, "total": {"grammar": 0, "words": 0, "phrases": 0}}
    bot.reply_to(message, "👋 Привет! Я помогу тебе учить английский!\n\nСначала пройди тест чтобы определить твой уровень.\n\n/test — начать тест")

@bot.message_handler(commands=['test'])
def start_test(message):
    uid = message.from_user.id
    user = get_user(uid)
    user['test_index'] = 0
    user['test_correct'] = 0
    user['test_topics'] = {"grammar": 0, "words": 0, "phrases": 0}
    ask_question(message, uid)

def ask_question(message, uid):
    user = get_user(uid)
    idx = user.get('test_index', 0)
    if idx >= len(test_questions):
        finish_test(message, uid)
        return
    q = test_questions[idx]
    options = q['options']
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for opt in options:
        markup.add(opt)
    bot.send_message(message.chat.id, f"❓ Вопрос {idx+1}/{len(test_questions)}:\n\n{q['q']}", reply_markup=markup)
    bot.register_next_step_handler(message, check_test_answer, uid)

def check_test_answer(message, uid):
    user = get_user(uid)
    idx = user.get('test_index', 0)
    q = test_questions[idx]
    if message.text == q['answer']:
        user['test_correct'] += 1
        user['test_topics'][q['topic']] += 1
    user['test_index'] = idx + 1
    ask_question(message, uid)

def finish_test(message, uid):
    user = get_user(uid)
    correct = user.get('test_correct', 0)
    topics = user.get('test_topics', {})
    if correct <= 3:
        level = "A1"
    elif correct <= 6:
        level = "B1"
    else:
        level = "B2"
    user['level'] = level
    weak = []
    for topic, count in topics.items():
        if count < 2:
            weak.append(topic)
    user['weak'] = weak if weak else list(topics.keys())
    weak_ru = {"grammar": "грамматика", "words": "слова", "phrases": "фразы"}
    weak_text = ", ".join([weak_ru[w] for w in user['weak']])
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f"✅ Тест завершён!\n\n📊 Правильных ответов: {correct}/{len(test_questions)}\n🎯 Твой уровень: *{level}*\n📌 Слабые места: {weak_text}\n\nТеперь начнём учиться по твоим слабым местам!\n\n/learn — начать обучение\n/progress — мой прогресс", parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['learn'])
def learn(message):
    uid = message.from_user.id
    user = get_user(uid)
    if not user['level']:
        bot.reply_to(message, "Сначала пройди тест! /test")
        return
    level = user['level']
    topic = random.choice(user['weak'])
    items = lessons.get(level, lessons['B1'])[topic]
    item = random.choice(items)
    topic_ru = {"grammar": "📖 Грамматика", "words": "📚 Слово", "phrases": "💬 Фраза"}
    bot.reply_to(message, f"{topic_ru[topic]}:\n\n*{item[0]}*\n🇷🇺 {item[1]}\n\n/quiz — проверь себя\n/learn — ещё урок", parse_mode='Markdown')

@bot.message_handler(commands=['quiz'])
def quiz(message):
    uid = message.from_user.id
    user = get_user(uid)
    if not user['level']:
        bot.reply_to(message, "Сначала пройди тест! /test")
        return
    level = user['level']
    topic = random.choice(user['weak'])
    items = lessons.get(level, lessons['B1'])[topic]
    item = random.choice(items)
    user['quiz_answer'] = item[1]
    user['quiz_topic'] = topic
    bot.reply_to(message, f"❓ Переведи на русский:\n\n*{item[0]}*", parse_mode='Markdown')
    bot.register_next_step_handler(message, check_quiz, uid)

def check_quiz(message, uid):
    user = get_user(uid)
    correct = user.get('quiz_answer', '')
    topic = user.get('quiz_topic', 'words')
    user['total'][topic] += 1
    if message.text.lower().strip() == correct.lower().strip():
        user['score'][topic] += 1
        bot.reply_to(message, "✅ Правильно! Молодец! 🎉\n\n/quiz — ещё вопрос\n/learn — новый урок")
    else:
        bot.reply_to(message, f"❌ Неправильно!\n✅ Правильный ответ: *{correct}*\n\n/quiz — ещё вопрос\n/learn — новый урок", parse_mode='Markdown')

@bot.message_handler(commands=['progress'])
def progress(message):
    uid = message.from_user.id
    user = get_user(uid)
    if not user['level']:
        bot.reply_to(message, "Сначала пройди тест! /test")
        return
    score = user['score']
    total = user['total']
    text = f"📊 Твой прогресс (уровень {user['level']}):\n\n"
    topics_ru = {"grammar": "Грамматика", "words": "Слова", "phrases": "Фразы"}
    for t, name in topics_ru.items():
        s = score[t]
        tot = total[t]
        pct = int(s/tot*100) if tot > 0 else 0
        text += f"{name}: {s}/{tot} ({pct}%)\n"
    bot.reply_to(message, text)

bot.infinity_polling()
