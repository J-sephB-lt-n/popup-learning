
import random 

from src.popups import PopupMessage, show_popup_messages
from src.question_sets.english_phrases_to_xhosa import english_phrases_to_xhosa 
from src.question_sets.xhosa_phrases_to_english import xhosa_phrases_to_english

if __name__ == "__main__":
    all_messages: tuple[tuple[PopupMessage, PopupMessage]] = english_phrases_to_xhosa + xhosa_phrases_to_english
    chosen_message_pair: tuple[PopupMessage, PopupMessage] = random.choice(all_messages)
    show_popup_messages(chosen_message_pair)


