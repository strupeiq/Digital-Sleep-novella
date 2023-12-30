# Определение персонажей игры.
define mainCharacter = Character('Миша', color = '#6F47D7')
define dima = Character('Дима', color = '#6F47D7')
define mother = Character('Мама', color = '#6F47D7')
define father = Character('Отец', color = '#6F47D7')
define pythonn = Character('[pythonName]', color = '#6F47D7')
define comment = Character(None, kind = nvl)
define c = Character('Главнокомандующая Си', color = '#6F47D7')
define swift = Character('Swift', color = '#6F47D7')
define java = Character('Java', color = '#6F47D7')
define js = Character('JavaScript', color = '#6F47D7')

define audio.default = "music/default music.mp3"
define audio.classic = "music/classic music.mp3"
define audio.happy = "music/happy music.mp3"
define audio.sad = "music/sad music.mp3"
define audio.fight1 = "music/dinamicfight.mp3"
define audio.fight2 = "music/agrofight.mp3"
define audio.elpeace = "music/electropeace.mp3"
define audio.bags = "sounds/bag sounds.mp3"
define audio.cooking = "sounds/cooking sound.mp3"
define audio.door = "sounds/door sound.mp3"
define audio.heartbeat = "sounds/heartbeat sound.mp3"
define audio.keyboard = "sounds/keyboard sound.mp3"
define audio.phone = "sounds/phone sound.mp3"
define audio.portal = "sounds/portal sound.mp3"
define audio.knock = "sounds/knock.mp3"
define audio.talk = "music/talk.mp3"
define audio.fun = "sounds/fun.mp3"
define audio.peace = "music/peace music.mp3"

init:
    $ rightPosition = Position(xalign = 0.8, yalign = 1.1)
    $ leftPosition = Position(xalign = 0.2, yalign = 1.1)
    $ centre = Position(xalign = 0.5, yalign = 1.1)

label start:

    play music default

    scene bg bus
    with fade

    #Шум общественного транспорта на фоне: болтовня, звуки двигателя.
    "Я ехал домой в автобусе после выпускного."
    "На улице уже стемнело. Подходил к концу мой последний школьный день."
    "Экзамены были сданы, а результаты получены, поэтому все наслаждались заслуженным отдыхом. Все радовались и поздравляли друг друга."
    "Однако я не разделял всеобщего веселья."
    "Меня не покидало чувство, будто я упускаю что-то важное..."

    scene bg blocked phone
    with fade

    "Я достал свой телефон и посмотрел на темный экран."
    "В моих глазах читались усталость и отчаяние."

    scene bg phone chat
    play sound phone volume 0.2

    "Я открыл переписку с друзьями, которые уже решили, куда они поступят."
    "Они обсуждали свои планы на будущее, свои мечты, цели и надежды."
    "Они казались такими уверенными и счастливыми..."
    "А я?"
    "Что насчет меня?"
    "Я не знал, какой путь мне выбрать..."
    "Все, что у меня было, - это любовь к программированию."
    "Но даже здесь у меня возникали сомнения."
    "Я изучал разные языки и технологии, но не чувствовал к ним страсти."
    "Не знал, что лучше подойдет именно мне."

    scene bg bus

    "Сунув телефон в карман, я перевел взгляд на окно."
    "В темноте вечернего города мерцали яркие огни."
    "Словно играя в салочки, они быстро мелькали за окном, не поспевая за движением автобуса."
    "От созерцания завораживающей картины меня отвлек тяжелый вздох друга, который, кажется, в очередной раз не смог пройти уровень в своей любимой игре."
    "Он тоже сидел отдельно ото всех, поэтому я, погруженный в размышления о предстоящем поступлении, решил узнать, как у него обстоят с этим дела."

    mainCharacter "Дим. Ты решил уже, куда поступать будешь?"

    show dima

    "Дима - мой лучший друг. Может, стоит пойти туда же, куда и он... Хотя бы не придется сильно париться по поводу новых знакомств."

    hide dima
    show dima talk

    dima "Я-то? Ну как, в МГУ планирую. Компьютерные науки, все дела..."
    dima "Там же самые лучшие преподы и оборудование. Где еще меня научат всему, что нужно для успешной карьеры в IT?"

    hide dima talk
    show dima fun

    "Его слова звучали уверенно. Явно давно уже решил..."

    mainCharacter "Да... круто."

    "Я ответил без особого энтузиазма."

    hide dima fun
    show dima talk

    dima "Ну чего ты раскис? Протрезвел, что ли?"

    hide dima talk
    show dima megafun

    "Он фыркнул, смеясь над своими же словами."
    "Я толкнул его в бок, сдерживая улыбку. Хоть что-то разбавило обстановку."

    hide dima megafun
    show dima talk

    dima "Ну ладно, ладно. Сам-то что?"
    dima "Тебе же тоже нравится программирование. Просто так инфу на ЕГЭ сдавал, что ли? Тоже ведь в IT хочешь."

    hide dima talk
    show dima

    mainCharacter "Ну, да. Но я уверен только в этом. Не знаю, какую сферу лучше выбрать..."

    "Дима похлопал меня по плечу."

    hide dima
    show dima talk

    dima "Ладно тебе, это ведь не самое важное. Главное, чтобы тебе нравилось то, что ты делаешь. А там уже само разрулится."

    hide dima talk with dissolve

    "Я покачал головой и пожал плечами."
    "Сомневаюсь, что все так просто."

    mainCharacter "Может быть..."

    "Меня вновь охватила тревога."
    "Я ведь все еще даже не выбрал направление, которое меня интересует..."
    "А если я ошибусь? Если не справлюсь? Если потеряю интерес? "
    "Что тогда?"
    "Дима вернулся к своей игре, друзья продолжили общаться между собой, а я остался наедине со своими мыслями."
    "{i}Я чувствовал, что мне нужна помощь.{/i}"
    "Но попросить ее было не у кого..."

    stop music fadeout 1
    scene bg kitchen
    with fade
    play music sad volume 0.8

    "Наконец я вернулся домой."
    "Я был уставшим и раздраженным."
    "Меньше всего сейчас хотелось видеться или говорить с кем-то."
    "Я хотел только одного - побыть в покое."

    mother "Неужели вернулся?"

    "Голос раздался из глубины квартиры. А через несколько секунд мама уже стояла передо мной."

    show mom talk at leftPosition
    with dissolve

    mother "Ну что, как выпускной? Есть будешь?"

    show mom

    "Мама выглядела не менее раздраженной, чем я."

    mainCharacter "Я не голоден, спасибо. Выпускной прошел хорошо."

    "Мама смерила меня недовольным взглядом, явно неудовлетворенная сухим ответом, и принялась накрывать на стол."

    hide mom with moveoutleft
    play sound cooking volume 0.5

    "Я знал, что она хотела поговорить о моем будущем."
    "Она была врачом и хотела, чтобы я пошел по ее стопам, поэтому всегда говорила мне, что врач - благородная и востребованная профессия. Она не понимала, что меня это не интересует."
    "Отец тоже постоянно поднимал эту тему."
    "Он был инженером и мечтал о том, чтобы я поступил в строительный вуз. Его не заботили мои желания и интересы."
    "Еще до сдачи ЕГЭ я соврал им, что давно определился с направлением поступления, думая, что они оставят меня в покое, если увидят уверенность в моих действиях и словах."
    "Но либо им было все равно, либо у меня плохо выходило врать. Их расспросы продолжались."
    "Я уже собирался идти в свою комнату, когда мама окликнула меня, приглашая за стол."

    stop sound

    show mom at leftPosition
    show dad at rightPosition
    with fade

    "Вся семья собралась за ужином. Я присоединился, только чтобы попить чай."
    "Я знал, что скоро начнется разговор, которого я так боялся."

    show dad talk at rightPosition

    father "Ну что, куда документы подавать будешь?"

    show dad at rightPosition

    "Голос отца разрезал тишину, заставляя меня напрячься."

    mainCharacter "Не знаю..."

    "Я пробубнил себе под нос, боясь поднять взгляд на разъяренных родителей. Врать уже не было смысла."

    hide mom
    show mom talk at leftPosition

    mother "Не знаешь?!"

    stop music fadeout 0.5
    play sound knock

    hide mom talk with dissolve
    show mom at centre

    play music talk

    "Мама чуть не вскочила из-за стола, повышая голос."

    show angry mom at centre

    mother "У тебя было столько времени, чтобы определиться! Ты не о том сейчас думаешь! Ходишь по выпускным, шляешься с друзьями... А о будущем кто думать будет? Я, что ли?!"
    hide angry mom with dissolve
    show mom at leftPosition
    mainCharacter "Мам, не кричи..."

    "Очередной шквал возмущений, словно ком, застрял у мамы в горле, когда отец перебил ее, вновь обращаясь ко мне."

    show angry dad at rightPosition

    father "Пора бы уже выбирать. Сколько можно тянуть? Ладно уж, если так нравятся тебе твои компьютеры и игрушки, займись этим. Там много ума не надо: сидишь дома, а тебе деньги платят."

    hide angry dad
    show dad at rightPosition

    "{i}Я понял, что они не воспринимают мои интересы всерьез.{/i}"

    mainCharacter "Нет же! Если бы все было так просто..."

    hide mom
    show angry mom at leftPosition

    mother "Ну и что сложного в твоем программировании?"

    hide angry mom
    show mom at leftPosition

    "Родители пристально смотрели на меня, ожидая ответа."

    mainCharacter "Понимаете, я хочу заниматься этим не только из-за денег... Поэтому мне так важно выбрать то, что будет мне действительно интересно. Я хочу полностью погрузиться в эту сферу."
    mainCharacter "Хочу узнать больше об этом мире, о профессиях, о языках. Но информации так много, что я просто не знаю, с чего начать... Еще эта учеба..."

    hide mom
    show angry mom at leftPosition

    mother "Не знает он, с чего начать. А ты хотя бы пытался?"

    hide angry mom
    show mom at leftPosition

    "Мама не дала мне договорить, подталкивая отца локтем, чтобы он тоже возразил что-то. {i}Родители не собирались меня слушать.{/i}"
    "Они уже были готовы снова разразиться руганью, поэтому я поднялся со своего места и направился к себе в комнату, игнорируя летящие вслед слова."

    hide mom
    hide dad

    stop music
    play sound door

    scene bg computer
    with fade

    play music default

    "Я закрыл за собой дверь и уселся за компьютер. День был окончательно испорчен."

    play sound keyboard

    "Уже не хотелось ничего делать, поэтому я лениво листал сайты и форумы, где люди рассказывали о программировании и своем опыте."
    "Я чувствовал себя растерянно, не находя ничего интересного в их словах."

    stop sound

    "Мне так не хватало помощи и поддержки..."
    "Веки тяжелели, и глаза уже начинали слипаться, поэтому я собирался лечь спать."

    scene bg computer

    "Однако, выключая компьютер, я заметил странный ярлык на рабочем столе. Раньше его тут точно не было."
    "Щелкнув по ярлыку мышкой, я открыл приложение, которое встретило меня ярким сообщением \"{b}Нужна твоя помощь{/b}\" и внезапно начавшейся загрузкой."

    play sound portal

    "Не успел я пошевелиться, как загрузка уже была завершена, экран погас и все погрузилось во мрак."

    stop music fadeout 0.5
    play music elpeace
    scene bg digital world
    with fade

    "Я открыл глаза, не понимая, где нахожусь."
    "Все рябило красным, а проглядывающиеся вдали силуэты напоминали город, словно поглощенный шумом и помехами."
    "Я еще не успел окончательно прийти в себя, когда кто-то подбежал и схватил меня под локоть."

    stop sound

    $ pythonName = "???"

    pythonn "За мной, если жизнь дорога!"

    "Я дернулся в попытке выбраться из крепкой хватки, но незнакомец уже тащил меня в здание с покосившейся вывеской \"SQL\"."

    comment "SQL - это язык программирования, который предназначен для программ управления базами данных."

    scene bg hall
    with fade

    play sound door

    "Незнакомец грубо толкнул меня на пол, оглядываясь по сторонам и закрывая за собой двери."
    "Он представился, не дав мне вставить и слова."

    $ pythonName = "Python"

    show pythonn talk at centre
    with dissolve

    pythonn "Я часовой этой крепости, меня зовут Python."

    hide pythonn talk
    show pythonn normal at centre

    "Кажется, он заметил страх в моих глазах, потому что тут же пояснил."

    hide pythonn normal
    show pythonn talk at centre

    pythonn "Здесь ты в безопасности. В нашем мире сейчас идет война, потому что один из языков решил уничтожить его."

    hide pythonn talk
    show pythonn normal at centre

    mainCharacter "Что за бред..."

    "Человек, представившийся как Python, хмыкнул, понимающе кивая."

    hide pythonn normal with dissolve
    show pythonn talk at leftPosition with dissolve

    pythonn "Я знал, что ты не поверишь. Пожалуйста, просто выслушай..."

    "И он ввел меня в курс дела: он сказал, что сейчас мы находимся в крепости под командованием C и что помимо него в их команде состоят Java, JavaScript и Swift."
    "Он много говорил о C, как о матери всего сущего, и о YoptaScript, который все это устроил и который нужно уничтожить."
    "Я старался вникать в то, что он говорил, но одного я все еще не мог понять."
    "При чем здесь я?"

    hide pythonn talk
    show pythonn normal at leftPosition

    mainCharacter "Допустим, это все правда. Но какое отношение к этому имею я?"
    hide pythonn normal
    show pythonn talk at leftPosition
    pythonn "Думаю, ты, как существо из другого мира, будешь нам полезен."
    pythonn "Пройдем за мной, я покажу тебе, как тут все устроено."

    hide pythonn talk
    show pythonn normal at centre
    hide pythonn normal with dissolve

    "Как мой новый знакомый и попросил, я проследовал за ним."

    stop music
    play music fight1

    scene bg fortress
    with fade

    "Пройдя немало коридоров, мы оказались в комнате со множеством экранов."
    "В центре нее на небольшой возвышенности, повернувшись к нам спиной, стояла женщина."
    "Python шепнул мне на ухо, что эта женщина - Главнокомандующая Си."

    c "Ошибка в правом секторе! Java, нужна подмога в 30 области памяти!"

    "Отдав команду и отвлекшись от мониторов, она обратила на нас свое внимание."

    show ci talk at centre
    with dissolve

    c "Не знаю, что ты такое, но я сразу почувствовала, что в тебе есть необычная сила."

    hide ci talk
    show ci at centre

    "Она обращалась ко мне."

    hide ci
    show ci talk at centre

    c "Когда ты был без сознания, я отправила пару программ узнать, что ты за артефакт."
    c "Но они разрушились, лишь дотронувшись до тебя."

    hide ci talk
    show ci at centre

    "В ее глазах промелькнула ярость, поэтому я сделал пару шагов назад."

    hide ci
    show ci at rightPosition with dissolve

    show pythonn talk at leftPosition
    with dissolve

    pythonn "Извините, Главнокомандующая, но я прикасался к чужаку, и ничего не произошло."

    hide ci
    show ci talk at rightPosition

    c "Что за неосторожность, Python?"

    hide ci talk
    show ci at rightPosition
    show confused pythonn at leftPosition

    "Мой знакомый неловко улыбнулся."

    hide ci
    show ci talk at rightPosition
    hide confused pythonn
    show pythonn normal at leftPosition

    c "Полагаю, языки, как ты и я, имеют иммунитет к этой силе. В любом случае, она нам очень поможет в борьбе с YoptaScript. Этот псевдоязык..."

    hide ci talk
    show ci at rightPosition

    "Главнокомандующая не закончила предложение, но мне стало ясно: так называемый YoptaScript действительно доставляет множество проблем."

    hide ci with dissolve
    hide pythonn normal
    show waylook pythonn at leftPosition

    "Я посмотрел на Python. Для меня он уже стал как наставник, поэтому, когда он махнул головой, я сразу понял, что нужно идти за ним."

    stop music
    play music default

    hide waylook pythonn with dissolve

    show bg hall
    with fade

    show pythonn talk at centre

    pythonn "Ты очень странный, но твоя способность удивительна."

    hide pythonn talk
    show pythonn normal at centre

    mainCharacter "Почему ты сразу не сказал, что у меня есть особая сила?"

    hide pythonn normal
    show pythonn talk at centre

    pythonn "Я просто выполнял приказ Cи. Мне нужно было доставить тебя в целости и посвятить в происходящее. Ничего более."
    pythonn "Но сейчас это уже неважно. Готов ли ты бороться с нами, когда узнал, что происходит?"

    hide pythonn talk
    show pythonn normal at centre

    "Я засомневался."

    mainCharacter "А у меня есть выбор?"

    "Я усмехнулся. Но, увидев строгий взгляд приятеля, заговорил серьезно."

    mainCharacter "Я не могу так просто верить вашим словам. Я не знаю мотивов \"врага\". Вдруг это вы тут злодеи?"
    mainCharacter "Я ничего не знаю о Java, JavaScript, Главнокомандующей Си... да даже о тебе!"

    hide pythonn normal
    show waylook pythonn at centre

    "Python понимающе кивнул."

    hide waylook pythonn
    show pythonn talk at centre

    pythonn "Могу понять твою неопределенность."
    pythonn "Главнокомандующая может показаться жестокой, но она не станет принуждать кого-либо к чему-либо."
    pythonn "Поэтому у тебя есть право голоса."

    hide pythonn talk
    show pythonn happy at centre

    "Мой друг хихикнул, и я тоже невольно улыбнулся."

    hide pythonn happy
    show pythonn fun talk at centre

    pythonn "Если тебе интересно узнать что-то о нас, то я готов рассказать. О ком ты хочешь узнать побольше?"

    hide pythonn fun talk
    show pythonn happy at centre

    $ q = {1: True, 2: True, 3: True, 4: True, 5: True, 6: False}
    while any(q.values()):
        menu:
            "Расскажи мне о..."

            "Себе" if q[1]:
                $ q[1] = False
                $ q[6] = True

                hide pythonn happy
                show pythonn closed eyes hand at centre
                pythonn "Я - один из самых чистых, простых и элегантных языков программирования."
                hide pythonn closed eyes hand
                show pythonn hand at centre
                pythonn "Мне часто говорят, что я похож на Главнокомандующую Си или JavaScript... Возможно, мы действительно похожи внешне."
                pythonn "Моими основными задачами являются: разработка веб-приложений, анализ данных и машинное обучение."
                pythonn "Всем нравится мой простой характер. Но в отличие от других языков, я не выдаюсь универсальностью и скоростью, в чем меня часто упрекает Си!"
                hide pythonn hand
                show pythonn closed eyes hand at centre
                pythonn "Однако я все еще остаюсь полезным и нужным!"
                hide pythonn closed eyes hand
                show pythonn fun talk at centre
                pythonn "Кстати, я уже думал о том, как бороться с YoptaScript..."
                hide pythonn fun talk
                show pythonn happy at centre
                "Какой активный..."

            "Главнокомандующей Си" if q[2]:
                $ q[2] = False
                $ q[6] = True

                hide pythonn happy
                show pythonn talk at centre
                pythonn "Ох, думаю, ты уже заметил, что она дама с характером..."
                hide pythonn talk
                show waylook pythonn at centre
                "Мой друг боязливо оглянулся по сторонам, переходя на шепот."
                hide waylook pythonn
                show pythonn talk at centre
                pythonn "Она имеет огромное влияние в нашем мире, так как является прародительницей многих других языков: C#, C++ и других."
                hide pythonn talk
                show pythonn closed eyes hand at centre
                pythonn "К созданию меня она также приложила руку!"
                "Гордая улыбка засияла на его лице."
                hide pythonn closed eyes hand
                show pythonn fun talk at centre
                pythonn "Ее скорости, эффективности и работоспособности может позавидовать любой язык."
                pythonn "Эти навыки необходимы ей как никому другому, потому что именно она занимается разработкой операционных систем, драйверов, игр и других приложений."
                pythonn "Боюсь представить, какой ценой она развила в себе эти качества!"
                hide pythonn fun talk
                show pythonn talk at centre
                pythonn "Поговаривают, что ради этого ей пришлось отказаться от встроенных структур данных и защиты от ошибок."
                pythonn "Кроме того, ей постоянно приходится самостоятельно управлять памятью главного компьютера."
                pythonn "Но в нашем мире не найдется человека, который не уважал бы Главнокомандующую."
                pythonn "Она давно продумала план действий по борьбе с YoptaScript. И ее решения весьма... категоричны."
                hide pythonn talk
                show pythonn happy at centre
                "Да уж, тяжело ей приходится..."

            "Java" if q[3]:
                $ q[3] = False
                $ q[6] = True

                hide pythonn happy
                show pythonn fun talk at centre
                pythonn "О, эта девушка пользуется огромной популярностью!"
                pythonn "Она является воспитанницей Си, но, как хорошая ученица, она превзошела своего учителя в некоторых начинаниях!"
                hide pythonn fun talk
                show pythonn hand at centre
                pythonn "Например, она не зависит от платформ, умеет автоматически управлять памятью и обладает встроенными коллекциями."
                hide pythonn hand
                show pythonn fun talk at centre
                pythonn "Обычно ее вызывают в главный штаб, когда необходима помощь с разработкой веб- и мобильных приложений."
                hide pythonn fun talk
                show pythonn talk at centre
                pythonn "Она имеет достаточно сложный характер, поэтому у многих могут возникнуть проблемы с пониманием ее хода мыслей."
                hide pythonn talk
                show pythonn fun talk at centre
                pythonn "Но есть у нас с ней и кое-что общее! Она такая же медленная, как я..."
                hide pythonn fun talk
                show confused pythonn at centre
                "Python неловко почесал затылок"
                hide confused pythonn
                show pythonn fun talk at centre
                pythonn "В общем, уверен, что она точно найдет способ борьбы с YoptaScript!"
                hide pythonn fun talk
                show pythonn happy at centre
                "Этот язык выглядит надежным..."

            "JavaScript" if q[4]:
                $ q[4] = False
                $ q[6] = True

                hide pythonn happy
                show pythonn talk at centre
                pythonn "О-о, первое, что я хочу тебе сказать: никогда не путай его с Java!"
                pythonn "Эти двое ненавидят, когда их принимают за один язык. А происходит такое нередко."
                hide pythonn talk
                show pythonn fun talk at centre
                pythonn "Он отличается динамичностью и гибкостью. А еще обладает возможностью работать в браузере! Поэтому зачастую работу в этой сфере поручают именно ему."
                pythonn "Кстати, именно с его трудами ты зачастую взаимодействуешь: изменение страницы, отправление и получение данных - все это его рук дело."
                hide pythonn fun talk
                show pythonn hand at centre
                pythonn "Думаю, мы с ним на одной волне: он такой же энергичный и веселый."
                pythonn "Не сомневаюсь, что у него уже заготовлен особый план по борьбе с YoptaScript."
                hide pythonn hand
                show pythonn happy at centre
                "Интересный язык..."

            "Swift" if q[5]:
                $ q[5] = False
                $ q[6] = True

                hide pythonn happy
                show pythonn fun talk at centre
                pythonn "Это новичок в нашем мире, и пока он только старается влиться в ритм нашей жизни. Однако это не мешает ему быть одним из самых быстрых."
                pythonn "Он, будучи потомком Objective-C, прокачал безопасность памяти и возможность компиляции в машинный код. Поэтому он стал более универсальным, чем предок."
                pythonn "Главнокомандующая Си часто упрекает Swift в его зависимости от Apple, ведь он создан для разработки приложений для iOS, iPadOS, macOS, watchOS и tvOS."
                hide pythonn fun talk
                show pythonn hand at centre
                pythonn "Сейчас он не пользуется популярностью и редко получает поручения, но уверен, когда-нибудь и он покажет себя!"
                hide pythonn hand
                show pythonn fun talk at centre
                pythonn "Возможно, война с YoptaScript - его шанс."
                hide pythonn fun talk
                show pythonn happy at centre
                "Его шанс..."

            "Думаю, я уже решил, за кем хочу следовать" if q[6]:
                hide pythonn happy
                show pythonn fun talk at centre
                pythonn "О, правда? И кто же это?"
                hide pythonn fun talk
                show pythonn happy at centre
                jump chooseLanguage

    "Все языки имеют свои особенности... Но думаю, я уже нашел единомышленника."
    jump chooseLanguage

label chooseLanguage:
    menu:
        "Я выбираю..."

        "Тебя":
            jump pythonEnding

        "Главнокомандующую Си":
            jump cEnding

        "Java":
            jump javaEnding

        "JavaScript":
            jump javaScriptEnding

        "Swift":
            jump swiftEnding
    return

    $ choosedLanguage = ""

label pythonEnding:
    mainCharacter "Ну, выкладывай, что ты там придумал."
    "Кажется, Python был доволен собой."

    show pythonn hand at centre
    pythonn "Рад, что ты выбрал меня. Можешь не волноваться - я не подведу."
    hide pythonn hand
    show pythonn closed eyes hand at centre
    "Он подмигнул мне."
    hide pythonn closed eyes hand
    show pythonn fun talk at centre
    pythonn "Все время, что я помогал Главнокомандующей Си, я так же занимался секретным проектом по разработке искусственного интеллекта, который помог бы в борьбе с YoptaScript."
    pythonn "Это не составило для меня большой сложности, потому что задачка из моего разряда. Но..."
    hide pythonn fun talk
    show pythonn talk at centre
    pythonn "Созданный мной код все еще имеет некоторые неточности и недостатки, что могут привести к неминуемым последствиям для всего нашего мира."
    pythonn "Времени на их исправление слишком мало, поэтому мне бы очень пригодилась твоя сила. Она помогла бы избавиться от багов и недочетов."
    hide pythonn talk
    show pythonn normal at centre
    "Я внимательно слушал Pythonn, размышляя о пользе и эффективности его идеи."
    hide pythonn normal
    show pythonn fun talk at centre
    pythonn "Ну что? Ты со мной?"

    menu:
        "Я думаю, что..."

        "Да":
            $ choosedLanguage = "Python"

            hide pythonn fun talk
            show pythonn closed eyes hand at centre

            "Отлично! Идем за мной."

            show pythonn closed eyes hand with dissolve
            hide pythonn closed eyes hand

            stop music
            play music fight1
            show bg fortress
            with fade

            "Мы снова оказались в командном центре, и Python подвел меня к одному из многочисленных компьютеров."
            show bg storagepc
            with fade
            pythonn "Сейчас мне нужно, чтобы ты подключился к этому компьютеру и внимательно следил за моими движениями."
            pythonn "Я буду указывать на ошибки, а твоей задачей будет лишь касаться их, чтобы устранить все угрозы."
            pythonn "Это может занять некоторое время, поэтому будь готов. Ясно?"
            "Я кивнул."
            mainCharacter "Все ясно."

            play sound keyboard
            "Уже через мгновение мы приступили к работе. Все происходило так, как описал Python: стоило мне лишь дотронуться до участка кода, как он лишался всяких дефектов."
            "Спустя несколько таких преобразований я потерял счет времени, поэтому дернулся, когда почувствовал чужую руку на своем плече."
            stop sound
            pythonn "Эй, ты чего?! Мы закончили. Следуй за мной."
            "Я с трудом поднялся с места и последовал за другом, который уже обращался к Главнокомандующей Си."

            show bg fortress
            with fade

            show ci at rightPosition
            show pythonn talk at leftPosition
            pythonn "Главнокомандующая, извиняюсь за самовольство, но у меня есть кое-что, что может помочь нам в борьбе с YoptaScript."
            hide pythonn talk
            show pythonn normal at leftPosition
            "Си сохраняла спокойтсвие и внимательно слушала Python."
            hide pythonn normal
            show pythonn talk at leftPosition
            pythonn "Я создал искусственный интеллект, с помощью которого мы можем совершить атаку на YoptaScript и легко разобраться с ним без особых потерь."
            pythonn "Можете не сомневаться в его работоспособности. Наш гость помог мне избавиться от всех ошибок и недостатков кода."
            hide pythonn talk
            show pythonn normal at leftPosition

            hide ci with dissolve
            show ci at rightPosition with dissolve:
                xzoom -1.0

            "Главнокомандующая бросила на меня быстрый взгляд."
            "Несмотря на то, что Python уверял ее в надежности кода, она все же быстро просмотрела его, даже не прикасаясь к компьютеру."
            "Удовлетворенно кивнув, Си дала добро."
            hide ci
            show ci talk at rightPosition with dissolve:
                xzoom -1.0

            c "Приступай."
            hide ci with dissolve
            hide pythonn normal

            stop music fadeout 0.8
            play music fight2

            show bg digital world
            with fade

            "Мы приблизились к крепости YoptaScript."
            "Его защита выглядела надежно, однако Python словно не замечал чужих блокировок, умело управляя своим ИИ."
            comment "ИИ - искусственный интеллект."
            "Python легко прорывался сквозь защиту."
            "Я поражался его силе и возможностям."

            show pythonn talk at centre

            stop music fadeout 0.5
            play music peace

            pythonn "С ним покончено."
            hide pythonn talk
            show pythonn normal at centre
            "Я взглянул на остатки синтаксиса и правил YoptaScript, что рассыпался прямо на глазах."
            "Python выделил небольшой участок памяти, сохраняя в нем крупицы побежденного языка."
            hide pythonn normal
            show pythonn talk at centre

            pythonn "Главнокомандующая Си, как слышно? Враг повержен и стерт из нашего мира."
            hide pythonn talk
            show waylook pythonn at centre
            "Я озадаченно посмотрел на своего приятеля. Си дала ему какие-то указания, и он снова обратил на меня свое внимание."
            hide waylook pythonn
            show pythonn talk at centre
            pythonn "Что?"
            pythonn "Не могу я его так просто уничтожить. Он ведь тоже... язык."
            hide pythonn talk
            show waylook pythonn at centre
            "Я понимающе кивнул."
            hide waylook pythonn
            show pythonn fun talk at centre
            pythonn "Поэтому пусть это будет наш маленький секрет. Все равно со всеми проблемами мне разбираться."
            hide pythonn fun talk
            show pythonn talk at centre
            pythonn "Я чувствую, что твоя связь с нашим миром начинает угасать."
            pythonn "Не могу точно сказать, что это значит. Думаю, скоро ты покинешь цифровой мир."
            hide pythonn talk
            show pythonn fun talk at centre
            pythonn "Надеюсь, ты оценил мои возможности и мы еще встретимся! Все зависит лишь от твоего желания."

            hide pythonn fun talk
            stop music
            jump ending

        "Нет":
            hide pythonn fun talk
            show pythonn normal at centre
            "Python погрустнел."
            hide pythonn normal
            show pythonn talk at centre
            pythonn "Что ж, возможно, тогда ты хочешь примкнуть к кому-то другому?"
            hide pythonn talk
            show pythonn happy at centre
            jump chooseLanguage

    return

label cEnding:

    mainCharacter "Я хочу сражаться на стороне Си."
    "Python одобрительно кивнул и попросил следовать за ним."

    stop music fadeout 0.5
    play music fight1
    hide pythonn fun talk
    show bg fortress
    with fade
    show ci at centre

    "Когда мы вернулись в центр управления, Си все еще была там, будто зная, что мы должны были вернуться к ней."
    mainCharacter "Я готов выслушать ваш план по борьбе с YoptaScript."
    "Главнокомандующая коротко кивнула, быстро прокликивая что-то на мониторах."

    hide ci
    show ci talk at centre

    c "Итак, я разработала программу, которая способна создавать туннель, позволяющий мне проникать в другие базы, оставаясь незамеченной."
    c "С его помощью я рассчитываю нарушить порядок в системе YoptaScript."
    c "Однако, к сожалению, мне не удалось узнать, насколько хороша защита YoptaScript, сколько бы вылазок мы не устраивали."
    c "Полагаю, что все не так просто. Поэтому мне нужна уверенность в собственной стратегии. Подушка безопасности."
    c "Времени на улчшение программы нет. Нужно действовать быстро."
    c "Твоя сила идеально подходит мне. Сомневаюсь, что в нашем мире для нее есть какие-либо преграды."
    c "Вместе мы уничтожим этот недоязык. Ты со мной?"

    hide ci talk
    show ci ha at centre

    menu:
        "Я думаю, что..."

        "Да":
            $ choosedLanguage = "C"

            "Она улыбнулась и снова перевела свое внимание на мониторы."

            hide ci ha
            show ci talk at centre

            c "Я рада, что ты на моей стороне. Ты сделал правильный выбор."
            c "Сейчас я запущу программу, которая создаст туннель в сеть YoptaScript и позволит мне войти в нее."
            c "Но туннель будет очень нестабилен и уязвим. Тебе нужно будет защищать его от атак YoptaScript и его сторонников."
            c "Ты должен использовать свою силу, чтобы уничтожать их код, который будет пытаться проникнуть в туннель или закрыть его."
            c "Все ясно?"

            hide ci talk
            show ci at centre

            mainCharacter "Да, я все понял. Давай начнем."

            hide ci with dissolve
            stop music fadeout 0.5
            play music fight2
            show bg tunnel with fade

            "Я подключился к компьютеру и увидел на экране туннель, который вел к крепости YoptaScript."
            "Си вошла в него и исчезла. Вражеские коды попытались атаковать туннель. Но я использовал свою силу, чтобы стирать их. Туннель трещал и дрожал."
            "Я чувствовал, как моя сила уменьшается, и не знал, сколько я смогу выдержать."

            c "Я дошла до крепости YoptaScript. Я вижу его код, эмоции, желания. За мной!"

            "Голос Си доносился откуда-то издалека, поэтому я просто старался следовать за звуком ее голоса."

            c "Я отвлеку YoptaScript. Дальше дело за тобой. Сотри его."

            "Код YoptaScript был вплотную ко мне. Я протянул к нему ослабшую руку, и он начал распадаться на пиксели."
            show bg tunnel with vpunch
            "Туннель начал разрушаться. А я чувствовал, как моя сила иссякает и что я теряю сознание."

            show bg fortress
            stop music
            play music peace
            show ci ha at centre with dissolve

            "Я открыл глаза и осознал, что нахожусь в крепости Си. Она стояла надо мной и улыбалась."

            hide ci ha
            show ci ha talk

            c "Благодаря тебе мы справились!"

            hide ci ha talk
            show ci ha

            play sound fun

            "По командному центру пронеслась волна радостных выкриков и возгласов."

            hide ci ha
            show ci ha talk

            c "Опасность устранена, поэтому нашему миру больше ничего не угрожает."
            c "Думаю, какую-то выгоду из сложившейся ситуации вынесли не только мы, не так ли?"

            hide ci ha talk
            show ci ha

            "Я задумался, вспоминая, сколько нового узнал о цифровом мире, языках программирования и их устройстве."
            "Пожалуй, Си была права."

            hide ci ha
            show ci ha talk

            c "Надеюсь, что ты сможешь сделать для себя выводы и выбрать собственный путь в программировании. С кем-то из нас ты еще точно пересечешься."

            play sound portal

            c "Мы еще обязательно встретимся."

            hide ci ha talk
            show ci ha

            "Си улыбнулась мне, и я ощутил такое же странное чувство, как то, когда я переместился сюда."

            hide ci ha
            stop music
            stop sound
            jump ending

        "Нет":

            hide ci ha
            show ci at centre
            "Дружелюбный взгляд Си резко сменился на враждебный."
            hide ci
            show ci talk at centre
            c "Python, проводи, пожалуйста, нашего гостя."

            hide ci talk
            show ci at centre
            hide ci with moveoutright

            "Я покосился на Python."

            show pythonn talk at leftPosition
            with dissolve

            pythonn "Так точно."

            show bg hall
            with fade

            pythonn "Ты чего это?"
            pythonn "Что ж, возможно, тогда ты хочешь примкнуть к кому-то другому?"
            hide pythonn talk
            show pythonn happy at leftPosition
            jump chooseLanguage

    return

label swiftEnding:

    mainCharacter "Мне бы хотелось узнать о планах Swift поподробнее."
    hide pythonn fun talk
    show pythonn hand at centre

    pythonn "О, тебя заинтересовал этот новичок? Что ж, тогда мне придется вас познакомить. Кажется, я видел его в командном центре, когда мы уходили."
    pythonn "Пошли за мной."

    stop music fadeout 0.5
    play music fight1
    hide pythonn hand with dissolve
    show bg fortress
    with fade
    show pythonn fun talk at centre

    pythonn "Дай мне секунду."

    hide pythonn fun talk
    show pythonn happy
    hide pythonn happy with moveoutright

    "Я замер в ожидании, размышляя о том, какие идеи могут быть у Swift."

    show pythonn happy at leftPosition
    with dissolve
    show swiftt ha open at rightPosition
    with dissolve

    swift "Привет, незнакомец! Меня зовут Swift. Мне тут нашептали, что ты хочешь помочь мне?"
    hide swiftt ha open
    show swiftt ha at rightPosition
    mainCharacter "Было бы неплохо для начала узнать, в чем заключается твой план."
    hide swiftt ha
    show swiftt nervous at rightPosition
    swift "Ах, и правда. Итак, поскольку я специализируюсь на разработке приложений для Apple, то для меня может быть несколько проблематична реализация моего плана."
    hide swiftt nervous
    show swiftt ha open at rightPosition
    swift "Не подумай, что я не могу тебе предложить что-то толковое! Ты бы просто мог послужить проводником."
    swift "Так как приложение, над которым я работаю в последнее время, чтобы помочь в борьбе с YoptaScript, применимо только для техники Apple..."
    hide swiftt ha open
    show swiftt nervous at rightPosition
    swift "У меня нет возможности очистить весь наш мир от угрозы со стороны этого языка."
    swift "Думаю, я создам только больше проблем, если попытаюсь..."
    hide swiftt nervous
    show swiftt confused at rightPosition
    "Я заметил, как Swift засомневался, но тут же приободрился."
    hide swiftt confused
    show swiftt ha open at rightPosition
    swift "Но появился ты, и я подумал, что ты сможешь расширить мои возможности! Вместе мы очистим цифровой мир от {b}грязи{/b}."
    swift "Ну как? Ты со мной?"

    menu:
        "Я думаю, что..."

        "Да":
            $ choosedLanguage = "Swift"

            swift "Правда?! Отлично! Тогда мы можем приступить прямо сейчас. Дай мне секунду."
            hide swiftt ha open with dissolve
            hide pythonn happy 
            show pythonn happy at centre
            play sound keyboard
            "Я наблюдал за тем, как Swift нажимает странные комбинации клавиш на клавиатуре у ближайшего к нам монитора, и все еще не понимал, что именно от меня требуется."
            stop sound
            mainCharacter "Эй, Swift, а мне что делать?"
            "Swift, увлеченный работой, ответил мне только спустя несколько секунд."
            swift "А, да, ты расширишь мои возможности при помощи своей силы!"
            "Я глупо посмотрел на свои руки. Я? Каким образом?"
            mainCharacter "Но как? Я умею только разрушать ваш мир..."

            hide pythonn happy
            show pythonn talk at centre with dissolve:
                xzoom -1.0

            pythonn "И правда. Я и сам был сведетелем его разрушений. Многие языки хотят заполучить его силу именно ради этого... Чтобы навсегда уничтожить YoptaScript."
            hide pythonn talk
            show pythonn normal at centre:
                xzoom -1.0
            "Python говорил с некоторым осуждением. Ему явно не нравились радикальные идеи других языков."
            hide pythonn normal with dissolve
            show pythonn normal at leftPosition
            show swiftt ha open at rightPosition
            swift "Я тоже собираюсь уничтожить его. Только ты у нас такой неженка. А мне надо заполучить доверие со стороны других языков."
            hide swiftt ha open
            show swiftt angry at rightPosition
            "Я наблюдал за их небольшой перепалкой, не решаясь вставить лишнего слова."
            hide swiftt angry
            show swiftt ha open at rightPosition
            swift "Итак, все готово. Сейчас я дам тебе доступ к своим архивам и коду приложения."
            swift "Твоя задача заключается в том, чтобы связать его с главным компьютером. Ты же можешь разрушить что угодно?"
            swift "Защита, которую поставила Главнокомандующая Си, надежна, но думаю, ты со своей силой легко ее пробьешь."
            hide swiftt ha open
            show swiftt ha at rightPosition
            mainCharacter "А это вообще законно?.."
            "Swift рассмеялся, подталкивая меня вперед."
            hide swiftt ha
            show swiftt ha open at rightPosition
            swift "Не волнуйся, наши законы на тебя не действуют, а удержать мы тебя не сможем. А Python меня не сдаст. Еще в соучастников запишут."
            hide swiftt ha open
            show swiftt ha at rightPosition
            hide pythonn normal
            show pythonn talk at leftPosition
            pythonn "Думаю, нам уже пора приступать."

            hide pythonn talk
            hide swiftt ha with fade

            "Языки отошли на несколько шагов назад, чтобы не мешать мне."

            stop music
            play music elpeace
            show bg codedef

            "Я взглянул на множество строк кода передо мной и прикоснулся к одной из них."

            swift "Все правильно! Продолжай в том же духе!"

            "Я не понимал, что делаю, но, судя по ободряющим словам Swift, все шло так, как надо."
            "Несколько экранов загрузки появились передо мной на секунду, а потм исчезли."
            "В этот же момент Swift начал активнее что-то печатать."

            swift "Отлично. Еще немного."

            "Прошло еще некоторое время, пока Swift что-то исправлял, а затем я резко потерял соединение с главным компьютером."

            stop music
            play music fight1
            show bg fortress
            with fade
            show swiftt ha open at rightPosition with dissolve
            show pythonn normal at leftPosition with dissolve

            swift "Все прошло успешно! YoptaScript стерт с лица цифрового мира."
            hide swiftt ha open
            show swiftt ha at rightPosition
            "Я был немного разочарован тем, что не смог взглянуть на главного злодея до его уничтожения, но быстро отбросил эти мысли."
            show swiftt nervous at rightPosition
            swift "Остается надеяться на то, что Си поверит в сказки о том, что это YoptaScript пробил ее защиту."
            hide swiftt nervous
            show swiftt confused at rightPosition
            hide pythonn normal
            show pythonn talk at leftPosition
            pythonn "Точно. Нужно доложить о произошедшем Главнокомандующей Си."
            hide pythonn talk
            show pythonn normal at leftPosition
            hide swiftt confuesd
            show swiftt ha open at rightPosition
            swift "Да-да, давай беги."

            hide pythonn normal with moveoutleft
            hide swiftt ha open
            show swiftt ha open at centre with dissolve

            swift "Ну что, я крут? Скажи ведь."
            hide swiftt ha open
            show swiftt ha at centre
            "Я молча кивнул в ответ. Swift действительно показался мне сообразительным и интересным."
            hide swiftt ha
            show swiftt nervous at centre
            swift "Спасибо за помощь. Но мое приложение было действительно достойным, хоть и ограниченным в возможностях."
            hide swiftt nervous
            show swiftt ha open at centre
            swift "Надеюсь, на тебя это тоже произвело впечатление."
            swift "Ты выглядел потерянным, когда я тебя только увидел. Но сейчас ты стал увереннее. Понравился цифровой мир, да?"
            swift "Что ж, надеюсь, ты не забудешь обо мне!"
            hide swiftt ha open
            show swiftt at centre
            "Я хотел еще поболтать со Swift, но разум вдруг затуманился, и я почувствовал, как меня поглощает темнота."
            hide swiftt
            stop music
            jump ending

        "Нет":
            hide swiftt ha open
            show swiftt nervous at rightPosition
            swift "Ну и ладно... Думаю, если я самостоятельно продолжу разработку, то выберусь за пределы своих возможностей..."
            hide swiftt nervous
            show swiftt angry at rightPosition
            "В его взгляде промелькнули злость и раздраженность."

            hide swiftt angry with moveoutright
            hide pythonn happy
            show pythonn talk at centre
            pythonn "Кажется, знакомство у вас не задалось... Ну ничего, возможно, ты хочешь еще поразмышлять о том, за кем пойти?"
            pythonn "Пошли в коридор. Не будем мешать чужой работе."

            hide pythonn talk
            show pythonn normal at centre
            show bg hall
            with fade
            hide pythonn normal
            show pythonn talk at leftPosition
            pythonn "Ну что, успел подумать?"
            hide pythonn talk
            show pythonn happy at leftPosition
            jump chooseLanguage

    return

label javaEnding:

    mainCharacter "Я бы хотел познакомиться с Java и узнать о ее идеях побольше."
    hide pythonn happy
    show pythonn fun talk at centre
    pythonn "Без проблем! Слышал, она давно занимается анализом тонкостей структуры YoptaScript и собирается помочь Си в борьбе с ним."
    pythonn "Давай пройдем в хранилище данных. Java там целыми днями зависает..."

    stop music fadeout 1
    hide pythonn fun talk
    show bg storage
    with fade
    play music peace

    show javaa talk at leftPosition
    java "Ну, привет, Миша."
    hide javaa talk
    show javaa at leftPosition
    "Я застыл на месте, не понимая, откуда ей известно мое имя и почему она выглядит так, будто все это время ждала нашего появления."
    mainCharacter "Откуда ты знаешь мое имя?.."
    hide javaa
    show javaa talk at leftPosition
    java "Мне известно все, что проникает в этот мир, и все, что из него выходит. Даже такие недоразумения, как ты, не проходят мимо меня."
    hide javaa talk
    show javaa talk at leftPosition with dissolve:
        xzoom -1.0

    java "Я знала, что вы явитесь ко мне. Python, где вас столько носило?"

    hide javaa talk
    show javaa at leftPosition:
        xzoom -1.0
    show pythonn hand at rightPosition

    pythonn "Нужно было доложить о ситуации Главнокомандующей Си. Пришлось немного побегать."
    pythonn "Мы пришли, потому что Миша хотел узнать больше о твоих планах."
    hide pythonn hand
    show pythonn happy at rightPosition
    hide javaa
    show javaa talk at leftPosition:
        xzoom -1.0
    java "Раз уж так... Слушай внимательно."
    java "Мы с Си давно разрабатываем совместный план по уничтожению этого недоязыка. Пока Си разрабатывает программу, я собираю данные и строю алгоритм."
    java "В последнее время находить информацию о YoptaScript и его перемещениях стало сложнее, что мешает поддерживать актуальность плана."
    java "Этот язык адаптировался и научился скрываться. Но нам важны уверенность в создаваемом алгоритме и точность. Иначе программа Си лишь усугубит положение."
    java "Твое умение удалять некоторые компоненты нашего мира помогло бы мне отсеивать ложную и сомнительную информацию."
    java "Я не доверю тебе управление всем хранилищем, поэтому от тебя требуется лишь небольшое содействие. Ну что, ты в деле?"
    hide javaa talk
    show javaa at leftPosition:
        xzoom -1.0

    menu:
        "Я думаю, что..."

        "Да":
            $ choosedLanguage = "Java"

            hide javaa
            show javaa talk at leftPosition
            java "Отлично. В таком случае, предлагаю приступить к работе прямо сейчас. Чем раньше закончим, тем раньше я предоставлю всю информацию Си."
            java "А ты, Python, свободен. Не мешайся под ногами."

            hide javaa talk
            hide pythonn happy
            show bg storagepc
            stop music
            play music fight1

            "Java усадила меня за компьютер, который стоял в самом углу между многочисленных стеллажей."
            java "Итак, все предельно просто. Сейчас я запущу программу, которая соберет с нашего мира всю информацию, в которой хоть как-то фигирирует YoptaScript."
            java "Действовать нужно быстро, чтобы не допустить перегрузки системы, поэтому смотри в оба."
            java "Я начинаю. Будь готов."

            show bg filess
            with fade

            "В следующее мгновение перед моими глазами всплыло множество информации. Я видел, как Java ловко фильтрует данные, выделяя важные и полезные фрагменты."
            "Однако спустя некоторое время поток данных стал усиливаться."

            java "Вот об этом я и говорила. Я перенаправляю на тебя сомнительные файлы."
            java "Тебе нужно лишь прикасаться к ним. Если от них что-то останется после твоего прикоснавения, то оставляй их мне."
            java "Больше ничего не трогай. Я разберусь с этим."

            "Я сделал все так, как она попросила, не до конца понимая, что несет в себе фильтруемая информация, но полностью погружаясь в процесс."
            java "Я закончила. Алгоритм работает, и на данный момент есть возможность расширения функционала программы. Отключаю тебя от системы."

            show bg storage
            with fade
            show javaa think at centre
            stop music
            play music peace

            "Java выглядела задумчиво, поэтому я поинтересовался, что ее так озадачило."

            hide javaa think
            show javaa talk at centre

            java "Дело в том, что нам с Си YoptaScript представлялся вредоносным вирусом, который не имеет ничего общего с другими языками."
            java "Но оказалось, что он тоже имеет \"скелет\". Синтаксис у него сомнительный, но это не делает его плохим языком, не думаешь?"

            hide javaa talk
            show javaa think at centre

            "Я озадаченно смотрел на Java."

            hide javaa think
            show javaa talk at centre

            java "Возможно, стоит дать ему второй шанс и попытаться вывести его на диалог..."

            hide javaa talk
            show javaa think at centre

            menu:
                "Я думаю..."

                "Это отличная идея":

                    mainCharacter "Если он такой же, как вы, то вы точно сможете найти общий язык и решить все мирно."
                    "Java задумчиво кивнула."
                    hide javaa think
                    show javaa talk at centre
                    java "Да, вероятно... Тогда нужно предупредить Си. Следуй за мной."
                    hide javaa talk
                    show javaa at centre

                    stop music fadeout 1
                    play music elpeace
                    hide javaa moveoutright
                    show bg fortress
                    show ci at rightPosition
                    show javaa at leftPosition:
                        xzoom -1.0

                    "Мы оказались в командном центре, где все еще находила Си, выполняя свою работу."

                    hide javaa
                    show javaa talk at leftPosition:
                        xzoom -1.0

                    java "Глвнокомандующая, позвольте предоставить Вам результаты анализа и возможные варианты развития событий."
                    hide javaa talk
                    show javaa at leftPosition:
                        xzoom -1.0
                    "Си кивнула, готовая внимательно слушать."
                    hide javaa
                    show javaa talk at leftPosition:
                        xzoom -1.0
                    java "Исходя из полученных данных, могу Вас заверить в том, что YoptaScript не представляет глобальной угрозы для цифрового мира."
                    java "Это означает, что он может быть обезврежен без полного удаления его компонентов из системы."
                    java "Кроме того, документация говорит о его принадлежности к таким же языкам, как мы. Поэтому..."
                    java "С Вашего позволения я бы могла внести в программу алгоритм, который не сотрет YoptaScript, но значительно ослабит его. Это будет удобным для переговоров."
                    hide javaa talk
                    show javaa at leftPosition:
                        xzoom -1.0
                    hide ci
                    show ci talk at rightPosition
                    c "Если все действительно так, как ты описала, то я согласна попробовать твою идею. Оставь изначальный алгоритм в качестве подстраховки."

                    hide ci talk with dissolve
                    "Java подключилась к одному из мониторов и переслала Си собранные данные."

                    hide javaa
                    show javaa talk at centre
                    java "Готово. Нам понадобится еще некоторое время на решение проблемы, но ты сильно облегчил нам работу."
                    java "Спасибо за помощь. Думаю, мы тоже помогли тебе решить для себя что-то, да?"
                    java "Ты так много узнал о нас и нашем мире, что могу понять свое замешательство. Не волнуйся, чем больше ты погружаешься в наш мир, тем понятнее он тебе становится."
                    java "Не сомневаюсь в том, что мы еще обязательно встретимся."
                    hide javaa talk
                    show javaa at centre
                    "Мне хотелось задать еще так много вопросов, но перед глазами все поплыло, и я почувствовал странную слабость."
                    stop music
                    hide javaa
                    jump ending

                "Не стоит рисковать":
                    mainCharacter "Мы не можем знать, во что в будущем превратиться YoptaScript. Лучше сразу обезопасить себя."

                    "Java некоторое время молчала, задумчиво глядя в сторону."

                    hide javaa think
                    show javaa talk at centre
                    java "Да, ты прав. Тогда остается лишь передать собранную информацию Си."

                    hide javaa talk
                    show javaa at centre

                    "Java подключилась к одному из мониторов и переслала Си собранные данные."

                    hide javaa
                    show javaa talk at centre

                    java "Что ж, совсем скоро с YoptaScript будет покончено. Дело остается за Си и ее программой. Думаю, мне стоит поблагодарить тебя."
                    java "Полагаю, мы помогли тебе не меньше, чем ты нам. Цифровой мир удивителен, не так ли?"
                    java "Мы еще обязательно встретимся, а сейчас тебе пора возвращаться."
                    hide javaa talk
                    show javaa at centre
                    "Мне хотелось задать еще так много вопросов, но перед глазами все поплыло, и я почувствовал странную слабость."
                    stop music
                    hide javaa
                    jump ending
            return

        "Нет":
            hide javaa
            show javaa talk at leftPosition
            java "Надо же. Ну, как скажешь. Думаю, эта сделка была бы выгодна всем."
            java "Ты ведь тоже находишься в затруднительном положении и оказался здесь не просто так, не так ли?"
            hide javaa talk
            show javaa at leftPosition
            "Я стушевался. Сложилось впечатление, будто Java знает все не только о цифровом мире..."

            "Хотелось расспросить ее об этом, но Python уже потянул меня обратно в коридор."

            hide javaa
            show bg hall
            stop music
            play music default
            show pythonn fun talk at leftPosition
            with dissolve

            pythonn "Что ж, возможно, тогда ты хочешь примкнуть к кому-то другому?"
            hide pythonn fun talk
            show pythonn happy at leftPosition
            jump chooseLanguage
    return

label javaScriptEnding:

    mainCharacter "Мне было бы интересно узнать, какой план действий может предложить JavaScript."
    hide pythonn happy
    show pythonn fun talk at centre

    pythonn "Слышал, он сейчас занимается разработкой какого-то веб-приложения... Думаю, он будет рад нас видеть. Пойдем за мной."

    stop music fadeout 1.0
    play music elpeace
    hide pythonn fun talk
    show bg scriptroom
    with fade

    "Python привел меня в темную комнату, полную мониторов. Я оглянулся по сторонам в поисках JavaScript."
    "Пока я рыскал взглядом по углам небольшой комнаты, он уже оказался прямо передо мной."

    show javascript with moveinright
    js "Привет! Так это ты, тот самый объект, наделавший кучу шума в нашем мире?"
    "Не успел я ответить, как JavaScript заговорил вновь. Да уж, Python не врал, когда говорил о его энергичности. Хотя такое поведение совсем не вязалось с его внешностью."
    hide javascript
    show javas fun
    js "Я наслышан о твоих невероятных способностях! Знаешь, мне пришла в голову мысль, что ты и твоя сила очень помогли бы мне в моем проекте!"
    mainCharacter "Был бы рад тебе помочь, но я даже не знаю, что тебе от меня требуется..."
    hide javas fun
    show javascript
    js "Ах, да, прости, совсем забылся!"
    "Мой новый знакомый еще больше оживился, готовый рассказать о всех своих планах."
    js "Итак, я специализируюсь на разработке веб-приложений, поэтому при всем своем желании не смогу устранить корень проблемы."
    hide javascript
    show javas fun
    js "Но мне очень хочется внести свой вклад в победу над YoptaScript, поэтому я намереваюсь предоставить программный доступ к объектам приложения, создаваемого Java и Си."
    hide javas fun
    show javascript
    js "Проще говоря, я беру на себя ответственность за интерфейс и его функциональность."
    js "Кроме того, есть еще кое-что, что я хочу добавить в свое приложение. Но это секрет."
    "Я не мог видеть эмоций JavaScript, поскольку его лицо было скрыто маской, однако в его глазах промелькнул азарт."
    js "Но для реализации всего этого мне нужен гарант надежности, чтобы не подставить весь командный центр. А у меня с этим проблемы... Поэтому мне нужна твоя помощь."
    hide javascript
    show javas fun
    js "Ну что, как тебе моя идея? Ты со мной?"

    menu:
        "Я думаю, что..."

        "Да":
            $ choosedLanguage = "JavaScript"

            hide javas fun
            show javas blink
            js "Ура! Я знал, что тебе понравится моя идея!"
            hide javas blink
            show javascript
            js "Тогда мы можем прямо сейчас приступить к ее реализации. От тебя потребуется не так много. Нужно лишь отредактировать код, удалив из него некоторые элементы."
            js "Пойдем за мной."

            hide javascript with moveoutleft
            show bg storagepc with fade

            "Мы прошли к одному из многочисленных компьютеров."
            js "Для улучшения надежности потребуется внести правки в код. Тебе нужно лишь просканировать все строчки, касаясь каждой из них."
            js "Твоя сила должна уничтожить все лишние функции и строчки. Я возьму на себя редактирование. Готов?"
            "Я кивнул, и мы приступили к монотонной, но необходимой работе."

            stop music fadeout 0.5
            play music default

            show bg scriptroom with fade

            "Я потерял счет времени, когда понял, что дошел до последней строчки кода. JavaScript тоже оторвался от экрана."

            show javas fun with dissolve

            js "Спасибо за помощь! В одиночку я бы делал это гораздо дольше. Осталось перенаправить это все Си для повторной проверки."

            hide javas fun with moveoutright

            "JavaScript вновь отошел к компьютеру. А я вдруг вспомнил о секретном компоненте приложения, о котором JavaScript умолчал."
            mainCharacter "Слушай, а ты ведь говорил что-то о \"кое-чем, что ты хотел бы добавить в свое приложение\". Что это?"
            js "А, ты все еще помнишь об этом. Придется раскрыть карты. Подойди сюда."

            stop music fadeout 0.5
            play music peace
            show bg comments
            with fade

            "Я подошел к компьютеру, за которым сидел JavaScript, чтобы рассмотреть, что было написано на экране."
            "Перед глазами мелькало множество сообщений и комментариев, заголовки, в которых фигурировало имя YoptaScript, и огромное количество файлов и ссылок."

            mainCharacter "Что это такое?.."
            js "Это второе приложение, которое я разработал, пока ты возился с кодом."
            js "Это сайт, на котором отражены все \"грехи\" YoptaScript со всевозможными доказательствами и опровержениями."
            js "Как видишь, система отлично работает. Куча гневных комментариев и отвернувшихся от него сторонников."

            show bg scriptroom with fade
            show javascript at rightPosition with dissolve

            "Мы отошли от компьютера, и JavaScript продолжил свою мысль."
            js "Если я не могу победить YoptaScript напрямую, то буду помогать всеми силами остальным языкам."
            js "Разработанное мной приложение уже находится в руках Главнокомандующей, а сайт сильно испортил репутацию YoptaScript."
            js "Это скажется на его силе. Многие отвернутся от него, поэтому он будет ослабевать и наша победа станет лишь вопросом времени."
            "Я внимательно слушал JavaScript, не сомневаясь в важности его вклада."
            mainCharacter "Никогда бы не подумал, что веб-сайты могут обладать такой силой."
            hide javascript
            show javas blink
            js "Теперь будешь знать! Очень надеюсь, что мы с тобой еще встретимся."
            hide javas blink
            show javascript
            js "А теперь мне пора идти помогать Си с дальнейшими действиями."

            hide javascript with dissolve

            "Я проводил взглядом JavaScript и вдруг почувствовал легкое головокружение, а перед глазами все поплыло."
            stop music fadeout 0.5
            jump ending

        "Нет":
            hide javas fun
            show javascript
            "Я заметил, как огонек в глазах JavaScript погас."
            js "Ну... как скажешь. Думаю, я смогу справиться с этой проблемой, если посижу с этим подольше."
            hide javascript with moveoutright
            stop music
            play music default
            show bg hall with fade
            show pythonn talk at leftPosition
            pythonn "Что такое?"
            hide pythonn talk
            show pythonn normal at leftPosition
            mainCharacter "Идея JavaScript показалась мне сомнительной, поэтому я решил не помогать ему."
            hide pythonn normal
            show pythonn fun talk at leftPosition
            pythonn "Тогда, возможно, ты хочешь присоединиться к кому-то другому?"
            hide pythonn fun talk
            show pythonn happy
            jump chooseLanguage
    return

label ending:
    play music default
    show bg computer
    with fade
    "Я открыл глаза и обнаружил себя сидящим за компьютером. Я что, так и заснул здесь?"
    "События вечера и ночи пронеслись перед глазами. Я резко все осознал."

    play sound door
    show bg room
    show angry mom at centre with dissolve

    mother "Господи, заснул за компьютером! Ну как так можно! Снова всю ночь в игрушки играл?"
    "Мама недовольно смотрела на меня, но я не замечал ни ее злости, ни собственной усталости, потому что..."

    mainCharacter "Мама, я наконец-то решил!"
    hide angry mom
    show happy mom at centre
    "Удивительно, как простой сон после тяжелого дня помог мне определиться с тем, что не давало мне спокойно жить столь долгое время."
    "Однако меня уже мало волновало, сколько времени мне потребовалось на осознание. Ведь теперь все было в порядке."
    "Внутри больше не было сомнений и терзаний. Я точно знал, кем хочу стать."
    "Почувствовав легкость, я наконец смог уверенно сказать..."
    mainCharacter "Я буду разработчиком на [choosedLanguage]!"
