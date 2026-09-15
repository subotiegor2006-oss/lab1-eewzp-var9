# Лабораторная работа №1

Субботин Егор Сергеевич, группа 221341, вариант 9, лабораторная №1.

## Задания варианта

Средняя сложность:

- №1 — установить Git и настроить имя и email
- №6 — слить ветку feature с основной
- №9 — отправить изменения на GitHub

Повышенная сложность:

- №2 — настроить SSH-ключ и подключить к GitHub
- №9 — сформировать отчёт о коммитах с git shortlog

## Клонирование

```bash
git clone git@github.com:subotiegor2006-oss/lab1-eewzp-var9.git
cd lab1-eewzp-var9
```

## Запуск

```bash
python main.py
```

## Проверки

```bash
git status
git log --graph --oneline --decorate --all
git shortlog -sn --all
```

## Ветка feature и слияние

Ветка `feature` создана, в ней добавлен файл `lab1/utils.py`.
Слияние выполнено через Pull Request с сохранением merge-коммита.

Граф истории:

```text
* ba9774f chore: добавить .gitignore для Python-проекта
*   94c1e1d feat: слить ветку feature с основной
|\
| * 169724e feat: добавить utils.py в ветке feature
|/
* baeee2f feat: добавить main.py с простой функцией приветствия
* 0fa9758 docs: добавить README с данными студента и заданиями варианта
* b56e496 Initial commit
```

Ветка `feature` сохранена в репозитории.

## Отчёт shortlog

```text
     5	eewzp
     1	subotiegor2006-oss
eewzp (5):
      docs: добавить README с данными студента и заданиями варианта
      feat: добавить main.py с простой функцией приветствия
      feat: добавить utils.py в ветке feature
      feat: слить ветку feature с основной
      chore: добавить .gitignore для Python-проекта

subotiegor2006-oss (1):
      Initial commit
```

Полный вывод также сохранён в `docs/shortlog.txt`.

## SSH

SSH-ключ создан (ed25519) и добавлен в настройки GitHub.

Проверка подключения:

```bash
ssh -T git@github.com
```

Вывод:

```text
Hi subotiegor2006-oss! You've successfully authenticated, but GitHub does not provide shell access.
```

Remote:

```text
origin  git@github.com:subotiegor2006-oss/lab1-eewzp-var9.git (fetch)
origin  git@github.com:subotiegor2006-oss/lab1-eewzp-var9.git (push)
```
