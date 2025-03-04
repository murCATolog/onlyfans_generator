import re

print('Введи інформацію про себе.')

# В цей список поміщується інформація про особу
personal_info = []

# Запити про особу
prompts = ['Імʼя: ',
           'Прізвище: ',
           'Ким працюєш: ',
           'Твій нік в Інстаграм: ',
           'Вік: ',
           'Зріст: ',
           'Вага: ',
           'Номер телефону: ',
           'Пару речень про себе: ',
           ]

# Перевірка введеної інформації
while len(personal_info) < len(prompts):
    prompts_generator = input(prompts[len(personal_info)])

    # Перевірка на ім'я та прізвище (тільки літери)
    if len(personal_info) <= 1 and not prompts_generator.isalpha():
        print('Треба вводити лише літери.')
        continue
    # Перевірка на Instagram нік (тільки латинські літери, цифри, підкреслення та дефіси)
    elif len(personal_info) == 3 and not re.match("^[a-zA-Z0-9_-]+$", prompts_generator):
        print('Треба вводити лише латинські літери, цифри, символи підкреслення та дефіси.')
        continue
    # Перевірка на цифри для віку, зросту, телефону та ваги
    elif 4 <= len(personal_info) <= 7 and not prompts_generator.isdigit():
        print('Треба вводити лише цифри.')
        continue
    # Перевірка на мінімальну кількість символів у "Пару речень про себе"
    elif len(personal_info) == 8 and len(prompts_generator) < 15:
        print('Замало інформації.')
        continue
    # Перевірка на мінімальну кількість символів в інших полях
    elif len(prompts_generator) < 2:
        print('Замало символів.')
        continue
    else:
        personal_info.append(prompts_generator)

# HTML сторінка
html = f'''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{personal_info[0]} {personal_info[1]}</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/solid.min.css" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            background-color: #fff;
            font-family: 'Roboto', sans-serif;
            font-size: 18px;
        }}
        header {{
            background-color: #2196F3;
            color: white;
            text-align: center;
            padding: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .logo {{
            font-size: 24px;
            font-weight: 500;
        }}
        .slogan {{
            font-size: 18px;
            font-weight: 300;
            transition: opacity 0.5s;
        }}
        .slogan.crossed {{
            text-decoration: line-through;
            opacity: 0.7;
        }}
        .new-star-text {{
            font-size: 36px;
            color: red;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }}
        main {{
            flex: 1;
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 40px;
        }}
        .progress-bar-container {{
            width: 100%;
            max-width: 600px;
            background-color: #f3f3f3;
            border-radius: 10px;
            height: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .progress-bar {{
            height: 100%;
            width: 0;
            background-color: #FFEB3B;
            border-radius: 10px;
            text-align: center;
            line-height: 30px;
            color: #333;
            font-weight: 500;
            transition: width 0.1s ease-out;
        }}
        .progress-text {{
            font-size: 16px;
            color: #555;
        }}
        .card-container {{
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: nowrap;
            position: relative;
            width: 100%;
            max-width: 1200px;
        }}
        .card {{
            width: 100%;
            max-width: 300px;
            padding: 20px;
            border-radius: 10px;
            background: #f5f5f5;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 0.8s ease-out forwards;
            flex-shrink: 0;
        }}
        .card h5 {{
            font-size: 20px;
            margin-bottom: 10px;
        }}
        @keyframes fadeInUp {{
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        @keyframes explode {{
            0% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(2) rotate(45deg); opacity: 0.5; }}
            100% {{ transform: scale(0); opacity: 0; }}
        }}
        .explode {{
            animation: explode 1s forwards;
        }}
        .new-card {{
            width: 100%;
            padding: 40px;
            border-radius: 0;
            background: #FF5722;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            opacity: 0;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            animation: fadeInUp 1s ease-out forwards;
            z-index: 10;
        }}
        .new-card h5 {{
            font-size: 28px;
            margin-bottom: 20px;
        }}
        .new-card a {{
            color: white;
            font-weight: 500;
            text-decoration: underline;
        }}
        footer {{
            background-color: #757575;
            color: white;
            padding: 20px;
            text-align: center;
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }}
        footer a {{
            color: white;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        @media (max-width: 768px) {{
            header {{ padding: 20px; }}
            .logo {{ font-size: 20px; }}
            .slogan {{ font-size: 16px; }}
            .new-star-text {{ font-size: 24px; }}
            main {{ padding: 20px; }}
            .card-container {{
                flex-wrap: wrap;
                justify-content: center;
            }}
            .card {{ max-width: 100%; }}
            .new-card {{
                position: static;
                border-radius: 10px;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <div class="logo">{personal_info[0]} {personal_info[1]}</div>
        <div class="slogan" id="managerText">{personal_info[2]}</div>
        <div class="new-star-text" id="newStarText">New OnlyFans Star!</div>
    </header>

    <main>
        <div class="progress-bar-container">
            <div class="progress-bar" id="progressBar">0%</div>
        </div>
        <div class="progress-text" id="progressText">Parsing...</div>
        <div class="card-container">
            <div class="card" style="animation-delay: 0.2s;">
                <h5>Вік:</h5>
                <p>{personal_info[4]}</p>
            </div>
            <div class="card" style="animation-delay: 0.4s;">
                <h5>Зріст:</h5>
                <p>{personal_info[5]}</p>
            </div>
            <div class="card" style="animation-delay: 0.6s;">
                <h5>Вага</h5>
                <p>{personal_info[6]}</p>
            </div>
            <div class="card" style="animation-delay: 0.8s;">
                <h5>Про себе:</h5>
                <p>{personal_info[8]}</p>
            </div>
        </div>
    </main>

    <footer>
        <a href="tel:{personal_info[7]}"><i class="fa fa-address-book"></i> {personal_info[7]}</a>
        <a href="https://instagram.com/{personal_info[3]}" target="_blank"><i class="fa fa-instagram"></i>Мій Instagram</a>
    </footer>

    <script>
        const progressBar = document.getElementById('progressBar');
        const progressText = document.getElementById('progressText');
        const cards = document.querySelectorAll('.card');
        const cardContainer = document.querySelector('.card-container');
        const managerText = document.getElementById('managerText');
        const newStarText = document.getElementById('newStarText');

        let progress = 0;
        const progressInterval = setInterval(() => {{
            progress++;
            progressBar.style.width = `${{progress}}%`;
            progressBar.textContent = `${{progress}}%`;
            progressText.textContent = progress < 100 ? 'Parsing...' : 'Completed!';
            if (progress >= 100) {{
                clearInterval(progressInterval);
                triggerExplosions();
            }}
        }}, 100);

        function triggerExplosions() {{
            cards.forEach(card => card.classList.add('explode'));
            setTimeout(addNewCard, 1000);
        }}

        function addNewCard() {{
            const newCard = document.createElement('div');
            newCard.classList.add('new-card');
            newCard.innerHTML = `
                <h5>Дякую, {personal_info[0]}!</h5>
                <p>Всі твої сторінки у соц. мережах та месенджери зламано!<br>Скоро всі твої інтимні фотографії зʼявляться на новій сторінці:<br><a href="https://onlyfans.com/{personal_info[3]}" target="_blank">onlyfans.com/{personal_info[3]}</a></p>
            `;
            cardContainer.appendChild(newCard);
            setTimeout(updateHeader, 1000);
        }}

        function updateHeader() {{
            managerText.classList.add('crossed');
            setTimeout(() => newStarText.style.opacity = 1, 500);
        }}
    </script>
</body>
</html>
'''

# Записуємо у файл
with open('index.html', 'w') as new_file:
    new_file.write(html)