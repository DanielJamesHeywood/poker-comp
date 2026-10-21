from poker.action import Action
from poker.card import Rank
from poker.game_state import GameState


# real_play_statistics mixed with raise_by_big_blind_unless_raised.
#
# The top three of the nine tiers of starting hands from statistics based on real play (PokerRoom.com's), as Wikipedia's
# "Texas hold 'em starting hands" lists them. A hand ending in "s" has both cards of the same suit, and one without it has
# two different suits.
GOOD_HANDS = {
    "AA", "KK", "QQ", "JJ", "AKs",
    "AQs", "TT", "AK", "AJs", "KQs", "99",
    "ATs", "AQ", "KJs", "88", "KTs", "QJs",
}
LETTERS = dict(zip(Rank, "23456789TJQKA"))  # Rank lists the ranks from lowest to highest


def hand(state: GameState) -> str:
    # Our two cards written like the tiers, such as "AKs", "AK" or "QQ"
    high, low = sorted(state.my_player.hole_cards, key=lambda card: list(Rank).index(card.rank), reverse=True)
    suited = high.suit is low.suit and high.rank is not low.rank
    return LETTERS[high.rank] + LETTERS[low.rank] + ("s" if suited else "")


def myAI(state: GameState) -> Action:
    me = state.my_player

    # Go all in with a good hand, or with any hand when we have fewer than 10 big blinds, as waiting lets the blinds eat our chips
    if hand(state) in GOOD_HANDS or (me.chips_in_stack + me.chips_bet) / state.big_blind < 10:
        return Action.raise_by(10 ** 9)

    # Otherwise raise by the big blind whenever nobody has bet more than the big blind, and fold to anything bigger
    biggest_bet = max(player.chips_bet for player in state.players)
    to_call = biggest_bet - me.chips_bet

    if biggest_bet > state.big_blind:
        return Action.check() if to_call == 0 else Action.fold()

    return Action.raise_by(state.big_blind)
