import logging
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

WEB_APP_URL = os.environ.get("WEBAPP_URL", "https://zagifasarkulova-sys.github.io/Ismail/")

from content.a1 import A1
from content.a2 import A2
from content.b1 import B1
from content.b2 import B2
from content.c1 import C1
from content.c2 import C2

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get("BOT_TOKEN")

LEVELS = [A1, A2, B1, B2, C1, C2]
LEVEL_KEYS = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']

def get_level(key):
    mapping = dict(zip(LEVEL_KEYS, LEVELS))
    return mapping.get(key, A1)

def build_markup(buttons):
    return InlineKeyboardMarkup(buttons)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    keyboard = []
    row = []
    for i, lvl in enumerate(LEVELS):
        row.append(InlineKeyboardButton(
            f"{lvl['emoji']} {lvl['name']}",
            callback_data=f"level_{LEVEL_KEYS[i]}"
        ))
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    keyboard.append([InlineKeyboardButton(
        "🎓 IELTS Master — открыть приложение",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )])
    text = "🎓 *English Learn Bot*\n\nВыбери свой уровень английского или открой IELTS приложение:"
    markup = build_markup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=markup, parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=markup, parse_mode="Markdown")

async def cb_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = query.data.replace("level_", "")
    context.user_data['level'] = level_key
    level = get_level(level_key)

    keyboard = [
        [InlineKeyboardButton("📚 Грамматика", callback_data="sec_grammar")],
        [InlineKeyboardButton("📖 Словарь", callback_data="sec_vocab")],
        [InlineKeyboardButton("💬 Фразы", callback_data="sec_phrases")],
        [InlineKeyboardButton("◀️ К уровням", callback_data="back_levels")],
    ]
    await query.edit_message_text(
        level['description'],
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_back_levels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(update, context)

async def cb_back_section(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    keyboard = [
        [InlineKeyboardButton("📚 Грамматика", callback_data="sec_grammar")],
        [InlineKeyboardButton("📖 Словарь", callback_data="sec_vocab")],
        [InlineKeyboardButton("💬 Фразы", callback_data="sec_phrases")],
        [InlineKeyboardButton("◀️ К уровням", callback_data="back_levels")],
    ]
    await query.edit_message_text(
        level['description'],
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_sec_grammar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    topics = level['grammar']

    keyboard = []
    for i, topic in enumerate(topics):
        keyboard.append([InlineKeyboardButton(
            f"{topic['icon']} {topic['title']}",
            callback_data=f"g_topic_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back_section")])

    await query.edit_message_text(
        f"📚 *Грамматика — {level['name']}*\n\nВыбери тему:",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_grammar_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    topic_idx = int(query.data.replace("g_topic_", ""))
    context.user_data['g_topic'] = topic_idx

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]

    keyboard = [
        [InlineKeyboardButton("✏️ Упражнения", callback_data="g_ex_0")],
        [InlineKeyboardButton("🧪 Тест", callback_data="g_test_0")],
        [InlineKeyboardButton("◀️ К темам", callback_data="sec_grammar")],
    ]

    text = topic['explanation']
    if len(text) > 4000:
        text = text[:4000] + "\n\n_...сокращено_"

    await query.edit_message_text(
        text,
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_grammar_exercise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    ex_idx = int(query.data.replace("g_ex_", ""))
    if ex_idx == 0:
        context.user_data['ex_correct'] = 0
    context.user_data['ex_idx'] = ex_idx

    level_key = context.user_data.get('level', 'a1')
    topic_idx = context.user_data.get('g_topic', 0)
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]
    exercises = topic['exercises']

    if ex_idx >= len(exercises):
        correct = context.user_data.get('ex_correct', 0)
        total = len(exercises)
        emoji = "🌟" if correct == total else ("👍" if correct >= total * 0.6 else "📚")
        keyboard = [
            [InlineKeyboardButton("🧪 Перейти к тесту", callback_data="g_test_0")],
            [InlineKeyboardButton("🔄 Повторить", callback_data="g_ex_0")],
            [InlineKeyboardButton("◀️ К теме", callback_data=f"g_topic_{topic_idx}")],
        ]
        await query.edit_message_text(
            f"✅ *Упражнения завершены!*\n\nРезультат: *{correct}/{total}*\n\n"
            f"{emoji} {'Отлично!' if correct == total else 'Продолжай в том же духе!'}",
            reply_markup=build_markup(keyboard),
            parse_mode="Markdown"
        )
        return

    ex = exercises[ex_idx]
    keyboard = []
    for i, opt in enumerate(ex['o']):
        keyboard.append([InlineKeyboardButton(
            f"{'ABCD'[i]}. {opt}",
            callback_data=f"g_ex_ans_{i}"
        )])

    await query.edit_message_text(
        f"✏️ *Упражнение [{ex_idx + 1}/{len(exercises)}]*\n\n{ex['q']}",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_exercise_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    ans_idx = int(query.data.replace("g_ex_ans_", ""))
    ex_idx = context.user_data.get('ex_idx', 0)

    level_key = context.user_data.get('level', 'a1')
    topic_idx = context.user_data.get('g_topic', 0)
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]
    ex = topic['exercises'][ex_idx]

    correct = ans_idx == ex['a']
    if correct:
        context.user_data['ex_correct'] = context.user_data.get('ex_correct', 0) + 1

    explanation = ex.get('e', '')
    if correct:
        result_text = "✅ *Правильно!*"
    else:
        result_text = f"❌ *Неправильно*\n\nПравильный ответ: *{ex['o'][ex['a']]}*"

    text = result_text
    if explanation:
        text += f"\n\n💡 {explanation}"

    next_idx = ex_idx + 1
    total = len(topic['exercises'])
    label = "➡️ Следующее" if next_idx < total else "🏁 Завершить"
    keyboard = [[InlineKeyboardButton(label, callback_data=f"g_ex_{next_idx}")]]

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")

async def cb_grammar_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    test_idx = int(query.data.replace("g_test_", ""))
    if test_idx == 0:
        context.user_data['test_correct'] = 0
    context.user_data['test_idx'] = test_idx

    level_key = context.user_data.get('level', 'a1')
    topic_idx = context.user_data.get('g_topic', 0)
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]
    tests = topic['test']

    if test_idx >= len(tests):
        correct = context.user_data.get('test_correct', 0)
        total = len(tests)
        pct = int(correct / total * 100) if total else 0
        if pct >= 80:
            grade = "🌟 Отлично!"
        elif pct >= 60:
            grade = "👍 Хорошо!"
        else:
            grade = "📚 Нужно повторить"

        keyboard = [
            [InlineKeyboardButton("🔄 Пройти снова", callback_data="g_test_0")],
            [InlineKeyboardButton("◀️ К темам", callback_data="sec_grammar")],
            [InlineKeyboardButton("🏠 Главное меню", callback_data="back_levels")],
        ]
        await query.edit_message_text(
            f"🧪 *Тест завершён!*\n\nРезультат: *{correct}/{total}* ({pct}%)\n\n{grade}",
            reply_markup=build_markup(keyboard),
            parse_mode="Markdown"
        )
        return

    t = tests[test_idx]
    keyboard = []
    for i, opt in enumerate(t['o']):
        keyboard.append([InlineKeyboardButton(
            f"{'ABCD'[i]}. {opt}",
            callback_data=f"g_test_ans_{i}"
        )])

    await query.edit_message_text(
        f"🧪 *Тест [{test_idx + 1}/{len(tests)}]*\n\n{t['q']}",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_test_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    ans_idx = int(query.data.replace("g_test_ans_", ""))
    test_idx = context.user_data.get('test_idx', 0)

    level_key = context.user_data.get('level', 'a1')
    topic_idx = context.user_data.get('g_topic', 0)
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]
    t = topic['test'][test_idx]

    correct = ans_idx == t['a']
    if correct:
        context.user_data['test_correct'] = context.user_data.get('test_correct', 0) + 1

    next_idx = test_idx + 1
    total = len(topic['test'])
    label = "➡️ Следующий" if next_idx < total else "🏁 Результат"
    keyboard = [[InlineKeyboardButton(label, callback_data=f"g_test_{next_idx}")]]

    if correct:
        text = "✅ *Правильно!*"
    else:
        text = f"❌ *Неправильно*\n\nПравильный ответ: *{t['o'][t['a']]}*"

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")

async def cb_sec_vocab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    cats = level['vocabulary']

    keyboard = []
    for i, cat in enumerate(cats):
        keyboard.append([InlineKeyboardButton(
            f"{cat['icon']} {cat['category']}",
            callback_data=f"v_cat_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back_section")])

    await query.edit_message_text(
        f"📖 *Словарь — {level['name']}*\n\nВыбери категорию:",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_vocab_cat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    cat_idx = int(query.data.replace("v_cat_", ""))
    context.user_data['v_cat'] = cat_idx
    context.user_data['v_word'] = 0
    await _show_vocab_word(query, context)

async def cb_vocab_next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    word_idx = int(query.data.replace("v_next_", ""))
    context.user_data['v_word'] = word_idx
    await _show_vocab_word(query, context)

async def _show_vocab_word(query, context):
    level_key = context.user_data.get('level', 'a1')
    cat_idx = context.user_data.get('v_cat', 0)
    word_idx = context.user_data.get('v_word', 0)

    level = get_level(level_key)
    cat = level['vocabulary'][cat_idx]
    words = cat['words']

    if word_idx >= len(words):
        keyboard = [
            [InlineKeyboardButton("🔄 Повторить", callback_data=f"v_cat_{cat_idx}")],
            [InlineKeyboardButton("◀️ К категориям", callback_data="sec_vocab")],
        ]
        await query.edit_message_text(
            f"✅ *Категория завершена!*\n\nВы изучили все слова в «{cat['category']}»!",
            reply_markup=build_markup(keyboard),
            parse_mode="Markdown"
        )
        return

    word = words[word_idx]
    progress = f"{word_idx + 1}/{len(words)}"

    keyboard = [
        [InlineKeyboardButton(
            "➡️ Следующее" if word_idx + 1 < len(words) else "✅ Завершить",
            callback_data=f"v_next_{word_idx + 1}"
        )],
        [InlineKeyboardButton("◀️ К категориям", callback_data="sec_vocab")],
    ]

    text = (
        f"📖 *{cat['icon']} {cat['category']}* [{progress}]\n\n"
        f"🇬🇧 *{word['en']}*\n"
        f"🇷🇺 {word['ru']}\n\n"
        f"💬 _{word.get('ex', '')}_"
    )

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")

async def cb_sec_phrases(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    phrases = level['phrases']

    keyboard = []
    for i, sit in enumerate(phrases):
        keyboard.append([InlineKeyboardButton(
            f"{sit['icon']} {sit['situation']}",
            callback_data=f"ph_sit_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back_section")])

    await query.edit_message_text(
        f"💬 *Фразы — {level['name']}*\n\nВыбери ситуацию:",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )

async def cb_phrase_sit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    sit_idx = int(query.data.replace("ph_sit_", ""))
    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    sit = level['phrases'][sit_idx]

    text = f"{sit['icon']} *{sit['situation']}*\n\n"
    for item in sit['items']:
        text += f"🇬🇧 *{item['en']}*\n"
        text += f"🇷🇺 {item['ru']}\n"
        if item.get('note'):
            text += f"📌 _{item['note']}_\n"
        text += "\n"

    if len(text) > 4000:
        text = text[:4000] + "\n\n_...сокращено_"

    keyboard = [
        [InlineKeyboardButton("◀️ К ситуациям", callback_data="sec_phrases")],
        [InlineKeyboardButton("🏠 Главное меню", callback_data="back_levels")],
    ]

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))

    app.add_handler(CallbackQueryHandler(cb_level, pattern=r"^level_"))
    app.add_handler(CallbackQueryHandler(cb_back_levels, pattern=r"^back_levels$"))
    app.add_handler(CallbackQueryHandler(cb_back_section, pattern=r"^back_section$"))

    app.add_handler(CallbackQueryHandler(cb_sec_grammar, pattern=r"^sec_grammar$"))
    app.add_handler(CallbackQueryHandler(cb_grammar_topic, pattern=r"^g_topic_"))
    app.add_handler(CallbackQueryHandler(cb_grammar_exercise, pattern=r"^g_ex_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_exercise_answer, pattern=r"^g_ex_ans_"))
    app.add_handler(CallbackQueryHandler(cb_grammar_test, pattern=r"^g_test_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_test_answer, pattern=r"^g_test_ans_"))

    app.add_handler(CallbackQueryHandler(cb_sec_vocab, pattern=r"^sec_vocab$"))
    app.add_handler(CallbackQueryHandler(cb_vocab_cat, pattern=r"^v_cat_"))
    app.add_handler(CallbackQueryHandler(cb_vocab_next, pattern=r"^v_next_"))

    app.add_handler(CallbackQueryHandler(cb_sec_phrases, pattern=r"^sec_phrases$"))
    app.add_handler(CallbackQueryHandler(cb_phrase_sit, pattern=r"^ph_sit_"))

    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
