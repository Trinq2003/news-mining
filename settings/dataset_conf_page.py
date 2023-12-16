import os

from .configuration_page import PageConfiguration


class PageDatasetConfiguration(PageConfiguration):

    def _calculate_step(self, step):
        step = int(step)
        return step
            
    def _init_properties(self):
        return [
            ['name', '', str],
            ['base_api_url', '', str],
            ['start_page', 1, int],
            ['end_page', 30, int],
            ['step', 1, self._calculate_step],
            ['path', '', str],
            ['sleep', 0.2, float],
        ]
