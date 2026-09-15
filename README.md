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
