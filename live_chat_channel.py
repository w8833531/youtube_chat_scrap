#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# live_chat_channel.py
# @Author : 吴鹰 (wuying)
# @Link   :
# @Date   : 12/19/2018, 2:11:53 PM
import requests
import time
import sys
import random

### how to get headers/params/data
### use chrome access a youtube live videa, and press F12 ,select Network, select XHR,right click get_live_chat_replay url and copy curl command
### access https://curl.trillworks.com/# paste curl command and get python requests and past headers/params/data


headers = {
}

params = (
)

data = ''


def get_response(headers='', params='', data=''):
    try:
        response = requests.post('https://gaming.youtube.com/youtubei/v1/live_chat/get_live_chat_replay', headers=headers, params=params, data=data)
    except:
        response=''
    return response

def print_channel_id(response):
    if response != '' and response.status_code == 200:
        for i in range(len(response.json()['continuationContents']['liveChatContinuation']['actions'])):
            try:
                print(response.json()['continuationContents']['liveChatContinuation']['actions'][i]['replayChatItemAction']['actions'][0]['addChatItemAction']['item']['liveChatTextMessageRenderer']['authorExternalChannelId'])
            except:
                print('')

def has_continuation(response):
    try:
        continuation = response.json()['continuationContents']['liveChatContinuation']['continuations'][1]['playerSeekContinuationData']['continuation']
    except:
        continuation = ''
    return continuation

response = get_response(headers=headers, params=params, data=data)
print_channel_id(response)
continuation = has_continuation(response)

player_off_setms = 0
while continuation != '':
    data = '{"context":{"client":{"clientName":"WEB_GAMING","clientVersion":"1.92","hl":"zh-CN","gl":"US","experimentIds":[],"theme":"GAMING"},"capabilities":{},"request":{"internalExperimentFlags":[{"key":"live_chat_flash_money_button_on_super_chat_delivery","value":"true"},{"key":"live_chat_replay_milliqps_threshold","value":"5000"},{"key":"third_party_integration","value":"true"},{"key":"live_chat_replay","value":"true"},{"key":"enable_gel_web_client_event_id","value":"true"},{"key":"optimistically_create_transport_client","value":"true"},{"key":"live_chat_top_chat_window_length_sec","value":"4"},{"key":"channel_about_page_gadgets","value":"true"},{"key":"live_chat_top_chat_split","value":"0.5"},{"key":"interaction_click_on_gel_web","value":"true"},{"key":"attach_child_on_gel_web","value":"true"},{"key":"live_fresca_v2","value":"true"},{"key":"polymer_page_data_load_refactoring","value":"true"},{"key":"live_chat_inline_moderation","value":"true"},{"key":"lact_local_listeners","value":"true"},{"key":"enable_creator_highlights","value":"true"},{"key":"interaction_logging_on_gel_web","value":"true"},{"key":"log_js_exceptions_fraction","value":"1"},{"key":"live_chat_use_new_default_filter_mode","value":"true"},{"key":"custom_emoji_upsell","value":"true"},{"key":"log_foreground_heartbeat_gaming","value":"true"},{"key":"remove_web_visibility_batching","value":"true"},{"key":"enable_docked_chat_messages","value":"true"},{"key":"retry_web_logging_batches","value":"true"},{"key":"html5_serverside_pagead_id_sets_cookie","value":"true"},{"key":"very_optimistically_create_gel_client","value":"true"},{"key":"interaction_screen_on_gel_web","value":"true"},{"key":"live_chat_message_sampling_rate","value":"4"},{"key":"log_playback_associated_web","value":"true"},{"key":"live_chat_flagging_reasons","value":"true"},{"key":"web_logging_max_batch","value":"100"},{"key":"use_push_for_desktop_live_chat","value":"true"},{"key":"enable_youtubei_innertube","value":"true"},{"key":"youtubei_for_web","value":"true"},{"key":"debug_forced_promo_id","value":""},{"key":"log_window_onerror_fraction","value":"1"}]}},"continuation":"%s","currentPlayerState":{"playerOffsetMs":"%s"}}' % (continuation,str(player_off_setms))
    response = get_response(headers=headers, params=params, data=data)
    print_channel_id(response)
    continuation = has_continuation(response)
    player_off_setms += random.randint(6000,12000)
    time.sleep(3)


