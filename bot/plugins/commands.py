#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @alphantime

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    buttons = [[
        InlineKeyboardButton('My Dev ๐จโ๐ฌ', url='https://t.me/alphantime'),
        InlineKeyboardButton('Source Code ๐งพ', url ='https://images.app.goo.gl/kfxLkFvb58MkUz3dA')
    ],[
        InlineKeyboardButton('Support ๐ ', url='https://t.me/alphantimebotsupport')
    ],[
        InlineKeyboardButton('Help โ', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home โก', callback_data='start'),
        InlineKeyboardButton('About ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home โก', callback_data='start'),
        InlineKeyboardButton('Close ๐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
    
