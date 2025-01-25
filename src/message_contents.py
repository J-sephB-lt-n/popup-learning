from src.question_sets.xhosa_phrases_to_english import (
    english_phrases_to_xhosa,
    xhosa_phrases_to_english,
)

messages: tuple[tuple[PopupMessage, ...]] = (
    english_phrases_to_xhosa + xhosa_phrases_to_english
)
