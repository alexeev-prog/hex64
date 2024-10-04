# hex64

<p align="center">Инструмент для мониторинга и диагностики ПК на Python</p>
<br>
<p align="center">
    <img src="https://img.shields.io/github/languages/top/alxvdev/hex64?style=for-the-badge">
    <img src="https://img.shields.io/github/languages/count/alxvdev/hex64?style=for-the-badge">
    <img src="https://img.shields.io/github/stars/alxvdev/hex64?style=for-the-badge">
    <img src="https://img.shields.io/github/issues/alxvdev/hex64?style=for-the-badge">
    <img src="https://img.shields.io/github/last-commit/alxvdev/hex64?style=for-the-badge">
    </br>
</p>

> **hex64 Diagnostic** это бесплатный Open Source инструмент для мониторинга, тестирования и анализа состояния ПК и ресурсов системы

> [!CAUTION]
> **hex64 Diagnostic поддерживает Linux®, а также Windows® (но в некоторых случаях могут возникнуть ошибки).** Другие ОС официально не поддерживаются, хотя вы можете запустить hex64 на них.

> [!CAUTION]
> Прямо сейчас hex64 Diagnostic находится в разработке, и он категорически не рекомендуется к использованию.

## Документация
Вы можете получить документацию по проекту по [этой ссылке.](./hex64-diagnostic/docs/index.md).

## Контакты и поддержка
Если у вас есть вопросы по использованию hex64, создайте [issue](https://github.com/alxvdev/hex64/issues/new) в репозитории или пришлите мне письмо на почту bro.alexeev@inbox.ru.

Вы можете также написать мне в телеграм: [@alexeev_dev](https://t.me/alexeev_dev)

hex64 Diagnostic - Open Source проект, и он поддерживается только благодаря вам.

Релизы проекта доступны по [этой ссылке](https://github.com/alxvdev/hex64/releases).

## Требования

> [!NOTE]
> hex64 Diagnostic использует систему управления проектов poetry

Чтобы запустить данную программу, вам нужны следующие зависимости::

 + Python interpreter (>=3.10)
 + Poetry (version 1.8.3)

## Установка
Если вы хотите получить стабильный релиз [на странице релизов](https://github.com/alxvdev/hex64/releases). Если вы хотите получить новейшую нестабильную git-версию, то следуйте следующим шагам:

1. Клонируйте репозиторий

```bash
git clone https://github.com/alxvdev/hex64.git
cd hex64 Diagnostic
```

2. Просто установите зависимости и войдите в шелл виртуального окружения.

```bash
poetry install
poetry shell
```

3. Готово! 💪 🎉  Вы можете использовать hex64 Diagnostic!

## Функционал
Ниже вы можете увидеть функционал который уже реализован или будет реализован в будущем.

 + [x] Конвертор из байтов в человекочитаемый размер
 + [x] Константы
 + [x] Инфраструктура бенчмарков
 + [x] Однопроцессорный и мультипроцессорный бенчмарк
 + [x] Инфраструктура хранения информации
 + [x] Репозиторий хранения информации о бенчмарках
 + [x] Репозиторий хранения информации об информации с сенсорах
 + [x] Инфраструктура получения информации о системе и ее ресурсах
 + [x] Сенсор CPU
 + [x] Сенсор диска
 + [x] Сенсор ОЗУ
 + [x] Сенсор температур
 + [x] Сенсор информации о сетевом подключении
 + [x] Определение типа диска и получение данных о HDD (и SMART)
 + [x] Создание графиков и их отображение
 + [x] Создание GUI-интерфейса hex64 Diagnostic (бета)
 + [ ] Создание CLI-интерфейса hex64 Diagnostic
 + [ ] Улучшение архитектуры проекта
 + [ ] Закончить документацию по hex64 Diagnostic
 + [ ] Сенсор GPU

## Схемы работы
Схемы работы на данный момент не предоставлены. Ожидайте будущих обновлений.

## Копирайты
hex64 Diagnostic - Инструмент для мониторинга и диагностики ПК на Python.

Copyright © 2024 Alexeev Bronislav. All rights reversed.

The registered trademark Linux® is used pursuant to a sublicense from LMI, the exclusive licensee of Linus Torvalds, owner of the mark on a world-wide basis.

The registered trademark Windows is created by Microsoft Corporation, owner of the mark on a world-wide basis.

