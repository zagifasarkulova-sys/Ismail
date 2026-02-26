C1 = {
    'name': 'C1 — Продвинутый',
    'emoji': '⭐',
    'description': (
        '⭐ *Уровень C1 — Продвинутый*\n\n'
        'Ты свободно общаешься и понимаешь сложные тексты.\n'
        'На этом уровне изучаем:\n'
        '• Сложные риторические конструкции\n'
        '• Инверсия и эллипсис\n'
        '• Модальные перфекты\n'
        '• Причастные и именные обороты\n'
        '• Дискурсивные маркеры\n\n'
        'Выбери раздел:'
    ),
    'grammar': [
        {
            'id': 'c1_g1',
            'title': 'Инверсия (Inversion)',
            'icon': '🔄',
            'explanation': (
                '📌 *Инверсия (Inversion) — Обратный порядок слов*\n\n'
                'Инверсия — перестановка подлежащего и вспомогательного глагола для усиления или в формальном стиле.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Типы инверсии:*\n\n'
                '1️⃣ *После отрицательных наречий:*\n'
                '• *Never* have I seen such beauty.\n'
                '• *Rarely* do we get such opportunities.\n'
                '• *Seldom* had he felt so happy.\n'
                '• *Not once* did she complain.\n\n'
                '2️⃣ *После "only":*\n'
                '• *Only then* did I understand.\n'
                '• *Only after reading* the book did she understand.\n'
                '• *Only by working* hard will you succeed.\n\n'
                '3️⃣ *После "no sooner...than" и "hardly...when":*\n'
                '• *No sooner* had I arrived *than* it started raining.\n'
                '• *Hardly* had she left *when* he called.\n\n'
                '4️⃣ *В условных предложениях (формально):*\n'
                '• *Should* you need help, call me. (= If you should need)\n'
                '• *Were* she to arrive, call me. (= If she were to arrive)\n'
                '• *Had* I known, I would have told you. (= If I had known)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Важно:*\n'
                'После отрицательных наречий в начале предложения ВСЕГДА инверсия!'
            ),
            'exercises': [
                {'q': '"I have never seen such a film." → Инверсия:', 'o': ['Never I have seen such a film.', 'Never have I seen such a film.', 'Have never I seen such a film.', 'Never seen have I such a film.'], 'a': 1, 'e': 'Never + вспомогательный + подлежащее: Never have I seen.'},
                {'q': '"Rarely ___ we have such luck." (do/does/have)', 'o': ['do', 'does', 'have', 'did'], 'a': 0, 'e': 'Rarely + do we (Present Simple инверсия).'},
                {'q': '"Only then ___ I understand." (do/did)', 'o': ['do', 'does', 'did', 'have'], 'a': 2, 'e': 'Only then + did I understand (Past Simple).'},
                {'q': 'Conditional без IF: "Should you need help, ___"', 'o': ['call me.', 'you call me.', 'I call you.', 'calling me.'], 'a': 0, 'e': 'Should you need help = If you should need help → call me.'},
                {'q': '"___ had she left when the phone rang." (No sooner/Hardly)', 'o': ['No sooner', 'Hardly', 'Seldom', 'Never'], 'a': 1, 'e': 'Hardly had she left when... (Hardly...when).'},
                {'q': '"Seldom ___ he complain." (do/does/did)', 'o': ['do', 'does', 'did', 'have'], 'a': 1, 'e': 'Seldom + does he (3-е лицо, Present Simple).'},
                {'q': 'Conditional без IF (Past Perfect):', 'o': ['If I had known → Had I known', 'If I knew → Had I known', 'If I know → Have I known', 'If I would know → Had I known'], 'a': 0, 'e': 'Had I known = If I had known.'},
                {'q': '"Not once ___ she apologise." (формально)', 'o': ['she did', 'did she', 'she has', 'has she'], 'a': 1, 'e': 'Not once + вспомогательный + подлежащее: did she.'},
                {'q': '"No sooner ___ I arrived than it rained."', 'o': ['have', 'had', 'has', 'did'], 'a': 1, 'e': 'No sooner + had I arrived (Past Perfect инверсия).'},
                {'q': 'Когда используется инверсия?', 'o': ['Всегда в вопросах', 'После отрицательных наречий в начале, в формальных условных', 'Только в поэзии', 'В любом предложении для красоты'], 'a': 1, 'e': 'Инверсия — после отрицательных наречий и в формальных условных.'},
            ],
            'test': [
                {'q': '"Never ___ I felt so embarrassed." (have/did)', 'o': ['have', 'had', 'did', 'do'], 'a': 0},
                {'q': '"Only after leaving ___ I realise my mistake."', 'o': ['I did', 'did I', 'have I', 'I have'], 'a': 1},
                {'q': '"___ you have any questions, please ask." (Should/Were)', 'o': ['Should', 'Were', 'Had', 'Have'], 'a': 0},
                {'q': '"Hardly ___ we sat down when the alarm went off."', 'o': ['we had', 'had we', 'we have', 'have we'], 'a': 1},
                {'q': '"Not until midnight ___ he arrive."', 'o': ['he did', 'did he', 'he has', 'has he'], 'a': 1},
                {'q': 'Formal conditional без IF: "If she were to ask..."', 'o': ['Should she ask', 'Were she to ask', 'Had she asked', 'Will she ask'], 'a': 1},
                {'q': '"No sooner ___ they arrived than problems started."', 'o': ['they had', 'had they', 'they have', 'have they'], 'a': 1},
                {'q': '"Seldom ___ such a talented student."', 'o': ['we see', 'do we see', 'we have seen', 'have seen we'], 'a': 1},
                {'q': '"___ I known, I would have told you." (Had/Were)', 'o': ['Had', 'Were', 'Should', 'Have'], 'a': 0},
                {'q': '"Rarely ___ such events occur."', 'o': ['such', 'do', 'they', 'events'], 'a': 1},
                {'q': '"Not only ___ he rude, but also arrogant."', 'o': ['was he', 'he was', 'is he', 'he is'], 'a': 0},
                {'q': '"Little ___ they know what was happening."', 'o': ['they did', 'did they', 'they have', 'have they'], 'a': 1},
                {'q': '"Under no circumstances ___ you do that!"', 'o': ['you should', 'should you', 'you must', 'must you'], 'a': 1},
                {'q': '"Only when she smiled ___ I recognise her."', 'o': ['I did', 'did I', 'I had', 'had I'], 'a': 1},
                {'q': '"___ you need assistance, the staff are here." (Should/Were)', 'o': ['Should', 'Were', 'Had', 'If'], 'a': 0},
            ]
        },
        {
            'id': 'c1_g2',
            'title': 'Cleft Sentences (Расщеплённые предложения)',
            'icon': '✂️',
            'explanation': (
                '📌 *Cleft Sentences — Расщеплённые предложения*\n\n'
                'Используются для выделения/подчёркивания определённой части предложения.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *It is/was... who/that:*\n\n'
                '• Normal: John broke the window.\n'
                '• Cleft (John): *It was John who* broke the window.\n'
                '• Cleft (window): *It was the window that* John broke.\n'
                '• Cleft (yesterday): *It was yesterday that* it happened.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *What-cleft (Pseudo-cleft):*\n\n'
                '• *What I need is* a cup of tea.\n'
                '• *What surprised me was* his reaction.\n'
                '• *What we need to do is* act quickly.\n'
                '• *What happened was that* she resigned.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '3️⃣ *All (that)... is/was:*\n\n'
                '• *All I want is* peace and quiet.\n'
                '• *All she did was* cry.\n'
                '• *All we need is* a little patience.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Зачем использовать?*\n'
                'Для усиления важности одного элемента в предложении.\n'
                'Часто используется в речи и формальных текстах.'
            ),
            'exercises': [
                {'q': '"Tom called me." → Выделить Tom:', 'o': ['It called Tom who me.', 'It was Tom who called me.', 'Tom it was who called me.', 'Was it Tom who called me.'], 'a': 1, 'e': 'It was Tom who called me.'},
                {'q': '"What ___ is a good rest." (I/need)', 'o': ['What I need', 'What need I', 'What I needs', 'What do I need'], 'a': 0, 'e': 'What I need is... (what-cleft).'},
                {'q': '"All ___ want is to be left alone." (she)', 'o': ['All what she', 'All she', 'She all', 'What all she'], 'a': 1, 'e': 'All she wants is...'},
                {'q': '"It was in Paris ___ they first met." (where/that)', 'o': ['where', 'which', 'that', 'when'], 'a': 2, 'e': 'It was... that (for places без where в cleft).'},
                {'q': '"She left her job." → Cleft, выделяем JOB:', 'o': ['It was her job that she left.', 'It was she who left her job.', 'What she left was her job.', 'Оба A и C правильны'], 'a': 3, 'e': 'Можно использовать оба варианта: It was her job that... OR What she left was...'},
                {'q': '"What happened was ___ the pipe burst."', 'o': ['what', 'that', 'when', 'which'], 'a': 1, 'e': 'What happened was that...'},
                {'q': '"It ___ John who told her." (was/is)', 'o': ['is', 'was', 'has been', 'were'], 'a': 1, 'e': 'Прошедшее действие → It was John who...'},
                {'q': '"All we ___ do is wait."', 'o': ['can', 'could', 'need to', 'have to'], 'a': 0, 'e': 'All we can do is wait.'},
                {'q': 'Цель cleft sentences:', 'o': ['Сделать предложение короче', 'Выделить/подчеркнуть определённую часть', 'Сделать текст неформальным', 'Избежать пассивного залога'], 'a': 1, 'e': 'Cleft = для выделения (emphasis).'},
                {'q': '"What surprised me ___ her confidence." (was/were)', 'o': ['were', 'was', 'is', 'are'], 'a': 1, 'e': 'What surprised me WAS...'},
            ],
            'test': [
                {'q': '"Anna wrote this." → Выделить Anna:', 'o': ['It is Anna who writes this.', 'It was Anna who wrote this.', 'Anna it was who wrote this.', 'Was it Anna who wrote this?'], 'a': 1},
                {'q': '"What ___ is your support." (I/want)', 'o': ['What want I', 'What I wants', 'What I want', 'What do I want'], 'a': 2},
                {'q': '"It was Monday ___ the accident happened." (when/that)', 'o': ['when', 'which', 'that', 'where'], 'a': 2},
                {'q': '"All ___ did was apologise."', 'o': ['what he', 'he', 'that he', 'him'], 'a': 1},
                {'q': '"What we need to do ___ plan carefully." (is/are)', 'o': ['are', 'were', 'is', 'have'], 'a': 2},
                {'q': '"It was the noise ___ woke me up."', 'o': ['what', 'who', 'that', 'where'], 'a': 2},
                {'q': '"What ___ was his resignation." (shocked everyone)', 'o': ['shocked everyone was', 'everyone shocked was', 'shocked everyone', 'What shocked everyone was'], 'a': 3},
                {'q': '"All she ___ is smile." (do)', 'o': ['can do', 'could', 'does', 'has'], 'a': 0},
                {'q': '"It ___ the cold that made him ill."', 'o': ['is', 'was', 'has been', 'were'], 'a': 1},
                {'q': '"What I love ___ the smell of coffee."', 'o': ['are', 'am', 'is', 'were'], 'a': 2},
                {'q': '"It ___ Shakespeare who wrote Hamlet."', 'o': ['is', 'was', 'has been', 'were'], 'a': 1},
                {'q': '"___ we did was try our best."', 'o': ['What', 'All that', 'All', 'All что'], 'a': 2},
                {'q': '"What happened ___ that the deal fell through."', 'o': ['is', 'was', 'were', 'has been'], 'a': 1},
                {'q': '"It was in the library ___ I found the book."', 'o': ['where', 'which', 'that', 'when'], 'a': 2},
                {'q': '"All ___ now is get some sleep."', 'o': ['I want', 'what I want', 'I needs', 'that I want'], 'a': 0},
            ]
        },
        {
            'id': 'c1_g3',
            'title': 'Modal Perfects (модальные перфекты)',
            'icon': '🎯',
            'explanation': (
                '📌 *Modal Perfects — Модальные глаголы + have + PP*\n\n'
                'Используются для суждений и предположений о ПРОШЛОМ.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Значения:*\n\n'
                '• *must have + PP* — Почти уверен (логический вывод о прошлом)\n'
                '  She *must have forgotten*. (наверняка забыла)\n\n'
                '• *can\'t/couldn\'t have + PP* — Уверен, что НЕТ\n'
                '  He *can\'t have done* it. (не мог этого сделать)\n\n'
                '• *might/may/could have + PP* — Возможно (слабая уверенность)\n'
                '  She *might have missed* the bus. (возможно опоздала)\n\n'
                '• *should have + PP* — Должен был, но не сделал (упрёк)\n'
                '  You *should have called* me! (надо было позвонить!)\n\n'
                '• *shouldn\'t have + PP* — Не должен был, но сделал\n'
                '  I *shouldn\'t have eaten* so much. (зря столько съел)\n\n'
                '• *would have + PP* — Сделал бы (условное прошлое)\n'
                '  I *would have helped* if I had known.\n\n'
                '• *needn\'t have + PP* — Сделал, но не нужно было\n'
                '  You *needn\'t have bought* flowers. (зря купил)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📊 *Шкала уверенности о прошлом:*\n'
                'must have (95%) > should have > might have (40%) > can\'t have (0%)'
            ),
            'exercises': [
                {'q': 'She was late. She ___ missed the bus.', 'o': ['must have', 'can\'t have', 'should have', 'needn\'t have'], 'a': 0, 'e': 'Логический вывод о прошлом: must have missed.'},
                {'q': 'He studied all night. He ___ passed easily.', 'o': ["must have", "can't have", "should have", "might have"], 'a': 0, 'e': "Почти уверен → must have passed."},
                {'q': 'You ___ told me earlier! (упрёк)', 'o': ['must have', "can't have", 'should have', "needn't have"], 'a': 2, 'e': "Упрёк (должен был) → should have told."},
                {'q': 'I ___ eaten so much — I feel ill. (зря)', 'o': ["should have", "shouldn't have", "must have", "can't have"], 'a': 1, 'e': "Не нужно было → shouldn't have eaten."},
                {'q': 'It ___ been him — he was in Paris at the time!', 'o': ["must have", "should have", "can't have", "would have"], 'a': 2, 'e': "Уверен, что НЕТ → can't have been."},
                {'q': 'She ___ left already — her car is gone.', 'o': ["must have", "can't have", "needn't have", "would have"], 'a': 0, 'e': "Логический вывод → must have left."},
                {'q': 'You ___ waited — I wasn\'t going to be long. (зря ждал)', 'o': ["should have", "must have", "needn't have", "can't have"], 'a': 2, 'e': "Needn't have waited = ждал, но не нужно было."},
                {'q': '"Она могла потерять ключи" (возможно):', 'o': ['She must have lost her keys.', 'She might have lost her keys.', "She can't have lost her keys.", 'She should have lost her keys.'], 'a': 1, 'e': "Возможно → might have lost."},
                {'q': 'Разница should have vs needn\'t have:', 'o': ['Нет разницы', "Should have = не сделал (но нужно было), needn't have = сделал (но не нужно)", "Should have = сделал, needn't have = не сделал", "Оба выражают сожаление об одном"], 'a': 1, 'e': "should have = должен был, но не сделал; needn't have = не нужно было, но сделал."},
                {'q': '"I would have helped if I had known." означает:', 'o': ['Я помог и знал', 'Я бы помог, если бы знал (но не знал → не помог)', 'Я должен был помочь', 'Я мог бы помочь сейчас'], 'a': 1, 'e': "Would have = нереальное прошлое (3-й тип условных)."},
            ],
            'test': [
                {'q': 'The lights are on — she ___ be home.', 'o': ['must have', 'should have', 'can\'t have', 'might have'], 'a': 0},
                {'q': 'I ___ told you earlier. Sorry! (нужно было)', 'o': ["must have", "can't have", "should have", "needn't have"], 'a': 2},
                {'q': 'He ___ done it — he was with me all day!', 'o': ["must have", "should have", "can't have", "might have"], 'a': 2},
                {'q': 'She ___ left — her coat is still here.', 'o': ["must have", "can't have", "should have", "would have"], 'a': 1},
                {'q': 'You ___ bought so much — we already had plenty.', 'o': ["should have", "must have", "needn't have", "can't have"], 'a': 2},
                {'q': 'I ___ been more careful. (зря не был)', 'o': ["must have", "should have", "can't have", "needn't have"], 'a': 1},
                {'q': '"Она, возможно, слышала" = She ___ heard.', 'o': ["must have", "can't have", "might have", "should have"], 'a': 2},
                {'q': 'He ___ passed — he failed the test 5 times!', 'o': ["must have", "should have", "can't have", "would have"], 'a': 2},
                {'q': '"I should have called" означает:', 'o': ['Я позвонил', 'Я не должен был звонить', 'Нужно было позвонить, но не позвонил', 'Я позвоню'], 'a': 2},
                {'q': '"She needn\'t have cooked" означает:', 'o': ['Она не готовила', 'Она приготовила, но не нужно было', 'Ей нужно готовить', 'Она должна была готовить'], 'a': 1},
                {'q': 'The keys ___ fallen under the sofa.', 'o': ["must have", "can't have", "should have", "needn't have"], 'a': 0},
                {'q': 'I ___ eaten that — now I feel sick.', 'o': ["should have eaten", "shouldn't have eaten", "must have eaten", "can't have eaten"], 'a': 1},
                {'q': '"Could have done" означает:', 'o': ['Сделал (прошлое)', 'Имел возможность сделать (но неизвестно, сделал ли)', 'Должен был сделать', 'Не мог сделать'], 'a': 1},
                {'q': 'She ___ studied all night — her paper is excellent.', 'o': ["must have", "can't have", "needn't have", "shouldn't have"], 'a': 0},
                {'q': '"We would have won if we had practised more."', 'o': ['Мы выиграли', 'Мы бы выиграли (но не выиграли)', 'Мы должны были выиграть', 'Мы не должны были выигрывать'], 'a': 1},
            ]
        },
        {
            'id': 'c1_g4',
            'title': 'Причастные обороты (Participial Clauses)',
            'icon': '🔗',
            'explanation': (
                '📌 *Причастные обороты (Participial Clauses)*\n\n'
                'Сжатые обороты, заменяющие придаточные предложения. Типично для письменной/формальной речи.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *Present Participle (-ing) = одновременные или причинные:*\n\n'
                '• *Walking down the street*, I saw an accident.\n'
                '  (= While I was walking... / When I walked...)\n'
                '• *Feeling tired*, she went to bed early.\n'
                '  (= Because she felt tired...)\n'
                '• *Not knowing what to do*, he called his mother.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *Past Participle (PP) = пассивное значение или завершённое:*\n\n'
                '• *Written in 1985*, the book is still popular.\n'
                '  (= The book, which was written in 1985...)\n'
                '• *Surrounded by fans*, she smiled.\n'
                '  (= She was surrounded by fans...)\n'
                '• *Exhausted after the race*, he sat down.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '3️⃣ *Perfect Participle (Having + PP) = предшествующее:*\n\n'
                '• *Having finished her work*, she relaxed.\n'
                '  (= After she had finished...)\n'
                '• *Having spent all his money*, he was broke.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '⚠️ *Важно:*\n'
                'Подлежащее причастного оборота должно совпадать с подлежащим главного!'
            ),
            'exercises': [
                {'q': '"While she was waiting, she read a book." → Причастный оборот:', 'o': ['Waited, she read a book.', 'Waiting, she read a book.', 'Having waited, she read a book.', 'Being waited, she read a book.'], 'a': 1, 'e': 'Одновременное действие: Waiting, she read a book.'},
                {'q': '"The letter which was written in French was hard to read." → Причастный:', 'o': ['Writing in French, the letter was hard to read.', 'Written in French, the letter was hard to read.', 'Having written in French, the letter was hard to read.', 'Being written in French, the letter was hard to read.'], 'a': 1, 'e': 'Пассивный PP: Written in French,...'},
                {'q': '"After he had eaten, he felt better." → Причастный:', 'o': ['Eating, he felt better.', 'Eaten, he felt better.', 'Having eaten, he felt better.', 'Being eaten, he felt better.'], 'a': 2, 'e': 'Предшествующее: Having eaten, he felt better.'},
                {'q': '"Because she felt nervous, she couldn\'t speak." → Причастный:', 'o': ['Felt nervous, she couldn\'t speak.', 'Feeling nervous, she couldn\'t speak.', 'Having felt nervous, she couldn\'t speak.', 'Being felt nervous, she couldn\'t speak.'], 'a': 1, 'e': 'Причина: Feeling nervous, she couldn\'t speak.'},
                {'q': '"Not ___ what to say, he kept silent."', 'o': ['knowing', 'known', 'having known', 'being known'], 'a': 0, 'e': 'Not knowing = не зная (Present Participle с отрицанием).'},
                {'q': '"Having spent all her money, she ___"', 'o': ['was going shopping', 'couldn\'t buy anything', 'has nothing', 'spent more'], 'a': 1, 'e': "Having spent all her money = потратив все деньги → couldn't buy anything."},
                {'q': '"___ in 1816, the novel is a classic." (Write)', 'o': ['Writing', 'Written', 'Having written', 'Being written'], 'a': 1, 'e': 'Пассивный PP: Written in 1816,...'},
                {'q': 'Ошибка в причастном обороте:', 'o': ['Walking in the park, I saw her.', 'Feeling tired, the bed was comfortable.', 'Having finished, she left.', 'Not knowing the answer, he guessed.'], 'a': 1, 'e': '"Feeling tired, the bed was comfortable" — ошибка: кровать не чувствовала усталости!'},
                {'q': '"___ he had read the report, he made his decision."', 'o': ['Reading', 'Read', 'Having read', 'Being read'], 'a': 2, 'e': 'После предшествующего: Having read...'},
                {'q': 'Perfect Participle (Having + PP) используется для:', 'o': ['Одновременных действий', 'Действия, предшествующего главному', 'Пассивных конструкций', 'Причинных отношений'], 'a': 1, 'e': 'Having + PP = после того, как... (предшествование).'},
            ],
            'test': [
                {'q': '"While waiting for the train, she called him." → Причастный:', 'o': ['Waited for the train, she called him.', 'Waiting for the train, she called him.', 'Having waited for the train, she called him.', 'Being waited for the train, she called him.'], 'a': 1},
                {'q': '"The bridge, which was built in 1900, is still strong." → Причастный:', 'o': ['Building in 1900, the bridge is still strong.', 'Built in 1900, the bridge is still strong.', 'Having built in 1900, the bridge is still strong.', 'Being built in 1900, the bridge is still strong.'], 'a': 1},
                {'q': '"After she had completed the course, she got a job." → Причастный:', 'o': ['Completing the course, she got a job.', 'Completed the course, she got a job.', 'Having completed the course, she got a job.', 'Being completed the course, she got a job.'], 'a': 2},
                {'q': '"Because he didn\'t know the rules, he made mistakes." → Причастный:', 'o': ['Known the rules, he made mistakes.', 'Knowing the rules, he made mistakes.', 'Not knowing the rules, he made mistakes.', 'Having known the rules, he made mistakes.'], 'a': 2},
                {'q': '"___ by the news, she burst into tears."', 'o': ['Shocking', 'Shocked', 'Having shocked', 'Being shocking'], 'a': 1},
                {'q': '"___ all the options, he chose the safest." (consider)', 'o': ['Considering', 'Considered', 'Having considered', 'Being considered'], 'a': 2},
                {'q': '"She sat by the fire, ___ a book." (read)', 'o': ['reading', 'read', 'having read', 'being read'], 'a': 0},
                {'q': '"___ in 1564, the composer lived a short life." (born)', 'o': ['Borning', 'Born', 'Having born', 'Being born'], 'a': 1},
                {'q': '"___ the door, he noticed a note." (open)', 'o': ['Opening', 'Opened', 'Having opened', 'Being opened'], 'a': 0},
                {'q': 'Правило согласования причастия:', 'o': ['Может иметь любое подлежащее', 'Подлежащее должно совпадать с главным предложением', 'Всегда используется в начале', 'Только в письменном тексте'], 'a': 1},
                {'q': '"___ so hard, she deserved a rest." (work)', 'o': ['Working', 'Worked', 'Having worked', 'Being worked'], 'a': 2},
                {'q': '"The results, ___ last week, were disappointing." (announce)', 'o': ['announcing', 'announced', 'having announced', 'being announcing'], 'a': 1},
                {'q': '"___ what she wanted, she left the shop." (buy)', 'o': ['Buying', 'Bought', 'Having bought', 'Being bought'], 'a': 2},
                {'q': '"___ time, the team struggled to finish." (not/have)', 'o': ['Not having', 'Not have', 'Having not', 'Not had'], 'a': 0},
                {'q': '"___ around the city, the tourists got tired." (walk)', 'o': ['Walked', 'Having walked', 'Walking', 'Being walked'], 'a': 2},
            ]
        },
        {
            'id': 'c1_g5',
            'title': 'Номинализация (Nominalisation)',
            'icon': '📝',
            'explanation': (
                '📌 *Номинализация (Nominalisation)*\n\n'
                'Преобразование глаголов/прилагательных в существительные. Широко используется в академическом и формальном письме.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Зачем?*\n'
                '• Более формальный и объективный стиль\n'
                '• Компактность выражения\n'
                '• Типично для академических текстов, репортажей, официальных документов\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Как образуется:*\n\n'
                'Глагол → Существительное:\n'
                '• decide → *decision*\n'
                '• analyse → *analysis*\n'
                '• develop → *development*\n'
                '• achieve → *achievement*\n'
                '• investigate → *investigation*\n'
                '• improve → *improvement*\n'
                '• manage → *management*\n'
                '• reduce → *reduction*\n\n'
                'Прилагательное → Существительное:\n'
                '• efficient → *efficiency*\n'
                '• important → *importance*\n'
                '• stable → *stability*\n'
                '• significant → *significance*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *Примеры трансформации:*\n\n'
                'Разговорное:\n'
                '"They decided to expand. This significantly improved profits."\n\n'
                'Академическое (с номинализацией):\n'
                '"*The decision to expand* resulted in a *significant improvement* in profits."'
            ),
            'exercises': [
                {'q': 'decide → существительное:', 'o': ['deciding', 'decided', 'decision', 'decidement'], 'a': 2, 'e': 'decide → decision.'},
                {'q': '"They investigated the case." → Номинализация:', 'o': ['The investigating of the case.', 'The case was investigating.', 'The investigation of the case.', 'Investigating the case.'], 'a': 2, 'e': 'investigate → investigation: The investigation of the case.'},
                {'q': 'significant → существительное:', 'o': ['significantness', 'significance', 'significantly', 'signification'], 'a': 1, 'e': 'significant → significance.'},
                {'q': '"The economy improved." → Формально:', 'o': ['The economy\'s improvement.', 'There was an improvement in the economy.', 'The economy was improving.', 'Improving the economy.'], 'a': 1, 'e': 'There was an improvement in the economy.'},
                {'q': 'develop → существительное:', 'o': ['developer', 'developed', 'developing', 'development'], 'a': 3, 'e': 'develop → development.'},
                {'q': '"They achieved great results." → Номинализация:', 'o': ['The achieving of great results.', 'The achievement of great results.', 'Achieving great results.', 'Their achievement great results.'], 'a': 1, 'e': 'achieve → achievement: The achievement of great results.'},
                {'q': 'stable → существительное:', 'o': ['stableness', 'stabilise', 'stability', 'stabling'], 'a': 2, 'e': 'stable → stability.'},
                {'q': 'Зачем используется номинализация?', 'o': ['Для разговорной речи', 'Для формального/академического стиля', 'Для упрощения текста', 'Для создания вопросов'], 'a': 1, 'e': 'Номинализация = академический, формальный стиль.'},
                {'q': 'manage → существительное:', 'o': ['manager', 'managed', 'managing', 'management'], 'a': 3, 'e': 'manage → management.'},
                {'q': '"We reduced costs." → Номинализация:', 'o': ['The reducing of costs.', 'The cost reduction.', 'Cost reducing.', 'Reducing costs.'], 'a': 1, 'e': 'reduce → reduction: The cost reduction.'},
            ],
            'test': [
                {'q': 'analyse → существительное:', 'o': ['analyser', 'analysed', 'analysis', 'analysation'], 'a': 2},
                {'q': 'improve → существительное:', 'o': ['improvement', 'improver', 'improving', 'improved'], 'a': 0},
                {'q': '"They failed to implement the policy." → Номинализация:', 'o': ['The failing to implement.', 'The implementation failure.', 'Implementing failure.', 'The failure to implement the policy.'], 'a': 3},
                {'q': 'efficient → существительное:', 'o': ['efficiency', 'effectness', 'efficiently', 'effectivity'], 'a': 0},
                {'q': '"Sales increased significantly." → Номинализация:', 'o': ['The significant sales increase.', 'Increasing significantly of sales.', 'The significant increase in sales.', 'Sales significantly increasing.'], 'a': 2},
                {'q': 'important → существительное:', 'o': ['importantness', 'importantly', 'importance', 'importation'], 'a': 2},
                {'q': '"He suggested a new approach." → Номинализация:', 'o': ['His suggesting a new approach.', 'His suggestion of a new approach.', 'He suggested approach.', 'New approach suggestion.'], 'a': 1},
                {'q': 'reduce → существительное:', 'o': ['reducer', 'reduced', 'reducing', 'reduction'], 'a': 3},
                {'q': '"They agreed to cooperate." → Академическое:', 'o': ['The agreeing to cooperate.', 'Their agreement to cooperate.', 'Agreement cooperating.', 'They cooperated agreeing.'], 'a': 1},
                {'q': 'achieve → существительное:', 'o': ['achiever', 'achieved', 'achieving', 'achievement'], 'a': 3},
                {'q': 'dependent → существительное:', 'o': ['dependentness', 'dependently', 'dependence', 'depender'], 'a': 2},
                {'q': '"The government decided to reform taxes." → Номинализация:', 'o': ['The deciding to reform.', "The government's decision to reform taxes.", 'Deciding reforms of taxes.', 'Government tax deciding.'], 'a': 1},
                {'q': 'investigate → существительное:', 'o': ['investigater', 'investigated', 'investigating', 'investigation'], 'a': 3},
                {'q': 'Номинализация превращает:', 'o': ['Существительные в глаголы', 'Глаголы/прилагательные в существительные', 'Предложения в вопросы', 'Активные в пассивные'], 'a': 1},
                {'q': '"They failed to deliver the project." — номинализация "failed":',  'o': ['failure', 'failing', 'failed', 'falls'], 'a': 0},
            ]
        },
        {
            'id': 'c1_g6',
            'title': 'Дискурсивные маркеры',
            'icon': '🗣️',
            'explanation': (
                '📌 *Дискурсивные маркеры (Discourse Markers)*\n\n'
                'Связующие слова и выражения, которые структурируют речь и текст.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *По функциям:*\n\n'
                '➡️ *Добавление:*\n'
                'Furthermore, Moreover, In addition, Besides,\n'
                'What is more, Not only...but also\n\n'
                '⚡ *Контраст:*\n'
                'However, Nevertheless, Nonetheless,\n'
                'On the contrary, In spite of, Despite,\n'
                'Whereas, While, Although, Even though\n\n'
                '🔄 *Причина/Следствие:*\n'
                'Therefore, Consequently, As a result,\n'
                'Thus, Hence, Accordingly, For this reason\n\n'
                '📌 *Уступка:*\n'
                'Admittedly, Granted, It is true that..., although,\n'
                'Even if, Despite the fact that\n\n'
                '🎯 *Пример:*\n'
                'For instance, For example, Such as,\n'
                'To illustrate, Namely\n\n'
                '📝 *Обобщение/Вывод:*\n'
                'In conclusion, To sum up, Overall,\n'
                'In short, To summarise, All in all\n\n'
                '🔍 *Уточнение:*\n'
                'In other words, That is to say, Namely,\n'
                'Put simply, To be more precise'
            ),
            'exercises': [
                {'q': '"She was tired. ___, she continued working." (несмотря на усталость)', 'o': ['Therefore', 'Nevertheless', 'Furthermore', 'As a result'], 'a': 1, 'e': 'Nevertheless = несмотря на это (контраст).'},
                {'q': '"He studied hard. ___, he passed the exam." (следствие)', 'o': ['However', 'Although', 'Consequently', 'Despite'], 'a': 2, 'e': 'Consequently = следовательно (причина-следствие).'},
                {'q': '"The book was long. ___, it was interesting." (добавление позитива)', 'o': ['However', 'Therefore', 'Furthermore', 'Nevertheless'], 'a': 3, 'e': 'Nevertheless = тем не менее (контраст-уступка).'},
                {'q': '"There are many reasons. ___, the main one is cost." (уточнение)', 'o': ['In conclusion', 'For instance', 'Namely', 'Furthermore'], 'a': 2, 'e': 'Namely = а именно (уточнение).'},
                {'q': '"She is talented. ___, she works hard." (добавление)', 'o': ['However', 'Nevertheless', 'Moreover', 'Despite'], 'a': 2, 'e': 'Moreover = более того (добавление).'},
                {'q': '"___ the rain, they continued the match." (несмотря)', 'o': ['Although', 'Despite', 'However', 'Nevertheless'], 'a': 1, 'e': 'Despite + noun/gerund: Despite the rain.'},
                {'q': '"___, I enjoyed the film." (подводя итог)', 'o': ['For instance', 'In other words', 'Overall', 'Namely'], 'a': 2, 'e': 'Overall = в целом (обобщение).'},
                {'q': '"The policy failed. ___, it was changed." (следствие)', 'o': ['Although', 'However', 'Therefore', 'Despite'], 'a': 2, 'e': 'Therefore = поэтому (следствие).'},
                {'q': '"___ many problems, the project succeeded." (несмотря на)', 'o': ['Although', 'Despite', 'However', 'Therefore'], 'a': 1, 'e': 'Despite + noun: Despite many problems.'},
                {'q': '"He is, ___, the best candidate for the job." (уточнение)', 'o': ['for instance', 'however', 'therefore', 'in other words'], 'a': 3, 'e': 'In other words = другими словами (уточнение).'},
            ],
            'test': [
                {'q': '"She failed the exam. ___, she retook it." (следствие)', 'o': ['However', 'Furthermore', 'As a result', 'Despite'], 'a': 2},
                {'q': '"The plan had flaws. ___, it was accepted." (контраст)', 'o': ['Therefore', 'Nevertheless', 'Furthermore', 'Consequently'], 'a': 1},
                {'q': '"___ hard work, success is not guaranteed." (несмотря на)', 'o': ['Although', 'However', 'Despite', 'Therefore'], 'a': 2},
                {'q': '"There are benefits. ___, there are risks." (добавление)', 'o': ['However', 'Furthermore', 'Therefore', 'Despite'], 'a': 1},
                {'q': '"He was late. ___, he apologised." (уступка)', 'o': ['Consequently', 'Furthermore', 'Admittedly', 'Therefore'], 'a': 2},
                {'q': '"The research shows X. ___ the claim is wrong." (следствие)', 'o': ['Although', 'Despite', 'Hence', 'Furthermore'], 'a': 2},
                {'q': '"___ to say, the results were poor." (уточнение)', 'o': ['That is', 'For instance', 'In addition', 'Despite'], 'a': 0},
                {'q': '"Prices rose. ___, demand fell." (следствие)', 'o': ['However', 'Furthermore', 'Consequently', 'Despite'], 'a': 2},
                {'q': '"She is shy. ___, she\'s a great speaker." (контраст)', 'o': ['Therefore', 'Furthermore', 'However', 'Consequently'], 'a': 2},
                {'q': '"___ he worked hard, he failed." (уступка)', 'o': ['Despite', 'However', 'Although', 'Therefore'], 'a': 2},
                {'q': 'Маркер ОБОБЩЕНИЯ:', 'o': ['For instance', 'To sum up', 'In addition', 'However'], 'a': 1},
                {'q': '"The results were mixed, ___ the experiment succeeded." (добавление)', 'o': ['however', 'yet', 'moreover', 'despite'], 'a': 2},
                {'q': '"___ the difficulties, we achieved our goal." (несмотря)', 'o': ['Although', 'However', 'Despite', 'Therefore'], 'a': 2},
                {'q': 'Маркер ПРИМЕРА:', 'o': ['Therefore', 'For instance', 'Nevertheless', 'Moreover'], 'a': 1},
                {'q': '"___ speaking, the situation is serious." (обобщение)', 'o': ['Generally', 'Namely', 'Therefore', 'Admittedly'], 'a': 0},
            ]
        },
        {
            'id': 'c1_g7',
            'title': 'Эллипсис и замещение',
            'icon': '✂️',
            'explanation': (
                '📌 *Эллипсис и Замещение (Ellipsis and Substitution)*\n\n'
                'Способы избежать повторения в речи и тексте.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *ЭЛЛИПСИС — пропуск слов:*\n\n'
                '• "Are you going?" — "Yes, I am [going]." (пропускаем going)\n'
                '• "Can you speak French?" — "Yes, I can [speak French]."\n'
                '• "He didn\'t help and [he] didn\'t apologise."\n'
                '• "I\'d like to go but [I] can\'t [go]."\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *ЗАМЕЩЕНИЕ — замена слова:*\n\n'
                '🔹 *ONE/ONES* (вместо существительного):\n'
                '• "Which cake?" — "The big *one*." / "The red *ones*."\n'
                '• "I need a pen." — "I\'ll get you *one*."\n\n'
                '🔹 *SO/NOT* (вместо придаточного):\n'
                '• "Will it rain?" — "I think *so*." / "I hope *not*."\n'
                '• "She told me *so*." (она мне так сказала)\n\n'
                '🔹 *DO SO* (вместо глагольной группы):\n'
                '• "He asked me to call, so I *did so*."\n'
                '• "She smiled and *did so* warmly."\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *SUBSTITUTION с AUX глаголами:*\n'
                '• "Does she work?" — "Yes, she *does*."\n'
                '• "He can\'t swim but she *can*." [swim]\n'
                '• "I didn\'t see it." — "Neither *did* I."'
            ),
            'exercises': [
                {'q': '"Are you coming?" — "Yes, I ___."', 'o': ['do', 'am', 'be', 'come'], 'a': 1, 'e': 'Эллипсис: Yes, I am [coming].'},
                {'q': '"Will it rain?" — "I hope ___."', 'o': ['not', 'so', 'yes', 'it'], 'a': 1, 'e': 'I hope so = надеюсь, что да.'},
                {'q': '"I need a pen." — "I\'ll get you ___."', 'o': ['it', 'one', 'them', 'that'], 'a': 1, 'e': 'One заменяет "a pen".'},
                {'q': '"She told me to apologise, so I ___ so."', 'o': ['made', 'did', 'do', 'done'], 'a': 1, 'e': 'Did so = сделал это (замещение глагольной группы).'},
                {'q': '"Is he coming?" — "I don\'t think ___."', 'o': ['not', 'so', 'it', 'that'], 'a': 1, 'e': 'I don\'t think so = не думаю.'},
                {'q': '"He can\'t swim but she ___."', 'o': ['can swim', 'can', 'swims', 'is'], 'a': 1, 'e': 'She can [swim] — эллипсис.'},
                {'q': '"Which shoes?" — "The black ___."', 'o': ['one', 'ones', 'them', 'these'], 'a': 1, 'e': 'Ones (множественное): the black ones.'},
                {'q': '"She didn\'t come." — "Neither ___ I."', 'o': ['did', 'was', 'had', 'am'], 'a': 0, 'e': 'Neither did I = Я тоже нет.'},
                {'q': '"Is it true?" — "I\'m afraid ___."', 'o': ['not', 'so', 'it is', 'yes'], 'a': 1, 'e': 'I\'m afraid so = боюсь, что да.'},
                {'q': 'Эллипсис в: "She smiled and left."', 'o': ['She smiled and she left.', 'She smiled and (she) left.', 'Нет эллипсиса', 'She smiled and did left.'], 'a': 1, 'e': '(She) — опущено подлежащее второго предложения.'},
            ],
            'test': [
                {'q': '"Can she drive?" — "Yes, she ___."', 'o': ['can drive', 'can', 'does', 'is'], 'a': 1},
                {'q': '"Will he come?" — "I think ___."', 'o': ['not', 'so', 'yes', 'him'], 'a': 1},
                {'q': '"I want a coffee." — "I\'ll make you ___."', 'o': ['it', 'one', 'some', 'that'], 'a': 1},
                {'q': '"He asked me to help and I ___ so."', 'o': ['made', 'did', 'do', 'have'], 'a': 1},
                {'q': '"Did she call?" — "I believe ___."', 'o': ['not', 'so', 'it', 'that'], 'a': 1},
                {'q': '"She didn\'t apologise." — "Neither ___ he."', 'o': ['did', 'was', 'had', 'has'], 'a': 0},
                {'q': '"Which dress?" — "The red ___."', 'o': ['one', 'ones', 'dress', 'it'], 'a': 0},
                {'q': '"Is it serious?" — "I\'m afraid ___."', 'o': ['not', 'so', 'it is', 'yes'], 'a': 1},
                {'q': '"He passed the exam." — "So ___ I."', 'o': ['was', 'did', 'am', 'have'], 'a': 1},
                {'q': 'Эллипсис — это:', 'o': ['Замена слова другим', 'Пропуск слова во избежание повторения', 'Инверсия порядка слов', 'Номинализация'], 'a': 1},
                {'q': '"She told me to call and I ___ so immediately."', 'o': ['made', 'did', 'do', 'done'], 'a': 1},
                {'q': '"I won\'t go." — "Neither ___ I."', 'o': ['will', 'shall', 'do', 'am'], 'a': 0},
                {'q': '"Are you happy?" — "I suppose ___."', 'o': ['not', 'so', 'yes', 'it'], 'a': 1},
                {'q': '"Which book?" — "The interesting ___."', 'o': ['one', 'ones', 'book', 'ones\''], 'a': 0},
                {'q': '"He can\'t come." — "Neither ___ she."', 'o': ['can', 'could', 'is', 'does'], 'a': 0},
            ]
        },
        {
            'id': 'c1_g8',
            'title': 'Сослагательное наклонение (Subjunctive)',
            'icon': '🎭',
            'explanation': (
                '📌 *Сослагательное наклонение (Subjunctive Mood)*\n\n'
                'Используется для выражения желаний, требований, предложений, необходимости — особенно в формальной речи.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *Present Subjunctive (base form):*\n'
                'После глаголов требования, предложения, настаивания:\n'
                'suggest, recommend, insist, demand, require, propose\n\n'
                '• I suggest that he *go* to the doctor.\n'
                '  (НЕ he goes — base form!)\n'
                '• They insisted that she *be* present.\n'
                '• The doctor recommended that he *take* rest.\n'
                '• It is essential that everyone *arrive* on time.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *Устойчивые выражения с subjunctive:*\n'
                '• *Long live* the king! (да здравствует)\n'
                '• *Be that as it may* (как бы то ни было)\n'
                '• *Come what may* (что бы ни случилось)\n'
                '• *God save* the Queen\n'
                '• *Suffice it to say* (достаточно сказать)\n\n'
                '━━━━━━━━━━━━━━━\n'
                '3️⃣ *Were-subjunctive:*\n'
                '• If I *were* you... (все лица — WERE)\n'
                '• I wish it *were* possible.\n'
                '• *Were* she to come...\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📌 *В британском английском:*\n'
                'should + base form вместо subjunctive:\n'
                '• I suggest that he *should go*. (= he go)'
            ),
            'exercises': [
                {'q': '"I suggest that he ___ a doctor." (go/goes)', 'o': ['goes', 'go', 'went', 'going'], 'a': 1, 'e': 'Subjunctive после suggest: that he go (base form).'},
                {'q': '"They insisted that she ___ present." (be/is)', 'o': ['is', 'was', 'be', 'being'], 'a': 2, 'e': 'Subjunctive: that she be (base form).'},
                {'q': '"It is essential that everyone ___ on time." (arrive/arrives)', 'o': ['arrives', 'arrive', 'arrived', 'arriving'], 'a': 1, 'e': 'Essential that + subjunctive: arrive (base form).'},
                {'q': '"The doctor recommended that he ___ rest." (take/takes)', 'o': ['takes', 'take', 'took', 'taking'], 'a': 1, 'e': 'Recommended that + subjunctive: take.'},
                {'q': '"Long ___ the king!" (live/lives)', 'o': ['lives', 'live', 'lived', 'living'], 'a': 1, 'e': 'Long live = устойчивое выражение (subjunctive).'},
                {'q': '"I demand that he ___ here now." (is/be)', 'o': ['is', 'are', 'was', 'be'], 'a': 3, 'e': 'Demand that + subjunctive: be.'},
                {'q': '"If I ___ you, I would leave." (was/were)', 'o': ['was', 'were', 'am', 'be'], 'a': 1, 'e': 'Were-subjunctive: If I were you.'},
                {'q': 'Британский вариант subjunctive:', 'o': ['Только base form', 'should + base form', 'would + base form', 'may + base form'], 'a': 1, 'e': 'Британский = should + base form.'},
                {'q': '"It is vital that she ___ the truth." (know/knows)', 'o': ['knows', 'know', 'knew', 'known'], 'a': 1, 'e': 'Vital that + subjunctive: know.'},
                {'q': 'Глагол после suggest/recommend в formal English:', 'o': ['3-е лицо с -S', 'Base form (subjunctive)', 'To-infinitive', 'Past Simple'], 'a': 1, 'e': 'Subjunctive = base form (без изменений для всех лиц).'},
            ],
            'test': [
                {'q': '"I propose that she ___ chairwoman." (be/is)', 'o': ['is', 'was', 'be', 'being'], 'a': 2},
                {'q': '"It is important that he ___ the rules." (follow/follows)', 'o': ['follows', 'follow', 'followed', 'following'], 'a': 1},
                {'q': '"They require that all staff ___ a uniform." (wear/wears)', 'o': ['wears', 'wear', 'wore', 'wearing'], 'a': 1},
                {'q': '"God ___ the Queen." (save/saves)', 'o': ['saves', 'save', 'saved', 'saving'], 'a': 1},
                {'q': '"The committee insisted that he ___ his decision." (reconsider)', 'o': ['reconsiders', 'reconsider', 'reconsidered', 'reconsidering'], 'a': 1},
                {'q': '"If he ___ here, we could ask him."', 'o': ['is', 'was', 'were', 'be'], 'a': 2},
                {'q': '"I wish it ___ possible." (was/were)', 'o': ['was', 'is', 'were', 'be'], 'a': 2},
                {'q': '"___ that as it may, we must continue."', 'o': ['Be', 'Is', 'Was', 'Were'], 'a': 0},
                {'q': '"It is necessary that he ___ early." (leave/leaves)', 'o': ['leaves', 'leave', 'left', 'leaving'], 'a': 1},
                {'q': 'Subjunctive после "it is important that":',  'o': ['3rd person -s', 'base form', 'past simple', 'to-infinitive'], 'a': 1},
                {'q': '"She recommended that he ___ the job." (take/takes)', 'o': ['takes', 'take', 'took', 'taking'], 'a': 1},
                {'q': '"___ what may, we will succeed."', 'o': ['Come', 'Goes', 'Coming', 'Came'], 'a': 0},
                {'q': '"I suggest that the meeting ___ rescheduled." (be/is)', 'o': ['is', 'was', 'be', 'being'], 'a': 2},
                {'q': '"It is crucial that everyone ___ the protocol." (follow)', 'o': ['follows', 'follow', 'followed', 'following'], 'a': 1},
                {'q': '"Were she ___ arrive, please call me." (to/∅)', 'o': ['to', '∅', 'for', 'in order to'], 'a': 0},
            ]
        },
    ],
    'vocabulary': [
        {
            'category': 'Академическая лексика',
            'icon': '🎓',
            'words': [
                {'en': 'paradigm', 'ru': 'парадигма', 'ex': 'A new scientific paradigm emerged.'},
                {'en': 'discourse', 'ru': 'дискурс/рассуждение', 'ex': 'Academic discourse is formal.'},
                {'en': 'methodology', 'ru': 'методология', 'ex': 'The research methodology was sound.'},
                {'en': 'empirical', 'ru': 'эмпирический', 'ex': 'We need empirical evidence.'},
                {'en': 'theoretical', 'ru': 'теоретический', 'ex': 'This is a theoretical framework.'},
                {'en': 'premise', 'ru': 'предпосылка/посылка', 'ex': 'The argument\'s premise is flawed.'},
                {'en': 'implication', 'ru': 'импликация/последствие', 'ex': 'The implications are serious.'},
                {'en': 'correlation', 'ru': 'корреляция', 'ex': 'There is a strong correlation.'},
                {'en': 'coherent', 'ru': 'последовательный/логичный', 'ex': 'A coherent argument is needed.'},
                {'en': 'ambiguous', 'ru': 'неоднозначный', 'ex': 'The results are ambiguous.'},
            ]
        },
        {
            'category': 'Юридическая лексика',
            'icon': '⚖️',
            'words': [
                {'en': 'verdict', 'ru': 'вердикт', 'ex': 'The jury reached a verdict.'},
                {'en': 'defendant', 'ru': 'обвиняемый', 'ex': 'The defendant pleaded not guilty.'},
                {'en': 'plaintiff', 'ru': 'истец', 'ex': 'The plaintiff won the case.'},
                {'en': 'testimony', 'ru': 'показания', 'ex': 'Her testimony was crucial.'},
                {'en': 'appeal', 'ru': 'апелляция', 'ex': 'He filed an appeal.'},
                {'en': 'jurisdiction', 'ru': 'юрисдикция', 'ex': 'This is outside our jurisdiction.'},
                {'en': 'statute', 'ru': 'устав/законодательный акт', 'ex': 'The statute was amended.'},
                {'en': 'litigation', 'ru': 'судебное разбирательство', 'ex': 'Litigation is expensive.'},
                {'en': 'injunction', 'ru': 'судебный запрет', 'ex': 'They obtained an injunction.'},
                {'en': 'liability', 'ru': 'ответственность (правовая)', 'ex': 'They accepted liability.'},
            ]
        },
        {
            'category': 'Психология и поведение',
            'icon': '🧠',
            'words': [
                {'en': 'cognitive', 'ru': 'когнитивный', 'ex': 'Cognitive development in children.'},
                {'en': 'perception', 'ru': 'восприятие', 'ex': 'Perception differs between people.'},
                {'en': 'motivation', 'ru': 'мотивация', 'ex': 'Motivation is key to success.'},
                {'en': 'subconscious', 'ru': 'подсознательный', 'ex': 'Subconscious fears affect us.'},
                {'en': 'anxiety', 'ru': 'тревожность', 'ex': 'She suffers from anxiety.'},
                {'en': 'resilience', 'ru': 'устойчивость/стрессоустойчивость', 'ex': 'Children show remarkable resilience.'},
                {'en': 'empathy', 'ru': 'эмпатия', 'ex': 'Empathy is a social skill.'},
                {'en': 'trauma', 'ru': 'психологическая травма', 'ex': 'Trauma affects mental health.'},
                {'en': 'stereotype', 'ru': 'стереотип', 'ex': 'Stereotypes can be harmful.'},
                {'en': 'rational', 'ru': 'рациональный', 'ex': 'A rational decision was made.'},
            ]
        },
        {
            'category': 'Экономика и финансы',
            'icon': '💰',
            'words': [
                {'en': 'fiscal', 'ru': 'фискальный/финансовый', 'ex': 'Fiscal policy was tightened.'},
                {'en': 'deficit', 'ru': 'дефицит', 'ex': 'The budget deficit grew.'},
                {'en': 'austerity', 'ru': 'жёсткая экономия', 'ex': 'Austerity measures were imposed.'},
                {'en': 'monetary', 'ru': 'монетарный/денежный', 'ex': 'Monetary policy affects inflation.'},
                {'en': 'deregulation', 'ru': 'дерегулирование', 'ex': 'Deregulation opened markets.'},
                {'en': 'subsidy', 'ru': 'субсидия', 'ex': 'Farming subsidies were cut.'},
                {'en': 'commodities', 'ru': 'товары/сырьё', 'ex': 'Oil is a key commodity.'},
                {'en': 'speculation', 'ru': 'спекуляция', 'ex': 'Market speculation is risky.'},
                {'en': 'quantitative easing', 'ru': 'количественное смягчение', 'ex': 'The bank used quantitative easing.'},
                {'en': 'sovereign debt', 'ru': 'государственный долг', 'ex': 'Sovereign debt is rising.'},
            ]
        },
        {
            'category': 'Философия и этика',
            'icon': '🤔',
            'words': [
                {'en': 'ethics', 'ru': 'этика', 'ex': 'Medical ethics is complex.'},
                {'en': 'morality', 'ru': 'нравственность', 'ex': 'Questions of morality arise.'},
                {'en': 'pragmatic', 'ru': 'прагматичный', 'ex': 'A pragmatic approach is needed.'},
                {'en': 'ideology', 'ru': 'идеология', 'ex': 'Political ideology shapes policy.'},
                {'en': 'philosophical', 'ru': 'философский', 'ex': 'A philosophical debate.'},
                {'en': 'utilitarianism', 'ru': 'утилитаризм', 'ex': 'Utilitarianism seeks the greatest good.'},
                {'en': 'paradox', 'ru': 'парадокс', 'ex': 'This is a moral paradox.'},
                {'en': 'subjective', 'ru': 'субъективный', 'ex': 'Art is subjective.'},
                {'en': 'objective', 'ru': 'объективный', 'ex': 'Science aims to be objective.'},
                {'en': 'intrinsic', 'ru': 'внутренний/присущий', 'ex': 'Art has intrinsic value.'},
            ]
        },
    ],
    'phrases': [
        {
            'situation': 'Академическое письмо',
            'icon': '📄',
            'items': [
                {'en': 'It is widely acknowledged that...', 'ru': 'Широко признано, что...', 'note': 'Общепризнанный факт'},
                {'en': 'The data indicates that...', 'ru': 'Данные свидетельствуют о том, что...', 'note': 'Ссылка на данные'},
                {'en': 'This is consistent with the view that...', 'ru': 'Это согласуется с точкой зрения...', 'note': 'Согласованность'},
                {'en': 'Notwithstanding the above...', 'ru': 'Несмотря на вышесказанное...', 'note': 'Контраст'},
                {'en': 'The findings lend support to...', 'ru': 'Результаты подкрепляют...', 'note': 'Поддержка тезиса'},
                {'en': 'It remains to be seen whether...', 'ru': 'Остаётся посмотреть, будет ли...', 'note': 'Неопределённость'},
                {'en': 'In light of this evidence...', 'ru': 'В свете этих данных...', 'note': 'Основываясь на доказательствах'},
            ]
        },
        {
            'situation': 'Формальные выступления',
            'icon': '🎤',
            'items': [
                {'en': 'I would like to draw your attention to...', 'ru': 'Хотел бы обратить ваше внимание на...', 'note': 'Привлечь внимание'},
                {'en': "Allow me to elaborate on this point.", 'ru': 'Позвольте мне расширить эту мысль.', 'note': 'Расширить аргумент'},
                {'en': 'As I mentioned previously...', 'ru': 'Как я уже упоминал ранее...', 'note': 'Ссылка на сказанное'},
                {'en': 'I would argue that the key issue is...', 'ru': 'Я бы утверждал, что ключевой вопрос...', 'note': 'Тезис'},
                {'en': 'With that in mind...', 'ru': 'Имея это в виду...', 'note': 'Переход'},
                {'en': 'To bring this to a close...', 'ru': 'Подводя итог...', 'note': 'Заключение'},
            ]
        },
        {
            'situation': 'Дипломатичная речь',
            'icon': '🤝',
            'items': [
                {'en': 'With the greatest respect...', 'ru': 'При всём уважении...', 'note': 'Вежливое несогласие'},
                {'en': "I take your point, however...", 'ru': 'Я понимаю вашу точку зрения, однако...', 'note': 'Контраргумент'},
                {'en': 'Perhaps we could consider an alternative...', 'ru': 'Возможно, мы могли бы рассмотреть альтернативу...', 'note': 'Предложение'},
                {'en': 'There is some merit in that argument.', 'ru': 'В этом аргументе есть определённая логика.', 'note': 'Частичное признание'},
                {'en': 'I\'m inclined to see it differently.', 'ru': 'Я склонен видеть это иначе.', 'note': 'Другая точка зрения'},
                {'en': 'I think we can find common ground.', 'ru': 'Думаю, мы можем найти общий язык.', 'note': 'Компромисс'},
            ]
        },
        {
            'situation': 'Описание данных и статистики',
            'icon': '📊',
            'items': [
                {'en': 'The data reveals a striking pattern...', 'ru': 'Данные обнаруживают поразительную закономерность...', 'note': 'Описание паттерна'},
                {'en': 'There is a marked increase/decrease in...', 'ru': 'Наблюдается заметный рост/спад...', 'note': 'Изменение'},
                {'en': 'The figures are somewhat misleading.', 'ru': 'Цифры несколько вводят в заблуждение.', 'note': 'Критика данных'},
                {'en': "This accounts for approximately X%.", 'ru': 'Это составляет приблизительно X%.', 'note': 'Процентное соотношение'},
                {'en': 'The correlation is statistically significant.', 'ru': 'Корреляция статистически значима.', 'note': 'Статистика'},
                {'en': 'These findings must be interpreted with caution.', 'ru': 'Эти результаты следует интерпретировать осторожно.', 'note': 'Осторожность'},
            ]
        },
        {
            'situation': 'Критическое мышление',
            'icon': '🔍',
            'items': [
                {'en': 'One must question the assumption that...', 'ru': 'Необходимо поставить под сомнение предположение о том, что...', 'note': 'Сомнение в предположении'},
                {'en': "This view overlooks the fact that...", 'ru': 'Эта точка зрения упускает из виду тот факт, что...', 'note': 'Критика позиции'},
                {'en': 'The argument breaks down when...', 'ru': 'Аргумент рассыпается, когда...', 'note': 'Опровержение'},
                {'en': 'This is a false dichotomy.', 'ru': 'Это ложная дихотомия.', 'note': 'Логическая ошибка'},
                {'en': 'The evidence is open to interpretation.', 'ru': 'Доказательства поддаются неоднозначной интерпретации.', 'note': 'Неоднозначность'},
                {'en': 'This raises the question of...', 'ru': 'Это поднимает вопрос о...', 'note': 'Проблема'},
            ]
        },
    ]
}
