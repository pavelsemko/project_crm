# Create your tasks here
from __future__ import absolute_import, unicode_literals

import json
from datetime import datetime, timezone
import urllib as urllib
import ssl
from django.db.models.functions import Now

import requests
from celery.task import periodic_task
from celery.schedules import crontab

from project_crm import celery, settings
from account.models import Planning


from celery import shared_task, app
@periodic_task(run_every=(crontab(minute='*/5')),name="send")
def send():
    p = Planning.objects.filter(update__lte=Now(), notification=True)
    for i in p:
        inline_button1 = {"text": "View customer", "url": "https://easycrm.xyz/lead/" + str(i.lead.id)}
        inline_keyboard = [[inline_button1]]
        keyboard = {"inline_keyboard": inline_keyboard}
        replyMarkup = json.dumps(keyboard)
        ssl._create_default_https_context = ssl._create_unverified_context
        text = urllib.parse.quote(f"<b>🛎️Напоминаем🛎️</b>\nУ вас стоит «{i.type}» на <b>{i.update.strftime('%d-%m-%Y %H:%M')}</b> {i.lead.full_name} (#{i.lead.id})\n☎️Не забудь позвонить☎️")
        url = "https://api.telegram.org/bot"+settings.TELEGRAM_API+"/sendMessage?chat_id=" + i.manager.telegram + "&parse_mode=html&text=" + text + "&reply_markup=" + replyMarkup

        payload = {}
        headers = {}

        requests.request("GET", url, headers=headers, data=payload)
    p.update(notification=False)
def hello2():
    print("Hello there!")