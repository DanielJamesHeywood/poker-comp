from poker.action import Action
from poker.game_state import GameState


def myAI(state: GameState) -> Action:
    if max(player.chips_bet for player in state.players) - state.my_player.chips_bet < state.my_player.chips_in_stack // 2:
        return Action.raise_by(1)
    else:
        return Action.fold()


def defaultAI(state: GameState) -> Action: # This ai runs if myAI raises an exception, returns an invalid action or takes too long
    return Action.check() if state.my_player.chips_bet == max(player.chips_bet for player in state.players) else Action.fold()
