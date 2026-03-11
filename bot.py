import logging
import sys
import os
import asyncio

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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

APP_NAME = "🎯 LinguaStep — Умный помощник в изучении английского"
APP_DESCRIPTION = (
    "Привет! 👋 Я *LinguaStep* — твой персональный тренер по английскому языку.\n\n"
    "📚 Что умею:\n"
    "• Объяснять грамматику понятным языком\n"
    "• Давать 10 упражнений по каждой теме\n"
    "• Проверять знания через 15-вопросный тест\n"
    "• Учить слова по категориям\n"
    "• Показывать полезные фразы по ситуациям\n"
    "• Следить за твоим прогрессом\n\n"
    "🎯 Уровни: A1 → A2 → B1 → B2 → C1 → C2\n\n"
    "Нажми кнопку ниже, чтобы начать учёбу! 👇"
)

LEVELS = [A1, A2, B1, B2, C1, C2]
LEVEL_KEYS = ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']


def get_level(key):
    mapping = dict(zip(LEVEL_KEYS, LEVELS))
    return mapping.get(key, A1)


def build_markup(buttons):
    return InlineKeyboardMarkup(buttons)


def get_progress(context, level_key):
    """Возвращает словарь прогресса пользователя по уровню."""
    progress = context.user_data.setdefault('progress', {})
    return progress.setdefault(level_key, {
        'grammar_done': [],    # список id завершённых тем грамматики
        'grammar_tested': [],  # список id тем, по которым пройден тест
        'vocab_done': [],      # список idx категорий словаря
        'phrases_done': [],    # список idx ситуаций фраз
    })


def progress_bar(done, total, length=10):
    filled = int(length * done / total) if total else 0
    bar = "█" * filled + "░" * (length - filled)
    pct = int(100 * done / total) if total else 0
    return f"[{bar}] {pct}%"


# ──────────────────────────────────────────────
# START
# ──────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    keyboard = [
        [InlineKeyboardButton("🚀 Начать обучение", callback_data="begin")],
        [InlineKeyboardButton("🌐 Открыть веб-версию", url="https://ismail-py59.onrender.com")],
    ]
    text = APP_DESCRIPTION
    markup = build_markup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=markup, parse_mode="Markdown")
    else:
        await update.callback_query.edit_message_text(text, reply_markup=markup, parse_mode="Markdown")


# ──────────────────────────────────────────────
# BEGIN — выбор уровня
# ──────────────────────────────────────────────

async def cb_begin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

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

    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back_home")])

    text = (
        "📊 *Выбери свой уровень английского:*\n\n"
        "🌱 *A1* — Начинающий (нулевые знания)\n"
        "🌿 *A2* — Элементарный (знаешь основы)\n"
        "🌳 *B1* — Средний (можешь общаться)\n"
        "🌲 *B2* — Выше среднего (свободное общение)\n"
        "⭐ *C1* — Продвинутый (почти как носитель)\n"
        "🏆 *C2* — Совершенный (уровень носителя)"
    )

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# УРОВЕНЬ — главное меню уровня
# ──────────────────────────────────────────────

async def cb_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = query.data.replace("level_", "")
    context.user_data['level'] = level_key
    level = get_level(level_key)

    prog = get_progress(context, level_key)
    total_grammar = len(level['grammar'])
    done_grammar = len(prog['grammar_done'])
    tested_grammar = len(prog['grammar_tested'])

    keyboard = [
        [InlineKeyboardButton("📚 Грамматика", callback_data="sec_grammar")],
        [InlineKeyboardButton("📖 Словарный запас", callback_data="sec_vocab")],
        [InlineKeyboardButton("💬 Разговорные фразы", callback_data="sec_phrases")],
        [InlineKeyboardButton("📊 Мой прогресс", callback_data="my_progress")],
        [InlineKeyboardButton("◀️ К уровням", callback_data="begin")],
    ]

    text = (
        f"{level['emoji']} *{level['name']}*\n\n"
        f"{level['description']}\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📈 *Твой прогресс:*\n"
        f"📚 Грамматика: {done_grammar}/{total_grammar} тем изучено\n"
        f"   {progress_bar(done_grammar, total_grammar)}\n"
        f"🧪 Тестов пройдено: {tested_grammar}/{total_grammar}\n"
        f"   {progress_bar(tested_grammar, total_grammar)}"
    )

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# МОЙ ПРОГРЕСС
# ──────────────────────────────────────────────

async def cb_my_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    prog = get_progress(context, level_key)

    total_g = len(level['grammar'])
    done_g = len(prog['grammar_done'])
    tested_g = len(prog['grammar_tested'])
    total_v = len(level['vocabulary'])
    done_v = len(prog['vocab_done'])
    total_ph = len(level['phrases'])
    done_ph = len(prog['phrases_done'])

    # Список пройденных тем
    done_topics = []
    for i, topic in enumerate(level['grammar']):
        status = ""
        if topic['id'] in prog['grammar_tested']:
            status = "✅ (тест пройден)"
        elif topic['id'] in prog['grammar_done']:
            status = "📖 (изучено)"
        else:
            status = "⬜ (не начато)"
        done_topics.append(f"  {topic['icon']} {topic['title']} — {status}")

    topics_text = "\n".join(done_topics) if done_topics else "  Нет данных"

    keyboard = [
        [InlineKeyboardButton("◀️ Назад к разделам", callback_data=f"level_{level_key}")],
    ]

    text = (
        f"📊 *Прогресс — {level['name']}*\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📚 *Грамматика:*\n"
        f"Изучено: {done_g}/{total_g} {progress_bar(done_g, total_g)}\n"
        f"Тестов: {tested_g}/{total_g} {progress_bar(tested_g, total_g)}\n\n"
        f"📖 *Словарь:*\n"
        f"Категорий: {done_v}/{total_v} {progress_bar(done_v, total_v)}\n\n"
        f"💬 *Фразы:*\n"
        f"Ситуаций: {done_ph}/{total_ph} {progress_bar(done_ph, total_ph)}\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📋 *Темы грамматики:*\n{topics_text}"
    )

    if len(text) > 4000:
        text = text[:4000] + "\n\n_...сокращено_"

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# НАВИГАЦИЯ
# ──────────────────────────────────────────────

async def cb_back_home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(update, context)


async def cb_back_levels(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await cb_begin(update, context)


async def cb_back_section(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    level_key = context.user_data.get('level', 'a1')
    # Simulate level callback
    query.data = f"level_{level_key}"
    await cb_level(update, context)


# ──────────────────────────────────────────────
# ГРАММАТИКА — список тем
# ──────────────────────────────────────────────

async def cb_sec_grammar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    topics = level['grammar']
    prog = get_progress(context, level_key)

    keyboard = []
    for i, topic in enumerate(topics):
        if topic['id'] in prog['grammar_tested']:
            status_icon = "✅"
        elif topic['id'] in prog['grammar_done']:
            status_icon = "📖"
        else:
            status_icon = "⬜"
        keyboard.append([InlineKeyboardButton(
            f"{status_icon} {topic['icon']} {topic['title']}",
            callback_data=f"g_topic_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data=f"level_{level_key}")])

    total = len(topics)
    done = len(prog['grammar_done'])

    await query.edit_message_text(
        f"📚 *Грамматика — {level['name']}*\n\n"
        f"Прогресс: {done}/{total} тем {progress_bar(done, total)}\n\n"
        f"✅ — тест пройден  📖 — изучено  ⬜ — не начато\n\n"
        f"Выбери тему:",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )


# ──────────────────────────────────────────────
# ГРАММАТИКА — объяснение темы
# ──────────────────────────────────────────────

async def cb_grammar_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    topic_idx = int(query.data.replace("g_topic_", ""))
    context.user_data['g_topic'] = topic_idx

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]

    # Отмечаем тему как изученную
    prog = get_progress(context, level_key)
    if topic['id'] not in prog['grammar_done']:
        prog['grammar_done'].append(topic['id'])

    total_ex = len(topic['exercises'])
    total_test = len(topic['test'])

    keyboard = [
        [InlineKeyboardButton(f"✏️ Упражнения ({total_ex} шт.)", callback_data="g_ex_menu")],
        [InlineKeyboardButton(f"🧪 Тест ({total_test} вопросов)", callback_data="g_test_0")],
        [InlineKeyboardButton("🔄 Повторить тему", callback_data=f"g_topic_{topic_idx}")],
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


# ──────────────────────────────────────────────
# УПРАЖНЕНИЯ — меню
# ──────────────────────────────────────────────

async def cb_grammar_exercise_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    topic_idx = context.user_data.get('g_topic', 0)
    level = get_level(level_key)
    topic = level['grammar'][topic_idx]
    total_ex = len(topic['exercises'])

    keyboard = [
        [InlineKeyboardButton("✏️ Начать упражнения", callback_data="g_ex_0")],
        [InlineKeyboardButton("⏭️ Пропустить → к тесту", callback_data="g_test_0")],
        [InlineKeyboardButton("◀️ К теме", callback_data=f"g_topic_{topic_idx}")],
    ]

    await query.edit_message_text(
        f"✏️ *Упражнения — {topic['title']}*\n\n"
        f"Здесь *{total_ex} упражнений* для закрепления темы.\n\n"
        f"💡 *Совет:* Попробуй сначала решить их в тетради, а потом проверь ответы здесь.\n\n"
        f"Что хочешь сделать?",
        reply_markup=build_markup(keyboard),
        parse_mode="Markdown"
    )


# ──────────────────────────────────────────────
# УПРАЖНЕНИЯ — вопрос
# ──────────────────────────────────────────────

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
        pct = int(correct / total * 100) if total else 0
        if pct == 100:
            emoji = "🌟"
            msg = "Идеально! Все верно!"
        elif pct >= 70:
            emoji = "👍"
            msg = "Отлично! Переходи к тесту!"
        else:
            emoji = "📚"
            msg = "Советую повторить тему и попробовать ещё раз."

        keyboard = [
            [InlineKeyboardButton("🧪 Перейти к тесту (15 вопросов)", callback_data="g_test_0")],
            [InlineKeyboardButton("🔄 Повторить упражнения", callback_data="g_ex_0")],
            [InlineKeyboardButton("📖 Повторить объяснение", callback_data=f"g_topic_{topic_idx}")],
            [InlineKeyboardButton("◀️ К темам", callback_data="sec_grammar")],
        ]
        await query.edit_message_text(
            f"{emoji} *Упражнения завершены!*\n\n"
            f"Результат: *{correct}/{total}* ({pct}%)\n"
            f"{progress_bar(correct, total)}\n\n"
            f"{msg}",
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

    progress = progress_bar(ex_idx, len(exercises))

    await query.edit_message_text(
        f"✏️ *Упражнение {ex_idx + 1}/{len(exercises)}*\n"
        f"{progress}\n\n"
        f"📝 {ex['q']}",
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
    label = "➡️ Следующее" if next_idx < total else "🏁 Завершить упражнения"
    keyboard = [[InlineKeyboardButton(label, callback_data=f"g_ex_{next_idx}")]]

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# ТЕСТ
# ──────────────────────────────────────────────

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
            grade = "🌟 Отлично! Тема освоена!"
            grade_note = "Можно переходить к следующей теме!"
        elif pct >= 60:
            grade = "👍 Хорошо!"
            grade_note = "Советую ещё раз повторить объяснение."
        else:
            grade = "📚 Нужно повторить"
            grade_note = "Перечитай объяснение и пройди упражнения снова."

        # Отмечаем тест как пройденный если >= 60%
        prog = get_progress(context, level_key)
        if pct >= 60 and topic['id'] not in prog['grammar_tested']:
            prog['grammar_tested'].append(topic['id'])

        keyboard = [
            [InlineKeyboardButton("🔄 Пройти тест снова", callback_data="g_test_0")],
            [InlineKeyboardButton("📖 Повторить объяснение", callback_data=f"g_topic_{topic_idx}")],
            [InlineKeyboardButton("✏️ Повторить упражнения", callback_data="g_ex_0")],
            [InlineKeyboardButton("◀️ К темам", callback_data="sec_grammar")],
            [InlineKeyboardButton("📊 Мой прогресс", callback_data="my_progress")],
        ]
        await query.edit_message_text(
            f"🧪 *Тест завершён!*\n\n"
            f"Тема: *{topic['title']}*\n"
            f"Результат: *{correct}/{total}* ({pct}%)\n"
            f"{progress_bar(correct, total)}\n\n"
            f"{grade}\n"
            f"_{grade_note}_",
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

    progress = progress_bar(test_idx, len(tests))

    await query.edit_message_text(
        f"🧪 *Тест {test_idx + 1}/{len(tests)}*\n"
        f"{progress}\n\n"
        f"❓ {t['q']}",
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
    label = "➡️ Следующий" if next_idx < total else "🏁 Результат теста"
    keyboard = [[InlineKeyboardButton(label, callback_data=f"g_test_{next_idx}")]]

    if correct:
        text = "✅ *Правильно!*"
    else:
        text = f"❌ *Неправильно*\n\nПравильный ответ: *{t['o'][t['a']]}*"

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# СЛОВАРЬ
# ──────────────────────────────────────────────

async def cb_sec_vocab(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    cats = level['vocabulary']
    prog = get_progress(context, level_key)

    keyboard = []
    for i, cat in enumerate(cats):
        status = "✅" if i in prog['vocab_done'] else "⬜"
        total_words = len(cat['words'])
        keyboard.append([InlineKeyboardButton(
            f"{status} {cat['icon']} {cat['category']} ({total_words} слов)",
            callback_data=f"v_cat_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data=f"level_{level_key}")])

    done_cats = len(prog['vocab_done'])
    total_cats = len(cats)
    total_words_all = sum(len(c['words']) for c in cats)

    await query.edit_message_text(
        f"📖 *Словарный запас — {level['name']}*\n\n"
        f"Всего слов в уровне: *{total_words_all}*\n"
        f"Категорий пройдено: {done_cats}/{total_cats} {progress_bar(done_cats, total_cats)}\n\n"
        f"✅ — пройдено  ⬜ — не начато\n\n"
        f"Выбери категорию:",
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
        prog = get_progress(context, level_key)
        if cat_idx not in prog['vocab_done']:
            prog['vocab_done'].append(cat_idx)

        keyboard = [
            [InlineKeyboardButton("🔄 Повторить категорию", callback_data=f"v_cat_{cat_idx}")],
            [InlineKeyboardButton("◀️ К категориям", callback_data="sec_vocab")],
        ]
        await query.edit_message_text(
            f"✅ *Категория завершена!*\n\n"
            f"🎉 Ты изучил все *{len(words)}* слов в «{cat['category']}»!\n\n"
            f"Хочешь повторить или перейти к другой категории?",
            reply_markup=build_markup(keyboard),
            parse_mode="Markdown"
        )
        return

    word = words[word_idx]
    progress = f"{word_idx + 1}/{len(words)}"
    bar = progress_bar(word_idx + 1, len(words))

    keyboard = [
        [InlineKeyboardButton(
            "➡️ Следующее слово" if word_idx + 1 < len(words) else "✅ Завершить категорию",
            callback_data=f"v_next_{word_idx + 1}"
        )],
        [InlineKeyboardButton("◀️ К категориям", callback_data="sec_vocab")],
    ]

    text = (
        f"📖 *{cat['icon']} {cat['category']}*\n"
        f"Слово {progress} {bar}\n\n"
        f"🇬🇧 *{word['en']}*\n"
        f"🇷🇺 {word['ru']}\n\n"
        f"💬 _{word.get('ex', '')}_"
    )

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# ФРАЗЫ
# ──────────────────────────────────────────────

async def cb_sec_phrases(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    level_key = context.user_data.get('level', 'a1')
    level = get_level(level_key)
    phrases = level['phrases']
    prog = get_progress(context, level_key)

    keyboard = []
    for i, sit in enumerate(phrases):
        status = "✅" if i in prog['phrases_done'] else "⬜"
        total_ph = len(sit['items'])
        keyboard.append([InlineKeyboardButton(
            f"{status} {sit['icon']} {sit['situation']} ({total_ph} фраз)",
            callback_data=f"ph_sit_{i}"
        )])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data=f"level_{level_key}")])

    done_ph = len(prog['phrases_done'])
    total_ph = len(phrases)
    total_items = sum(len(s['items']) for s in phrases)

    await query.edit_message_text(
        f"💬 *Разговорные фразы — {level['name']}*\n\n"
        f"Всего фраз в уровне: *{total_items}*\n"
        f"Ситуаций пройдено: {done_ph}/{total_ph} {progress_bar(done_ph, total_ph)}\n\n"
        f"Выбери ситуацию:",
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

    # Отмечаем как просмотренное
    prog = get_progress(context, level_key)
    if sit_idx not in prog['phrases_done']:
        prog['phrases_done'].append(sit_idx)

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
        [InlineKeyboardButton("🔄 Повторить", callback_data=f"ph_sit_{sit_idx}")],
        [InlineKeyboardButton("◀️ К ситуациям", callback_data="sec_phrases")],
        [InlineKeyboardButton("📊 Мой прогресс", callback_data="my_progress")],
    ]

    await query.edit_message_text(text, reply_markup=build_markup(keyboard), parse_mode="Markdown")


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))

    # Навигация
    app.add_handler(CallbackQueryHandler(cb_begin, pattern=r"^begin$"))
    app.add_handler(CallbackQueryHandler(cb_back_home, pattern=r"^back_home$"))
    app.add_handler(CallbackQueryHandler(cb_back_levels, pattern=r"^back_levels$"))
    app.add_handler(CallbackQueryHandler(cb_back_section, pattern=r"^back_section$"))

    # Уровни
    app.add_handler(CallbackQueryHandler(cb_level, pattern=r"^level_"))
    app.add_handler(CallbackQueryHandler(cb_my_progress, pattern=r"^my_progress$"))

    # Грамматика
    app.add_handler(CallbackQueryHandler(cb_sec_grammar, pattern=r"^sec_grammar$"))
    app.add_handler(CallbackQueryHandler(cb_grammar_topic, pattern=r"^g_topic_"))
    app.add_handler(CallbackQueryHandler(cb_grammar_exercise_menu, pattern=r"^g_ex_menu$"))
    app.add_handler(CallbackQueryHandler(cb_grammar_exercise, pattern=r"^g_ex_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_exercise_answer, pattern=r"^g_ex_ans_"))
    app.add_handler(CallbackQueryHandler(cb_grammar_test, pattern=r"^g_test_\d+$"))
    app.add_handler(CallbackQueryHandler(cb_test_answer, pattern=r"^g_test_ans_"))

    # Словарь
    app.add_handler(CallbackQueryHandler(cb_sec_vocab, pattern=r"^sec_vocab$"))
    app.add_handler(CallbackQueryHandler(cb_vocab_cat, pattern=r"^v_cat_"))
    app.add_handler(CallbackQueryHandler(cb_vocab_next, pattern=r"^v_next_"))

    # Фразы
    app.add_handler(CallbackQueryHandler(cb_sec_phrases, pattern=r"^sec_phrases$"))
    app.add_handler(CallbackQueryHandler(cb_phrase_sit, pattern=r"^ph_sit_"))

    print("✅ LinguaStep Bot запущен!")
    app.run_polling(drop_pending_updates=True, stop_signals=[])


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    main()
