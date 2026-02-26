A2 = {
    'name': 'A2 — Элементарный',
    'emoji': '🌿',
    'description': (
        '🌿 *Уровень A2 — Элементарный*\n\n'
        'На этом уровне ты уже умеешь основы и готов идти дальше!\n'
        'Ты научишься:\n'
        '• Говорить о ежедневных действиях (Present Simple)\n'
        '• Рассказывать о том, что происходит прямо сейчас\n'
        '• Говорить о прошлом\n'
        '• Строить планы на будущее\n'
        '• Сравнивать предметы и людей\n\n'
        'Выбери раздел для изучения:'
    ),
    'grammar': [
        {
            'id': 'a2_g1',
            'title': 'Present Simple — настоящее время',
            'icon': '🔄',
            'explanation': (
                '📌 *Present Simple — Настоящее простое время*\n\n'
                'Используется для описания регулярных действий, привычек и фактов.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Когда использовать:*\n'
                '• Регулярные действия: I *work* every day.\n'
                '• Привычки: She *drinks* coffee in the morning.\n'
                '• Факты: Water *boils* at 100°C.\n'
                '• Расписание: The train *leaves* at 8.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '✅ *Утверждение:*\n'
                '• I / You / We / They + глагол (base form)\n'
                '  I *work*. We *live* in Moscow.\n'
                '• He / She / It + глагол + *S* (или ES/IES)\n'
                '  She *works*. He *watches* TV.\n\n'
                '📌 *Правила добавления -S:*\n'
                '• Обычно: + s (work → works)\n'
                '• После s/sh/ch/x/o: + es (watch → watches)\n'
                '• После согласной + y: ies (study → studies)\n'
                '• have → has (исключение!)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I/You/We/They + *do not* (don\'t) + глагол\n'
                '  I *don\'t* like coffee.\n'
                '• He/She/It + *does not* (doesn\'t) + глагол\n'
                '  She *doesn\'t* work on Sundays.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❓ *Вопрос:*\n'
                '• *Do* + I/you/we/they + глагол?\n'
                '  *Do* you like pizza?\n'
                '• *Does* + he/she/it + глагол?\n'
                '  *Does* she speak English?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⏰ *Слова-маркеры:*\n'
                'always, usually, often, sometimes, rarely, never\n'
                'every day/week/morning, on Mondays, at 8 o\'clock'
            ),
            'exercises': [
                {'q': 'She ___ (work) every day.', 'o': ['work', 'works', 'working', 'worked'], 'a': 1, 'e': 'She + глагол с -S: works.'},
                {'q': 'They ___ (live) in London.', 'o': ['live', 'lives', 'living', 'lived'], 'a': 0, 'e': 'They + глагол без изменений: live.'},
                {'q': 'He ___ (not/like) coffee.', 'o': ["don't like", "doesn't like", "not likes", "isn't like"], 'a': 1, 'e': 'He + doesn\'t like (does not + base form).'},
                {'q': '___ you speak French?', 'o': ['Do', 'Does', 'Are', 'Have'], 'a': 0, 'e': 'You → Do you...?'},
                {'q': '___ she work on Sundays?', 'o': ['Do', 'Does', 'Is', 'Has'], 'a': 1, 'e': 'She → Does she...?'},
                {'q': 'He ___ (watch) TV every evening.', 'o': ['watch', 'watchs', 'watches', 'watching'], 'a': 2, 'e': 'watch + es после ch: watches.'},
                {'q': 'She ___ (study) every day.', 'o': ['study', 'studys', 'studies', 'studying'], 'a': 2, 'e': 'study (y после согласной) → studies.'},
                {'q': 'I ___ (not/drink) alcohol.', 'o': ["doesn't drink", "don't drink", "not drink", "isn't drink"], 'a': 1, 'e': 'I + don\'t drink.'},
                {'q': 'Выбери слово-маркер Present Simple:', 'o': ['now', 'yesterday', 'always', 'tomorrow'], 'a': 2, 'e': 'Always — маркер Present Simple (регулярность).'},
                {'q': 'My dog ___ (have) long ears.', 'o': ['have', 'has', 'haves', 'having'], 'a': 1, 'e': 'have → has (исключение для 3-го лица).'},
            ],
            'test': [
                {'q': 'He ___ to school every day.', 'o': ['go', 'goes', 'going', 'gone'], 'a': 1},
                {'q': 'We ___ meat. (не едим)', 'o': ["don't eat", "doesn't eat", "not eat", "aren't eat"], 'a': 0},
                {'q': '___ your mother cook well?', 'o': ['Do', 'Does', 'Is', 'Are'], 'a': 1},
                {'q': 'She ___ English and French.', 'o': ['speak', 'speaks', 'is speak', 'speaking'], 'a': 1},
                {'q': 'The sun ___ in the east.', 'o': ['rise', 'rises', 'is rising', 'rised'], 'a': 1},
                {'q': 'I ___ TV in the evening.', 'o': ['watch', 'watches', 'watching', 'watched'], 'a': 0},
                {'q': '___ they live near here?', 'o': ['Do', 'Does', 'Are', 'Have'], 'a': 0},
                {'q': 'He ___ books in his free time.', 'o': ['read', 'reads', 'reading', 'readed'], 'a': 1},
                {'q': 'She ___ like cold weather.', 'o': ["don't", "doesn't", "isn't", "aren't"], 'a': 1},
                {'q': 'Маркер Present Simple:', 'o': ['right now', 'last week', 'twice a week', 'at the moment'], 'a': 2},
                {'q': 'My sister ___ the piano.', 'o': ['play', 'plays', 'playing', 'played'], 'a': 1},
                {'q': '___ you drink coffee?', 'o': ['Do', 'Does', 'Are', 'Is'], 'a': 0},
                {'q': 'He ___ to bed late.', 'o': ['go', 'goes', 'going', 'gone'], 'a': 1},
                {'q': 'Birds ___ south in winter.', 'o': ['fly', 'flys', 'flies', 'flying'], 'a': 0},
                {'q': 'She ___ a shower every morning.', 'o': ['have', 'has', 'having', 'haves'], 'a': 1},
            ]
        },
        {
            'id': 'a2_g2',
            'title': 'Present Continuous — действие сейчас',
            'icon': '▶️',
            'explanation': (
                '📌 *Present Continuous — Настоящее продолженное*\n\n'
                'Используется для действий, происходящих ПРЯМО СЕЙЧАС или в этот период.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'am / is / are + глагол + *-ING*\n\n'
                '✅ *Утверждение:*\n'
                '• I *am working*. — Я работаю (сейчас).\n'
                '• She *is reading*. — Она читает (сейчас).\n'
                '• They *are playing*. — Они играют (сейчас).\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I *am not* (\'m not) working.\n'
                '• She *is not* (isn\'t) sleeping.\n'
                '• They *are not* (aren\'t) watching TV.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❓ *Вопрос:*\n'
                '• *Am* I doing it right?\n'
                '• *Is* she studying?\n'
                '• *Are* they coming?\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Правила добавления -ING:*\n'
                '• Обычно: + ing (work → working)\n'
                '• Немое E убираем: make → making, write → writing\n'
                '• Удвоение согласной (CVC): run → running, swim → swimming\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⏰ *Маркеры:*\n'
                'now, right now, at the moment, Look!, Listen!\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚡ *Present Simple vs Continuous:*\n'
                '• I usually *work* at home. (привычка)\n'
                '• I *am working* at home today. (сейчас)'
            ),
            'exercises': [
                {'q': 'She ___ (read) a book now.', 'o': ['read', 'reads', 'is reading', 'are reading'], 'a': 2, 'e': 'She + is + reading (сейчас).'},
                {'q': 'They ___ (play) football at the moment.', 'o': ['play', 'plays', 'is playing', 'are playing'], 'a': 3, 'e': 'They + are + playing.'},
                {'q': 'Look! The baby ___ (sleep).', 'o': ['sleeps', 'is sleeping', 'are sleeping', 'sleep'], 'a': 1, 'e': 'Look! = сейчас → is sleeping.'},
                {'q': 'write → форма -ing:', 'o': ['writeing', 'writing', 'writting', 'writeing'], 'a': 1, 'e': 'write → убираем e → writing.'},
                {'q': 'run → форма -ing:', 'o': ['runing', 'running', 'runeing', 'runned'], 'a': 1, 'e': 'run (CVC) → удвоение → running.'},
                {'q': '___ you listening to me?', 'o': ['Do', 'Are', 'Is', 'Am'], 'a': 1, 'e': 'You → Are you...?'},
                {'q': 'I ___ (not/watch) TV right now.', 'o': ["don't watch", "doesn't watch", "am not watching", "not watching"], 'a': 2, 'e': 'Сейчас → am not watching.'},
                {'q': 'Маркер Present Continuous:', 'o': ['always', 'every day', 'at the moment', 'usually'], 'a': 2, 'e': 'At the moment — маркер действия прямо сейчас.'},
                {'q': 'He usually *works* at home, but today he ___ in the office.', 'o': ['works', 'is working', 'work', 'working'], 'a': 1, 'e': 'Today (сейчас, исключение) → is working.'},
                {'q': 'swim → форма -ing:', 'o': ['swiming', 'swimming', 'swimeing', 'swimmed'], 'a': 1, 'e': 'swim (CVC) → удвоение → swimming.'},
            ],
            'test': [
                {'q': 'She ___ dinner now.', 'o': ['cooks', 'is cooking', 'are cooking', 'cooking'], 'a': 1},
                {'q': 'We ___ TV at the moment.', 'o': ['watch', 'watches', 'are watching', 'is watching'], 'a': 2},
                {'q': 'make → -ing форма:', 'o': ['makeing', 'making', 'makking', 'maked'], 'a': 1},
                {'q': '___ he sleeping?', 'o': ['Do', 'Does', 'Is', 'Are'], 'a': 2},
                {'q': 'I ___ at the moment. (работаю)', 'o': ["'m working", "'re working", "'s working", 'working'], 'a': 0},
                {'q': 'sit → -ing форма:', 'o': ['siting', 'sitting', 'siteing', 'sitted'], 'a': 1},
                {'q': 'Listen! Someone ___ at the door.', 'o': ['knock', 'knocks', 'is knocking', 'are knocking'], 'a': 2},
                {'q': 'They ___ not playing outside now.', 'o': ['is', 'are', 'do', 'does'], 'a': 1},
                {'q': 'What ___ you doing right now?', 'o': ['do', 'does', 'are', 'is'], 'a': 2},
                {'q': 'He usually drives, but today he ___ the bus.', 'o': ['take', 'takes', 'is taking', 'taking'], 'a': 2},
                {'q': 'The dog ___ in the garden right now.', 'o': ['run', 'runs', 'is running', 'are running'], 'a': 2},
                {'q': 'I ___ a book at the moment.', 'o': ["'m reading", "'re reading", "'s reading", 'read'], 'a': 0},
                {'q': '___ they having lunch?', 'o': ['Do', 'Does', 'Is', 'Are'], 'a': 3},
                {'q': 'dance → -ing форма:', 'o': ['danceing', 'dancing', 'danccing', 'danced'], 'a': 1},
                {'q': 'She ___ homework right now.', 'o': ['do', 'does', 'is doing', 'are doing'], 'a': 2},
            ]
        },
        {
            'id': 'a2_g3',
            'title': 'Past Simple — правильные глаголы',
            'icon': '⏮️',
            'explanation': (
                '📌 *Past Simple — Прошедшее простое время*\n'
                '*(правильные глаголы)*\n\n'
                'Используется для завершённых действий в прошлом.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '✅ *Утверждение — правильные глаголы + ED:*\n'
                '• work → work*ed* (I worked yesterday.)\n'
                '• live → liv*ed* (She lived in Paris.)\n'
                '• stop → stopp*ed* (He stopped the car.)\n'
                '• study → studi*ed* (We studied all night.)\n\n'
                '📌 *Правила добавления -ED:*\n'
                '• Обычно: + ed (work → worked)\n'
                '• Немое E: + d (live → lived, dance → danced)\n'
                '• CVC: удвоение согласной (stop → stopped)\n'
                '• Y после согласной → ied (study → studied)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                'did not (didn\'t) + глагол (base form)\n'
                '• I *didn\'t* work yesterday.\n'
                '• She *didn\'t* come to the party.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❓ *Вопрос:*\n'
                '*Did* + подлежащее + глагол (base form)?\n'
                '• *Did* you work yesterday?\n'
                '• *Did* she call you?\n'
                '— Yes, I did. / No, I didn\'t.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⏰ *Маркеры:*\n'
                'yesterday, last week/month/year, ago,\n'
                'in 2020, this morning (если день прошёл)'
            ),
            'exercises': [
                {'q': 'She ___ (work) yesterday.', 'o': ['work', 'works', 'worked', 'working'], 'a': 2, 'e': 'Past Simple: worked.'},
                {'q': 'I ___ (not/watch) TV last night.', 'o': ["didn't watch", "don't watch", "wasn't watch", "not watched"], 'a': 0, 'e': "didn't + base form: didn't watch."},
                {'q': '___ you call her yesterday?', 'o': ['Do', 'Did', 'Have', 'Were'], 'a': 1, 'e': 'Past Simple question: Did you...?'},
                {'q': 'stop → Past Simple:', 'o': ['stopted', 'stoped', 'stopped', 'stopt'], 'a': 2, 'e': 'stop (CVC) → doubled → stopped.'},
                {'q': 'study → Past Simple:', 'o': ['studyed', 'studiyed', 'studied', 'studyed'], 'a': 2, 'e': 'study (y после согласной) → studied.'},
                {'q': 'We ___ (visit) the museum last Saturday.', 'o': ['visit', 'visits', 'visited', 'visiting'], 'a': 2, 'e': 'Last Saturday → Past Simple: visited.'},
                {'q': 'She ___ (not/like) the film.', 'o': ["didn't like", "doesn't like", "not liked", "wasn't like"], 'a': 0, 'e': "didn't like."},
                {'q': 'Маркер Past Simple:', 'o': ['now', 'at the moment', 'last week', 'every day'], 'a': 2, 'e': 'Last week — маркер прошлого.'},
                {'q': '___ he finish his homework?', 'o': ['Do', 'Does', 'Did', 'Was'], 'a': 2, 'e': 'Past Simple question: Did...?'},
                {'q': 'dance → Past Simple:', 'o': ['danceed', 'dancing', 'danced', 'dancted'], 'a': 2, 'e': 'dance + d (немое е) = danced.'},
            ],
            'test': [
                {'q': 'They ___ football yesterday.', 'o': ['play', 'plays', 'played', 'playing'], 'a': 2},
                {'q': 'I ___ (not/go) to school yesterday.', 'o': ["didn't go", "don't go", "wasn't go", "not went"], 'a': 0},
                {'q': '___ she call you?', 'o': ['Do', 'Does', 'Did', 'Was'], 'a': 2},
                {'q': 'He ___ (arrive) late.', 'o': ['arrive', 'arrives', 'arrived', 'arriving'], 'a': 2},
                {'q': 'plan → Past Simple:', 'o': ['planed', 'planned', 'planied', 'planing'], 'a': 1},
                {'q': 'We ___ the party last night.', 'o': ['enjoy', 'enjoys', 'enjoyed', 'enjoying'], 'a': 2},
                {'q': 'try → Past Simple:', 'o': ['tryed', 'trys', 'tried', 'try'], 'a': 2},
                {'q': 'Маркер Past Simple:', 'o': ['tomorrow', 'now', 'in 2020', 'next year'], 'a': 2},
                {'q': '___ you enjoy the concert?', 'o': ['Do', 'Did', 'Have', 'Are'], 'a': 1},
                {'q': 'She ___ (not/finish) her homework.', 'o': ["didn't finish", "doesn't finish", "not finished", "wasn't finish"], 'a': 0},
                {'q': 'He ___ (watch) a film last night.', 'o': ['watch', 'watches', 'watched', 'watching'], 'a': 2},
                {'q': 'drop → Past Simple:', 'o': ['droped', 'dropted', 'dropped', 'droping'], 'a': 2},
                {'q': 'I ___ (clean) my room this morning.', 'o': ['clean', 'cleans', 'cleaned', 'cleaning'], 'a': 2},
                {'q': '___ they finish the project?', 'o': ['Do', 'Does', 'Did', 'Have'], 'a': 2},
                {'q': 'She ___ (live) in Paris for 2 years.', 'o': ['live', 'lives', 'lived', 'living'], 'a': 2},
            ]
        },
        {
            'id': 'a2_g4',
            'title': 'Past Simple — неправильные глаголы',
            'icon': '📚',
            'explanation': (
                '📌 *Past Simple — неправильные глаголы*\n\n'
                'Неправильные глаголы нужно учить наизусть!\n'
                'Они не подчиняются правилу +ED.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Самые важные неправильные глаголы:*\n\n'
                'go → *went* (идти)\n'
                'come → *came* (приходить)\n'
                'have → *had* (иметь)\n'
                'make → *made* (делать)\n'
                'take → *took* (брать)\n'
                'see → *saw* (видеть)\n'
                'give → *gave* (давать)\n'
                'get → *got* (получать)\n'
                'say → *said* (говорить)\n'
                'know → *knew* (знать)\n'
                'think → *thought* (думать)\n'
                'buy → *bought* (покупать)\n'
                'eat → *ate* (есть)\n'
                'drink → *drank* (пить)\n'
                'write → *wrote* (писать)\n'
                'read → *read* (читать — читается "рэд"!)\n'
                'sit → *sat* (сидеть)\n'
                'run → *ran* (бежать)\n'
                'speak → *spoke* (говорить)\n'
                'meet → *met* (встречать)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Важно:*\n'
                'В отрицании и вопросе — глагол возвращается в base form!\n'
                '• He went → He *didn\'t go* (НЕ didn\'t went!)\n'
                '• Did she *eat*? (НЕ Did she ate?)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Как учить:*\n'
                'go-went-gone\n'
                'Учи группами по 5-10 глаголов каждый день!'
            ),
            'exercises': [
                {'q': 'She ___ (go) to the cinema yesterday.', 'o': ['goed', 'goes', 'went', 'gone'], 'a': 2, 'e': 'go → went.'},
                {'q': 'I ___ (see) a great film last night.', 'o': ['seed', 'saw', 'seen', 'sees'], 'a': 1, 'e': 'see → saw.'},
                {'q': 'They ___ (eat) pizza for dinner.', 'o': ['eated', 'eaten', 'ate', 'eats'], 'a': 2, 'e': 'eat → ate.'},
                {'q': 'He ___ (not/go) to work yesterday.', 'o': ["didn't went", "didn't go", "doesn't go", "not went"], 'a': 1, 'e': "didn't + base form: didn't go (НЕ went!)."},
                {'q': '___ you (buy) anything at the market?', 'o': ['Did you buy', 'Did you bought', 'Do you buy', 'Have you bought'], 'a': 0, 'e': "Did you + base form: Did you buy?"},
                {'q': 'She ___ (write) a long email.', 'o': ['writed', 'written', 'wrote', 'writes'], 'a': 2, 'e': 'write → wrote.'},
                {'q': 'We ___ (meet) at the café.', 'o': ['meeted', 'meted', 'met', 'meets'], 'a': 2, 'e': 'meet → met.'},
                {'q': 'He ___ (speak) to his boss.', 'o': ['speaked', 'spoken', 'spoke', 'speaks'], 'a': 2, 'e': 'speak → spoke.'},
                {'q': 'read → Past Simple:', 'o': ['readed', 'red', 'read', 'reads'], 'a': 2, 'e': 'read → read (пишется одинаково, но произносится "рэд").'},
                {'q': 'think → Past Simple:', 'o': ['thinked', 'thinkt', 'thought', 'thinks'], 'a': 2, 'e': 'think → thought.'},
            ],
            'test': [
                {'q': 'I ___ (have) a great time at the party.', 'o': ['haved', 'has', 'had', 'have'], 'a': 2},
                {'q': 'She ___ (come) home late.', 'o': ['comed', 'came', 'comes', 'come'], 'a': 1},
                {'q': 'They ___ (drink) tea.', 'o': ['drinked', 'drunk', 'drank', 'drinks'], 'a': 2},
                {'q': '___ (not/take) the bus.', 'o': ["didn't took", "didn't take", "don't take", "not took"], 'a': 1},
                {'q': 'He ___ (give) me a gift.', 'o': ['gived', 'gave', 'given', 'gives'], 'a': 1},
                {'q': '___ she (know) the answer?', 'o': ['Did she knew', 'Did she know', 'Does she know', 'Do she know'], 'a': 1},
                {'q': 'We ___ (run) in the park.', 'o': ['runned', 'runs', 'ran', 'run'], 'a': 2},
                {'q': 'He ___ (buy) a new phone.', 'o': ['buyed', 'boughted', 'bought', 'buys'], 'a': 2},
                {'q': 'I ___ (get) a letter yesterday.', 'o': ['getted', 'gotten', 'got', 'gets'], 'a': 2},
                {'q': 'She ___ (make) a cake.', 'o': ['maked', 'makes', 'made', 'making'], 'a': 2},
                {'q': 'They ___ (sit) by the window.', 'o': ['sitted', 'seted', 'sat', 'sits'], 'a': 2},
                {'q': 'He ___ (say) nothing.', 'o': ['sayed', 'saied', 'said', 'says'], 'a': 2},
                {'q': '___ (not/see) her at the party.', 'o': ["didn't saw", "didn't see", "don't see", "not seen"], 'a': 1},
                {'q': 'She ___ (take) a taxi.', 'o': ['taked', 'taken', 'took', 'takes'], 'a': 2},
                {'q': 'We ___ (go) to the beach last summer.', 'o': ['goed', 'gone', 'went', 'goes'], 'a': 2},
            ]
        },
        {
            'id': 'a2_g5',
            'title': 'Будущее с "going to"',
            'icon': '🔮',
            'explanation': (
                '📌 *Going to — Планы и намерения*\n\n'
                '«Going to» используется для планов и намерений на будущее, а также для очевидных предсказаний.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Формула:*\n'
                'am/is/are + *going to* + глагол\n\n'
                '✅ *Утверждение:*\n'
                '• I *am going to* study tonight. — Я собираюсь учиться.\n'
                '• She *is going to* visit her parents. — Она планирует навестить родителей.\n'
                '• They *are going to* move to a new flat. — Они переезжают.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❌ *Отрицание:*\n'
                '• I *\'m not going to* go. — Я не собираюсь идти.\n'
                '• He *isn\'t going to* call. — Он не планирует звонить.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❓ *Вопрос:*\n'
                '• *Are you going to* cook dinner?\n'
                '• *Is she going to* come?\n'
                '— Yes, I am. / No, I\'m not.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *2 случая использования:*\n\n'
                '1. Планы и намерения:\n'
                'I\'m going to buy a car next year.\n'
                '(у меня есть такой план)\n\n'
                '2. Очевидные предсказания:\n'
                'Look at those clouds! It\'s going to rain.\n'
                '(вижу облака — очевидно, что будет дождь)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Разница с Will:*\n'
                '• going to = план уже есть\n'
                '• will = решение принято прямо сейчас'
            ),
            'exercises': [
                {'q': 'I ___ (study) medicine. (план)', 'o': ['am going to study', 'is going to study', 'will to study', 'going study'], 'a': 0, 'e': 'I + am going to + study.'},
                {'q': 'She ___ (visit) London next summer.', 'o': ['is going to visit', 'are going to visit', 'going to visits', 'will going to visit'], 'a': 0, 'e': 'She + is going to + visit.'},
                {'q': 'They ___ (not/come) to the party.', 'o': ["aren't going to come", "isn't going to come", "don't going to come", "not going to come"], 'a': 0, 'e': "They + aren't going to come."},
                {'q': '___ you (travel) this summer?', 'o': ['Are you going to travel', 'Is you going to travel', 'Do you going to travel', 'Will you going to travel'], 'a': 0, 'e': 'Are you going to...?'},
                {'q': 'Look at those clouds! It ___ rain.', 'o': ["'s going to", "'re going to", "'m going to", 'going to'], 'a': 0, 'e': "It + is going to → it's going to rain (очевидное предсказание)."},
                {'q': 'We ___ (buy) a new TV soon.', 'o': ['are going to buy', 'is going to buy', 'am going to buy', 'going to buy'], 'a': 0, 'e': 'We + are going to buy.'},
                {'q': 'He ___ (not/eat) meat anymore.', 'o': ["isn't going to eat", "aren't going to eat", "don't going to eat", "not going eat"], 'a': 0, 'e': "He + isn't going to eat."},
                {'q': '___ she (start) a new job?', 'o': ['Is she going to start', 'Are she going to start', 'Does she going to start', 'Will she going to start'], 'a': 0, 'e': 'Is she going to start?'},
                {'q': 'Ответ "Нет" на "Are you going to call?":', 'o': ["No, I'm not.", "No, I isn't.", "No, I don't.", "No, I won't."], 'a': 0, 'e': "Are you? → No, I'm not."},
                {'q': 'I feel sick. I think I ___ (be) ill.', 'o': ["'m going to be", "'re going to be", "'s going to be", 'going to be'], 'a': 0, 'e': "I + 'm going to be ill (очевидное предсказание)."},
            ],
            'test': [
                {'q': 'She ___ (learn) Spanish next year.', 'o': ['is going to learn', 'are going to learn', 'going to learns', 'will going learn'], 'a': 0},
                {'q': 'We ___ (have) a party on Friday.', 'o': ['are going to have', 'is going to have', 'am going to have', 'going to have'], 'a': 0},
                {'q': '___ (not/watch) the match tonight.', 'o': ["I'm not going to watch", "I'm not going watch", "I don't going to watch", "I isn't going to watch"], 'a': 0},
                {'q': '___ he (get) a new job?', 'o': ['Is he going to get', 'Are he going to get', 'Does he going to get', 'Do he going to get'], 'a': 0},
                {'q': 'She ___ (move) to a bigger flat.', 'o': ["is going to move", "are going to move", "going to moves", "is going move"], 'a': 0},
                {'q': 'They look tired. They ___ fall asleep.', 'o': ["are going to", "is going to", "am going to", "going to"], 'a': 0},
                {'q': 'I ___ (study) all weekend.', 'o': ["'m going to study", "'re going to study", "'s going to study", 'going study'], 'a': 0},
                {'q': 'He ___ (not/eat) spicy food.', 'o': ["isn't going to eat", "aren't going to eat", "don't going to eat", "not going eat"], 'a': 0},
                {'q': '___ you (visit) your parents?', 'o': ['Are you going to visit', 'Is you going to visit', 'Do you going to visit', 'Will you going visit'], 'a': 0},
                {'q': 'Ответ "Да" на "Is she going to come?":', 'o': ['Yes, she is.', 'Yes, she are.', 'Yes, she does.', 'Yes, she will.'], 'a': 0},
                {'q': 'We ___ (take) a holiday in July.', 'o': ['are going to take', 'is going to take', 'am going take', 'going to takes'], 'a': 0},
                {'q': 'It ___ (be) a great party!', 'o': ["'s going to be", "'re going to be", "'m going to be", 'going to be'], 'a': 0},
                {'q': '___ (not/go) to the gym today.', 'o': ["She isn't going to go", "She aren't going to go", "She don't going to go", "She not going go"], 'a': 0},
                {'q': 'I ___ (finish) this book today.', 'o': ["'m going to finish", "'re going to finish", "'s going to finish", 'going finish'], 'a': 0},
                {'q': 'They ___ (buy) a house.', 'o': ['are going to buy', 'is going to buy', 'am going to buy', 'going buy'], 'a': 0},
            ]
        },
        {
            'id': 'a2_g6',
            'title': 'Сравнительные прилагательные',
            'icon': '📊',
            'explanation': (
                '📌 *Сравнительные прилагательные (Comparatives)*\n\n'
                'Используются для сравнения двух предметов или людей.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Правила образования:*\n\n'
                '1️⃣ *Короткие прилагательные (1 слог) → + ER:*\n'
                '• fast → fast*er* (быстрее)\n'
                '• tall → tall*er* (выше)\n'
                '• old → old*er* (старше)\n'
                '• Если CVC: big → bigg*er*, hot → hott*er*\n'
                '• Если -e: nice → nic*er*, large → larg*er*\n'
                '• Если -y: happy → happ*ier*, easy → eas*ier*\n\n'
                '2️⃣ *Длинные прилагательные (2+ слога) → MORE +...:*\n'
                '• interesting → *more* interesting\n'
                '• expensive → *more* expensive\n'
                '• beautiful → *more* beautiful\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Неправильные формы:*\n'
                '• good → *better* (лучше)\n'
                '• bad → *worse* (хуже)\n'
                '• far → *further/farther* (дальше)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Структура с THAN:*\n'
                '• He is *taller than* me.\n'
                '• This film is *more interesting than* that one.\n'
                '• She is *better than* him at maths.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *AS...AS (так же...как):*\n'
                '• She is *as tall as* her brother.\n'
                '• It\'s *not as expensive as* I thought.'
            ),
            'exercises': [
                {'q': 'tall → сравнительная форма:', 'o': ['taller', 'more tall', 'tallier', 'most tall'], 'a': 0, 'e': 'Короткое прилагательное → + er: taller.'},
                {'q': 'interesting → сравнительная форма:', 'o': ['interestinger', 'more interesting', 'interestier', 'most interesting'], 'a': 1, 'e': 'Длинное прилагательное → more interesting.'},
                {'q': 'good → сравнительная форма:', 'o': ['gooder', 'more good', 'better', 'best'], 'a': 2, 'e': 'Исключение: good → better.'},
                {'q': 'hot → сравнительная форма:', 'o': ['hoter', 'hotter', 'more hot', 'hotier'], 'a': 1, 'e': 'hot (CVC) → удвоение → hotter.'},
                {'q': 'happy → сравнительная форма:', 'o': ['happyer', 'more happy', 'happier', 'happiest'], 'a': 2, 'e': 'happy (-y после согласной) → happier.'},
                {'q': 'Москва ___ (big) than Paris.', 'o': ['more big', 'bigger', 'biggest', 'biger'], 'a': 1, 'e': 'big (CVC) → bigger.'},
                {'q': 'bad → сравнительная форма:', 'o': ['badder', 'more bad', 'worse', 'worst'], 'a': 2, 'e': 'Исключение: bad → worse.'},
                {'q': 'This car is ___ (expensive) than that one.', 'o': ['expensiver', 'more expensive', 'most expensive', 'expensier'], 'a': 1, 'e': 'Длинное слово → more expensive.'},
                {'q': 'She is ___ (tall) as her sister. (одинаковые)', 'o': ['taller than', 'as tall as', 'more tall than', 'as taller as'], 'a': 1, 'e': 'Одинаковые → as tall as.'},
                {'q': 'large → сравнительная форма:', 'o': ['largeer', 'larger', 'more large', 'largier'], 'a': 1, 'e': 'large (немое е) → larger.'},
            ],
            'test': [
                {'q': 'old → сравнительная:', 'o': ['older', 'more old', 'elder', 'oldest'], 'a': 0},
                {'q': 'beautiful → сравнительная:', 'o': ['beautifuler', 'more beautiful', 'beautier', 'most beautiful'], 'a': 1},
                {'q': 'good → сравнительная:', 'o': ['gooder', 'more good', 'better', 'weller'], 'a': 2},
                {'q': 'This book is ___ (long) than that one.', 'o': ['more long', 'longer', 'longing', 'most long'], 'a': 1},
                {'q': 'My score is ___ (bad) than yours.', 'o': ['badder', 'more bad', 'worse', 'worst'], 'a': 2},
                {'q': 'thin → сравнительная:', 'o': ['thiner', 'thinner', 'more thin', 'thinest'], 'a': 1},
                {'q': 'This film is ___ (boring) than that one.', 'o': ['boringer', 'more boring', 'boringier', 'boriner'], 'a': 1},
                {'q': 'She runs ___ (fast) than him.', 'o': ['more fast', 'faster', 'fastest', 'fastest'], 'a': 1},
                {'q': 'He is ___ (good) at tennis than me.', 'o': ['gooder', 'more good', 'better', 'best'], 'a': 2},
                {'q': 'easy → сравнительная:', 'o': ['easyer', 'easier', 'more easy', 'easyer'], 'a': 1},
                {'q': 'This restaurant is ___ (expensive) than the other.', 'o': ['expensiver', 'more expensive', 'most expensive', 'expensiver'], 'a': 1},
                {'q': 'He is as ___ as his father. (tall)', 'o': ['taller', 'more tall', 'tall', 'tallest'], 'a': 2},
                {'q': 'far → сравнительная:', 'o': ['farer', 'farthest', 'further', 'farder'], 'a': 2},
                {'q': 'small → сравнительная:', 'o': ['smaler', 'smaller', 'more small', 'smallest'], 'a': 1},
                {'q': 'young → сравнительная:', 'o': ['younger', 'more young', 'younder', 'youngier'], 'a': 0},
            ]
        },
        {
            'id': 'a2_g7',
            'title': 'Превосходная степень прилагательных',
            'icon': '🏆',
            'explanation': (
                '📌 *Превосходная степень (Superlatives)*\n\n'
                'Используется для сравнения трёх и более предметов — выделяем самый лучший/худший.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Правила образования:*\n\n'
                '1️⃣ *Короткие прилагательные → THE + EST:*\n'
                '• fast → the fast*est*\n'
                '• tall → the tall*est*\n'
                '• CVC: big → the bigg*est*\n'
                '• -e: nice → the nic*est*\n'
                '• -y: happy → the happ*iest*\n\n'
                '2️⃣ *Длинные прилагательные → THE MOST:*\n'
                '• interesting → the *most* interesting\n'
                '• expensive → the *most* expensive\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Неправильные формы:*\n'
                '• good → the *best*\n'
                '• bad → the *worst*\n'
                '• far → the *furthest/farthest*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Примеры:*\n'
                '• He is *the tallest* in the class.\n'
                '• This is *the most expensive* restaurant.\n'
                '• She is *the best* student.\n'
                '• That was *the worst* film.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Сравнительная vs Превосходная:*\n'
                '• She is tall*er* than Anna. (сравниваем двух)\n'
                '• She is *the tallest* in class. (из всех)'
            ),
            'exercises': [
                {'q': 'tall → превосходная форма:', 'o': ['tallest', 'the tallest', 'most tall', 'the most tall'], 'a': 1, 'e': 'The tallest — с артиклем THE.'},
                {'q': 'interesting → превосходная форма:', 'o': ['interestingest', 'the interestingest', 'the most interesting', 'most interesting'], 'a': 2, 'e': 'The most interesting.'},
                {'q': 'good → превосходная форма:', 'o': ['the goodest', 'the most good', 'the best', 'the better'], 'a': 2, 'e': 'good → the best.'},
                {'q': 'He is ___ (old) person in the family.', 'o': ['older', 'the oldest', 'most old', 'the most old'], 'a': 1, 'e': 'The oldest (с артиклем THE).'},
                {'q': 'bad → превосходная форма:', 'o': ['the baddest', 'the most bad', 'the worst', 'the worse'], 'a': 2, 'e': 'bad → the worst.'},
                {'q': 'This is ___ (expensive) shop in the city.', 'o': ['expensiver', 'the expensivest', 'the most expensive', 'most expensive'], 'a': 2, 'e': 'The most expensive (длинное слово).'},
                {'q': 'hot → превосходная форма:', 'o': ['the hotest', 'the hottest', 'the most hot', 'hottest'], 'a': 1, 'e': 'hot (CVC) → the hottest.'},
                {'q': 'She is ___ (beautiful) girl I know.', 'o': ['the beautifulest', 'more beautiful', 'the most beautiful', 'most beautiful'], 'a': 2, 'e': 'The most beautiful.'},
                {'q': 'easy → превосходная форма:', 'o': ['the easiest', 'the most easy', 'the easyer', 'the easyest'], 'a': 0, 'e': 'easy → the easiest.'},
                {'q': 'This is ___ (good) pizza I\'ve ever eaten!', 'o': ['the better', 'the goodest', 'the best', 'the most good'], 'a': 2, 'e': 'good → the best.'},
            ],
            'test': [
                {'q': 'big → превосходная:', 'o': ['the bigest', 'the biggest', 'the most big', 'bigest'], 'a': 1},
                {'q': 'This is ___ (long) river in Russia.', 'o': ['longer', 'the longest', 'most long', 'the most long'], 'a': 1},
                {'q': 'bad → превосходная:', 'o': ['the baddest', 'the worst', 'the most bad', 'the worse'], 'a': 1},
                {'q': 'She is ___ (smart) student in class.', 'o': ['smarter', 'the smartest', 'the most smart', 'most smart'], 'a': 1},
                {'q': 'expensive → превосходная:', 'o': ['the expensivest', 'the most expensive', 'expensivest', 'most expensivest'], 'a': 1},
                {'q': 'good → превосходная:', 'o': ['the better', 'the goodest', 'the best', 'the most good'], 'a': 2},
                {'q': 'thin → превосходная:', 'o': ['the thinest', 'the thinnest', 'the most thin', 'thinnest'], 'a': 1},
                {'q': 'He is ___ (young) in the group.', 'o': ['younger', 'the youngest', 'most young', 'the most young'], 'a': 1},
                {'q': 'cold → превосходная:', 'o': ['the coldest', 'the most cold', 'coldest', 'colder'], 'a': 0},
                {'q': 'That was ___ (bad) day of my life.', 'o': ['the worse', 'the worst', 'the baddest', 'the most bad'], 'a': 1},
                {'q': 'happy → превосходная:', 'o': ['the happyest', 'the happiest', 'the most happy', 'happiest'], 'a': 1},
                {'q': 'old → превосходная:', 'o': ['the older', 'the eldest', 'the oldest', 'most old'], 'a': 2},
                {'q': 'This is ___ (interesting) book I\'ve read.', 'o': ['interestinger', 'the interestingest', 'the most interesting', 'more interesting'], 'a': 2},
                {'q': 'far → превосходная:', 'o': ['the farthest', 'the further', 'the farer', 'the farder'], 'a': 0},
                {'q': 'small → превосходная:', 'o': ['the smaler', 'the smallest', 'the most small', 'smallest'], 'a': 1},
            ]
        },
        {
            'id': 'a2_g8',
            'title': 'Модальные глаголы: can / can\'t',
            'icon': '💪',
            'explanation': (
                '📌 *Can / Can\'t — умение, возможность, разрешение*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Can используется для:*\n\n'
                '1️⃣ *Умение/способность:*\n'
                '• I *can* swim. — Я умею плавать.\n'
                '• She *can* speak three languages. — Она говорит на трёх языках.\n'
                '• He *can\'t* drive. — Он не умеет водить.\n\n'
                '2️⃣ *Возможность:*\n'
                '• We *can* meet tomorrow. — Мы можем встретиться завтра.\n'
                '• I *can\'t* come today. — Я не могу прийти сегодня.\n\n'
                '3️⃣ *Разрешение (неформально):*\n'
                '• *Can* I use your pen? — Можно использовать твою ручку?\n'
                '• You *can* sit here. — Ты можешь (разрешаю) сидеть здесь.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Структура:*\n'
                '• can + глагол (base form) — БЕЗ изменений!\n'
                '• She *can* swim. (НЕ she cans swim!)\n'
                '• He *can\'t* cook. (НЕ he can\'ts!)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '❓ *Вопрос:*\n'
                '• *Can* you help me?\n'
                '• *Can* she drive?\n'
                '— Yes, I can. / No, I can\'t.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Could — вежливая форма:*\n'
                '• *Could* you help me, please? (более вежливо)\n'
                '• *Could* I have a coffee? (вежливая просьба)'
            ),
            'exercises': [
                {'q': 'She ___ swim very well.', 'o': ['cans', 'can', 'can to', 'is can'], 'a': 1, 'e': "Can не изменяется: she can (НЕ cans!)."},
                {'q': 'He ___ drive. (не умеет)', 'o': ["can't", "cans't", "doesn't can", "not can"], 'a': 0, 'e': "can't = cannot."},
                {'q': '___ you speak English?', 'o': ['Do', 'Are', 'Can', 'Have'], 'a': 2, 'e': 'Can you...? — вопрос об умении.'},
                {'q': 'I ___ speak French, but I ___ speak German.', 'o': ["can / can't", "can't / can", "cans / can't", "can / cannot's"], 'a': 0, 'e': "Умею французский, не умею немецкий: can / can't."},
                {'q': 'Правильная структура с CAN:', 'o': ['She can to swim.', 'She cans swim.', 'She can swim.', 'She can swimming.'], 'a': 2, 'e': 'Can + base form (без to, без s): she can swim.'},
                {'q': '___ I sit here? (вежливо)', 'o': ['Can', 'Could', 'Should', 'Must'], 'a': 1, 'e': 'Could — более вежливая форма разрешения.'},
                {'q': 'Ответ "Да" на "Can he cook?":', 'o': ['Yes, he can.', 'Yes, he cans.', 'Yes, he could.', 'Yes, he does.'], 'a': 0, 'e': 'Yes, he can.'},
                {'q': 'Birds ___ fly.', 'o': ['can to', 'cans', 'can', 'are can'], 'a': 2, 'e': 'Birds can fly (способность).'},
                {'q': '"Я не могу прийти" → I ___ come.', 'o': ["can't", "cans't", "don't can", "am not can"], 'a': 0, 'e': "I can't come."},
                {'q': 'Babies ___ walk. (не умеют)', 'o': ["can't", "cans't", "don't can", "not can"], 'a': 0, 'e': "Babies can't walk."},
            ],
            'test': [
                {'q': 'She ___ play the piano.', 'o': ['cans', 'can', 'can to', 'is can'], 'a': 1},
                {'q': 'He ___ cook. (умеет)', 'o': ['can', 'can to', 'cans', 'is able'], 'a': 0},
                {'q': '___ you help me, please?', 'o': ['Do', 'Are', 'Can', 'Have'], 'a': 2},
                {'q': 'I ___ find my keys. (не могу)', 'o': ["can't find", "don't can find", "can not to find", "cann't find"], 'a': 0},
                {'q': 'Правильное предложение:', 'o': ['She cans sing.', 'She can sings.', 'She can sing.', 'She can to sing.'], 'a': 2},
                {'q': 'Fish ___ live in water.', 'o': ['can to', 'cans', 'can', 'are can'], 'a': 2},
                {'q': 'Ответ "Нет" на "Can she drive?":', 'o': ["No, she can't.", "No, she cans't.", "No, she doesn't.", "No, she couldn't."], 'a': 0},
                {'q': '___ I open the window?', 'o': ['Do', 'Should', 'Can', 'Must'], 'a': 2},
                {'q': 'He ___ read when he was 4.', 'o': ['can', 'could', 'cans', 'is able to'], 'a': 1},
                {'q': 'We ___ hear you. (не слышим)', 'o': ["can't hear", "don't can hear", "can not to hear", "cans't hear"], 'a': 0},
                {'q': '"Можно мне стакан воды?" → ___ I have a glass of water?', 'o': ['Could', 'Should', 'Must', 'Will'], 'a': 0},
                {'q': 'She ___ speak 4 languages.', 'o': ['cans', 'can to', 'can', 'is can'], 'a': 2},
                {'q': 'Dogs ___ fly.', 'o': ["can", "can't", "cans", "don't can"], 'a': 1},
                {'q': 'Ответ "Да" на "Can you swim?":', 'o': ['Yes, I can.', 'Yes, I can to.', 'Yes, I do.', 'Yes, I could.'], 'a': 0},
                {'q': '"Он умеет петь" → He ___ sing.', 'o': ['cans', 'can to', 'can', 'could to'], 'a': 2},
            ]
        },
    ],
    'vocabulary': [
        {
            'category': 'Работа и профессии',
            'icon': '💼',
            'words': [
                {'en': 'doctor', 'ru': 'врач', 'ex': 'She is a doctor.'},
                {'en': 'teacher', 'ru': 'учитель', 'ex': 'He is a good teacher.'},
                {'en': 'engineer', 'ru': 'инженер', 'ex': 'My father is an engineer.'},
                {'en': 'manager', 'ru': 'менеджер', 'ex': 'She works as a manager.'},
                {'en': 'nurse', 'ru': 'медсестра/медбрат', 'ex': 'The nurse helps patients.'},
                {'en': 'driver', 'ru': 'водитель', 'ex': 'He is a bus driver.'},
                {'en': 'chef', 'ru': 'повар', 'ex': 'The chef cooks amazing food.'},
                {'en': 'journalist', 'ru': 'журналист', 'ex': 'She is a journalist.'},
                {'en': 'lawyer', 'ru': 'юрист/адвокат', 'ex': 'I need a good lawyer.'},
                {'en': 'student', 'ru': 'студент', 'ex': 'I am a student.'},
            ]
        },
        {
            'category': 'Транспорт',
            'icon': '🚗',
            'words': [
                {'en': 'car', 'ru': 'машина', 'ex': 'I drive a car.'},
                {'en': 'bus', 'ru': 'автобус', 'ex': 'I take the bus to school.'},
                {'en': 'train', 'ru': 'поезд', 'ex': 'The train is fast.'},
                {'en': 'plane', 'ru': 'самолёт', 'ex': 'We flew by plane.'},
                {'en': 'taxi', 'ru': 'такси', 'ex': 'I took a taxi home.'},
                {'en': 'bicycle', 'ru': 'велосипед', 'ex': 'She rides a bicycle.'},
                {'en': 'metro / subway', 'ru': 'метро', 'ex': 'The metro is underground.'},
                {'en': 'boat', 'ru': 'лодка/корабль', 'ex': 'We sailed on a boat.'},
                {'en': 'tram', 'ru': 'трамвай', 'ex': 'The tram goes through the city.'},
                {'en': 'motorcycle', 'ru': 'мотоцикл', 'ex': 'He rides a motorcycle.'},
            ]
        },
        {
            'category': 'Погода',
            'icon': '🌤️',
            'words': [
                {'en': 'sunny', 'ru': 'солнечный', 'ex': "It's sunny today."},
                {'en': 'cloudy', 'ru': 'облачный', 'ex': "It's very cloudy."},
                {'en': 'rainy', 'ru': 'дождливый', 'ex': 'I hate rainy days.'},
                {'en': 'snowy', 'ru': 'снежный', 'ex': 'It was a snowy winter.'},
                {'en': 'windy', 'ru': 'ветреный', 'ex': "It's too windy outside."},
                {'en': 'cold', 'ru': 'холодный', 'ex': "It's cold in winter."},
                {'en': 'hot', 'ru': 'жаркий', 'ex': "It's very hot in summer."},
                {'en': 'warm', 'ru': 'тёплый', 'ex': 'It\'s warm in spring.'},
                {'en': 'thunder', 'ru': 'гром', 'ex': 'I hear thunder.'},
                {'en': 'fog', 'ru': 'туман', 'ex': 'There is a thick fog.'},
            ]
        },
        {
            'category': 'Одежда',
            'icon': '👕',
            'words': [
                {'en': 'shirt', 'ru': 'рубашка', 'ex': 'He wears a white shirt.'},
                {'en': 'trousers / pants', 'ru': 'брюки', 'ex': 'These trousers are too long.'},
                {'en': 'dress', 'ru': 'платье', 'ex': 'She wore a beautiful dress.'},
                {'en': 'jacket', 'ru': 'куртка/пиджак', 'ex': 'Put on your jacket.'},
                {'en': 'shoes', 'ru': 'туфли/ботинки', 'ex': 'I need new shoes.'},
                {'en': 'socks', 'ru': 'носки', 'ex': 'Where are my socks?'},
                {'en': 'hat', 'ru': 'шляпа/шапка', 'ex': 'Wear a hat in winter.'},
                {'en': 'coat', 'ru': 'пальто', 'ex': 'It\'s cold, wear your coat.'},
                {'en': 'sweater / jumper', 'ru': 'свитер', 'ex': 'This sweater is very warm.'},
                {'en': 'jeans', 'ru': 'джинсы', 'ex': 'She always wears jeans.'},
            ]
        },
        {
            'category': 'Город и места',
            'icon': '🏙️',
            'words': [
                {'en': 'bank', 'ru': 'банк', 'ex': 'I need to go to the bank.'},
                {'en': 'hospital', 'ru': 'больница', 'ex': 'The hospital is on Main Street.'},
                {'en': 'supermarket', 'ru': 'супермаркет', 'ex': 'I shop at the supermarket.'},
                {'en': 'school', 'ru': 'школа', 'ex': 'Children go to school.'},
                {'en': 'park', 'ru': 'парк', 'ex': 'We walk in the park.'},
                {'en': 'restaurant', 'ru': 'ресторан', 'ex': 'Let\'s go to a restaurant.'},
                {'en': 'café', 'ru': 'кафе', 'ex': 'I like this café.'},
                {'en': 'library', 'ru': 'библиотека', 'ex': 'I study at the library.'},
                {'en': 'post office', 'ru': 'почта', 'ex': 'I sent a letter from the post office.'},
                {'en': 'pharmacy', 'ru': 'аптека', 'ex': 'Buy medicine at the pharmacy.'},
            ]
        },
    ],
    'phrases': [
        {
            'situation': 'В ресторане',
            'icon': '🍽️',
            'items': [
                {'en': "I'd like a table for two.", 'ru': 'Я бы хотел столик на двоих.', 'note': 'Заказать столик'},
                {'en': 'Can I see the menu?', 'ru': 'Можно меню?', 'note': 'Попросить меню'},
                {'en': "I'll have the chicken, please.", 'ru': 'Я возьму курицу, пожалуйста.', 'note': 'Сделать заказ'},
                {'en': 'Could I have the bill, please?', 'ru': 'Счёт, пожалуйста.', 'note': 'Попросить счёт'},
                {'en': 'Is service included?', 'ru': 'Обслуживание включено?', 'note': 'Про чаевые'},
                {'en': 'This is delicious!', 'ru': 'Это очень вкусно!', 'note': 'Похвалить еду'},
            ]
        },
        {
            'situation': 'Направления и дорога',
            'icon': '🗺️',
            'items': [
                {'en': 'Excuse me, how do I get to...?', 'ru': 'Простите, как добраться до...?', 'note': 'Спросить дорогу'},
                {'en': 'Turn left at the traffic lights.', 'ru': 'Поверните налево на светофоре.', 'note': 'Указать направление'},
                {'en': "It's on the right.", 'ru': 'Это справа.', 'note': 'Указать сторону'},
                {'en': "It's about 5 minutes on foot.", 'ru': 'Около 5 минут пешком.', 'note': 'Расстояние'},
                {'en': "You can't miss it.", 'ru': 'Вы не пропустите.', 'note': 'Легко найти'},
                {'en': 'Is it far from here?', 'ru': 'Это далеко отсюда?', 'note': 'Спросить расстояние'},
            ]
        },
        {
            'situation': 'Покупки',
            'icon': '🛍️',
            'items': [
                {'en': "I'm just looking, thanks.", 'ru': 'Я просто смотрю, спасибо.', 'note': 'Когда не нужна помощь'},
                {'en': 'Do you have this in a bigger size?', 'ru': 'У вас есть это большего размера?', 'note': 'Спросить размер'},
                {'en': 'Can I try it on?', 'ru': 'Можно примерить?', 'note': 'Примерочная'},
                {'en': "I'll take it.", 'ru': 'Я возьму это.', 'note': 'Купить товар'},
                {'en': 'Is there a discount?', 'ru': 'Есть скидка?', 'note': 'Спросить о скидке'},
                {'en': 'Can I pay by card?', 'ru': 'Можно оплатить картой?', 'note': 'Способ оплаты'},
            ]
        },
        {
            'situation': 'Телефонный разговор',
            'icon': '📞',
            'items': [
                {'en': 'Hello, can I speak to...?', 'ru': 'Здравствуйте, могу я поговорить с...?', 'note': 'Начало звонка'},
                {'en': "Speaking. / That's me.", 'ru': 'Это я. / Слушаю.', 'note': 'Ответ "это я"'},
                {'en': 'Could you call back later?', 'ru': 'Вы можете перезвонить позже?', 'note': 'Если занят'},
                {'en': "I'll leave a message.", 'ru': 'Я оставлю сообщение.', 'note': 'Оставить сообщение'},
                {'en': "I can't hear you very well.", 'ru': 'Я плохо вас слышу.', 'note': 'Плохая связь'},
                {'en': 'Thank you for calling. Goodbye!', 'ru': 'Спасибо за звонок. До свидания!', 'note': 'Завершение звонка'},
            ]
        },
        {
            'situation': 'Выражение мнения',
            'icon': '💭',
            'items': [
                {'en': 'I think...', 'ru': 'Я думаю, что...', 'note': 'Выразить мнение'},
                {'en': 'In my opinion...', 'ru': 'По моему мнению...', 'note': 'Формальное мнение'},
                {'en': 'I agree with you.', 'ru': 'Я с тобой согласен/согласна.', 'note': 'Согласие'},
                {'en': "I don't agree.", 'ru': 'Я не согласен/согласна.', 'note': 'Несогласие'},
                {'en': "That's a good idea!", 'ru': 'Это хорошая идея!', 'note': 'Одобрение'},
                {'en': "I'm not sure about that.", 'ru': 'Я не уверен/уверена в этом.', 'note': 'Сомнение'},
            ]
        },
    ]
}
