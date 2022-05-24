# Веб-сервис для классификации больных или здоровых растений по листу
## Описание
Данное веб-приложение предназначено для помощи людям в определение здорового или больного растения по зеленому листу.
Цель данного приложения упростить и ускорить работу с различными растениями, особенно в работе с большим количеством растений.

## Установка
Эти инструкции позволят вам запустить и запустить копию проекта на вашем локальном компьютере.

### 1. Необходимые компоненты:
<code>python==3.7 or 3.8</code>

<h3>2. Клонирование</h3>
<p>Клонирование репозитория используя git:</p>

    git clone --recurse-submodules https://github.com/AAIvanchenko/definition_of_diseases.git
    
<p>или просто загрузите, используя приведенный ниже URL-адрес:</p>
<code>https://github.com/AAIvanchenko/definition_of_diseases.git</code>

<p>затем перейдите в каталог проекта.</p>

<h3>3. Настройка pipenv & Установка Requirements</h3>

    pip install pipenv
    pipenv install -r requirements.txt
    pipenv shell

<h3>4.Открытие сервера</h3>
<p>Перейдите в директорию</p>
<code>definition_of_diseases/src</code>
<h3>5. Migrate Database</h3>

    python manage.py makemigrations
    python manage.py migrate

<h3>6. Доступ администратора</h3>
<p>Чтобы использовать панель администратора, вам необходимо создать суперпользователя с помощью этой команды:</p>

    python manage.py createsuperuser

<h2>Использование</h2>
<p>Запустите сервер в каталоге src, используя эту команду:</p>

    python manage.py runserver
<p>В вашем веб-браузере введите адрес : http://localhost:8000 or http://127.0.0.1:8000/</p>

<h3> Внешний вид системы: </h3>

#### Главное окно веб-сервиса.

![image](https://user-images.githubusercontent.com/90927578/170117686-4084bcf6-cd1c-4799-8fc0-198629a3612c.png)


#### Окно результата веб-сервиса.
![image](https://user-images.githubusercontent.com/90927578/170117938-2eeda1c3-83c8-4df0-bffc-59f204d394c5.png)

