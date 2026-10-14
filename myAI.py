from poker.action import Action
from poker.card import Rank
from poker.game_state import GameState


def myAI(state: GameState) -> Action:
    card, other_card = state.my_player.hole_cards
    if card.rank == Rank.ACE and other_card.rank == Rank.ACE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.KING and other_card.rank == Rank.KING:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.QUEEN and other_card.rank == Rank.QUEEN:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.JACK and other_card.rank == Rank.JACK:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.TEN and other_card.rank == Rank.TEN:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.ACE and other_card.rank == Rank.KING or card.rank == Rank.KING and other_card.rank == Rank.ACE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.NINE and other_card.rank == Rank.NINE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.ACE and other_card.rank == Rank.TEN or card.rank == Rank.TEN and other_card.rank == Rank.ACE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.KING and other_card.rank == Rank.JACK or card.rank == Rank.JACK and other_card.rank == Rank.KING:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.QUEEN and other_card.rank == Rank.JACK or card.rank == Rank.JACK and other_card.rank == Rank.QUEEN:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.JACK and other_card.rank == Rank.TEN or card.rank == Rank.TEN and other_card.rank == Rank.JACK:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.ACE and other_card.rank == Rank.QUEEN or card.rank == Rank.QUEEN and other_card.rank == Rank.ACE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.EIGHT and other_card.rank == Rank.EIGHT:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.KING and other_card.rank == Rank.TEN or card.rank == Rank.TEN and other_card.rank == Rank.KING:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.QUEEN and other_card.rank == Rank.TEN or card.rank == Rank.TEN and other_card.rank == Rank.QUEEN:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.JACK and other_card.rank == Rank.NINE or card.rank == Rank.NINE and other_card.rank == Rank.JACK:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.TEN and other_card.rank == Rank.NINE or card.rank == Rank.NINE and other_card.rank == Rank.TEN:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.suit == other_card.suit and card.rank == Rank.NINE and other_card.rank == Rank.EIGHT or card.rank == Rank.EIGHT and other_card.rank == Rank.NINE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.ACE and other_card.rank == Rank.JACK or card.rank == Rank.JACK and other_card.rank == Rank.ACE:
        return Action.raise_by(state.my_player.chips_in_stack)
    if card.rank == Rank.KING and other_card.rank == Rank.QUEEN or card.rank == Rank.QUEEN and other_card.rank == Rank.KING:
        return Action.raise_by(state.my_player.chips_in_stack)
    return defaultAI(state)


def defaultAI(state: GameState) -> Action: # This ai runs if myAI raises an exception, returns an invalid action or takes too long
    return Action.check() if state.my_player.chips_bet == max(player.chips_bet for player in state.players) else Action.fold()
