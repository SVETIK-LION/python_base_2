from random import choice
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from log import log_command


def start_command(update: Update, context: CallbackContext) -> None:
    log_command(update, context)  # Логирует данные пользователя чата
    question_buttton = ReplyKeyboardMarkup([['/question']], resize_keyboard=True)
    update.message.reply_text(f'Здравствуй, {update.effective_user.first_name}! Я - магическая сфера.'
                              f'И я буду отвечать на твои вопросы.'
                              f'Нажми кнопку /question, если хочешь задать вопрос.', reply_markup=question_buttton)


def another_question(update: Update, context: CallbackContext) -> None:
    log_command(update, context)
    answer = choice(
        ['Что же ты хочешь узнать? Задай вопрос о себе, на который можно ответить "да" или "нет".',
         'Задай вопрос о себе, на который можно ответить "да" или "нет". Спрашивай...',
         'Слушаю тебя, мой друг... Задай вопрос о себе, на который можно ответить "да" или "нет".',
         'Задай вопрос о себе, на который можно ответить "да" или "нет". Ожидаю...'])
    update.message.reply_text(f'{answer}')


def sphere_answer(update, context):
    log_command(update, context)  # Логирует данные пользователя чата
    ansver = choice(["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
                  "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
                  "Пока не ясно, попробуй снова", "Сори, но об этом нельзя рассказывать... :)", "Спроси позже",
                     "Лучше не рассказывать", "Сейчас нельзя предсказать",
                  "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
                  "Перспективы не очень хорошие", "Весьма сомнительно", "Вполне возможно"])
    update.message.reply_text(f'{ansver}')
