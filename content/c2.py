C2 = {
    'name': 'C2 — Мастерство',
    'emoji': '💎',
    'description': (
        '💎 *Уровень C2 — Мастерство*\n\n'
        'Ты владеешь английским свободно и точно.\n'
        'На этом уровне изучаем:\n'
        '• Номинализация и академический стиль\n'
        '• Расщеплённые предложения (Cleft)\n'
        '• Хеджинг и смягчение высказываний\n'
        '• Стилистика и риторика\n'
        '• Сложные коллокации\n\n'
        'Выбери раздел:'
    ),
    'grammar': [
        {
            'id': 'c2_g1',
            'title': 'Номинализация',
            'icon': '📝',
            'explanation': (
                '📌 *Номинализация (Nominalisation)*\n\n'
                'Номинализация — превращение глаголов/прилагательных в существительные для академического/формального стиля.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Как образуется:*\n\n'
                '🔹 Глагол → Существительное:\n'
                '• decide → *decision*\n'
                '• analyse → *analysis*\n'
                '• develop → *development*\n'
                '• fail → *failure*\n'
                '• apply → *application*\n\n'
                '🔹 Прилагательное → Существительное:\n'
                '• complex → *complexity*\n'
                '• effective → *effectiveness*\n'
                '• significant → *significance*\n'
                '• accurate → *accuracy*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '✅ *Примеры трансформации:*\n\n'
                '❌ Неформально: They decided to increase prices.\n'
                '✅ Формально: A decision was made to increase prices.\n\n'
                '❌ We analysed the results carefully.\n'
                '✅ A careful analysis of the results was conducted.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Зачем нужна:*\n'
                '• Академическое письмо — объективность\n'
                '• Деловой язык — нейтральность\n'
                '• Создаёт дистанцию от субъекта\n\n'
                '⚠️ Избыток номинализации делает текст тяжёлым!'
            ),
            'exercises': [
                {'q': 'Номинализация от "investigate": The police → ___ of the crime', 'o': ['investigated', 'investigation', 'investigative', 'to investigate'], 'a': 1, 'e': 'investigate → investigation.'},
                {'q': 'Трансформируй: "They failed to meet the deadline." →', 'o': ['The failure to meet the deadline was noted.', 'They had failure.', 'The failing deadline.', 'Meeting deadline failure.'], 'a': 0, 'e': 'fail → failure. Пассивная конструкция.'},
                {'q': 'Номинализация от "develop": rapid ___ of technology', 'o': ['developing', 'developer', 'development', 'developed'], 'a': 2, 'e': 'develop → development.'},
                {'q': 'Академическая форма: "Scientists discovered a new element."', 'o': ['Scientists had a discovery.', 'The discovery of a new element was made.', 'A new element was discovering.', 'There was discover.'], 'a': 1, 'e': 'discover → discovery + пассивный залог.'},
                {'q': 'Номинализация от "accurate": the ___ of measurements', 'o': ['accurate', 'accurateness', 'accuracy', 'accuration'], 'a': 2, 'e': 'accurate → accuracy.'},
                {'q': 'Трансформируй: "They decided quickly." →', 'o': ['The decision was quick.', 'Quick deciding happened.', 'They were decisive.', 'A quick decision was reached.'], 'a': 3, 'e': 'decide → decision. "A quick decision was reached."'},
                {'q': 'Номинализация от "significant": ___ of the findings', 'o': ['significant', 'significantly', 'significance', 'signification'], 'a': 2, 'e': 'significant → significance.'},
                {'q': 'Цель номинализации в академическом письме:', 'o': ['Неформальный стиль', 'Объективность и дистанция', 'Упрощение структуры', 'Эмоциональность'], 'a': 1, 'e': 'Номинализация создаёт объективность, убирая субъект.'},
                {'q': '"We increased output." → академическая форма:', 'o': ['An increase in output was achieved.', 'Output increasing happened.', 'They increased.', 'Output was increasing.'], 'a': 0, 'e': 'increase → increase (сущ.) + пассив.'},
                {'q': 'Номинализация от "vary": considerable ___ in results', 'o': ['vary', 'various', 'variation', 'variously'], 'a': 2, 'e': 'vary → variation.'},
            ],
            'test': [
                {'q': 'Номинализация от "fail": The project ended in ___', 'o': ['failing', 'failed', 'failure', 'fails'], 'a': 2},
                {'q': 'Академическая форма "We increased output":', 'o': ['Increasing output happened.', 'An increase in output was achieved.', 'Output increasing was done.', 'They were increasing.'], 'a': 1},
                {'q': 'Номинализация от "complex": the ___ of the problem', 'o': ['complex', 'complexly', 'complexion', 'complexity'], 'a': 3},
                {'q': 'Трансформируй: "She analysed data." →', 'o': ['An analysis of the data was conducted.', 'Analysing the data she did.', 'Analysis she did.', 'Data was analysing.'], 'a': 0},
                {'q': 'Номинализация от "effective": ___ of the treatment', 'o': ['effective', 'effectively', 'effect', 'effectiveness'], 'a': 3},
                {'q': '"The government decided to act." → формальная форма:', 'o': ['A government action decision was.', 'A decision to take action was made.', 'Decision was actioned.', 'The government had decide.'], 'a': 1},
                {'q': 'Номинализация от "apply": ___ form must be completed', 'o': ['apply', 'applied', 'application', 'applicant'], 'a': 2},
                {'q': 'Почему НЕ стоит злоупотреблять номинализацией?', 'o': ['Неправильная грамматика', 'Текст становится тяжёлым', 'Слишком разговорный стиль', 'Сложно перевести'], 'a': 1},
                {'q': 'Номинализация от "reduce": significant ___ in costs', 'o': ['reducing', 'reduce', 'reduction', 'reductive'], 'a': 2},
                {'q': '"They investigated fraud." → номинализация:', 'o': ['A fraud investigation was conducted.', 'Fraud was investigating.', 'Investigation fraud occurred.', 'Investigated fraud happened.'], 'a': 0},
                {'q': 'Номинализация от "improve": continuous ___ of skills', 'o': ['improving', 'improved', 'improvement', 'improver'], 'a': 2},
                {'q': 'Академическое предложение с номинализацией:', 'o': ['They found very interesting things.', 'A significant finding emerged from the research.', 'Research was done nicely.', 'Findings came out.'], 'a': 1},
                {'q': 'Номинализация от "assume": a basic ___ of the study', 'o': ['assume', 'assuming', 'assumption', 'assumptive'], 'a': 2},
                {'q': 'Трансформируй: "They implemented changes."', 'o': ['The implementation of changes was carried out.', 'Changes implementing happened.', 'They did implement.', 'Changes were implementing.'], 'a': 0},
                {'q': 'Номинализация от "conclude": the main ___ of the study', 'o': ['conclude', 'concluded', 'conclusion', 'conclusive'], 'a': 2},
            ]
        },
        {
            'id': 'c2_g2',
            'title': 'Расщеплённые предложения (Cleft)',
            'icon': '✂️',
            'explanation': (
                '📌 *Расщеплённые предложения (Cleft Sentences)*\n\n'
                'Cleft sentences разбивают предложение на две части для выделения одного элемента.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '1️⃣ *IT-Cleft: It is/was... that/who*\n\n'
                'Формула: It + be + выделяемый элемент + that/who\n\n'
                '• John broke the window.\n'
                '→ *It was John who* broke the window.\n\n'
                '• She met him in Paris.\n'
                '→ *It was in Paris that* she met him.\n\n'
                '• He came because he was worried.\n'
                '→ *It was because he was worried that* he came.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '2️⃣ *WH-Cleft: What... is/was*\n\n'
                'Формула: What + clause + be + emphasis\n\n'
                '• I need your help.\n'
                '→ *What I need is your help.*\n\n'
                '• She wants to travel.\n'
                '→ *What she wants is to travel.*\n\n'
                '━━━━━━━━━━━━━━━\n'
                '3️⃣ *Reversed WH-Cleft*\n\n'
                '• *Your help* is what I need.\n'
                '• *To travel* is what she wants.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Функция:*\n'
                '• Контрастивное выделение\n'
                '• Подчёркивание важной информации\n'
                '• Устранение неоднозначности'
            ),
            'exercises': [
                {'q': 'IT-Cleft: "Mary solved the problem." → выделить Mary:', 'o': ['It was Mary who solved the problem.', 'It is the problem that Mary solved.', 'Mary it was solved.', 'What Mary solved the problem.'], 'a': 0, 'e': 'IT-Cleft для субъекта: It was Mary who...'},
                {'q': 'WH-Cleft: "I need rest." →', 'o': ['It is rest that I need.', 'What I need is rest.', 'Rest what I need.', 'I what need is rest.'], 'a': 1, 'e': 'What I need is rest.'},
                {'q': '"She left YESTERDAY." → IT-Cleft:', 'o': ['It was yesterday that she left.', 'It was she who left yesterday.', 'Yesterday it was left.', 'What she left was yesterday.'], 'a': 0, 'e': 'Выделяем время: It was yesterday that...'},
                {'q': 'Reversed WH-Cleft: "What she wants is respect." →', 'o': ['Respect is what she wants.', 'She is wanting respect.', 'What wants is respect.', 'Respect was what she wanted.'], 'a': 0, 'e': 'Reversed: emphasis + is + what clause.'},
                {'q': '"He succeeded BECAUSE OF hard work." → IT-Cleft:', 'o': ['It was hard work that he succeeded.', 'It was because of hard work that he succeeded.', 'Hard work it was he succeeded.', 'Because of work is what succeeded.'], 'a': 1, 'e': 'Выделяем причину: It was because of hard work that...'},
                {'q': 'WH-Cleft для "She enjoys reading." →', 'o': ['It was reading she enjoys.', 'What she enjoys is reading.', 'Reading what she enjoys.', 'She is what enjoys reading.'], 'a': 1, 'e': 'What she enjoys is reading.'},
                {'q': 'IT-Cleft может выделять:', 'o': ['Только подлежащее', 'Только дополнение', 'Любой элемент предложения', 'Только время'], 'a': 2, 'e': 'IT-Cleft выделяет субъект, объект, обстоятельства, причину.'},
                {'q': '"The boss made the decision." → WH-Cleft (субъект):', 'o': ['What the boss made was the decision.', 'It was the boss who made.', 'The boss is what decided.', 'What made the decision was the boss.'], 'a': 3, 'e': 'WH-Cleft для субъекта: What made the decision was the boss.'},
            ],
            'test': [
                {'q': '"They announced the news ON FRIDAY." → IT-Cleft:', 'o': ['It was they who announced on Friday.', 'It was on Friday that they announced the news.', 'Friday was that they announced.', 'What they announced was Friday.'], 'a': 1},
                {'q': 'WH-Cleft: "I want a solution."', 'o': ['It is a solution I want.', 'What I want is a solution.', 'A solution is I want.', 'What want I is solution.'], 'a': 1},
                {'q': 'IT-Cleft: "ALICE wrote the report."', 'o': ['It is Alice who writes the report.', 'It was Alice who wrote the report.', 'What Alice wrote was the report.', 'Alice it was wrote.'], 'a': 1},
                {'q': 'Reversed WH-Cleft: "What we need is cooperation."', 'o': ['Cooperation is what we need.', 'We need cooperation.', 'What cooperation is we need.', 'Need is what we cooperate.'], 'a': 0},
                {'q': '"She called HIM." → IT-Cleft (выделить him):', 'o': ['It was she who called him.', 'It was him that she called.', 'It called was him.', 'What she called was him.'], 'a': 1},
                {'q': 'WH-Cleft: "He enjoys playing chess."', 'o': ['It is chess that he enjoys.', 'What he enjoys is playing chess.', 'Playing chess what he enjoys.', 'He is what enjoys chess.'], 'a': 1},
                {'q': '"They moved to London IN 2020." → выделить время:', 'o': ['It was London they moved.', 'What they did was move.', 'It was in 2020 that they moved to London.', 'They moved it was 2020.'], 'a': 2},
                {'q': 'Функция Cleft sentences:', 'o': ['Упрощение грамматики', 'Выделение и фокусировка', 'Прошедшее время', 'Официальный тон'], 'a': 1},
                {'q': '"She solved it ALONE." → IT-Cleft:', 'o': ['It was alone that she solved it.', 'It was her who solved alone.', 'What alone she solved.', 'She solved it that was alone.'], 'a': 0},
                {'q': 'WH-Cleft: "They need funding."', 'o': ['It is funding that they need.', 'Funding is they need.', 'What they need is funding.', 'They are needing what is funding.'], 'a': 2},
                {'q': '"The CEO approved the plan." → WH-Cleft (субъект):', 'o': ['What approved the plan was the CEO.', 'It was the CEO approved.', 'The CEO is what planned.', 'What CEO is approved.'], 'a': 0},
                {'q': 'IT-Cleft с причиной: "He left BECAUSE HE WAS ANGRY."', 'o': ['It was he who left angry.', 'It was because he was angry that he left.', 'Because angry it was left.', 'He was angry it was that.'], 'a': 1},
                {'q': 'Reversed Pseudo-cleft: ___ is what worries me.', 'o': ['Worry', 'The situation', 'Worried', 'Worrying'], 'a': 1},
                {'q': '"We achieved SUCCESS." → IT-Cleft:', 'o': ['It was success that we achieved.', 'It was we who success achieved.', 'What we it was achieved.', 'Success is it we achieved.'], 'a': 0},
                {'q': 'WH-Cleft vs IT-Cleft: Основное различие?', 'o': ['IT-Cleft только для прошлого', 'WH-Cleft начинается с What, IT-Cleft с It', 'Они одинаковые', 'WH только для вопросов'], 'a': 1},
            ]
        },
        {
            'id': 'c2_g3',
            'title': 'Хеджинг (Hedging)',
            'icon': '🛡️',
            'explanation': (
                '📌 *Хеджинг (Hedging) — Смягчение утверждений*\n\n'
                'Хеджинг — языковые приёмы для выражения неопределённости или осторожности.\n\n'
                '━━━━━━━━━━━━━━━\n'
                '📋 *Средства хеджинга:*\n\n'
                '1️⃣ *Модальные глаголы:*\n'
                '• may/might — It *may* cause problems.\n'
                '• could — This *could* be significant.\n'
                '• would — This *would* suggest...\n\n'
                '2️⃣ *Адвербиалы:*\n'
                '• *arguably* — можно утверждать\n'
                '• *seemingly* — по всей видимости\n'
                '• *presumably* — предположительно\n'
                '• *possibly, perhaps* — возможно\n\n'
                '3️⃣ *Глаголы:*\n'
                '• *seem, appear* — казаться\n'
                '• *suggest, indicate* — предполагать\n'
                '• *tend* — быть склонным\n\n'
                '4️⃣ *Фразы:*\n'
                '• It is possible that...\n'
                '• It would appear that...\n'
                '• To some extent...\n'
                '• In most cases...\n\n'
                '━━━━━━━━━━━━━━━\n'
                '💡 *Зачем нужен:*\n'
                '• Академическое письмо — точность\n'
                '• Бизнес — вежливость\n'
                '• Наука — честность о неопределённости'
            ),
            'exercises': [
                {'q': 'Добавь хеджинг: "___ this approach is effective." (мягкое утверждение)', 'o': ['Definitely', 'It is certain that', 'It would appear that', 'Absolutely'], 'a': 2, 'e': '"It would appear that this approach is effective."'},
                {'q': 'Хеджинг с модалом: "The data ___ suggest a correlation."', 'o': ['definitely', 'would', 'never', 'always'], 'a': 1, 'e': '"would suggest" — осторожное предположение.'},
                {'q': 'Академический хеджинг: "The results ___ indicate..."', 'o': ['absolutely', 'certainly', 'may', 'definitely'], 'a': 2, 'e': '"may indicate" — возможность, не уверенность.'},
                {'q': 'Какое слово является хеджингом?', 'o': ['definitely', 'absolutely', 'arguably', 'certainly'], 'a': 2, 'e': '"Arguably" = можно утверждать — типичный академический хеджинг.'},
                {'q': '"Seemingly, the policy failed." — что означает seemingly?', 'o': ['определённо', 'по всей видимости', 'безусловно', 'явно'], 'a': 1, 'e': 'Seemingly = по всей видимости (hedging adverb).'},
                {'q': 'Добавь хеджинг: "Climate change causes floods."', 'o': ['Climate change certainly causes floods.', 'Climate change may contribute to flooding.', 'Climate change definitely causes floods.', 'Climate change absolutely causes floods.'], 'a': 1, 'e': '"may contribute" — хеджинг вместо категоричного.'},
                {'q': 'Глагол-хеджинг: "The data ___ that emissions are rising."', 'o': ['proves', 'suggests', 'shows exactly', 'confirms absolutely'], 'a': 1, 'e': '"suggests" — более осторожно, чем proves/shows.'},
                {'q': 'Зачем хеджинг в науке?', 'o': ['Избежать ответственности', 'Честно отразить неопределённость', 'Запутать читателя', 'Звучать неуверенно'], 'a': 1, 'e': 'Хеджинг отражает степень уверенности в результатах.'},
                {'q': '"The treatment ___ to reduce symptoms." (тенденция)', 'o': ['proves', 'shows', 'tends', 'ensures'], 'a': 2, 'e': '"tends to" — выражает тенденцию, не закон.'},
                {'q': 'Лучший хеджинг для научного текста:', 'o': ['The results absolutely prove...', 'The results may suggest...', 'The results definitely show...', 'The results clearly confirm...'], 'a': 1, 'e': '"may suggest" — наиболее осторожно.'},
            ],
            'test': [
                {'q': 'Лучший хеджинг для научного текста:', 'o': ['The results absolutely prove...', 'The results may suggest...', 'The results definitely show...', 'The results clearly confirm...'], 'a': 1},
                {'q': '"___ this is the main cause." (хеджинг-наречие)', 'o': ['Certainly', 'Arguably', 'Definitely', 'Obviously'], 'a': 1},
                {'q': 'Модальный хеджинг для неопределённости в прошлом:', 'o': ['will', 'would', 'may have', 'must'], 'a': 2},
                {'q': '"The treatment ___ to reduce symptoms." (показывает тенденцию)', 'o': ['proves', 'shows', 'tends', 'ensures'], 'a': 2},
                {'q': 'Фраза-хеджинг: "It ___ that further research is needed."', 'o': ['is obvious', 'would appear', 'is certain', 'is absolute'], 'a': 1},
                {'q': '"Presumably, the company ___ face challenges."', 'o': ['definitely will', 'will surely', 'might', 'absolutely will'], 'a': 2},
                {'q': 'Хеджинг НЕ нужен для:', 'o': ['Академического письма', 'Юридических документов', 'Экстренных предупреждений', 'Научных статей'], 'a': 2},
                {'q': '"The findings ___ indicate a positive trend."', 'o': ['absolutely', 'would seem to', 'certainly', 'definitely'], 'a': 1},
                {'q': '"To some extent, inflation ___ caused by..." (хеджинг)', 'o': ['is definitely', 'may be', 'is certainly', 'is absolutely'], 'a': 1},
                {'q': 'Наречие-хеджинг в "There has ___ been a decline":', 'o': ['certainly', 'apparently', 'definitely', 'obviously'], 'a': 1},
                {'q': '"The approach ___ be considered effective in most cases."', 'o': ['definitely', 'could', 'certainly', 'always'], 'a': 1},
                {'q': '"___, the intervention helped." — хеджинг-наречие:', 'o': ['Definitely', 'Certainly', 'Apparently', 'Obviously'], 'a': 2},
                {'q': 'Хеджинг с "seem": "The results ___ to confirm..."', 'o': ['absolutely seem', 'seem', 'certainly seem', 'totally seem'], 'a': 1},
                {'q': '"It is ___ that this represents a breakthrough."', 'o': ['certain', 'possible', 'obvious', 'clear'], 'a': 1},
                {'q': 'Хеджинг в бизнесе нужен для:', 'o': ['Угроз', 'Категоричных заявлений', 'Смягчения отказа и критики', 'Утаивания информации'], 'a': 2},
            ]
        },
    ],
    'vocabulary': [
        {
            'category': 'Риторика и стилистика',
            'icon': '🎭',
            'words': [
                {'en': 'rhetoric', 'ru': 'риторика', 'ex': 'His speech was full of empty rhetoric.'},
                {'en': 'metaphor', 'ru': 'метафора', 'ex': 'Life is a journey — that\'s a metaphor.'},
                {'en': 'allusion', 'ru': 'аллюзия', 'ex': 'The allusion to Shakespeare was clear.'},
                {'en': 'euphemism', 'ru': 'эвфемизм', 'ex': '"Passed away" is a euphemism for death.'},
                {'en': 'irony', 'ru': 'ирония', 'ex': 'The irony of the situation was lost on him.'},
                {'en': 'hyperbole', 'ru': 'гипербола', 'ex': '"I\'ve told you a million times" — that\'s hyperbole.'},
                {'en': 'understatement', 'ru': 'преуменьшение', 'ex': 'Calling it "a minor setback" was an understatement.'},
                {'en': 'nuance', 'ru': 'нюанс', 'ex': 'The nuances of the argument were complex.'},
                {'en': 'connotation', 'ru': 'коннотация', 'ex': '"Slim" has positive connotations.'},
                {'en': 'denotation', 'ru': 'денотация (прямое значение)', 'ex': 'The denotation of "snake" is a reptile.'},
            ]
        },
        {
            'category': 'Академические глаголы',
            'icon': '🎓',
            'words': [
                {'en': 'postulate', 'ru': 'постулировать', 'ex': 'The theory postulates that matter is constant.'},
                {'en': 'substantiate', 'ru': 'подкреплять доказательствами', 'ex': 'Please substantiate your claims.'},
                {'en': 'refute', 'ru': 'опровергать', 'ex': 'The evidence refutes the hypothesis.'},
                {'en': 'corroborate', 'ru': 'подтверждать/подкреплять', 'ex': 'New data corroborates the findings.'},
                {'en': 'juxtapose', 'ru': 'сопоставлять', 'ex': 'The author juxtaposes tradition and modernity.'},
                {'en': 'extrapolate', 'ru': 'экстраполировать', 'ex': 'We can extrapolate from these trends.'},
                {'en': 'elucidate', 'ru': 'прояснять', 'ex': 'Please elucidate your position.'},
                {'en': 'delineate', 'ru': 'очертить/обозначить', 'ex': 'The report delineates the key challenges.'},
                {'en': 'reconcile', 'ru': 'согласовать/примирить', 'ex': 'Hard to reconcile these two views.'},
                {'en': 'underpin', 'ru': 'подкреплять/лежать в основе', 'ex': 'Theory underpins practice.'},
            ]
        },
        {
            'category': 'Идиомы высокого уровня',
            'icon': '💡',
            'words': [
                {'en': 'a double-edged sword', 'ru': 'палка о двух концах', 'ex': 'Technology is a double-edged sword.'},
                {'en': 'to beg the question', 'ru': 'предполагать то, что нужно доказать', 'ex': 'This argument begs the question.'},
                {'en': 'the elephant in the room', 'ru': 'очевидная проблема, которую игнорируют', 'ex': 'The funding issue is the elephant in the room.'},
                {'en': 'a slippery slope', 'ru': 'скользкий путь', 'ex': 'This law could lead to a slippery slope.'},
                {'en': 'to play devil\'s advocate', 'ru': 'выступать адвокатом дьявола', 'ex': 'Let me play devil\'s advocate here.'},
                {'en': 'a catch-22', 'ru': 'замкнутый круг (безвыходная ситуация)', 'ex': 'It\'s a catch-22 — you need experience to get a job.'},
                {'en': 'at face value', 'ru': 'за чистую монету', 'ex': 'Don\'t take statistics at face value.'},
                {'en': 'a paradigm shift', 'ru': 'изменение парадигмы', 'ex': 'This represents a paradigm shift in thinking.'},
                {'en': 'to cut corners', 'ru': 'экономить на качестве', 'ex': 'They cut corners on safety.'},
                {'en': 'the thin end of the wedge', 'ru': 'начало опасного прецедента', 'ex': 'This could be the thin end of the wedge.'},
            ]
        },
        {
            'category': 'Философские понятия',
            'icon': '🤔',
            'words': [
                {'en': 'epistemology', 'ru': 'эпистемология (теория познания)', 'ex': 'Epistemology asks: how do we know?'},
                {'en': 'ontology', 'ru': 'онтология (учение о бытии)', 'ex': 'Ontology studies the nature of existence.'},
                {'en': 'dialectic', 'ru': 'диалектика', 'ex': 'Hegel\'s dialectic: thesis, antithesis, synthesis.'},
                {'en': 'determinism', 'ru': 'детерминизм', 'ex': 'Hard determinism denies free will.'},
                {'en': 'nihilism', 'ru': 'нигилизм', 'ex': 'Nihilism rejects all moral principles.'},
                {'en': 'relativism', 'ru': 'релятивизм', 'ex': 'Cultural relativism is a contested idea.'},
                {'en': 'empiricism', 'ru': 'эмпиризм', 'ex': 'Empiricism grounds knowledge in experience.'},
                {'en': 'rationalism', 'ru': 'рационализм', 'ex': 'Rationalism relies on reason, not experience.'},
                {'en': 'scepticism', 'ru': 'скептицизм', 'ex': 'Philosophical scepticism questions everything.'},
                {'en': 'solipsism', 'ru': 'солипсизм', 'ex': 'Solipsism holds only one\'s mind is real.'},
            ]
        },
        {
            'category': 'Лингвистические термины',
            'icon': '🔤',
            'words': [
                {'en': 'pragmatics', 'ru': 'прагматика (изучение контекстного смысла)', 'ex': 'Pragmatics studies language in context.'},
                {'en': 'syntax', 'ru': 'синтаксис', 'ex': 'English syntax follows SVO order.'},
                {'en': 'morphology', 'ru': 'морфология', 'ex': 'Morphology studies word structure.'},
                {'en': 'semantics', 'ru': 'семантика', 'ex': 'Semantics deals with meaning.'},
                {'en': 'register', 'ru': 'регистр (стиль речи)', 'ex': 'Use a formal register in academic writing.'},
                {'en': 'discourse', 'ru': 'дискурс', 'ex': 'Academic discourse is highly structured.'},
                {'en': 'deixis', 'ru': 'дейксис (указательные слова)', 'ex': 'This, that, here, now — deictic expressions.'},
                {'en': 'anaphora', 'ru': 'анафора', 'ex': 'In rhetoric, anaphora repeats the opening.'},
                {'en': 'collocation', 'ru': 'коллокация (устойчивое сочетание)', 'ex': '"Make" collocates with "decision".'},
                {'en': 'phonology', 'ru': 'фонология', 'ex': 'Phonology analyzes sound systems.'},
            ]
        },
    ],
    'phrases': [
        {
            'situation': 'Академическая аргументация',
            'icon': '📜',
            'items': [
                {'en': 'It is worth noting that...', 'ru': 'Стоит отметить, что...', 'note': 'Привлечь внимание'},
                {'en': 'Notwithstanding this, it remains the case that...', 'ru': 'Несмотря на это, по-прежнему верно, что...', 'note': 'Противопоставление'},
                {'en': 'The extent to which this applies is debatable.', 'ru': 'В какой мере это применимо — вопрос дискуссионный.', 'note': 'Ограничение'},
                {'en': 'This is not to say that...', 'ru': 'Это не означает, что...', 'note': 'Уточнение позиции'},
                {'en': 'It is beyond the scope of this paper to...', 'ru': 'Данная работа не ставит целью...', 'note': 'Ограничение объёма'},
                {'en': 'The preponderance of evidence indicates...', 'ru': 'Большинство доказательств свидетельствует о...', 'note': 'Вес доказательств'},
                {'en': 'Taken in isolation, this evidence suggests...', 'ru': 'Если рассматривать вне контекста...', 'note': 'Изолированный анализ'},
            ]
        },
        {
            'situation': 'Публичные выступления',
            'icon': '🎤',
            'items': [
                {'en': 'What I\'d like to leave you with today is...', 'ru': 'Главное, что я хочу вам сказать...', 'note': 'Заключение'},
                {'en': 'The crux of the matter is...', 'ru': 'Суть вопроса заключается в...', 'note': 'Ключевой момент'},
                {'en': 'Let me put this in perspective.', 'ru': 'Позвольте взглянуть на это в перспективе.', 'note': 'Переосмысление'},
                {'en': 'Far from being a weakness, this is...', 'ru': 'Это отнюдь не слабость, это...', 'note': 'Переворот аргумента'},
                {'en': 'The implications of this cannot be overstated.', 'ru': 'Важность этого трудно переоценить.', 'note': 'Подчеркнуть значимость'},
                {'en': 'I think it behoves us all to consider...', 'ru': 'Нам всем следует задуматься о...', 'note': 'Призыв к размышлению'},
            ]
        },
        {
            'situation': 'Хеджинг в разговоре',
            'icon': '🛡️',
            'items': [
                {'en': 'I might be wrong, but...', 'ru': 'Возможно, я ошибаюсь, но...', 'note': 'Оговорка'},
                {'en': 'It\'s hard to say with certainty, however...', 'ru': 'Трудно утверждать с уверенностью, однако...', 'note': 'Неопределённость'},
                {'en': 'This could well be the case, although...', 'ru': 'Это вполне может быть так, хотя...', 'note': 'Осторожное согласие'},
                {'en': 'Without wishing to generalise...', 'ru': 'Не желая обобщать...', 'note': 'Ограничение'},
                {'en': 'I tend to think that... but I\'m open to other views.', 'ru': 'Я склонен думать, что... но открыт к другим взглядам.', 'note': 'Умеренная позиция'},
                {'en': 'The evidence is somewhat ambiguous.', 'ru': 'Доказательства несколько неоднозначны.', 'note': 'Признание неоднозначности'},
            ]
        },
        {
            'situation': 'Критический анализ',
            'icon': '🔬',
            'items': [
                {'en': 'This reasoning is flawed insofar as...', 'ru': 'Это рассуждение ошибочно в той мере, в какой...', 'note': 'Указание на ошибку'},
                {'en': 'One must guard against the temptation to...', 'ru': 'Следует остерегаться соблазна...', 'note': 'Предостережение'},
                {'en': 'A more nuanced reading suggests...', 'ru': 'Более тонкий анализ предполагает...', 'note': 'Углублённый анализ'},
                {'en': 'This conflates two distinct issues.', 'ru': 'Здесь смешиваются два разных вопроса.', 'note': 'Смешение понятий'},
                {'en': 'The premise is questionable at best.', 'ru': 'Предпосылка в лучшем случае сомнительна.', 'note': 'Критика основания'},
                {'en': 'A cursory reading would suggest... however...', 'ru': 'Поверхностное прочтение предполагает... однако...', 'note': 'Углубление анализа'},
            ]
        },
        {
            'situation': 'Стилистические приёмы',
            'icon': '✍️',
            'items': [
                {'en': 'To put it bluntly...', 'ru': 'Говоря прямо...', 'note': 'Прямолинейность'},
                {'en': 'Strange as it may seem...', 'ru': 'Как ни странно...', 'note': 'Неожиданный факт'},
                {'en': 'Make no mistake about it...', 'ru': 'Не заблуждайтесь на этот счёт...', 'note': 'Категоричное утверждение'},
                {'en': 'Suffice it to say that...', 'ru': 'Достаточно сказать, что...', 'note': 'Краткое изложение'},
                {'en': 'All things being equal...', 'ru': 'При прочих равных условиях...', 'note': 'Условие'},
                {'en': 'Not to put too fine a point on it...', 'ru': 'Не вдаваясь в детали...', 'note': 'Упрощение'},
            ]
        },
    ]
}
