### Оглавление
1. [Про Python](#python)
2. [Установка Python](#установка-python)
3. [Про PyCharm](#pycharm)
4. [Установка и настройка PyCharm](#установка-и-настройка-pycharm)

# Python
### Python это высокоуровневый интерпретируемый язык программирования общего назначения.

Что это означает:

**Высокоуровневый:** Код, написанный на высокоуровневом языке (понятный человеку), впоследствие трансформируется в код понятный компьютеру (машинный код) при помощи специальных утилит: компиляторов и интерпретаторов.
Таким образом он является неким "переводчиком", который помогает общаться человеку с компьютером.

**Интерпретируемый:** Интерпретаторы проходятся по каждой строке программы и выполняют все команды строчка за строчкой.

*Компилируемые языки сразу переводят в машинный код, который может выполнить процессор, перед началом выполнения программы.

**Общего назначения:** означает, что использовать Python можно в различных областях: веб, десктоп и мобильные приложения, тестирование, работа с данными, работа с большими данными (big data), искусственный интеллект и машинное обучение, автоматизация и даже игры!


➕ Pithon:
- простые, понятные, явные конструкции;
- хорошо читаемый текст программ;
- богатая библиотека модулей

➖ Python:
- более *медленная* (по сравнению с компилируемыми языками) скорость работы;
- большой объём используемой памяти

⬆️[Оглавление](#оглавление)
___
## Установка Python
(для Windows)

1. Скачать Python можно на [официальном сайте](https://www.python.org)

Переходим по ссылке. При наведении на **Downloads** нам предлагают сразу скачать последнюю стабильную версию для вашей ОС.

[![1.png](https://i.postimg.cc/N0fXFRf5/1.png)](https://postimg.cc/XrmqDG5b)

То же самое предлагают при нажатии на **Downnloads** и выборе своей версии ОС, или просто при нажатии на **Downloads**.

2. Выбираем последнюю стабильную версию для вашей ОС или любую другую (если нужно), но из списка стабильных, и скачиваем на свой компьютер.

[![2.png](https://i.postimg.cc/PqRmzbW7/2.png)](https://postimg.cc/67C2Bv1V)

3. Начинаем установку. Запускаем загрузчик. В начале установки появится окно, в котором **обязательно** следует отметить галочкой опцию **"Add Python.exe to PATH"**. Она позволит в дальнейшем запускать интерпретатор языка без указания полного пути к нему.

[![3.png](https://i.postimg.cc/ncp0Lk0K/3.png)](https://postimg.cc/DmpqjqVm)

4. Затем, выбираем режим установки **"Customize installation"**. Этот процесс установки предназначен для установки дополнительных инструментов Python, которые необходимы для обработки языка, наиболее важным из которых является установка инструмента **"pip"**.

Здесь все опции должны быть отмечены галочками:

[![4.png](https://i.postimg.cc/XJ27yx9Z/4.png)](https://postimg.cc/JDkWfN6m)

5. Нажимаем **"Next"** и в следующем окне путь, который прописан по умолчанию, лучше изменить на другой.

А именно, убрать все промежуточные подкаталоги и установить интерпретатор в корень выбранного диска (не как на скриншоте, а, например С:\Python311). Также дополнительно указываем версию языка 3.11. Это также рекомендуется делать, так как разных версий на одном устройстве может быть несколько и чтобы переключаться между ними, они должны находиться в разных директориях.

[![5.png](https://i.postimg.cc/1XdW4gMx/5.png)](https://postimg.cc/n9vKPh6T)

После этого, нажимаем на кнопку «Install» и программа устанавливается в указанный каталог.

6. Осталось проверить работоспособность языка Python.

- Во-первых, мы можем открыть окно выполнения команд в ОС Windows (Win+R) и в появившемся окне набрать «cmd»:

[![6.png](https://i.postimg.cc/52JnkMHM/6.png)](https://postimg.cc/mtdYtJNd)

- Также  мы можем открыть его, выполнив поиск в меню "Пуск" или на панели поиска. Просто найдите его и щелкните по нему, чтобы открыть cmd.
- Далее, в консольном командном окне пишем команду,

 ```
python
```
или

```
python --version
```

[![7.png](https://i.postimg.cc/8zDq9zt1/7.png)](https://postimg.cc/4mLLhZDM)

 в результате которой должны увидеть текущую версию интерпретатора этого языка.

 Если вы работаете под Linux или Mac OS, то следует набрать команду

 ```
python3
```

Если мы видим, что команда выводит результаты в виде версии, которую загрузили, это означает, что мы выполнили установку отлично и можем начать работать над ней сейчас.

Но писать и исполнять команды самого языка лучше через среду IDLE, которая устанавливается вместе с интерпретатором. Для ее запуска достаточно нажать на кнопку "Пуск" и найти оболочку IDLE. Появится окно, в котором можно в интерактивном режиме выполнять любые команды языка.

Также можете использовать Power Shell, который имеет больше возможностей, чем просто CMD.

⬆️[Оглавление](#оглавление)
___
## PyCharm
**PyCharm** — это среда программирования для языка Python, или **IDE**. 

Средами называют программы, в которых можно писать, запускать и отлаживать код, устанавливать новые расширения и дополнительные модули. Это мощный многофункциональный инструмент для разработчиков.

PyCharm существует для нескольких операционных систем: Windows, Linux и macOS. Она поддерживает разные версии Python: и 2.x, и 3.x. Её широкие возможности делают разработку на Python быстрее и эффективнее.

### Для чего нужен PyCharm
Языки программирования устроены так, что писать код на них можно где угодно, даже в «Блокноте». Главное — сохранить файл в нужном расширении, а потом запустить с помощью установленного интерпретатора или компилятора. Но большинство разработчиков все равно пользуются IDE. И вот почему.

**Код писать удобнее.** 

В средах, в том числе PyCharm, есть подсветка синтаксиса: разные ключевые слова и конструкции выделяются цветами, так что нужное место в коде проще найти.

**Возможности среды шире.** 

В IDE можно не только написать код, но и запустить его и сразу посмотреть на результат работы программы. Там есть инструменты для отладки, контроля версий, например с помощью Git; можно в несколько кликов устанавливать сторонние библиотеки и фреймворки.

**Командная работа проще.** 

Профессиональная версия среды дает возможность синхронизироваться с другими разработчиками и делать командную работу эффективнее.

Для Python существует несколько популярных сред. PyCharm выбирает большинство: его легко настраивать, в нем удобный и функциональный интерфейс, а возможностей много. Он подходит для широкого спектра задач: от автоматического тестирования до машинного обучения. Другие среды для языка обычно или менее удобные, или более узкие в применении.


### Что позволяет делать PyCharm
IDE — это не просто редактор для кода. У него намного больше возможностей, облегчающих жизнь разработчику. PyCharm можно представить как комбайн, где есть большинство функций, важных для программиста. Вот лишь некоторые вещи, которые в нем можно делать.

**Создавать проекты.** 

Проект на языке программирования — это не просто создание файла. Когда разработчик создает проект в PyCharm, среда выделяет под него отдельную папку, где хранит все связанное с этим проектом. Так нужные файлы и компоненты находятся под рукой. Структуру проекта PyCharm показывает в левой части интерфейса и дает возможность в любой момент переключиться на интересующий файл внутри него.

**Писать код на Python.** 

Внутри проекта можно создать файл в нужном расширении и писать в нем код. Синтаксис подсвечивается автоматически, причем параметры подсветки можно настроить. К тому же PyCharm дает возможность сразу проверять правильность написания и выделять ошибочные моменты. Среда помогает писать более чистый код.

**Запускать.** 

IDE подключены к интерпретатору или компилятору нужного языка. Python — интерпретируемый язык, и PyCharm может запустить его интерпретатор. Поэтому код можно выполнить прямо внутри среды, для этого не понадобится открывать консоль или любое стороннее приложение. В интерфейсе IDE есть кнопка запуска: достаточно нажать на нее, и код запустится. Результат исполнения программа покажет сразу — выведет в специальную консоль внутри среды или откроет новое окно.

**Отлаживать.** 

В среде есть инструменты для отладки кода. Например, можно настроить режим отладки так, чтобы показывать значения разных переменных в любой момент времени. Или остановить выполнение на конкретной строчке и смотреть, нормально ли код работает в этом моменте, — это помогает найти место, в котором происходит ошибка. Есть и пошаговое выполнение: программа выполняет одну строчку кода и останавливается, чтобы разработчик мог проверить, правильно ли она работает на этом участке.

**Тестировать.** 

Автоматическое тестирование — одна из распространенных сфер применения Python. И делать это в PyCharm удобно. В среде есть инструменты для автоматической генерации кода, и к ней легко подключить модули для тестирования.

**Корректировать.** 

Чтобы код был чистым и красивым и его было легко читать, нужно следовать правилам «хорошего тона» для разработчиков. PyCharm может следить за выполнением этих правил. Он также может автоматически расставлять переносы строк и отступы и дополнять написанное: человек вводит только часть команды, а PyCharm уже предлагает подсказки для ее окончания.

**Устанавливать библиотеки и фреймворки.** 

Некоторые версии PyCharm «из коробки» поддерживают ряд популярных фреймворков для языка, другие дают возможность быстро их скачать и установить. Одна из возможностей среды – быстро найти нужный фреймворк в сети, загрузить и подключить к проекту. Это удобно: для установки и развертывания окружения не приходится пользоваться множеством дополнительных инструментов.

**Устанавливать дополнения и плагины.** 

Для самой среды тоже есть модули, расширяющие ее функциональность. Их можно установить изнутри IDE. Примеры таких модулей – проверка читаемости кода, подсказки с помощью искусственного интеллекта, расстановка недостающих скобок и многое другое. Некоторые плагины меняют интерфейс, если разработчику не нравится стандартный. Другие расширяют возможности самой среды. После установки дополнением можно пользоваться как частью IDE.

**Писать на других языках.** 

PyCharm предназначена для Python, но в ней есть поддержка и других языков. Например, Python часто используется в веб-разработке, поэтому IDE также поддерживает JavaScript для браузера и SQL для баз данных. Кроме JavaScript, поддерживаются основанные на нем TypeScript и CoffeeScript, популярные JS-фреймворки, а также языки HTML и CSS для верстки. В среде можно пользоваться шаблонизаторами – специальными инструментами, которые помогают создавать шаблоны для веб-страниц. Языки шаблонизаторов PyCharm тоже понимает.

### Полезные особенности PyCharm
**Использование шаблонов.** 

Можно пользоваться шаблонами кода, чтобы быстрее решать типовые задачи.

**Автогенерация кода.** 

Среда может сгенерировать код по заданным вами критериям – обычно это используют для шаблонных действий, например, для подключения библиотек или оформления функций.

**Умный редактор.** 

Автодополнение кода, обнаружение ошибок и возможности для автоматического исправления предохраняют разработчика от части неприятных сбоев.

**Рефакторинг.** 

Так называют исправление и изменение кода, и для него в PyCharm много функций: быстрая вставка или переименование сущности по всему проекту, структурирование кода и другие. Все делается быстро, и многое автоматизировано.

**Умный поиск.** 

Благодаря интеллектуальному поиску что угодно можно найти буквально в несколько кликов – и в коде, и внутри самой среды.

**Встроенные инструменты.** 

В PyCharm можно работать с системами контроля версий, такими как Git, а также с СУБД и удаленными устройствами. Среда поддерживает и другие технологии.
___
*Полный текст статьи про PyCharm в [блоге Skillfactory](https://blog.skillfactory.ru/glossary/pycharm/)*
___
⬆️[Оглавление](#оглавление)
___
## Установка и настройка PyCharm
Для того, чтобы начать работу с PyCharm понадобится скачать и установить интерпретатор для Python (его установку я описала в [предыдущем разделе](#установка-python), а также саму среду разработки для работы с Python.

1. Для установки PyCharm нам нужно
- перейти на [официальный сайт](https://www.jetbrains.com) программы
- выбрать раздел **Developer Tools**
- выбрать в выпадающем списке **PyCharm**

[![1.png](https://i.postimg.cc/0Qzmp4XL/1.png)](https://postimg.cc/8JVjGZSH)

2. Нажать на любую кнопку загрузки

 [![2.png](https://i.postimg.cc/V6tvsPVL/2.png)](https://postimg.cc/mzbBVJ40)

 3. У PyCharm две основных версии:
- бесплатная **Community**
- платная **Pro.**

Про-версия предназначена для профессиональных разработчиков, которым нужна более широкая функциональность. В комьюнити-версии можно учиться, писать код для себя или для небольших проектов. Для большинства задач ее достаточно.

[![3.png](https://i.postimg.cc/MHdSqsqp/3.png)](https://postimg.cc/WqFK7wdB)

4. После загруки установщика, его нужно запустить и выдать необходимые Windows-разрешения. Далее надо несколько раз нажать **Next** и отметить галочки для создания ярлыка на рабочем столе и связи PyCharm с .py-файлами

[![4.png](https://i.postimg.cc/Njtzp8cN/4.png)](https://postimg.cc/KR9fYM4L)

Далее снова нажимем **Next** и **Install**, чтобы запустить процесс установки.

5. После завершения нажимаем **Finish** и теперь можно запускать **PyCharm** кликнув по ярлыку на рабочем столе. На этом этапе у вас может всплыть окно с лицензионным соглашением, которое надо принять.

Также вам может быть предложено импортировать настройки из ранее установленного PyCharm. Можно смело выбрать **Don’t import settings** и нажать **OK**.

Если всё прошло успешно, то произойдет первый запуск IDE и на этом этапе Брандмауэр Windows может попросить разрешения доступа. Надо разрешить.

6. После откроется Welcome окно, в котором необходимо создать наш первый проект, нажав на **New Project**

[![5.png](https://i.postimg.cc/JztPTpF5/5.png)](https://postimg.cc/LJKt532J)

7. В верхней строке нам предлагают выбрать каталог, в котором мы будем хранить наш проект. Сам PyCharm рекомендует создать внутри домашней папки пользователя каталог **PycharmProjects** для хранения всех проектов и pythonProject для хранения нашего текущего

[![6.png](https://i.postimg.cc/wMfDLp98/6.png)](https://postimg.cc/8fvFgxFt)

Давайте PycharmProjects оставим как есть, а вот создаваемый проект переименуем во что-то другое. Вы можете дать ему любое имя, которое вам нравится, но постарайтесь выполнить два условия:

- Используйте только латиницу.
- Не используйте пробелы.

8. Далее нам надо выбрать версию Питона, которую мы будем использовать в нашем проекте. Причем PyCharm нам сразу предлагает использовать **виртуальные окружения**. Нажимаем на стрелочку и выбираем нужный интерпретатор в той директории, куда его установили.

[![7.png](https://i.postimg.cc/Pf0S6gZf/7.png)](https://postimg.cc/dDmR3S4g)

Отметим также галочкой (рекомендую только для первого проекта, дальше он не нужен) **Create a main.py welcome script** и кликаем **Create** внизу окна.

9. Перед нами откроется окно PyCharm. Слева отображается структура проекта. Сейчас в нём уже есть приветственный файл **main.py**

[![8.png](https://i.postimg.cc/sD0Yw8Lf/8.png)](https://postimg.cc/Tpg5PkGB)

Для запуска файла нажимаем на зелёную стрелочку ▶️. Эта стрелочка запускает программу. После запуска внизу вы должны увидеть результат её работы — фразу «Hi, PyCharm» от JetBrains

10. Можете попробовать написать свою первую программу! Для этого проделайте следующие шаги:

- нажмите правой кнопкой мышки в любом месте поля со структурой файла и выберите **new** > **Python File**. Напишите имя файла, например first_file и нажмите Enter и этот файл автоматически добавится в ваш проект с расширением .py

[![9.png](https://i.postimg.cc/qRZX8pCK/9.png)](https://postimg.cc/tZWxbQkR)

- в рабочем окне напишите свой первый скрипт:

```Python3
print("Hello World!")
```

[![10.png](https://i.postimg.cc/KYb222jt/10.png)](https://postimg.cc/RWg872c0)

- для запуска программы
  * или нажмите на зелёную стрелочку, убедившись, что слева от неё написано "Current File",
  * или, нажав правую кнопку мышки в любом месте рабочего окна, выберите **Run 'имя_вашего_файла'**
 
Программа начнёт выполняться и внизу появится результат её работы.

[![12.png](https://i.postimg.cc/1RB2gFtn/12.png)](https://postimg.cc/qgtjSz24)

В данной программе мы задали вывести на экран строку с текстом **Hello World!**

Поздравляю! Вы написали свою первую программу 🎉🏆

⬆️[Оглавление](#оглавление)
___
В файлах мои решения задачек на Python и небольшие конструкции для решения определённых задач в программировании на Python
