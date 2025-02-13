from .termination_condition_base import BaseTerminationCondition
from ..core.catalog import Catalog as c
from colorama import Fore

class ExtremeState(BaseTerminationCondition):
    """
    ExtremeState
    End up the simulation if the aircraft is on an extreme state.
    """

    def __init__(self, config):
        super().__init__(config)

    def get_termination(self, task, env, agent_id, info={}):
        """
        Return whether the episode should terminate.
        End up the simulation if the aircraft is on an extreme state.

        Args:
            task: task instance
            env: environment instance

        Returns:
            (tuple): (done, success, info)
        """
        success = True
        done = bool(env.agents[agent_id].get_property_value(c.detect_extreme_state))
        if done:
            env.agents[agent_id].crash()
            self.log(f'{agent_id} is on an extreme state! Total Steps={env.current_step}')
            info['done_condition'] = Fore.LIGHTRED_EX + f'{agent_id} is on an extreme state! Total Steps={env.current_step}'
            success = False
        return done, success, info
