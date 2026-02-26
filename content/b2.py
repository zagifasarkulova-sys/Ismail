B2 = {
    'name': 'B2 — Выше среднего',
    'emoji': '🌲',
    'description': (
        '🌲 *Уровень B2 — Выше среднего*\n\n'
        'Ты свободно общаешься на большинство тем. Теперь — шлифуем!\n'
        'На этом уровне:\n'
        '• Сложные временные конструкции\n'
        '• Все типы условных предложений\n'
        '• Продвинутый страдательный залог\n'
        '• Сложные грамматические структуры\n\n'
        'Выбери раздел:'
    ),
    'grammar': [
        {
            'id': 'b2_g1',
            'title': 'Present Perfect Continuous',
            'icon': '⏱️',
            'explanation': (
                '📌 *Present Perfect Continuous*\n\n'
                'Подчёркивает продолжительность действия, которое началось в прошлом и продолжается сейчас (или только что завершилось).\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'have/has been + глагол + *-ING*\n\n'
                '✅ *Примеры:*\n'
                '• I *\'ve been studying* for 3 hours. (и ещё учусь)\n'
                '• She *\'s been working* here since 2019.\n'
                '• They *\'ve been waiting* for an hour!\n'
                '• He looks tired — he *\'s been running*.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *PP vs PP Continuous:*\n\n'
                '• I *\'ve read* 50 pages. (результат — сколько прочитал)\n'
                '• I *\'ve been reading* for 2 hours. (процесс — как долго)\n\n'
                '• She *\'s written* 3 emails. (количество)\n'
                '• She *\'s been writing* emails all morning. (процесс)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Маркеры:* for, since, all day/morning, how long\n\n'
                '⚠️ *Глаголы состояния (state verbs) НЕ используют -ing:*\n'
                'know, like, love, hate, want, believe, understand\n'
                '• I\'ve *known* him for years. ✅\n'
                '• ~~I\'ve been knowing him~~ ❌'
            ),
            'exercises': [
                {'q': 'She looks tired. She ___ (work) all day.', 'o': ["has worked", "has been working", "had worked", "worked"], 'a': 1, 'e': "Процесс → has been working."},
                {'q': 'I ___ (wait) for 2 hours!', 'o': ["waited", "have waited", "have been waiting", "has been waiting"], 'a': 2, 'e': "Продолжительность → have been waiting."},
                {'q': 'How long ___ you (study) English?', 'o': ["do", "have", "have been", "did"], 'a': 2, 'e': "How long have you been studying?"},
                {'q': 'He ___ (run) — he\'s all sweaty!', 'o': ["ran", "has run", "has been running", "had run"], 'a': 2, 'e': "Свежий результат+процесс → has been running."},
                {'q': 'Выбери PP Continuous:', 'o': ["She's written 5 emails.", "She's been writing emails.", "She wrote emails.", "She has write emails."], 'a': 1, 'e': "Been writing — PP Continuous (процесс)."},
                {'q': 'They ___ (live) here since 2010.', 'o': ["live", "lived", "have lived", "have been living"], 'a': 3, 'e': "Since + продолжающееся → have been living."},
                {'q': '"Я знаю его 10 лет" → I ___ him for 10 years.', 'o': ["know", "knew", "have been knowing", "have known"], 'a': 3, 'e': "know — глагол состояния → have known (НЕ been knowing!)."},
                {'q': 'It ___ (rain) all morning.', 'o': ["rained", "has rained", "has been raining", "had rained"], 'a': 2, 'e': "Продолжительность → has been raining."},
                {'q': 'PP vs PP Continuous: "I\'ve read the report" vs "I\'ve been reading":', 'o': ['Нет разницы', 'Первое — результат (сколько), второе — процесс (как долго)', 'Первое — прошлое, второе — настоящее', 'Первое — более формально'], 'a': 1, 'e': "Первое = результат, второе = продолжительность."},
                {'q': 'She ___ (not/sleep) well lately.', 'o': ["hasn't sleep", "hasn't been sleeping", "didn't sleep", "wasn't sleeping"], 'a': 1, 'e': "PP Continuous: hasn't been sleeping."},
            ],
            'test': [
                {'q': 'How long ___ you (learn) English?', 'o': ["do you learn", "have you been learning", "did you learn", "are you learning"], 'a': 1},
                {'q': 'She ___ (study) since 8am.', 'o': ["studied", "has studied", "has been studying", "had studied"], 'a': 2},
                {'q': 'I ___ (work) on this project for 6 months.', 'o': ["worked", "have worked", "have been working", "am working"], 'a': 2},
                {'q': 'He looks pale — he ___ (not/feel) well.', 'o': ["hasn't felt", "hasn't been feeling", "didn't feel", "wasn't feeling"], 'a': 1},
                {'q': 'PP Continuous маркер:', 'o': ['yesterday', 'last year', 'for two weeks', 'at 5pm'], 'a': 2},
                {'q': '"Глагол состояния" — нельзя с PP Continuous:', 'o': ['work', 'sleep', 'know', 'study'], 'a': 2},
                {'q': 'They ___ (argue) all evening.', 'o': ["argued", "have argued", "have been arguing", "had argued"], 'a': 2},
                {'q': 'She ___ (cry) — her eyes are red.', 'o': ["cried", "has cried", "has been crying", "had cried"], 'a': 2},
                {'q': 'I ___ (want) to visit Japan for years.', 'o': ["want", "have wanted", "have been wanting", "wanted"], 'a': 1},
                {'q': 'We ___ (live) in London since 2015.', 'o': ["lived", "live", "have been living", "had lived"], 'a': 2},
                {'q': 'She\'s tired because she ___ (exercise).', 'o': ["exercises", "has exercised", "has been exercising", "exercised"], 'a': 2},
                {'q': 'Разница: "I\'ve written 3 reports" vs "I\'ve been writing":', 'o': ['Нет разницы', 'Первое = результат, второе = процесс', 'Первое = процесс, второе = результат', 'Оба = результат'], 'a': 1},
                {'q': 'He ___ (not/sleep) since Monday.', 'o': ["hasn't slept", "hasn't been sleeping", "didn't sleep", "wasn't sleeping"], 'a': 1},
                {'q': 'It ___ (get) warmer recently.', 'o': ["gets", "got", "has been getting", "had gotten"], 'a': 2},
                {'q': 'You look sunburned! ___ you (sit) in the sun?', 'o': ["Did you sit", "Have you been sitting", "Were you sitting", "Do you sit"], 'a': 1},
            ]
        },
        {
            'id': 'b2_g2',
            'title': 'Past Perfect',
            'icon': '⏮️',
            'explanation': (
                '📌 *Past Perfect — Прошлое до прошлого*\n\n'
                'Описывает действие, которое завершилось ДО другого прошлого действия.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'had + Past Participle (3-я форма)\n\n'
                '✅ *Примеры:*\n'
                '• When I arrived, she *had already left*.\n'
                '  (Сначала она ушла → потом я пришёл)\n'
                '• He was tired because he *hadn\'t slept*.\n'
                '• I didn\'t know the film because I *hadn\'t seen* it.\n'
                '• By the time we arrived, it *had stopped* raining.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Временная шкала:*\n'
                'Past Perfect → Past Simple → Present\n'
                '(сначала)     (потом)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I *hadn\'t* finished when he called.\n\n'
                '❓ *Вопрос:*\n'
                '• *Had* you *eaten* before we left?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Ключевые слова:*\n'
                'when, by the time, before, after, already,\n'
                'never, just, because'
            ),
            'exercises': [
                {'q': 'When I arrived, she ___ (already/leave).', 'o': ['already left', 'had already left', 'has already left', 'was already left'], 'a': 1, 'e': 'Past Perfect: had already left.'},
                {'q': 'He was tired because he ___ (not/sleep).', 'o': ["didn't sleep", "hasn't slept", "hadn't slept", "wasn't sleeping"], 'a': 2, 'e': "Причина в прошлом → hadn't slept."},
                {'q': 'By the time we got there, the film ___ (start).', 'o': ['started', 'has started', 'had started', 'was starting'], 'a': 2, 'e': "By the time → Past Perfect: had started."},
                {'q': '___ you (eat) before the meeting?', 'o': ['Did you eat', 'Have you eaten', 'Had you eaten', 'Were you eating'], 'a': 2, 'e': "Past Perfect question: Had you eaten?"},
                {'q': 'She ___ (never/visit) London before that trip.', 'o': ["never visited", "has never visited", "had never visited", "was never visiting"], 'a': 2, 'e': "Опыт до другого прошлого → had never visited."},
                {'q': 'I recognised him because I ___ (see) him before.', 'o': ['saw', 'have seen', 'had seen', 'was seeing'], 'a': 2, 'e': "Предшествующее прошлое → had seen."},
                {'q': 'After they ___ (finish) dinner, they went for a walk.', 'o': ['finished', 'have finished', 'had finished', 'were finishing'], 'a': 2, 'e': "After + Past Perfect: had finished."},
                {'q': 'I ___ (just/send) the email when the internet cut off.', 'o': ['just sent', 'have just sent', 'had just sent', 'was just sending'], 'a': 2, 'e': "had just sent (Past Perfect)."},
                {'q': 'Порядок: "She left before I arrived."', 'o': ['Сначала я, потом она', 'Сначала она, потом я', 'Одновременно', 'Нельзя определить'], 'a': 1, 'e': 'Она ушла (Past Perfect/Simple) до того, как я пришёл (Past Simple).'},
                {'q': 'He couldn\'t pay — he ___ (lose) his wallet.', 'o': ['lost', 'has lost', 'had lost', 'was losing'], 'a': 2, 'e': "Причина в прошлом → had lost."},
            ],
            'test': [
                {'q': 'When she called, I ___ (already/go) to bed.', 'o': ['already went', 'have already gone', 'had already gone', 'was already going'], 'a': 2},
                {'q': 'I ___ (never/eat) sushi before my trip to Japan.', 'o': ["never ate", "have never eaten", "had never eaten", "never eating"], 'a': 2},
                {'q': '___ he (finish) his homework before dinner?', 'o': ['Did he finish', 'Has he finished', 'Had he finished', 'Was he finishing'], 'a': 2},
                {'q': 'By the time we arrived, they ___ (leave).', 'o': ['left', 'have left', 'had left', 'were leaving'], 'a': 2},
                {'q': 'She was sad because she ___ (fail) the exam.', 'o': ["failed", "has failed", "had failed", "was failing"], 'a': 2},
                {'q': 'After he ___ (read) the book, he watched the film.', 'o': ['read', 'has read', 'had read', 'was reading'], 'a': 2},
                {'q': 'I ___ (not/meet) him before that day.', 'o': ["didn't meet", "haven't met", "hadn't met", "wasn't meeting"], 'a': 2},
                {'q': 'The students ___ (just/finish) when the teacher arrived.', 'o': ['just finished', 'have just finished', 'had just finished', 'were just finishing'], 'a': 2},
                {'q': 'She looked familiar — I ___ (see) her somewhere before.', 'o': ['saw', 'have seen', 'had seen', 'was seeing'], 'a': 2},
                {'q': 'Past Perfect маркер:', 'o': ['now', 'at the moment', 'by the time', 'every day'], 'a': 2},
                {'q': '___ you (hear) about this before he told you?', 'o': ['Did you hear', 'Have you heard', 'Had you heard', 'Were you hearing'], 'a': 2},
                {'q': 'He was tired because he ___ (work) all day.', 'o': ["worked", "has worked", "had worked", "was working"], 'a': 2},
                {'q': 'They couldn\'t enter — they ___ (forget) the password.', 'o': ["forgot", "have forgotten", "had forgotten", "were forgetting"], 'a': 2},
                {'q': 'Before I called you, I ___ (already/try) 3 times.', 'o': ['already tried', 'have already tried', 'had already tried', 'was already trying'], 'a': 2},
                {'q': 'Формула Past Perfect:', 'o': ['was/were + -ing', 'have/has + PP', 'had + PP', 'will + verb'], 'a': 2},
            ]
        },
        {
            'id': 'b2_g3',
            'title': 'Second Conditional (2-й тип)',
            'icon': '💭',
            'explanation': (
                '📌 *Second Conditional — 2-й тип условных*\n\n'
                'Воображаемые, нереальные ситуации в настоящем/будущем.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Структура:*\n'
                '*IF + Past Simple, would + глагол*\n\n'
                '✅ *Примеры:*\n'
                '• If I *were* a millionaire, I *would* travel the world.\n'
                '  (Но я не миллионер — нереально)\n'
                '• If she *had* more time, she *would learn* Spanish.\n'
                '• What *would* you do if you *won* the lottery?\n'
                '• I *wouldn\'t* buy that if I *were* you.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *WERE вместо WAS:*\n'
                'В 2-м типе условных формально используется WERE для всех лиц:\n'
                '• If I *were* you... ✅ (разговорно: If I was you)\n'
                '• If he *were* here...\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *1-й vs 2-й тип:*\n'
                '• If it *rains*, I\'ll take an umbrella. (реально, 1-й)\n'
                '• If I *were* a bird, I *would* fly. (нереально, 2-й)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Could/Might вместо Would:*\n'
                '• If I had money, I *could* buy it. (была бы возможность)\n'
                '• If I had more time, I *might* go. (может быть пошёл бы)'
            ),
            'exercises': [
                {'q': 'If I ___ (be) rich, I would travel more.', 'o': ['am', 'was', 'were', 'would be'], 'a': 2, 'e': "2-й тип: IF + Past Simple (were для всех лиц)."},
                {'q': 'If she ___ (have) more time, she would call.', 'o': ['has', 'had', 'would have', 'have'], 'a': 1, 'e': "2-й тип: IF + Past Simple: had."},
                {'q': 'I ___ (buy) that car if I had enough money.', 'o': ['buy', 'bought', 'would buy', 'will buy'], 'a': 2, 'e': "Главное предложение → would buy."},
                {'q': 'What ___ you do if you (win) the lottery?', 'o': ['will / win', 'would / won', 'would / wins', 'do / win'], 'a': 1, 'e': "Would + Past Simple: would you do if you won."},
                {'q': 'Разница 1-го и 2-го типа условных:', 'o': ['Нет разницы', '1-й = реальное, 2-й = нереальное/воображаемое', '1-й = прошлое, 2-й = будущее', '1-й = нереальное, 2-й = реальное'], 'a': 1, 'e': "1-й тип = реальное условие, 2-й = гипотетическое."},
                {'q': 'If he ___ (not/be) so busy, he would help us.', 'o': ["isn't", "wasn't", "weren't", "wouldn't be"], 'a': 2, 'e': "IF + Past Simple: weren't."},
                {'q': '"If I were you, I ___ (talk) to him."', 'o': ['will talk', 'would talk', 'talked', 'talk'], 'a': 1, 'e': "would talk."},
                {'q': 'She ___ (learn) to drive if she had more time.', 'o': ['learns', 'would learn', 'learned', 'will learn'], 'a': 1, 'e': "Главное → would learn."},
                {'q': 'Could вместо would во 2-м типе:', 'o': ['Нельзя никогда', 'Можно — означает "имел бы возможность"', 'Только в формальной речи', 'Только в вопросах'], 'a': 1, 'e': "Could = была бы возможность (instead of would)."},
                {'q': 'Правильное предложение (2-й тип):', 'o': ['If it will rain, I would stay.', 'If it rains, I would stay.', 'If it rained, I would stay.', 'If it rained, I will stay.'], 'a': 2, 'e': "IF + Past Simple, would + verb: If it rained, I would stay."},
            ],
            'test': [
                {'q': 'If I ___ (know) the answer, I would tell you.', 'o': ['know', 'knew', 'would know', 'known'], 'a': 1},
                {'q': 'She ___ (be) happier if she had a different job.', 'o': ['is', 'was', 'would be', 'will be'], 'a': 2},
                {'q': 'If he ___ (not/eat) so much, he would be healthier.', 'o': ["doesn't eat", "didn't eat", "wouldn't eat", "hadn't eaten"], 'a': 1},
                {'q': 'What would you do if you ___ (can) fly?', 'o': ['can', 'could', 'would can', 'will can'], 'a': 1},
                {'q': 'If I ___ (be) you, I wouldn\'t do that.', 'o': ['am', 'was', 'were', 'would be'], 'a': 2},
                {'q': 'He would work harder if the salary ___ (be) better.', 'o': ['is', 'was', 'were', 'would be'], 'a': 2},
                {'q': 'I ___ (call) her if I had her number.', 'o': ['call', 'called', 'would call', 'will call'], 'a': 2},
                {'q': '___ you (travel) if you had more money?', 'o': ['Will you travel', 'Would you travel', 'Do you travel', 'Did you travel'], 'a': 1},
                {'q': 'If animals ___ (can/speak), what would they say?', 'o': ['can', 'could', 'would', 'were'], 'a': 1},
                {'q': 'She ___ (might/understand) if you explained clearly.', 'o': ['might understand', 'might understood', 'would might understand', 'might to understand'], 'a': 0},
                {'q': 'If I ___ (live) in Spain, I\'d speak Spanish.', 'o': ['live', 'lived', 'would live', 'will live'], 'a': 1},
                {'q': 'They ___ (enjoy) the trip more if the weather were better.', 'o': ['enjoy', 'enjoyed', 'would enjoy', 'will enjoy'], 'a': 2},
                {'q': 'Нереальное условие → использование:', 'o': ['1-й тип', '2-й тип', '3-й тип', 'Mixed conditional'], 'a': 1},
                {'q': 'If you ___ (be) more careful, you wouldn\'t make mistakes.', 'o': ['are', 'was', 'were', 'would be'], 'a': 2},
                {'q': 'I could help more if I ___ (have) more time.', 'o': ['have', 'had', 'would have', 'having'], 'a': 1},
            ]
        },
        {
            'id': 'b2_g4',
            'title': 'Third Conditional (3-й тип)',
            'icon': '🕰️',
            'explanation': (
                '📌 *Third Conditional — 3-й тип условных*\n\n'
                'Нереальные ситуации в ПРОШЛОМ — то, чего уже не изменить.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Структура:*\n'
                '*IF + Past Perfect, would have + Past Participle*\n\n'
                '✅ *Примеры:*\n'
                '• If I *had studied* harder, I *would have passed*.\n'
                '  (Но я не учился → и не сдал — прошлое)\n'
                '• If she *had arrived* earlier, she *would have met* him.\n'
                '• If we *hadn\'t taken* a taxi, we *would have been* late.\n'
                '• I *wouldn\'t have said* that if I *had known* the truth.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Сокращения:*\n'
                '• would have → *\'d have*\n'
                '• would not have → *wouldn\'t have*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *Все 3 типа:*\n'
                '1-й: IF + Pres.Simple, WILL → реальное будущее\n'
                '2-й: IF + Past Simple, WOULD → нереальное настоящее\n'
                '3-й: IF + Past Perfect, WOULD HAVE → нереальное прошлое'
            ),
            'exercises': [
                {'q': 'If I ___ (study), I would have passed.', 'o': ['studied', 'had studied', 'have studied', 'would study'], 'a': 1, 'e': '3-й тип: IF + Past Perfect: had studied.'},
                {'q': 'She ___ (get) the job if she had prepared better.', 'o': ['would get', 'would have gotten', 'got', 'had gotten'], 'a': 1, 'e': "Главная часть → would have gotten."},
                {'q': 'If we had left earlier, we ___ (not/miss) the train.', 'o': ["wouldn't miss", "wouldn't have missed", "didn't miss", "hadn't missed"], 'a': 1, 'e': "wouldn't have missed."},
                {'q': 'I ___ (call) you if I had had your number.', 'o': ['would call', 'would have called', 'called', 'had called'], 'a': 1, 'e': "3-й тип: would have called."},
                {'q': '___ you (buy) it if the price had been lower?', 'o': ['Would you buy', 'Would you have bought', 'Did you buy', 'Had you bought'], 'a': 1, 'e': "Would you have bought? (3-й тип)."},
                {'q': 'Правильное предложение (3-й тип):', 'o': ['If I had money, I will buy it.', 'If I had had money, I would buy it.', 'If I had had money, I would have bought it.', 'If I have had money, I would have bought it.'], 'a': 2, 'e': "IF + Past Perfect, would have + PP."},
                {'q': 'She ___ (not/feel) ill if she hadn\'t eaten that.', 'o': ["wouldn't feel", "wouldn't have felt", "didn't feel", "hadn't felt"], 'a': 1, 'e': "wouldn't have felt."},
                {'q': 'If the weather ___ (be) better, we would have had a picnic.', 'o': ['was', 'were', 'had been', 'would be'], 'a': 2, 'e': "3-й тип: IF + Past Perfect: had been."},
                {'q': '3-й тип условных используется для:', 'o': ['Реального будущего', 'Нереального настоящего', 'Нереального прошлого', 'Регулярных действий'], 'a': 2, 'e': "3-й тип = нереальная прошлая ситуация."},
                {'q': 'If I ___ (know) she was coming, I\'d have cooked more.', 'o': ['knew', 'had known', 'would know', 'have known'], 'a': 1, 'e': "had known (Past Perfect)."},
            ],
            'test': [
                {'q': 'If he ___ (work) harder, he would have got promoted.', 'o': ['worked', 'had worked', 'has worked', 'would work'], 'a': 1},
                {'q': 'I ___ (not/say) that if I had known.', 'o': ["wouldn't say", "wouldn't have said", "didn't say", "hadn't said"], 'a': 1},
                {'q': 'If she ___ (take) the medicine, she would have recovered.', 'o': ['took', 'had taken', 'has taken', 'would take'], 'a': 1},
                {'q': '___ you (go) if you had had the chance?', 'o': ['Would you go', 'Would you have gone', 'Did you go', 'Had you gone'], 'a': 1},
                {'q': 'If they ___ (arrive) earlier, they wouldn\'t have missed the show.', 'o': ['arrived', 'had arrived', 'have arrived', 'would arrive'], 'a': 1},
                {'q': 'He ___ (win) if he had tried harder.', 'o': ['would win', 'would have won', 'won', 'had won'], 'a': 1},
                {'q': 'If I ___ (not/forget) my passport, I could have boarded.', 'o': ["didn't forget", "hadn't forgotten", "have not forgotten", "wouldn't forget"], 'a': 1},
                {'q': 'She ___ (be) happy if she had got the job.', 'o': ['would be', 'would have been', 'was', 'had been'], 'a': 1},
                {'q': 'Правильная формула 3-го типа:', 'o': ['IF + Present, WILL', 'IF + Past, WOULD', 'IF + Past Perfect, WOULD HAVE + PP', 'IF + PP, HAD + PP'], 'a': 2},
                {'q': 'They ___ (help) if they had known about the problem.', 'o': ['would help', 'would have helped', 'helped', 'had helped'], 'a': 1},
                {'q': 'If I ___ (see) that film, I would have loved it.', 'o': ['saw', 'had seen', 'have seen', 'would see'], 'a': 1},
                {'q': 'We ___ (not/get) lost if we had used the map.', 'o': ["wouldn't get", "wouldn't have got", "didn't get", "hadn't got"], 'a': 1},
                {'q': 'If the car ___ (not/break) down, we would have arrived on time.', 'o': ["didn't break", "hadn't broken", "hasn't broken", "wouldn't break"], 'a': 1},
                {'q': 'He ___ (apply) for the job if he had seen the advert.', 'o': ['would apply', 'would have applied', 'applied', 'had applied'], 'a': 1},
                {'q': 'I ___ (not/buy) it if I had read the reviews.', 'o': ["wouldn't buy", "wouldn't have bought", "didn't buy", "hadn't bought"], 'a': 1},
            ]
        },
        {
            'id': 'b2_g5',
            'title': 'Страдательный залог — все времена',
            'icon': '🔄',
            'explanation': (
                '📌 *Passive Voice — все времена*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *Таблица Passive по временам:*\n\n'
                '*Present Simple:* is/are + PP\n'
                '• The office *is cleaned* daily.\n\n'
                '*Past Simple:* was/were + PP\n'
                '• The letter *was sent* yesterday.\n\n'
                '*Future Simple:* will be + PP\n'
                '• The results *will be announced* tomorrow.\n\n'
                '*Present Continuous:* is/are being + PP\n'
                '• The house *is being painted* now.\n\n'
                '*Past Continuous:* was/were being + PP\n'
                '• The road *was being repaired* all week.\n\n'
                '*Present Perfect:* has/have been + PP\n'
                '• The project *has been completed*.\n\n'
                '*Past Perfect:* had been + PP\n'
                '• The file *had been deleted* before we arrived.\n\n'
                '*Modal + Passive:* modal + be + PP\n'
                '• This *must be done* today.\n'
                '• The problem *should be solved*.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Активный → Пассивный:*\n'
                '1. Объект → подлежащее\n'
                '2. Добавить нужную форму be\n'
                '3. Глагол → Past Participle\n'
                '4. Подлежащее → by + (если нужно)'
            ),
            'exercises': [
                {'q': 'The windows ___ (clean) right now. (Continuous)', 'o': ['are cleaning', 'are being cleaned', 'have been cleaned', 'were cleaned'], 'a': 1, 'e': 'Present Continuous Passive: are being cleaned.'},
                {'q': 'The report ___ (write) before the meeting. (Past Perfect)', 'o': ['was written', 'had been written', 'has been written', 'were written'], 'a': 1, 'e': 'Past Perfect Passive: had been written.'},
                {'q': 'This problem ___ (solve) tomorrow. (Future)', 'o': ['will solve', 'will be solved', 'is solved', 'was solved'], 'a': 1, 'e': 'Future Passive: will be solved.'},
                {'q': 'The road ___ (repair) when we drove past. (Past Continuous)', 'o': ['was repairing', 'was being repaired', 'has been repaired', 'had been repaired'], 'a': 1, 'e': 'Past Continuous Passive: was being repaired.'},
                {'q': 'The contract ___ (sign) already. (Present Perfect)', 'o': ['has signed', 'has been signed', 'was signed', 'is signed'], 'a': 1, 'e': 'Present Perfect Passive: has been signed.'},
                {'q': 'This ___ (must/do) immediately.', 'o': ['must do', 'must be done', 'must have done', 'must be doing'], 'a': 1, 'e': 'Modal Passive: must be done.'},
                {'q': 'Active → Passive: "They are building a new bridge."', 'o': ['A new bridge is building.', 'A new bridge is being built.', 'A new bridge has been built.', 'A new bridge was built.'], 'a': 1, 'e': 'Present Continuous Passive: is being built.'},
                {'q': 'The mistake ___ (should/correct).', 'o': ['should correct', 'should be corrected', 'should have correct', 'should been corrected'], 'a': 1, 'e': 'Modal Passive: should be corrected.'},
                {'q': '"They had finished the project." → Passive:', 'o': ['The project was finished.', 'The project has been finished.', 'The project had been finished.', 'The project is finished.'], 'a': 2, 'e': 'Past Perfect Passive: had been finished.'},
                {'q': 'The concert ___ (cancel) due to bad weather.', 'o': ['was cancelled', 'was cancelling', 'is cancelled', 'had cancelled'], 'a': 0, 'e': 'Past Simple Passive: was cancelled.'},
            ],
            'test': [
                {'q': 'The new policy ___ (announce) yesterday.', 'o': ['announced', 'was announced', 'is announced', 'has announced'], 'a': 1},
                {'q': 'The building ___ (renovate) at the moment.', 'o': ['is renovating', 'is being renovated', 'has been renovated', 'was renovated'], 'a': 1},
                {'q': 'The letter ___ (not/send) yet.', 'o': ["wasn't sent", "hasn't been sent", "isn't being sent", "hadn't been sent"], 'a': 1},
                {'q': 'All employees ___ (inform) before the changes.', 'o': ['were informed', 'had been informed', 'are informed', 'were being informed'], 'a': 1},
                {'q': 'The new road ___ (complete) by 2025.', 'o': ['will complete', 'will be completed', 'is completed', 'was completed'], 'a': 1},
                {'q': '"They should fix this." → Passive:', 'o': ['This should fix.', 'This should be fixed.', 'This should fixed.', 'This should have fixed.'], 'a': 1},
                {'q': 'The criminals ___ (arrest) last night.', 'o': ['arrested', 'were arrested', 'have been arrested', 'are arrested'], 'a': 1},
                {'q': '"Someone is watching you." → Passive:', 'o': ['You are watching.', 'You are being watched.', 'You have been watched.', 'You were watched.'], 'a': 1},
                {'q': 'The film ___ (make) in 1984.', 'o': ['made', 'was made', 'has been made', 'is made'], 'a': 1},
                {'q': 'The decision ___ (must/make) today.', 'o': ['must make', 'must be made', 'must have made', 'must been made'], 'a': 1},
                {'q': 'The emails ___ (already/send). (Present Perfect)', 'o': ['already sent', 'have already been sent', 'were already sent', 'are already sent'], 'a': 1},
                {'q': 'My bag ___ (steal) while I was shopping.', 'o': ['stole', 'was stolen', 'is stolen', 'had stolen'], 'a': 1},
                {'q': '"He had already written the report." → Passive:', 'o': ['The report had written already.', 'The report had been already written.', 'The report had already been written.', 'The report was already written.'], 'a': 2},
                {'q': 'A new hospital ___ (build) in our town.', 'o': ['is building', 'is being built', 'has built', 'builds'], 'a': 1},
                {'q': 'The test ___ (should/take) seriously.', 'o': ['should take', 'should be taken', 'should taking', 'should have taken'], 'a': 1},
            ]
        },
        {
            'id': 'b2_g6',
            'title': 'Causative: have/get something done',
            'icon': '🛠️',
            'explanation': (
                '📌 *Causative — have/get something done*\n\n'
                'Используется когда мы не делаем что-то САМИ, а заставляем/просим других.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Структура:*\n'
                'have/get + объект + Past Participle\n\n'
                '✅ *Примеры:*\n'
                '• I *had* my hair *cut*.\n'
                '  (Я постриг волосы — в парикмахерской, не сам)\n'
                '• She *got* her car *repaired*.\n'
                '  (Она отдала машину в ремонт)\n'
                '• We *had* the house *painted*.\n'
                '• He\'s *getting* his teeth *checked*.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *По временам:*\n'
                '• I *have* my hair *cut* every month. (Present Simple)\n'
                '• She *had* her nails *done* yesterday. (Past Simple)\n'
                '• I\'m *having* the car *serviced*. (Present Cont.)\n'
                '• She *has had* her photo *taken*. (Present Perfect)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Have vs Get:*\n'
                '• *Have* — более формальный\n'
                '• *Get* — более разговорный\n'
                '• Both are correct!\n\n'
                '⚠️ *Разница с Passive:*\n'
                '• Passive: My car *was repaired*. (просто факт)\n'
                '• Causative: I *had* my car *repaired*. (я организовал)'
            ),
            'exercises': [
                {'q': 'She ___ her hair ___ at the salon. (cut)', 'o': ['did / cut', 'had / cut', 'made / cut', 'got / cutting'], 'a': 1, 'e': 'had + hair + cut (PP).'},
                {'q': 'I need to ___ my laptop ___. (repair)', 'o': ['have / repaired', 'make / repaired', 'do / repaired', 'get / repaired'], 'a': 0, 'e': 'have + laptop + repaired (or get).'},
                {'q': 'They\'re ___ their house ___. (paint)', 'o': ['having / paint', 'having / painted', 'making / painted', 'doing / painting'], 'a': 1, 'e': 'having + house + painted.'},
                {'q': 'Значение "I had my car serviced":', 'o': ['Я сам починил машину', 'Я отдал машину на техобслуживание', 'Моя машина сломалась', 'Мне нужно починить машину'], 'a': 1, 'e': 'Causative = я организовал, кто-то другой сделал.'},
                {'q': '"Get" в causative:', 'o': ['Нельзя использовать', 'Более формальный вариант have', 'Более разговорный вариант have', 'Используется только в вопросах'], 'a': 2, 'e': 'Get = разговорный вариант have в causative.'},
                {'q': 'I ___ my teeth ___ twice a year. (check)', 'o': ['have / check', 'have / checked', 'make / checked', 'do / check'], 'a': 1, 'e': 'have + teeth + checked.'},
                {'q': 'She got her photo ___ for her passport.', 'o': ['take', 'taking', 'taken', 'took'], 'a': 2, 'e': 'get + photo + taken (PP).'},
                {'q': 'Правильная структура causative:', 'o': ['have + PP + object', 'have + object + PP', 'have + object + base', 'have + verb-ing + object'], 'a': 1, 'e': 'have/get + OBJECT + Past Participle.'},
                {'q': 'He ___ his suit ___. (dry-clean)', 'o': ['had / dry-cleaned', 'made / dry-cleaned', 'did / dry-clean', 'got / dry-cleaning'], 'a': 0, 'e': 'had + suit + dry-cleaned.'},
                {'q': 'Разница Passive vs Causative:', 'o': ['Нет разницы', "Passive = просто факт, Causative = кто-то организовал", "Causative = сам сделал, Passive = кто-то другой", "Оба одинаковы по смыслу"], 'a': 1, 'e': "Passive = факт произошёл, Causative = субъект организовал это."},
            ],
            'test': [
                {'q': 'I need to ___ my eyes ___. (test)', 'o': ['make / tested', 'have / tested', 'do / tested', 'get / test'], 'a': 1},
                {'q': 'She ___ her portrait ___. (paint)', 'o': ['had / painted', 'made / painted', 'did / paint', 'got / painting'], 'a': 0},
                {'q': 'They\'re ___ a new kitchen ___. (install)', 'o': ['having / installed', 'making / installed', 'doing / install', 'getting / install'], 'a': 0},
                {'q': '"She got her nails done" означает:', 'o': ['Она сама сделала ногти', 'Ей сделали ногти', 'Её ногти красивые', 'Нужно сделать ногти'], 'a': 1},
                {'q': 'He\'s ___ his car ___. (service)', 'o': ['having / serviced', 'making / serviced', 'doing / service', 'getting / servicing'], 'a': 0},
                {'q': 'Правильное предложение (causative):', 'o': ['I had cut my hair.', 'I had my hair cut.', 'I had my hair cutting.', 'I had myself hair cut.'], 'a': 1},
                {'q': 'We ___ our house ___. (decorate)', 'o': ['had / decorated', 'made / decorated', 'did / decorate', 'got / decorating'], 'a': 0},
                {'q': 'She ___ her bag ___. (steal)', 'o': ['had / stolen', 'made / stolen', 'did / steal', 'got / stealing'], 'a': 0},
                {'q': 'I\'m going to ___ my phone screen ___. (fix)', 'o': ['have / fixed', 'make / fixed', 'do / fix', 'get / fixing'], 'a': 0},
                {'q': 'He ___ his blood ___. (test)', 'o': ['had / tested', 'made / tested', 'did / test', 'got / testing'], 'a': 0},
                {'q': '"Более разговорный" causative:', 'o': ['have something done', 'get something done', 'make something done', 'do something done'], 'a': 1},
                {'q': 'They ___ the roof ___. (repair)', 'o': ['had / repaired', 'made / repair', 'did / repaired', 'got / repairing'], 'a': 0},
                {'q': 'She ___ her visa ___. (renew)', 'o': ['had / renewed', 'made / renewed', 'did / renew', 'got / renewing'], 'a': 0},
                {'q': 'I need to ___ my windows ___. (clean)', 'o': ['have / cleaned', 'make / cleaned', 'do / clean', 'get / cleaning'], 'a': 0},
                {'q': '"She had her car stolen" означает:', 'o': ['Она продала машину', 'У неё украли машину (не по её воле)', 'Она отдала машину', 'Она взяла чужую машину'], 'a': 1},
            ]
        },
        {
            'id': 'b2_g7',
            'title': 'Wish / If only',
            'icon': '🌟',
            'explanation': (
                '📌 *Wish / If only — сожаление и желание*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *Wish + Past Simple — о настоящем/будущем:*\n'
                '(Хочу, чтобы что-то было по-другому СЕЙЧАС)\n\n'
                '• I *wish* I *knew* the answer.\n'
                '  (Жаль, что не знаю — но не знаю)\n'
                '• She *wishes* she *lived* near the sea.\n'
                '• I *wish* I *were* taller.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *Wish + Past Perfect — о прошлом:*\n'
                '(Сожалею о том, что произошло/не произошло)\n\n'
                '• I *wish* I *had studied* harder.\n'
                '  (Жаль, что не учился — теперь не изменить)\n'
                '• She *wishes* she *hadn\'t said* that.\n'
                '• I *wish* I *had gone* to the party.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '3️⃣ *Wish + would — о поведении:*\n'
                '(Хочу, чтобы кто-то изменил поведение)\n\n'
                '• I *wish* you *would stop* making noise!\n'
                '• She *wishes* he *would listen* to her.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *If only = Wish (более эмоционально):*\n'
                '• *If only* I had more time!\n'
                '• *If only* she hadn\'t left!'
            ),
            'exercises': [
                {'q': 'I wish I ___ (know) the answer. (сейчас не знаю)', 'o': ['know', 'knew', 'had known', 'would know'], 'a': 1, 'e': 'Wish + Past Simple (о настоящем): knew.'},
                {'q': 'She wishes she ___ (not/say) that. (уже сказала — прошлое)', 'o': ["didn't say", "hadn't said", "wouldn't say", "hasn't said"], 'a': 1, 'e': 'Wish + Past Perfect (о прошлом): hadn\'t said.'},
                {'q': 'I wish you ___ (stop) talking! (измени поведение)', 'o': ['stop', 'stopped', 'had stopped', 'would stop'], 'a': 3, 'e': 'Wish + would (просьба изменить поведение).'},
                {'q': 'If only I ___ (study) harder! (сожаление о прошлом)', 'o': ['study', 'studied', 'had studied', 'would study'], 'a': 2, 'e': 'If only + Past Perfect: had studied.'},
                {'q': 'He wishes he ___ (be) taller. (сейчас)', 'o': ['is', 'was', 'were', 'had been'], 'a': 2, 'e': 'Wish + were (Past Simple для to be, все лица).'},
                {'q': 'Wish + Past Perfect выражает:', 'o': ['Желание о будущем', 'Сожаление о прошлом', 'Просьбу изменить поведение', 'Факт о настоящем'], 'a': 1, 'e': 'Wish + Past Perfect = сожаление о прошлом.'},
                {'q': 'I wish I ___ (can) swim. (сейчас не умею)', 'o': ['can', 'could', 'would can', 'had can'], 'a': 1, 'e': 'Wish + Past Simple: could (прошедшая форма can).'},
                {'q': '"If only he would listen!" означает:', 'o': ['Он слушал в прошлом', 'Жаль, что он не слушает (сейчас)', 'Я хочу чтобы он слушал (просьба)', 'Он будет слушать'], 'a': 2, 'e': 'Wish/If only + would = желание изменить поведение другого.'},
                {'q': 'She wishes she ___ (live) in Paris. (мечта о настоящем)', 'o': ['lives', 'lived', 'had lived', 'would live'], 'a': 1, 'e': 'Wish + Past Simple о настоящем: lived.'},
                {'q': 'Разница: "I wish I had studied" vs "I wish I studied":', 'o': ['Нет разницы', 'Первое = прошлое, второе = настоящее', 'Первое = настоящее, второе = прошлое', 'Оба = настоящее'], 'a': 1, 'e': 'had studied = Past Perfect = сожаление о прошлом; studied = настоящее.'},
            ],
            'test': [
                {'q': 'I wish I ___ (speak) Spanish. (сейчас)', 'o': ['speak', 'spoke', 'had spoken', 'would speak'], 'a': 1},
                {'q': 'She wishes she ___ (go) to the concert. (прошлое)', 'o': ['went', 'has gone', 'had gone', 'would go'], 'a': 2},
                {'q': 'I wish he ___ (be) more helpful. (поведение)', 'o': ['is', 'was', 'were', 'would be'], 'a': 3},
                {'q': 'If only I ___ (not/eat) so much! (прошлое)', 'o': ["didn't eat", "hadn't eaten", "wouldn't eat", "wouldn't have eaten"], 'a': 1},
                {'q': 'He wishes he ___ (know) the answer. (сейчас)', 'o': ['knows', 'knew', 'had known', 'would know'], 'a': 1},
                {'q': 'I wish you ___ (not/smoke) indoors. (поведение)', 'o': ["don't smoke", "didn't smoke", "hadn't smoked", "wouldn't smoke"], 'a': 3},
                {'q': 'She wishes she ___ (study) medicine. (прошлое)', 'o': ['studied', 'had studied', 'would study', 'studies'], 'a': 1},
                {'q': 'If only it ___ (be) sunny! (сейчас)', 'o': ['is', 'was', 'were', 'would be'], 'a': 2},
                {'q': 'I wish I ___ (take) that opportunity. (прошлое)', 'o': ['take', 'took', 'had taken', 'would take'], 'a': 2},
                {'q': 'Wish + Past Simple = ?', 'o': ['Сожаление о прошлом', 'Желание о настоящем', 'Просьба изменить поведение', 'Предсказание'], 'a': 1},
                {'q': 'They wish they ___ (live) closer to the city.', 'o': ['live', 'lived', 'had lived', 'would live'], 'a': 1},
                {'q': 'I wish I ___ (be) on holiday right now!', 'o': ['am', 'was', 'were', 'would be'], 'a': 2},
                {'q': 'She wishes she ___ (not/quit) her job. (прошлое)', 'o': ["didn't quit", "hadn't quit", "wouldn't quit", "hasn't quit"], 'a': 1},
                {'q': 'I wish he ___ (call) me back. (поведение)', 'o': ['calls', 'called', 'had called', 'would call'], 'a': 3},
                {'q': 'If only I ___ (be) taller! (сейчас)', 'o': ['am', 'was', 'were', 'would be'], 'a': 2},
            ]
        },
        {
            'id': 'b2_g8',
            'title': 'Mixed Conditionals (смешанные)',
            'icon': '🔀',
            'explanation': (
                '📌 *Mixed Conditionals — Смешанные условные*\n\n'
                'Смешивают времена из 2-го и 3-го типов, когда условие и результат относятся к разному времени.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *Прошлое условие → Настоящий результат:*\n'
                '(3-й тип в IF + 2-й тип в главном)\n\n'
                'IF + Past Perfect → would + verb\n\n'
                '• If I *had studied* harder, I *would be* a doctor now.\n'
                '  (Если бы учился — сейчас был бы доктором)\n'
                '• If she *hadn\'t moved* to London, she *wouldn\'t be* my colleague.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *Настоящее условие → Прошлый результат:*\n'
                '(2-й тип в IF + 3-й тип в главном)\n\n'
                'IF + Past Simple → would have + PP\n\n'
                '• If I *were* more confident, I *would have applied* for the job.\n'
                '  (Если бы был увереннее — подал бы заявку тогда)\n'
                '• If he *weren\'t* so lazy, he *would have finished* by now.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *Итого все типы:*\n'
                '0: IF + Pres → Pres (факты)\n'
                '1-й: IF + Pres → WILL (реальное)\n'
                '2-й: IF + Past → WOULD (нереальное наст.)\n'
                '3-й: IF + Past Perf → WOULD HAVE (прошлое)\n'
                'Mixed: IF + Past Perf → WOULD (прошлое→наст.)\n'
                '       IF + Past Simple → WOULD HAVE (наст.→прошлое)'
            ),
            'exercises': [
                {'q': 'If I ___ (study) medicine, I would be a doctor now.', 'o': ['studied', 'had studied', 'have studied', 'would study'], 'a': 1, 'e': 'Past Perfect в IF → прошлое условие.'},
                {'q': 'If she hadn\'t moved here, she ___ (not/be) my friend.', 'o': ["wouldn't be", "wouldn't have been", "wasn't", "hadn't been"], 'a': 0, 'e': 'Прошлое условие → настоящий результат: wouldn\'t be.'},
                {'q': 'If he ___ (not/be) so lazy, he would have finished by now.', 'o': ["wasn't", "weren't", "hadn't been", "wouldn't be"], 'a': 1, 'e': 'Настоящее условие (2-й тип): weren\'t.'},
                {'q': 'If I were braver, I ___ (apply) for the job last year.', 'o': ['would apply', 'would have applied', 'applied', 'had applied'], 'a': 1, 'e': 'Настоящее условие → прошлый результат: would have applied.'},
                {'q': 'Mixed Conditional Type 1 (PP→Pres): результат относится к:', 'o': ['Прошлому', 'Настоящему', 'Будущему', 'Нет разницы'], 'a': 1, 'e': 'Past Perfect условие → настоящий результат.'},
                {'q': 'If they ___ (take) my advice, they wouldn\'t be in trouble now.', 'o': ['took', 'had taken', 'would take', 'have taken'], 'a': 1, 'e': 'Прошлое условие: had taken.'},
                {'q': 'If he weren\'t so shy, he ___ (ask) her out ages ago.', 'o': ['would ask', 'would have asked', 'asked', 'had asked'], 'a': 1, 'e': 'Настоящее условие → прошлый результат: would have asked.'},
                {'q': 'Правильный Mixed Conditional:', 'o': ['If she studies hard, she would pass.', 'If she had studied hard, she would pass now.', 'If she would study hard, she will pass.', 'If she had study, she would have passed.'], 'a': 1, 'e': 'If + Past Perfect → would (настоящее).'},
                {'q': 'If I ___ (know) then what I know now, I would have acted differently.', 'o': ['know', 'knew', 'had known', 'would know'], 'a': 2, 'e': 'Прошлое условие: had known.'},
                {'q': 'If she weren\'t so careless, she ___ (not/lose) the contract last month.', 'o': ["wouldn't lose", "wouldn't have lost", "didn't lose", "hadn't lost"], 'a': 1, 'e': 'Настоящее условие → прошлый результат: wouldn\'t have lost.'},
            ],
            'test': [
                {'q': 'If I had worked harder, I ___ (have) a better job now.', 'o': ['would have', "would've had", 'would had', 'had had'], 'a': 1},
                {'q': 'If she ___ (not/be) so stubborn, she would have accepted the offer.', 'o': ["wasn't", "weren't", "hadn't been", "wouldn't be"], 'a': 1},
                {'q': 'If they had invested wisely, they ___ (be) rich now.', 'o': ['would be', "would've been", 'are', 'were'], 'a': 0},
                {'q': 'If I ___ (study) harder at school, I would have a better career.', 'o': ['study', 'studied', 'had studied', 'would study'], 'a': 2},
                {'q': 'If he weren\'t so proud, he ___ (ask) for help earlier.', 'o': ['would ask', 'would have asked', 'asked', 'had asked'], 'a': 1},
                {'q': 'Тип: "If + Past Perfect → would"', 'o': ['1-й', '2-й', '3-й', 'Mixed (прошлое → настоящее)'], 'a': 3},
                {'q': 'If she ___ (be) more patient, she would have succeeded.', 'o': ['is', 'was', 'were', 'had been'], 'a': 2},
                {'q': 'If I hadn\'t taken that course, I ___ (not/have) this job now.', 'o': ["wouldn't have", "wouldn't have had", "don't have", "didn't have"], 'a': 0},
                {'q': 'If you ___ (tell) me earlier, I would have helped.', 'o': ['told', 'had told', 'tell', 'would tell'], 'a': 1},
                {'q': 'If he weren\'t so negative, things ___ (work out) better last year.', 'o': ['would work out', 'would have worked out', 'worked out', 'had worked out'], 'a': 1},
                {'q': 'If I had listened to my parents, I ___ (be) a lawyer now.', 'o': ["'d be", "'d have been", "am", "were"], 'a': 0},
                {'q': 'If she ___ (not/waste) time, she would have graduated on time.', 'o': ["didn't waste", "weren't wasting", "hadn't wasted", "wouldn't waste"], 'a': 2},
                {'q': 'Тип: "If + Past Simple → would have"', 'o': ['1-й', '2-й', '3-й', 'Mixed (настоящее → прошлое)'], 'a': 3},
                {'q': 'If I ___ (be) taller, I would have become a basketball player.', 'o': ['am', 'was', 'were', 'had been'], 'a': 2},
                {'q': 'If they hadn\'t argued, they ___ (still/be) together.', 'o': ['would still be', "would've still been", 'are still', 'still were'], 'a': 0},
            ]
        },
    ],
    'vocabulary': [
        {
            'category': 'Бизнес и экономика',
            'icon': '📈',
            'words': [
                {'en': 'profit', 'ru': 'прибыль', 'ex': 'The company made a profit.'},
                {'en': 'budget', 'ru': 'бюджет', 'ex': 'We need to cut the budget.'},
                {'en': 'invest', 'ru': 'инвестировать', 'ex': 'Invest in your education.'},
                {'en': 'bankruptcy', 'ru': 'банкротство', 'ex': 'The company went bankrupt.'},
                {'en': 'revenue', 'ru': 'доход/выручка', 'ex': 'Annual revenue increased.'},
                {'en': 'entrepreneur', 'ru': 'предприниматель', 'ex': 'She is a successful entrepreneur.'},
                {'en': 'merger', 'ru': 'слияние (компаний)', 'ex': 'The merger created jobs.'},
                {'en': 'shareholder', 'ru': 'акционер', 'ex': 'Shareholders approved the deal.'},
                {'en': 'inflation', 'ru': 'инфляция', 'ex': 'Inflation is rising.'},
                {'en': 'recession', 'ru': 'рецессия', 'ex': 'The country is in recession.'},
            ]
        },
        {
            'category': 'СМИ и общество',
            'icon': '📰',
            'words': [
                {'en': 'broadcast', 'ru': 'транслировать/передача', 'ex': 'The match was broadcast live.'},
                {'en': 'censorship', 'ru': 'цензура', 'ex': 'Censorship limits freedom.'},
                {'en': 'propaganda', 'ru': 'пропаганда', 'ex': 'They spread propaganda.'},
                {'en': 'headline', 'ru': 'заголовок', 'ex': 'The headline was shocking.'},
                {'en': 'editorial', 'ru': 'редакционная статья', 'ex': 'The editorial was critical.'},
                {'en': 'circulation', 'ru': 'тираж', 'ex': 'The paper has large circulation.'},
                {'en': 'subscription', 'ru': 'подписка', 'ex': 'I have a Netflix subscription.'},
                {'en': 'bias', 'ru': 'предвзятость', 'ex': 'The report showed bias.'},
                {'en': 'influence', 'ru': 'влияние', 'ex': 'Media has great influence.'},
                {'en': 'coverage', 'ru': 'освещение (событий)', 'ex': 'The news coverage was extensive.'},
            ]
        },
        {
            'category': 'Наука и технологии',
            'icon': '🔬',
            'words': [
                {'en': 'experiment', 'ru': 'эксперимент', 'ex': 'The experiment was successful.'},
                {'en': 'hypothesis', 'ru': 'гипотеза', 'ex': 'The hypothesis was proved.'},
                {'en': 'breakthrough', 'ru': 'прорыв', 'ex': 'A medical breakthrough occurred.'},
                {'en': 'artificial intelligence', 'ru': 'искусственный интеллект', 'ex': 'AI is changing the world.'},
                {'en': 'genetic engineering', 'ru': 'генная инженерия', 'ex': 'Genetic engineering is controversial.'},
                {'en': 'innovation', 'ru': 'инновация', 'ex': 'Innovation drives progress.'},
                {'en': 'prototype', 'ru': 'прототип', 'ex': 'They built a prototype.'},
                {'en': 'patent', 'ru': 'патент', 'ex': 'The invention has a patent.'},
                {'en': 'algorithm', 'ru': 'алгоритм', 'ex': 'The algorithm is complex.'},
                {'en': 'data', 'ru': 'данные', 'ex': 'We need more data.'},
            ]
        },
        {
            'category': 'Политика',
            'icon': '🏛️',
            'words': [
                {'en': 'democracy', 'ru': 'демократия', 'ex': 'Democracy protects rights.'},
                {'en': 'parliament', 'ru': 'парламент', 'ex': 'Parliament voted on the bill.'},
                {'en': 'election', 'ru': 'выборы', 'ex': 'Elections are in November.'},
                {'en': 'campaign', 'ru': 'предвыборная кампания', 'ex': 'The campaign lasted 3 months.'},
                {'en': 'policy', 'ru': 'политика/курс', 'ex': 'New economic policy was set.'},
                {'en': 'legislation', 'ru': 'законодательство', 'ex': 'New legislation was passed.'},
                {'en': 'opposition', 'ru': 'оппозиция', 'ex': 'The opposition criticized the plan.'},
                {'en': 'referendum', 'ru': 'референдум', 'ex': 'A referendum was held.'},
                {'en': 'corruption', 'ru': 'коррупция', 'ex': 'Corruption is a major problem.'},
                {'en': 'sanction', 'ru': 'санкция', 'ex': 'Economic sanctions were imposed.'},
            ]
        },
        {
            'category': 'Искусство и культура',
            'icon': '🎭',
            'words': [
                {'en': 'masterpiece', 'ru': 'шедевр', 'ex': 'It\'s a true masterpiece.'},
                {'en': 'exhibition', 'ru': 'выставка', 'ex': 'The art exhibition opens Friday.'},
                {'en': 'contemporary', 'ru': 'современный', 'ex': 'Contemporary art is unique.'},
                {'en': 'sculpture', 'ru': 'скульптура', 'ex': 'The sculpture is beautiful.'},
                {'en': 'symphony', 'ru': 'симфония', 'ex': 'Beethoven\'s 9th Symphony.'},
                {'en': 'genre', 'ru': 'жанр', 'ex': 'What genre of music do you like?'},
                {'en': 'heritage', 'ru': 'наследие', 'ex': 'Cultural heritage must be preserved.'},
                {'en': 'literary', 'ru': 'литературный', 'ex': 'She has literary talent.'},
                {'en': 'controversial', 'ru': 'спорный/вызывающий споры', 'ex': 'The artwork was controversial.'},
                {'en': 'aesthetic', 'ru': 'эстетический', 'ex': 'I appreciate the aesthetic design.'},
            ]
        },
    ],
    'phrases': [
        {
            'situation': 'Деловая переписка',
            'icon': '📧',
            'items': [
                {'en': 'I am writing with regard to...', 'ru': 'Я пишу по поводу...', 'note': 'Формальное начало письма'},
                {'en': 'Further to our conversation...', 'ru': 'Продолжая нашу беседу...', 'note': 'Ссылка на прошлый разговор'},
                {'en': 'I would be grateful if you could...', 'ru': 'Я был бы признателен, если бы вы...', 'note': 'Вежливая просьба'},
                {'en': 'Please find attached...', 'ru': 'Во вложении вы найдёте...', 'note': 'Про вложение'},
                {'en': 'I look forward to hearing from you.', 'ru': 'С нетерпением жду вашего ответа.', 'note': 'Завершение письма'},
                {'en': 'Yours sincerely / Yours faithfully', 'ru': 'С уважением (формальное завершение)', 'note': 'Подпись письма'},
            ]
        },
        {
            'situation': 'Переговоры',
            'icon': '🤝',
            'items': [
                {'en': "Let's find a middle ground.", 'ru': 'Давайте найдём компромисс.', 'note': 'Поиск компромисса'},
                {'en': 'That\'s not quite what we had in mind.', 'ru': 'Это не совсем то, что мы имели в виду.', 'note': 'Вежливый отказ'},
                {'en': 'What if we were to...?', 'ru': 'Что если нам...?', 'note': 'Предложение альтернативы'},
                {'en': 'We\'re prepared to offer...', 'ru': 'Мы готовы предложить...', 'note': 'Предложение'},
                {'en': "That's a deal.", 'ru': 'По рукам. / Договорились.', 'note': 'Согласие с условиями'},
                {'en': "I'll need to consult with my team.", 'ru': 'Мне нужно проконсультироваться с командой.', 'note': 'Просьба о времени'},
            ]
        },
        {
            'situation': 'Академическое обсуждение',
            'icon': '🎓',
            'items': [
                {'en': 'The evidence suggests that...', 'ru': 'Данные свидетельствуют о том, что...', 'note': 'Ссылка на данные'},
                {'en': 'This can be attributed to...', 'ru': 'Это можно объяснить тем, что...', 'note': 'Объяснение причины'},
                {'en': 'According to recent research...', 'ru': 'Согласно последним исследованиям...', 'note': 'Ссылка на исследование'},
                {'en': 'It could be argued that...', 'ru': 'Можно утверждать, что...', 'note': 'Предположение'},
                {'en': 'However, this view is not without its critics.', 'ru': 'Тем не менее, эта точка зрения не без критиков.', 'note': 'Контраргумент'},
                {'en': 'The implications of this are...', 'ru': 'Последствия этого таковы...', 'note': 'Последствия'},
            ]
        },
        {
            'situation': 'Описание тенденций',
            'icon': '📊',
            'items': [
                {'en': 'There has been a sharp increase in...', 'ru': 'Произошёл резкий рост...', 'note': 'Описать рост'},
                {'en': 'The figures have declined steadily.', 'ru': 'Цифры неуклонно снижались.', 'note': 'Описать спад'},
                {'en': 'It has remained fairly constant.', 'ru': 'Это оставалось достаточно стабильным.', 'note': 'Описать стабильность'},
                {'en': 'This peaked at... in...', 'ru': 'Пик был достигнут в... году/размере...', 'note': 'Описать пик'},
                {'en': 'Overall, the trend shows...', 'ru': 'В целом тенденция показывает...', 'note': 'Общая тенденция'},
                {'en': 'This is likely due to...', 'ru': 'Вероятно, это связано с...', 'note': 'Причина тенденции'},
            ]
        },
        {
            'situation': 'Выражение неуверенности',
            'icon': '🤔',
            'items': [
                {'en': "I'm not entirely sure, but...", 'ru': 'Я не совсем уверен/а, но...', 'note': 'Неуверенность'},
                {'en': "It's hard to say exactly...", 'ru': 'Сложно сказать точно...', 'note': 'Сложно определить'},
                {'en': 'That depends on...', 'ru': 'Это зависит от...', 'note': 'Условная ситуация'},
                {'en': 'There are arguments on both sides.', 'ru': 'Есть аргументы с обеих сторон.', 'note': 'Нейтральная позиция'},
                {'en': "I'd have to think about that.", 'ru': 'Мне нужно подумать об этом.', 'note': 'Нужно время'},
                {'en': "To the best of my knowledge...", 'ru': 'Насколько мне известно...', 'note': 'Ограниченные знания'},
            ]
        },
    ]
}
