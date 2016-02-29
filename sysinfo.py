import sys
print(sys.version_info)
print(sys.version)

"""
Создание проекта в рамках курса на stepic.org

Мы начинаем практическую часть курса, которая состоит в разработке web приложения на языке python c использованием фреймворка Django.  Проект разделен на отдельные задания, которые оформлены в виде шагов stepic.org.

При разработке проекта необходимо учесть особенности платформы stepic, а именно:

    При выполнении каждого задания (шага) stepic создает новую виртуальную машину. А это значит, что результаты предыдущих заданий не сохраняются.
    Доступ в виртуальную машину осуществляется с помощью Web-терминала. Доступ весьма ограничен и не достаточен для полноценного редактирования кода.

Исходя из этого при выполнении последующих задач (имеются в виду linux-задачи, а не тесты и т.п.) необходимо придерживаться следующего протокола:

    Весь проект (включая конфигурационные файлы серверов) должен быть расположен в репозитории на github.com.  Если у вас нет аккаунта на github, его придется создать.
    Репозиторий должен быть склонирован в директорию /home/box/web  на виртуальной машине.
    Загрузка кода в виртуальную машину происходит через github. Т.е. вы редактируете (и проверяете) код вашего проекта локально на вашей машине, после этого делаете git push, после этого делаете git pull в терминале stepic.

Поскольку разработка проекта связана не только с написание кода, но и установкой и настройкой серверов, то вам будет необходимо автоматизировать этот процесс, а именно в создать в репозитории файл init.sh, в котором будут перечислены все необходимые действия для данного этапа проекта.  Вот пример такого файла:

sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

Тогда при решении очередного задания необходимые действия будут сведены к минимуму:

git clone https://github.com/your_account/stepic_web_project.git /home/box/web
bash /home/box/web/init.sh
"""