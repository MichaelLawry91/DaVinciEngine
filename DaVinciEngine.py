#!/usr/bin/env python
# coding: utf-8

# In[7]:
from csv import writer
from socket import socket

import pandas as pd
import numpy as np
from pandas import DataFrame
import random

import time
import socket
import threading
from _thread import *

HEADER = 1024
#PORT = 5050
PORT2 = 5051
PORT3 = 5052
PORT4 = 5053
PORT5 = 5054
PORT6 = 5055
PORT7 = 5056
PORT8 = 5057
PORT9 = 5058
PORT10 = 5059
PORT11 = 5060
PORT12 = 5061
PORT13 = 5062

#SERVER = "192.168.1.6"
host, port = "192.168.1.8", 5050
#addr = SERVER, PORT
#addr2 = (SERVER, PORT2)
#addr3 = (SERVER, PORT3)
#addr4 = (SERVER, PORT4)
##addr5 = (SERVER, PORT5)
#addr6 = (SERVER, PORT6)
#addr7 = (SERVER, PORT7)
#addr8 = (SERVER, PORT8)
#addr9 = (SERVER, PORT9)
#addr10 = (SERVER, PORT10)
#addr11 = (SERVER, PORT11)
#addr12 = (SERVER, PORT12)

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

#server2 = socket.socket()
#server3 = socket.socket()
#server4 = socket.socket()
#server5 = socket.socket()
#server6 = socket.socket()
#server7 = socket.socket()
#server8 = socket.socket()
#server9 = socket.socket()
#server10 = socket.socket()
#server11 = socket.socket()
#server12 = socket.socket()

#server.bind(addr)
#server2.bind(addr2)
#server3.bind(addr3)
#server4.bind(addr4)
##server5.bind(addr5)
#server6.bind(addr6)
#server7.bind(addr7)
#server8.bind(addr8)
#server9.bind(addr9)
#server10.bind(addr10)
#server11.bind(addr11)
#server12.bind(addr12)

# l = 0
# receivedData = sock.recv(1024).decode("UTF-8")
#
# print(receivedData)
# Num_of_Hands = int(input("Input the number of Hands to be generated"))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
round = 0
Card1 = []
Card2 = []
startPos = []

while (round < 5):




    cards_value = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    card_val = []
    cards_suit = ['h', 'd', 'c', 's']
    card_list = []
    cards = []
    Win_Lose_Tie = []
    suit = 0
    hero_SO = []
    hero_hand = []
    hero_hand_val = []
    hero_card1 = []
    hero_card2 = []
    list_of_rankings = []
    card_num = 1
    rank_str = 1
    ranks = []
    sorted_hands = []
    rank_list = []
    card_vals = []
    i = 0

    for i in range(0, 13):

        for suit in range(0, 4):
            cards.append(cards_value[i] + cards_suit[suit])
            card_vals.append(cards_value[i])

    random.shuffle(cards)

    # for i in range(0,1):
    small_blind_card1 = cards[0]
    small_blind_card2 = cards[1]
    big_blind_card1 = cards[2]
    big_blind_card2 = cards[3]
    UTG_card1 = cards[4]
    UTG_card2 = cards[5]
    UTG2_card1 = cards[6]
    UTG2_card2 = cards[7]
    MP_card1 = cards[8]
    MP_card2 = cards[9]
    MP2_card1 = cards[10]
    MP2_card2 = cards[11]
    MP3_card1 = cards[12]
    MP3_card2 = cards[13]
    HJ_card1 = cards[14]
    HJ_card2 = cards[15]
    Button_card1 = cards[16]
    Button_card2 = cards[17]
    Burn_card1 = cards[18]
    Flop_card1 = cards[19]
    Flop_card2 = cards[20]
    Flop_card3 = cards[21]
    Burn_card2 = cards[22]
    Turn = cards[23]
    Burn_card3 = cards[24]
    River = cards[25]
    cards_value_df = []
    cards_suit_df = []

    # Button_card1 = "8c"
    # Button_card2 = "Kd"
    # small_blind_card1 = "2h"
    # small_blind_card2 = "Kc"

    # Flop_card1 = "4c"
    # Flop_card2 = "9c"
    # Flop_card3 = "Qh"

    # Turn = "Ac"
    # River = "6c"

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    Hero_Card_Suits = []
    Hero_Hand_Rank = []
    Card_Suits_ = []
    Button_card1_str = str(Button_card1)
    Button_card2_str = str(Button_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    Hero_Card_Ranks = []

    Button_Hand_Rank = []
    Button_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == Button_card1[1]:
            Button_Hand_Suits.append(Button_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Button_card2[1]:
            Button_Hand_Suits.append(Button_card2_str[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == Button_card1[0]:
            Button_Hand_Rank.append(Button_card1[0])
            Hero_Card_Ranks.append(y)
            Hero_Card_Suits.append(Button_card1[1])

        if cards_value_df.at[y, "card_values"] == Button_card2[0]:
            Button_Hand_Rank.append(Button_card2[0])
            Hero_Card_Ranks.append(y)
            Hero_Card_Suits.append(Button_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            Hero_Card_Suits.append(Flop_card1[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            Hero_Card_Suits.append(Flop_card2[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            Hero_Card_Suits.append(Flop_card3[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            Hero_Card_Suits.append(Turn[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            Hero_Card_Suits.append(River[1])
            Hero_Card_Ranks.append(y)

        y += 1

    Heros_Hand_df = pd.DataFrame(list(zip(Hero_Card_Ranks, Hero_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                                 columns=["Card_Rank", "Card_Suit", "Suit_Value"])

    Heros_Hand_rank_suit_df = Heros_Hand_df.sort_values(by=["Card_Rank"], ascending=True)
    Heros_Hand_df_sum = Heros_Hand_df.groupby('Card_Suit', as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    Heros_Hand_sorted_df_sum = Heros_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)

    # Hero_Suit_Sum_index = []
    # n = 0
    # while n < len(Heros_Hand_sorted_df_sum["Suit_Value"]):
    # Hero_Suit_Sum_index.append(n)
    # n += 1
    # Heros_Hand_sorted_df_sum["index"] = Hero_Suit_Sum_index
    # Heros_Hand_sorted_df_sum.set_index("index", inplace=True)
    Hero_Hand_Rank_Flush = []
    # if Heros_Hand_df.at[0, "Card_Suit"]:

    if Heros_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        Hero_Hand_Rank_Flush.clear()
        Hero_Hand_Rank_Flush.append(5)
        if Button_card1[1] == Heros_Hand_df.at[0, 'Card_Suit']:
            Hero_Hand_Rank_Flush.append(Heros_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if Button_card2[1] == Heros_Hand_df.at[0, 'Card_Suit']:
            Hero_Hand_Rank_Flush.append(Heros_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            Hero_Hand_Rank_Flush.append(0)
            Hero_Hand_Rank_Flush.append(0)
            Hero_Hand_Rank_Flush.append(0)
            Hero_Hand_Rank_Flush.append(0)
            Hero_Hand_Rank_Flush.append(0)

    Hero_Suit_for_straight = Heros_Hand_sorted_df_sum.at[0, "Card_Suit"]

    Button_Hand_Rank_sort = sorted(Button_Hand_Rank)
    Heros_Hand = sorted(Hero_Card_Ranks)
    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    Hero_seen = set()
    uniq = []
    Hero_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    Hero_Hand_index = []
    for p in Heros_Hand:
        if p not in Hero_seen:
            Hero_seen[p] = 1

        else:

            Hero_seen[p] += 1
    while s < len(Hero_seen):
        Hero_Hand_index.append(s)
        s += 1

    Card_Rank_Hand = []
    # printing iniial_dictionary

    # split dictionary into keys and values
    Hero_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = Hero_seen.items()
    for item in items:
        Hero_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    Hero_Hand_dict = []
    Hero_Hand_dict_sortforpair = []
    Hero_Hand_dict_sortforstraight = []

    Hero_Hand_dict = pd.DataFrame(list(zip(Hero_Card_Rank_Hand, Num_of_Cards, Hero_Card_Suits)),
                                  columns=['a', 'b', 'c'])
    Hero_Hand_dict_straight = pd.DataFrame(list(zip(Hero_Card_Rank_Hand, Num_of_Cards, Hero_Card_Suits)),
                                           columns=['a', 'b', 'c'])
    Hero_Hand_dict_sortforpair = Hero_Hand_dict.sort_values(by=['b'], ascending=False)
    Hero_Hand_dict_sortforstraight = Hero_Hand_dict_straight.sort_values(by=['a'])

    v = 0
    f = 0

    q = 0
    Hero_Hand_Rank_straight = []
    Hero_Hand_Rank_straight.clear()
    Hero_Hand_Rank_straight_wheel = []
    Hero_Hand_Rank_straight_wheel.clear()
    Hero_Hand_Rank_straight_wheel_flush = []
    Hero_Hand_Rank_straight_wheel_flush.clear()
    Hero_Hand_Rank_Royal_Flush = []
    Hero_Hand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    Hero_Hand_Rank_straight_flush = []
    Hero_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(Hero_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 6), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])
                v += 1

        elif len(Hero_Hand_dict_sortforstraight) == 6:
            v = 0
            while v < 2:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 5), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 4), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 2), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])

                                                            break

                v += 1

        elif len(Hero_Hand_dict_sortforstraight) == 5:

            v = 0
            while v < 1:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(
                                        Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 3), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[
                                                                    (v + 1), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])

                                                            break

                v += 1
        if len(Hero_Hand_dict_sortforstraight) == 4:
            break
        if len(Hero_Hand_dict_sortforstraight) == 3:
            break
        q += 1

    f = 0

    q = 0
    v = 0

    while q < 9:

        if len(Hero_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break

                v += 1

        if len(Hero_Hand_dict_sortforstraight) == 6:
            v = 0
            while v < 2:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)

                                                            break

                v += 1

        if len(Hero_Hand_dict_sortforstraight) == 5:
            v = 0
            while v < 1:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)

                                                            break

                v += 1
        if len(Hero_Hand_dict_sortforstraight) == 4:
            break
        if len(Hero_Hand_dict_sortforstraight) == 3:
            break

        q += 1
    q = 0

    q = 0

    Hero_Hand_dict_sortforpair["index"] = Hero_Hand_index
    Hero_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    c = 0
    if Hero_Hand_dict_sortforpair.at[0, "b"] == 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(10)
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(9)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[5, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(8)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 2:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(8)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(7)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])

    if len(Hero_Hand_Rank_straight_wheel) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(6)
        Hero_Hand_Rank.append(9)
        Hero_Hand_Rank.append(10)
        Hero_Hand_Rank.append(11)
        Hero_Hand_Rank.append(12)
        Hero_Hand_Rank.append(13)

    if len(Hero_Hand_Rank_straight) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(6)
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[4])

    if len(Hero_Hand_Rank_Flush) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(5)
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[1])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 2:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 3:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 3:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if len(Hero_Hand_Rank_straight_wheel_flush) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(2)
        Hero_Hand_Rank.append(9)
        Hero_Hand_Rank.append(10)
        Hero_Hand_Rank.append(11)
        Hero_Hand_Rank.append(12)
        Hero_Hand_Rank.append(13)

    if len(Hero_Hand_Rank_straight_flush) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(2)
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[4])

    if len(Hero_Hand_Rank_Royal_Flush) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(1)
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[4])

    hero_hand.append(Button_card1)
    hero_hand.append(Button_card2)

    #########################################################################################################################
    ########################################################################################################################

    Hero_Rank = Hero_Hand_Rank
    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    Villain_Card_Suits = []

    Villain_Hand_Rank = []
    Card_Suits_ = []
    small_blind_card1_str = str(small_blind_card1)
    small_blind_card2_str = str(small_blind_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    Villain_Card_Ranks = []

    small_blind_Hand_Rank = []
    small_blind_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == small_blind_card1[1]:
            small_blind_Hand_Suits.append(small_blind_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == small_blind_card2[1]:
            small_blind_Hand_Suits.append(small_blind_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == small_blind_card1[0]:
            small_blind_Hand_Rank.append(small_blind_card1[0])
            Villain_Card_Ranks.append(y)
            Villain_Card_Suits.append(small_blind_card1[1])

        if cards_value_df.at[y, "card_values"] == small_blind_card2[0]:
            small_blind_Hand_Rank.append(small_blind_card2[0])
            Villain_Card_Ranks.append(y)
            Villain_Card_Suits.append(small_blind_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            Villain_Card_Suits.append(Flop_card1[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            Villain_Card_Suits.append(Flop_card2[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            Villain_Card_Suits.append(Flop_card3[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            Villain_Card_Suits.append(Turn[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            Villain_Card_Suits.append(River[1])
            Villain_Card_Ranks.append(y)

        y += 1

    Villain_Hand_df = pd.DataFrame(list(zip(Villain_Card_Ranks, Villain_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                                   columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    Villain_Hand_rank_suit_df = Villain_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    Villain_Hand_df_sum = Villain_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    Villain_Hand_sorted_df_sum = Villain_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    Villain_Suit_Sum_index = []
    Villain_Suit_Sum_index.clear()
    n = 0
    while n < len(Villain_Hand_sorted_df_sum["Suit_Value"]):
        Villain_Suit_Sum_index.append(n)
        n += 1
    Villain_Hand_sorted_df_sum["index"] = Villain_Suit_Sum_index
    Villain_Hand_sorted_df_sum.set_index("index", inplace=True)
    Villain_Hand_Rank_Flush = []

    if Villain_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        Villain_Hand_Rank_Flush.clear()
        Villain_Hand_Rank_Flush.append(5)
        if big_blind_card1[1] == Villain_Hand_df.at[0, 'Card_Suit']:
            Villain_Hand_Rank_Flush.append(Villain_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if small_blind_card2[1] == Villain_Hand_df.at[0, 'Card_Suit']:
            Villain_Hand_Rank_Flush.append(Villain_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            Villain_Hand_Rank_Flush.append(0)
            Villain_Hand_Rank_Flush.append(0)
            Villain_Hand_Rank_Flush.append(0)
            Villain_Hand_Rank_Flush.append(0)
            Villain_Hand_Rank_Flush.append(0)

    Suit_for_straight = str(Villain_Hand_sorted_df_sum.at[0, "Card_Suit"])

    small_blind_Hand_Rank_sort = sorted(small_blind_Hand_Rank)
    Villain_Hand = sorted(Villain_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    Villain_seen = set()
    uniq = []
    Villain_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    Villain_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    Villain_Hand_index = []
    for p in Villain_Hand:
        if p not in Villain_seen:
            Villain_seen[p] = 1

        else:

            Villain_seen[p] += 1

    while s < len(Villain_seen):
        Villain_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    Villain_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = Villain_seen.items()
    for item in items:
        Villain_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    Villain_Hand_dict = []
    Villain_Hand_dict_sortforpair = []
    Villain_Hand_dict_sortforstraight = []
    Villain_Hand_dict = pd.DataFrame(list(zip(Villain_Card_Rank_Hand, Num_of_Cards, Villain_Card_Suits)),
                                     columns=['a', 'b', 'c'])
    Villain_Hand_dict_straight = pd.DataFrame(list(zip(Villain_Card_Rank_Hand, Num_of_Cards, Villain_Card_Suits)),
                                              columns=['a', 'b', 'c'])
    Villain_Hand_dict_sortforpair = Villain_Hand_dict.sort_values(by=['b'], ascending=False)
    Villain_Hand_dict_sortforstraight = Villain_Hand_dict_straight.sort_values(by=['a'])
    Villain_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    Villain_Hand_Rank_straight = []
    Villain_Hand_Rank_straight.clear()
    Villain_Hand_Rank_straight_wheel = []
    Villain_Hand_Rank_straight_wheel.clear()
    Villain_Hand_Rank_straight_wheel_flush = []
    Villain_Hand_Rank_straight_wheel_flush.clear()
    VillainHand_Rank_Royal_Flush = []
    VillainHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    Villain_Hand_Rank_straight_flush = []
    Villain_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(Villain_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Villain_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if Villain_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    Villain_Hand_Rank_straight_wheel.clear()

                                    Villain_Hand_Rank_straight_wheel.append(12)
                                    Villain_Hand_Rank_straight_wheel.append(11)
                                    Villain_Hand_Rank_straight_wheel.append(10)
                                    Villain_Hand_Rank_straight_wheel.append(9)
                                    Villain_Hand_Rank_straight_wheel.append(0)

                                    if len(Villain_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            Villain_Hand_Rank_straight_wheel_flush.clear()

                                                            Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(Villain_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if Villain_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        Villain_Hand_Rank_straight_wheel.clear()

                                        Villain_Hand_Rank_straight_wheel.append(12)
                                        Villain_Hand_Rank_straight_wheel.append(11)
                                        Villain_Hand_Rank_straight_wheel.append(10)
                                        Villain_Hand_Rank_straight_wheel.append(9)
                                        Villain_Hand_Rank_straight_wheel.append(0)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                Villain_Hand_Rank_straight_wheel_flush.clear()

                                                                Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(Villain_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        Villain_Hand_Rank_straight_wheel.clear()

                                        Villain_Hand_Rank_straight_wheel.append(12)
                                        Villain_Hand_Rank_straight_wheel.append(11)
                                        Villain_Hand_Rank_straight_wheel.append(10)
                                        Villain_Hand_Rank_straight_wheel.append(9)
                                        Villain_Hand_Rank_straight_wheel.append(0)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                Villain_Hand_Rank_straight_wheel_flush.clear()

                                                                Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(Villain_Hand_dict_sortforstraight) == 4:
                break
            if len(Villain_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(Villain_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Villain_Hand_Rank_straight.clear()

                                    Villain_Hand_Rank_straight.append(q)
                                    Villain_Hand_Rank_straight.append(q + 1)
                                    Villain_Hand_Rank_straight.append(q + 2)
                                    Villain_Hand_Rank_straight.append(q + 3)
                                    Villain_Hand_Rank_straight.append(q + 4)

                                    if len(Villain_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                Villain_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Villain_Hand_Rank_straight_flush.clear()

                                                            Villain_Hand_Rank_straight_flush.append(q)
                                                            Villain_Hand_Rank_straight_flush.append(q + 1)
                                                            Villain_Hand_Rank_straight_flush.append(q + 2)
                                                            Villain_Hand_Rank_straight_flush.append(q + 3)
                                                            Villain_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                VillainHand_Rank_Royal_Flush.clear()
                                                                VillainHand_Rank_Royal_Flush.append(0)
                                                                VillainHand_Rank_Royal_Flush.append(1)
                                                                VillainHand_Rank_Royal_Flush.append(2)
                                                                VillainHand_Rank_Royal_Flush.append(3)
                                                                VillainHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(Villain_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        Villain_Hand_Rank_straight.clear()

                                        Villain_Hand_Rank_straight.append(q)
                                        Villain_Hand_Rank_straight.append(q + 1)
                                        Villain_Hand_Rank_straight.append(q + 2)
                                        Villain_Hand_Rank_straight.append(q + 3)
                                        Villain_Hand_Rank_straight.append(q + 4)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[
                                                                        (v + 4), 'c']:

                                                                Villain_Hand_Rank_straight_flush.clear()

                                                                Villain_Hand_Rank_straight_flush.append(q)
                                                                Villain_Hand_Rank_straight_flush.append(q + 1)
                                                                Villain_Hand_Rank_straight_flush.append(q + 2)
                                                                Villain_Hand_Rank_straight_flush.append(q + 3)
                                                                Villain_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    VillainHand_Rank_Royal_Flush.clear()
                                                                    VillainHand_Rank_Royal_Flush.append(0)
                                                                    VillainHand_Rank_Royal_Flush.append(1)
                                                                    VillainHand_Rank_Royal_Flush.append(2)
                                                                    VillainHand_Rank_Royal_Flush.append(3)
                                                                    VillainHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(Villain_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        Villain_Hand_Rank_straight.clear()

                                        Villain_Hand_Rank_straight.append(q)
                                        Villain_Hand_Rank_straight.append(q + 1)
                                        Villain_Hand_Rank_straight.append(q + 2)
                                        Villain_Hand_Rank_straight.append(q + 3)
                                        Villain_Hand_Rank_straight.append(q + 4)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                Villain_Hand_Rank_straight_flush.clear()

                                                                Villain_Hand_Rank_straight_flush.append(q)
                                                                Villain_Hand_Rank_straight_flush.append(q + 1)
                                                                Villain_Hand_Rank_straight_flush.append(q + 2)
                                                                Villain_Hand_Rank_straight_flush.append(q + 3)
                                                                Villain_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    VillainHand_Rank_Royal_Flush.clear()
                                                                    VillainHand_Rank_Royal_Flush.append(0)
                                                                    VillainHand_Rank_Royal_Flush.append(1)
                                                                    VillainHand_Rank_Royal_Flush.append(2)
                                                                    VillainHand_Rank_Royal_Flush.append(3)
                                                                    VillainHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(Villain_Hand_dict_sortforstraight) == 4:
                break
            if len(Villain_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    Villain_Hand_dict_sortforpair["index"] = Villain_Hand_index
    Villain_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(10)
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(9)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[5, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 2:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(8)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(8)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(7)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if len(Villain_Hand_Rank_straight_wheel) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(6)
        Villain_Hand_Rank.append(9)
        Villain_Hand_Rank.append(10)
        Villain_Hand_Rank.append(11)
        Villain_Hand_Rank.append(12)
        Villain_Hand_Rank.append(13)

    if len(Villain_Hand_Rank_straight) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(6)
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[4])

    if len(Villain_Hand_Rank_Flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(5)
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[1])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 2:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 3:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 3:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])

    if len(Villain_Hand_Rank_straight_wheel_flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(2)
        Villain_Hand_Rank.append(9)
        Villain_Hand_Rank.append(10)
        Villain_Hand_Rank.append(11)
        Villain_Hand_Rank.append(12)
        Villain_Hand_Rank.append(13)

    if len(Villain_Hand_Rank_straight_flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(2)
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[4])

    if len(VillainHand_Rank_Royal_Flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(1)
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[0])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[1])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[2])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[3])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[4])

    ########################################################################################################################
    ########################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    BB_Card_Suits = []

    BB_Hand_Rank = []
    Card_Suits_ = []
    small_blind_card1_str = str(big_blind_card1)
    small_blind_card2_str = str(small_blind_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    BB_Card_Ranks = []

    big_blind_Hand_Rank = []
    big_blind_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == big_blind_card1[1]:
            big_blind_Hand_Suits.append(big_blind_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == big_blind_card2[1]:
            big_blind_Hand_Suits.append(big_blind_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == big_blind_card1[0]:
            big_blind_Hand_Rank.append(big_blind_card1[0])
            BB_Card_Ranks.append(y)
            BB_Card_Suits.append(big_blind_card1[1])

        if cards_value_df.at[y, "card_values"] == big_blind_card2[0]:
            big_blind_Hand_Rank.append(big_blind_card2[0])
            BB_Card_Ranks.append(y)
            BB_Card_Suits.append(big_blind_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            BB_Card_Suits.append(Flop_card1[1])
            BB_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            BB_Card_Suits.append(Flop_card2[1])
            BB_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            BB_Card_Suits.append(Flop_card3[1])
            BB_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            BB_Card_Suits.append(Turn[1])
            BB_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            BB_Card_Suits.append(River[1])
            BB_Card_Ranks.append(y)

        y += 1

    BB_Hand_df = pd.DataFrame(list(zip(BB_Card_Ranks, BB_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                              columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    BB_Hand_rank_suit_df = BB_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    BB_Hand_df_sum = BB_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    BB_Hand_sorted_df_sum = BB_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    BB_Suit_Sum_index = []
    BB_Suit_Sum_index.clear()
    n = 0
    while n < len(BB_Hand_sorted_df_sum["Suit_Value"]):
        BB_Suit_Sum_index.append(n)
        n += 1
    BB_Hand_sorted_df_sum["index"] = BB_Suit_Sum_index
    BB_Hand_sorted_df_sum.set_index("index", inplace=True)
    BB_Hand_Rank_Flush = []

    if BB_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        BB_Hand_Rank_Flush.clear()
        BB_Hand_Rank_Flush.append(5)
        if big_blind_card1[1] == BB_Hand_df.at[0, 'Card_Suit']:
            BB_Hand_Rank_Flush.append(BB_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if big_blind_card2[1] == BB_Hand_df.at[0, 'Card_Suit']:
            BB_Hand_Rank_Flush.append(BB_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            BB_Hand_Rank_Flush.append(0)
            BB_Hand_Rank_Flush.append(0)
            BB_Hand_Rank_Flush.append(0)
            BB_Hand_Rank_Flush.append(0)
            BB_Hand_Rank_Flush.append(0)

    Suit_for_straight = str(BB_Hand_sorted_df_sum.at[0, "Card_Suit"])

    small_blind_Hand_Rank_sort = sorted(small_blind_Hand_Rank)
    BB_Hand = sorted(BB_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    BB_seen = set()
    uniq = []
    BB_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    BB_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    BB_Hand_index = []
    for p in BB_Hand:
        if p not in BB_seen:
            BB_seen[p] = 1

        else:

            BB_seen[p] += 1

    while s < len(BB_seen):
        BB_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    BB_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = BB_seen.items()
    for item in items:
        BB_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    BB_Hand_dict = []
    BB_Hand_dict_sortforpair = []
    BB_Hand_dict_sortforstraight = []
    BB_Hand_dict = pd.DataFrame(list(zip(BB_Card_Rank_Hand, Num_of_Cards, BB_Card_Suits)),
                                columns=['a', 'b', 'c'])
    BB_Hand_dict_straight = pd.DataFrame(list(zip(BB_Card_Rank_Hand, Num_of_Cards, BB_Card_Suits)),
                                         columns=['a', 'b', 'c'])
    BB_Hand_dict_sortforpair = BB_Hand_dict.sort_values(by=['b'], ascending=False)
    BB_Hand_dict_sortforstraight = BB_Hand_dict_straight.sort_values(by=['a'])
    BB_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    BB_Hand_Rank_straight = []
    BB_Hand_Rank_straight.clear()
    BB_Hand_Rank_straight_wheel = []
    BB_Hand_Rank_straight_wheel.clear()
    BB_Hand_Rank_straight_wheel_flush = []
    BB_Hand_Rank_straight_wheel_flush.clear()
    BBHand_Rank_Royal_Flush = []
    BBHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    BB_Hand_Rank_straight_flush = []
    BB_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(BB_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if BB_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if BB_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if BB_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    BB_Hand_Rank_straight_wheel.clear()

                                    BB_Hand_Rank_straight_wheel.append(12)
                                    BB_Hand_Rank_straight_wheel.append(11)
                                    BB_Hand_Rank_straight_wheel.append(10)
                                    BB_Hand_Rank_straight_wheel.append(9)
                                    BB_Hand_Rank_straight_wheel.append(0)

                                    if len(BB_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            BB_Hand_Rank_straight_wheel_flush.clear()

                                                            BB_Hand_Rank_straight_wheel_flush.append(12)
                                                            BB_Hand_Rank_straight_wheel_flush.append(11)
                                                            BB_Hand_Rank_straight_wheel_flush.append(10)
                                                            BB_Hand_Rank_straight_wheel_flush.append(9)
                                                            BB_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(BB_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if BB_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if BB_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if BB_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        BB_Hand_Rank_straight_wheel.clear()

                                        BB_Hand_Rank_straight_wheel.append(12)
                                        BB_Hand_Rank_straight_wheel.append(11)
                                        BB_Hand_Rank_straight_wheel.append(10)
                                        BB_Hand_Rank_straight_wheel.append(9)
                                        BB_Hand_Rank_straight_wheel.append(0)

                                        if len(BB_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    BB_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                BB_Hand_Rank_straight_wheel_flush.clear()

                                                                BB_Hand_Rank_straight_wheel_flush.append(12)
                                                                BB_Hand_Rank_straight_wheel_flush.append(11)
                                                                BB_Hand_Rank_straight_wheel_flush.append(10)
                                                                BB_Hand_Rank_straight_wheel_flush.append(9)
                                                                BB_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(BB_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if BB_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if BB_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if BB_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        BB_Hand_Rank_straight_wheel.clear()

                                        BB_Hand_Rank_straight_wheel.append(12)
                                        BB_Hand_Rank_straight_wheel.append(11)
                                        BB_Hand_Rank_straight_wheel.append(10)
                                        BB_Hand_Rank_straight_wheel.append(9)
                                        BB_Hand_Rank_straight_wheel.append(0)

                                        if len(BB_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    BB_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                BB_Hand_Rank_straight_wheel_flush.clear()

                                                                BB_Hand_Rank_straight_wheel_flush.append(12)
                                                                BB_Hand_Rank_straight_wheel_flush.append(11)
                                                                BB_Hand_Rank_straight_wheel_flush.append(10)
                                                                BB_Hand_Rank_straight_wheel_flush.append(9)
                                                                BB_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(BB_Hand_dict_sortforstraight) == 4:
                break
            if len(BB_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(BB_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if BB_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if BB_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if BB_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    BB_Hand_Rank_straight.clear()

                                    BB_Hand_Rank_straight.append(q)
                                    BB_Hand_Rank_straight.append(q + 1)
                                    BB_Hand_Rank_straight.append(q + 2)
                                    BB_Hand_Rank_straight.append(q + 3)
                                    BB_Hand_Rank_straight.append(q + 4)

                                    if len(BB_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                BB_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            BB_Hand_Rank_straight_flush.clear()

                                                            BB_Hand_Rank_straight_flush.append(q)
                                                            BB_Hand_Rank_straight_flush.append(q + 1)
                                                            BB_Hand_Rank_straight_flush.append(q + 2)
                                                            BB_Hand_Rank_straight_flush.append(q + 3)
                                                            BB_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                BBHand_Rank_Royal_Flush.clear()
                                                                BBHand_Rank_Royal_Flush.append(0)
                                                                BBHand_Rank_Royal_Flush.append(1)
                                                                BBHand_Rank_Royal_Flush.append(2)
                                                                BBHand_Rank_Royal_Flush.append(3)
                                                                BBHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(BB_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if BB_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if BB_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if BB_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        BB_Hand_Rank_straight.clear()

                                        BB_Hand_Rank_straight.append(q)
                                        BB_Hand_Rank_straight.append(q + 1)
                                        BB_Hand_Rank_straight.append(q + 2)
                                        BB_Hand_Rank_straight.append(q + 3)
                                        BB_Hand_Rank_straight.append(q + 4)

                                        if len(BB_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                BB_Hand_Rank_straight_flush.clear()

                                                                BB_Hand_Rank_straight_flush.append(q)
                                                                BB_Hand_Rank_straight_flush.append(q + 1)
                                                                BB_Hand_Rank_straight_flush.append(q + 2)
                                                                BB_Hand_Rank_straight_flush.append(q + 3)
                                                                BB_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    BBHand_Rank_Royal_Flush.clear()
                                                                    BBHand_Rank_Royal_Flush.append(0)
                                                                    BBHand_Rank_Royal_Flush.append(1)
                                                                    BBHand_Rank_Royal_Flush.append(2)
                                                                    BBHand_Rank_Royal_Flush.append(3)
                                                                    BBHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(BB_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if BB_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if BB_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if BB_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if BB_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if BB_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        BB_Hand_Rank_straight.clear()

                                        BB_Hand_Rank_straight.append(q)
                                        BB_Hand_Rank_straight.append(q + 1)
                                        BB_Hand_Rank_straight.append(q + 2)
                                        BB_Hand_Rank_straight.append(q + 3)
                                        BB_Hand_Rank_straight.append(q + 4)

                                        if len(BB_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == BB_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == BB_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    BB_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                BB_Hand_Rank_straight_flush.clear()

                                                                BB_Hand_Rank_straight_flush.append(q)
                                                                BB_Hand_Rank_straight_flush.append(q + 1)
                                                                BB_Hand_Rank_straight_flush.append(q + 2)
                                                                BB_Hand_Rank_straight_flush.append(q + 3)
                                                                BB_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    BBHand_Rank_Royal_Flush.clear()
                                                                    BBHand_Rank_Royal_Flush.append(0)
                                                                    BBHand_Rank_Royal_Flush.append(1)
                                                                    BBHand_Rank_Royal_Flush.append(2)
                                                                    BBHand_Rank_Royal_Flush.append(3)
                                                                    BBHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(BB_Hand_dict_sortforstraight) == 4:
                break
            if len(BB_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    BB_Hand_dict_sortforpair["index"] = BB_Hand_index
    BB_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if BB_Hand_dict_sortforpair.at[0, "b"] == 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(10)
        BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
        BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])
        BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])
        BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
        BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[4, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 2:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 1:
            BB_Hand_Rank.clear()
            BB_Hand_Rank.append(9)
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[5, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[4, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 2:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 2:
            if BB_Hand_dict_sortforpair.at[2, "b"] == 2:
                BB_Hand_Rank.clear()
                BB_Hand_Rank.append(8)
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 2:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 2:
            if BB_Hand_dict_sortforpair.at[2, "b"] == 1:
                BB_Hand_Rank.clear()
                BB_Hand_Rank.append(8)
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[4, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 3:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 1:
            BB_Hand_Rank.clear()
            BB_Hand_Rank.append(7)
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[4, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if len(BB_Hand_Rank_straight_wheel) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(6)
        BB_Hand_Rank.append(9)
        BB_Hand_Rank.append(10)
        BB_Hand_Rank.append(11)
        BB_Hand_Rank.append(12)
        BB_Hand_Rank.append(13)

    if len(BB_Hand_Rank_straight) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(6)
        BB_Hand_Rank.append(BB_Hand_Rank_straight[0])
        BB_Hand_Rank.append(BB_Hand_Rank_straight[1])
        BB_Hand_Rank.append(BB_Hand_Rank_straight[2])
        BB_Hand_Rank.append(BB_Hand_Rank_straight[3])
        BB_Hand_Rank.append(BB_Hand_Rank_straight[4])

    if len(BB_Hand_Rank_Flush) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(5)
        BB_Hand_Rank.append(BB_Hand_Rank_Flush[1])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 3:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 2:
            if BB_Hand_dict_sortforpair.at[2, "b"] == 1:
                BB_Hand_Rank.clear()
                BB_Hand_Rank.append(4)
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 3:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 2:
            if BB_Hand_dict_sortforpair.at[2, "b"] == 2:
                BB_Hand_Rank.clear()
                BB_Hand_Rank.append(4)
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 3:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 3:
            if BB_Hand_dict_sortforpair.at[2, "b"] == 1:
                BB_Hand_Rank.clear()
                BB_Hand_Rank.append(4)
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
                BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 4:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 1:
            BB_Hand_Rank.clear()
            BB_Hand_Rank.append(3)
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[3, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 4:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 2:
            BB_Hand_Rank.clear()
            BB_Hand_Rank.append(3)
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[2, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])

    if BB_Hand_dict_sortforpair.at[0, "b"] == 4:
        if BB_Hand_dict_sortforpair.at[1, "b"] == 3:
            BB_Hand_Rank.clear()
            BB_Hand_Rank.append(3)
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[0, "a"])
            BB_Hand_Rank.append(BB_Hand_dict_sortforpair.at[1, "a"])

    if len(BB_Hand_Rank_straight_wheel_flush) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(2)
        BB_Hand_Rank.append(9)
        BB_Hand_Rank.append(10)
        BB_Hand_Rank.append(11)
        BB_Hand_Rank.append(12)
        BB_Hand_Rank.append(13)

    if len(BB_Hand_Rank_straight_flush) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(2)
        BB_Hand_Rank.append(BB_Hand_Rank_straight_flush[0])
        BB_Hand_Rank.append(BB_Hand_Rank_straight_flush[1])
        BB_Hand_Rank.append(BB_Hand_Rank_straight_flush[2])
        BB_Hand_Rank.append(BB_Hand_Rank_straight_flush[3])
        BB_Hand_Rank.append(BB_Hand_Rank_straight_flush[4])

    if len(BBHand_Rank_Royal_Flush) >= 1:
        BB_Hand_Rank.clear()
        BB_Hand_Rank.append(1)
        BB_Hand_Rank.append(BBHand_Rank_Royal_Flush[0])
        BB_Hand_Rank.append(BBHand_Rank_Royal_Flush[1])
        BB_Hand_Rank.append(BBHand_Rank_Royal_Flush[2])
        BB_Hand_Rank.append(BBHand_Rank_Royal_Flush[3])
        BB_Hand_Rank.append(BBHand_Rank_Royal_Flush[4])

    #########################################################################################################################
    #####################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    UTG_Card_Suits = []

    UTG_Hand_Rank = []
    Card_Suits_ = []
    UTG_card1_str = str(UTG_card1)
    UTG_card2_str = str(UTG_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    UTG_Card_Ranks = []

    UTG_Hand_Rank = []
    UTG_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == UTG_card1[1]:
            UTG_Hand_Suits.append(UTG_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == UTG_card2[1]:
            UTG_Hand_Suits.append(UTG_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == UTG_card1[0]:
            UTG_Hand_Rank.append(UTG_card1[0])
            UTG_Card_Ranks.append(y)
            UTG_Card_Suits.append(UTG_card1[1])

        if cards_value_df.at[y, "card_values"] == UTG_card2[0]:
            UTG_Hand_Rank.append(UTG_card2[0])
            UTG_Card_Ranks.append(y)
            UTG_Card_Suits.append(UTG_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            UTG_Card_Suits.append(Flop_card1[1])
            UTG_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            UTG_Card_Suits.append(Flop_card2[1])
            UTG_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            UTG_Card_Suits.append(Flop_card3[1])
            UTG_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            UTG_Card_Suits.append(Turn[1])
            UTG_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            UTG_Card_Suits.append(River[1])
            UTG_Card_Ranks.append(y)

        y += 1

    UTG_Hand_df = pd.DataFrame(list(zip(UTG_Card_Ranks, UTG_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                               columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    UTG_Hand_rank_suit_df = UTG_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    UTG_Hand_df_sum = UTG_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    UTG_Hand_sorted_df_sum = UTG_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    UTG_Suit_Sum_index = []
    UTG_Suit_Sum_index.clear()
    n = 0
    while n < len(UTG_Hand_sorted_df_sum["Suit_Value"]):
        UTG_Suit_Sum_index.append(n)
        n += 1
    UTG_Hand_sorted_df_sum["index"] = UTG_Suit_Sum_index
    UTG_Hand_sorted_df_sum.set_index("index", inplace=True)
    UTG_Hand_Rank_Flush = []

    if UTG_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        UTG_Hand_Rank_Flush.clear()
        UTG_Hand_Rank_Flush.append(5)
        if UTG_card1[1] == UTG_Hand_df.at[0, 'Card_Suit']:
            UTG_Hand_Rank_Flush.append(UTG_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if UTG_card2[1] == UTG_Hand_df.at[0, 'Card_Suit']:
            UTG_Hand_Rank_Flush.append(UTG_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            UTG_Hand_Rank_Flush.append(0)
            UTG_Hand_Rank_Flush.append(0)
            UTG_Hand_Rank_Flush.append(0)
            UTG_Hand_Rank_Flush.append(0)
            UTG_Hand_Rank_Flush.append(0)

    Suit_for_straight = str(UTG_Hand_sorted_df_sum.at[0, "Card_Suit"])

    UTG_Hand_Rank_sort = sorted(UTG_Hand_Rank)
    UTG_Hand = sorted(UTG_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    UTG_seen = set()
    uniq = []
    UTG_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    UTG_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    UTG_Hand_index = []
    for p in UTG_Hand:
        if p not in UTG_seen:
            UTG_seen[p] = 1

        else:

            UTG_seen[p] += 1

    while s < len(UTG_seen):
        UTG_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    UTG_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = UTG_seen.items()
    for item in items:
        UTG_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    UTG_Hand_dict = []
    UTG_Hand_dict_sortforpair = []
    UTG_Hand_dict_sortforstraight = []
    UTG_Hand_dict = pd.DataFrame(list(zip(UTG_Card_Rank_Hand, Num_of_Cards, UTG_Card_Suits)),
                                 columns=['a', 'b', 'c'])
    UTG_Hand_dict_straight = pd.DataFrame(list(zip(UTG_Card_Rank_Hand, Num_of_Cards, UTG_Card_Suits)),
                                          columns=['a', 'b', 'c'])
    UTG_Hand_dict_sortforpair = UTG_Hand_dict.sort_values(by=['b'], ascending=False)
    UTG_Hand_dict_sortforstraight = UTG_Hand_dict_straight.sort_values(by=['a'])
    UTG_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    UTG_Hand_Rank_straight = []
    UTG_Hand_Rank_straight.clear()
    UTG_Hand_Rank_straight_wheel = []
    UTG_Hand_Rank_straight_wheel.clear()
    UTG_Hand_Rank_straight_wheel_flush = []
    UTG_Hand_Rank_straight_wheel_flush.clear()
    UTGHand_Rank_Royal_Flush = []
    UTGHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    UTG_Hand_Rank_straight_flush = []
    UTG_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(UTG_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if UTG_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if UTG_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if UTG_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    UTG_Hand_Rank_straight_wheel.clear()

                                    UTG_Hand_Rank_straight_wheel.append(12)
                                    UTG_Hand_Rank_straight_wheel.append(11)
                                    UTG_Hand_Rank_straight_wheel.append(10)
                                    UTG_Hand_Rank_straight_wheel.append(9)
                                    UTG_Hand_Rank_straight_wheel.append(0)

                                    if len(UTG_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            UTG_Hand_Rank_straight_wheel_flush.clear()

                                                            UTG_Hand_Rank_straight_wheel_flush.append(12)
                                                            UTG_Hand_Rank_straight_wheel_flush.append(11)
                                                            UTG_Hand_Rank_straight_wheel_flush.append(10)
                                                            UTG_Hand_Rank_straight_wheel_flush.append(9)
                                                            UTG_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(UTG_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if UTG_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if UTG_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if UTG_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        UTG_Hand_Rank_straight_wheel.clear()

                                        UTG_Hand_Rank_straight_wheel.append(12)
                                        UTG_Hand_Rank_straight_wheel.append(11)
                                        UTG_Hand_Rank_straight_wheel.append(10)
                                        UTG_Hand_Rank_straight_wheel.append(9)
                                        UTG_Hand_Rank_straight_wheel.append(0)

                                        if len(UTG_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                UTG_Hand_Rank_straight_wheel_flush.clear()

                                                                UTG_Hand_Rank_straight_wheel_flush.append(12)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(11)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(10)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(9)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(UTG_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if UTG_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if UTG_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if UTG_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        UTG_Hand_Rank_straight_wheel.clear()

                                        UTG_Hand_Rank_straight_wheel.append(12)
                                        UTG_Hand_Rank_straight_wheel.append(11)
                                        UTG_Hand_Rank_straight_wheel.append(10)
                                        UTG_Hand_Rank_straight_wheel.append(9)
                                        UTG_Hand_Rank_straight_wheel.append(0)

                                        if len(UTG_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                UTG_Hand_Rank_straight_wheel_flush.clear()

                                                                UTG_Hand_Rank_straight_wheel_flush.append(12)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(11)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(10)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(9)
                                                                UTG_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(UTG_Hand_dict_sortforstraight) == 4:
                break
            if len(UTG_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(UTG_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if UTG_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if UTG_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if UTG_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    UTG_Hand_Rank_straight.clear()

                                    UTG_Hand_Rank_straight.append(q)
                                    UTG_Hand_Rank_straight.append(q + 1)
                                    UTG_Hand_Rank_straight.append(q + 2)
                                    UTG_Hand_Rank_straight.append(q + 3)
                                    UTG_Hand_Rank_straight.append(q + 4)

                                    if len(UTG_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                UTG_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            UTG_Hand_Rank_straight_flush.clear()

                                                            UTG_Hand_Rank_straight_flush.append(q)
                                                            UTG_Hand_Rank_straight_flush.append(q + 1)
                                                            UTG_Hand_Rank_straight_flush.append(q + 2)
                                                            UTG_Hand_Rank_straight_flush.append(q + 3)
                                                            UTG_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                UTGHand_Rank_Royal_Flush.clear()
                                                                UTGHand_Rank_Royal_Flush.append(0)
                                                                UTGHand_Rank_Royal_Flush.append(1)
                                                                UTGHand_Rank_Royal_Flush.append(2)
                                                                UTGHand_Rank_Royal_Flush.append(3)
                                                                UTGHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(UTG_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if UTG_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if UTG_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if UTG_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        UTG_Hand_Rank_straight.clear()

                                        UTG_Hand_Rank_straight.append(q)
                                        UTG_Hand_Rank_straight.append(q + 1)
                                        UTG_Hand_Rank_straight.append(q + 2)
                                        UTG_Hand_Rank_straight.append(q + 3)
                                        UTG_Hand_Rank_straight.append(q + 4)

                                        if len(UTG_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                UTG_Hand_Rank_straight_flush.clear()

                                                                UTG_Hand_Rank_straight_flush.append(q)
                                                                UTG_Hand_Rank_straight_flush.append(q + 1)
                                                                UTG_Hand_Rank_straight_flush.append(q + 2)
                                                                UTG_Hand_Rank_straight_flush.append(q + 3)
                                                                UTG_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    UTGHand_Rank_Royal_Flush.clear()
                                                                    UTGHand_Rank_Royal_Flush.append(0)
                                                                    UTGHand_Rank_Royal_Flush.append(1)
                                                                    UTGHand_Rank_Royal_Flush.append(2)
                                                                    UTGHand_Rank_Royal_Flush.append(3)
                                                                    UTGHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(UTG_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if UTG_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if UTG_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if UTG_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if UTG_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if UTG_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        UTG_Hand_Rank_straight.clear()

                                        UTG_Hand_Rank_straight.append(q)
                                        UTG_Hand_Rank_straight.append(q + 1)
                                        UTG_Hand_Rank_straight.append(q + 2)
                                        UTG_Hand_Rank_straight.append(q + 3)
                                        UTG_Hand_Rank_straight.append(q + 4)

                                        if len(UTG_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == UTG_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                UTG_Hand_Rank_straight_flush.clear()

                                                                UTG_Hand_Rank_straight_flush.append(q)
                                                                UTG_Hand_Rank_straight_flush.append(q + 1)
                                                                UTG_Hand_Rank_straight_flush.append(q + 2)
                                                                UTG_Hand_Rank_straight_flush.append(q + 3)
                                                                UTG_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    UTGHand_Rank_Royal_Flush.clear()
                                                                    UTGHand_Rank_Royal_Flush.append(0)
                                                                    UTGHand_Rank_Royal_Flush.append(1)
                                                                    UTGHand_Rank_Royal_Flush.append(2)
                                                                    UTGHand_Rank_Royal_Flush.append(3)
                                                                    UTGHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(UTG_Hand_dict_sortforstraight) == 4:
                break
            if len(UTG_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    UTG_Hand_dict_sortforpair["index"] = UTG_Hand_index
    UTG_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(10)
        UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
        UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])
        UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])
        UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
        UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[4, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG_Hand_Rank.clear()
            UTG_Hand_Rank.append(9)
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[5, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[4, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG_Hand_dict_sortforpair.at[2, "b"] == 2:
                UTG_Hand_Rank.clear()
                UTG_Hand_Rank.append(8)
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG_Hand_Rank.clear()
                UTG_Hand_Rank.append(8)
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[4, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG_Hand_Rank.clear()
            UTG_Hand_Rank.append(7)
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[4, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if len(UTG_Hand_Rank_straight_wheel) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(6)
        UTG_Hand_Rank.append(9)
        UTG_Hand_Rank.append(10)
        UTG_Hand_Rank.append(11)
        UTG_Hand_Rank.append(12)
        UTG_Hand_Rank.append(13)

    if len(UTG_Hand_Rank_straight) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(6)
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight[0])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight[1])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight[2])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight[3])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight[4])

    if len(UTG_Hand_Rank_Flush) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(5)
        UTG_Hand_Rank.append(UTG_Hand_Rank_Flush[1])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG_Hand_Rank.clear()
                UTG_Hand_Rank.append(4)
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG_Hand_dict_sortforpair.at[2, "b"] == 2:
                UTG_Hand_Rank.clear()
                UTG_Hand_Rank.append(4)
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 3:
            if UTG_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG_Hand_Rank.clear()
                UTG_Hand_Rank.append(4)
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
                UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG_Hand_Rank.clear()
            UTG_Hand_Rank.append(3)
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[3, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 2:
            UTG_Hand_Rank.clear()
            UTG_Hand_Rank.append(3)
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[2, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])

    if UTG_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG_Hand_dict_sortforpair.at[1, "b"] == 3:
            UTG_Hand_Rank.clear()
            UTG_Hand_Rank.append(3)
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[0, "a"])
            UTG_Hand_Rank.append(UTG_Hand_dict_sortforpair.at[1, "a"])

    if len(UTG_Hand_Rank_straight_wheel_flush) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(2)
        UTG_Hand_Rank.append(9)
        UTG_Hand_Rank.append(10)
        UTG_Hand_Rank.append(11)
        UTG_Hand_Rank.append(12)
        UTG_Hand_Rank.append(13)

    if len(UTG_Hand_Rank_straight_flush) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(2)
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight_flush[0])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight_flush[1])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight_flush[2])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight_flush[3])
        UTG_Hand_Rank.append(UTG_Hand_Rank_straight_flush[4])

    if len(UTGHand_Rank_Royal_Flush) >= 1:
        UTG_Hand_Rank.clear()
        UTG_Hand_Rank.append(1)
        UTG_Hand_Rank.append(UTGHand_Rank_Royal_Flush[0])
        UTG_Hand_Rank.append(UTGHand_Rank_Royal_Flush[1])
        UTG_Hand_Rank.append(UTGHand_Rank_Royal_Flush[2])
        UTG_Hand_Rank.append(UTGHand_Rank_Royal_Flush[3])
        UTG_Hand_Rank.append(UTGHand_Rank_Royal_Flush[4])

    #########################################################################################################################
    ####################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    UTG2_Card_Suits = []

    UTG2_Hand_Rank = []
    Card_Suits_ = []
    UTG2_card1_str = str(UTG2_card1)
    UTG2_card2_str = str(UTG2_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    UTG2_Card_Ranks = []

    UTG2_Hand_Rank = []
    UTG2_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == UTG2_card1[1]:
            UTG2_Hand_Suits.append(UTG2_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == UTG2_card2[1]:
            UTG2_Hand_Suits.append(UTG2_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == UTG2_card1[0]:
            UTG2_Hand_Rank.append(UTG2_card1[0])
            UTG2_Card_Ranks.append(y)
            UTG2_Card_Suits.append(UTG2_card1[1])

        if cards_value_df.at[y, "card_values"] == UTG2_card2[0]:
            UTG2_Hand_Rank.append(UTG2_card2[0])
            UTG2_Card_Ranks.append(y)
            UTG2_Card_Suits.append(UTG2_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            UTG2_Card_Suits.append(Flop_card1[1])
            UTG2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            UTG2_Card_Suits.append(Flop_card2[1])
            UTG2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            UTG2_Card_Suits.append(Flop_card3[1])
            UTG2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            UTG2_Card_Suits.append(Turn[1])
            UTG2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            UTG2_Card_Suits.append(River[1])
            UTG2_Card_Ranks.append(y)

        y += 1

    UTG2_Hand_df = pd.DataFrame(list(zip(UTG2_Card_Ranks, UTG2_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                                columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    UTG2_Hand_rank_suit_df = UTG2_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    UTG2_Hand_df_sum = UTG2_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    UTG2_Hand_sorted_df_sum = UTG2_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    UTG2_Suit_Sum_index = []
    UTG2_Suit_Sum_index.clear()
    n = 0
    while n < len(UTG2_Hand_sorted_df_sum["Suit_Value"]):
        UTG2_Suit_Sum_index.append(n)
        n += 1
    UTG2_Hand_sorted_df_sum["index"] = UTG2_Suit_Sum_index
    UTG2_Hand_sorted_df_sum.set_index("index", inplace=True)
    UTG2_Hand_Rank_Flush = []

    if UTG2_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        UTG2_Hand_Rank_Flush.clear()
        UTG2_Hand_Rank_Flush.append(5)
        if UTG2_card1[1] == UTG2_Hand_df.at[0, 'Card_Suit']:
            UTG2_Hand_Rank_Flush.append(UTG2_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if UTG2_card2[1] == UTG2_Hand_df.at[0, 'Card_Suit']:
            UTG2_Hand_Rank_Flush.append(UTG2_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            UTG2_Hand_Rank_Flush.append(0)
            UTG2_Hand_Rank_Flush.append(0)
            UTG2_Hand_Rank_Flush.append(0)
            UTG2_Hand_Rank_Flush.append(0)
            UTG2_Hand_Rank_Flush.append(0)

    Suit_for_straight = str(UTG2_Hand_sorted_df_sum.at[0, "Card_Suit"])

    UTG2_Hand_Rank_sort = sorted(UTG2_Hand_Rank)
    UTG2_Hand = sorted(UTG2_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    UTG2_seen = set()
    uniq = []
    UTG2_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    UTG2_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    UTG2_Hand_index = []
    for p in UTG2_Hand:
        if p not in UTG2_seen:
            UTG2_seen[p] = 1

        else:

            UTG2_seen[p] += 1

    while s < len(UTG2_seen):
        UTG2_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    UTG2_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    # Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = UTG2_seen.items()
    for item in items:
        UTG2_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    UTG2_Hand_dict = []
    UTG2_Hand_dict_sortforpair = []
    UTG2_Hand_dict_sortforstraight = []
    UTG2_Hand_dict = pd.DataFrame(list(zip(UTG2_Card_Rank_Hand, Num_of_Cards, UTG2_Card_Suits)),
                                  columns=['a', 'b', 'c'])
    UTG2_Hand_dict_straight = pd.DataFrame(list(zip(UTG2_Card_Rank_Hand, Num_of_Cards, UTG2_Card_Suits)),
                                           columns=['a', 'b', 'c'])
    UTG2_Hand_dict_sortforpair = UTG2_Hand_dict.sort_values(by=['b'], ascending=False)
    UTG2_Hand_dict_sortforstraight = UTG2_Hand_dict_straight.sort_values(by=['a'])
    UTG2_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    UTG2_Hand_Rank_straight = []
    UTG2_Hand_Rank_straight.clear()
    UTG2_Hand_Rank_straight_wheel = []
    UTG2_Hand_Rank_straight_wheel.clear()
    UTG2_Hand_Rank_straight_wheel_flush = []
    UTG2_Hand_Rank_straight_wheel_flush.clear()
    UTG2Hand_Rank_Royal_Flush = []
    UTG2Hand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    UTG2_Hand_Rank_straight_flush = []
    UTG2_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(UTG2_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if UTG2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if UTG2_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if UTG2_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    UTG2_Hand_Rank_straight_wheel.clear()

                                    UTG2_Hand_Rank_straight_wheel.append(12)
                                    UTG2_Hand_Rank_straight_wheel.append(11)
                                    UTG2_Hand_Rank_straight_wheel.append(10)
                                    UTG2_Hand_Rank_straight_wheel.append(9)
                                    UTG2_Hand_Rank_straight_wheel.append(0)

                                    if len(UTG2_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            UTG2_Hand_Rank_straight_wheel_flush.clear()

                                                            UTG2_Hand_Rank_straight_wheel_flush.append(12)
                                                            UTG2_Hand_Rank_straight_wheel_flush.append(11)
                                                            UTG2_Hand_Rank_straight_wheel_flush.append(10)
                                                            UTG2_Hand_Rank_straight_wheel_flush.append(9)
                                                            UTG2_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(UTG2_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if UTG2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if UTG2_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if UTG2_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        UTG2_Hand_Rank_straight_wheel.clear()

                                        UTG2_Hand_Rank_straight_wheel.append(12)
                                        UTG2_Hand_Rank_straight_wheel.append(11)
                                        UTG2_Hand_Rank_straight_wheel.append(10)
                                        UTG2_Hand_Rank_straight_wheel.append(9)
                                        UTG2_Hand_Rank_straight_wheel.append(0)

                                        if len(UTG2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG2_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                UTG2_Hand_Rank_straight_wheel_flush.clear()

                                                                UTG2_Hand_Rank_straight_wheel_flush.append(12)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(11)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(10)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(9)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(UTG2_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if UTG2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if UTG2_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        UTG2_Hand_Rank_straight_wheel.clear()

                                        UTG2_Hand_Rank_straight_wheel.append(12)
                                        UTG2_Hand_Rank_straight_wheel.append(11)
                                        UTG2_Hand_Rank_straight_wheel.append(10)
                                        UTG2_Hand_Rank_straight_wheel.append(9)
                                        UTG2_Hand_Rank_straight_wheel.append(0)

                                        if len(UTG2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG2_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                UTG2_Hand_Rank_straight_wheel_flush.clear()

                                                                UTG2_Hand_Rank_straight_wheel_flush.append(12)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(11)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(10)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(9)
                                                                UTG2_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(UTG2_Hand_dict_sortforstraight) == 4:
                break
            if len(UTG2_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(UTG2_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if UTG2_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if UTG2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if UTG2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    UTG2_Hand_Rank_straight.clear()

                                    UTG2_Hand_Rank_straight.append(q)
                                    UTG2_Hand_Rank_straight.append(q + 1)
                                    UTG2_Hand_Rank_straight.append(q + 2)
                                    UTG2_Hand_Rank_straight.append(q + 3)
                                    UTG2_Hand_Rank_straight.append(q + 4)

                                    if len(UTG2_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                UTG2_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            UTG2_Hand_Rank_straight_flush.clear()

                                                            UTG2_Hand_Rank_straight_flush.append(q)
                                                            UTG2_Hand_Rank_straight_flush.append(q + 1)
                                                            UTG2_Hand_Rank_straight_flush.append(q + 2)
                                                            UTG2_Hand_Rank_straight_flush.append(q + 3)
                                                            UTG2_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                UTG2Hand_Rank_Royal_Flush.clear()
                                                                UTG2Hand_Rank_Royal_Flush.append(0)
                                                                UTG2Hand_Rank_Royal_Flush.append(1)
                                                                UTG2Hand_Rank_Royal_Flush.append(2)
                                                                UTG2Hand_Rank_Royal_Flush.append(3)
                                                                UTG2Hand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(UTG2_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if UTG2_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if UTG2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        UTG2_Hand_Rank_straight.clear()

                                        UTG2_Hand_Rank_straight.append(q)
                                        UTG2_Hand_Rank_straight.append(q + 1)
                                        UTG2_Hand_Rank_straight.append(q + 2)
                                        UTG2_Hand_Rank_straight.append(q + 3)
                                        UTG2_Hand_Rank_straight.append(q + 4)

                                        if len(UTG2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                UTG2_Hand_Rank_straight_flush.clear()

                                                                UTG2_Hand_Rank_straight_flush.append(q)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 1)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 2)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 3)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    UTG2Hand_Rank_Royal_Flush.clear()
                                                                    UTG2Hand_Rank_Royal_Flush.append(0)
                                                                    UTG2Hand_Rank_Royal_Flush.append(1)
                                                                    UTG2Hand_Rank_Royal_Flush.append(2)
                                                                    UTG2Hand_Rank_Royal_Flush.append(3)
                                                                    UTG2Hand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(UTG2_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if UTG2_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if UTG2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if UTG2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if UTG2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if UTG2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        UTG2_Hand_Rank_straight.clear()

                                        UTG2_Hand_Rank_straight.append(q)
                                        UTG2_Hand_Rank_straight.append(q + 1)
                                        UTG2_Hand_Rank_straight.append(q + 2)
                                        UTG2_Hand_Rank_straight.append(q + 3)
                                        UTG2_Hand_Rank_straight.append(q + 4)

                                        if len(UTG2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == UTG2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    UTG2_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                UTG2_Hand_Rank_straight_flush.clear()

                                                                UTG2_Hand_Rank_straight_flush.append(q)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 1)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 2)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 3)
                                                                UTG2_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    UTG2Hand_Rank_Royal_Flush.clear()
                                                                    UTG2Hand_Rank_Royal_Flush.append(0)
                                                                    UTG2Hand_Rank_Royal_Flush.append(1)
                                                                    UTG2Hand_Rank_Royal_Flush.append(2)
                                                                    UTG2Hand_Rank_Royal_Flush.append(3)
                                                                    UTG2Hand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(UTG2_Hand_dict_sortforstraight) == 4:
                break
            if len(UTG2_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    UTG2_Hand_dict_sortforpair["index"] = UTG2_Hand_index
    UTG2_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(10)
        UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
        UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])
        UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])
        UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
        UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[4, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG2_Hand_Rank.clear()
            UTG2_Hand_Rank.append(9)
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[5, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[4, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG2_Hand_dict_sortforpair.at[2, "b"] == 2:
                UTG2_Hand_Rank.clear()
                UTG2_Hand_Rank.append(8)
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG2_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG2_Hand_Rank.clear()
                UTG2_Hand_Rank.append(8)
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[4, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG2_Hand_Rank.clear()
            UTG2_Hand_Rank.append(7)
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[4, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if len(UTG2_Hand_Rank_straight_wheel) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(6)
        UTG2_Hand_Rank.append(9)
        UTG2_Hand_Rank.append(10)
        UTG2_Hand_Rank.append(11)
        UTG2_Hand_Rank.append(12)
        UTG2_Hand_Rank.append(13)

    if len(UTG2_Hand_Rank_straight) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(6)
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight[0])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight[1])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight[2])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight[3])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight[4])

    if len(UTG2_Hand_Rank_Flush) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(5)
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_Flush[1])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG2_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG2_Hand_Rank.clear()
                UTG2_Hand_Rank.append(4)
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if UTG2_Hand_dict_sortforpair.at[2, "b"] == 2:
                UTG2_Hand_Rank.clear()
                UTG2_Hand_Rank.append(4)
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 3:
            if UTG2_Hand_dict_sortforpair.at[2, "b"] == 1:
                UTG2_Hand_Rank.clear()
                UTG2_Hand_Rank.append(4)
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
                UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 1:
            UTG2_Hand_Rank.clear()
            UTG2_Hand_Rank.append(3)
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[3, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 2:
            UTG2_Hand_Rank.clear()
            UTG2_Hand_Rank.append(3)
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[2, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])

    if UTG2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if UTG2_Hand_dict_sortforpair.at[1, "b"] == 3:
            UTG2_Hand_Rank.clear()
            UTG2_Hand_Rank.append(3)
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[0, "a"])
            UTG2_Hand_Rank.append(UTG2_Hand_dict_sortforpair.at[1, "a"])

    if len(UTG2_Hand_Rank_straight_wheel_flush) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(2)
        UTG2_Hand_Rank.append(9)
        UTG2_Hand_Rank.append(10)
        UTG2_Hand_Rank.append(11)
        UTG2_Hand_Rank.append(12)
        UTG2_Hand_Rank.append(13)

    if len(UTG2_Hand_Rank_straight_flush) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(2)
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight_flush[0])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight_flush[1])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight_flush[2])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight_flush[3])
        UTG2_Hand_Rank.append(UTG2_Hand_Rank_straight_flush[4])

    if len(UTG2Hand_Rank_Royal_Flush) >= 1:
        UTG2_Hand_Rank.clear()
        UTG2_Hand_Rank.append(1)
        UTG2_Hand_Rank.append(UTG2Hand_Rank_Royal_Flush[0])
        UTG2_Hand_Rank.append(UTG2Hand_Rank_Royal_Flush[1])
        UTG2_Hand_Rank.append(UTG2Hand_Rank_Royal_Flush[2])
        UTG2_Hand_Rank.append(UTG2Hand_Rank_Royal_Flush[3])
        UTG2_Hand_Rank.append(UTG2Hand_Rank_Royal_Flush[4])

    ##########################################################################################################################
    ########################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    MP_Card_Suits = []

    MP_Hand_Rank = []
    Card_Suits_ = []
    MP_card1_str = str(MP_card1)
    MP_card2_str = str(MP_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    MP_Card_Ranks = []

    MP_Hand_Rank = []
    MP_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == MP_card1[1]:
            MP_Hand_Suits.append(MP_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == MP_card2[1]:
            MP_Hand_Suits.append(MP_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP_card1[0]:
            MP_Hand_Rank.append(MP_card1[0])
            MP_Card_Ranks.append(y)
            MP_Card_Suits.append(MP_card1[1])

        if cards_value_df.at[y, "card_values"] == MP_card2[0]:
            MP_Hand_Rank.append(MP_card2[0])
            MP_Card_Ranks.append(y)
            MP_Card_Suits.append(MP_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            MP_Card_Suits.append(Flop_card1[1])
            MP_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            MP_Card_Suits.append(Flop_card2[1])
            MP_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            MP_Card_Suits.append(Flop_card3[1])
            MP_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            MP_Card_Suits.append(Turn[1])
            MP_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            MP_Card_Suits.append(River[1])
            MP_Card_Ranks.append(y)

        y += 1

    MP_Hand_df = pd.DataFrame(list(zip(MP_Card_Ranks, MP_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                              columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    MP_Hand_rank_suit_df = MP_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    MP_Hand_df_sum = MP_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    MP_Hand_sorted_df_sum = MP_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    MP_Suit_Sum_index = []
    MP_Suit_Sum_index.clear()
    n = 0
    while n < len(MP_Hand_sorted_df_sum["Suit_Value"]):
        MP_Suit_Sum_index.append(n)
        n += 1
    MP_Hand_sorted_df_sum["index"] = MP_Suit_Sum_index
    MP_Hand_sorted_df_sum.set_index("index", inplace=True)
    MP_Hand_Rank_Flush = []

    if MP_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        MP_Hand_Rank_Flush.clear()
        MP_Hand_Rank_Flush.append(5)
        if MP_card1[1] == MP_Hand_df.at[0, 'Card_Suit']:
            MP_Hand_Rank_Flush.append(MP_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if MP_card2[1] == MP_Hand_df.at[0, 'Card_Suit']:
            MP_Hand_Rank_Flush.append(MP_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            MP_Hand_Rank_Flush.append(0)
            MP_Hand_Rank_Flush.append(0)
            MP_Hand_Rank_Flush.append(0)
            MP_Hand_Rank_Flush.append(0)
            MP_Hand_Rank_Flush.append(0)

    Suit_for_straight = ""
    Suit_for_straight = str(MP_Hand_sorted_df_sum.at[0, "Card_Suit"])

    MP_Hand_Rank_sort = sorted(MP_Hand_Rank)
    MP_Hand = sorted(MP_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    MP_seen = set()
    uniq = []
    MP_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    MP_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    MP_Hand_index = []
    for p in MP_Hand:
        if p not in MP_seen:
            MP_seen[p] = 1

        else:

            MP_seen[p] += 1

    while s < len(MP_seen):
        MP_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    MP_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    # Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = MP_seen.items()
    for item in items:
        MP_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    MP_Hand_dict = []
    MP_Hand_dict_sortforpair = []
    MP_Hand_dict_sortforstraight = []
    MP_Hand_dict = pd.DataFrame(list(zip(MP_Card_Rank_Hand, Num_of_Cards, MP_Card_Suits)),
                                columns=['a', 'b', 'c'])
    MP_Hand_dict_straight = pd.DataFrame(list(zip(MP_Card_Rank_Hand, Num_of_Cards, MP_Card_Suits)),
                                         columns=['a', 'b', 'c'])
    MP_Hand_dict_sortforpair = MP_Hand_dict.sort_values(by=['b'], ascending=False)
    MP_Hand_dict_sortforstraight = MP_Hand_dict_straight.sort_values(by=['a'])
    MP_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    MP_Hand_Rank_straight = []
    MP_Hand_Rank_straight.clear()
    MP_Hand_Rank_straight_wheel = []
    MP_Hand_Rank_straight_wheel.clear()
    MP_Hand_Rank_straight_wheel_flush = []
    MP_Hand_Rank_straight_wheel_flush.clear()
    MPHand_Rank_Royal_Flush = []
    MPHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    MP_Hand_Rank_straight_flush = []
    MP_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(MP_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if MP_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if MP_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    MP_Hand_Rank_straight_wheel.clear()

                                    MP_Hand_Rank_straight_wheel.append(12)
                                    MP_Hand_Rank_straight_wheel.append(11)
                                    MP_Hand_Rank_straight_wheel.append(10)
                                    MP_Hand_Rank_straight_wheel.append(9)
                                    MP_Hand_Rank_straight_wheel.append(0)

                                    if len(MP_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            MP_Hand_Rank_straight_wheel_flush.clear()

                                                            MP_Hand_Rank_straight_wheel_flush.append(12)
                                                            MP_Hand_Rank_straight_wheel_flush.append(11)
                                                            MP_Hand_Rank_straight_wheel_flush.append(10)
                                                            MP_Hand_Rank_straight_wheel_flush.append(9)
                                                            MP_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(MP_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if MP_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        MP_Hand_Rank_straight_wheel.clear()

                                        MP_Hand_Rank_straight_wheel.append(12)
                                        MP_Hand_Rank_straight_wheel.append(11)
                                        MP_Hand_Rank_straight_wheel.append(10)
                                        MP_Hand_Rank_straight_wheel.append(9)
                                        MP_Hand_Rank_straight_wheel.append(0)

                                        if len(MP_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                MP_Hand_Rank_straight_wheel_flush.clear()

                                                                MP_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(MP_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if MP_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if MP_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        MP_Hand_Rank_straight_wheel.clear()

                                        MP_Hand_Rank_straight_wheel.append(12)
                                        MP_Hand_Rank_straight_wheel.append(11)
                                        MP_Hand_Rank_straight_wheel.append(10)
                                        MP_Hand_Rank_straight_wheel.append(9)
                                        MP_Hand_Rank_straight_wheel.append(0)

                                        if len(MP_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                MP_Hand_Rank_straight_wheel_flush.clear()

                                                                MP_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(MP_Hand_dict_sortforstraight) == 4:
                break
            if len(MP_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(MP_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if MP_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if MP_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    MP_Hand_Rank_straight.clear()

                                    MP_Hand_Rank_straight.append(q)
                                    MP_Hand_Rank_straight.append(q + 1)
                                    MP_Hand_Rank_straight.append(q + 2)
                                    MP_Hand_Rank_straight.append(q + 3)
                                    MP_Hand_Rank_straight.append(q + 4)

                                    if len(MP_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                MP_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            MP_Hand_Rank_straight_flush.clear()

                                                            MP_Hand_Rank_straight_flush.append(q)
                                                            MP_Hand_Rank_straight_flush.append(q + 1)
                                                            MP_Hand_Rank_straight_flush.append(q + 2)
                                                            MP_Hand_Rank_straight_flush.append(q + 3)
                                                            MP_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                MPHand_Rank_Royal_Flush.clear()
                                                                MPHand_Rank_Royal_Flush.append(0)
                                                                MPHand_Rank_Royal_Flush.append(1)
                                                                MPHand_Rank_Royal_Flush.append(2)
                                                                MPHand_Rank_Royal_Flush.append(3)
                                                                MPHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(MP_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP_Hand_Rank_straight.clear()

                                        MP_Hand_Rank_straight.append(q)
                                        MP_Hand_Rank_straight.append(q + 1)
                                        MP_Hand_Rank_straight.append(q + 2)
                                        MP_Hand_Rank_straight.append(q + 3)
                                        MP_Hand_Rank_straight.append(q + 4)

                                        if len(MP_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                MP_Hand_Rank_straight_flush.clear()

                                                                MP_Hand_Rank_straight_flush.append(q)
                                                                MP_Hand_Rank_straight_flush.append(q + 1)
                                                                MP_Hand_Rank_straight_flush.append(q + 2)
                                                                MP_Hand_Rank_straight_flush.append(q + 3)
                                                                MP_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MPHand_Rank_Royal_Flush.clear()
                                                                    MPHand_Rank_Royal_Flush.append(0)
                                                                    MPHand_Rank_Royal_Flush.append(1)
                                                                    MPHand_Rank_Royal_Flush.append(2)
                                                                    MPHand_Rank_Royal_Flush.append(3)
                                                                    MPHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(MP_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP_Hand_Rank_straight.clear()

                                        MP_Hand_Rank_straight.append(q)
                                        MP_Hand_Rank_straight.append(q + 1)
                                        MP_Hand_Rank_straight.append(q + 2)
                                        MP_Hand_Rank_straight.append(q + 3)
                                        MP_Hand_Rank_straight.append(q + 4)

                                        if len(MP_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                MP_Hand_Rank_straight_flush.clear()

                                                                MP_Hand_Rank_straight_flush.append(q)
                                                                MP_Hand_Rank_straight_flush.append(q + 1)
                                                                MP_Hand_Rank_straight_flush.append(q + 2)
                                                                MP_Hand_Rank_straight_flush.append(q + 3)
                                                                MP_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MPHand_Rank_Royal_Flush.clear()
                                                                    MPHand_Rank_Royal_Flush.append(0)
                                                                    MPHand_Rank_Royal_Flush.append(1)
                                                                    MPHand_Rank_Royal_Flush.append(2)
                                                                    MPHand_Rank_Royal_Flush.append(3)
                                                                    MPHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(MP_Hand_dict_sortforstraight) == 4:
                break
            if len(MP_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    MP_Hand_dict_sortforpair["index"] = MP_Hand_index
    MP_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if MP_Hand_dict_sortforpair.at[0, "b"] == 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(10)
        MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
        MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])
        MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])
        MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
        MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[4, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP_Hand_Rank.clear()
            MP_Hand_Rank.append(9)
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[5, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[4, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP_Hand_Rank.clear()
                MP_Hand_Rank.append(8)
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP_Hand_Rank.clear()
                MP_Hand_Rank.append(8)
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[4, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP_Hand_Rank.clear()
            MP_Hand_Rank.append(7)
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[4, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if len(MP_Hand_Rank_straight_wheel) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(6)
        MP_Hand_Rank.append(9)
        MP_Hand_Rank.append(10)
        MP_Hand_Rank.append(11)
        MP_Hand_Rank.append(12)
        MP_Hand_Rank.append(13)

    if len(MP_Hand_Rank_straight) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(6)
        MP_Hand_Rank.append(MP_Hand_Rank_straight[0])
        MP_Hand_Rank.append(MP_Hand_Rank_straight[1])
        MP_Hand_Rank.append(MP_Hand_Rank_straight[2])
        MP_Hand_Rank.append(MP_Hand_Rank_straight[3])
        MP_Hand_Rank.append(MP_Hand_Rank_straight[4])

    if len(MP_Hand_Rank_Flush) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(5)
        MP_Hand_Rank.append(MP_Hand_Rank_Flush[1])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP_Hand_Rank.clear()
                MP_Hand_Rank.append(4)
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP_Hand_Rank.clear()
                MP_Hand_Rank.append(4)
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 3:
            if MP_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP_Hand_Rank.clear()
                MP_Hand_Rank.append(4)
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
                MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP_Hand_Rank.clear()
            MP_Hand_Rank.append(3)
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[3, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 2:
            MP_Hand_Rank.clear()
            MP_Hand_Rank.append(3)
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[2, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])

    if MP_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP_Hand_dict_sortforpair.at[1, "b"] == 3:
            MP_Hand_Rank.clear()
            MP_Hand_Rank.append(3)
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[0, "a"])
            MP_Hand_Rank.append(MP_Hand_dict_sortforpair.at[1, "a"])

    if len(MP_Hand_Rank_straight_wheel_flush) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(2)
        MP_Hand_Rank.append(9)
        MP_Hand_Rank.append(10)
        MP_Hand_Rank.append(11)
        MP_Hand_Rank.append(12)
        MP_Hand_Rank.append(13)

    if len(MP_Hand_Rank_straight_flush) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(2)
        MP_Hand_Rank.append(MP_Hand_Rank_straight_flush[0])
        MP_Hand_Rank.append(MP_Hand_Rank_straight_flush[1])
        MP_Hand_Rank.append(MP_Hand_Rank_straight_flush[2])
        MP_Hand_Rank.append(MP_Hand_Rank_straight_flush[3])
        MP_Hand_Rank.append(MP_Hand_Rank_straight_flush[4])

    if len(MPHand_Rank_Royal_Flush) >= 1:
        MP_Hand_Rank.clear()
        MP_Hand_Rank.append(1)
        MP_Hand_Rank.append(MPHand_Rank_Royal_Flush[0])
        MP_Hand_Rank.append(MPHand_Rank_Royal_Flush[1])
        MP_Hand_Rank.append(MPHand_Rank_Royal_Flush[2])
        MP_Hand_Rank.append(MPHand_Rank_Royal_Flush[3])
        MP_Hand_Rank.append(MPHand_Rank_Royal_Flush[4])

    #########################################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []

    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    MP2_Card_Suits = []

    MP2_Hand_Rank = []
    Card_Suits_ = []
    MP2_card1_str = str(MP2_card1)
    MP2_card2_str = str(MP2_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    MP2_Card_Ranks = []

    MP2_Hand_Rank = []
    MP2_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == MP2_card1[1]:
            MP2_Hand_Suits.append(MP2_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == MP2_card2[1]:
            MP2_Hand_Suits.append(MP2_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP2_card1[0]:
            MP2_Hand_Rank.append(MP2_card1[0])
            MP2_Card_Ranks.append(y)
            MP2_Card_Suits.append(MP2_card1[1])

        if cards_value_df.at[y, "card_values"] == MP2_card2[0]:
            MP2_Hand_Rank.append(MP2_card2[0])
            MP2_Card_Ranks.append(y)
            MP2_Card_Suits.append(MP2_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            MP2_Card_Suits.append(Flop_card1[1])
            MP2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            MP2_Card_Suits.append(Flop_card2[1])
            MP2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            MP2_Card_Suits.append(Flop_card3[1])
            MP2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            MP2_Card_Suits.append(Turn[1])
            MP2_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            MP2_Card_Suits.append(River[1])
            MP2_Card_Ranks.append(y)

        y += 1

    MP2_Hand_df = pd.DataFrame(list(zip(MP2_Card_Ranks, MP2_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                               columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    MP2_Hand_rank_suit_df = MP2_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    MP2_Hand_df_sum = MP2_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    MP2_Hand_sorted_df_sum = MP2_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    MP2_Suit_Sum_index = []
    MP2_Suit_Sum_index.clear()
    n = 0
    while n < len(MP2_Hand_sorted_df_sum["Suit_Value"]):
        MP2_Suit_Sum_index.append(n)
        n += 1
    MP2_Hand_sorted_df_sum["index"] = MP2_Suit_Sum_index
    MP2_Hand_sorted_df_sum.set_index("index", inplace=True)
    MP2_Hand_Rank_Flush = []

    if MP2_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        MP2_Hand_Rank_Flush.clear()
        MP2_Hand_Rank_Flush.append(5)
        if MP2_card1[1] == MP2_Hand_df.at[0, 'Card_Suit']:
            MP2_Hand_Rank_Flush.append(MP2_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if MP2_card2[1] == MP2_Hand_df.at[0, 'Card_Suit']:
            MP2_Hand_Rank_Flush.append(MP2_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            MP2_Hand_Rank_Flush.append(0)
            MP2_Hand_Rank_Flush.append(0)
            MP2_Hand_Rank_Flush.append(0)
            MP2_Hand_Rank_Flush.append(0)
            MP2_Hand_Rank_Flush.append(0)

    Suit_for_straight = ""
    Suit_for_straight = str(MP2_Hand_sorted_df_sum.at[0, "Card_Suit"])

    MP2_Hand_Rank_sort = sorted(MP2_Hand_Rank)
    MP2_Hand = sorted(MP2_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    MP2_seen = set()
    uniq = []
    MP2_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    MP2_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    MP2_Hand_index = []
    for p in MP2_Hand:
        if p not in MP2_seen:
            MP2_seen[p] = 1

        else:

            MP2_seen[p] += 1

    while s < len(MP2_seen):
        MP2_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    MP2_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    # Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = MP2_seen.items()
    for item in items:
        MP2_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    MP2_Hand_dict = []
    MP2_Hand_dict_sortforpair = []
    MP2_Hand_dict_sortforstraight = []
    MP2_Hand_dict = pd.DataFrame(list(zip(MP2_Card_Rank_Hand, Num_of_Cards, MP2_Card_Suits)),
                                 columns=['a', 'b', 'c'])
    MP2_Hand_dict_straight = pd.DataFrame(list(zip(MP2_Card_Rank_Hand, Num_of_Cards, MP2_Card_Suits)),
                                          columns=['a', 'b', 'c'])
    MP2_Hand_dict_sortforpair = MP2_Hand_dict.sort_values(by=['b'], ascending=False)
    MP2_Hand_dict_sortforstraight = MP2_Hand_dict_straight.sort_values(by=['a'])
    MP2_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    MP2_Hand_Rank_straight = []
    MP2_Hand_Rank_straight.clear()
    MP2_Hand_Rank_straight_wheel = []
    MP2_Hand_Rank_straight_wheel.clear()
    MP2_Hand_Rank_straight_wheel_flush = []
    MP2_Hand_Rank_straight_wheel_flush.clear()
    MP2Hand_Rank_Royal_Flush = []
    MP2Hand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    MP2_Hand_Rank_straight_flush = []
    MP2_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(MP2_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if MP2_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if MP2_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    MP2_Hand_Rank_straight_wheel.clear()

                                    MP2_Hand_Rank_straight_wheel.append(12)
                                    MP2_Hand_Rank_straight_wheel.append(11)
                                    MP2_Hand_Rank_straight_wheel.append(10)
                                    MP2_Hand_Rank_straight_wheel.append(9)
                                    MP2_Hand_Rank_straight_wheel.append(0)

                                    if len(MP2_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            MP2_Hand_Rank_straight_wheel_flush.clear()

                                                            MP2_Hand_Rank_straight_wheel_flush.append(12)
                                                            MP2_Hand_Rank_straight_wheel_flush.append(11)
                                                            MP2_Hand_Rank_straight_wheel_flush.append(10)
                                                            MP2_Hand_Rank_straight_wheel_flush.append(9)
                                                            MP2_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(MP2_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP2_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if MP2_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        MP2_Hand_Rank_straight_wheel.clear()

                                        MP2_Hand_Rank_straight_wheel.append(12)
                                        MP2_Hand_Rank_straight_wheel.append(11)
                                        MP2_Hand_Rank_straight_wheel.append(10)
                                        MP2_Hand_Rank_straight_wheel.append(9)
                                        MP2_Hand_Rank_straight_wheel.append(0)

                                        if len(MP2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP2_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                MP2_Hand_Rank_straight_wheel_flush.clear()

                                                                MP2_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(MP2_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP2_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if MP2_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if MP2_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        MP2_Hand_Rank_straight_wheel.clear()

                                        MP2_Hand_Rank_straight_wheel.append(12)
                                        MP2_Hand_Rank_straight_wheel.append(11)
                                        MP2_Hand_Rank_straight_wheel.append(10)
                                        MP2_Hand_Rank_straight_wheel.append(9)
                                        MP2_Hand_Rank_straight_wheel.append(0)

                                        if len(MP2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP2_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                MP2_Hand_Rank_straight_wheel_flush.clear()

                                                                MP2_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP2_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(MP2_Hand_dict_sortforstraight) == 4:
                break
            if len(MP2_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(MP2_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP2_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if MP2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if MP2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    MP2_Hand_Rank_straight.clear()

                                    MP2_Hand_Rank_straight.append(q)
                                    MP2_Hand_Rank_straight.append(q + 1)
                                    MP2_Hand_Rank_straight.append(q + 2)
                                    MP2_Hand_Rank_straight.append(q + 3)
                                    MP2_Hand_Rank_straight.append(q + 4)

                                    if len(MP2_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                MP2_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            MP2_Hand_Rank_straight_flush.clear()

                                                            MP2_Hand_Rank_straight_flush.append(q)
                                                            MP2_Hand_Rank_straight_flush.append(q + 1)
                                                            MP2_Hand_Rank_straight_flush.append(q + 2)
                                                            MP2_Hand_Rank_straight_flush.append(q + 3)
                                                            MP2_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                MP2Hand_Rank_Royal_Flush.clear()
                                                                MP2Hand_Rank_Royal_Flush.append(0)
                                                                MP2Hand_Rank_Royal_Flush.append(1)
                                                                MP2Hand_Rank_Royal_Flush.append(2)
                                                                MP2Hand_Rank_Royal_Flush.append(3)
                                                                MP2Hand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(MP2_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP2_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP2_Hand_Rank_straight.clear()

                                        MP2_Hand_Rank_straight.append(q)
                                        MP2_Hand_Rank_straight.append(q + 1)
                                        MP2_Hand_Rank_straight.append(q + 2)
                                        MP2_Hand_Rank_straight.append(q + 3)
                                        MP2_Hand_Rank_straight.append(q + 4)

                                        if len(MP2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                MP2_Hand_Rank_straight_flush.clear()

                                                                MP2_Hand_Rank_straight_flush.append(q)
                                                                MP2_Hand_Rank_straight_flush.append(q + 1)
                                                                MP2_Hand_Rank_straight_flush.append(q + 2)
                                                                MP2_Hand_Rank_straight_flush.append(q + 3)
                                                                MP2_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MP2Hand_Rank_Royal_Flush.clear()
                                                                    MP2Hand_Rank_Royal_Flush.append(0)
                                                                    MP2Hand_Rank_Royal_Flush.append(1)
                                                                    MP2Hand_Rank_Royal_Flush.append(2)
                                                                    MP2Hand_Rank_Royal_Flush.append(3)
                                                                    MP2Hand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(MP2_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP2_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP2_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP2_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP2_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP2_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP2_Hand_Rank_straight.clear()

                                        MP2_Hand_Rank_straight.append(q)
                                        MP2_Hand_Rank_straight.append(q + 1)
                                        MP2_Hand_Rank_straight.append(q + 2)
                                        MP2_Hand_Rank_straight.append(q + 3)
                                        MP2_Hand_Rank_straight.append(q + 4)

                                        if len(MP2_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP2_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP2_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                MP2_Hand_Rank_straight_flush.clear()

                                                                MP2_Hand_Rank_straight_flush.append(q)
                                                                MP2_Hand_Rank_straight_flush.append(q + 1)
                                                                MP2_Hand_Rank_straight_flush.append(q + 2)
                                                                MP2_Hand_Rank_straight_flush.append(q + 3)
                                                                MP2_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MP2Hand_Rank_Royal_Flush.clear()
                                                                    MP2Hand_Rank_Royal_Flush.append(0)
                                                                    MP2Hand_Rank_Royal_Flush.append(1)
                                                                    MP2Hand_Rank_Royal_Flush.append(2)
                                                                    MP2Hand_Rank_Royal_Flush.append(3)
                                                                    MP2Hand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(MP2_Hand_dict_sortforstraight) == 4:
                break
            if len(MP2_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    MP2_Hand_dict_sortforpair["index"] = MP2_Hand_index
    MP2_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(10)
        MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
        MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])
        MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])
        MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
        MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[4, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP2_Hand_Rank.clear()
            MP2_Hand_Rank.append(9)
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[5, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[4, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP2_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP2_Hand_Rank.clear()
                MP2_Hand_Rank.append(8)
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP2_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP2_Hand_Rank.clear()
                MP2_Hand_Rank.append(8)
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[4, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP2_Hand_Rank.clear()
            MP2_Hand_Rank.append(7)
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[4, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if len(MP2_Hand_Rank_straight_wheel) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(6)
        MP2_Hand_Rank.append(9)
        MP2_Hand_Rank.append(10)
        MP2_Hand_Rank.append(11)
        MP2_Hand_Rank.append(12)
        MP2_Hand_Rank.append(13)

    if len(MP2_Hand_Rank_straight) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(6)
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight[0])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight[1])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight[2])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight[3])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight[4])

    if len(MP2_Hand_Rank_Flush) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(5)
        MP2_Hand_Rank.append(MP2_Hand_Rank_Flush[1])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP2_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP2_Hand_Rank.clear()
                MP2_Hand_Rank.append(4)
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP2_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP2_Hand_Rank.clear()
                MP2_Hand_Rank.append(4)
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 3:
            if MP2_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP2_Hand_Rank.clear()
                MP2_Hand_Rank.append(4)
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
                MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP2_Hand_Rank.clear()
            MP2_Hand_Rank.append(3)
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[3, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 2:
            MP2_Hand_Rank.clear()
            MP2_Hand_Rank.append(3)
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[2, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])

    if MP2_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP2_Hand_dict_sortforpair.at[1, "b"] == 3:
            MP2_Hand_Rank.clear()
            MP2_Hand_Rank.append(3)
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[0, "a"])
            MP2_Hand_Rank.append(MP2_Hand_dict_sortforpair.at[1, "a"])

    if len(MP2_Hand_Rank_straight_wheel_flush) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(2)
        MP2_Hand_Rank.append(9)
        MP2_Hand_Rank.append(10)
        MP2_Hand_Rank.append(11)
        MP2_Hand_Rank.append(12)
        MP2_Hand_Rank.append(13)

    if len(MP2_Hand_Rank_straight_flush) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(2)
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight_flush[0])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight_flush[1])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight_flush[2])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight_flush[3])
        MP2_Hand_Rank.append(MP2_Hand_Rank_straight_flush[4])

    if len(MP2Hand_Rank_Royal_Flush) >= 1:
        MP2_Hand_Rank.clear()
        MP2_Hand_Rank.append(1)
        MP2_Hand_Rank.append(MP2Hand_Rank_Royal_Flush[0])
        MP2_Hand_Rank.append(MP2Hand_Rank_Royal_Flush[1])
        MP2_Hand_Rank.append(MP2Hand_Rank_Royal_Flush[2])
        MP2_Hand_Rank.append(MP2Hand_Rank_Royal_Flush[3])
        MP2_Hand_Rank.append(MP2Hand_Rank_Royal_Flush[4])

    #######################################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []

    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    MP3_Card_Suits = []

    MP3_Hand_Rank = []
    Card_Suits_ = []
    MP3_card1_str = str(MP3_card1)
    MP3_card2_str = str(MP3_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    MP3_Card_Ranks = []

    MP3_Hand_Rank = []
    MP3_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == MP3_card1[1]:
            MP3_Hand_Suits.append(MP3_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == MP3_card2[1]:
            MP3_Hand_Suits.append(MP3_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP3_card1[0]:
            MP3_Hand_Rank.append(MP3_card1[0])
            MP3_Card_Ranks.append(y)
            MP3_Card_Suits.append(MP3_card1[1])

        if cards_value_df.at[y, "card_values"] == MP3_card2[0]:
            MP3_Hand_Rank.append(MP3_card2[0])
            MP3_Card_Ranks.append(y)
            MP3_Card_Suits.append(MP3_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            MP3_Card_Suits.append(Flop_card1[1])
            MP3_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            MP3_Card_Suits.append(Flop_card2[1])
            MP3_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            MP3_Card_Suits.append(Flop_card3[1])
            MP3_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            MP3_Card_Suits.append(Turn[1])
            MP3_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            MP3_Card_Suits.append(River[1])
            MP3_Card_Ranks.append(y)

        y += 1

    MP3_Hand_df = pd.DataFrame(list(zip(MP3_Card_Ranks, MP3_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                               columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    MP3_Hand_rank_suit_df = MP3_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    MP3_Hand_df_sum = MP3_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    MP3_Hand_sorted_df_sum = MP3_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    MP3_Suit_Sum_index = []
    MP3_Suit_Sum_index.clear()
    n = 0
    while n < len(MP3_Hand_sorted_df_sum["Suit_Value"]):
        MP3_Suit_Sum_index.append(n)
        n += 1
    MP3_Hand_sorted_df_sum["index"] = MP3_Suit_Sum_index
    MP3_Hand_sorted_df_sum.set_index("index", inplace=True)
    MP3_Hand_Rank_Flush = []

    if MP3_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        MP3_Hand_Rank_Flush.clear()
        MP3_Hand_Rank_Flush.append(5)
        if MP3_card1[1] == MP3_Hand_df.at[0, 'Card_Suit']:
            MP3_Hand_Rank_Flush.append(MP3_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if MP3_card2[1] == MP3_Hand_df.at[0, 'Card_Suit']:
            MP3_Hand_Rank_Flush.append(MP3_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            MP3_Hand_Rank_Flush.append(0)
            MP3_Hand_Rank_Flush.append(0)
            MP3_Hand_Rank_Flush.append(0)
            MP3_Hand_Rank_Flush.append(0)
            MP3_Hand_Rank_Flush.append(0)

    Suit_for_straight = ""
    Suit_for_straight = str(MP3_Hand_sorted_df_sum.at[0, "Card_Suit"])

    MP3_Hand_Rank_sort = sorted(MP3_Hand_Rank)
    MP3_Hand = sorted(MP3_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    MP3_seen = set()
    uniq = []
    MP3_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    MP3_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    MP3_Hand_index = []
    for p in MP3_Hand:
        if p not in MP3_seen:
            MP3_seen[p] = 1

        else:

            MP3_seen[p] += 1

    while s < len(MP3_seen):
        MP3_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    MP3_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    # Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = MP3_seen.items()
    for item in items:
        MP3_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    MP3_Hand_dict = []
    MP3_Hand_dict_sortforpair = []
    MP3_Hand_dict_sortforstraight = []
    MP3_Hand_dict = pd.DataFrame(list(zip(MP3_Card_Rank_Hand, Num_of_Cards, MP3_Card_Suits)),
                                 columns=['a', 'b', 'c'])
    MP3_Hand_dict_straight = pd.DataFrame(list(zip(MP3_Card_Rank_Hand, Num_of_Cards, MP3_Card_Suits)),
                                          columns=['a', 'b', 'c'])
    MP3_Hand_dict_sortforpair = MP3_Hand_dict.sort_values(by=['b'], ascending=False)
    MP3_Hand_dict_sortforstraight = MP3_Hand_dict_straight.sort_values(by=['a'])
    MP3_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    MP3_Hand_Rank_straight = []
    MP3_Hand_Rank_straight.clear()
    MP3_Hand_Rank_straight_wheel = []
    MP3_Hand_Rank_straight_wheel.clear()
    MP3_Hand_Rank_straight_wheel_flush = []
    MP3_Hand_Rank_straight_wheel_flush.clear()
    MP3Hand_Rank_Royal_Flush = []
    MP3Hand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    MP3_Hand_Rank_straight_flush = []
    MP3_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(MP3_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP3_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if MP3_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if MP3_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    MP3_Hand_Rank_straight_wheel.clear()

                                    MP3_Hand_Rank_straight_wheel.append(12)
                                    MP3_Hand_Rank_straight_wheel.append(11)
                                    MP3_Hand_Rank_straight_wheel.append(10)
                                    MP3_Hand_Rank_straight_wheel.append(9)
                                    MP3_Hand_Rank_straight_wheel.append(0)

                                    if len(MP3_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            MP3_Hand_Rank_straight_wheel_flush.clear()

                                                            MP3_Hand_Rank_straight_wheel_flush.append(12)
                                                            MP3_Hand_Rank_straight_wheel_flush.append(11)
                                                            MP3_Hand_Rank_straight_wheel_flush.append(10)
                                                            MP3_Hand_Rank_straight_wheel_flush.append(9)
                                                            MP3_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(MP3_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP3_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP3_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if MP3_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        MP3_Hand_Rank_straight_wheel.clear()

                                        MP3_Hand_Rank_straight_wheel.append(12)
                                        MP3_Hand_Rank_straight_wheel.append(11)
                                        MP3_Hand_Rank_straight_wheel.append(10)
                                        MP3_Hand_Rank_straight_wheel.append(9)
                                        MP3_Hand_Rank_straight_wheel.append(0)

                                        if len(MP3_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP3_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                MP3_Hand_Rank_straight_wheel_flush.clear()

                                                                MP3_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(MP3_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP3_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if MP3_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if MP3_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        MP3_Hand_Rank_straight_wheel.clear()

                                        MP3_Hand_Rank_straight_wheel.append(12)
                                        MP3_Hand_Rank_straight_wheel.append(11)
                                        MP3_Hand_Rank_straight_wheel.append(10)
                                        MP3_Hand_Rank_straight_wheel.append(9)
                                        MP3_Hand_Rank_straight_wheel.append(0)

                                        if len(MP3_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP3_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                MP3_Hand_Rank_straight_wheel_flush.clear()

                                                                MP3_Hand_Rank_straight_wheel_flush.append(12)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(11)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(10)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(9)
                                                                MP3_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(MP3_Hand_dict_sortforstraight) == 4:
                break
            if len(MP3_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(MP3_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if MP3_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if MP3_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if MP3_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    MP3_Hand_Rank_straight.clear()

                                    MP3_Hand_Rank_straight.append(q)
                                    MP3_Hand_Rank_straight.append(q + 1)
                                    MP3_Hand_Rank_straight.append(q + 2)
                                    MP3_Hand_Rank_straight.append(q + 3)
                                    MP3_Hand_Rank_straight.append(q + 4)

                                    if len(MP3_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                MP3_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            MP3_Hand_Rank_straight_flush.clear()

                                                            MP3_Hand_Rank_straight_flush.append(q)
                                                            MP3_Hand_Rank_straight_flush.append(q + 1)
                                                            MP3_Hand_Rank_straight_flush.append(q + 2)
                                                            MP3_Hand_Rank_straight_flush.append(q + 3)
                                                            MP3_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                MP3Hand_Rank_Royal_Flush.clear()
                                                                MP3Hand_Rank_Royal_Flush.append(0)
                                                                MP3Hand_Rank_Royal_Flush.append(1)
                                                                MP3Hand_Rank_Royal_Flush.append(2)
                                                                MP3Hand_Rank_Royal_Flush.append(3)
                                                                MP3Hand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(MP3_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if MP3_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP3_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP3_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP3_Hand_Rank_straight.clear()

                                        MP3_Hand_Rank_straight.append(q)
                                        MP3_Hand_Rank_straight.append(q + 1)
                                        MP3_Hand_Rank_straight.append(q + 2)
                                        MP3_Hand_Rank_straight.append(q + 3)
                                        MP3_Hand_Rank_straight.append(q + 4)

                                        if len(MP3_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                MP3_Hand_Rank_straight_flush.clear()

                                                                MP3_Hand_Rank_straight_flush.append(q)
                                                                MP3_Hand_Rank_straight_flush.append(q + 1)
                                                                MP3_Hand_Rank_straight_flush.append(q + 2)
                                                                MP3_Hand_Rank_straight_flush.append(q + 3)
                                                                MP3_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MP3Hand_Rank_Royal_Flush.clear()
                                                                    MP3Hand_Rank_Royal_Flush.append(0)
                                                                    MP3Hand_Rank_Royal_Flush.append(1)
                                                                    MP3Hand_Rank_Royal_Flush.append(2)
                                                                    MP3Hand_Rank_Royal_Flush.append(3)
                                                                    MP3Hand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(MP3_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if MP3_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if MP3_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if MP3_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if MP3_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if MP3_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        MP3_Hand_Rank_straight.clear()

                                        MP3_Hand_Rank_straight.append(q)
                                        MP3_Hand_Rank_straight.append(q + 1)
                                        MP3_Hand_Rank_straight.append(q + 2)
                                        MP3_Hand_Rank_straight.append(q + 3)
                                        MP3_Hand_Rank_straight.append(q + 4)

                                        if len(MP3_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == MP3_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    MP3_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                MP3_Hand_Rank_straight_flush.clear()

                                                                MP3_Hand_Rank_straight_flush.append(q)
                                                                MP3_Hand_Rank_straight_flush.append(q + 1)
                                                                MP3_Hand_Rank_straight_flush.append(q + 2)
                                                                MP3_Hand_Rank_straight_flush.append(q + 3)
                                                                MP3_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    MP3Hand_Rank_Royal_Flush.clear()
                                                                    MP3Hand_Rank_Royal_Flush.append(0)
                                                                    MP3Hand_Rank_Royal_Flush.append(1)
                                                                    MP3Hand_Rank_Royal_Flush.append(2)
                                                                    MP3Hand_Rank_Royal_Flush.append(3)
                                                                    MP3Hand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(MP3_Hand_dict_sortforstraight) == 4:
                break
            if len(MP3_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    MP3_Hand_dict_sortforpair["index"] = MP3_Hand_index
    MP3_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(10)
        MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
        MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])
        MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])
        MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
        MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[4, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP3_Hand_Rank.clear()
            MP3_Hand_Rank.append(9)
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[5, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[4, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP3_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP3_Hand_Rank.clear()
                MP3_Hand_Rank.append(8)
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 2:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP3_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP3_Hand_Rank.clear()
                MP3_Hand_Rank.append(8)
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[4, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP3_Hand_Rank.clear()
            MP3_Hand_Rank.append(7)
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[4, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if len(MP3_Hand_Rank_straight_wheel) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(6)
        MP3_Hand_Rank.append(9)
        MP3_Hand_Rank.append(10)
        MP3_Hand_Rank.append(11)
        MP3_Hand_Rank.append(12)
        MP3_Hand_Rank.append(13)

    if len(MP3_Hand_Rank_straight) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(6)
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight[0])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight[1])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight[2])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight[3])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight[4])

    if len(MP3_Hand_Rank_Flush) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(5)
        MP3_Hand_Rank.append(MP3_Hand_Rank_Flush[1])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP3_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP3_Hand_Rank.clear()
                MP3_Hand_Rank.append(4)
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 2:
            if MP3_Hand_dict_sortforpair.at[2, "b"] == 2:
                MP3_Hand_Rank.clear()
                MP3_Hand_Rank.append(4)
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 3:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 3:
            if MP3_Hand_dict_sortforpair.at[2, "b"] == 1:
                MP3_Hand_Rank.clear()
                MP3_Hand_Rank.append(4)
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
                MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 1:
            MP3_Hand_Rank.clear()
            MP3_Hand_Rank.append(3)
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[3, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 2:
            MP3_Hand_Rank.clear()
            MP3_Hand_Rank.append(3)
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[2, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])

    if MP3_Hand_dict_sortforpair.at[0, "b"] == 4:
        if MP3_Hand_dict_sortforpair.at[1, "b"] == 3:
            MP3_Hand_Rank.clear()
            MP3_Hand_Rank.append(3)
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[0, "a"])
            MP3_Hand_Rank.append(MP3_Hand_dict_sortforpair.at[1, "a"])

    if len(MP3_Hand_Rank_straight_wheel_flush) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(2)
        MP3_Hand_Rank.append(9)
        MP3_Hand_Rank.append(10)
        MP3_Hand_Rank.append(11)
        MP3_Hand_Rank.append(12)
        MP3_Hand_Rank.append(13)

    if len(MP3_Hand_Rank_straight_flush) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(2)
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight_flush[0])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight_flush[1])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight_flush[2])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight_flush[3])
        MP3_Hand_Rank.append(MP3_Hand_Rank_straight_flush[4])

    if len(MP3Hand_Rank_Royal_Flush) >= 1:
        MP3_Hand_Rank.clear()
        MP3_Hand_Rank.append(1)
        MP3_Hand_Rank.append(MP3Hand_Rank_Royal_Flush[0])
        MP3_Hand_Rank.append(MP3Hand_Rank_Royal_Flush[1])
        MP3_Hand_Rank.append(MP3Hand_Rank_Royal_Flush[2])
        MP3_Hand_Rank.append(MP3Hand_Rank_Royal_Flush[3])
        MP3_Hand_Rank.append(MP3Hand_Rank_Royal_Flush[4])
    ##################################################################################################################################################

    x = 0
    y = 0
    index = []
    suit_index = []

    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    HJ_Card_Suits = []

    HJ_Hand_Rank = []
    Card_Suits_ = []
    HJ_card1_str = str(HJ_card1)
    HJ_card2_str = str(HJ_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    HJ_Card_Ranks = []

    HJ_Hand_Rank = []
    HJ_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == HJ_card1[1]:
            HJ_Hand_Suits.append(HJ_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == HJ_card2[1]:
            HJ_Hand_Suits.append(HJ_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == HJ_card1[0]:
            HJ_Hand_Rank.append(HJ_card1[0])
            HJ_Card_Ranks.append(y)
            HJ_Card_Suits.append(HJ_card1[1])

        if cards_value_df.at[y, "card_values"] == HJ_card2[0]:
            HJ_Hand_Rank.append(HJ_card2[0])
            HJ_Card_Ranks.append(y)
            HJ_Card_Suits.append(HJ_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            HJ_Card_Suits.append(Flop_card1[1])
            HJ_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            HJ_Card_Suits.append(Flop_card2[1])
            HJ_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            HJ_Card_Suits.append(Flop_card3[1])
            HJ_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            HJ_Card_Suits.append(Turn[1])
            HJ_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            HJ_Card_Suits.append(River[1])
            HJ_Card_Ranks.append(y)

        y += 1

    HJ_Hand_df = pd.DataFrame(list(zip(HJ_Card_Ranks, HJ_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                              columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    HJ_Hand_rank_suit_df = HJ_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    HJ_Hand_df_sum = HJ_Hand_df.groupby(['Card_Suit'], as_index=False).sum()[
        ['Suit_Value', 'Card_Rank', 'Card_Suit']]
    HJ_Hand_sorted_df_sum = HJ_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)
    HJ_Suit_Sum_index = []
    HJ_Suit_Sum_index.clear()
    n = 0
    while n < len(HJ_Hand_sorted_df_sum["Suit_Value"]):
        HJ_Suit_Sum_index.append(n)
        n += 1
    HJ_Hand_sorted_df_sum["index"] = HJ_Suit_Sum_index
    HJ_Hand_sorted_df_sum.set_index("index", inplace=True)
    HJ_Hand_Rank_Flush = []

    if HJ_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        HJ_Hand_Rank_Flush.clear()
        HJ_Hand_Rank_Flush.append(5)
        if HJ_card1[1] == HJ_Hand_df.at[0, 'Card_Suit']:
            HJ_Hand_Rank_Flush.append(HJ_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        if HJ_card2[1] == HJ_Hand_df.at[0, 'Card_Suit']:
            HJ_Hand_Rank_Flush.append(HJ_Hand_sorted_df_sum.at[0, 'Card_Rank'])

        else:
            HJ_Hand_Rank_Flush.append(0)
            HJ_Hand_Rank_Flush.append(0)
            HJ_Hand_Rank_Flush.append(0)
            HJ_Hand_Rank_Flush.append(0)
            HJ_Hand_Rank_Flush.append(0)

    Suit_for_straight = ""
    Suit_for_straight = str(HJ_Hand_sorted_df_sum.at[0, "Card_Suit"])

    HJ_Hand_Rank_sort = sorted(HJ_Hand_Rank)
    HJ_Hand = sorted(HJ_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    HJ_seen = set()
    uniq = []
    HJ_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    HJ_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    HJ_Hand_index = []
    for p in HJ_Hand:
        if p not in HJ_seen:
            HJ_seen[p] = 1

        else:

            HJ_seen[p] += 1

    while s < len(HJ_seen):
        HJ_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    HJ_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    # Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = HJ_seen.items()
    for item in items:
        HJ_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    HJ_Hand_dict = []
    HJ_Hand_dict_sortforpair = []
    HJ_Hand_dict_sortforstraight = []
    HJ_Hand_dict = pd.DataFrame(list(zip(HJ_Card_Rank_Hand, Num_of_Cards, HJ_Card_Suits)),
                                columns=['a', 'b', 'c'])
    HJ_Hand_dict_straight = pd.DataFrame(list(zip(HJ_Card_Rank_Hand, Num_of_Cards, HJ_Card_Suits)),
                                         columns=['a', 'b', 'c'])
    HJ_Hand_dict_sortforpair = HJ_Hand_dict.sort_values(by=['b'], ascending=False)
    HJ_Hand_dict_sortforstraight = HJ_Hand_dict_straight.sort_values(by=['a'])
    HJ_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    HJ_Hand_Rank_straight = []
    HJ_Hand_Rank_straight.clear()
    HJ_Hand_Rank_straight_wheel = []
    HJ_Hand_Rank_straight_wheel.clear()
    HJ_Hand_Rank_straight_wheel_flush = []
    HJ_Hand_Rank_straight_wheel_flush.clear()
    HJHand_Rank_Royal_Flush = []
    HJHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    HJ_Hand_Rank_straight_flush = []
    HJ_Hand_Rank_straight_flush.clear()

    while q < 9:

        if len(HJ_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if HJ_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if HJ_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if HJ_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    HJ_Hand_Rank_straight_wheel.clear()

                                    HJ_Hand_Rank_straight_wheel.append(12)
                                    HJ_Hand_Rank_straight_wheel.append(11)
                                    HJ_Hand_Rank_straight_wheel.append(10)
                                    HJ_Hand_Rank_straight_wheel.append(9)
                                    HJ_Hand_Rank_straight_wheel.append(0)

                                    if len(HJ_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            HJ_Hand_Rank_straight_wheel_flush.clear()

                                                            HJ_Hand_Rank_straight_wheel_flush.append(12)
                                                            HJ_Hand_Rank_straight_wheel_flush.append(11)
                                                            HJ_Hand_Rank_straight_wheel_flush.append(10)
                                                            HJ_Hand_Rank_straight_wheel_flush.append(9)
                                                            HJ_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break

                v += 1

            if len(HJ_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if HJ_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if HJ_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if HJ_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        HJ_Hand_Rank_straight_wheel.clear()

                                        HJ_Hand_Rank_straight_wheel.append(12)
                                        HJ_Hand_Rank_straight_wheel.append(11)
                                        HJ_Hand_Rank_straight_wheel.append(10)
                                        HJ_Hand_Rank_straight_wheel.append(9)
                                        HJ_Hand_Rank_straight_wheel.append(0)

                                        if len(HJ_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    HJ_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                HJ_Hand_Rank_straight_wheel_flush.clear()

                                                                HJ_Hand_Rank_straight_wheel_flush.append(12)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(11)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(10)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(9)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(HJ_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if HJ_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if HJ_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if HJ_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        HJ_Hand_Rank_straight_wheel.clear()

                                        HJ_Hand_Rank_straight_wheel.append(12)
                                        HJ_Hand_Rank_straight_wheel.append(11)
                                        HJ_Hand_Rank_straight_wheel.append(10)
                                        HJ_Hand_Rank_straight_wheel.append(9)
                                        HJ_Hand_Rank_straight_wheel.append(0)

                                        if len(HJ_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    HJ_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                HJ_Hand_Rank_straight_wheel_flush.clear()

                                                                HJ_Hand_Rank_straight_wheel_flush.append(12)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(11)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(10)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(9)
                                                                HJ_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(HJ_Hand_dict_sortforstraight) == 4:
                break
            if len(HJ_Hand_dict_sortforstraight) == 3:
                break

        q += 1
    q = 0

    f = 0
    q = 0
    v = 0

    while q < 9:

        if len(HJ_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if HJ_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if HJ_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if HJ_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    HJ_Hand_Rank_straight.clear()

                                    HJ_Hand_Rank_straight.append(q)
                                    HJ_Hand_Rank_straight.append(q + 1)
                                    HJ_Hand_Rank_straight.append(q + 2)
                                    HJ_Hand_Rank_straight.append(q + 3)
                                    HJ_Hand_Rank_straight.append(q + 4)

                                    if len(HJ_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                HJ_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            HJ_Hand_Rank_straight_flush.clear()

                                                            HJ_Hand_Rank_straight_flush.append(q)
                                                            HJ_Hand_Rank_straight_flush.append(q + 1)
                                                            HJ_Hand_Rank_straight_flush.append(q + 2)
                                                            HJ_Hand_Rank_straight_flush.append(q + 3)
                                                            HJ_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                HJHand_Rank_Royal_Flush.clear()
                                                                HJHand_Rank_Royal_Flush.append(0)
                                                                HJHand_Rank_Royal_Flush.append(1)
                                                                HJHand_Rank_Royal_Flush.append(2)
                                                                HJHand_Rank_Royal_Flush.append(3)
                                                                HJHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break

                v += 1
            q += 1

            if len(HJ_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if HJ_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if HJ_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if HJ_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        HJ_Hand_Rank_straight.clear()

                                        HJ_Hand_Rank_straight.append(q)
                                        HJ_Hand_Rank_straight.append(q + 1)
                                        HJ_Hand_Rank_straight.append(q + 2)
                                        HJ_Hand_Rank_straight.append(q + 3)
                                        HJ_Hand_Rank_straight.append(q + 4)

                                        if len(HJ_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                HJ_Hand_Rank_straight_flush.clear()

                                                                HJ_Hand_Rank_straight_flush.append(q)
                                                                HJ_Hand_Rank_straight_flush.append(q + 1)
                                                                HJ_Hand_Rank_straight_flush.append(q + 2)
                                                                HJ_Hand_Rank_straight_flush.append(q + 3)
                                                                HJ_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    HJHand_Rank_Royal_Flush.clear()
                                                                    HJHand_Rank_Royal_Flush.append(0)
                                                                    HJHand_Rank_Royal_Flush.append(1)
                                                                    HJHand_Rank_Royal_Flush.append(2)
                                                                    HJHand_Rank_Royal_Flush.append(3)
                                                                    HJHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break

                    v += 1

            if len(HJ_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if HJ_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if HJ_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if HJ_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if HJ_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if HJ_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        HJ_Hand_Rank_straight.clear()

                                        HJ_Hand_Rank_straight.append(q)
                                        HJ_Hand_Rank_straight.append(q + 1)
                                        HJ_Hand_Rank_straight.append(q + 2)
                                        HJ_Hand_Rank_straight.append(q + 3)
                                        HJ_Hand_Rank_straight.append(q + 4)

                                        if len(HJ_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == HJ_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    HJ_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                HJ_Hand_Rank_straight_flush.clear()

                                                                HJ_Hand_Rank_straight_flush.append(q)
                                                                HJ_Hand_Rank_straight_flush.append(q + 1)
                                                                HJ_Hand_Rank_straight_flush.append(q + 2)
                                                                HJ_Hand_Rank_straight_flush.append(q + 3)
                                                                HJ_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    HJHand_Rank_Royal_Flush.clear()
                                                                    HJHand_Rank_Royal_Flush.append(0)
                                                                    HJHand_Rank_Royal_Flush.append(1)
                                                                    HJHand_Rank_Royal_Flush.append(2)
                                                                    HJHand_Rank_Royal_Flush.append(3)
                                                                    HJHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(HJ_Hand_dict_sortforstraight) == 4:
                break
            if len(HJ_Hand_dict_sortforstraight) == 3:
                break

        q += 1

    HJ_Hand_dict_sortforpair["index"] = HJ_Hand_index
    HJ_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(10)
        HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
        HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])
        HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])
        HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
        HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[4, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 2:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 1:
            HJ_Hand_Rank.clear()
            HJ_Hand_Rank.append(9)
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[5, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[4, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 2:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 2:
            if HJ_Hand_dict_sortforpair.at[2, "b"] == 2:
                HJ_Hand_Rank.clear()
                HJ_Hand_Rank.append(8)
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 2:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 2:
            if HJ_Hand_dict_sortforpair.at[2, "b"] == 1:
                HJ_Hand_Rank.clear()
                HJ_Hand_Rank.append(8)
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[4, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 3:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 1:
            HJ_Hand_Rank.clear()
            HJ_Hand_Rank.append(7)
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[4, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if len(HJ_Hand_Rank_straight_wheel) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(6)
        HJ_Hand_Rank.append(9)
        HJ_Hand_Rank.append(10)
        HJ_Hand_Rank.append(11)
        HJ_Hand_Rank.append(12)
        HJ_Hand_Rank.append(13)

    if len(HJ_Hand_Rank_straight) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(6)
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight[0])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight[1])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight[2])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight[3])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight[4])

    if len(HJ_Hand_Rank_Flush) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(5)
        HJ_Hand_Rank.append(HJ_Hand_Rank_Flush[1])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 3:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 2:
            if HJ_Hand_dict_sortforpair.at[2, "b"] == 1:
                HJ_Hand_Rank.clear()
                HJ_Hand_Rank.append(4)
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 3:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 2:
            if HJ_Hand_dict_sortforpair.at[2, "b"] == 2:
                HJ_Hand_Rank.clear()
                HJ_Hand_Rank.append(4)
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 3:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 3:
            if HJ_Hand_dict_sortforpair.at[2, "b"] == 1:
                HJ_Hand_Rank.clear()
                HJ_Hand_Rank.append(4)
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
                HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 4:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 1:
            HJ_Hand_Rank.clear()
            HJ_Hand_Rank.append(3)
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[3, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 4:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 2:
            HJ_Hand_Rank.clear()
            HJ_Hand_Rank.append(3)
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[2, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])

    if HJ_Hand_dict_sortforpair.at[0, "b"] == 4:
        if HJ_Hand_dict_sortforpair.at[1, "b"] == 3:
            HJ_Hand_Rank.clear()
            HJ_Hand_Rank.append(3)
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[0, "a"])
            HJ_Hand_Rank.append(HJ_Hand_dict_sortforpair.at[1, "a"])

    if len(HJ_Hand_Rank_straight_wheel_flush) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(2)
        HJ_Hand_Rank.append(9)
        HJ_Hand_Rank.append(10)
        HJ_Hand_Rank.append(11)
        HJ_Hand_Rank.append(12)
        HJ_Hand_Rank.append(13)

    if len(HJ_Hand_Rank_straight_flush) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(2)
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight_flush[0])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight_flush[1])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight_flush[2])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight_flush[3])
        HJ_Hand_Rank.append(HJ_Hand_Rank_straight_flush[4])

    if len(HJHand_Rank_Royal_Flush) >= 1:
        HJ_Hand_Rank.clear()
        HJ_Hand_Rank.append(1)
        HJ_Hand_Rank.append(HJHand_Rank_Royal_Flush[0])
        HJ_Hand_Rank.append(HJHand_Rank_Royal_Flush[1])
        HJ_Hand_Rank.append(HJHand_Rank_Royal_Flush[2])
        HJ_Hand_Rank.append(HJHand_Rank_Royal_Flush[3])
        HJ_Hand_Rank.append(HJHand_Rank_Royal_Flush[4])

    ###########################################################################################################################################

    if Button_card1[1] == Button_card2[1]:
        hero_SO = 's'
    elif Button_card1[0] == Button_card2[0]:
        hero_SO = ''
    else:
        hero_SO = 'o'

    y = 0
    while y < 13:

        if cards_value_df.at[y, "card_values"] == Button_card1[0]:
            hero_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == Button_card2[0]:
            hero_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1
    y = 0

    hero_hand_val.append(hero_SO)

    rel_hero_hand = ''.join([str(elem) for elem in hero_hand_val])

    print("hero:", rel_hero_hand)

    Hero_Rank = Hero_Hand_Rank

    Hero_Rank_card = ()

    if Hero_Rank[0] == 10:
        Hero_Rank_card = "High Card"
    if Hero_Rank[0] == 9:
        Hero_Rank_card = "Pair"
    if Hero_Rank[0] == 8:
        Hero_Rank_card = "Two Pair"
    if Hero_Rank[0] == 7:
        Hero_Rank_card = "Three of a Kind"
    if Hero_Rank[0] == 6:
        Hero_Rank_card = "Straight"
    if Hero_Rank[0] == 5:
        Hero_Rank_card = "Flush"
    if Hero_Rank[0] == 4:
        Hero_Rank_card = "Full House"
    if Hero_Rank[0] == 3:
        Hero_Rank_card = "Four of a Kind"
    if Hero_Rank[0] == 2:
        Hero_Rank_card = "Straight Flush"
    if Hero_Rank[0] == 1:
        Hero_Rank_card = "Royal Flush"

    ############################################################################################################################################
    if small_blind_card1[1] == small_blind_card2[1]:
        villain_SO = 's'
    elif small_blind_card1[0] == small_blind_card2[0]:
        villain_SO = ''
    else:
        villain_SO = 'o'

    y = 0

    villain_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == small_blind_card1[0]:
            villain_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == small_blind_card2[0]:
            villain_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    villain_hand_val.append(villain_SO)

    rel_villain_hand = ''.join([str(elem) for elem in villain_hand_val])

    print("villain: ", rel_villain_hand)

    Villain_Rank = Villain_Hand_Rank

    Villain_Rank_card = ()

    if Villain_Rank[0] == 10:
        Villain_Rank_card = "High Card"
    if Villain_Rank[0] == 9:
        Villain_Rank_card = "Pair"
    if Villain_Rank[0] == 8:
        Villain_Rank_card = "Two Pair"
    if Villain_Rank[0] == 7:
        Villain_Rank_card = "Three of a Kind"
    if Villain_Rank[0] == 6:
        Villain_Rank_card = "Straight"
    if Villain_Rank[0] == 5:
        Villain_Rank_card = "Flush"
    if Villain_Rank[0] == 4:
        Villain_Rank_card = "Full House"
    if Villain_Rank[0] == 3:
        Villain_Rank_card = "Four of a Kind"
    if Villain_Rank[0] == 2:
        Villain_Rank_card = "Straight Flush"
    if Villain_Rank[0] == 1:
        Villain_Rank_card = "Royal Flush"

    #################################################################################################################################################

    if big_blind_card1[1] == big_blind_card2[1]:
        BB_SO = 's'
    elif big_blind_card1[0] == big_blind_card2[0]:
        BB_SO = ''
    else:
        BB_SO = 'o'

    y = 0

    BB_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == big_blind_card1[0]:
            BB_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == big_blind_card2[0]:
            BB_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    BB_hand_val.append(BB_SO)

    rel_BB_hand = ''.join([str(elem) for elem in BB_hand_val])

    print("Big Blind: ", rel_BB_hand)

    BB_Rank = BB_Hand_Rank

    BB_Rank_card = ()

    if BB_Rank[0] == 10:
        BB_Rank_card = "High Card"
    if BB_Rank[0] == 9:
        BB_Rank_card = "Pair"
    if BB_Rank[0] == 8:
        BB_Rank_card = "Two Pair"
    if BB_Rank[0] == 7:
        BB_Rank_card = "Three of a Kind"
    if BB_Rank[0] == 6:
        BB_Rank_card = "Straight"
    if BB_Rank[0] == 5:
        BB_Rank_card = "Flush"
    if BB_Rank[0] == 4:
        BB_Rank_card = "Full House"
    if BB_Rank[0] == 3:
        BB_Rank_card = "Four of a Kind"
    if BB_Rank[0] == 2:
        BB_Rank_card = "Straight Flush"
    if BB_Rank[0] == 1:
        BB_Rank_card = "Royal Flush"

    #################################################################################################################################################

    if UTG_card1[1] == UTG_card2[1]:
        UTG_SO = 's'
    elif UTG_card1[0] == UTG_card2[0]:
        UTG_SO = ''
    else:
        UTG_SO = 'o'

    y = 0

    UTG_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == UTG_card1[0]:
            UTG_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == UTG_card2[0]:
            UTG_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    UTG_hand_val.append(UTG_SO)

    rel_UTG_hand = ''.join([str(elem) for elem in UTG_hand_val])

    print("Under The Gun: ", rel_UTG_hand)

    UTG_Rank = UTG_Hand_Rank

    UTG_Rank_card = ()

    if UTG_Rank[0] == 10:
        UTG_Rank_card = "High Card"
    if UTG_Rank[0] == 9:
        UTG_Rank_card = "Pair"
    if UTG_Rank[0] == 8:
        UTG_Rank_card = "Two Pair"
    if UTG_Rank[0] == 7:
        UTG_Rank_card = "Three of a Kind"
    if UTG_Rank[0] == 6:
        UTG_Rank_card = "Straight"
    if UTG_Rank[0] == 5:
        UTG_Rank_card = "Flush"
    if UTG_Rank[0] == 4:
        UTG_Rank_card = "Full House"
    if UTG_Rank[0] == 3:
        UTG_Rank_card = "Four of a Kind"
    if UTG_Rank[0] == 2:
        UTG_Rank_card = "Straight Flush"
    if UTG_Rank[0] == 1:
        UTG_Rank_card = "Royal Flush"

    #############################################################################################################################################

    if UTG2_card1[1] == UTG2_card2[1]:
        UTG2_SO = 's'
    elif UTG2_card1[0] == UTG2_card2[0]:
        UTG2_SO = ''
    else:
        UTG2_SO = 'o'

    y = 0

    UTG2_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == UTG2_card1[0]:
            UTG2_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == UTG2_card2[0]:
            UTG2_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    UTG2_hand_val.append(UTG2_SO)

    rel_UTG2_hand = ''.join([str(elem) for elem in UTG2_hand_val])

    print("Under The Gun #2: ", rel_UTG2_hand)

    UTG2_Rank = UTG2_Hand_Rank

    UTG2_Rank_card = ()

    if UTG2_Rank[0] == 10:
        UTG2_Rank_card = "High Card"
    if UTG2_Rank[0] == 9:
        UTG2_Rank_card = "Pair"
    if UTG2_Rank[0] == 8:
        UTG2_Rank_card = "Two Pair"
    if UTG2_Rank[0] == 7:
        UTG2_Rank_card = "Three of a Kind"
    if UTG2_Rank[0] == 6:
        UTG2_Rank_card = "Straight"
    if UTG2_Rank[0] == 5:
        UTG2_Rank_card = "Flush"
    if UTG2_Rank[0] == 4:
        UTG2_Rank_card = "Full House"
    if UTG2_Rank[0] == 3:
        UTG2_Rank_card = "Four of a Kind"
    if UTG2_Rank[0] == 2:
        UTG2_Rank_card = "Straight Flush"
    if UTG2_Rank[0] == 1:
        UTG2_Rank_card = "Royal Flush"

    ###########################################################################################################################################

    if MP_card1[1] == MP_card2[1]:
        MP_SO = 's'
    elif MP_card1[0] == MP_card2[0]:
        MP_SO = ''
    else:
        MP_SO = 'o'

    y = 0

    MP_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP_card1[0]:
            MP_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == MP_card2[0]:
            MP_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    MP_hand_val.append(MP_SO)

    rel_MP_hand = ''.join([str(elem) for elem in MP_hand_val])

    print("Mid Position: ", rel_MP_hand)

    MP_Rank = MP_Hand_Rank

    MP_Rank_card = ()

    if MP_Rank[0] == 10:
        MP_Rank_card = "High Card"
    if MP_Rank[0] == 9:
        MP_Rank_card = "Pair"
    if MP_Rank[0] == 8:
        MP_Rank_card = "Two Pair"
    if MP_Rank[0] == 7:
        MP_Rank_card = "Three of a Kind"
    if MP_Rank[0] == 6:
        MP_Rank_card = "Straight"
    if MP_Rank[0] == 5:
        MP_Rank_card = "Flush"
    if MP_Rank[0] == 4:
        MP_Rank_card = "Full House"
    if MP_Rank[0] == 3:
        MP_Rank_card = "Four of a Kind"
    if MP_Rank[0] == 2:
        MP_Rank_card = "Straight Flush"
    if MP_Rank[0] == 1:
        MP_Rank_card = "Royal Flush"

    #############################################################################################################################################

    if MP2_card1[1] == MP2_card2[1]:
        MP2_SO = 's'
    elif MP2_card1[0] == MP2_card2[0]:
        MP2_SO = ''
    else:
        MP2_SO = 'o'

    y = 0

    MP2_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP2_card1[0]:
            MP2_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == MP2_card2[0]:
            MP2_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    MP2_hand_val.append(MP2_SO)

    rel_MP2_hand = ''.join([str(elem) for elem in MP2_hand_val])

    print("Mid Position2: ", rel_MP2_hand)

    MP2_Rank = MP2_Hand_Rank

    MP2_Rank_card = ()

    if MP2_Rank[0] == 10:
        MP2_Rank_card = "High Card"
    if MP2_Rank[0] == 9:
        MP2_Rank_card = "Pair"
    if MP2_Rank[0] == 8:
        MP2_Rank_card = "Two Pair"
    if MP2_Rank[0] == 7:
        MP2_Rank_card = "Three of a Kind"
    if MP2_Rank[0] == 6:
        MP2_Rank_card = "Straight"
    if MP2_Rank[0] == 5:
        MP2_Rank_card = "Flush"
    if MP2_Rank[0] == 4:
        MP2_Rank_card = "Full House"
    if MP2_Rank[0] == 3:
        MP2_Rank_card = "Four of a Kind"
    if MP2_Rank[0] == 2:
        MP2_Rank_card = "Straight Flush"
    if MP2_Rank[0] == 1:
        MP2_Rank_card = "Royal Flush"

    ###############################################################################################################################################

    if MP3_card1[1] == MP3_card2[1]:
        MP3_SO = 's'
    elif MP3_card1[0] == MP3_card2[0]:
        MP3_SO = ''
    else:
        MP3_SO = 'o'

    y = 0

    MP3_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == MP3_card1[0]:
            MP3_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == MP3_card2[0]:
            MP3_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    MP3_hand_val.append(MP3_SO)

    rel_MP3_hand = ''.join([str(elem) for elem in MP3_hand_val])

    print("Mid Position: ", rel_MP3_hand)

    MP3_Rank = MP3_Hand_Rank

    MP3_Rank_card = ()

    if MP3_Rank[0] == 10:
        MP3_Rank_card = "High Card"
    if MP3_Rank[0] == 9:
        MP3_Rank_card = "Pair"
    if MP3_Rank[0] == 8:
        MP3_Rank_card = "Two Pair"
    if MP3_Rank[0] == 7:
        MP3_Rank_card = "Three of a Kind"
    if MP3_Rank[0] == 6:
        MP3_Rank_card = "Straight"
    if MP3_Rank[0] == 5:
        MP3_Rank_card = "Flush"
    if MP3_Rank[0] == 4:
        MP3_Rank_card = "Full House"
    if MP3_Rank[0] == 3:
        MP3_Rank_card = "Four of a Kind"
    if MP3_Rank[0] == 2:
        MP3_Rank_card = "Straight Flush"
    if MP3_Rank[0] == 1:
        MP3_Rank_card = "Royal Flush"

    ##############################################################################################################################################

    if HJ_card1[1] == HJ_card2[1]:
        HJ_SO = 's'
    elif HJ_card1[0] == HJ_card2[0]:
        HJ_SO = ''
    else:
        HJ_SO = 'o'

    y = 0

    HJ_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == HJ_card1[0]:
            HJ_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == HJ_card2[0]:
            HJ_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1

    y = 0

    HJ_hand_val.append(HJ_SO)

    rel_HJ_hand = ''.join([str(elem) for elem in HJ_hand_val])

    print("Hi Jacker: ", rel_HJ_hand)

    HJ_Rank = HJ_Hand_Rank
    print(Hero_Hand_Rank)
    HJ_Rank_card = ()

    if HJ_Rank[0] == 10:
        HJ_Rank_card = "High Card"
    if HJ_Rank[0] == 9:
        HJ_Rank_card = "Pair"
    if HJ_Rank[0] == 8:
        HJ_Rank_card = "Two Pair"
    if HJ_Rank[0] == 7:
        HJ_Rank_card = "Three of a Kind"
    if HJ_Rank[0] == 6:
        HJ_Rank_card = "Straight"
    if HJ_Rank[0] == 5:
        HJ_Rank_card = "Flush"
    if HJ_Rank[0] == 4:
        HJ_Rank_card = "Full House"
    if HJ_Rank[0] == 3:
        HJ_Rank_card = "Four of a Kind"
    if HJ_Rank[0] == 2:
        HJ_Rank_card = "Straight Flush"
    if HJ_Rank[0] == 1:
        HJ_Rank_card = "Royal Flush"

    print("HJ_Rank:" , HJ_Rank)

    #############################################################################################################################################

    x = 0

    y = 0
    if len(Hero_Rank) < len(Villain_Rank):
        x = 0
        while x < len(Hero_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x += 1

    if len(Hero_Rank) > len(Villain_Rank):
        x = 0
        while x < len(Villain_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x += 1

    if len(Hero_Rank) == len(Villain_Rank):
        x = 0
        while x < len(Hero_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x += 1

    print("WLT", Win_Lose_Tie)

    #def append_list_as_row(file_name, list_of_elem):
        # Open file in append mode
        #with open("PokerHandData.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            #csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            #csv_writer.writerow(list_of_elem)

    # if Win_Lose_Tie==0:

    # New_Row = [l, (Button_card1,Button_card2), (small_blind_card1,small_blind_card2), (rel_hero_hand), (rel_villain_hand), Flop_card1, Flop_card2, Flop_card3, Turn, River, Hero_Rank_card,
    #    Villain_Rank_card, Win_Lose_Tie]
    # append_list_as_row("PokerHandData.csv", New_Row)
    pokerhanddata = [Button_card1, Button_card2, small_blind_card1, small_blind_card2, big_blind_card1, big_blind_card2,
                     UTG_card1, UTG_card2, UTG2_card1, UTG2_card2, MP_card1, MP_card2, MP2_card1, MP2_card2, MP3_card1,
                     MP3_card2, HJ_card1, HJ_card2, Flop_card1, Flop_card2, Flop_card3, Turn, River, BB_Rank_card,
                     Villain_Rank_card, Hero_Rank_card, UTG_Rank_card, UTG2_Rank_card, MP_Rank_card, MP2_Rank_card,
                     MP3_Rank_card, HJ_Rank_card, Win_Lose_Tie]
    pokerhanddatastr = ','.join(map(str, pokerhanddata))
    Hero_Hand_Rank_str = ','.join(map(str, Hero_Hand_Rank))
    Pre_flopButton = [Button_card1, Button_card2]
    Button = ','.join(map(str, Pre_flopButton))
    Pre_flopSB = [small_blind_card1, small_blind_card2]
    SB = ','.join(map(str, Pre_flopSB))
    Pre_flopBB = [big_blind_card1, big_blind_card2]
    BB = ','.join(map(str, Pre_flopBB))
    Pre_flopUTG = [UTG_card1, UTG_card2]
    UTG = ','.join(map(str, Pre_flopUTG))
    Pre_flopUTG2 = [UTG2_card1, UTG2_card2]
    UTG2 = ','.join(map(str, Pre_flopUTG2))
    Pre_flopMP = [MP_card1, MP_card2]
    MP = ','.join(map(str, Pre_flopMP))
    Pre_flopMP2 = [MP2_card1, MP2_card2]
    MP2 = ','.join(map(str, Pre_flopMP2))
    Pre_flopMP3 = [MP3_card1, MP3_card2]
    MP3 = ','.join(map(str, Pre_flopMP3))
    Pre_flopHJ = [HJ_card1, HJ_card2]
    HJ = ','.join(map(str, Pre_flopHJ))
    Flop = [Flop_card1, Flop_card2, Flop_card3]
    Flop = ','.join(map(str, Flop))
    Turn = Turn[0:]
    River = River[0:]
    Hero_Cards = ','.join(map(str, [Button_card1, Button_card2]))
    Hero_Rank_card
    Villain_Cards = [small_blind_card1, small_blind_card2]
    Villain_Rank_card
    Flop_Cards = ','.join(map(str, [Flop_card1, Flop_card2, Flop_card3]))
    Turn_Card = Turn
    River_Card = River
    print(pokerhanddatastr)
    ##sock.sendall(pokerhanddatastr.encode("UTF-8"))

    print(rel_hero_hand)
    print(rel_villain_hand)

    # In[ ]:0
    # print(pokerhanddata)  # Vector3   x = 0, y = 0, z = 0
    #print(f"[NEW CONNECTION] {addr} connected.")
    #time.sleep(3600)


    #DaVinciEngine()

    Card1 = Button[0] + Button[1]
    print(Card1)
    Card2 = Button[3] + Button[4]
    round += 1

    startPos = [round, Card1, Card2]
    print(startPos)
    posString = ','.join(map(str, startPos))

    print(posString)
    sock.sendall(posString.encode("UTF-8"))
    receivedData = sock.recv(1024).decode(FORMAT)
    print(receivedData)
    time.sleep(0.5)
    del Hero_Rank_card
    del Villain_Rank_card









#DaVinciEngine()

    #conn2.send(SB.encode(FORMAT))
    #conn3.send(BB.encode(FORMAT))
    #conn4.send(UTG.encode(FORMAT))
    #conn5.send(UTG2.encode(FORMAT))
    #conn6.send(MP.encode(FORMAT))
    #conn7.send(MP2.encode(FORMAT))
    #conn8.send(MP3.encode(FORMAT))
    #conn9.send(HJ.encode(FORMAT))
    #conn10.send(Flop.encode(FORMAT))
    #conn11.send(Turn.encode(FORMAT))
    #conn12.send(River.encode(FORMAT))


    # print(f"[{addr}] {msg}")
#    reply = ""

    #connected = True
    #while connected:
     #   print('yerr')
      #  print(conn.sendall(str.encode(reply)))

       # try:
        #    data = conn.recv(HEADER)
            ##reply = data.decode(FORMAT)
         #   print('yerr')

          #  if not data:
           #     print("Disconnected")
            #    break
            #else:
             #   data = len(data)
              #  reply = conn.recv(2048).decode(FORMAT)

               # print("Received: ", reply)
               # print("Sending: ", reply)
                #DaVinciEngine(conn, addr, addr2)

              #  if msg == DISCONNECT_MESSAGE:
              #      connected = False
          #  print('yer1')

           # break


        #except:
       #     break
        #print("Lost connection")


# def start():
# server.listen()
# print(f"[LISTENING] Server is listening on {SERVER}")
# while True:


# start2()


# print("yooo", conn, addr, addr2)

# print("yertt")


# print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# print(thread.start())

##DaVinciEngine(conn, addr, addr2)

#def start():

    #server.listen()
    #print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")
    #server2.listen()
    #print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    #server3.listen()
    #server4.listen()
    #server5.listen()
    #server6.listen()
    #server7.listen()
    #server8.listen()
    #server9.listen()
#    print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")
    #server10.listen()
    #print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    #server11.listen()
    #print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    #server12.listen()
    #print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

### print(f'Client 2 Connected at {time.perf_counter()}...')

        #conn3, addr3 = server3.accept()
        #print(f'Client 3 Connected at {time.perf_counter()}...')

        #conn4, addr4 = server4.accept()
       # print(f'Client 4 Connected at {time.perf_counter()}...')

        #conn5, addr5 = server5.accept()
       # print(f'Client 5 Connected at {time.perf_counter()}...')

        #conn6, addr6 = server6.accept()
       # print(f'Client 6 Connected at {time.perf_counter()}...')

        #conn7, addr7 = server7.accept()
       # print(f'Client 7 Connected at {time.perf_counter()}...')

        #conn8, addr8 = server8.accept()
      #  print(f'Client 8 Connected at {time.perf_counter()}...')

        #conn9, addr9 = server9.accept()
       # print(f'Client 9 Connected at {time.perf_counter()}...')
        #conn10, addr10 = server10.accept()
       # print(f'Client 10 Connected at {time.perf_counter()}...')
        #conn11, addr11 = server11.accept()
       # print(f'Client 11 Connected at {time.perf_counter()}...')
        #conn12, addr12 = server12.accept()
       # print(f'Client 12 Connected at {time.perf_counter()}...')

        #thread = threading.Thread(target=DaVinciEngine(conn, conn2, conn3, conn10, conn11, conn12, addr, addr2, addr3, addr10, addr11, addr12), args=(conn, conn2, conn3, addr, addr2, addr3))
        #thread.start()


    # server4.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    # server5.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    # server6.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    # server7.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    # server8.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

    # server9.listen()
    # print(f"[LISTENING] Server is listening on {SERVER} at {time.perf_counter()}")

   #hile True:




        # conn4, addr4 = server4.accept()
        # print(f'Client 4 Connected at {time.perf_counter()}...')
        # conn5, addr5 = server5.accept()
        # print(f'Client 5 Connected at {time.perf_counter()}...')
        # conn6, addr6 = server6.accept()
        # print(f'Client 6 Connected at {time.perf_counter()}...')
        # conn7, addr7 = server7.accept()
        # print(f'Client 7 Connected at {time.perf_counter()}...')
        # conn8, addr8 = server8.accept()
        # print(f'Client 8 Connected at {time.perf_counter()}...')
        # conn9, addr9 = server9.accept()
        # print(f'Client 9 Connected at {time.perf_counter()}...')

      #  print("yooo", conn, addr, addr2)

      #  print("yertt")
       # thread = threading.Thread(target=DaVinciEngine(conn10, conn11, conn12, conn, conn2, conn3, addr10, addr11, addr12, addr, addr2, addr3), args=(conn, addr, addr2))
       # print('yoyo')
       # thread2 = threading.Thread(target=DaVinciEngine(conn2, addr, addr2), args=(conn2, addr, addr2))

       # print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

       # print(thread2.start())
        #thread.start()
        ##DaVinciEngine(conn, addr, addr2)

    # print(l)

#DaVinciEngine()

# l+=1


# In[ ]:
