B1 = {
    'name': 'B1 — Средний',
    'emoji': '🌳',
    'description': (
        '🌳 *Уровень B1 — Средний*\n\n'
        'Ты уже знаешь основы и можешь общаться на простые темы!\n'
        'На этом уровне ты научишься:\n'
        '• Говорить о прошлом опыте (Present Perfect)\n'
        '• Строить условные предложения\n'
        '• Использовать страдательный залог\n'
        '• Выражать советы и обязанности\n'
        '• Пересказывать чужие слова\n\n'
        'Выбери раздел для изучения:'
    ),
    'grammar': [
        {
            'id': 'b1_g1',
            'title': 'Present Perfect',
            'icon': '✅',
            'explanation': (
                '📌 *Present Perfect — Настоящее совершённое*\n\n'
                'Связывает прошлое с настоящим — действие произошло в прошлом, но важен его результат СЕЙЧАС.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'have/has + *Past Participle* (3-я форма глагола)\n\n'
                '✅ *Когда использовать:*\n'
                '1. Опыт (случалось ли когда-нибудь?):\n'
                '   Have you ever *been* to France?\n'
                '2. Свежий результат:\n'
                '   I\'ve *lost* my keys. (И сейчас нет ключей!)\n'
                '3. С just/already/yet:\n'
                '   She has *just* left.\n'
                '   I\'ve *already* eaten.\n'
                '   Has he arrived *yet*?\n'
                '4. With for/since:\n'
                '   I\'ve lived here *for* 5 years.\n'
                '   We\'ve known each other *since* 2018.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I *haven\'t* seen that film.\n'
                '• She *hasn\'t* called me.\n\n'
                '❓ *Вопрос:*\n'
                '• *Have* you *finished*?\n'
                '• *Has* she *eaten*?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Present Perfect vs Past Simple:*\n'
                '• I\'ve *lost* my keys. (сейчас нет → Present Perfect)\n'
                '• I *lost* my keys yesterday. (вчера → Past Simple)\n'
                '• Have you ever *been* to Japan? (опыт → PP)\n'
                '• I *went* to Japan in 2019. (конкретное время → PS)'
            ),
            'exercises': [
                {'q': 'She ___ (finish) the project.', 'o': ['finish', 'finished', 'has finished', 'have finished'], 'a': 2, 'e': 'She + has + finished (3-я форма).'},
                {'q': 'I ___ (never/be) to Australia.', 'o': ["haven't never been", "have never been", "never have been", "has never been"], 'a': 1, 'e': 'I + have never been.'},
                {'q': 'Have you ___ (see) this film?', 'o': ['saw', 'seen', 'seed', 'see'], 'a': 1, 'e': 'Have + seen (3-я форма от see).'},
                {'q': 'She has ___ (just/leave).', 'o': ['left just', 'just leaved', 'just left', 'left already'], 'a': 2, 'e': 'has just left (just стоит перед глаголом).'},
                {'q': 'I ___ (live) here for 10 years.', 'o': ['live', 'lived', 'have lived', 'has lived'], 'a': 2, 'e': 'For + период → Present Perfect: have lived.'},
                {'q': 'Has he arrived ___?', 'o': ['already', 'still', 'yet', 'just'], 'a': 2, 'e': 'Yet — в вопросах и отрицаниях (в конце предложения).'},
                {'q': 'I ___ (already/eat) lunch.', 'o': ["have already eaten", "have already ate", "already have eaten", "has already eaten"], 'a': 0, 'e': "have already eaten (already + 3-я форма)."},
                {'q': 'Правильное предложение (Present Perfect):', 'o': ["I've saw her.", "I've seen her.", "I've see her.", "I've seed her."], 'a': 1, 'e': "see → seen (3-я форма). I've seen her."},
                {'q': 'We ___ (know) each other since 2015.', 'o': ["knew", "have known", "know", "has known"], 'a': 1, 'e': "Since → Present Perfect: have known."},
                {'q': 'Выбери правильное время:', 'o': ["I've lost my phone yesterday.", "I lost my phone yesterday.", "I have lose my phone yesterday.", "I lose my phone yesterday."], 'a': 1, 'e': "Yesterday — конкретное время → Past Simple: lost."},
            ],
            'test': [
                {'q': 'He ___ (finish) his homework.', 'o': ['finish', 'finished', 'has finished', 'have finished'], 'a': 2},
                {'q': '___ you ever (try) sushi?', 'o': ['Did', 'Have', 'Do', 'Are'], 'a': 1},
                {'q': 'I ___ (just/call) him.', 'o': ['have just called', 'just have called', 'has just called', 'called just'], 'a': 0},
                {'q': 'She ___ (never/meet) him.', 'o': ["has never met", "have never met", "never has met", "never met"], 'a': 0},
                {'q': 'We ___ (live) here for 3 years.', 'o': ["live", "lived", "have lived", "has lived"], 'a': 2},
                {'q': 'go → Past Participle:', 'o': ['goed', 'went', 'gone', 'going'], 'a': 2},
                {'q': 'I ___ (not/see) that film yet.', 'o': ["haven't seen", "didn't see", "don't see", "hasn't seen"], 'a': 0},
                {'q': 'She has ___ (already/finish).', 'o': ['already finished', 'finished already', 'already finish', 'already finishing'], 'a': 0},
                {'q': 'Has she ___ (write) the report?', 'o': ['wrote', 'written', 'write', 'writing'], 'a': 1},
                {'q': 'Правильное использование PP:', 'o': ["I've been to Paris in 2019.", "I went to Paris in 2019.", "I have went to Paris in 2019.", "I been to Paris in 2019."], 'a': 1},
                {'q': 'They ___ (work) together since 2020.', 'o': ["worked", "work", "have worked", "has worked"], 'a': 2},
                {'q': 'eat → Past Participle:', 'o': ['ate', 'eated', 'eaten', 'eating'], 'a': 2},
                {'q': 'Have you ___ (speak) to him yet?', 'o': ['spoken', 'spoke', 'speak', 'speaking'], 'a': 0},
                {'q': 'He ___ (not/come) home yet.', 'o': ["hasn't come", "didn't come", "don't come", "haven't come"], 'a': 0},
                {'q': 'I ___ (know) her for many years.', 'o': ["know", "knew", "have known", "has known"], 'a': 2},
            ]
        },
        {
            'id': 'b1_g2',
            'title': 'Past Continuous',
            'icon': '⏳',
            'explanation': (
                '📌 *Past Continuous — Прошедшее продолженное*\n\n'
                'Описывает действие, которое было В ПРОЦЕССЕ в определённый момент в прошлом.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'was/were + глагол + *-ING*\n\n'
                '✅ *Когда использовать:*\n\n'
                '1. Действие в процессе в прошлом:\n'
                '   At 8pm yesterday, I *was studying*.\n'
                '   (В 8 вечера я учился — был в процессе)\n\n'
                '2. Фоновое действие + прерывающее:\n'
                '   I *was watching* TV when he *called*.\n'
                '   (Смотрел — Past Cont.; позвонил — Past Simple)\n\n'
                '3. Параллельные действия:\n'
                '   While she *was cooking*, he *was watching* TV.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I *was not* (wasn\'t) sleeping.\n'
                '• They *were not* (weren\'t) working.\n\n'
                '❓ *Вопрос:*\n'
                '• *Was* she sleeping?\n'
                '• *Were* they playing?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Ключевые слова:*\n'
                'while, when, at (time), all day/morning'
            ),
            'exercises': [
                {'q': 'At 9pm, she ___ (watch) TV.', 'o': ['watched', 'was watching', 'were watching', 'is watching'], 'a': 1, 'e': 'She + was + watching.'},
                {'q': 'I ___ (sleep) when the phone rang.', 'o': ['slept', 'was sleeping', 'were sleeping', 'am sleeping'], 'a': 1, 'e': 'Фоновое действие → was sleeping.'},
                {'q': 'While they ___ (play), it started to rain.', 'o': ['played', 'were playing', 'was playing', 'are playing'], 'a': 1, 'e': 'They + were + playing.'},
                {'q': '___ you working at 6pm yesterday?', 'o': ['Did', 'Were', 'Was', 'Have'], 'a': 1, 'e': 'You → Were you...?'},
                {'q': 'He ___ (not/study) when I called.', 'o': ["didn't study", "wasn't studying", "weren't studying", "not studying"], 'a': 1, 'e': "wasn't studying (was not + -ing)."},
                {'q': 'What ___ you (do) at midnight?', 'o': ['did', 'were', 'was', 'have'], 'a': 1, 'e': 'What were you doing?'},
                {'q': 'I fell while I ___ (run).', 'o': ['ran', 'was running', 'were running', 'run'], 'a': 1, 'e': 'Фоновое действие → was running.'},
                {'q': 'We ___ (have) lunch when he arrived.', 'o': ['had', 'were having', 'was having', 'have had'], 'a': 1, 'e': 'We + were having.'},
                {'q': 'She ___ (work) all day yesterday.', 'o': ['worked', 'was working', 'were working', 'has worked'], 'a': 1, 'e': 'All day → was working.'},
                {'q': 'Правильное предложение:', 'o': ['He were sleeping.', 'He was sleeping.', 'He was slept.', 'He were sleep.'], 'a': 1, 'e': 'He + was (единственное число) + sleeping.'},
            ],
            'test': [
                {'q': 'At 7am, he ___ (have) breakfast.', 'o': ['had', 'was having', 'were having', 'has had'], 'a': 1},
                {'q': 'They ___ (play) football when it rained.', 'o': ['played', 'were playing', 'was playing', 'are playing'], 'a': 1},
                {'q': '___ she working when you called?', 'o': ['Did', 'Was', 'Were', 'Has'], 'a': 1},
                {'q': 'While I ___ (read), she watched TV.', 'o': ['read', 'was reading', 'were reading', 'reads'], 'a': 1},
                {'q': 'He ___ (not/listen) when she spoke.', 'o': ["didn't listen", "wasn't listening", "weren't listening", "not listened"], 'a': 1},
                {'q': 'I ___ (study) all evening.', 'o': ['studied', 'was studying', 'were studying', 'study'], 'a': 1},
                {'q': 'What ___ you doing at 10pm?', 'o': ['did', 'were', 'was', 'have'], 'a': 1},
                {'q': 'She ___ (write) a letter when he came.', 'o': ['wrote', 'was writing', 'were writing', 'written'], 'a': 1},
                {'q': 'We ___ (wait) for an hour!', 'o': ['waited', 'were waiting', 'was waiting', 'have waited'], 'a': 1},
                {'q': 'He slipped while he ___ (walk).', 'o': ['walked', 'was walking', 'were walking', 'walk'], 'a': 1},
                {'q': '___ they sleeping when you arrived?', 'o': ['Did', 'Was', 'Were', 'Have'], 'a': 2},
                {'q': 'I ___ (not/work) when she called.', 'o': ["didn't work", "wasn't working", "weren't working", "not working"], 'a': 1},
                {'q': 'At 3pm, she ___ (sit) in a café.', 'o': ['sat', 'was sitting', 'were sitting', 'sitted'], 'a': 1},
                {'q': 'While he ___ (drive), his phone rang.', 'o': ['drove', 'was driving', 'were driving', 'driven'], 'a': 1},
                {'q': 'Маркер Past Continuous:', 'o': ['yesterday', 'last year', 'at 5pm yesterday', 'every day'], 'a': 2},
            ]
        },
        {
            'id': 'b1_g3',
            'title': 'Future Simple (will)',
            'icon': '🔭',
            'explanation': (
                '📌 *Future Simple — Будущее время с WILL*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Когда использовать WILL:*\n\n'
                '1. Спонтанное решение (принятое прямо сейчас):\n'
                '   "There\'s no milk." — "I *\'ll* buy some."\n\n'
                '2. Предсказание (мнение, не факт):\n'
                '   I think it *will* rain tomorrow.\n'
                '   She *will* probably be late.\n\n'
                '3. Обещания:\n'
                '   I *\'ll* help you, I promise.\n\n'
                '4. Просьбы:\n'
                '   *Will* you open the window?\n\n'
                '5. Предложения:\n'
                '   *Shall* I help you? (брит. Eng.)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'will + глагол (base form)\n\n'
                '✅ I *will* go. / I *\'ll* go.\n'
                '❌ I *will not* go. / I *won\'t* go.\n'
                '❓ *Will* you go?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Will vs Going to:*\n'
                '• I *\'m going to* buy a car. (уже есть план)\n'
                '• I *\'ll* buy a car. (спонтанное решение)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⏰ *Маркеры:*\n'
                'tomorrow, next week/year, in 2030,\n'
                'probably, I think, I\'m sure, maybe'
            ),
            'exercises': [
                {'q': '"There is no coffee." "I ___ (make) some."', 'o': ["'m going to make", "'ll make", "'m making", 'will to make'], 'a': 1, 'e': 'Спонтанное решение → will: I\'ll make.'},
                {'q': 'I think she ___ (pass) the exam.', 'o': ["'s going to pass", "'ll pass", "is passing", "will to pass"], 'a': 1, 'e': "Предсказание-мнение → I think she'll pass."},
                {'q': 'I ___ (not/tell) anyone, I promise.', 'o': ["won't tell", "wouldn't tell", "am not going to tell", "don't tell"], 'a': 0, 'e': "Обещание → won't tell."},
                {'q': '___ you help me with this?', 'o': ['Are', 'Do', 'Will', 'Have'], 'a': 2, 'e': 'Will you...? — просьба.'},
                {'q': 'It ___ (probably/be) cold tomorrow.', 'o': ["will probably be", "probably will be", "is probably going to be", "probably be"], 'a': 0, 'e': "Will + probably → will probably be."},
                {'q': 'Разница: "I\'ll call him" vs "I\'m going to call him":', 'o': ['Нет разницы', "Will — спонтанно, Going to — уже есть план", "Going to — спонтанно, Will — план", "Will всегда более вежливо"], 'a': 1, 'e': "Will = спонтанно, Going to = план есть."},
                {'q': 'She ___ (not/come) to the party.', 'o': ["won't come", "will not to come", "doesn't will come", "isn't going come"], 'a': 0, 'e': "won't come (will not)."},
                {'q': '"Phone is ringing" → I ___ (answer) it!', 'o': ["'m going to answer", "'ll answer", "am answering", "was answering"], 'a': 1, 'e': "Спонтанно → I'll answer it!"},
                {'q': 'I\'m sure they ___ (love) it.', 'o': ["are going to love", "will love", "love", "would love"], 'a': 1, 'e': "Уверенное предсказание → will love."},
                {'q': 'Маркер Future Simple:', 'o': ['yesterday', 'at 5pm yesterday', 'next year', 'at the moment'], 'a': 2, 'e': 'Next year — маркер будущего.'},
            ],
            'test': [
                {'q': '"I\'m thirsty." "I ___ get you some water."', 'o': ["'m going to", "'ll", "am", "go to"], 'a': 1},
                {'q': 'It ___ (probably/snow) tonight.', 'o': ["will probably snow", "probably will snow", "is snowing probably", "snow probably"], 'a': 0},
                {'q': '___ you be at home tomorrow?', 'o': ['Are', 'Do', 'Will', 'Have'], 'a': 2},
                {'q': 'I ___ (not/forget) your birthday.', 'o': ["won't forget", "don't forget", "am not forgetting", "will not to forget"], 'a': 0},
                {'q': 'She ___ (probably/be) late.', 'o': ["will probably be", "probably will be", "is probably be", "probably is"], 'a': 0},
                {'q': '"Lights are off." → I ___ (turn) them on.', 'o': ["'m going to turn", "'ll turn", "am turning", "turn"], 'a': 1},
                {'q': 'I think the economy ___ (improve) next year.', 'o': ["improves", "will improve", "is improving", "improved"], 'a': 1},
                {'q': 'He ___ (never/forget) this day.', 'o': ["will never forget", "never will forget", "won't never forget", "never forgets"], 'a': 0},
                {'q': '___ you close the door, please?', 'o': ['Are', 'Do', 'Will', 'Shall'], 'a': 2},
                {'q': 'Maybe they ___ come.', 'o': ["will come", "are coming", "come", "came"], 'a': 0},
                {'q': 'I promise I ___ call you tomorrow.', 'o': ["will call", "am calling", "call", "called"], 'a': 0},
                {'q': 'Маркер с Will:', 'o': ['last night', 'every day', 'in 5 years', 'at the moment'], 'a': 2},
                {'q': 'She ___ (not/tell) anyone.', 'o': ["won't tell", "doesn't tell", "isn't telling", "will not to tell"], 'a': 0},
                {'q': 'I think he ___ win.', 'o': ["will win", "is winning", "wins", "won"], 'a': 0},
                {'q': '"I can help." vs "I will help.":', 'o': ['Can = умею, Will = обещаю', 'Нет разницы', 'Will = прошлое, Can = настоящее', 'Can = будущее, Will = умение'], 'a': 0},
            ]
        },
        {
            'id': 'b1_g4',
            'title': 'First Conditional — первый тип условных',
            'icon': '⚡',
            'explanation': (
                '📌 *First Conditional (1-й тип условных предложений)*\n\n'
                'Реальное условие в настоящем/будущем — возможная, реальная ситуация.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Структура:*\n'
                '*IF + Present Simple, will + глагол*\n\n'
                '✅ *Примеры:*\n'
                '• If it *rains*, I *\'ll* take an umbrella.\n'
                '  (Если будет дождь — возьму зонт. Реально!)\n'
                '• If she *studies* hard, she *will pass* the exam.\n'
                '• If you *hurry*, you *won\'t* be late.\n'
                '• *Will* you call me if you *need* help?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Важные правила:*\n\n'
                '1. В придаточном с IF — Present Simple (НЕ will!):\n'
                '   ✅ If it *rains*...\n'
                '   ❌ If it *will rain*...\n\n'
                '2. Порядок частей можно менять:\n'
                '   If it rains, I\'ll stay home.\n'
                '   = I\'ll stay home *if* it rains.\n'
                '   (запятая только когда IF в начале!)\n\n'
                '3. Можно использовать другие модальные:\n'
                '   If you\'re tired, you *can* rest.\n'
                '   If she calls, *tell* her I\'m busy. (imperative)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Unless = If...not:*\n'
                '• *Unless* you hurry, you\'ll be late.\n'
                '= *If* you *don\'t* hurry, you\'ll be late.'
            ),
            'exercises': [
                {'q': 'If it ___ (rain), we\'ll cancel the trip.', 'o': ['will rain', 'rains', 'rained', 'is raining'], 'a': 1, 'e': 'В IF-придаточном — Present Simple: rains.'},
                {'q': 'If you study, you ___ (pass) the test.', 'o': ['pass', 'will pass', 'would pass', 'passed'], 'a': 1, 'e': 'В главном предложении → will pass.'},
                {'q': 'I ___ (call) you if I need help.', 'o': ["call", "'ll call", "would call", "called"], 'a': 1, 'e': "Главное предложение → I'll call."},
                {'q': 'Правильное предложение:', 'o': ['If it will rain, I\'ll stay home.', 'If it rains, I\'ll stay home.', 'If it rains, I would stay home.', 'If it rains, I stay home.'], 'a': 1, 'e': 'IF + Present Simple, will + base form.'},
                {'q': '___ you help me if I ask?', 'o': ['Do', 'Would', 'Will', 'Are'], 'a': 2, 'e': 'Реальное условие → Will you...?'},
                {'q': 'Unless you ___ (hurry), you\'ll miss the bus.', 'o': ['hurry', 'will hurry', 'hurried', 'are hurrying'], 'a': 0, 'e': 'Unless = if not → Present Simple: hurry.'},
                {'q': 'If she ___ (not/eat), she\'ll be hungry.', 'o': ["won't eat", "doesn't eat", "didn't eat", "not eats"], 'a': 1, 'e': "IF + Present Simple: doesn't eat."},
                {'q': 'Переставь порядок (без запятой):', 'o': ['I\'ll stay home, if it rains.', 'I\'ll stay home if it rains.', 'I\'ll stay home if it will rain.', 'I stay home if it rains.'], 'a': 1, 'e': "Когда IF в конце — запятая не нужна."},
                {'q': 'If you ___ (touch) that, you\'ll burn yourself!', 'o': ['will touch', 'touch', 'touched', 'are touching'], 'a': 1, 'e': 'IF + Present Simple: touch.'},
                {'q': '"Unless = ___"', 'o': ['If', 'If not', 'When not', 'While not'], 'a': 1, 'e': 'Unless = if not.'},
            ],
            'test': [
                {'q': 'If he ___ (work) hard, he\'ll succeed.', 'o': ['will work', 'works', 'worked', 'is working'], 'a': 1},
                {'q': 'She ___ (be) angry if you do that.', 'o': ["'ll be", "would be", "is", "was"], 'a': 0},
                {'q': '___ you call me if you need anything?', 'o': ['Do', 'Would', 'Will', 'Are'], 'a': 2},
                {'q': 'If it ___ (snow), we\'ll build a snowman.', 'o': ['will snow', 'snows', 'snowed', 'is snowing'], 'a': 1},
                {'q': 'I\'ll wait ___ you come back.', 'o': ['if', 'unless', 'when', 'while'], 'a': 2},
                {'q': 'Unless she ___ (call), I won\'t know.', 'o': ['will call', 'calls', 'called', 'is calling'], 'a': 1},
                {'q': 'If you ___ (not/sleep), you\'ll be tired.', 'o': ["won't sleep", "don't sleep", "didn't sleep", "not sleep"], 'a': 1},
                {'q': 'If I ___ (have) time, I\'ll visit you.', 'o': ['will have', 'have', 'had', 'am having'], 'a': 1},
                {'q': 'She ___ (not/pass) unless she studies.', 'o': ["won't pass", "doesn't pass", "didn't pass", "not passes"], 'a': 0},
                {'q': 'Правильная структура 1-го условного:', 'o': ['If + will, Present', 'If + Present, will + verb', 'If + Past, would + verb', 'If + Present, Present'], 'a': 1},
                {'q': 'If you ___ (eat) that, you\'ll feel sick.', 'o': ['will eat', 'eat', 'ate', 'are eating'], 'a': 1},
                {'q': 'I\'ll buy it if I ___ (have) enough money.', 'o': ['will have', 'have', 'had', 'having'], 'a': 1},
                {'q': 'Unless it ___ (stop) raining, we\'ll stay inside.', 'o': ['will stop', 'stops', 'stopped', 'is stopping'], 'a': 1},
                {'q': 'If he ___ (arrive) late, tell him to wait.', 'o': ['will arrive', 'arrives', 'arrived', 'is arriving'], 'a': 1},
                {'q': '1-й тип условных выражает:', 'o': ['Нереальное прошлое', 'Реальное/возможное будущее', 'Воображаемую ситуацию', 'Постоянные истины'], 'a': 1},
            ]
        },
        {
            'id': 'b1_g5',
            'title': 'Модальные глаголы: must/should/might',
            'icon': '⚖️',
            'explanation': (
                '📌 *Модальные глаголы: must / should / might*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *MUST — обязанность, сильная уверенность*\n\n'
                '1. Обязанность (от говорящего):\n'
                '   You *must* do your homework.\n'
                '   I *must* call her. (я сам так считаю)\n\n'
                '2. Сильная уверенность (логический вывод):\n'
                '   He works 16 hours a day. He *must* be tired!\n'
                '   She *must* be at home — her car is outside.\n\n'
                '❌ *Отрицание:*\n'
                '• *Mustn\'t* = нельзя (запрет)!\n'
                '  You *mustn\'t* smoke here.\n'
                '• *Don\'t have to* = не нужно (нет обязательства)\n'
                '  You *don\'t have to* come. (но можешь)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *SHOULD — совет, рекомендация*\n\n'
                '• You *should* see a doctor.\n'
                '• She *shouldn\'t* eat so much sugar.\n'
                '• *Should* I call him?\n'
                '• You *should have* called earlier. (совет о прошлом)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *MIGHT — слабая возможность (может быть)*\n\n'
                '• I *might* go to the party. (может быть пойду)\n'
                '• She *might* be late. (возможно, опоздает)\n'
                '• It *might* rain. (может дождь пойдёт)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *Шкала вероятности:*\n'
                'must (90%) > should (80%) > might (30%)'
            ),
            'exercises': [
                {'q': '"Ты не должен здесь курить!" (запрет)', 'o': ['You must smoke here.', "You mustn't smoke here.", "You shouldn't smoke here.", "You don't have to smoke here."], 'a': 1, 'e': "Mustn't = запрет (нельзя!)."},
                {'q': 'You look tired. You ___ go to bed.', 'o': ['must', 'should', 'might', 'mustn\'t'], 'a': 1, 'e': "Should = совет (иди спать)."},
                {'q': 'He works 20 hours a day. He ___ be exhausted!', 'o': ['should', 'might', 'must', 'mustn\'t'], 'a': 2, 'e': "Must = логический вывод (100% уверен)."},
                {'q': 'It\'s getting dark. It ___ rain.', 'o': ['must', 'should', 'might', 'mustn\'t'], 'a': 2, 'e': "Might = слабая возможность (может пойдёт)."},
                {'q': '"Тебе не нужно приходить" (нет обязательства):', 'o': ["You mustn't come.", "You shouldn't come.", "You don't have to come.", "You can't come."], 'a': 2, 'e': "Don't have to = нет необходимости."},
                {'q': 'You ___ drink more water. It\'s good for you.', 'o': ['must', 'should', 'might', 'mustn\'t'], 'a': 1, 'e': "Should = рекомендация."},
                {'q': 'She ___ be home. Her lights are on.', 'o': ['should', 'might', 'must', 'mustn\'t'], 'a': 2, 'e': "Must = сильный логический вывод."},
                {'q': 'I ___ go to the party tonight. I\'m not sure.', 'o': ['must', 'should', 'might', 'mustn\'t'], 'a': 2, 'e': "Might = неуверенность, слабая возможность."},
                {'q': 'Разница: mustn\'t vs don\'t have to:', 'o': ['Нет разницы', "Mustn't = запрет, don't have to = не нужно", "Mustn't = не нужно, don't have to = запрет", "Оба означают запрет"], 'a': 1, 'e': "Mustn't = нельзя!, Don't have to = не обязательно."},
                {'q': '___ I call him? What do you think?', 'o': ['Must', 'Should', 'Might', "Mustn't"], 'a': 1, 'e': "Should I...? = просьба о совете."},
            ],
            'test': [
                {'q': 'You ___ be quiet in the library.', 'o': ['should', 'must', 'might', 'mustn\'t'], 'a': 0},
                {'q': 'She\'s very pale. She ___ be sick.', 'o': ['should', 'might', 'must', 'mustn\'t'], 'a': 2},
                {'q': 'You ___ touch the exhibits! (запрет)', 'o': ["mustn't", "should", "might", "don't have to"], 'a': 0},
                {'q': 'I ___ go to the shops later. Not sure.', 'o': ['must', 'should', 'might', "mustn't"], 'a': 2},
                {'q': 'He ___ see a doctor.', 'o': ['must', 'should', 'might', "mustn't"], 'a': 1},
                {'q': '"Тебе не нужно его звать" (не обязательно):', 'o': ["You mustn't call him.", "You shouldn't call him.", "You don't have to call him.", "You can't call him."], 'a': 2},
                {'q': 'There\'s a car. He ___ be here.', 'o': ['should', 'might', 'must', "mustn't"], 'a': 2},
                {'q': '___ I help you? (предложение помощи)', 'o': ['Must', 'Should', 'Might', "Mustn't"], 'a': 1},
                {'q': 'You look pale. You ___ rest.', 'o': ['must', 'should', 'might', "mustn't"], 'a': 1},
                {'q': 'Самый сильный модальный для обязательства:', 'o': ['should', 'might', 'must', 'can'], 'a': 2},
                {'q': 'It ___ be him. Hard to say.', 'o': ['must', 'should', 'might', "mustn't"], 'a': 2},
                {'q': 'Employees ___ wear a uniform. (обязательство)', 'o': ['should', 'might', 'must', "mustn't"], 'a': 2},
                {'q': 'You ___ eat so much junk food.', 'o': ["must", "should", "shouldn't", "mustn't"], 'a': 2},
                {'q': 'We ___ be late. Let\'s hurry! (нельзя)', 'o': ["mustn't", "shouldn't", "might not", "don't have to"], 'a': 0},
                {'q': 'She looks young. She ___ be 18.', 'o': ["must be", "should be", "might be", "mustn't be"], 'a': 2},
            ]
        },
        {
            'id': 'b1_g6',
            'title': 'Страдательный залог (Passive Voice)',
            'icon': '🔄',
            'explanation': (
                '📌 *Passive Voice — Страдательный залог*\n\n'
                'Используется когда важен объект действия, а не тот, кто его совершает.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'am/is/are + *Past Participle* (3-я форма)\n\n'
                '✅ *Активный vs Пассивный:*\n'
                '• Active: The chef *cooks* dinner.\n'
                '• Passive: Dinner *is cooked* by the chef.\n\n'
                '• Active: They *clean* the office every day.\n'
                '• Passive: The office *is cleaned* every day.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *По временам:*\n\n'
                'Present Simple Passive:\n'
                'is/are + Past Participle\n'
                '• English *is spoken* here.\n'
                '• Cars *are made* in this factory.\n\n'
                'Past Simple Passive:\n'
                'was/were + Past Participle\n'
                '• The letter *was written* yesterday.\n'
                '• Many houses *were destroyed* in the flood.\n\n'
                'Future Passive:\n'
                'will be + Past Participle\n'
                '• The project *will be finished* next week.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *BY — исполнитель (если важен):*\n'
                '• This novel was written *by Tolstoy*.\n'
                '• The windows are cleaned *by a cleaner*.\n\n'
                '💡 *Когда BY не нужен:*\n'
                'Когда исполнитель неизвестен или неважен:\n'
                '• My car was stolen. (неизвестно кем)'
            ),
            'exercises': [
                {'q': 'English ___ (speak) all over the world.', 'o': ['speaks', 'is spoken', 'spoke', 'has spoken'], 'a': 1, 'e': 'Passive: is spoken (is + Past Participle).'},
                {'q': 'The window ___ (break) yesterday.', 'o': ['broke', 'was broken', 'is broken', 'break'], 'a': 1, 'e': 'Past Passive: was broken.'},
                {'q': 'The letter ___ (write) by Anna.', 'o': ['wrote', 'has written', 'was written', 'is writing'], 'a': 2, 'e': 'Past Passive: was written by Anna.'},
                {'q': 'These shoes ___ (make) in Italy.', 'o': ['make', 'makes', 'are made', 'made'], 'a': 2, 'e': 'Present Passive: are made.'},
                {'q': 'The project ___ (finish) next week.', 'o': ['will finish', 'will be finished', 'is finished', 'finishes'], 'a': 1, 'e': 'Future Passive: will be finished.'},
                {'q': 'Активный → Пассивный: "They sell books here."', 'o': ['Books are selling here.', 'Books are sold here.', 'Books is sold here.', 'Books sell here.'], 'a': 1, 'e': 'Books are sold here (are + Past Participle sold).'},
                {'q': 'My car ___ (steal) last night!', 'o': ['stole', 'was stolen', 'is stolen', 'stolen'], 'a': 1, 'e': 'Past Passive: was stolen.'},
                {'q': 'This building ___ (build) in 1900.', 'o': ['built', 'was built', 'is built', 'builds'], 'a': 1, 'e': 'Past Passive: was built.'},
                {'q': 'The results ___ (announce) tomorrow.', 'o': ['will announce', 'will be announced', 'are announced', 'announce'], 'a': 1, 'e': 'Future Passive: will be announced.'},
                {'q': 'Зачем используется Passive Voice?', 'o': ['Для действий в прошлом', 'Когда важен объект, а не исполнитель', 'Только с модальными глаголами', 'Для будущего времени'], 'a': 1, 'e': 'Passive используется когда важен объект, а не тот, кто действует.'},
            ],
            'test': [
                {'q': 'Coffee ___ (grow) in Brazil.', 'o': ['grows', 'is growing', 'is grown', 'grow'], 'a': 2},
                {'q': 'The report ___ (write) by the manager.', 'o': ['wrote', 'was written', 'is writing', 'written'], 'a': 1},
                {'q': 'The new bridge ___ (open) next year.', 'o': ['will open', 'will be opened', 'is opened', 'opens'], 'a': 1},
                {'q': 'Thousands of people ___ (employ) by this company.', 'o': ['employ', 'employs', 'are employed', 'employed'], 'a': 2},
                {'q': 'The building ___ (damage) in the storm.', 'o': ['damaged', 'was damaged', 'is damaged', 'has damaged'], 'a': 1},
                {'q': 'Active → Passive: "Scientists discovered a new planet."', 'o': ['A new planet discovered.', 'A new planet was discovered.', 'A new planet is discovered.', 'A new planet has discovered.'], 'a': 1},
                {'q': 'All guests ___ (invite) to the ceremony.', 'o': ['invite', 'invites', 'are invited', 'invited'], 'a': 2},
                {'q': 'My wallet ___ (steal).', 'o': ['stole', 'was stolen', 'stolen', 'stealed'], 'a': 1},
                {'q': 'The film ___ (show) on TV tonight.', 'o': ['will show', 'will be shown', 'shows', 'is showing'], 'a': 1},
                {'q': 'French ___ (speak) in many countries.', 'o': ['speaks', 'spoke', 'is spoken', 'spoken'], 'a': 2},
                {'q': 'The car ___ (make) in Germany.', 'o': ['make', 'makes', 'is made', 'was making'], 'a': 2},
                {'q': 'The winners ___ (announce) yesterday.', 'o': ['announced', 'were announced', 'are announced', 'will be announced'], 'a': 1},
                {'q': 'The meeting ___ (hold) every Monday.', 'o': ['holds', 'is holding', 'is held', 'held'], 'a': 2},
                {'q': 'The new law ___ (sign) by the president.', 'o': ['signed', 'was signed', 'is signing', 'has signed'], 'a': 1},
                {'q': 'Children ___ (teach) respect.', 'o': ['teach', 'teaches', 'are taught', 'taught'], 'a': 2},
            ]
        },
        {
            'id': 'b1_g7',
            'title': 'Определительные придаточные (who/which/that)',
            'icon': '🔗',
            'explanation': (
                '📌 *Определительные придаточные предложения*\n'
                '*(Relative Clauses)*\n\n'
                'Придаточные определительные уточняют, о ком или о чём мы говорим.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Относительные местоимения:*\n\n'
                '• *WHO* — для людей:\n'
                '  The woman *who* lives next door is a doctor.\n'
                '  I met a man *who* speaks 5 languages.\n\n'
                '• *WHICH* — для предметов и животных:\n'
                '  The book *which* I bought is great.\n'
                '  Do you have a cat *which* can do tricks?\n\n'
                '• *THAT* — для людей И предметов (неформально):\n'
                '  The film *that* I saw was amazing.\n'
                '  The man *that* called is my boss.\n\n'
                '• *WHERE* — для мест:\n'
                '  This is the restaurant *where* we met.\n\n'
                '• *WHEN* — для времени:\n'
                '  I remember the day *when* we first met.\n\n'
                '• *WHOSE* — притяжательное (чей):\n'
                '  The girl *whose* bag was stolen called the police.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Можно опускать that/which/who:*\n'
                'Если это объект (не подлежащее):\n'
                '• The film (that) I saw... ✅\n'
                '• The man (who) I met... ✅\n'
                '• НО: The man who called me... ❌ (нельзя убрать — подлежащее)'
            ),
            'exercises': [
                {'q': 'The woman ___ called is my teacher.', 'o': ['which', 'who', 'where', 'whose'], 'a': 1, 'e': 'Для людей → WHO.'},
                {'q': 'The book ___ I read was interesting.', 'o': ['who', 'which', 'where', 'when'], 'a': 1, 'e': 'Для предметов → WHICH (или that).'},
                {'q': 'That\'s the house ___ I was born.', 'o': ['who', 'which', 'where', 'when'], 'a': 2, 'e': 'Для мест → WHERE.'},
                {'q': 'I know a man ___ can fix your car.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1, 'e': 'Для людей → WHO.'},
                {'q': 'The girl ___ bag was stolen went to the police.', 'o': ['who', 'which', 'whose', 'that'], 'a': 2, 'e': 'Притяжательное → WHOSE.'},
                {'q': 'This is the day ___ everything changed.', 'o': ['who', 'which', 'where', 'when'], 'a': 3, 'e': 'Для времени → WHEN.'},
                {'q': 'The car ___ he drives is very expensive.', 'o': ['who', 'which', 'whose', 'where'], 'a': 1, 'e': 'Для предметов → WHICH (или that).'},
                {'q': 'Can who быть заменён на that?', 'o': ['Никогда', 'Всегда', 'Только в неформальной речи', 'Только когда это объект'], 'a': 2, 'e': 'That можно использовать вместо who в неформальной речи.'},
                {'q': 'People ___ live in cold regions are used to snow.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1, 'e': 'Для людей → WHO.'},
                {'q': 'Можно ли опустить "that" в "The film that I saw was great"?', 'o': ['Нет, нельзя', 'Да, можно — это объектное', 'Только в вопросе', 'Только в письменной речи'], 'a': 1, 'e': 'That = объект → можно опустить: "The film I saw..."'},
            ],
            'test': [
                {'q': 'The doctor ___ treated me was excellent.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1},
                {'q': 'This is the city ___ I grew up.', 'o': ['who', 'which', 'where', 'when'], 'a': 2},
                {'q': 'The book ___ is on the table is mine.', 'o': ['who', 'which', 'whose', 'where'], 'a': 1},
                {'q': 'The student ___ essay won first prize is my friend.', 'o': ['who', 'which', 'whose', 'that'], 'a': 2},
                {'q': 'I remember the moment ___ she told me the news.', 'o': ['who', 'which', 'where', 'when'], 'a': 3},
                {'q': 'People ___ work night shifts are often tired.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1},
                {'q': 'Is this the bag ___ you lost?', 'o': ['who', 'that', 'whose', 'where'], 'a': 1},
                {'q': 'The hotel ___ we stayed had a pool.', 'o': ['who', 'which', 'where', 'whose'], 'a': 2},
                {'q': 'She has a friend ___ knows the president.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1},
                {'q': 'The film ___ won the award was French.', 'o': ['which', 'who', 'whose', 'where'], 'a': 0},
                {'q': 'The man ___ car was stolen called the police.', 'o': ['who', 'which', 'whose', 'that'], 'a': 2},
                {'q': 'She is the woman ___ helped me.', 'o': ['which', 'who', 'whose', 'where'], 'a': 1},
                {'q': 'The town ___ I was born is small.', 'o': ['who', 'which', 'where', 'when'], 'a': 2},
                {'q': 'Можно ли опустить "who" в "The man who called me"?', 'o': ['Да, всегда', 'Нет, это подлежащее', 'Да, в вопросах', 'Да, в неформальной речи'], 'a': 1},
                {'q': 'The key ___ opens this door is missing.', 'o': ['who', 'which', 'whose', 'where'], 'a': 1},
            ]
        },
        {
            'id': 'b1_g8',
            'title': 'Герундий и инфинитив',
            'icon': '🔧',
            'explanation': (
                '📌 *Герундий (-ING) и Инфинитив (TO + глагол)*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Герундий (-ing) используется после:*\n\n'
                'enjoy, mind, avoid, finish, suggest,\n'
                'consider, keep, admit, deny, practise,\n'
                'give up, carry on, look forward to\n\n'
                '• I *enjoy swimming*.\n'
                '• She *finished reading* the book.\n'
                '• He *avoided answering* my question.\n'
                '• I *look forward to hearing* from you.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Инфинитив (to + verb) после:*\n\n'
                'want, hope, plan, decide, need, agree,\n'
                'offer, refuse, seem, manage, fail,\n'
                'would like, would love, be able to\n\n'
                '• She *wants to go*.\n'
                '• He *decided to leave*.\n'
                '• I *managed to pass* the exam.\n'
                '• They *agreed to help*.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *После прилагательных — инфинитив:*\n'
                '• It\'s easy *to learn* English.\n'
                '• I\'m happy *to help*.\n'
                '• It\'s important *to sleep* well.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Глаголы с ОБЕИМИ формами (с разным смыслом!):*\n\n'
                '• I *stopped smoking*. (перестал курить)\n'
                '• I *stopped to smoke*. (остановился, чтобы закурить)\n\n'
                '• I *remember posting* the letter. (помню, что отправил)\n'
                '• I *remembered to post* the letter. (не забыл отправить)\n\n'
                '• She *tried learning* Greek. (попробовала изучать)\n'
                '• She *tried to learn* Greek. (пыталась выучить)'
            ),
            'exercises': [
                {'q': 'I enjoy ___ (read).', 'o': ['to read', 'reading', 'read', 'reads'], 'a': 1, 'e': 'enjoy + -ing: enjoy reading.'},
                {'q': 'She wants ___ (go) home.', 'o': ['going', 'go', 'to go', 'goes'], 'a': 2, 'e': 'want + to + verb: wants to go.'},
                {'q': 'He avoided ___ (answer) my question.', 'o': ['to answer', 'answering', 'answer', 'answers'], 'a': 1, 'e': 'avoid + -ing: avoided answering.'},
                {'q': 'I decided ___ (study) medicine.', 'o': ['studying', 'study', 'to study', 'studies'], 'a': 2, 'e': 'decide + to + verb: to study.'},
                {'q': 'She finished ___ (write) the report.', 'o': ['to write', 'write', 'writing', 'writes'], 'a': 2, 'e': 'finish + -ing: finished writing.'},
                {'q': 'He managed ___ (pass) the exam.', 'o': ['passing', 'pass', 'to pass', 'passes'], 'a': 2, 'e': 'manage + to + verb: managed to pass.'},
                {'q': 'I look forward to ___ (hear) from you.', 'o': ['hear', 'to hear', 'hearing', 'heard'], 'a': 2, 'e': 'look forward to + -ing: hearing.'},
                {'q': '"I stopped ___ (smoke)." — Он перестал:', 'o': ['to smoke', 'smoking', 'smoke', 'smokes'], 'a': 1, 'e': 'stopped smoking = перестал курить.'},
                {'q': 'It\'s difficult ___ (learn) Japanese.', 'o': ['learning', 'learn', 'to learn', 'learns'], 'a': 2, 'e': 'После прилагательного → to learn.'},
                {'q': 'She suggested ___ (go) to the park.', 'o': ['to go', 'going', 'go', 'goes'], 'a': 1, 'e': 'suggest + -ing: suggested going.'},
            ],
            'test': [
                {'q': 'I love ___ (swim) in the sea.', 'o': ['to swim', 'swim', 'swimming', 'swims'], 'a': 2},
                {'q': 'She hopes ___ (become) a doctor.', 'o': ['becoming', 'become', 'to become', 'becomes'], 'a': 2},
                {'q': 'They kept ___ (talk) all night.', 'o': ['to talk', 'talk', 'talking', 'talked'], 'a': 2},
                {'q': 'He refused ___ (help) us.', 'o': ['helping', 'help', 'to help', 'helps'], 'a': 2},
                {'q': 'I can\'t stand ___ (wait) in queues.', 'o': ['to wait', 'wait', 'waiting', 'waits'], 'a': 2},
                {'q': 'She agreed ___ (join) the team.', 'o': ['joining', 'join', 'to join', 'joins'], 'a': 2},
                {'q': 'We plan ___ (visit) Rome.', 'o': ['visiting', 'visit', 'to visit', 'visits'], 'a': 2},
                {'q': 'He admitted ___ (steal) the money.', 'o': ['to steal', 'steal', 'stealing', 'stole'], 'a': 2},
                {'q': 'I\'d like ___ (speak) to the manager.', 'o': ['speaking', 'speak', 'to speak', 'speaks'], 'a': 2},
                {'q': 'She gave up ___ (eat) junk food.', 'o': ['to eat', 'eat', 'eating', 'eats'], 'a': 2},
                {'q': 'They failed ___ (finish) on time.', 'o': ['finishing', 'finish', 'to finish', 'finishes'], 'a': 2},
                {'q': 'I remember ___ (post) the letter. (помню, что отправил)', 'o': ['to post', 'post', 'posting', 'posts'], 'a': 2},
                {'q': 'Practise ___ (speak) English every day.', 'o': ['to speak', 'speak', 'speaking', 'speaks'], 'a': 2},
                {'q': 'He seems ___ (be) happy.', 'o': ['being', 'be', 'to be', 'is'], 'a': 2},
                {'q': 'It\'s nice ___ (meet) you.', 'o': ['meeting', 'meet', 'to meet', 'met'], 'a': 2},
            ]
        },
    ],
    'vocabulary': [
        {
            'category': 'Работа и карьера',
            'icon': '💼',
            'words': [
                {'en': 'apply for a job', 'ru': 'подать заявление на работу', 'ex': 'I applied for a job yesterday.'},
                {'en': 'interview', 'ru': 'собеседование', 'ex': 'I have an interview tomorrow.'},
                {'en': 'salary', 'ru': 'зарплата', 'ex': 'My salary is good.'},
                {'en': 'promote', 'ru': 'повышать (в должности)', 'ex': 'She was promoted to manager.'},
                {'en': 'colleague', 'ru': 'коллега', 'ex': 'My colleagues are friendly.'},
                {'en': 'deadline', 'ru': 'срок сдачи', 'ex': 'The deadline is Friday.'},
                {'en': 'resign', 'ru': 'уволиться', 'ex': 'He resigned from his job.'},
                {'en': 'retire', 'ru': 'уйти на пенсию', 'ex': 'She retired at 65.'},
                {'en': 'experience', 'ru': 'опыт', 'ex': 'I have 5 years of experience.'},
                {'en': 'qualification', 'ru': 'квалификация', 'ex': 'What qualifications do you have?'},
            ]
        },
        {
            'category': 'Здоровье',
            'icon': '🏥',
            'words': [
                {'en': 'symptom', 'ru': 'симптом', 'ex': 'What are your symptoms?'},
                {'en': 'prescription', 'ru': 'рецепт', 'ex': 'The doctor gave me a prescription.'},
                {'en': 'surgery', 'ru': 'операция', 'ex': 'He had heart surgery.'},
                {'en': 'allergy', 'ru': 'аллергия', 'ex': 'I have an allergy to cats.'},
                {'en': 'vaccine', 'ru': 'вакцина', 'ex': 'Get the flu vaccine.'},
                {'en': 'recover', 'ru': 'выздоравливать', 'ex': 'She recovered quickly.'},
                {'en': 'injury', 'ru': 'травма', 'ex': 'He has a knee injury.'},
                {'en': 'diet', 'ru': 'диета/питание', 'ex': 'A healthy diet is important.'},
                {'en': 'stress', 'ru': 'стресс', 'ex': 'Stress can cause illness.'},
                {'en': 'appointment', 'ru': 'запись/прием', 'ex': 'I have a doctor\'s appointment.'},
            ]
        },
        {
            'category': 'Технологии',
            'icon': '💻',
            'words': [
                {'en': 'software', 'ru': 'программное обеспечение', 'ex': 'Update your software.'},
                {'en': 'download', 'ru': 'скачивать', 'ex': 'Download the app.'},
                {'en': 'upload', 'ru': 'загружать', 'ex': 'Upload your photo.'},
                {'en': 'password', 'ru': 'пароль', 'ex': 'Choose a strong password.'},
                {'en': 'search engine', 'ru': 'поисковик', 'ex': 'Google is a search engine.'},
                {'en': 'social media', 'ru': 'социальные сети', 'ex': 'Social media is popular.'},
                {'en': 'connection', 'ru': 'соединение', 'ex': 'The connection is slow.'},
                {'en': 'screen', 'ru': 'экран', 'ex': 'The screen is broken.'},
                {'en': 'keyboard', 'ru': 'клавиатура', 'ex': 'I need a new keyboard.'},
                {'en': 'battery', 'ru': 'батарея', 'ex': 'The battery is low.'},
            ]
        },
        {
            'category': 'Окружающая среда',
            'icon': '🌍',
            'words': [
                {'en': 'pollution', 'ru': 'загрязнение', 'ex': 'Air pollution is a problem.'},
                {'en': 'recycle', 'ru': 'перерабатывать', 'ex': 'We should recycle plastic.'},
                {'en': 'climate change', 'ru': 'изменение климата', 'ex': 'Climate change is real.'},
                {'en': 'renewable energy', 'ru': 'возобновляемая энергия', 'ex': 'Solar is renewable energy.'},
                {'en': 'endangered', 'ru': 'под угрозой исчезновения', 'ex': 'Tigers are endangered.'},
                {'en': 'drought', 'ru': 'засуха', 'ex': 'The drought killed crops.'},
                {'en': 'flood', 'ru': 'наводнение', 'ex': 'The flood damaged homes.'},
                {'en': 'deforestation', 'ru': 'вырубка лесов', 'ex': 'Deforestation destroys habitats.'},
                {'en': 'sustainability', 'ru': 'устойчивость', 'ex': 'We need sustainability.'},
                {'en': 'carbon footprint', 'ru': 'углеродный след', 'ex': 'Reduce your carbon footprint.'},
            ]
        },
        {
            'category': 'Образование',
            'icon': '📚',
            'words': [
                {'en': 'degree', 'ru': 'степень/диплом', 'ex': 'She has a degree in law.'},
                {'en': 'assignment', 'ru': 'задание', 'ex': 'Submit your assignment.'},
                {'en': 'essay', 'ru': 'эссе', 'ex': 'Write a 500-word essay.'},
                {'en': 'scholarship', 'ru': 'стипендия', 'ex': 'She got a scholarship.'},
                {'en': 'tuition', 'ru': 'плата за обучение', 'ex': 'Tuition fees are high.'},
                {'en': 'pass an exam', 'ru': 'сдать экзамен', 'ex': 'Did you pass the exam?'},
                {'en': 'fail an exam', 'ru': 'провалить экзамен', 'ex': 'He failed the exam.'},
                {'en': 'revise', 'ru': 'повторять (материал)', 'ex': 'I need to revise for my test.'},
                {'en': 'graduate', 'ru': 'окончить вуз', 'ex': 'She graduated last year.'},
                {'en': 'curriculum', 'ru': 'учебный план', 'ex': 'The curriculum is challenging.'},
            ]
        },
    ],
    'phrases': [
        {
            'situation': 'Выражение мнения',
            'icon': '💭',
            'items': [
                {'en': 'In my view / From my perspective...', 'ru': 'С моей точки зрения...', 'note': 'Выразить позицию'},
                {'en': 'I strongly believe that...', 'ru': 'Я твёрдо убеждён, что...', 'note': 'Уверенное мнение'},
                {'en': "As far as I'm concerned...", 'ru': 'Что касается меня...', 'note': 'Личная позиция'},
                {'en': 'It seems to me that...', 'ru': 'Мне кажется, что...', 'note': 'Предположение'},
                {'en': "On the other hand...", 'ru': 'С другой стороны...', 'note': 'Контраргумент'},
                {'en': "That's a fair point.", 'ru': 'Это справедливое замечание.', 'note': 'Признать аргумент'},
                {'en': 'I take your point, but...', 'ru': 'Я понимаю тебя, но...', 'note': 'Вежливое возражение'},
            ]
        },
        {
            'situation': 'Соглашение и несогласие',
            'icon': '🤝',
            'items': [
                {'en': 'Absolutely! / Exactly!', 'ru': 'Абсолютно! / Точно!', 'note': 'Полное согласие'},
                {'en': 'I couldn\'t agree more.', 'ru': 'Полностью согласен/согласна.', 'note': 'Сильное согласие'},
                {'en': "I'm not so sure about that.", 'ru': 'Я не так уверен/уверена.', 'note': 'Мягкое несогласие'},
                {'en': "I see your point, but I disagree.", 'ru': 'Понимаю тебя, но не согласен/согласна.', 'note': 'Несогласие'},
                {'en': "That's not necessarily true.", 'ru': 'Это не обязательно так.', 'note': 'Сомнение'},
                {'en': "We'll have to agree to disagree.", 'ru': 'Нам придётся остаться при своих мнениях.', 'note': 'Компромисс'},
            ]
        },
        {
            'situation': 'Собеседование на работу',
            'icon': '👔',
            'items': [
                {'en': "I have X years of experience in...", 'ru': 'У меня X лет опыта в...', 'note': 'Рассказ об опыте'},
                {'en': "My greatest strength is...", 'ru': 'Моя главная сильная сторона...', 'note': 'Сильные стороны'},
                {'en': "I'm a good team player.", 'ru': 'Я хорошо работаю в команде.', 'note': 'Командный игрок'},
                {'en': "I work well under pressure.", 'ru': 'Я хорошо работаю в условиях давления.', 'note': 'Стрессоустойчивость'},
                {'en': "I\'m very interested in this position.", 'ru': 'Я очень заинтересован в этой должности.', 'note': 'Интерес к работе'},
                {'en': 'What are the main responsibilities?', 'ru': 'Каковы основные обязанности?', 'note': 'Вопрос о работе'},
            ]
        },
        {
            'situation': 'Рассказ о прошлом опыте',
            'icon': '📖',
            'items': [
                {'en': "I've been to / I've visited...", 'ru': 'Я был(а) в... / Я посещал(а)...', 'note': 'Опыт путешествий'},
                {'en': "I've never tried...", 'ru': 'Я никогда не пробовал(а)...', 'note': 'Отсутствие опыта'},
                {'en': "The best experience I've had was...", 'ru': 'Лучший опыт в моей жизни...', 'note': 'Лучший опыт'},
                {'en': "I used to...", 'ru': 'Раньше я... (больше не делаю)', 'note': 'Прошлые привычки'},
                {'en': "It was a memorable experience.", 'ru': 'Это был незабываемый опыт.', 'note': 'Описать опыт'},
                {'en': "Looking back, I realise that...", 'ru': 'Оглядываясь назад, понимаю, что...', 'note': 'Рефлексия'},
            ]
        },
        {
            'situation': 'Описание проблем и решений',
            'icon': '🔧',
            'items': [
                {'en': 'The main problem is...', 'ru': 'Главная проблема в том, что...', 'note': 'Назвать проблему'},
                {'en': 'One possible solution is...', 'ru': 'Одним из возможных решений является...', 'note': 'Предложить решение'},
                {'en': 'What if we tried...?', 'ru': 'Что если попробовать...?', 'note': 'Предложение'},
                {'en': "The advantage of this is...", 'ru': 'Преимущество этого в том, что...', 'note': 'Плюс'},
                {'en': "The disadvantage is...", 'ru': 'Недостаток в том, что...', 'note': 'Минус'},
                {'en': "To sum up / In conclusion...", 'ru': 'Подводя итог / В заключение...', 'note': 'Вывод'},
            ]
        },
    ]
}
